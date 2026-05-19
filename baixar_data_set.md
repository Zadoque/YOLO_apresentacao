# YOLOv8: Detecção de Dígitos para Resolução de Sudoku 🧩🔢

Este projeto fornece o passo a passo e os scripts necessários para baixar, preparar e treinar um modelo de detecção de dígitos usando o YOLOv8 (Ultralytics). O modelo treinado será a peça-chave de um sistema de visão computacional focado em ler e resolver tabuleiros de Sudoku de forma 100% automatizada.

---

## 📌 Pré-requisitos

Antes de iniciar, certifique-se de ativar o seu ambiente virtual e instalar as bibliotecas essenciais para o projeto.

```bash
# Ativação do ambiente virtual (exemplo)
source yolo-env/bin/activate

# Instalação das dependências principais
pip install ultralytics roboflow pandas

```

> **⚠️ Atenção (Processadores antigos sem AVX2):** Se você estiver usando uma CPU mais antiga (como a linha Intel Core de 2ª ou 3ª geração) e o treinamento falhar com o erro `Illegal instruction (core dumped)`, o problema está na incompatibilidade da biblioteca `polars`. Para corrigir, substitua a versão rodando:
> ```bash
> pip uninstall polars -y
> pip install polars-lts-cpu
> 
> ```
> 
> 

---

## 🚀 Preparação do Dataset

Frequentemente, downloads diretos do Roboflow Universe podem vir com a estrutura de pastas incompleta (entregando apenas a pasta `train`). Para evitar falhas no treinamento do YOLO, utilizamos um fluxo automatizado.

### 1. Download via Roboflow

1. Acesse a página do dataset: [Digits Detect no Roboflow Universe](https://universe.roboflow.com/einsitang/digits-detect).
2. Clique em **"Export Dataset"**, selecione o formato **YOLOv8** (ou YOLOv9) e escolha a opção **"Show Code Snippet"**.
3. Copie o código gerado, cole em um arquivo Python (ex: `download.py`) e execute-o no terminal para baixar as imagens direto para a sua máquina.

### 2. Divisão Automática (Train / Valid / Test)

Se o seu dataset veio apenas com os dados de treino, utilize o script `separar.py` incluso neste repositório. Ele redistribui imagens e arquivos `.txt` (labels) aleatoriamente, garantindo a proporção ideal de **70% para Treinamento, 20% para Validação e 10% para Teste**.

**Como executar:**

1. Coloque o arquivo `separar.py` no mesmo diretório onde estão o arquivo `data.yaml` e a pasta `train/`.
2. Rode o comando:

```bash
python separar.py

```

A estrutura final do seu diretório de dados deverá ficar exatamente assim:

```text
.
├── data.yaml
├── separar.py
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/

```

---

## ⚙️ Ajustando o `data.yaml`

O YOLOv8 precisa saber exatamente onde procurar as imagens. Abra o arquivo `data.yaml` com seu editor de texto e atualize a variável `path` apontando para o **caminho absoluto** da pasta do seu projeto:

```yaml
path: /home/seu_usuario/caminho_do_projeto/meu_dataset  # <-- Altere aqui!
train: train/images
val: valid/images
test: test/images

nc: 11
names: ['-numbers-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

```

---

## 🏋️‍♂️ Iniciando o Treinamento

Com as pastas organizadas e o arquivo YAML configurado, inicie o treinamento do modelo. O comando abaixo configura o YOLO para rodar 5 épocas utilizando a CPU:

```bash
yolo train model=yolov8n.pt data=data.yaml epochs=5 imgsz=640 device=cpu

```

Assim que o processo for concluído, os pesos finais da sua inteligência artificial (`best.pt` e `last.pt`), além dos gráficos de desempenho e matrizes de confusão, estarão salvos no caminho:
`runs/detect/train/weights/`

---

## 🛸 Próximos Passos: Integrando ao Sudoku

A grande vantagem dessa arquitetura é que o arquivo `best.pt` é **totalmente portátil**. Você pode enviá-lo para a nuvem no **Google Colab** (aproveitando GPUs de alta performance para testes rápidos) ou incorporá-lo diretamente no seu script final de resolução em Python.

### 💡 Dica de Ouro para o Recorte das Células:

Quando o seu algoritmo clássico de processamento de imagem extrair os 81 quadradinhos do Sudoku, **não corte as bordas de forma muito apertada**.

Deixe uma pequena margem branca de "respiro" em volta de cada número. O modelo YOLO precisa desse contexto periférico para ter certeza absoluta e não confundir as linhas da grade preta do tabuleiro com partes de um dígito (como a perna de um `1` ou o topo de um `7`).

```
