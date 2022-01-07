from django import forms

#Classe que cria um formulario de contato.
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=255)
    email = forms.EmailField(label='Email' ,max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=255)
    mensagem = forms.CharField(label='Mensagem', widget= forms.Textarea())