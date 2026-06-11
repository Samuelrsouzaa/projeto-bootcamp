import sys
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from weather_service import obter_clima

# Load environment variables from .env file
load_dotenv()

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL", "")
key: str = os.environ.get("SUPABASE_KEY", "")
supabase: Client = create_client(url, key) if url and key else None

def exibir_menu():
    print("\n" + "="*35)
    print("      GoNext Lite - GERENCIADOR      ")
    print("="*35)
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Sair")
    print("="*35)

def main():
    print("Bem-vindo ao GoNext Lite integrado com Banco de Dados!")
    
    if not supabase:
        print("⚠️  Aviso: As variáveis SUPABASE_URL e SUPABASE_KEY não foram encontradas no arquivo .env.")
        print("Certifique-se de configurar o arquivo .env corretamente para o banco funcionar.")
    
    cidade = input("Digite sua cidade para verificar o clima atual (ou Enter para pular): ")
    if cidade.strip():
        print(f"Buscando informações climáticas para {cidade}...")
        status_clima = obter_clima(cidade)
        print(f"\n🌤️  Clima atual em {cidade}: {status_clima}")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            titulo = input("Título da tarefa: ").strip()
            if titulo:
                if supabase:
                    try:
                        data, count = supabase.table("tarefas").insert({"titulo": titulo, "concluida": False}).execute()
                        print(f"✅ Tarefa '{titulo}' salva na nuvem com sucesso!")
                    except Exception as e:
                        print(f"❌ Erro ao salvar no banco: {e}")
                else:
                    print("❌ Erro: Supabase não configurado.")
            else:
                print("❌ Erro: O título não pode ser vazio.")
                
        elif opcao == "2":
            if supabase:
                try:
                    response = supabase.table("tarefas").select("*").order("id").execute()
                    tarefas = response.data
                    if not tarefas:
                        print("Nenhuma tarefa cadastrada no banco.")
                    else:
                        print("\n📋 SUAS TAREFAS NA NUVEM:")
                        for tarefa in tarefas:
                            status = "🟩 [Concluída]" if tarefa.get("concluida") else "🟥 [Pendente]"
                            print(f"[{tarefa['id']}] {tarefa['titulo']} - {status}")
                except Exception as e:
                    print(f"❌ Erro ao listar tarefas: {e}")
            else:
                print("❌ Erro: Supabase não configurado.")
                    
        elif opcao == "3":
            if supabase:
                try:
                    num = input("ID da tarefa que deseja concluir: ").strip()
                    if num.isdigit():
                        response = supabase.table("tarefas").update({"concluida": True}).eq("id", int(num)).execute()
                        if response.data:
                            print(f"✅ Tarefa ID {num} marcada como concluída na nuvem!")
                        else:
                            print("❌ Tarefa não encontrada com esse ID.")
                    else:
                        print("❌ ID inválido. Digite o número que aparece entre colchetes [].")
                except Exception as e:
                    print(f"❌ Erro ao atualizar tarefa: {e}")
            else:
                 print("❌ Erro: Supabase não configurado.")
                
        elif opcao == "4":
            print("Saindo do GoNext Lite. Até logo! 🚀")
            sys.exit(0)
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()