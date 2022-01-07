from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def posts(request):
    return render(request, 'postagens.html')


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            print(f'POST:{request.POST}')
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            msg = form.cleaned_data['msg']

            print("Mensagem enviada")
            print(f'{nome}')
            print(f'{email}')
            print(f'{assunto}')
            print(f'{msg}')

            messages.success(request, "Mensagem enviada.")
            form = ContatoForm()
    else:
            messages.error(request, 'Houve um erro.')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)
