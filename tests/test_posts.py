import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_buscar_comentarios_de_varios_posts(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")

    assert response.status_code == 200
    comentarios = response.json()
    assert isinstance(comentarios, list)
    assert len(comentarios) > 0

def test_buscar_post_existente_retorna_sucesso():
    # Arrange: Definimos o ID que vamos buscar
    post_id = 1

    # Act: chamamos a API para buscar o post
    response = requests.get(f"{BASE_URL}/posts/{post_id}")

    # Assert: Vamos verificar se o resultado e o que esperamos
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == post_id
    assert "title" in body
    assert "body" in body

def test_listar_todos_posts_retorna_lista_nao_vazia():
    
    # Arrange: Nenhum dado específico é necessário para este teste

    # Act: chamamos a API para listar todos os posts
    response = requests.get(f"{BASE_URL}/posts")

    # Assert: Verificamos se o resultado é uma lista e se não está vazia
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0  # Esperamos que a lista NÃO esteja vazia

def test_buscar_post_inexistente_retorna_404():
    post_id = 9999

    response = requests.get(f"{BASE_URL}/posts/{post_id}")

    assert response.status_code == 404

def test_criar_post_com_dados_validos():
    payload = {
        "title": "Meu post de teste",
        "body": "Conteúdo do post de teste",
        "userId": 1,
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert "id" in body

def test_criar_post_sem_titulo_e_aceito_pela_api_fake():
    payload = {
        "body": "Post sem título",
        "userId": 1,
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    # A JSONPlaceholder é uma API "fake" — ela não valida campos obrigatórios,
    # então documentamos o comportamento real observado, em vez de assumir
    # o comportamento ideal de uma API de produção.
    assert response.status_code == 201

