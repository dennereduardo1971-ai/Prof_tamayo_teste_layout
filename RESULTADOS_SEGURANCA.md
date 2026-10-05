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

## Próxima rodada

1. Instalar `snyk-agent-scan` e rodar nos MCPs que forem de fato instalados (procura instruções maliciosas nas descrições das ferramentas).
2. Revisar os 52 MCPs de prioridade média de `SEGURANCA.md`.
