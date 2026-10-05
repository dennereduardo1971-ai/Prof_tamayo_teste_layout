# Índice de ferramentas

Busque aqui primeiro. Detalhes, `alternativas` e `combina-com` ficam no frontmatter de cada `tools/<nome>/README.md`.

Seções: [Pesquisa](#pesquisa) · [Economia de tokens](#economia-de-tokens) · [Design](#design) · [Jogos](#jogos) · [Godot](#godot) · [Aprendizado](#aprendizado)

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
