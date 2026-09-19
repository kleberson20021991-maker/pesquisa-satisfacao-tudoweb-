def realizar_pesquisa():
    TOTAL_ENTREVISTADOS = 50
    
    qtd_excelente = 0
    qtd_ruim = 0

    print(f"--- INÍCIO DA PESQUISA DE OPINIÃO (TudoWeb) ---")
    print(f"Total de entrevistados previstos: {TOTAL_ENTREVISTADOS}\n")

    for i in range(1, TOTAL_ENTREVISTADOS + 1):
        print(f"--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
        
        nome = input("Digite o nome do entrevistado: ")
        
        try:
            idade = int(input("Digite a idade do entrevistado: "))
        except ValueError:
            print("Idade inválida. Considerando 0.")
            idade = 0

        while True:
            try:
                opiniao = int(input("Digite a opinião sobre o atendimento:\n[1] EXCELENTE\n[2] BOM\n[3] RUIM\nOpção: "))
                if opiniao in [1, 2, 3]:
                    break
                else:
                    print("Opção inválida! Digite apenas 1, 2 ou 3.")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro (1, 2 ou 3).")

        if opiniao == 1:
            qtd_excelente += 1
        elif opiniao == 3:
            qtd_ruim += 1

        print("-" * 35 + "\n")

    print("=" * 40)
    print("          RESULTADO DA PESQUISA")
    print("=" * 40)
    print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
    print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
    print("=" * 40)

if __name__ == "__main__":
    realizar_pesquisa()
