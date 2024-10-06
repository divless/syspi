from django.db import models


class Cliente(models.Model):
    name = models.CharField("Nome",max_length=250)
    birth = models.DateField("Data de nascimento",blank=True)
    addr = models.TextField("Endereço")
    email = models.EmailField("E-mail")
    picture = models.ImageField(upload_to="uploads/pic/")
    added = models.DateTimeField("Adicionado",auto_now=True)
    active = models.BooleanField("Ativo",default=True)

    def __str__(self) -> str:
        return self.name


class Ficha(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    title = models.CharField("Título",max_length=200)
    desc = models.TextField("Observações")
    file = models.FileField(upload_to="uploads/fichas/")
    added = models.DateTimeField("Adicionado",auto_now=True)

    def __str__(self) -> str:
        return self.title


class Plano(models.Model):
    name = models.CharField("Nome",max_length=250)
    price = models.DecimalField("Valor",max_digits=8,decimal_places=2)
    desc = models.TextField("Descrição")
    active = models.BooleanField("Ativo",default=True)
    added = models.DateTimeField("Adicionado",auto_now=True)


class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    start = models.DateField("Início")
    end = models.DateField("Fim")
    file = models.FileField(upload_to="uploads/contracts/")
    active = models.BooleanField("Ativo",default=True)
    added = models.DateTimeField("Adicionado",auto_now=True)