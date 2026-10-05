# Ferramentas

Acervo privado de ferramentas. Fonte principal de busca: consulte o [INDEX.md](INDEX.md) primeiro.

## Estrutura

```
tools/<nome-da-ferramenta>/
  README.md   # frontmatter + uso
  ...         # código da ferramenta (autocontido)
tools/_template/   # modelo para novas ferramentas
INDEX.md           # índice central (nome, descrição, tags)
```

## Adicionar ferramenta

1. Copie `tools/_template` para `tools/<nome>` (kebab-case).
2. Preencha o frontmatter do `README.md`.
3. Adicione uma linha no `INDEX.md`.
