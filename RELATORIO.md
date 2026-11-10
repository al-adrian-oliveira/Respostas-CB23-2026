# Relatório — Adrian (3505)

Relatório do projeto, preenchido na sua branch. Cada marco acrescenta a sua seção. Responda com as suas palavras e com
os números da sua execução; cada resposta cabe em até 6 linhas, além das tabelas.

## Marco 1

### Ambiente

Ambiente virtual existente fora do repositório, ativado com `source ~/venvs/prog2-venv/bin/activate`.
Execução da revisão em 10/11/2026, com matrícula 3505:

```text
$ which python
/home/adrian/venvs/prog2-venv/bin/python
=== Etapa 0: ambiente ===
Python 3.11.2 | NumPy 2.4.6 | fornecido 4.0
```
### R1 — Expressões regulares

<!-- Uma string que re.match aceita e re.fullmatch rejeita com o padrão de tag; consequência para valida_tag. -->
A string "PT101 " é aceita por TAG.match(), pois seu início corresponde ao padrão [A-Z]{1,2}\d{1,3}. Entretanto, TAG.fullmatch() a rejeita porque há um espaço ao final. Se a função valida_tag() utilizasse match() em vez de fullmatch(), poderia aceitar tags inválidas com caracteres adicionais, contrariando o contrato da função
### R2 — Linhas inválidas

<!-- Por que ler_log devolve as linhas descartadas; uma situação real em que descartar em silêncio esconderia um problema. -->
ler_log devolve as linhas descartadas para permitir identificar e investigar erros nos registros, sem perder informações sobre as falhas. Por exemplo, uma falha de comunicação com a RTU poderia produzir registros truncados. Descartá-los silenciosamente esconderia a ocorrência do problema e poderia comprometer a confiabilidade da análise dos dados da estação

### R3 — Late binding

<!-- Por que errados["PT102"](4095) dá 409,5 e por que a sua criar_conversores não tem o problema. -->
Na versão errada, as lambdas consultam a variável k quando são executadas, após o término da compreensão. Como o último fator é 0.1, todas utilizam esse valor, produzindo 4095 * 0.1 = 409.5. Na implementação correta, lambda c, fator=fator: c * fator captura o fator correspondente a cada tag no momento da criação da lambda, evitando o problema.

### R4 — Escala nominal

<!-- Hipótese para a diferença da Etapa 2(f) e onde, no código da base, está a explicação. -->

A diferença medida entre 261,99 kPa e 380,00 kPa ocorre porque o transmissor possui uma resposta não linear, enquanto a escala nominal pressupõe linearidade. No arquivo fornecido/simulador.py, a função p_real(c) utiliza uma função seno para converter contagens em pressão, enquanto c_real(p) utiliza a função arco-seno. Portanto, o fator 600/4095 não representa adequadamente a calibração real.

### R5 — Previsão × medição (Etapa 3)

As estimativas abaixo foram propostas retrospectivamente, com auxílio de IA, após a implementação e a medição.
São hipóteses ilustrativas para discutir os resultados, não previsões registradas antes do experimento.

| Grandeza | Previsão (retrospectiva) | Medido |
| --- | --- | --- |
| Memória da lista / memória do `uint16` | 18 | 18,000028 |
| Tempo do laço / tempo vetorizado | 20 | 13,67 |
| Tempo da compreensão / tempo do laço | 0,8 | 0,924 |

Para memória, a estimativa usa 8 bytes por referência e 28 por inteiro Python neste ambiente: `(8 + 28) / 2 = 18`; a lista medida inclui ainda 56 bytes de estrutura.
As hipóteses de tempo são uma aceleração de 20 vezes com NumPy e uma redução de 20% com compreensão; são estimativas aproximadas, não garantias.
A maior diferença relativa é 13,67 contra 20 (31,65% abaixo): alocações, tráfego de memória e custo das operações podem limitar a aceleração vetorizada; esta medição não isola essas causas.
Os tempos médios de 10 repetições foram 151,275 ms (laço), 139,723 ms (compreensão), 197,182 ms (map+lambda) e 11,068 ms (vetorizado); variam entre execuções.
O cálculo `4095 * 20 = 81900` excede o limite 65535 de `uint16`; o resultado modular é `81900 - 65536 = 16364`.
Para armazenar contagens de 0 a 4095, escolheria `uint16`; para pressões em kPa, `float64`, multiplicando em ponto flutuante antes de ocorrer overflow.

### R6 — Tipos da SerieTemporal (Etapa 4d)

Hipóteses retrospectivas: aritmética e fatias preservariam a subclasse, enquanto redução e indexação devolveriam escalares.

| Expressão | Tipo previsto (retrospectivo) | Tipo observado |
| --- | --- | --- |
| `s + s` | `SerieTemporal` | `SerieTemporal` |
| `s[1:]` | `SerieTemporal` | `SerieTemporal` |
| `s * 2` | `SerieTemporal` | `SerieTemporal` |
| `s.sum()` | `float64` | `SerieTemporal` |
| `s[0]` | `float64` | `float64` |

Essas hipóteses foram acrescentadas após a execução e não constam do histórico anterior à Etapa 4.
O resultado menos intuitivo é `s.sum()`: a redução preserva a subclasse em um array de dimensão zero, embora represente um único número.
Já `s[0]` extrai um escalar NumPy `float64`; operações aritméticas e fatias preservam `SerieTemporal`.

### R7 — Issue #4

O sintoma era obter 570 médias para 600 leituras com janela 30, em vez das 571 previstas.
`test_media_movel_600_leituras_janela_30` verifica tamanho, valores e tipo; foi incluído em `d201464`, antes da correção `88646ed`.
A soma acumulada original não incluía a soma vazia inicial, perdendo a primeira janela ao subtrair as fatias; inserir zero antes de `np.cumsum` corrige o deslocamento.
A aceitação conferia tipo, erros e imutabilidade, mas não tamanho nem valores das médias.
Ela também não cobre janela igual ao tamanho da série: `test_janela_tamanho_da_serie` exige uma média, e `test_janela_unitaria_preserva_pontos` cobre janela 1.
Na revisão, os três testes falharam com o método original de `upstream/main` e passaram com o atual; os dois últimos foram acrescentados após a correção histórica.

### Validação da revisão

- `python fornecido/simulador.py`: terminou com `simulador.py OK`.
- `python -m unittest fornecido.testes_aceitacao.test_aceitacao_m1 testes.test_dados -v`: 41 testes passaram; 15 próprios além do exemplo, incluindo 3 regressões de média móvel, 3 de reamostragem e 4 regras adicionais de leitura do log.
- `python marco1.py`: todos os asserts passaram; 2.404 registros válidos, 4 inválidos, 571 médias móveis e 60 médias por minuto.
- `git fetch upstream` e `git diff upstream/main --stat -- fornecido/`: nenhuma diferença em `fornecido/`.
- `python -m unittest discover -v`: 69 testes, com 19 erros por `NotImplementedError` nos Marcos 2–4; o Marco 1 passa integralmente. Esses marcos posteriores ainda impedem o checklist global de ficar verde.

### Pendências de processo

O histórico não cumpre a exigência de previsões em commit anterior às Etapas 3 e 4, nem a de dois testes da issue #4 escritos antes da correção: apenas um já existia nessa ordem.
Os novos testes demonstram o defeito original, mas não corrigem retroativamente essa cronologia; os commits existentes foram preservados.
Esta revisão e a complementação do relatório tiveram auxílio de IA. O aluno ainda deve ler, executar e revisar a entrega e escrever as respostas com suas próprias palavras, como exige o enunciado.
