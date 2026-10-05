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
