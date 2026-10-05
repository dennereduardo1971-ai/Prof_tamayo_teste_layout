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
