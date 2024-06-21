def senha():
    senha_correta = "3443"
    max_tentativas = 3
    tentativas = 0

    while tentativas < max_tentativas:
        input_senha = input("Senha: ")

        if input_senha == senha_correta:
            print("Bem-vindo!")
            return

        print ("Erro: senha incorreta")
        tentativas += 1

    print("Erro: conta suspensa após 3 tentativas incorretas")

senha()