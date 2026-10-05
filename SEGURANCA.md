# Varredura de segurança dos MCPs

Gerado por `scripts/security_inventory.py`; não edite à mão. Ao revisar um MCP, registre o resultado no `tools/<nome>/README.md` dele.

Total: 149 MCPs · prioridade alta 22, média 52, baixa 75.

## Grupos por origem

- **A** (38): Conector oficial do registro do Claude: revisar escopos OAuth pedidos, o que a ferramenta consegue escrever/apagar e política de dados do fornecedor.
- **B** (48): Repositório no GitHub: clonar e rodar snyk-agent-scan/mcpscan (tool poisoning, instruções escondidas), `npm audit`/`pip-audit`, grep por exec/eval/subprocess/rede, conferir manutenção e licença.
- **C** (63): Só página de diretório/site: achar o repositório ou fornecedor real; sem código público, tratar como não verificável e preferir alternativa.

## O que procurar em todos

- Tool poisoning / prompt injection nas descrições das ferramentas.
- Permissões demais (escrita, exclusão, envio) além do necessário.
- Segredos: chave de API em texto puro na config, tokens com escopo amplo.
- Execução de código ou shell sem confirmação; acesso amplo ao sistema de arquivos.
- Envio de dados para terceiros (telemetria, servidores não documentados).
- Dependências vulneráveis, projeto abandonado, autor desconhecido, nome imitando projeto oficial.

## Ordem de revisão

Prioridade: **alta** = acessa dados sensíveis e executa localmente, ou tem acesso e origem não verificável; **média** = um dos dois; **baixa** = nenhum.

| Prioridade | Grupo | MCP | Tema | Acesso | Fonte |
|---|---|---|---|---|---|
| alta | A | [google-drive-mcp](tools/google-drive-mcp) | automacao | dados, exec | Registro de conectores do Claude (claude.ai) |
| alta | A | [n8n-mcp](tools/n8n-mcp) | automacao | dados, exec | Registro de conectores do Claude (claude.ai) |
| alta | C | [bifrost-code-mode](tools/bifrost-code-mode) | tokens | exec | https://www.getmaxim.ai/articles/how-to-reduce-mcp-token-costs-for-claude-code-at-scale/ |
| alta | C | [bigquery-mcp](tools/bigquery-mcp) | dados | dados | https://heyclau.de/entry/mcp/bigquery-mcp-server |
| alta | C | [browserbase-mcp](tools/browserbase-mcp) | navegador | exec | https://www.webfuse.com/blog/the-top-5-best-mcp-servers-for-ai-agent-browser-automation |
| alta | C | [buffer-mcp](tools/buffer-mcp) | social | dados | https://mcpmarket.com/server/buffer |
| alta | C | [chrome-devtools-mcp](tools/chrome-devtools-mcp) | navegador | exec | https://mcp.directory/blog/chrome-devtools-mcp-vs-playwright-mcp-2026 |
| alta | C | [davinci-resolve-mcp](tools/davinci-resolve-mcp) | midia | exec | https://glama.ai/mcp/servers/hemichaeli/davinci-resolve-mcp |
| alta | C | [discord-mcp](tools/discord-mcp) | social | dados | https://heyclau.de/compare/messaging-mcp-servers |
| alta | C | [excel-mcp](tools/excel-mcp) | dados | exec | https://www.vibestack.in/blog/mcp-servers-data-analysis-2026 |
| alta | C | [gdai-mcp](tools/gdai-mcp) | godot | exec | https://gdaimcp.com/ |
| alta | C | [godot-ai-dlight](tools/godot-ai-dlight) | godot | exec | https://store.godotengine.org/asset/dlight/godot-ai/ |
| alta | C | [godot-forge](tools/godot-forge) | godot | exec | https://glama.ai/mcp/servers/gregario/godot-forge |
| alta | C | [jumper](tools/jumper) | midia | exec | https://getjumper.io/ai-agents |
| alta | C | [make-mcp](tools/make-mcp) | automacao | dados | https://fast.io/resources/best-mcp-servers-automation/ |
| alta | C | [meta-ads-mcp](tools/meta-ads-mcp) | marketing | dados | https://ferrerponseti.com/en/blog/official-meta-ads-mcp-claude/ |
| alta | C | [postgres-mcp](tools/postgres-mcp) | dev | dados, exec | https://www.vibestack.in/blog/mcp-servers-data-analysis-2026 |
| alta | C | [roblox-studio-mcp](tools/roblox-studio-mcp) | jogos | exec | https://devforum.roblox.com/t/introducing-the-open-source-studio-mcp-server/3649365 |
| alta | C | [segmentstream](tools/segmentstream) | marketing | dados | https://segmentstream.com/blog/articles/best-mcp-servers-for-claude |
| alta | C | [strayspark-godot-mcp](tools/strayspark-godot-mcp) | godot | exec | https://www.strayspark.studio/blog/godot-mcp-setup-claude-code-2026 |
| alta | C | [upload-post-mcp](tools/upload-post-mcp) | social | dados | https://www.upload-post.com/mcp/ |
| alta | C | [xero-mcp](tools/xero-mcp) | financas | dados | https://top-mcps.com/mcp/xero |
| média | A | [adspirer](tools/adspirer) | marketing | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [adwhispr](tools/adwhispr) | marketing | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [aftership-tiktok-shop](tools/aftership-tiktok-shop) | ecommerce | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [gmail-mcp](tools/gmail-mcp) | automacao | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [google-calendar-mcp](tools/google-calendar-mcp) | automacao | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [hubspot-mcp](tools/hubspot-mcp) | marketing | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [linear-mcp](tools/linear-mcp) | automacao | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [mailchimp-mcp](tools/mailchimp-mcp) | marketing | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [mem0](tools/mem0) | aprendizado | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [motion-creative-analytics](tools/motion-creative-analytics) | marketing | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [notion-mcp](tools/notion-mcp) | automacao | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [quickbooks-mcp](tools/quickbooks-mcp) | financas | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [sentry-mcp](tools/sentry-mcp) | dev | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [shopify-mcp](tools/shopify-mcp) | ecommerce | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [stripe-mcp](tools/stripe-mcp) | ecommerce | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [supabase-mcp](tools/supabase-mcp) | dev | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [supermetrics](tools/supermetrics) | marketing | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [tiktok-for-business](tools/tiktok-for-business) | social | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [tinyfish](tools/tinyfish) | navegador | exec | Registro de conectores do Claude (claude.ai) |
| média | A | [typefully](tools/typefully) | marketing | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [vidiq](tools/vidiq) | social | dados | Registro de conectores do Claude (claude.ai) |
| média | A | [zapier-mcp](tools/zapier-mcp) | automacao | dados | Registro de conectores do Claude (claude.ai) |
| média | B | [blender-mcp](tools/blender-mcp) | jogos | exec | https://github.com/ahujasid/mcp-for-blender |
| média | B | [claude-godot-mcp](tools/claude-godot-mcp) | godot | exec | https://github.com/PiMPStudios/Claude-GoDot-MCP |
| média | B | [datalikers-mcp](tools/datalikers-mcp) | social | dados | https://github.com/subzeroid/datalikers-mcp |
| média | B | [ffmpeg-mcp-server](tools/ffmpeg-mcp-server) | midia | exec | https://github.com/beambuilder/ffmpeg-mcp-server |
| média | B | [gimp-mcp](tools/gimp-mcp) | midia | exec | https://github.com/maorcc/gimp-mcp |
| média | B | [github-mcp](tools/github-mcp) | dev | dados | https://github.com/github/github-mcp-server |
| média | B | [godot-mcp](tools/godot-mcp) | godot | exec | https://github.com/tomyud1/godot-mcp |
| média | B | [godot-mcp-coding-solo](tools/godot-mcp-coding-solo) | godot | exec | https://github.com/Coding-Solo/godot-mcp |
| média | B | [godot-mcp-mkdevkit](tools/godot-mcp-mkdevkit) | godot | exec | https://github.com/mkdevkit/godot-mcp |
| média | B | [godot-mcp-pro](tools/godot-mcp-pro) | godot | exec | https://github.com/youichi-uda/godot-mcp-pro |
| média | B | [godot-mcp-satelliteoflove](tools/godot-mcp-satelliteoflove) | godot | exec | https://github.com/satelliteoflove/godot-mcp/blob/main/docs/claude-code-setup.md |
| média | B | [google-ads-mcp](tools/google-ads-mcp) | marketing | dados | https://github.com/googleads/google-ads-mcp |
| média | B | [google-analytics-mcp](tools/google-analytics-mcp) | marketing | dados | https://github.com/googleanalytics/google-analytics-mcp |
| média | B | [hasdata-social](tools/hasdata-social) | social | dados | https://github.com/HasData/tiktok-mcp |
| média | B | [insightsocial](tools/insightsocial) | social | dados | https://github.com/insightsocial/cli |
| média | B | [instagram-mcp](tools/instagram-mcp) | social | dados | https://github.com/postoncehq/instagram-mcp |
| média | B | [kinocut](tools/kinocut) | midia | exec | https://github.com/KyaniteLabs/kinocut |
| média | B | [krita-mcp](tools/krita-mcp) | midia | exec | https://github.com/SanSaSane/krita-mcp |
| média | B | [linkedin-mcp](tools/linkedin-mcp) | social | dados | https://github.com/stickerdaniel/linkedin-mcp-server |
| média | B | [mcp-unity](tools/mcp-unity) | jogos | exec | https://github.com/CoderGamester/mcp-unity |
| média | B | [playwright-mcp](tools/playwright-mcp) | navegador | exec | https://github.com/microsoft/playwright-mcp |
| média | B | [posteverywhere-mcp](tools/posteverywhere-mcp) | social | dados | https://github.com/posteverywhere/mcp |
| média | B | [ryze-ads-mcp](tools/ryze-ads-mcp) | marketing | dados | https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp |
| média | B | [telegram-mcp](tools/telegram-mcp) | social | dados | https://github.com/chigwell/telegram-mcp |
| média | B | [trends-mcp](tools/trends-mcp) | social | dados | https://github.com/rugvedp/Trends-MCP |
| média | B | [unreal-mcp](tools/unreal-mcp) | jogos | exec | https://github.com/chongdashu/unreal-mcp |
| média | B | [video-audio-mcp](tools/video-audio-mcp) | midia | exec | https://github.com/misbahsy/video-audio-mcp |
| média | B | [video-transcriber-mcp](tools/video-transcriber-mcp) | audio | dados | https://github.com/nhatvu148/video-transcriber-mcp |
| média | B | [whatsapp-mcp](tools/whatsapp-mcp) | social | dados | https://github.com/Akram-Atassi/claude-whatsapp-mcp |
| média | B | [youtube-mcp](tools/youtube-mcp) | social | dados | https://github.com/mrchevyceleb/youtube-mcp |
| baixa | A | [adobe-marketing-agent](tools/adobe-marketing-agent) | marketing | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [ahrefs-mcp](tools/ahrefs-mcp) | marketing | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [cloudinary-mcp](tools/cloudinary-mcp) | midia | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [elevenlabs-mcp](tools/elevenlabs-mcp) | midia | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [goodnotes](tools/goodnotes) | aprendizado | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [klaviyo-mcp](tools/klaviyo-mcp) | marketing | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [kuliko-ai](tools/kuliko-ai) | aprendizado | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [learning-commons](tools/learning-commons) | aprendizado | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [metricool](tools/metricool) | marketing | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [openrush](tools/openrush) | marketing | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [openseo](tools/openseo) | marketing | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [orshot](tools/orshot) | midia | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [semrush-mcp](tools/semrush-mcp) | marketing | - | Registro de conectores do Claude (claude.ai) |
| baixa | A | [unsplash-mcp](tools/unsplash-mcp) | midia | - | Registro de conectores do Claude (claude.ai) |
| baixa | B | [anki-mcp](tools/anki-mcp) | aprendizado | - | https://github.com/dhkim0124/anki-mcp-server |
| baixa | B | [bluesky-mcp](tools/bluesky-mcp) | social | - | https://github.com/morinokami/mcp-server-bluesky |
| baixa | B | [context7](tools/context7) | pesquisa | - | https://github.com/upstash/context7 |
| baixa | B | [ecommerce-mcp-server](tools/ecommerce-mcp-server) | ecommerce | - | https://github.com/HelpCode-ai/ecommerce-mcp-server |
| baixa | B | [ludo-mcp](tools/ludo-mcp) | jogos | - | https://github.com/Ludo-AI/ludo-mcp |
| baixa | B | [mcp-image](tools/mcp-image) | midia | - | https://github.com/shinpr/mcp-image |
| baixa | B | [obsidian-mcp](tools/obsidian-mcp) | aprendizado | - | https://github.com/iansinnott/obsidian-claude-code-mcp |
| baixa | B | [photoshop-mcp](tools/photoshop-mcp) | midia | - | https://github.com/alisaitteke/photoshop-mcp |
| baixa | B | [postiz](tools/postiz) | social | - | https://github.com/gitroomhq/postiz-app |
| baixa | B | [reddit-mcp-buddy](tools/reddit-mcp-buddy) | social | - | https://github.com/karanb192/reddit-mcp-buddy |
| baixa | B | [suno-mcp](tools/suno-mcp) | audio | - | https://github.com/AceDataCloud/SunoMCP |
| baixa | B | [token-reducer](tools/token-reducer) | tokens | - | https://github.com/madhan230205/token-reducer |
| baixa | B | [whisper-mcp](tools/whisper-mcp) | audio | - | https://github.com/jwulff/whisper-mcp |
| baixa | B | [wikipedia-mcp](tools/wikipedia-mcp) | aprendizado | - | https://github.com/Rudra-ravi/wikipedia-mcp |
| baixa | B | [wolfram-alpha-mcp](tools/wolfram-alpha-mcp) | aprendizado | - | https://github.com/cnosuke/mcp-wolfram-alpha |
| baixa | B | [x-mcp](tools/x-mcp) | social | - | https://github.com/postoncehq/x-mcp |
| baixa | B | [youtube-transcript-mcp](tools/youtube-transcript-mcp) | aprendizado | - | https://github.com/zxl777/youtube-transcript-mcp |
| baixa | B | [zotero-mcp](tools/zotero-mcp) | aprendizado | - | https://github.com/54yyyu/zotero-mcp |
| baixa | C | [adobe-mcp](tools/adobe-mcp) | design | - | https://www.toools.design/blog-posts/best-mcp-servers-for-designers |
| baixa | C | [aidesigner-mcp](tools/aidesigner-mcp) | design | - | https://www.aidesigner.ai/blog/best-mcp-servers |
| baixa | C | [ayrshare-mcp](tools/ayrshare-mcp) | social | - | https://www.oneupapp.io/blog/7-best-social-media-schedulers-with-an-mcp-server-2026 |
| baixa | C | [brave-search](tools/brave-search) | pesquisa | - | https://brave.com/search/api/ |
| baixa | C | [canva-mcp](tools/canva-mcp) | design | - | https://mcp.directory/blog/best-mcp-servers-for-design-2026 |
| baixa | C | [context-mode](tools/context-mode) | tokens | - | https://glama.ai/mcp/servers/@mksglu/claude-context-mode/blob/627bd7c8567d00ddbff5fba860d9f00e2af53916/README.md |
| baixa | C | [creatomate](tools/creatomate) | midia | - | https://www.wireflow.ai/blog/best-mcp-server-for-video-editing-tools-in-2026 |
| baixa | C | [doop-design](tools/doop-design) | design | - | https://doop.design/blog/claude-code-design-tools |
| baixa | C | [editassist](tools/editassist) | midia | - | https://editassist.dev/integrations |
| baixa | C | [elevenlabs-official-mcp](tools/elevenlabs-official-mcp) | audio | - | https://elevenlabs.io/blog/introducing-voice-music-image-and-video-generation-in-the-elevenlabs-mcp |
| baixa | C | [embedsocial](tools/embedsocial) | social | - | https://mcpservers.org/servers/embedsocial-mcp |
| baixa | C | [exa-search](tools/exa-search) | pesquisa | - | https://exa.ai |
| baixa | C | [fal-ai-mcp](tools/fal-ai-mcp) | midia | - | https://www.wireflow.ai/blog/best-mcp-server-for-video-editing-tools-in-2026 |
| baixa | C | [figma-mcp](tools/figma-mcp) | design | - | https://mcp.directory/blog/best-mcp-servers-for-design-2026 |
| baixa | C | [firecrawl-research](tools/firecrawl-research) | pesquisa | - | https://www.firecrawl.dev/blog/best-web-search-mcp |
| baixa | C | [gamedev-all-in-one-mcp](tools/gamedev-all-in-one-mcp) | jogos | - | https://mcpservers.org/servers/dmae97/gamedev-all-in-one-mcp |
| baixa | C | [gamelabs-mcp](tools/gamelabs-mcp) | jogos | - | https://gamelabstudio.co/mcp |
| baixa | C | [google-sheets-mcp](tools/google-sheets-mcp) | dados | - | https://www.vibestack.in/blog/mcp-servers-data-analysis-2026 |
| baixa | C | [image-generation-mcp](tools/image-generation-mcp) | midia | - | https://crossaitools.com/mcp/pvliesdonk/image-generation-mcp |
| baixa | C | [imagineart-mcp](tools/imagineart-mcp) | midia | - | https://www.imagine.art/blogs/best-mcp-servers-claude-code-image-prompting |
| baixa | C | [intenthunter](tools/intenthunter) | social | - | https://intenthunter.com/mcp |
| baixa | C | [magic-patterns-mcp](tools/magic-patterns-mcp) | design | - | https://www.magicpatterns.com/blog/aeo/blog/listicle/what-are-the-best-mcp-servers-for-ui-design-and-prototyping-c97b12 |
| baixa | C | [memory-knowledge-graph](tools/memory-knowledge-graph) | aprendizado | - | https://www.claudedirectory.org/mcp-servers/topic/knowledge-memory |
| baixa | C | [metabase-mcp](tools/metabase-mcp) | dados | - | https://www.inkoop.io/blog/bi-tools-with-mcp-support-in-2026/ |
| baixa | C | [moda-mcp](tools/moda-mcp) | design | - | https://moda.app/blog/ai-agent-design-mcp-tools |
| baixa | C | [octolens](tools/octolens) | social | - | https://octolens.com/mcp |
| baixa | C | [parallel-search](tools/parallel-search) | pesquisa | - | https://parallel.ai/articles/best-mcp-servers-for-claude-code |
| baixa | C | [perplexity-mcp](tools/perplexity-mcp) | pesquisa | - | https://www.perplexity.ai |
| baixa | C | [phaser-game-agent-mcp](tools/phaser-game-agent-mcp) | jogos | - | https://phaser.io/agent/mcp |
| baixa | C | [pipedream-mcp](tools/pipedream-mcp) | automacao | - | https://latenode.com/blog/mcp-servers-for-automation |
| baixa | C | [postsyncer-mcp](tools/postsyncer-mcp) | social | - | https://mcpservers.org/servers/postsyncer/claude-plugin |
| baixa | C | [publer-mcp](tools/publer-mcp) | social | - | https://glama.ai/mcp/servers/alexkess/publer-mcp-server |
| baixa | C | [reap](tools/reap) | midia | - | https://www.wireflow.ai/blog/best-mcp-server-for-video-editing-tools-in-2026 |
| baixa | C | [recraft-mcp](tools/recraft-mcp) | midia | - | https://www.recraft.ai/blog/how-to-generate-images-in-claude |
| baixa | C | [semantic-cache-mcp](tools/semantic-cache-mcp) | tokens | - | https://glama.ai/mcp/servers/CoderDayton/semantic-cache-mcp |
| baixa | C | [shotstack](tools/shotstack) | midia | - | https://www.wireflow.ai/blog/best-mcp-server-for-video-editing-tools-in-2026 |
| baixa | C | [social-listening-mcp](tools/social-listening-mcp) | social | - | https://glama.ai/mcp/servers/@fred-em/social-listening/inspect |
| baixa | C | [socialclaw](tools/socialclaw) | marketing | - | https://getsocialclaw.com/blog/best-claude-mcp-servers-for-marketing |
| baixa | C | [spritecook-mcp](tools/spritecook-mcp) | jogos | - | https://mcpservers.org/servers/spritecook/spritecook-mcp |
| baixa | C | [superset-mcp](tools/superset-mcp) | dados | - | https://www.inkoop.io/blog/bi-tools-with-mcp-support-in-2026/ |
| baixa | C | [tavily-search](tools/tavily-search) | pesquisa | - | https://tavily.com |
| baixa | C | [wireflow](tools/wireflow) | midia | - | https://www.wireflow.ai/blog/best-mcp-server-for-video-editing-tools-in-2026 |
| baixa | C | [woocommerce-mcp](tools/woocommerce-mcp) | ecommerce | - | https://mention.network/learn/best-mcp-servers-for-shopify-and-woocommerce/ |
