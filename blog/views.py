from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from .forms import ContatoForm
from .models import Postagem


def home(request):

    post = Postagem.objects.all().order_by('-criado')
    paginacao = Paginator(post, 3)
    page = request.GET.get('page')
    conteudo = paginacao.get_page(page)

    context = {
        'post': conteudo
    }

    return render(request, 'home.html', context)


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


def postagem(request, id):
    post1 = get_object_or_404(Postagem, pk=id)

    context = {
        'post': post1
    }

    return render(request, 'post.html', context)
