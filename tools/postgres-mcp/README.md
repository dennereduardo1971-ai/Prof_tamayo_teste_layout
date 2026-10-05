---
name: postgres-mcp
description: "Escreve e executa SQL em qualquer Postgres (Supabase, Neon, Railway) a partir de perguntas em linguagem natural."
tema: dev
tipo: mcp
tags: [dev, mcp]
status: catalogado
alternativas: [bigquery-mcp, supabase-mcp]
combina-com: []
---

# postgres-mcp

Escreve e executa SQL em qualquer Postgres (Supabase, Neon, Railway) a partir de perguntas em linguagem natural.

- **Tipo:** mcp
- **Fonte:** https://www.vibestack.in/blog/mcp-servers-data-analysis-2026

## Uso

Não use o servidor de referência (`@modelcontextprotocol/server-postgres`): SQL injection sem correção. Use `@zeddotdev/postgres-context-server` ≥ 0.1.4 com usuário só-leitura. Ver RESULTADOS_SEGURANCA.md.

## Status

Catalogado, ainda não instalado/testado.
