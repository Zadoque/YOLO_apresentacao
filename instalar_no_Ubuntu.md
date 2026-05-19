# Guia de Instalação do YOLO no Ubuntu 🚀

Este repositório contém o passo a passo detalhado para instalar e configurar o YOLO (via ecossistema oficial da Ultralytics) no Ubuntu Linux utilizando o gerenciador de pacotes `apt`.

Devido à conformidade com a norma **PEP 668** adotada pelas versões recentes do Ubuntu, o gerenciador de pacotes `pip` bloqueia instalações globais. Por conta disso, este guia utiliza um ambiente virtual Python (`venv`).

---

## 📋 Passo 1: Criando o Ambiente do Projeto

Antes de instalar as dependências, precisamos preparar a pasta do projeto. No Ubuntu, o módulo de ambiente virtual precisa ser instalado separadamente, o que faremos no próximo passo. Por enquanto, crie a estrutura de diretórios:

```bash
# Cria e acessa o diretório do projeto
mkdir meu_projeto_yolo && cd meu_projeto_yolo
```

---

## 🛠️ Passos 2 e 3: Instalação do Sistema e PyTorch (Lado a Lado)

Escolha a coluna correspondente ao seu hardware. Os comandos estão dispostos lado a lado para facilitar a visualização das diferenças de configuração:

<table>
  <tr>
    <th align="left" width="50%">💻 Opção A: Apenas CPU (Sem GPU)</th>
    <th align="left" width="50%">🎮 Opção B: Com GPU (NVIDIA CUDA)</th>
  </tr>
  <tr>
    <td valign="top">
      <p><strong>2. Instale as dependências básicas via apt:</strong></p>
<pre><code>sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git build-essential -y</code></pre>
      <br>
      <p><strong>3. Crie e ative o ambiente virtual:</strong></p>
<pre><code>python3 -m venv yolo-env
source yolo-env/bin/activate</code></pre>
      <br>
      <p><strong>4. Instale o PyTorch padrão para CPU:</strong></p>
<pre><code>pip install torch torchvision torchaudio</code></pre>
    </td>
    <td valign="top">
      <p><strong>2. Instale o Toolkit CUDA e ferramentas essenciais:</strong></p>
<pre><code>sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git build-essential nvidia-cuda-toolkit -y</code></pre>
      <p><em>*Nota: Certifique-se de já ter o driver proprietário da NVIDIA instalado via "Drivers Adicionais" do Ubuntu antes de prosseguir.</em></p>
      <p><strong>3. Crie e ative o ambiente virtual:</strong></p>
<pre><code>python3 -m venv yolo-env
source yolo-env/bin/activate</code></pre>
      <p><strong>4. Instale o PyTorch com suporte a CUDA:</strong></p>
<pre><code>pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121</code></pre>
    </td>
  </tr>
</table>

---

## 📦 Passo 4: Instalar o YOLO (Ultralytics)

Com o seu ambiente virtual ativo e o PyTorch correto injetado, a instalação do pacote do YOLO é universal. Execute o comando abaixo no terminal:

```bash
pip install ultralytics
```

---

## ✅ Passo 5: Validar a Instalação

Para testar se o YOLO está perfeitamente operacional, execute o comando de inferência rápida. Ele baixará automaticamente uma imagem de teste e o modelo mais leve (YOLOv8 Nano), salvando os resultados no seu diretório atual.

```bash
yolo predict model=yolov8n.pt source='[https://ultralytics.com/images/zidane.jpg](https://ultralytics.com/images/zidane.jpg)'
```

### 🔍 Verificação de Aceleração por GPU (Apenas para Opção B)
Se você configurou o suporte à GPU, valide se o ecossistema está de fato conversando com a sua placa de vídeo rodando esta linha de código no terminal:

```bash
python3 -c "import torch; print('CUDA Ativo?:', torch.cuda.is_available()); print('Placa Detectada:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'Nenhuma')"
```

* **Resultado esperado para CPU:** `CUDA Ativo?: False`
* **Resultado esperado para GPU:** `CUDA Ativo?: True` (seguido pelo modelo da sua GPU NVIDIA).

---

## ⚠️ Dicas e Solução de Problemas no Ubuntu

1. **O comando `yolo` não foi encontrado:** O comando só funciona quando o ambiente virtual está ativo. Sempre que abrir um novo terminal, lembre-se de navegar até a pasta do projeto e rodar:
   ```bash
   source yolo-env/bin/activate
   ```
2. **Erro `externally-managed-environment`:** Isso ocorre se você tentar usar o `pip install` fora do ambiente virtual ou utilizando `sudo`. No Ubuntu, mantenha todas as instalações de pacotes Python de IA estritamente dentro do `venv` e sem privilégios de superusuário.
3. **Versão do Python:** O Ubuntu mapeia o interpretador como `python3`. Evite usar apenas o comando `python` fora do ambiente virtual para não chamar versões incorretas do sistema.
