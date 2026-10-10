---
name: applio
description: "Interface de RVC: converte uma fala gravada no timbre de outra voz, treina modelos e junta TTS+RVC; converte na CPU."
tema: audio
tipo: outro
tags: [audio, outro]
status: catalogado
alternativas: [rvc-webui, tts-webui]
combina-com: [ultimate-vocal-remover, voice-models-com, chatterbox-tts, kokoro-tts, piper-tts]
---

# applio

Interface de RVC: converte uma fala gravada no timbre de outra voz, treina modelos e junta TTS+RVC; converte na CPU.

- **Tipo:** outro
- **Fonte:** https://github.com/IAHispano/Applio

## Uso

- MIT, 3,8 mil estrelas, release 3.6.5 (19/09/2026). Windows: `run-install.bat` e `run-applio.bat`.
- Conversão roda na CPU (lenta, serve para falas curtas). Treino precisa de GPU: usar Colab ou Kaggle.
- O RVC só troca o timbre: atuação, sotaque e palavras vêm da voz de entrada (gravação própria ou TTS). Um modelo treinado em japonês "fala" português com aquele timbre.
- Modelos `.pth` + `.index`: ver voice-models-com. HuBERT em português para treino: https://huggingface.co/Politrees/RVC_resources

## Status

Catalogado, ainda não instalado/testado.
