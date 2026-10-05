# Resultados da varredura de segurança

Rodada 1 (2026-10-05): os 22 MCPs de prioridade alta de `SEGURANCA.md`, mais o godot-mcp-coding-solo (tem CVE). Método: busca de CVEs e advisories públicos, verificação da origem e leitura do código quando o repositório é público. Nada foi instalado; scanners (snyk-agent-scan, mcpscan) ainda não foram rodados.

## Crítico: não usar como está

| MCP | Problema | O que fazer |
|---|---|---|
| [postgres-mcp](tools/postgres-mcp) | O servidor de referência (`@modelcontextprotocol/server-postgres`) foi arquivado sem correção. Um `COMMIT;` na query escapa do modo só-leitura e executa qualquer SQL ([Datadog](https://securitylabs.datadoghq.com/articles/mcp-vulnerability-case-study-SQL-injection-in-the-postgresql-mcp-server/)). | Trocar pelo fork corrigido `@zeddotdev/postgres-context-server` ≥ 0.1.4, ou pelo da AWS ≥ 1.1.7 ([advisory](https://github.com/awslabs/mcp/security/advisories/GHSA-fph8-pg5w-78fv)). Usar sempre um usuário do banco só com permissão de leitura. |
| [excel-mcp](tools/excel-mcp) | `haris-musa/excel-mcp-server`: path traversal com leitura e escrita de qualquer arquivo do computador. CVE-2026-40576 (≤ 0.1.7, modo HTTP/SSE) e CVE-2026-85661 (0.1.8, stdio sem `EXCEL_FILES_PATH`) ([OpenCVE](https://app.opencve.io/cve/CVE-2026-40576), [issue](https://github.com/haris-musa/excel-mcp-server/issues/115)). | Usar a versão mais nova, sempre com `EXCEL_FILES_PATH` definido e só em stdio. Ou usar a skill xlsx (anthropic-document-skills). |
| [bifrost-code-mode](tools/bifrost-code-mode) | Gateway com RCE sem autenticação quando a autenticação de gerenciamento está desligada: CVE-2026-86242 (< 2.0.0) e CVE-2026-90898, CVSS 9.8 (< 2.1.0). O atacante rouba as chaves de API de todos os provedores ([JFrog](https://research.jfrog.com/vulnerabilities/bifrost-is-vulnerable-to-unauthenticated-remote-code-execution-via-a-custom-plugin-http-path-on-dynamically-linked-builds-cve-2026-86242-jfsa-2026-001684572/), [The Hacker News](https://thehackernews.com/2026/09/critical-bifrost-ai-gateway-flaw-lets.html)). | Versão ≥ 2.1.0, autenticação de gerenciamento ligada e porta fechada para a rede. |
| [godot-mcp-coding-solo](tools/godot-mcp-coding-solo) | CVE-2026-25546 (< 0.1.1): `projectPath` vai direto para `exec()`, permitindo injetar comandos de shell ([issue](https://github.com/Coding-Solo/godot-mcp/issues/64)). | Versão ≥ 0.1.1. |

## Atenção: usar com cuidado

| MCP | Ponto | O que fazer |
|---|---|---|
| [n8n-mcp](tools/n8n-mcp) | O n8n em si teve vários RCE críticos em 2026 (CVE-2026-21858 "Ni8mare", CVSS 10, sem autenticação; CVE-2026-21877; CVE-2026-25049) ([Rapid7](https://www.rapid7.com/blog/post/etr-ni8mare-n8scape-flaws-multiple-critical-vulnerabilities-affecting-n8n/)). O `czlonkowski/n8n-mcp` ≤ 2.47.10 grava tokens nos logs quando roda em modo HTTP ([advisory](https://github.com/czlonkowski/n8n-mcp/security/advisories/GHSA-pfm2-2mhg-8wpx)). | Manter o n8n atualizado; n8n-mcp ≥ 2.47.11 ou em stdio. |
| [chrome-devtools-mcp](tools/chrome-devtools-mcp) | É oficial do Google. CVE-2026-53765 e CVE-2026-53766 (médias, CVSS 6.1): symlinks escapam da pasta permitida ([advisories](https://github.com/ChromeDevTools/chrome-devtools-mcp/security/advisories)). O agente vê tudo o que estiver aberto no navegador. | Versão ≥ 1.1.0, com um perfil de navegador separado (sem login em contas pessoais). |
| [davinci-resolve-mcp](tools/davinci-resolve-mcp) | O repositório `hemichaeli/davinci-resolve-mcp` citado pelo glama não existe mais no GitHub, então a origem não pode ser verificada. | Trocar por uma alternativa com código público (ex.: `samuelgursky/davinci-resolve-mcp`) e revisá-la antes. |
| [discord-mcp](tools/discord-mcp) | Repositório não identificado. Um bot com muitas permissões e sob prompt injection pode vazar mensagens e fazer DMs ou moderação em massa ([AgentSeal](https://agentseal.org/mcp/pasympa-discord-mcp): 58/100). | Escolher um repositório concreto e dar ao bot só as permissões mínimas. |
| [gdai-mcp](tools/gdai-mcp) | Escuta só em 127.0.0.1 e restringe arquivos a `res://`, mas tem `execute_editor_command` ([docs](https://gdaimcp.com/docs/configuration)). | Ok para uso local; aprovar manualmente os comandos. |
| [godot-ai-dlight](tools/godot-ai-dlight) | Repositório [hi-godot/godot-ai](https://github.com/hi-godot/godot-ai): autenticação nas conexões locais, apenas loopback. Envia telemetria anônima. | Ok; para desligar a telemetria, `GODOT_AI_DISABLE_TELEMETRY=true`. Atenção: existem cópias do repositório com outros autores. |
| [meta-ads-mcp](tools/meta-ads-mcp) | O oficial (`mcp.facebook.com/ads`) está em beta e pode alterar campanhas e orçamentos. A alternativa comunitária `pipeboard-co/meta-ads-mcp` < 1.0.115 tinha um bypass de autenticação (CVE-2026-54547, [advisory](https://advisories.gitlab.com/pypi/meta-ads-mcp/CVE-2026-54547/)). | Usar o oficial; conectar só a conta de anúncios necessária. |
| [make-mcp](tools/make-mcp) | Oficial. Os escopos de gerenciamento podem alterar cenários, conexões e webhooks ([docs](https://developers.make.com/mcp-server)). | Gerar o token só com os escopos de execução de cenários. |
| [roblox-studio-mcp](tools/roblox-studio-mcp) | Oficial, mas descontinuado; a Roblox recomenda o MCP embutido no Studio ([repo](https://github.com/Roblox/studio-rust-mcp-server)). | Usar o MCP embutido no Roblox Studio. |

## Sem problema conhecido

- **[godot-forge](tools/godot-forge)**: código lido; usa `spawn` sem shell, não faz chamadas de rede e tem uma única dependência (o SDK do MCP).
- **[xero-mcp](tools/xero-mcp)**: oficial da Xero; o token fica salvo em arquivo com permissão 0600.
- **[upload-post-mcp](tools/upload-post-mcp)**, **[buffer-mcp](tools/buffer-mcp)**: oficiais do fornecedor (remotos). Risco = publicar em todas as redes conectadas. Revisar os posts antes de publicar.
- **[bigquery-mcp](tools/bigquery-mcp)**: gerenciado pelo Google; restringir o IAM a leitura e definir um limite de custo.
- **[browserbase-mcp](tools/browserbase-mcp)**: oficial, sem CVE encontrado; o navegador roda na nuvem do fornecedor.
- **[google-drive-mcp](tools/google-drive-mcp)**: conector oficial do registro do Claude. Revisar a permissão OAuth pedida.
- **[jumper](tools/jumper)**: comercial; MCP local e análise de vídeo feita no próprio computador ([FAQ](https://docs.getjumper.io/faq)).

## Não verificáveis (comerciais, sem código público)

- **[strayspark-godot-mcp](tools/strayspark-godot-mcp)**, **[segmentstream](tools/segmentstream)**: pagos, sem repositório nem advisories. Só usar se forem necessários, e com dados de teste primeiro.

## Rodada 2: tema Godot (2026-10-05)

26 ferramentas. Código lido em 17 repositórios públicos, com busca por execução de comandos, portas abertas na rede, autenticação, chamadas externas, hooks e instruções escondidas (incluindo unicode invisível). Nenhuma instrução maliciosa ou caractere oculto foi encontrado. Nada foi instalado nem testado em execução.

### 🔴 Corrigir antes de usar

| Ferramenta | Problema | O que fazer |
|---|---|---|
| [claude-godot-mcp](tools/claude-godot-mcp) | O plugin abre um servidor HTTP em `127.0.0.1:3571` **sem autenticação** e com `Access-Control-Allow-Origin: *`. Qualquer site aberto no navegador pode chamar a API, inclusive `/api/file/write_text`, que grava arquivos em `res://`. Um script `@tool` gravado assim roda no editor. (Análise de código; não testado em execução.) | Não usar enquanto não tiver token e CORS restrito. Prefira godot-ai-dlight ou godot-mcp-satelliteoflove. |
| [godot-claude-skills](tools/godot-claude-skills) | O addon de testes PlayGodot (`example-project/addons/playgodot/server.gd`) chama `TCPServer.listen(porta)` sem endereço. No Godot, o padrão é escutar em **todas as interfaces**, então qualquer pessoa na mesma rede (Wi-Fi da escola, por exemplo) pode controlar o jogo e chamar métodos. Os scripts de CI usam `--dangerously-skip-permissions`. | Se usar o PlayGodot, trocar para `listen(porta, "127.0.0.1")`. Não copiar o modo sem permissões para uso local. |

### 🟡 Atenção

| Ferramenta | Ponto |
|---|---|
| [godot-mcp-coding-solo](tools/godot-mcp-coding-solo) | A CVE-2026-25546 está corrigida no código atual (`execFile` com lista de argumentos). Use a versão ≥ 0.1.1. |
| [godot-mcp-pro](tools/godot-mcp-pro) | Pago; o servidor MCP não está no repositório (só o addon). Traz `settings.local.permissive.json` com `Bash(*)` liberado e só uma lista de bloqueios. **Não use esse arquivo**; use o `settings.local.json` padrão. |
| [godot-mcp-mkdevkit](tools/godot-mcp-mkdevkit) | Escuta só em `127.0.0.1`, mas não tem autenticação. Tem `execute_editor_script` (executa expressões no editor) e `OS.execute` para adb (Android). Aprovar manualmente essas ferramentas. |
| [godot-mcp-satelliteoflove](tools/godot-mcp-satelliteoflove) | Bem feito: escuta em localhost por padrão e valida o endereço. A ferramenta `exec` roda GDScript no jogo, protegida só por uma lista de funções proibidas (`OS.execute` etc.), o que pode ser contornado. |
| [godot-ai-dlight](tools/godot-ai-dlight) | O mais seguro dos MCPs: autenticação nas duas conexões locais, apenas loopback, rede externa só com `--allow-host`. Tem `game_eval` (executa código no jogo) e telemetria anônima (`GODOT_AI_DISABLE_TELEMETRY=true` desliga). |
| [godot-mcp](tools/godot-mcp) | `tomyud1`: escuta em `127.0.0.1`; `execSync` só recebe o número da porta (ok). |
| [gdai-mcp](tools/gdai-mcp) | **Código fechado**: o repositório só tem a documentação e um projeto de exemplo. Pela documentação, escuta só em 127.0.0.1. Não dá para auditar. |
| [ai-assistant-hub](tools/ai-assistant-hub) | Envia estatísticas de uso (versão, versão do Godot, APIs usadas) para `abacus.jasoncameron.dev` sem opção de desligar. Monta GDScript concatenando o nome de classe vindo da IA (`"static func eval(): return " + classe`), o que é uma injeção de código possível. |
| [claude-godot-tools](tools/claude-godot-tools) | O hook `PreToolUse` baixa binários do GitHub Releases **sem conferir checksum**. A origem é confiável (GDQuest e o próprio autor), mas não há verificação de integridade. |
| [godotprompter](tools/godotprompter), [godot-agent-skills-qblab](tools/godot-agent-skills-qblab) | Instalam hooks (`SessionStart`, `PreToolUse`). Revisei: só leem arquivos locais e bloqueiam edições estruturais em `.tscn`. Ok. |

### 🟢 Sem problema encontrado

[godot-forge](tools/godot-forge) (`spawn` sem shell, só stdio, uma dependência) · skills só de texto: [gd-agentic-skills](tools/gd-agentic-skills), [godot-claude-skills-alexmeckes](tools/godot-claude-skills-alexmeckes), [godot-skill-shihab](tools/godot-skill-shihab), [godot-skills-vl4dt](tools/godot-skills-vl4dt) (o bridge MCP incluído conecta em localhost).

### ⚪ Não auditáveis (sem código público ou comerciais)

[strayspark-godot-mcp](tools/strayspark-godot-mcp), [ziva](tools/ziva), [summer-engine](tools/summer-engine), [godot-ai-assistant-groq](tools/godot-ai-assistant-groq), [golem-ai](tools/golem-ai), [fuku](tools/fuku), [flatten-for-llm](tools/flatten-for-llm). [godot-ai-guide](tools/godot-ai-guide) é só um guia.

### Recomendação

Para usar em aula ou em casa: **godot-ai-dlight** (mais seguro) ou **godot-mcp-satelliteoflove**, com as skills **godotprompter** ou **godot-agent-skills-qblab**. Evitar o claude-godot-mcp.

## Próxima rodada

1. Instalar `snyk-agent-scan` e rodar nos MCPs que forem de fato instalados (procura instruções maliciosas nas descrições das ferramentas).
2. Revisar os 52 MCPs de prioridade média de `SEGURANCA.md`.
