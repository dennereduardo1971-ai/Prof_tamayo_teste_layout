---
name: libigl-python
description: "Biblioteca de geometria (ARAP, Laplaciano, biarmônica) em Python; deforma malha 3D presa por âncoras pra bater com um desenho."
tema: jogos
tipo: outro
tags: [jogos, outro, blender, 3d, malha]
status: catalogado
alternativas: [blender-laplacian-deform]
combina-com: [blender-cryptomatte-diagnostico, blender-mcp]
---

# libigl-python

Deformação de malha que preserva detalhe (ARAP, Laplaciano, biarmônica com alças), rodando fora do Blender.

- **Tipo:** outro (biblioteca Python)
- **Fonte:** https://github.com/libigl/libigl-python-bindings
- **Instalação:** `pip install libigl` (wheel 2.6.3 abi3 win_amd64, serve no Python 3.12+; sem GPU)
- **Licença:** GPL-3.0 (uso em casa ok; não levar pra produto)

## Uso

Receita do Nealen 2005 / SilSketch: a borda do render vai pro contorno do desenho, o miolo (olhos, boca) fica preso,
o ARAP acomoda o resto. Base: tutorial `401_BiharmonicDeformation`. Busca de origem:
`_buscas/2026-10-27_correcoes-frente-noah` (Sense Life).

## Status

Catalogado, ainda não instalado/testado.
