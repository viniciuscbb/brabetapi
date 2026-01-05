# Brabet API Wrapper

Esta é uma interface simples em Python para interagir com a API da Brabet. O wrapper lida automaticamente com a autenticação de visitante e fornece métodos fáceis para obter dados de histórico de jogos.

## 📋 Pré-requisitos

O projeto requer a biblioteca `requests`.

```bash
pip install requests
```

## 🚀 Como Usar

### Inicialização

A classe `BrabetAPI` gerencia a sessão e obtém automaticamente um token de visitante ao ser instanciada.

```python
from brabetapi.api import BrabetAPI

# Inicializa a API e autentica automaticamente
api = BrabetAPI()
```

### 🎲 Métodos Disponíveis

#### Obter Histórico do Double

Recupera o histórico de resultados do jogo Double.

```python
def get_double_history(limit: int = 12, result_type: int = 3)
```

**Parâmetros:**
- `limit` (int, opcional): Número de resultados a retornar. Padrão: 12.
- `result_type` (int, opcional): Tipo de filtro de resultado. Padrão: 3. Use 5 para resultados mais detalhados.

**Exemplo:**
```python
history = api.get_double_history(limit=15)
print(history)
# Saída: ['8', '1', '10', ...]
```

#### Formatar Histórico do Double

Converte o histórico bruto de números em objetos detalhados com cor.

```python
def format_double_history(history: list)
```

**Parâmetros:**
- `history` (list): Lista de resultados retornada por `get_double_history`.

**Exemplo:**
```python
formatted = api.format_double_history(history)
print(formatted)
# Saída: [{'roll': 8, 'color': 'black'}, {'roll': 1, 'color': 'red'}, ...]
```

#### Obter Histórico do Crash

Recupera o histórico de resultados do jogo Crash.

```python
def get_crash_history()
```

**Exemplo:**
```python
crash_data = api.get_crash_history()
print(crash_data)
```

## 📂 Estrutura do Projeto

- `brabetapi/`: Pacote principal.
  - `api.py`: Contém a classe principal `BrabetAPI`.
  - `headers.py`: Configurações de cabeçalhos HTTP.
- `exemple.py`: Exemplo de uso da biblioteca.
