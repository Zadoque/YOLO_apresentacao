import os
import random
import shutil
from pathlib import Path

# 1. Definir proporções (70% treino, 20% validação, 10% teste)
P_VAL = 0.20
P_TEST = 0.10

# 2. Caminhos das pastas
base_dir = Path(".")
train_img_dir = base_dir / "train" / "images"
train_lbl_dir = base_dir / "train" / "labels"

# Criar novas pastas que estão faltando
for folder in ["valid/images", "valid/labels", "test/images", "test/labels"]:
    (base_dir / folder).mkdir(parents=True, exist_ok=True)

# 3. Listar e embaralhar todas as imagens atuais
imagens = sorted([f for f in os.listdir(train_img_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
random.seed(42) # Garante que o embaralhamento seja reprodutível
random.shuffle(imagens)

total_imagens = len(imagens)
num_val = int(total_imagens * P_VAL)
num_test = int(total_imagens * P_TEST)

val_files = imagens[:num_val]
test_files = imagens[num_val : num_val + num_test]

print(f"Total de imagens encontradas: {total_imagens}")
print(f"Movendo {len(val_files)} para Validação e {len(test_files)} para Teste...")

# 4. Função auxiliar para mover imagem + label correspondente
def mover_par(lista_arquivos, destino):
    for img_name in lista_arquivos:
        src_img = train_img_dir / img_name
        dst_img = base_dir / destino / "images" / img_name
        
        # Aqui está a correção: pegando o nome limpo e adicionando .txt
        label_name = os.path.splitext(img_name)[0] + ".txt"
        
        src_lbl = train_lbl_dir / label_name
        dst_lbl = base_dir / destino / "labels" / label_name
        
        # Mover imagem
        if src_img.exists():
            shutil.move(str(src_img), str(dst_img))
        
        # Mover label correspondente (se existir)
        if src_lbl.exists():
            shutil.move(str(src_lbl), str(dst_lbl))

# 5. Executar a movimentação
mover_par(val_files, "valid")
mover_par(test_files, "test")

print("⚡ Separação concluída com sucesso!")
print(f"Restaram {len(os.listdir(train_img_dir))} imagens na pasta de treino.")
