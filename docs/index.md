# Documentação - Data Quality

Para desenvolver o modelo, vamos montar a seguinte ETL
```mermaid
graph TD;
    A[Configura Variáveis] --> B[Ler o Banco SQL];
    B --> V[Validação do Schema de Entrada];
    V -->|Falha| X[Alerta de Erro];
    V -->|Sucesso| C[Transformar os KPIs];
    C --> Y[Validação do Schema de Saída];
    Y -->|Falha| Z[Alerta de Erro];
    Y -->|Sucesso| D[Salvar no DuckDB];
```

## Contrato de dados

::: app.schema.ProdutoSchema

## Transformação

::: app.etl.extrair_do_sql

::: app.etl.load_settings

::: app.etl.transformar

::: app.etl.load_to_duckdb