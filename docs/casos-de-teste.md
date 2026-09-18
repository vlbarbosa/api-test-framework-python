# Matriz de Casos de Teste — API JSONPlaceholder

| ID   | Endpoint          | Cenário                                  | Resultado Esperado           | Prioridade |
|------|-------------------|-------------------------------------------|-------------------------------|------------|
| CT01 | GET /posts/1      | Buscar post existente                     | Status 200, campo "id" = 1   | Alta       |
| CT02 | GET /posts        | Listar todos os posts                     | Status 200, lista não vazia  | Alta       |
| CT03 | GET /posts/9999   | Buscar post inexistente                   | Status 404                   | Alta       |
| CT04 | POST /posts       | Criar post com dados válidos              | Status 201, retorna o post   | Alta       |
| CT05 | POST /posts       | Criar post sem o campo "title"            | Documentar comportamento real| Média      |
| CT06 | GET /posts/1/comments | Buscar comentários de um post          | Status 200, lista não vazia  | Média      |