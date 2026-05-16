import sys
from weather_service import obter_clima

TAREFAS = []

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
    print("Bem-vindo ao GoNext Lite!")
    
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
                TAREFAS.append({"titulo": titulo, "concluida": False})
                print(f"✅ Tarefa '{titulo}' adicionada com sucesso!")
            else:
                print("❌ Erro: O título não pode ser vazio.")
                
        elif opcao == "2":
            if not TAREFAS:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("\n📋 SUAS TAREFAS:")
                for i, tarefa in enumerate(TAREFAS, start=1):
                    status = "🟩 [Concluída]" if tarefa["concluida"] else "🟥 [Pendente]"
                    print(f"{i}. {tarefa['titulo']} - {status}")
                    
        elif opcao == "3":
            if not TAREFAS:
                print("Nenhuma tarefa para concluir.")
                continue
            try:
                num = int(input("Número da tarefa que deseja concluir: "))
                if 1 <= num <= len(TAREFAS):
                    TAREFAS[num-1]["concluida"] = True
                    print(f"✅ Tarefa '{TAREFAS[num-1]['titulo']}' concluída!")
                else:
                    print("❌ Número de tarefa inválido.")
            except ValueError:
                print("❌ Por favor, digite um número válido.")
                
        elif opcao == "4":
            print("Saindo do GoNext Lite. Até logo! 🚀")
            sys.exit(0)
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()