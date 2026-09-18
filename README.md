# API Test Framework — Python + Pytest

Framework de testes automatizados de API, construído para demonstrar a
transição de testes manuais (Postman) para testes de API versionáveis e
automatizados em Python.

## Motivação

Como Analista de QA com experiência em validação de regras de negócio e
Quality Gate, este projeto aplica os mesmos princípios de matriz de
rastreabilidade e cobertura de cenários (positivos, negativos e de borda)
em um contexto de automação de testes.

## API testada

[JSONPlaceholder](https://jsonplaceholder.typicode.com) — API pública
gratuita para prática de testes.

## Tecnologias

- Python 3.10+
- Pytest
- Requests
- pytest-html

## Como rodar

\`\`\`bash
python -m venv venv
source venv/bin/activate   # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
pytest -v
\`\`\`

## Gerar relatório

\`\`\`bash
pytest --html=docs/report.html --self-contained-html
\`\`\`

## Matriz de casos de teste

Ver [docs/casos-de-teste.md](docs/casos-de-teste.md)