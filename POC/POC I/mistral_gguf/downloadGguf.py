from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="TheBloke/Llama-2-7B-Chat-GGUF",
    local_dir="./llama_gguf",
    allow_patterns=["llama-2-7b-chat.Q5_K_M.gguf"]
)
