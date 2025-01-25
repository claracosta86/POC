from llama_cpp import Llama

# Caminho para o modelo quantizado GGUF
model_path = "./mistral_gguf/Mistral-7B-Instruct-v0.3.Q5_K_M.gguf"

# Inicializar o modelo
print("Carregando o modelo...")
llm = Llama(model_path=model_path)

# Caminho para o arquivo de entrada
input_file = "classes.txt"

# Ler o conteúdo do arquivo
with open(input_file, "r") as file:
    input_text = file.read()

# Enviar o texto para o modelo
print("Enviando texto para o modelo...")
response = llm(input_text, max_tokens=3512, stop=["###"])  # Ajuste o max_tokens conforme necessário

# Função para dividir o texto em pedaços menores
def split_text(text, max_length=400):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

# Dividir o texto e enviar cada parte separadamente
text_chunks = split_text(input_text, max_length=400)

for chunk in text_chunks:
    response = llm(chunk, max_tokens=100, stop=["###"])
    print(response["choices"][0]["text"])

