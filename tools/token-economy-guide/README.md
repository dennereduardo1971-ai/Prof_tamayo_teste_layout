---
name: token-economy-guide
description: Boas práticas para gastar menos tokens no Claude Code.
tags: [economia-de-token, guia]
---

# token-economy-guide

- Desconecte MCPs que não usa: cada servidor carrega seu schema inteiro (pode custar 50-70 mil tokens por sessão).
- Rode `/compact` com 60-70% do contexto, com âncoras explícitas.
- Roteie tarefas simples para Haiku.
- Mantenha o prefixo do prompt (system, skills, manifesto MCP) estável para aproveitar o cache de 5 minutos.
- Combine RTK (saída de CLI) com context-mode (saída de MCP).

## Fontes

- https://computingforgeeks.com/reduce-claude-code-token-usage-tools/
- https://www.firecrawl.dev/blog/claude-code-token-efficiency
- https://buildtolaunch.substack.com/p/claude-code-token-optimization
- https://milvus.io/blog/claude-code-context-management-tools.md
- https://dev.to/kmusicman/9-verified-tools-to-stop-burning-claude-tokens-unnecessarily-f9e
