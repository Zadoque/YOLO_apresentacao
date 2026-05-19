# Guia de Instalação do YOLO no Arch Linux 🚀

Este repositório contém o passo a passo detalhado para instalar e configurar o YOLO (via ecossistema oficial da Ultralytics) no Arch Linux. 

Devido à conformidade com a norma **PEP 668** adotada pelo Arch Linux, o gerenciador de pacotes `pip` bloqueia instalações globais para evitar quebras no sistema. Por conta disso, este guia utiliza estritamente um ambiente virtual Python (`venv`).

---

## 📋 Passo 1: Preparando o Diretório do Projeto

Antes de instalar as dependências de hardware, crie uma pasta dedicada para o seu projeto e configure a estrutura inicial do ambiente virtual. Abra o seu terminal e execute:

```bash
# Cria e acessa o diretório do projeto
mkdir meu_projeto_yolo && cd meu_projeto_yolo

# Cria o ambiente virtual Python
python -m venv yolo-env
```

---

## 🛠️ Passos 2 e 3: Instalação do Sistema e PyTorch (Lado a Lado)

Dependendo do hardware do seu computador, escolha a coluna correspondente abaixo. Os comandos estão dispostos lado a lado para evidenciar as diferenças de configuração:

<table>
  <tr>
    <th align="left" width="50%">💻 Opção A: Apenas CPU (Sem GPU)</th>
    <th align="left" width="50%">🎮 Opção B: Com GPU (NVIDIA CUDA)</th>
  </tr>
  <tr>
    <td valign="top">
      <p><strong>2. Instale as dependências básicas via pacman:</strong></p>
<pre><code>sudo pacman -Syu
sudo pacman -S python python-pip git base-devel</code></pre>
      <br>
      <p><strong>3. Ative o ambiente virtual:</strong></p>
<pre><code>source yolo-env/bin/activate</code></pre>
      <br>
      <p><strong>4. Instale o PyTorch padrão para CPU:</strong></p>
<pre><code>pip install torch torchvision torchaudio</code></pre>
    </td>
    <td valign="top">
      <p><strong>2. Instale o CUDA, cuDNN e ferramentas básicas:</strong></p>
<pre><code>sudo pacman -Syu
sudo pacman -S cuda cudnn python python-pip git base-devel</code></pre>
      <p><em>*Nota: É altamente recomendável reiniciar o computador após a primeira instalação do CUDA.</em></p>
      <p><strong>3. Ative o ambiente virtual:</strong></p>
<pre><code>source yolo-env/bin/activate</code></pre>
      <br>
      <p><strong>4. Instale o PyTorch compilado com suporte a CUDA:</strong></p>
<pre><code>pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121</code></pre>
    </td>
  </tr>
</table>

---

## 📦 Passo 4: Instalar o YOLO (Ultralytics)

Agora que o ambiente virtual está ativo e o PyTorch correto foi injetado, a instalação do pacote do YOLO é idêntica para ambos os casos. Execute no terminal:

```bash
pip install ultralytics
```

---

## ✅ Passo 5: Validar a Instalação

Para testar se o YOLO está funcionando corretamente, execute o comando de inferência rápida nativo. Ele fará o download automático de uma imagem de teste e do modelo mais leve (YOLOv8 Nano), salvando os resultados em seu diretório.

```bash
yolo predict model=yolov8n.pt source='[https://ultralytics.com/images/zidane.jpg](https://ultralytics.com/images/zidane.jpg)'
```

### 🔍 Verificação de Aceleração por GPU (Apenas para Opção B)
Se você configurou o suporte à GPU NVIDIA, valide se o framework está realmente utilizando a placa de vídeo rodando esta linha de código Python no terminal:

```bash
python -c "import torch; print('CUDA Ativo?:', torch.cuda.is_available()); print('Placa Detectada:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'Nenhuma')"
```

* **Resultado esperado para CPU:** `CUDA Ativo?: False`
* **Resultado esperado para GPU:** `CUDA Ativo?: True` (seguido pelo nome do seu modelo NVIDIA).

---

## ⚠️ Dicas e Solução de Problemas no Arch

1. **O comando `yolo` sumiu / não funciona:** O comando só fica disponível quando o ambiente virtual está ativo. Toda vez que abrir um novo terminal para trabalhar no projeto, lembre-se de navegar até a pasta e rodar:
   ```bash
   source yolo-env/bin/activate
   ```
2. **Erro `externally-managed-environment`:** Se você visualizar este erro, significa que você esqueceu de ativar o ambiente virtual ou tentou usar o `sudo pip`. Nunca utilize `sudo pip` no Arch Linux.
3. **Erros de biblioteca CUDA:** Caso o terminal aponte falta de alguma biblioteca `.so`, certifique-se de que seu sistema Arch está completamente atualizado executando `sudo pacman -Syu`.
