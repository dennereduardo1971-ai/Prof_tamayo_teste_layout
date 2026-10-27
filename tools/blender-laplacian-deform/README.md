---
name: blender-laplacian-deform
description: "Modificador nativo do Blender que deforma a malha preservando detalhe a partir de âncoras; ajustar silhueta sem amassar."
tema: jogos
tipo: guia
tags: [jogos, guia, blender, 3d, malha]
status: catalogado
alternativas: [libigl-python]
combina-com: [blender-cryptomatte-diagnostico, blender-mcp]
---

# blender-laplacian-deform

Modificador Laplacian Deform (embutido no Blender): grupo de vértices de âncora + `bpy.ops.object.laplaciandeform_bind`.

- **Tipo:** guia (recurso nativo)
- **Fonte:** https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/laplacian_deform.html

## Uso

Âncoras = vértices da borda já levados pro alvo + miolo e nuca parados; o resto acompanha sem dobra. Alternativa sem
instalar nada ao `libigl-python`. Busca de origem: `_buscas/2026-10-27_correcoes-frente-noah`.

## Status

Catalogado, ainda não instalado/testado.
