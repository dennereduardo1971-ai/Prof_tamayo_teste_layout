# Índice de ferramentas

| Ferramenta | Descrição | Tags |
|---|---|---|
| [parallel-search](tools/parallel-search) | MCP gratuito e sem login com web_search e web_fetch (Parallel). | pesquisa, mcp |
| [exa-search](tools/exa-search) | MCP de busca semântica para agentes; bom para docs técnicas e papers. | pesquisa, mcp |
| [tavily-search](tools/tavily-search) | MCP de busca e pesquisa com resultados estruturados para agentes. | pesquisa, mcp |
| [brave-search](tools/brave-search) | MCP de busca web, notícias, imagens, vídeos e local via Brave. | pesquisa, mcp |
| [perplexity-mcp](tools/perplexity-mcp) | MCP de busca com etapa de raciocínio que responde perguntas com fontes. | pesquisa, mcp |
| [firecrawl-research](tools/firecrawl-research) | Agente autônomo de pesquisa e scraping para temas com muitas fontes. | pesquisa, mcp |
| [context7](tools/context7) | MCP com documentação de bibliotecas atualizada e por versão. | pesquisa, mcp |
| [claude-deep-research-skill](tools/claude-deep-research-skill) | Skill de deep research com pipeline de 8 fases, credibilidade de fontes e relatório com citações. | pesquisa, skill |
| [deep-research-skills-hitl](tools/deep-research-skills-hitl) | Pesquisa estruturada em duas fases com aprovação humana a cada etapa. | pesquisa, skill |
| [agent-research-skills](tools/agent-research-skills) | 31 skills para pesquisa acadêmica, da revisão de literatura a slides. | pesquisa, skill |
| [github-deep-research](tools/github-deep-research) | Investigação em 4 etapas de repositórios GitHub (API, web, timeline, saúde da comunidade). | pesquisa, skill |
| [rtk](tools/rtk) | CLI em Rust que comprime saídas de comandos antes de chegarem ao Claude (60-90% a menos). | economia-de-token, cli-hook |
| [context-mode](tools/context-mode) | Plugin MCP que envia saídas grandes de ferramentas para uma base local em vez da conversa. | economia-de-token, mcp |
| [token-reducer](tools/token-reducer) | Compressão de contexto local e gratuita com RAG híbrido (BM25 + ONNX), chunking por AST e reranking. | economia-de-token, mcp |
| [semantic-cache-mcp](tools/semantic-cache-mcp) | MCP de cache semântico para reduzir leituras repetidas. | economia-de-token, mcp |
| [bifrost-code-mode](tools/bifrost-code-mode) | Expõe servidores MCP como arquivos Python leves para o modelo ler só o necessário. | economia-de-token, mcp |
| [inference-optimizer](tools/inference-optimizer) | Ferramenta de otimização de inferência encontrada na busca; detalhes não verificados. | economia-de-token, outro |
| [token-savior-caveman](tools/token-savior-caveman) | token-savior e caveman, citados em comparativo com reduções de 20-43% junto com cache MCP e roteamento Haiku. | economia-de-token, outro |
| [token-economy-guide](tools/token-economy-guide) | Boas práticas para gastar menos tokens no Claude Code. | economia-de-token, guia |
| [figma-mcp](tools/figma-mcp) | Conector oficial do Figma: contexto de design, tokens, variáveis, Code Connect e diagramas. | design, mcp |
| [canva-mcp](tools/canva-mcp) | Conector do Canva para buscar, criar, preencher e exportar designs. | design, mcp |
| [adobe-mcp](tools/adobe-mcp) | Conector Adobe com ferramentas pro de design, edição e animação. | design, mcp |
| [magic-patterns-mcp](tools/magic-patterns-mcp) | Conector para discutir e iterar protótipos de UI do Magic Patterns. | design, mcp |
| [moda-mcp](tools/moda-mcp) | Conector Moda para slides, anúncios, motion graphics e posts editáveis. | design, mcp |
| [aidesigner-mcp](tools/aidesigner-mcp) | MCP de geração de UI com IA. | design, mcp |
| [doop-design](tools/doop-design) | Comparativo de MCPs de design para Claude Code (Doop, Figma Dev Mode, Paper, Pencil, Magic). | design, mcp |
| [anthropic-frontend-design](tools/anthropic-frontend-design) | Skill oficial da Anthropic para frontends distintos, longe do visual genérico de IA. | design, skill |
| [ui-ux-pro-max](tools/ui-ux-pro-max) | Gera design system completo: 84 estilos, 192 paletas, 74 pares de fontes, 98 diretrizes de UX. | design, skill |
| [taste-skill](tools/taste-skill) | Suíte de 11 variantes de skill de frontend e 3 de geração de imagem, com ajuste por 3 parâmetros. | design, skill |
| [awesome-claude-design](tools/awesome-claude-design) | DESIGN.md por família estética, receitas e kits anti-slop. | design, lista |
| [libreuiux](tools/libreuiux) | Sistema de UI/UX com dezenas de agentes, skills, slash commands e vocabulário de design. | design, skill |
| [claude-frontend-skills](tools/claude-frontend-skills) | Plugin de skills para frontends distintos e não genéricos. | design, skill |
| [frontend-design-anchors](tools/frontend-design-anchors) | Skill com 8 âncoras estéticas que fixam paleta, tipografia e textura em tokens CSS. | design, skill |
| [frontend-design-toolkit](tools/frontend-design-toolkit) | Coletânea de skills, plugins, MCPs e truques de CLAUDE.md para frontends melhores. | design, lista |
| [mcp-unity](tools/mcp-unity) | Plugin MCP que conecta o Unity Editor ao Claude Code (GameObjects, componentes, pacotes). | jogos, mcp |
| [unreal-mcp](tools/unreal-mcp) | MCPs open source para Unreal Engine; UE 5.8 traz plugin MCP experimental oficial. | jogos, mcp |
| [godot-mcp](tools/godot-mcp) | MCPs para o editor Godot: cenas, nós, scripts, erros e logs. | jogos, mcp |
| [blender-mcp](tools/blender-mcp) | MCP original da comunidade para controlar o Blender (cenas, objetos, render). | jogos, mcp |
| [roblox-studio-mcp](tools/roblox-studio-mcp) | MCP nativo do Roblox Studio: insere modelos da Creator Store e executa Luau. | jogos, mcp |
| [phaser-game-agent-mcp](tools/phaser-game-agent-mcp) | MCP oficial do Phaser para criar jogos web com código, arte e som pelo agente. | jogos, mcp |
| [ludo-mcp](tools/ludo-mcp) | Gera sprites, spritesheets, modelos 3D, animações, efeitos sonoros, música e voz. | jogos, mcp |
| [spritecook-mcp](tools/spritecook-mcp) | Gera sprites, animações, tilesets e arte de jogo. | jogos, mcp |
| [gamelabs-mcp](tools/gamelabs-mcp) | Gera sprites com fundo transparente, animações e sprite sheets prontas para engine. | jogos, mcp |
| [gamedev-all-in-one-mcp](tools/gamedev-all-in-one-mcp) | MCP multi-engine de desenvolvimento de jogos. | jogos, mcp |
| [gstack-game](tools/gstack-game) | 27 skills do conceito ao build: design review, protótipo, game feel, QA e release. | jogos, skill |
| [claude-code-game-studios](tools/claude-code-game-studios) | Estúdio de jogos com 49 agentes e mais de 70 skills coordenados. | jogos, skill |
| [claude-code-game-development](tools/claude-code-game-development) | 22 plugins de jogos (Godot, Unity, Unreal, multiplayer, áudio, shaders) e manual de 80 capítulos. | jogos, plugin |
| [awesome-gamedev-agent-skills](tools/awesome-gamedev-agent-skills) | 74 skills de gamedev (Godot, Unity, Unreal, Phaser, three.js, Bevy, Roblox) com roteador por engine. | jogos, skill |
| [godogen](tools/godogen) | Desenvolvimento autônomo de jogos para Godot, Bevy e Babylon.js. | jogos, skill |
| [godot-claude-skills](tools/godot-claude-skills) | Skills do Claude para a engine Godot. | jogos, skill |
| [godot-mcp-coding-solo](tools/godot-mcp-coding-solo) | MCP MIT sem plugin: abre o editor, roda o projeto em debug e captura a saída via linha de comando. | jogos, godot, mcp |
| [gdai-mcp](tools/gdai-mcp) | MCP apontado como o mais polido para Godot: cenas, recursos, scripts, erros e logs do editor. | jogos, godot, mcp |
| [godot-ai-dlight](tools/godot-ai-dlight) | Plugin MIT que conecta Claude Code a um editor Godot ao vivo via MCP (Godot 4.5+). | jogos, godot, mcp |
| [godot-mcp-pro](tools/godot-mcp-pro) | 162 ferramentas MCP: cena, animação, 3D, física, partículas, áudio, shader, simulação de input, testes. | jogos, godot, mcp |
| [claude-godot-mcp](tools/claude-godot-mcp) | MCP com cerca de 170 ferramentas: nós, scripts, sinais, grupos, autoloads e shaders. | jogos, godot, mcp |
| [godot-forge](tools/godot-forge) | MCP com suporte preciso a GDScript, análise de projeto, docs e testes GUT/GdUnit4 headless. | jogos, godot, mcp |
| [godot-mcp-satelliteoflove](tools/godot-mcp-satelliteoflove) | MCP com 77 ferramentas em 15 categorias, incluindo testes headless e debug com breakpoints. | jogos, godot, mcp |
| [godot-mcp-mkdevkit](tools/godot-mcp-mkdevkit) | MCP open source para controlar o editor Godot 4 diretamente. | jogos, godot, mcp |
| [strayspark-godot-mcp](tools/strayspark-godot-mcp) | MCP comercial focado em edição de cenas e scripts do Godot 4.x, com ferramentas curadas. | jogos, godot, mcp |
| [godotprompter](tools/godotprompter) | 56 skills para Godot 4.x (GDScript e C#): arquitetura, física, shaders, UI, multiplayer, otimização. | jogos, godot, skill |
| [gd-agentic-skills](tools/gd-agentic-skills) | 99 skills e 27 blueprints de gênero com GDScript tipado para Godot 4.7+. | jogos, godot, skill |
| [godot-skills-vl4dt](tools/godot-skills-vl4dt) | 12 skills (GDScript, C#, física, animação, UI, rede, debug) cobrindo Godot 4.7. | jogos, godot, skill |
| [godot-agent-skills-qblab](tools/godot-agent-skills-qblab) | Edição segura de .tscn/.tres sem quebrar UIDs, guardas contra API do Godot 3 e hooks de verificação. | jogos, godot, skill |
| [godot-skill-shihab](tools/godot-skill-shihab) | Skill para GDScript 2.0 com tipagem estática estrita e guia de estilo oficial (Godot 4.3+). | jogos, godot, skill |
| [godot-claude-skills-alexmeckes](tools/godot-claude-skills-alexmeckes) | Coleção de skills do Claude para Godot. | jogos, godot, skill |
| [claude-godot-tools](tools/claude-godot-tools) | Plugins Claude Code: servidor de linguagem GDScript (LSP) e integração com gdUnit4. | jogos, godot, plugin |
| [ai-assistant-hub](tools/ai-assistant-hub) | Plugin open source (MIT) para usar LLMs dentro do editor (Ollama, Gemini, OpenRouter). | jogos, godot, editor |
| [golem-ai](tools/golem-ai) | Assistente no dock do editor com modelos locais ou na nuvem, incluindo Anthropic. | jogos, godot, editor |
| [fuku](tools/fuku) | Plugin que integra vários provedores de IA ao editor Godot. | jogos, godot, editor |
| [godot-ai-assistant-groq](tools/godot-ai-assistant-groq) | Assistente de GDScript, cenas e chat usando a API gratuita do Groq (LLaMA). | jogos, godot, editor |
| [flatten-for-llm](tools/flatten-for-llm) | Achata o projeto Godot em texto para colar num LLM. | jogos, godot, editor |
| [ziva](tools/ziva) | Agente de IA dentro do editor Godot 4.2+: árvore de cenas, sinais, GDScript/C#, sprites e TileMaps. | jogos, godot, editor |
| [summer-engine](tools/summer-engine) | Editor AI-native compatível com projetos .godot, com chat e acesso ao jogo rodando. | jogos, godot, editor |
| [godot-ai-guide](tools/godot-ai-guide) | Comparativos de ferramentas de IA para Godot (MCPs, plugins e assistentes). | jogos, godot, guia |
| [study-skill](tools/study-skill) | Tutor interativo com repetição espaçada FSRS-6, agentes de pesquisa, catálogo de livros e sessões adaptadas a TDAH. | aprendizado, skill |
| [maxlearn](tools/maxlearn) | Mod do Claude Code que transforma tópicos das suas conversas em aulas curtas e flashcards com FSRS. | aprendizado, plugin |
| [key-learning](tools/key-learning) | Tutor para qualquer área: explica por primeiros princípios, diagnostica nível de Bloom, cria plano e agenda revisões em markdown. | aprendizado, skill |
| [agent-tutor-skill](tools/agent-tutor-skill) | Tutor baseado em ciência cognitiva: ciclo de ensino, FSRS, quizzes sem dica e domínio por conceito. | aprendizado, skill |
| [study-skills-jacquard](tools/study-skills-jacquard) | 8 skills combináveis: flashcards, quizzes, checagem de conceitos, leitor de papers e mais. | aprendizado, skill |
| [claude-tutor-kirilxd](tools/claude-tutor-kirilxd) | Tutor com planos personalizados, quizzes adaptativos, repetição SM-2 e painel web. | aprendizado, plugin |
| [claude-tutor-kubilaiswf](tools/claude-tutor-kubilaiswf) | Tutor com syllabus, lições liberadas por domínio, provas e revisão espaçada; regras citadas da pesquisa. | aprendizado, plugin |
| [adhd-study-coach](tools/adhd-study-coach) | Agente de estudo para TDAH: blocos pequenos, repetição espaçada e reflexão Feynman. | aprendizado, skill |
| [learn-mode](tools/learn-mode) | Comando /learn que explica os conceitos do que o Claude acabou de fazer e salva notas. | aprendizado, skill |
| [learning-output-style](tools/learning-output-style) | Plugin oficial da Anthropic que faz o Claude pedir sua contribuição em pontos de decisão. | aprendizado, plugin |
| [codebase-to-course](tools/codebase-to-course) | Transforma um código em curso HTML interativo com quizzes e tradução para linguagem simples. | aprendizado, skill |
| [anki-mcp](tools/anki-mcp) | MCPs que criam, buscam e revisam flashcards no Anki via AnkiConnect. | aprendizado, mcp |
| [zotero-mcp](tools/zotero-mcp) | Conecta a biblioteca Zotero: busca em PDFs, resumos, citações e anotações. | aprendizado, mcp |
| [youtube-transcript-mcp](tools/youtube-transcript-mcp) | Lê transcrições do YouTube sem chave de API. | aprendizado, mcp |
| [obsidian-mcp](tools/obsidian-mcp) | MCPs para ler, buscar e editar notas de um cofre Obsidian. | aprendizado, mcp |
| [wikipedia-mcp](tools/wikipedia-mcp) | Busca artigos, resumos, referências e categorias da Wikipédia. | aprendizado, mcp |
| [wolfram-alpha-mcp](tools/wolfram-alpha-mcp) | Cálculos, equações, conversões e dados factuais via Wolfram Alpha. | aprendizado, mcp |
| [memory-knowledge-graph](tools/memory-knowledge-graph) | Memória oficial de referência do MCP: entidades, relações e observações em JSON local. | aprendizado, mcp |
| [mem0](tools/mem0) | Memória persistente para agentes (adicionar, buscar e atualizar memórias). | aprendizado, mcp |
| [kuliko-ai](tools/kuliko-ai) | Companheiro de estudo: matérias, documentos, recursos gerados e flashcards. | aprendizado, mcp |
| [learning-commons](tools/learning-commons) | Padrões, habilidades e progressões de aprendizagem do ensino básico (K-12, EUA). | aprendizado, mcp |
| [goodnotes](tools/goodnotes) | Gera documentos, diagramas Mermaid e imagens SVG no Goodnotes. | aprendizado, mcp |
