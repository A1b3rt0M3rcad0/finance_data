# API Documentation - Stock Endpoint

## POST `/stock`

Consulta dados históricos de ações com base no símbolo fornecido.

### Request

**Method:**\
`POST`

**Content-Type:**\
`application/json`

### Body Parameters

| Campo      | Tipo   | Obrigatório | Descrição                                             |
| ---------- | ------ | ----------- | ----------------------------------------------------- |
| `symbol`   | string | Sim         | Código da ação (ex: "AAPL", "GOOG").                  |
| `interval` | string | Sim         | Intervalo entre os dados (ex: "1m", "5m", "1d").      |
| `period`   | string | Sim         | Período total de dados (ex: "1d", "5d", "1mo", "1y"). |

**Exemplo de Requisição:**

```json
{
  "symbol": "AAPL",
  "interval": "1m",
  "period": "1d"
}
```

---

### Response

**Content-Type:**\
`application/json`

**Formato:**

```json
{
  "Close": { "timestamp1": value1, "timestamp2": value2, ... },
  "Dividends": { "timestamp1": value1, "timestamp2": value2, ... },
  "High": { "timestamp1": value1, "timestamp2": value2, ... },
  "Low": { "timestamp1": value1, "timestamp2": value2, ... },
  "Open": { "timestamp1": value1, "timestamp2": value2, ... },
  "Stock Splits": { "timestamp1": value1, "timestamp2": value2, ... },
  "Volume": { "timestamp1": value1, "timestamp2": value2, ... }
}
```

**Campos:**

| Campo          | Tipo   | Descrição                                        |
| -------------- | ------ | ------------------------------------------------ |
| `Close`        | objeto | Preços de fechamento por timestamp.              |
| `Dividends`    | objeto | Dividendos pagos por timestamp.                  |
| `High`         | objeto | Preço mais alto por timestamp.                   |
| `Low`          | objeto | Preço mais baixo por timestamp.                  |
| `Open`         | objeto | Preço de abertura por timestamp.                 |
| `Stock Splits` | objeto | Eventos de desdobramento de ações por timestamp. |
| `Time`         | array  | Lista de timestamps dos dados.                   |
| `Volume`       | objeto | Volume negociado por timestamp.                  |

**Exemplo de Resposta:**

```json
{
  "Close": {
    "1682592000": 165.02,
    "1682592060": 165.05
  },
  "Dividends": {
    "1682592000": 0
  },
  "High": {
    "1682592000": 165.10,
    "1682592060": 165.12
  },
  "Low": {
    "1682592000": 164.98,
    "1682592060": 165.00
  },
  "Open": {
    "1682592000": 165.00,
    "1682592060": 165.01
  },
  "Stock Splits": {
    "1682592000": 0
  },
  "Time": [
    1682592000,
    1682592060
  ],
  "Volume": {
    "1682592000": 1200,
    "1682592060": 800
  }
}
```

---

### Status Codes

| Código | Significado                           |
| ------ | ------------------------------------- |
| 200    | Dados retornados com sucesso.         |
| 500    | Erro interno do servidor.             |