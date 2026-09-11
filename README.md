# Missão Aquário Digital

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge\&logo=python\&logoColor=white)
![Git](https://img.shields.io/badge/Git-Versionamento-orange?style=for-the-badge\&logo=git\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?style=for-the-badge\&logo=github\&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

Exercício desenvolvido para a disciplina de **Gestão e Qualidade de Software**, com foco na aplicação prática de conceitos de **versionamento, qualidade de software e gestão de ambientes utilizando Git e GitHub**.

A atividade simula o desenvolvimento de um sistema de monitoramento de um **aquário digital**, responsável por verificar parâmetros essenciais da qualidade da água, utilizando um fluxo de desenvolvimento estruturado em três ambientes:

```text
develop → stage → main
```

O principal objetivo é compreender como uma funcionalidade pode ser desenvolvida, testada, homologada e posteriormente disponibilizada em produção de maneira organizada e controlada.


## ▸ Conceito da atividade

A atividade consiste na criação do repositório `aquario-digital-core` e no desenvolvimento de um módulo responsável pelo monitoramento dos parâmetros de qualidade da água do aquário.

O módulo implementado realiza a verificação de dois parâmetros:

* **pH da água**;
* **Temperatura da água**.

Os valores são comparados com os limites considerados ideais para o funcionamento do aquário.

O projeto também utiliza um fluxo de branches baseado em três ambientes:

```text
develop
   ↓
stage
   ↓
main
```

Cada branch possui uma finalidade específica dentro do processo de desenvolvimento e entrega do software.

## ▸ Camadas do ambiente

### `develop` - Desenvolvimento

A branch `develop` representa o ambiente de **desenvolvimento** do projeto.

É nesta etapa que novas funcionalidades são implementadas e alterações no código são realizadas.

Neste ambiente são realizadas atividades como:

* Desenvolvimento do módulo de controle da qualidade da água;
* Implementação das regras de negócio;
* Correções e melhorias no código;
* Testes iniciais;
* Integração das funcionalidades desenvolvidas.

As funcionalidades são inicialmente desenvolvidas em branches específicas e posteriormente integradas à `develop` através de Pull Requests.

---

### `stage` - Homologação

A branch `stage` representa o ambiente de **testes e homologação**.

Depois que as alterações são integradas à `develop`, elas são promovidas para `stage` através de um Pull Request.

Nesta etapa são realizadas:

* Validação das funcionalidades;
* Revisão do código;
* Testes do módulo;
* Simulação de Code Review;
* Verificação do comportamento esperado;
* Aprovação antes da publicação em produção.

A `stage` funciona como uma camada intermediária entre o desenvolvimento e a produção.

---

### `main` - Produção

A branch `main` representa o ambiente de **produção** e contém a versão considerada estável do projeto.

Somente alterações que passaram pelo processo de desenvolvimento e homologação devem ser promovidas para esta branch.

O fluxo de entrega segue:

```text
develop → stage → main
```

Dessa forma, o código presente na `main` representa uma versão que passou pelas etapas anteriores de validação.

## ▸ Módulo de Controle da Qualidade da Água

O módulo principal desenvolvido nesta atividade é o:

```text
ControleQualidadeAgua
```

Sua responsabilidade é verificar se os parâmetros da água estão dentro dos limites estabelecidos.

### Parâmetros monitorados

| Parâmetro       | Limite mínimo | Limite máximo |
| --------------- | ------------- | ------------- |
| **pH**          | 6.8           | 7.6           |
| **Temperatura** | 22.0 °C       | 28.0 °C       |

Caso o pH esteja fora do intervalo permitido, o sistema apresenta um alerta:

```text
ALERTA QA: Nível de pH fora do limite ideal!
```

Caso a temperatura esteja fora do intervalo seguro:

```text
ALERTA QA: Temperatura fora do limite seguro!
```

Quando os dois parâmetros estão dentro dos limites estabelecidos:

```text
STATUS: Parâmetros da água em níveis ideais.
```

---

## ▸ Implementação

O módulo foi desenvolvido em **Python**, utilizando programação orientada a objetos.

```python
class ControleQualidadeAgua:
    def __init__(self, ph, temperatura):
        self.ph = ph
        self.temperatura = temperatura

    def verificar_parametros(self):
        if self.ph < 6.8 or self.ph > 7.6:
            print("ALERTA QA: Nível de pH fora do limite ideal!")
            return False

        if self.temperatura < 22.0 or self.temperatura > 28.0:
            print("ALERTA QA: Temperatura fora do limite seguro!")
            return False

        print("STATUS: Parâmetros da água em níveis ideais.")
        return True
```

A classe recebe os valores de **pH** e **temperatura** através do construtor e disponibiliza o método `verificar_parametros()` para realizar a validação.


## ▸ Branch de funcionalidade

Para o desenvolvimento do módulo foi criada uma branch específica:

```text
feature/controle-qualidade
```

O fluxo utilizado foi:

```text
develop
   ↓
feature/controle-qualidade
```

Após a implementação e validação inicial, a feature foi enviada ao GitHub e integrada à `develop` através de um Pull Request.

## ▸ Fluxo de Pull Requests

A atividade utiliza Pull Requests para controlar a promoção das alterações entre os ambientes.

### 1. Feature → Develop

```text
feature/controle-qualidade
              ↓
           develop
```

A funcionalidade de controle da qualidade da água foi desenvolvida na branch:

```text
feature/controle-qualidade
```

Após a implementação, foi criado um Pull Request para integrar a funcionalidade à branch `develop`.



### 2. Develop → Stage

```text
develop
   ↓
stage
```

Após a consolidação da funcionalidade na `develop`, foi criado um Pull Request para promover as alterações para o ambiente de homologação.

**Título do Pull Request:**

```text
[Stage] Feat: Módulo de Controle da Água.
```

Nesta etapa são realizadas as validações necessárias antes da liberação para produção.

### 3. Stage → Main

```text
stage
   ↓
main
```

Após a validação do código no ambiente de homologação, foi criado um segundo Pull Request para promover as alterações para produção.

**Título do Pull Request:**

```text
[Release v1.0] Implantação do Módulo de Controle da Água.
```

A aprovação deste Pull Request representa a liberação da funcionalidade para o ambiente de produção.

## ▸ Versionamento e qualidade de software

O projeto foi desenvolvido utilizando práticas de **controle de versão e gestão da qualidade de software**.

Durante a atividade foram aplicados os seguintes conceitos:

| Conceito           | Aplicação                                 |
| ------------------ | ----------------------------------------- |
| **Repositório**    | Armazenamento do código e documentação    |
| **Branch**         | Separação dos ambientes e funcionalidades |
| **`develop`**      | Desenvolvimento                           |
| **`stage`**        | Testes e homologação                      |
| **`main`**         | Produção                                  |
| **Feature Branch** | Desenvolvimento isolado da funcionalidade |
| **Commit**         | Registro das alterações                   |
| **Push**           | Envio das alterações para o GitHub        |
| **Pull Request**   | Solicitação de integração entre branches  |
| **Code Review**    | Revisão das alterações                    |
| **Merge**          | Integração do código                      |
| **Homologação**    | Validação antes da produção               |

A utilização dessas práticas permite controlar o ciclo de vida das alterações e reduzir o risco de disponibilizar funcionalidades não validadas no ambiente de produção.

## ▸ Fluxo completo de desenvolvimento

O processo realizado durante a atividade pode ser representado da seguinte maneira:

```text
1. Criar repositório
        ↓
2. Criar branch stage
        ↓
3. Criar branch develop
        ↓
4. Criar feature/controle-qualidade
        ↓
5. Implementar módulo de controle da água
        ↓
6. Atualizar documentação
        ↓
7. Commit das alterações
        ↓
8. Push da feature para o GitHub
        ↓
9. Pull Request: feature → develop
        ↓
10. Revisão e Merge
        ↓
11. Pull Request: develop → stage
        ↓
12. Homologação e validação
        ↓
13. Aprovação
        ↓
14. Pull Request: stage → main
        ↓
15. Aprovação final
        ↓
16. Merge para produção
```

## ▸ Comandos utilizados

### Criar a branch `stage`

```bash
git checkout -b stage
git push origin stage
```

### Criar a branch `develop`

```bash
git checkout -b develop
git push origin develop
```

### Criar a branch de funcionalidade

```bash
git checkout -b feature/controle-qualidade
```

### Adicionar alterações

```bash
git add .
```

### Criar commit

```bash
git commit -m "feat: implementa modulo de monitoramento da qualidade da agua"
```

### Enviar a feature para o GitHub

```bash
git push origin feature/controle-qualidade
```

---

## ▸ Como executar

### Pré-requisito

É necessário possuir o **Python** instalado na máquina.

### Clonar o repositório

```bash
git clone https://github.com/miguelalchaar/aquario-digital-core.git
```

### Acessar o projeto

```bash
cd src/aquario-digital-core
```

### Executar o módulo

```bash
python ControleQualidadeAgua.py
```

> Caso o arquivo possua uma função de execução ou exemplos de utilização, eles podem ser executados a partir do próprio arquivo.

---

## ▸ Responsáveis

* **Miguel Alchaar** - Desenvolvedor

## ▸ Objetivo da missão

A **Missão Aquário Digital** tem como objetivo demonstrar, de maneira prática, a aplicação de conceitos de **Gestão e Qualidade de Software**, utilizando um cenário de monitoramento de qualidade da água.

Além da implementação do algoritmo, a atividade permite praticar um fluxo de desenvolvimento organizado utilizando:

```text
Feature → Develop → Stage → Main
```

Esse processo representa uma estratégia de desenvolvimento na qual as funcionalidades são implementadas, revisadas, homologadas e somente então disponibilizadas em produção.

