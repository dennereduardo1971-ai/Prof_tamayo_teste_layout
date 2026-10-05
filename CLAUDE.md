# Acervo de ferramentas

Este repositório é a fonte principal para achar ferramentas (MCPs, skills, plugins) para o Claude.

## Como buscar

1. Leia `INDEX.md` primeiro: está dividido por tema, com uma recomendação ("Comece por") em cada seção.
2. Para filtrar, use grep nos frontmatters de `tools/*/README.md`:
   - por tema: `grep -l '^tema: godot' tools/*/README.md`
   - por tipo: `grep -l '^tipo: mcp' tools/*/README.md`
   - só testadas: `grep -l '^status: testado' tools/*/README.md`
3. Use `alternativas` (mesma função) e `combina-com` (uso conjunto) para sugerir opções e combinações.

## Vocabulário fixo

- `tema`: pesquisa, tokens, design, jogos, godot, aprendizado, midia
- `tipo`: mcp, skill, plugin, editor, cli, lista, guia, outro
- `status`: catalogado, testado

## Ao adicionar uma ferramenta

1. Copie `tools/_template` para `tools/<nome>` (kebab-case) e preencha o frontmatter.
2. Atualize `alternativas` e `combina-com` nos dois lados da relação.
3. Rode `python3 scripts/build_index.py` para regenerar o `INDEX.md` (tema novo: adicione-o em `SECOES` no script).
4. Ao instalar e validar uma ferramenta, mude `status` para `testado` e regenere o índice.
