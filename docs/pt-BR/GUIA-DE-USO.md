# Guia detalhado de uso

## Objetivo

Este projeto fornece um processo reutilizável para criar, auditar e manter a
documentação de projetos de software sem inventar informações.

Ele pode ser utilizado em:

- projetos SaaS
- websites e aplicações web
- APIs e integrações
- infraestrutura e plataformas
- projetos com desenvolvimento assistido por IA
- projetos novos sem documentação
- projetos existentes com documentação desatualizada
- projetos que utilizam Spec-Driven Development

## Como o framework está organizado

O repositório possui quatro partes principais:

1. **Skill:** define o processo que um agente de IA compatível deve seguir.
2. **Referências:** definem os padrões de documentação e alinhamento com specs.
3. **Templates:** fornecem estruturas iniciais adaptáveis.
4. **Scripts:** coletam evidências e validam o repositório.

A documentação específica de um sistema deve permanecer no repositório desse
sistema. Este repositório central mantém apenas o padrão reutilizável.

## Compatibilidade com agentes de IA

Esta não é uma skill exclusiva do Codex. Ela segue a especificação aberta
[Agent Skills](https://agentskills.io/specification), utilizada por diferentes
ferramentas. O conteúdo da skill é o mesmo, mas o diretório de instalação e o
comando de ativação podem mudar.

| Agente | Diretório no projeto | Ativação explícita |
| --- | --- | --- |
| Codex | `.agents/skills/document-software-project/` | `$document-software-project` |
| Gemini CLI | `.agents/skills/document-software-project/` | Solicitar o uso da skill pelo nome |
| GitHub Copilot | `.agents/skills/document-software-project/` | Incluir `/document-software-project` no pedido |
| Claude Code | `.claude/skills/document-software-project/` | `/document-software-project` |

A compatibilidade depende da ferramenta que executa o agente, não apenas do modelo
de linguagem. Para utilizar o fluxo completo, o agente precisa acessar os arquivos
do projeto e executar Python 3.

Consulte também o
[guia completo de compatibilidade](../COMPATIBILITY.md).

## Escolha o tipo de instalação

### Instalação em um projeto para Codex, Gemini CLI ou GitHub Copilot

Use esta opção quando a skill deve ser compartilhada com todos que trabalham em um
repositório específico.

O caminho final será:

```text
meu-projeto/.agents/skills/document-software-project/
```

Passos:

```bash
git clone https://github.com/alessonviana/software-documentation-framework.git
mkdir -p /caminho/meu-projeto/.agents/skills
cp -R software-documentation-framework/.agents/skills/document-software-project \
  /caminho/meu-projeto/.agents/skills/
```

Antes de incluir a skill em outro repositório, verifique a licença vigente e as
políticas da equipe.

### Instalação em um projeto para Claude Code

O Claude Code utiliza o mesmo conteúdo, mas procura skills do projeto em
`.claude/skills`:

```bash
mkdir -p /caminho/meu-projeto/.claude/skills
cp -R software-documentation-framework/.agents/skills/document-software-project \
  /caminho/meu-projeto/.claude/skills/
```

Depois, inicie o Claude Code no projeto e utilize:

```text
/document-software-project
Audite a documentação deste projeto sem modificar arquivos.
```

### Instalação para todos os projetos no Codex, Gemini CLI ou GitHub Copilot

Use o escopo do usuário:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R software-documentation-framework/.agents/skills/document-software-project \
  "$HOME/.agents/skills/"
```

Também é possível utilizar um link simbólico:

```bash
ln -s "$(pwd)/software-documentation-framework/.agents/skills/document-software-project" \
  "$HOME/.agents/skills/document-software-project"
```

O Codex reconhece skills armazenadas ou vinculadas nesse diretório.

### Instalação para todos os projetos no Claude Code

```bash
mkdir -p "$HOME/.claude/skills"
cp -R software-documentation-framework/.agents/skills/document-software-project \
  "$HOME/.claude/skills/"
```

Nas versões atuais, o Claude Code também aceita links simbólicos no diretório de
skills.

### Instalação pelo skill installer do Codex

No Codex, utilize:

```text
$skill-installer
Instale a skill document-software-project a partir de:
https://github.com/alessonviana/software-documentation-framework/tree/main/.agents/skills/document-software-project
```

## Como ativar a skill

No Codex:

```text
$document-software-project
<descreva o trabalho de documentação>
```

No Claude Code:

```text
/document-software-project
<descreva o trabalho de documentação>
```

No GitHub Copilot:

```text
Use a skill /document-software-project.
<descreva o trabalho de documentação>
```

No Gemini CLI ou em outro agente compatível:

```text
Use a skill document-software-project.
<descreva o trabalho de documentação>
```

A skill também pode ser ativada automaticamente quando o pedido corresponder à
descrição dela e a ferramenta oferecer ativação automática.

## Fluxo recomendado para um projeto novo

Utilize:

```text
$document-software-project
Examine este projeto e crie sua documentação do zero. Não invente informações.
Antes de escrever, apresente o mapa de documentos recomendado e faça perguntas
quando uma decisão importante não puder ser comprovada.
```

A skill deverá:

1. Ler as instruções do repositório.
2. Identificar código, specs, testes, banco, APIs, infraestrutura e CI/CD.
3. Separar fatos confirmados, inferências, conflitos e informações desconhecidas.
4. Identificar os públicos da documentação.
5. Propor o menor conjunto suficiente de documentos.
6. Atualizar primeiro os artefatos de especificação afetados.
7. Criar os documentos selecionados.
8. Validar comandos, links, exemplos, contratos e diagramas.
9. Apresentar as alterações e limitações.

## Fluxo recomendado para um projeto existente

Antes de permitir alterações, solicite uma auditoria:

```text
$document-software-project
Audite a documentação deste projeto sem modificar arquivos. Compare documentação,
specs, testes, contratos e implementação. Mostre inconsistências, informações sem
evidência, lacunas por público e uma proposta priorizada de correção.
```

Depois de revisar o relatório:

```text
$document-software-project
Implemente as correções de prioridade alta aprovadas na auditoria. Preserve a
estrutura existente quando ela continuar adequada. Não altere o comportamento do
software.
```

## Atualização após uma funcionalidade

```text
$document-software-project
Analise as alterações desta funcionalidade e atualize todas as especificações e
documentações afetadas. Mostre o vínculo entre requisitos, critérios de aceitação,
plano, tarefas, testes e documentação de release.
```

A skill verifica impacto sobre:

- comportamento visível ao usuário
- permissões e regras de negócio
- requisitos funcionais e não funcionais
- APIs, eventos, CLI e integrações
- banco de dados e migrações
- arquitetura e dependências
- configuração e ambiente local
- deployment, rollback e observabilidade
- segurança, privacidade e retenção

## Análise de divergência com SDD

```text
$document-software-project
Compare a especificação, o plano, as tarefas, os testes e a implementação. Gere um
relatório de divergência antes de alterar a intenção normativa. Se não for possível
determinar se o código ou a spec está correto, pergunte.
```

O framework reconhece convenções como:

- GitHub Spec Kit
- OpenSpec
- Kiro Specs
- BDD
- RFCs e ADRs
- diretórios próprios de requisitos ou especificações

Ele não instala nem migra automaticamente nenhum desses frameworks.

## Modelo de evidências

Toda informação material deve ser classificada:

| Classe | Significado | Tratamento |
| --- | --- | --- |
| Confirmada | Possui fonte autoritativa direta | Pode ser escrita como fato |
| Inferida | É sugerida pelo código ou configuração | Deve ser identificada e confirmada |
| Conflitante | Fontes autoritativas discordam | Exige relatório e decisão |
| Desconhecida | Não existe evidência suficiente | Deve ser perguntada, omitida ou marcada com aprovação |

Exemplo:

- O código pode confirmar que hoje uma rota aceita determinado campo.
- A especificação pode confirmar que o produto deveria exigir outro comportamento.
- Nenhum deles, isoladamente, resolve qual intenção deve prevalecer.

## Utilização direta do coletor

O script pode ser utilizado sem ativar a skill.

### Saída em Markdown

```bash
python3 .agents/skills/document-software-project/scripts/collect_project_evidence.py \
  --root /caminho/do/projeto \
  --format markdown
```

### Saída em JSON

```bash
python3 .agents/skills/document-software-project/scripts/collect_project_evidence.py \
  --root /caminho/do/projeto \
  --format json
```

### Limitar a quantidade de arquivos inspecionados

```bash
python3 .agents/skills/document-software-project/scripts/collect_project_evidence.py \
  --root /caminho/do/projeto \
  --format json \
  --max-files 5000
```

O coletor identifica:

- documentos e arquivos de instrução
- artefatos de especificação
- manifests e tecnologias
- contratos de API
- banco e migrações
- testes
- containers
- infraestrutura
- pipelines de CI/CD
- nomes de variáveis presentes em arquivos de exemplo

O coletor não lê:

- valores de arquivos `.env` reais
- chaves privadas
- arquivos de credenciais comuns
- dependências vendorizadas
- diretórios gerados
- arquivos acessados por links simbólicos

O resultado do coletor é apenas um inventário. Ele não comprova regras de negócio ou
intenção de produto.

## Como utilizar os templates

Os templates ficam em:

```text
.agents/skills/document-software-project/assets/templates/
```

Exemplo:

```bash
cp .agents/skills/document-software-project/assets/templates/ARCHITECTURE.template.md \
  docs/ARCHITECTURE.md
```

Depois de copiar:

1. Defina o público e a finalidade.
2. Remova seções que não sejam necessárias.
3. Substitua placeholders somente por informações comprovadas.
4. Adicione links para fontes autoritativas.
5. Valide comandos, caminhos, exemplos e diagramas.
6. Inclua o documento no README ou índice de documentação.

Nunca publique um template cheio de campos vazios.

## Documentos disponíveis

| Necessidade | Template |
| --- | --- |
| Entrada principal do projeto | `README.template.md` |
| Visão, problema e escopo | `PROJECT-OVERVIEW.template.md` |
| Requisitos de funcionalidade | `FEATURE-SPEC.template.md` |
| Componentes e arquitetura | `ARCHITECTURE.template.md` |
| Decisão técnica relevante | `ADR.template.md` |
| Ambiente e contribuição | `DEVELOPMENT.template.md` |
| Publicação e rollback | `DEPLOYMENT.template.md` |
| Diagnóstico e recuperação | `RUNBOOK.template.md` |
| Instruções para agentes | `AGENTS.template.md` |

## Preparação para agentes de IA

Pedido recomendado:

```text
$document-software-project
Prepare este repositório para desenvolvedores e agentes de IA. Crie ou atualize um
AGENTS.md curto e operacional. Ele deve apontar para as fontes autoritativas, sem
duplicar arquitetura ou requisitos. Verifique todos os comandos obrigatórios.
```

Um bom `AGENTS.md` deve informar:

- mapa do projeto
- documentos obrigatórios
- comandos seguros
- restrições de mudança
- regras de atualização documental
- definição de pronto

Ele não deve copiar toda a documentação técnica.

## Integração com pull requests

Adicione esta seção ao template de PR do projeto:

```markdown
## Impacto na documentação

- [ ] Nenhuma alteração documental é necessária, com justificativa abaixo.
- [ ] Especificações foram atualizadas.
- [ ] Documentação de desenvolvimento ou operação foi atualizada.
- [ ] Documentação de API, dados, release ou usuário foi atualizada.

Justificativa ou links:
```

Isso obriga o autor a avaliar o impacto sem exigir documentos desnecessários.

## Perguntas que a skill poderá fazer

A skill deve perguntar quando a resposta afetar:

- objetivo ou escopo
- usuários, permissões e regras
- arquitetura ou integrações
- dados, segurança ou privacidade
- requisitos de desempenho ou disponibilidade
- ambientes, deployment ou recuperação
- público, idioma ou visibilidade da documentação

Ela não deve perguntar algo que já possa ser comprovado no projeto.

## Validação esperada

Quando aplicável, a skill deverá:

- executar comandos de instalação e uso
- testar exemplos de código
- validar links e âncoras
- comparar APIs com seus contratos
- comparar dados com schemas ou migrações
- conferir deployment e rollback com as configurações
- validar diagramas Mermaid
- executar linters e builds documentais existentes
- revisar o diff final

Quando algo não puder ser validado, isso deve aparecer claramente no relatório
final.

## Auditoria para repositório público

Utilize:

```text
$document-software-project
Audite este repositório antes da publicação pública. Procure credenciais, caminhos
privados, dados pessoais ou de clientes, anexos internos, conteúdo protegido,
exemplos inseguros e informações sem evidência. Não publique nem apague arquivos.
```

Consulte também a
[política de segurança para repositório público](../PUBLIC-REPOSITORY-SAFETY.md).

## Validação deste framework

Dentro deste repositório:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

Essas verificações também são executadas pelo GitHub Actions.

## Limitações

- O framework não recupera sozinho a intenção original de negócio.
- Testes aprovados não provam que todos os requisitos foram representados.
- Código existente pode refletir um bug ou workaround.
- Documentação gerada automaticamente não substitui explicações orientadas ao
  leitor.
- A skill não deve escolher licenças, responsáveis, metas ou políticas sem
  autorização.

## Próximo passo recomendado

Comece com uma auditoria sem alterações em um projeto real. Revise as perguntas e o
mapa de documentos proposto. Somente depois autorize a criação ou reorganização dos
arquivos.
