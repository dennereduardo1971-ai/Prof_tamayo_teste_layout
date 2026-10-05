"""Gera INDEX.md a partir do frontmatter de tools/*/README.md. Uso: python3 scripts/build_index.py"""
import os, re

SECOES = {  # tema: (título, recomendação "Comece por")
    'pesquisa': ('Pesquisa', 'parallel-search + claude-deep-research-skill'),
    'tokens': ('Economia de tokens', 'rtk + context-mode + token-economy-guide'),
    'design': ('Design', 'figma-mcp + ui-ux-pro-max'),
    'jogos': ('Jogos', 'MCP da sua engine + ludo-mcp (assets)'),
    'godot': ('Godot', 'godot-ai-dlight ou gdai-mcp + godotprompter + godot-agent-skills-qblab'),
    'aprendizado': ('Aprendizado', 'key-learning ou study-skill + anki-mcp + youtube-transcript-mcp'),
    'midia': ('Imagem e vídeo', 'kinocut (vídeo) + mcp-image (imagem) + claude-remotion-skill'),
    'marketing': ('Marketing', 'marketingskills + ahrefs-mcp ou semrush-mcp + google-analytics-mcp'),
    'social': ('Redes sociais', 'postiz ou buffer-mcp (agendar) + MCP da rede principal + social-calendar-skill + octolens (escuta)'),
    'automacao': ('Automação e produtividade', 'zapier-mcp ou n8n-mcp + gmail-mcp + google-calendar-mcp + notion-mcp'),
    'dev': ('Desenvolvimento', 'github-mcp + context7 + playwright-mcp + supabase-mcp ou postgres-mcp + sentry-mcp'),
    'navegador': ('Navegador e scraping', 'playwright-mcp (automatizar) + chrome-devtools-mcp (depurar)'),
    'audio': ('Áudio, voz e música', 'elevenlabs-official-mcp + whisper-mcp'),
    'dados': ('Dados e planilhas', 'postgres-mcp ou bigquery-mcp + google-sheets-mcp + metabase-mcp'),
    'documentos': ('Documentos e escrita', 'anthropic-document-skills'),
    'agentes': ('Agentes e orquestração', 'awesome-claude-code-subagents + workflow-orchestration'),
    'ensino': ('Ensino (professor)', 'claude-edu-plugins + teacher-skills-guide'),
    'ecommerce': ('E-commerce', 'shopify-mcp ou ecommerce-mcp-server (Mercado Livre) + stripe-mcp'),
    'financas': ('Finanças', 'quickbooks-mcp ou xero-mcp + stripe-mcp'),
    'seguranca': ('Segurança', 'snyk-agent-scan + /security-review do Claude Code'),
}

rows = {k: [] for k in SECOES}
for t in sorted(os.listdir('tools')):
    if t.startswith('_'):
        continue
    fm = re.match(r'---\n(.*?)\n---', open(f'tools/{t}/README.md').read(), re.S).group(1)
    d = dict(re.match(r'([\w-]+): (.*)', l).groups() for l in fm.splitlines())
    desc = d['description'].strip('"')
    rows[d['tema']].append(f"| [{t}](tools/{t}) | {d['tipo']} | {desc} | {d['status']} |")

out = ['# Índice de ferramentas', '',
       'Busque aqui primeiro. Detalhes, `alternativas` e `combina-com` ficam no frontmatter de cada `tools/<nome>/README.md`.',
       'Gerado por `scripts/build_index.py`; não edite à mão.', '',
       'Seções: ' + ' · '.join(f"[{n}](#{n.lower().replace(' ', '-')})" for n, _ in SECOES.values()), '']
for k, (nome, rec) in SECOES.items():
    out += [f'## {nome}', '', f'**Comece por:** {rec}', '',
            '| Ferramenta | Tipo | Descrição | Status |', '|---|---|---|---|'] + rows[k] + ['']
open('INDEX.md', 'w').write('\n'.join(out))
print({k: len(v) for k, v in rows.items()})
