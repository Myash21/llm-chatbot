from langchain.llms import Ollama
ollama = Ollama(base_url = "http://localhost:11434", model = "agri-mate")
q = input("Enter your question:")
print(ollama.invoke(q))