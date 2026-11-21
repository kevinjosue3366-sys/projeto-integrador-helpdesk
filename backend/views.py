Python
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Chamado, Usuario

PRIORIDADES_VALIDAS = {"Baixa", "Média", "Alta", "Urgente"}
STATUS_VALIDOS = {"Aberto", "Em Andamento", "Concluído", "Cancelado"}


@require_http_methods(["GET"])
def listar_chamados(request):
    """Consulta os chamados persistidos e retorna a listagem ao utilizador."""
    chamados = Chamado.objects.select_related("usuario").order_by("-data_criacao")
    dados = [
        {
            "id": c.id,
            "titulo": c.titulo,
            "descricao": c.descricao,
            "prioridade": c.prioridade,
            "status": c.status,
            "solicitante": c.usuario.nome,
            "data_criacao": c.data_criacao.isoformat(),
        }
        for c in chamados
    ]
    return JsonResponse({"total": len(dados), "chamados": dados}, status=200)


@csrf_exempt
@require_http_methods(["POST"])
def criar_chamado(request):
    """Recebe requisição, valida os dados, persiste o chamado e retorna confirmação."""
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"erro": "Payload JSON inválido."}, status=400)

    titulo = (payload.get("titulo") or "").strip()
    descricao = (payload.get("descricao") or "").strip()
    prioridade = (payload.get("prioridade") or "Média").strip()
    usuario_id = payload.get("usuario_id")

    if not titulo or not descricao or not usuario_id:
        return JsonResponse(
            {"erro": "Campos obrigatórios: titulo, descricao e usuario_id."},
            status=400,
        )

    if prioridade not in PRIORIDADES_VALIDAS:
        return JsonResponse(
            {"erro": "Prioridade inválida. Use: Baixa, Média, Alta ou Urgente."},
            status=400,
        )

    try:
        usuario = Usuario.objects.get(pk=usuario_id)
    except Usuario.DoesNotExist:
        return JsonResponse({"erro": "Utilizador informado não encontrado."}, status=404)

    chamado = Chamado.objects.create(
        titulo=titulo,
        descricao=descricao,
        prioridade=prioridade,
        status="Aberto",
        usuario=usuario,
    )

    return JsonResponse(
        {
            "mensagem": "Chamado criado com sucesso.",
            "chamado": {
                "id": chamado.id,
                "titulo": chamado.titulo,
                "prioridade": chamado.prioridade,
                "status": chamado.status,
                "usuario_id": usuario.id,
            },
        },
        status=201,
    )
