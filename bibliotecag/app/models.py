from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Cidades"

    def __str__(self):
        return self.nome

        
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Usuarios"

    def __str__(self):
            return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Generos"

    def __str__(self):
        return self.nome
        

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Editoras"

    def __str__(self):
        return self.nome
        

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome
        

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    Genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autor =models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    preco = models.IntegerField()
    datapublicacao = models.DateField()

    class Meta:
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.nome



class Emprestimo(models.Model):
    leitor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    dataemprestimo = models.DateField()
    datadevolucao =models.DateField()

    class Meta:
        verbose_name_plural = "Emprestimos"

    def __str__(self):
        return self.livro
        