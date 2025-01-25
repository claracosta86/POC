import subprocess

# Caminho do arquivo que contém a classe e o teste
input_file = "classes.txt"

# Leia o conteúdo do arquivo
with open(input_file, "r") as file:
    input_text = file.read()

# Comando para executar o Mistral usando o conteúdo do arquivo como entrada
command = [
    "./build/bin/llama-cli",
    "-m", "./mistral_gguf/Mistral-7B-Instruct-v0.3.Q5_K_M.gguf",
    input_text,
]

# Execute o comando
try:
    result = subprocess.run(command, text=True, capture_output=True, check=True)
    print("Resposta do modelo:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Erro ao executar o modelo:")
    print(e.stderr)

