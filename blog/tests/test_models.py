from model_mommy import mommy
from django.test import TestCase
from blog.models import Postagem


class PostagemTestCase(TestCase):

    def setUp(self):
        self.postagem = mommy.make('Postagem')

    def test_str(self):
        self.assertEquals(str(self.postagem), self.postagem.titulo)
