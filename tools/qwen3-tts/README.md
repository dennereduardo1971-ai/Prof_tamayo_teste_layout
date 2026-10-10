---
name: qwen3-tts
description: "Família de TTS aberto da Qwen (0.6B/1.7B): clone com 3 s de referência, vozes prontas e voz desenhada por descrição; 10 línguas com português."
tema: audio
tipo: cli
tags: [audio, cli]
status: catalogado
alternativas: [chatterbox-tts, f5-tts, omnivoice]
combina-com: [ultimate-vocal-remover]
---

# qwen3-tts

Família de TTS aberto da Qwen (0.6B/1.7B): clone com 3 s de referência, vozes prontas e voz desenhada por descrição; 10 línguas com português.

- **Tipo:** cli
- **Fonte:** https://github.com/QwenLM/Qwen3-TTS

## Uso

- Apache 2.0, 13,7 mil estrelas, lançado em 22/01/2026.
- Modelos: `0.6B-Base` / `1.7B-Base` (clonagem), `CustomVoice` (9 vozes com controle de estilo), `1.7B-VoiceDesign` (cria voz a partir de descrição).
- CPU: relato de terceiros com 0.6B int8 deu ~3 s de processamento por segundo de áudio (https://dev.ocdevel.com/blog/20260711-quantized-cpu-tts). Porte GGUF para CPU: https://huggingface.co/CC-TM/Qwen3-TTS-GGUF
- Relato de usuário: o CustomVoice "deriva" em trechos longos; fixar a semente ajuda (https://archy.net/from-qwen3-tts-to-chatterbox-finally-getting-voice-cloning-right/).
- O 1.7B pesa para PCs com 8 GB de RAM.

## Status

Catalogado, ainda não instalado/testado.
