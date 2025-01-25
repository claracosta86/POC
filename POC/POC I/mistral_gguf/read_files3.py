from llama_cpp import Llama

# Caminho do modelo quantizado
model_path = "./mistral_gguf/Mistral-7B-Instruct-v0.3.Q5_K_M.gguf"

# Inicializar o modelo com tamanho de contexto ajustado
llm = Llama(model_path=model_path, n_ctx=512)  # Ajuste n_ctx se o modelo suportar mais

# Caminho do arquivo de entrada
input_file = "classes.txt"

# Ler o conteúdo do arquivo
with open(input_file, "r") as file:
    input_text = file.read()

# Dividir texto se necessário
def split_text(text, max_length=400):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

text_chunks = split_text(input_text, max_length=400)

# Processar cada pedaço
for i, chunk in enumerate(text_chunks, 1):
    print(f"Processando pedaço {i}/{len(text_chunks)}...")
    response = llm(chunk, max_tokens=100, stop=["###"])  # Ajuste max_tokens conforme necessário
    print(f"Resposta do pedaço {i}:")
    print(response["choices"][0]["text"])

