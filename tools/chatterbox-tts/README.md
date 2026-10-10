---
name: chatterbox-tts
description: "TTS aberto (Resemble AI) que clona voz com um trecho curto de referência; Multilingual V3 fala 23 línguas, inclusive português."
tema: audio
tipo: cli
tags: [audio, cli]
status: catalogado
alternativas: [qwen3-tts, f5-tts, fish-audio, fish-speech, omnivoice]
combina-com: [ultimate-vocal-remover, yt-dlp, applio]
---

# chatterbox-tts

TTS aberto (Resemble AI) que clona voz com um trecho curto de referência; Multilingual V3 fala 23 línguas, inclusive português.

- **Tipo:** cli
- **Fonte:** https://github.com/resemble-ai/chatterbox

## Uso

- MIT, 26,8 mil estrelas, push em 21/07/2026. Modelo de 0,5B; aceita `device="cpu"` (lento, sem número oficial).
- Clonagem: referência de 10 a 20 s limpa, **no mesmo idioma** do texto (senão o sotaque vaza); `cfg_weight=0` reduz a transferência de sotaque.
- Bom para gerar falas fixas em lote (jogos, narração) e deixar rodando de madrugada numa CPU sem GPU.
- Demo: https://huggingface.co/spaces/ResembleAI/Chatterbox-Multilingual-TTS

## Status

Catalogado, ainda não instalado/testado.
