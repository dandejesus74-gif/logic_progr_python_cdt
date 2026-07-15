''
def como_trocar_pneu(estado_pneu):
    """
    Função para verificar se precisa trocar o pneu e mostrar o passo a passo
    estado_pneu: 'furado' ou 'bom'
    """
    estado_pneu = estado_pneu.lower().strip()  # deixa tudo minúsculo e tira espaço

    if estado_pneu == 'furado':
        print("=== TROCANDO O PNEU ===")
        print("1. Estacione o carro em um local seguro.")
        print("2. Acione o freio de mão.")
        print("3. Pegue o macaco e a chave de roda.")
        print("4. Afrouxe os parafusos da roda.")
        print("5. Levante o carro com o macaco.")
        print("6. Retire a roda com o pneu furado.")
        print("7. Coloque o estepe.")
        print("8. Aperte os parafusos.")
        print("9. Abaixe o carro.")
        print("10. Aperte os parafusos novamente.")
        print("Pneu trocado com sucesso! ✅")
        resultado = 'pneu trocado'
    
    elif estado_pneu == 'bom':
        print("O pneu não está furado. Não é necessário trocar. 👍")
        resultado = 'pneu ainda bom'
    
    else:
        print('Estado inválido! Digite "furado" ou "bom"')
        resultado = None

    return resultado

# ===== TESTES =====
print("Teste 1:")
pneu1 = como_trocar_pneu('furado')  
print(f'Meu carro está: {pneu1}\n')

print("Teste 2:")
pneu2 = como_trocar_pneu('bom')  
print(f'Meu carro está: {pneu2}\n')

