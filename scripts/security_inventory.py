"""Gera SEGURANCA.md: plano da varredura de segurança dos MCPs. Uso: python3 scripts/security_inventory.py"""
import os, re

# Palavras no nome/descrição que indicam o tipo de acesso (define a prioridade).
DADOS_SENSIVEIS = r'gmail|mail|drive|calendar|notion|hubspot|stripe|quickbooks|xero|shopify|supabase|postgres|bigquery|github|linear|sentry|slack|discord|whatsapp|telegram|instagram|linkedin|facebook|tiktok|\bads\b|analytics|financ|pagamento|banco|\bcrm\b|mem0|zapier|n8n|make-mcp'
EXEC_LOCAL = r'blender|godot|unity|unreal|roblox|gimp|krita|ffmpeg|davinci|chrome|playwright|browser|navegador|shell|terminal|filesystem|arquivo|excel|\bexec|execut'

PASSOS = {
    'A': 'Conector oficial do registro do Claude: revisar escopos OAuth pedidos, o que a ferramenta consegue escrever/apagar e política de dados do fornecedor.',
    'B': 'Repositório no GitHub: clonar e rodar snyk-agent-scan/mcpscan (tool poisoning, instruções escondidas), `npm audit`/`pip-audit`, grep por exec/eval/subprocess/rede, conferir manutenção e licença.',
    'C': 'Só página de diretório/site: achar o repositório ou fornecedor real; sem código público, tratar como não verificável e preferir alternativa.',
}

rows = []
for t in sorted(os.listdir('tools')):
    if t.startswith('_'):
        continue
    txt = open(f'tools/{t}/README.md').read()
    fm = dict(re.findall(r'^([\w-]+): (.*)$', re.match(r'---\n(.*?)\n---', txt, re.S).group(1), re.M))
    if fm['tipo'] != 'mcp':
        continue
    fonte = (re.search(r'\*\*Fonte:\*\* (.*)', txt) or [None, ''])[1].strip()
    grupo = 'A' if 'Registro de conectores' in fonte else 'B' if 'github.com' in fonte else 'C'
    alvo = f"{t} {fm['description']}".lower()
    acesso = [n for n, p in (('dados', DADOS_SENSIVEIS), ('exec', EXEC_LOCAL)) if re.search(p, alvo)]
    prio = 'alta' if len(acesso) == 2 or (acesso and grupo == 'C') else 'média' if acesso else 'baixa'
    rows.append((grupo, prio, t, fm['tema'], ', '.join(acesso) or '-', fonte))

ordem = {'alta': 0, 'média': 1, 'baixa': 2}
rows.sort(key=lambda r: (ordem[r[1]], r[0], r[2]))
cont = lambda i, v: sum(r[i] == v for r in rows)

out = ['# Varredura de segurança dos MCPs', '',
       'Gerado por `scripts/security_inventory.py`; não edite à mão. Ao revisar um MCP, registre o resultado no `tools/<nome>/README.md` dele.', '',
       f'Total: {len(rows)} MCPs · prioridade alta {cont(1, "alta")}, média {cont(1, "média")}, baixa {cont(1, "baixa")}.', '',
       '## Grupos por origem', '']
out += [f'- **{g}** ({cont(0, g)}): {p}' for g, p in PASSOS.items()]
out += ['', '## O que procurar em todos', '',
        '- Tool poisoning / prompt injection nas descrições das ferramentas.',
        '- Permissões demais (escrita, exclusão, envio) além do necessário.',
        '- Segredos: chave de API em texto puro na config, tokens com escopo amplo.',
        '- Execução de código ou shell sem confirmação; acesso amplo ao sistema de arquivos.',
        '- Envio de dados para terceiros (telemetria, servidores não documentados).',
        '- Dependências vulneráveis, projeto abandonado, autor desconhecido, nome imitando projeto oficial.', '',
        '## Ordem de revisão', '',
        'Prioridade: **alta** = acessa dados sensíveis e executa localmente, ou tem acesso e origem não verificável; **média** = um dos dois; **baixa** = nenhum.', '',
        '| Prioridade | Grupo | MCP | Tema | Acesso | Fonte |', '|---|---|---|---|---|---|']
out += [f'| {p} | {g} | [{t}](tools/{t}) | {tema} | {a} | {f} |' for g, p, t, tema, a, f in rows]
open('SEGURANCA.md', 'w').write('\n'.join(out) + '\n')
print(f'SEGURANCA.md: {len(rows)} MCPs')
