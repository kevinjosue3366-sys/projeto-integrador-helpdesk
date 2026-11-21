from django.db import models


class Usuario(models.Model):
    PERFIS = [
        ("Cliente", "Cliente"),
        ("Tecnico", "Técnico"),
        ("Administrador", "Administrador"),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    tipo_perfil = models.CharField(max_length=20, choices=PERFIS, default="Cliente")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.tipo_perfil})"


class Chamado(models.Model):
    PRIORIDADES = [
        ("Baixa", "Baixa"),
        ("Média", "Média"),
        ("Alta", "Alta"),
        ("Urgente", "Urgente"),
    ]
    STATUS = [
        ("Aberto", "Aberto"),
        ("Em Andamento", "Em Andamento"),
        ("Concluído", "Concluído"),
        ("Cancelado", "Cancelado"),
    ]

    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    prioridade = models.CharField(max_length=20, choices=PRIORIDADES, default="Média")
    status = models.CharField(max_length=30, choices=STATUS, default="Aberto")
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="chamados")

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="comentarios")

    def __str__(self):
        return f"Comentário #{self.id} - {self.chamado.titulo}"
