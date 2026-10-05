# Índice de ferramentas

Busque aqui primeiro. Detalhes, `alternativas` e `combina-com` ficam no frontmatter de cada `tools/<nome>/README.md`.
Gerado por `scripts/build_index.py`; não edite à mão.

Seções: [Pesquisa](#pesquisa) · [Economia de tokens](#economia-de-tokens) · [Design](#design) · [Jogos](#jogos) · [Godot](#godot) · [Aprendizado](#aprendizado) · [Imagem e vídeo](#imagem-e-vídeo) · [Marketing](#marketing) · [Redes sociais](#redes-sociais)

## Pesquisa

**Comece por:** parallel-search + claude-deep-research-skill

| Ferramenta | Tipo | Descrição | Status |
|---|---|---|---|
| [agent-research-skills](tools/agent-research-skills) | skill | 31 skills para pesquisa acadêmica, da revisão de literatura a slides. | catalogado |
| [brave-search](tools/brave-search) | mcp | MCP de busca web, notícias, imagens, vídeos e local via Brave. | catalogado |
| [claude-deep-research-skill](tools/claude-deep-research-skill) | skill | Skill de deep research com pipeline de 8 fases, credibilidade de fontes e relatório com citações. | catalogado |
| [context7](tools/context7) | mcp | MCP com documentação de bibliotecas atualizada e por versão. | catalogado |
| [deep-research-skills-hitl](tools/deep-research-skills-hitl) | skill | Pesquisa estruturada em duas fases com aprovação humana a cada etapa. | catalogado |
| [exa-search](tools/exa-search) | mcp | MCP de busca semântica para agentes; bom para docs técnicas e papers. | catalogado |
| [firecrawl-research](tools/firecrawl-research) | mcp | Agente autônomo de pesquisa e scraping para temas com muitas fontes. | catalogado |
| [github-deep-research](tools/github-deep-research) | skill | Investigação em 4 etapas de repositórios GitHub (API, web, timeline, saúde da comunidade). | catalogado |
| [parallel-search](tools/parallel-search) | mcp | MCP gratuito e sem login com web_search e web_fetch (Parallel). | catalogado |
| [perplexity-mcp](tools/perplexity-mcp) | mcp | MCP de busca com etapa de raciocínio que responde perguntas com fontes. | catalogado |
| [tavily-search](tools/tavily-search) | mcp | MCP de busca e pesquisa com resultados estruturados para agentes. | catalogado |

## Economia de tokens

**Comece por:** rtk + context-mode + token-economy-guide

| Ferramenta | Tipo | Descrição | Status |
|---|---|---|---|
| [bifrost-code-mode](tools/bifrost-code-mode) | mcp | Expõe servidores MCP como arquivos Python leves para o modelo ler só o necessário. | catalogado |
| [context-mode](tools/context-mode) | mcp | Plugin MCP que envia saídas grandes de ferramentas para uma base local em vez da conversa. | catalogado |
| [inference-optimizer](tools/inference-optimizer) | outro | Ferramenta de otimização de inferência encontrada na busca; detalhes não verificados. | catalogado |
| [rtk](tools/rtk) | cli | CLI em Rust que comprime saídas de comandos antes de chegarem ao Claude (60-90% a menos). | catalogado |
| [semantic-cache-mcp](tools/semantic-cache-mcp) | mcp | MCP de cache semântico para reduzir leituras repetidas. | catalogado |
| [token-economy-guide](tools/token-economy-guide) | guia | Boas práticas para gastar menos tokens no Claude Code. | catalogado |
| [token-reducer](tools/token-reducer) | mcp | Compressão de contexto local e gratuita com RAG híbrido (BM25 + ONNX), chunking por AST e reranking. | catalogado |
| [token-savior-caveman](tools/token-savior-caveman) | outro | token-savior e caveman, citados em comparativo com reduções de 20-43% junto com cache MCP e roteamento Haiku. | catalogado |

## Design

**Comece por:** figma-mcp + ui-ux-pro-max

| Ferramenta | Tipo | Descrição | Status |
|---|---|---|---|
| [adobe-mcp](tools/adobe-mcp) | mcp | Conector Adobe com ferramentas pro de design, edição e animação. | catalogado |
| [aidesigner-mcp](tools/aidesigner-mcp) | mcp | MCP de geração de UI com IA. | catalogado |
| [anthropic-frontend-design](tools/anthropic-frontend-design) | skill | Skill oficial da Anthropic para frontends distintos, longe do visual genérico de IA. | catalogado |
| [awesome-claude-design](tools/awesome-claude-design) | lista | DESIGN.md por família estética, receitas e kits anti-slop. | catalogado |
| [canva-mcp](tools/canva-mcp) | mcp | Conector do Canva para buscar, criar, preencher e exportar designs. | catalogado |
| [claude-frontend-skills](tools/claude-frontend-skills) | skill | Plugin de skills para frontends distintos e não genéricos. | catalogado |
| [doop-design](tools/doop-design) | mcp | Comparativo de MCPs de design para Claude Code (Doop, Figma Dev Mode, Paper, Pencil, Magic). | catalogado |
| [figma-mcp](tools/figma-mcp) | mcp | Conector oficial do Figma: contexto de design, tokens, variáveis, Code Connect e diagramas. | catalogado |
| [frontend-design-anchors](tools/frontend-design-anchors) | skill | Skill com 8 âncoras estéticas que fixam paleta, tipografia e textura em tokens CSS. | catalogado |
| [frontend-design-toolkit](tools/frontend-design-toolkit) | lista | Coletânea de skills, plugins, MCPs e truques de CLAUDE.md para frontends melhores. | catalogado |
| [libreuiux](tools/libreuiux) | skill | Sistema de UI/UX com dezenas de agentes, skills, slash commands e vocabulário de design. | catalogado |
| [magic-patterns-mcp](tools/magic-patterns-mcp) | mcp | Conector para discutir e iterar protótipos de UI do Magic Patterns. | catalogado |
| [moda-mcp](tools/moda-mcp) | mcp | Conector Moda para slides, anúncios, motion graphics e posts editáveis. | catalogado |
| [taste-skill](tools/taste-skill) | skill | Suíte de 11 variantes de skill de frontend e 3 de geração de imagem, com ajuste por 3 parâmetros. | catalogado |
| [ui-ux-pro-max](tools/ui-ux-pro-max) | skill | Gera design system completo: 84 estilos, 192 paletas, 74 pares de fontes, 98 diretrizes de UX. | catalogado |

## Jogos

**Comece por:** MCP da sua engine + ludo-mcp (assets)

| Ferramenta | Tipo | Descrição | Status |
|---|---|---|---|
| [awesome-gamedev-agent-skills](tools/awesome-gamedev-agent-skills) | skill | 74 skills de gamedev (Godot, Unity, Unreal, Phaser, three.js, Bevy, Roblox) com roteador por engine. | catalogado |
| [blender-mcp](tools/blender-mcp) | mcp | MCP original da comunidade para controlar o Blender (cenas, objetos, render). | catalogado |
| [claude-code-game-development](tools/claude-code-game-development) | plugin | 22 plugins de jogos (Godot, Unity, Unreal, multiplayer, áudio, shaders) e manual de 80 capítulos. | catalogado |
| [claude-code-game-studios](tools/claude-code-game-studios) | skill | Estúdio de jogos com 49 agentes e mais de 70 skills coordenados. | catalogado |
| [gamedev-all-in-one-mcp](tools/gamedev-all-in-one-mcp) | mcp | MCP multi-engine de desenvolvimento de jogos. | catalogado |
| [gamelabs-mcp](tools/gamelabs-mcp) | mcp | Gera sprites com fundo transparente, animações e sprite sheets prontas para engine. | catalogado |
| [godogen](tools/godogen) | skill | Desenvolvimento autônomo de jogos para Godot, Bevy e Babylon.js. | catalogado |
| [gstack-game](tools/gstack-game) | skill | 27 skills do conceito ao build: design review, protótipo, game feel, QA e release. | catalogado |
| [ludo-mcp](tools/ludo-mcp) | mcp | Gera sprites, spritesheets, modelos 3D, animações, efeitos sonoros, música e voz. | catalogado |
| [mcp-unity](tools/mcp-unity) | mcp | Plugin MCP que conecta o Unity Editor ao Claude Code (GameObjects, componentes, pacotes). | catalogado |
| [phaser-game-agent-mcp](tools/phaser-game-agent-mcp) | mcp | MCP oficial do Phaser para criar jogos web com código, arte e som pelo agente. | catalogado |
| [roblox-studio-mcp](tools/roblox-studio-mcp) | mcp | MCP nativo do Roblox Studio: insere modelos da Creator Store e executa Luau. | catalogado |
| [spritecook-mcp](tools/spritecook-mcp) | mcp | Gera sprites, animações, tilesets e arte de jogo. | catalogado |
| [unreal-mcp](tools/unreal-mcp) | mcp | MCPs open source para Unreal Engine; UE 5.8 traz plugin MCP experimental oficial. | catalogado |

## Godot

**Comece por:** godot-ai-dlight ou gdai-mcp + godotprompter + godot-agent-skills-qblab

| Ferramenta | Tipo | Descrição | Status |
|---|---|---|---|
| [ai-assistant-hub](tools/ai-assistant-hub) | editor | Plugin open source (MIT) para usar LLMs dentro do editor (Ollama, Gemini, OpenRouter). | catalogado |
| [claude-godot-mcp](tools/claude-godot-mcp) | mcp | MCP com cerca de 170 ferramentas: nós, scripts, sinais, grupos, autoloads e shaders. | catalogado |
| [claude-godot-tools](tools/claude-godot-tools) | plugin | Plugins Claude Code: servidor de linguagem GDScript (LSP) e integração com gdUnit4. | catalogado |
| [flatten-for-llm](tools/flatten-for-llm) | editor | Achata o projeto Godot em texto para colar num LLM. | catalogado |
| [fuku](tools/fuku) | editor | Plugin que integra vários provedores de IA ao editor Godot. | catalogado |
| [gd-agentic-skills](tools/gd-agentic-skills) | skill | 99 skills e 27 blueprints de gênero com GDScript tipado para Godot 4.7+. | catalogado |
| [gdai-mcp](tools/gdai-mcp) | mcp | MCP apontado como o mais polido para Godot: cenas, recursos, scripts, erros e logs do editor. | catalogado |
| [godot-agent-skills-qblab](tools/godot-agent-skills-qblab) | skill | Edição segura de .tscn/.tres sem quebrar UIDs, guardas contra API do Godot 3 e hooks de verificação. | catalogado |
| [godot-ai-assistant-groq](tools/godot-ai-assistant-groq) | editor | Assistente de GDScript, cenas e chat usando a API gratuita do Groq (LLaMA). | catalogado |
| [godot-ai-dlight](tools/godot-ai-dlight) | mcp | Plugin MIT que conecta Claude Code a um editor Godot ao vivo via MCP (Godot 4.5+). | catalogado |
| [godot-ai-guide](tools/godot-ai-guide) | guia | Comparativos de ferramentas de IA para Godot (MCPs, plugins e assistentes). | catalogado |
| [godot-claude-skills](tools/godot-claude-skills) | skill | Skills do Claude para a engine Godot. | catalogado |
| [godot-claude-skills-alexmeckes](tools/godot-claude-skills-alexmeckes) | skill | Coleção de skills do Claude para Godot. | catalogado |
| [godot-forge](tools/godot-forge) | mcp | MCP com suporte preciso a GDScript, análise de projeto, docs e testes GUT/GdUnit4 headless. | catalogado |
| [godot-mcp](tools/godot-mcp) | mcp | MCPs para o editor Godot: cenas, nós, scripts, erros e logs. | catalogado |
| [godot-mcp-coding-solo](tools/godot-mcp-coding-solo) | mcp | MCP MIT sem plugin: abre o editor, roda o projeto em debug e captura a saída via linha de comando. | catalogado |
| [godot-mcp-mkdevkit](tools/godot-mcp-mkdevkit) | mcp | MCP open source para controlar o editor Godot 4 diretamente. | catalogado |
| [godot-mcp-pro](tools/godot-mcp-pro) | mcp | 162 ferramentas MCP: cena, animação, 3D, física, partículas, áudio, shader, simulação de input, testes. | catalogado |
| [godot-mcp-satelliteoflove](tools/godot-mcp-satelliteoflove) | mcp | MCP com 77 ferramentas em 15 categorias, incluindo testes headless e debug com breakpoints. | catalogado |
| [godot-skill-shihab](tools/godot-skill-shihab) | skill | Skill para GDScript 2.0 com tipagem estática estrita e guia de estilo oficial (Godot 4.3+). | catalogado |
| [godot-skills-vl4dt](tools/godot-skills-vl4dt) | skill | 12 skills (GDScript, C#, física, animação, UI, rede, debug) cobrindo Godot 4.7. | catalogado |
| [godotprompter](tools/godotprompter) | skill | 56 skills para Godot 4.x (GDScript e C#): arquitetura, física, shaders, UI, multiplayer, otimização. | catalogado |
| [golem-ai](tools/golem-ai) | editor | Assistente no dock do editor com modelos locais ou na nuvem, incluindo Anthropic. | catalogado |
| [strayspark-godot-mcp](tools/strayspark-godot-mcp) | mcp | MCP comercial focado em edição de cenas e scripts do Godot 4.x, com ferramentas curadas. | catalogado |
| [summer-engine](tools/summer-engine) | editor | Editor AI-native compatível com projetos .godot, com chat e acesso ao jogo rodando. | catalogado |
| [ziva](tools/ziva) | editor | Agente de IA dentro do editor Godot 4.2+: árvore de cenas, sinais, GDScript/C#, sprites e TileMaps. | catalogado |

## Aprendizado

**Comece por:** key-learning ou study-skill + anki-mcp + youtube-transcript-mcp

| Ferramenta | Tipo | Descrição | Status |
|---|---|---|---|
| [adhd-study-coach](tools/adhd-study-coach) | skill | Agente de estudo para TDAH: blocos pequenos, repetição espaçada e reflexão Feynman. | catalogado |
| [agent-tutor-skill](tools/agent-tutor-skill) | skill | Tutor baseado em ciência cognitiva: ciclo de ensino, FSRS, quizzes sem dica e domínio por conceito. | catalogado |
| [anki-mcp](tools/anki-mcp) | mcp | MCPs que criam, buscam e revisam flashcards no Anki via AnkiConnect. | catalogado |
| [claude-tutor-kirilxd](tools/claude-tutor-kirilxd) | plugin | Tutor com planos personalizados, quizzes adaptativos, repetição SM-2 e painel web. | catalogado |
| [claude-tutor-kubilaiswf](tools/claude-tutor-kubilaiswf) | plugin | Tutor com syllabus, lições liberadas por domínio, provas e revisão espaçada; regras citadas da pesquisa. | catalogado |
| [codebase-to-course](tools/codebase-to-course) | skill | Transforma um código em curso HTML interativo com quizzes e tradução para linguagem simples. | catalogado |
| [goodnotes](tools/goodnotes) | mcp | Gera documentos, diagramas Mermaid e imagens SVG no Goodnotes. | catalogado |
| [key-learning](tools/key-learning) | skill | Tutor para qualquer área: explica por primeiros princípios, diagnostica nível de Bloom, cria plano e agenda revisões em markdown. | catalogado |
| [kuliko-ai](tools/kuliko-ai) | mcp | Companheiro de estudo: matérias, documentos, recursos gerados e flashcards. | catalogado |
| [learn-mode](tools/learn-mode) | skill | Comando /learn que explica os conceitos do que o Claude acabou de fazer e salva notas. | catalogado |
| [learning-commons](tools/learning-commons) | mcp | Padrões, habilidades e progressões de aprendizagem do ensino básico (K-12, EUA). | catalogado |
| [learning-output-style](tools/learning-output-style) | plugin | Plugin oficial da Anthropic que faz o Claude pedir sua contribuição em pontos de decisão. | catalogado |
| [maxlearn](tools/maxlearn) | plugin | Mod do Claude Code que transforma tópicos das suas conversas em aulas curtas e flashcards com FSRS. | catalogado |
| [mem0](tools/mem0) | mcp | Memória persistente para agentes (adicionar, buscar e atualizar memórias). | catalogado |
| [memory-knowledge-graph](tools/memory-knowledge-graph) | mcp | Memória oficial de referência do MCP: entidades, relações e observações em JSON local. | catalogado |
| [obsidian-mcp](tools/obsidian-mcp) | mcp | MCPs para ler, buscar e editar notas de um cofre Obsidian. | catalogado |
| [study-skill](tools/study-skill) | skill | Tutor interativo com repetição espaçada FSRS-6, agentes de pesquisa, catálogo de livros e sessões adaptadas a TDAH. | catalogado |
| [study-skills-jacquard](tools/study-skills-jacquard) | skill | 8 skills combináveis: flashcards, quizzes, checagem de conceitos, leitor de papers e mais. | catalogado |
| [wikipedia-mcp](tools/wikipedia-mcp) | mcp | Busca artigos, resumos, referências e categorias da Wikipédia. | catalogado |
| [wolfram-alpha-mcp](tools/wolfram-alpha-mcp) | mcp | Cálculos, equações, conversões e dados factuais via Wolfram Alpha. | catalogado |
| [youtube-transcript-mcp](tools/youtube-transcript-mcp) | mcp | Lê transcrições do YouTube sem chave de API. | catalogado |
| [zotero-mcp](tools/zotero-mcp) | mcp | Conecta a biblioteca Zotero: busca em PDFs, resumos, citações e anotações. | catalogado |

## Imagem e vídeo

**Comece por:** kinocut (vídeo) + mcp-image (imagem) + claude-remotion-skill

| Ferramenta | Tipo | Descrição | Status |
|---|---|---|---|
| [awesome-claude-video-skills](tools/awesome-claude-video-skills) | lista | Lista com 180 repositórios de vídeo para agentes, classificados por tipo e segurança. | catalogado |
| [claude-code-video-toolkit](tools/claude-code-video-toolkit) | skill | Kit de produção de vídeo: Remotion, ElevenLabs, FFmpeg, gravação com Playwright e edição de imagem. | catalogado |
| [claude-remotion-skill](tools/claude-remotion-skill) | skill | Skill para criar e editar vídeos de motion graphics com Remotion: legendas sincronizadas, cor e som. | catalogado |
| [cloudinary-mcp](tools/cloudinary-mcp) | mcp | Gerencia, transforma e entrega imagens e vídeos. | catalogado |
| [creatomate](tools/creatomate) | mcp | Renderização de vídeo a partir de templates via MCP. | catalogado |
| [davinci-resolve-mcp](tools/davinci-resolve-mcp) | mcp | Controle do DaVinci Resolve: edição, cor, áudio e render. Resolve 21.1 tem MCP nativo. | catalogado |
| [editassist](tools/editassist) | mcp | MCP que busca clipes, lê transcrições, monta rough cuts e controla o editor de vídeo localmente. | catalogado |
| [elevenlabs-mcp](tools/elevenlabs-mcp) | mcp | Conector ElevenLabs no registro do Claude (foco em agentes de voz). | catalogado |
| [fal-ai-mcp](tools/fal-ai-mcp) | mcp | MCP hospedado com acesso a mais de 1000 modelos generativos de imagem, vídeo e áudio. | catalogado |
| [ffmpeg-mcp-server](tools/ffmpeg-mcp-server) | mcp | MCP com FFmpeg para velocidade, keyframes, concatenação e extração de destaques. | catalogado |
| [gimp-mcp](tools/gimp-mcp) | mcp | Controle do GIMP pelo Claude para edição de imagem. | catalogado |
| [image-generation-mcp](tools/image-generation-mcp) | mcp | Uma interface para DALL-E, modelos de imagem do Gemini e Stable Diffusion local. | catalogado |
| [imagineart-mcp](tools/imagineart-mcp) | mcp | Gera imagem, vídeo e música, remove fundo e faz upscale 4x num só endpoint. | catalogado |
| [jumper](tools/jumper) | mcp | MCP para tarefas repetitivas em Premiere Pro, DaVinci Resolve, Final Cut Pro e Avid. | catalogado |
| [kinocut](tools/kinocut) | mcp | MCP local e gratuito de edição de vídeo com FFmpeg: cortar, legendar, reaproveitar e checar qualidade. | catalogado |
| [krita-mcp](tools/krita-mcp) | mcp | Controle do Krita: camadas, desenho, filtros, exportação, e lê o canvas como PNG para ver o resultado. | catalogado |
| [mcp-image](tools/mcp-image) | mcp | Gera e edita imagens com otimização automática de prompt (Gemini, GPT Image, Seedream). | catalogado |
| [midia-guide](tools/midia-guide) | guia | Comparativos de MCPs de imagem e vídeo para o Claude. | catalogado |
| [orshot](tools/orshot) | mcp | Automatiza vídeos, PDFs e imagens a partir de templates e publica em redes sociais. | catalogado |
| [photoshop-mcp](tools/photoshop-mcp) | mcp | Controle do Adobe Photoshop: camadas, filtros, IA generativa e receitas. | catalogado |
| [reap](tools/reap) | mcp | Cortes, legendas e dublagem de vídeos para redes sociais via MCP. | catalogado |
| [recraft-mcp](tools/recraft-mcp) | mcp | MCP do Recraft para gerar imagens e vetores. | catalogado |
| [shotstack](tools/shotstack) | mcp | API de edição de vídeo na nuvem com MCP nativo. | catalogado |
| [unsplash-mcp](tools/unsplash-mcp) | mcp | Busca e usa imagens HD gratuitas do Unsplash. | catalogado |
| [video-audio-mcp](tools/video-audio-mcp) | mcp | MCP com FFmpeg para vídeo e áudio: conversão, cortes, sobreposições, transições e áudio. | catalogado |
| [video-editing-skill](tools/video-editing-skill) | skill | Fluxo de edição de vídeo real: FFmpeg, Remotion, ElevenLabs, fal.ai e acabamento no Descript ou CapCut. | catalogado |
| [video-toolkit-wilwaldon](tools/video-toolkit-wilwaldon) | lista | Coletânea de skills, MCPs e ferramentas de vídeo: Remotion, Manim, gravação de tela, YouTube e FFmpeg. | catalogado |
| [wireflow](tools/wireflow) | mcp | MCP hospedado que roda pipelines completos de vídeo com IA. | catalogado |

## Marketing

**Comece por:** marketingskills + ahrefs-mcp ou semrush-mcp + google-analytics-mcp

| Ferramenta | Tipo | Descrição | Status |
|---|---|---|---|
| [adobe-marketing-agent](tools/adobe-marketing-agent) | mcp | Insights de campanhas e públicos da Adobe (Experience Platform). | catalogado |
| [adspirer](tools/adspirer) | mcp | Agente de mídia paga que planeja, lança e gerencia campanhas em Google, Meta, LinkedIn, TikTok e mais. | catalogado |
| [adwhispr](tools/adwhispr) | mcp | Pesquisa anúncios ativos de marcas no Facebook e TikTok, acha concorrentes e lança campanhas. | catalogado |
| [ahrefs-mcp](tools/ahrefs-mcp) | mcp | MCP oficial do Ahrefs: palavras-chave, ranking, backlinks, auditoria de site e visibilidade em buscas de IA. | catalogado |
| [ai-marketing-claude](tools/ai-marketing-claude) | skill | 15 skills com subagentes: auditoria de site, copy, sequências de e-mail, anúncios, calendário e relatórios em PDF. | catalogado |
| [boraoztunc-skills](tools/boraoztunc-skills) | skill | Skills de copywriting, SEO e design. | catalogado |
| [claude-marketing-rebecca](tools/claude-marketing-rebecca) | skill | Pacotes de skills para Klaviyo, Shopify, GA4, Looker Studio e mídia paga. | catalogado |
| [claude-skills-alirezarezvani](tools/claude-skills-alirezarezvani) | skill | Mais de 380 skills e plugins (engenharia, marketing, produto, compliance, negócios). | catalogado |
| [google-ads-mcp](tools/google-ads-mcp) | mcp | MCP oficial do Google Ads, open source e somente leitura (3 ferramentas, consultas GAQL). | catalogado |
| [google-analytics-mcp](tools/google-analytics-mcp) | mcp | MCP oficial do Google Analytics 4, somente leitura. | catalogado |
| [hubspot-mcp](tools/hubspot-mcp) | mcp | MCP oficial do HubSpot: contatos, empresas, negócios, atribuição de campanhas e analytics de e-mail. | catalogado |
| [klaviyo-mcp](tools/klaviyo-mcp) | mcp | Relatórios, estratégia e criação de campanhas com dados do Klaviyo em tempo real. | catalogado |
| [mailchimp-mcp](tools/mailchimp-mcp) | mcp | Cria e edita campanhas de e-mail no Mailchimp (temas, textos, imagens). | catalogado |
| [marketing-guide](tools/marketing-guide) | guia | Comparativos de MCPs para marketing (analytics, anúncios, SEO, social). | catalogado |
| [marketingskills](tools/marketingskills) | skill | Skills de marketing: CRO, copywriting, SEO, analytics, testes A/B e growth. | catalogado |
| [meta-ads-mcp](tools/meta-ads-mcp) | mcp | MCP oficial da Meta (beta gratuito) com leitura e escrita em campanhas de Facebook e Instagram. | catalogado |
| [metricool](tools/metricool) | mcp | MCP oficial do Metricool: agenda posts, melhor horário por rede e análise de métricas sociais. | catalogado |
| [motion-creative-analytics](tools/motion-creative-analytics) | mcp | Analisa criativos de anúncios da Meta e bibliotecas de anúncios de concorrentes. | catalogado |
| [openclaudia-skills](tools/openclaudia-skills) | skill | 77 skills open source de marketing: SEO, conteúdo, e-mail, anúncios, analytics e growth. | catalogado |
| [openrush](tools/openrush) | mcp | SEO e concorrência com dados ao vivo: palavras-chave, ranking, gap de backlinks, auditoria e citações em IA. | catalogado |
| [openseo](tools/openseo) | mcp | SEO simplificado: projetos, rastreamento de ranking, concorrentes na SERP e auditoria. | catalogado |
| [ryze-ads-mcp](tools/ryze-ads-mcp) | mcp | MCP hospedado com Google Ads, Meta Ads, GA4 e Search Console (mais de 250 ferramentas), login OAuth e escrita com aprovação. | catalogado |
| [segmentstream](tools/segmentstream) | mcp | Analytics de marketing com atribuição entre canais a partir do data warehouse. | catalogado |
| [semrush-mcp](tools/semrush-mcp) | mcp | MCP do Semrush: palavras-chave, concorrentes, tráfego, backlinks, domínios e PPC. | catalogado |
| [socialclaw](tools/socialclaw) | mcp | MCP hospedado de publicação em redes sociais com 17 ferramentas e contas via OAuth. | catalogado |
| [supermetrics](tools/supermetrics) | mcp | Dados de mais de 200 fontes de marketing (Google Ads, Meta, GA, TikTok, LinkedIn, YouTube) num só conector. | catalogado |
| [typefully](tools/typefully) | mcp | Agenda e escreve posts para X, LinkedIn, Substack, Threads, Bluesky e Mastodon. | catalogado |

## Redes sociais

**Comece por:** postiz ou buffer-mcp (agendar) + MCP da rede principal + social-calendar-skill + octolens (escuta)

| Ferramenta | Tipo | Descrição | Status |
|---|---|---|---|
| [ayrshare-mcp](tools/ayrshare-mcp) | mcp | API de redes sociais para desenvolvedores com MCP cobrindo mais de 13 plataformas. | catalogado |
| [bluesky-mcp](tools/bluesky-mcp) | mcp | Conjunto de ferramentas MCP para interagir com o Bluesky. | catalogado |
| [buffer-mcp](tools/buffer-mcp) | mcp | MCP do Buffer em todos os planos (inclusive o grátis): cria e agenda posts, gerencia fila, ideias e analytics. | catalogado |
| [claude-code-channels](tools/claude-code-channels) | plugin | Recurso do Claude Code (março de 2026) que liga uma sessão ao Telegram ou Discord para conversar com o agente por lá. | catalogado |
| [claude-instagram](tools/claude-instagram) | skill | Motor de conteúdo para Instagram: 13 sub-skills, 6 agentes, ganchos, Reels, carrosséis e pontuação de 100 pontos. | catalogado |
| [datalikers-mcp](tools/datalikers-mcp) | mcp | 29 ferramentas de dados do Instagram e TikTok. | catalogado |
| [discord-mcp](tools/discord-mcp) | mcp | MCP de bot do Discord com cerca de 71 ferramentas: canais, cargos, moderação, eventos e automod. | catalogado |
| [embedsocial](tools/embedsocial) | mcp | MCP oficial do EmbedSocial: posts, avaliações, menções e conteúdo gerado por usuários em relatórios. | catalogado |
| [hasdata-social](tools/hasdata-social) | mcp | MCPs hospedados da HasData com dados públicos (só leitura) de perfis, posts, vídeos e comentários do Instagram e TikTok. | catalogado |
| [insightsocial](tools/insightsocial) | mcp | CLI e MCP oficial com 239 endpoints de dados públicos de Instagram, TikTok, LinkedIn, YouTube, X e mais. | catalogado |
| [instagram-mcp](tools/instagram-mcp) | mcp | Publica e agenda posts, carrosséis e Reels pela API oficial do Instagram (contas Business/Creator). | catalogado |
| [instagram-skills](tools/instagram-skills) | skill | Skills de legendas, carrosséis, ganchos, hashtags e plano semanal para Instagram, na sua voz. | catalogado |
| [intenthunter](tools/intenthunter) | mcp | Menções da marca e de concorrentes com pontuação, para filtrar e priorizar. | catalogado |
| [linkedin-mcp](tools/linkedin-mcp) | mcp | MCP open source do LinkedIn: perfis, empresas, vagas e mensagens (o mais popular, mais de 3 mil estrelas). | catalogado |
| [octolens](tools/octolens) | mcp | Escuta social: menções da marca em mais de 15 plataformas e gestão de palavras-chave. | catalogado |
| [posteverywhere-mcp](tools/posteverywhere-mcp) | mcp | MCP oficial do PostEverywhere: agenda e publica em Instagram, TikTok, YouTube, LinkedIn, Facebook, X, Threads e Pinterest. | catalogado |
| [postiz](tools/postiz) | mcp | Agendador open source com MCP próprio: contas, rascunhos, mídia, agendamento e publicação em mais de 30 redes. | catalogado |
| [postsyncer-mcp](tools/postsyncer-mcp) | mcp | Plugin/MCP do PostSyncer para agendar posts em várias redes. | catalogado |
| [publer-mcp](tools/publer-mcp) | mcp | Agenda e publica em 9 redes pelo Publer (inclui Bluesky e Mastodon). | catalogado |
| [reddit-mcp-buddy](tools/reddit-mcp-buddy) | mcp | Navega posts, busca conteúdo e analisa usuários do Reddit sem chave de API. | catalogado |
| [social-calendar-skill](tools/social-calendar-skill) | skill | Gera calendário mensal de redes sociais pesquisado e auditado, com análise de concorrentes, num só comando. | catalogado |
| [social-guide](tools/social-guide) | guia | Comparativos de MCPs para redes sociais (agendamento, plataformas, escuta). | catalogado |
| [social-listening-mcp](tools/social-listening-mcp) | mcp | MCP comunitário de escuta social. | catalogado |
| [social-mcp-collections](tools/social-mcp-collections) | lista | Coleções de MCPs sociais: X, Bluesky, LinkedIn, Reddit, Discord e Hacker News. | catalogado |
| [social-media-manager-borghei](tools/social-media-manager-borghei) | skill | Skill de gestor de redes sociais: estratégia, ganchos, calendário e reaproveitamento de conteúdo. | catalogado |
| [telegram-mcp](tools/telegram-mcp) | mcp | Lê chats, gerencia grupos e envia ou edita mensagens e mídia no Telegram (Telethon). | catalogado |
| [threads-carousel-skill](tools/threads-carousel-skill) | skill | Transforma um post de texto em imagens de carrossel para Threads, Instagram, LinkedIn e TikTok (PNG ou PDF). | catalogado |
| [tiktok-for-business](tools/tiktok-for-business) | mcp | Conector oficial do TikTok for Business para criar, gerenciar e analisar campanhas de anúncios. | catalogado |
| [trends-mcp](tools/trends-mcp) | mcp | Busca tendências do YouTube, TikTok e Reels do Instagram. | catalogado |
| [upload-post-mcp](tools/upload-post-mcp) | mcp | Publica e agenda vídeos, fotos, carrosséis e textos em 11 redes e lê analytics e comentários. | catalogado |
| [vidiq](tools/vidiq) | mcp | Pesquisa de palavras-chave, vídeos em alta, outliers e estatísticas de canais para YouTube, Instagram e TikTok. | catalogado |
| [whatsapp-mcp](tools/whatsapp-mcp) | mcp | Liga sua conta pessoal do WhatsApp ao Claude: ler, buscar, enviar, transmitir e gerenciar grupos (22 ferramentas, local). | catalogado |
| [x-mcp](tools/x-mcp) | mcp | Publica e agenda tweets com imagens, GIFs e vídeo pela API oficial do X, com skills de threads e calendário. | catalogado |
| [youtube-mcp](tools/youtube-mcp) | mcp | Gestão de canal do YouTube com 21 ferramentas, incluindo analytics (views, watch time, inscritos, receita). | catalogado |
