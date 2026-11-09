# Relatório — <seu nome> (<sua matrícula>)

Relatório do projeto, preenchido na sua branch. Cada marco acrescenta a sua seção. Responda com as suas palavras e com
os números da sua execução; cada resposta cabe em até 6 linhas, além das tabelas.

## Marco 1

### Ambiente

<!-- Cole aqui a saída de `which python` e da Etapa 0 do `python marco1.py`. -->
/home/adrian/venvs/prog2-venv/bin/python
Python 3.11.2 | NumPy 2.4.6 | fornecido 3.0
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

A diferença entre aproximadamente 262 kPa e 380 kPa ocorre porque o transmissor possui uma resposta não linear, enquanto a escala nominal pressupõe linearidade. No arquivo fornecido/simulador.py, a função p_real(c) utiliza uma função seno para converter contagens em pressão, enquanto c_real(p) utiliza a função arco-seno. Portanto, o fator 600/4095 não representa adequadamente a calibração real.

### R5 — Previsão × medição (Etapa 3)

Previsões registradas no commit: <!-- cole o hash curto do commit de previsões -->

| Grandeza | Previsão | Medido |
| --- | --- | --- |
| Memória da lista / memória do `uint16` | | |
| Tempo do laço / tempo vetorizado | | |
| Tempo da compreensão / tempo do laço | | |

<!-- Explique a maior diferença entre previsão e medição; por que uint16 * 20 dá 16364; que dtype você escolheria para contagens e para kPa. -->

### R6 — Tipos da SerieTemporal (Etapa 4d)

| Expressão | Tipo previsto | Tipo observado |
| --- | --- | --- |
| `s + s` | | |
| `s[1:]` | | |
| `s * 2` | | |
| `s.sum()` | | |
| `s[0]` | | |

<!-- Explique o resultado que mais surpreendeu você. -->

### R7 — Issue #4

<!-- Sintoma; o teste de regressão (nome); a causa, em termos da soma acumulada; a correção; por que os testes de aceitação não pegaram o defeito; mais um caso que eles não cobrem e qual teste seu o cobre. -->
