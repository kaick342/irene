
nlista=[]
slista=[]
horalista=[]
while True:
    nome=input("digite um nome:")
    nlista.append(nome)
    salário= int(input("digite seu salário:"))
    slista.append(salário)
    horas=float(input("digite quantas horas esse funcionario trabalha?:"))
    horalista.append(horas)
    dec=input("deseja continuar S/N:")
    dec=dec.lower()
    if dec == "s":
        print("RENICIANDO")
    elif dec == "n":
        print("teste")
        break
print("=================="*10)
dec1=input("deseja visualizar o Salário, nome e INSS do funcionário? S/N:")
dec1=dec1.lower()
if dec1 == "s":
    dec2=int(input("deseja visualizar qual ordem de funcionário?:"))-1
valorhr=salário/horas
if salário <= 1412:
    inss=(salário*7.5)/100
elif salário > 1412 and salário < 2666:
    inss=(salário*9)/100
elif salário > 2666 and salário < 4000:
    inss=(salário*12)/100
elif salário > 4000:
    inss=(salário*14)/100
total=salário-inss
print("O funcionário: {}, com o id {},tem o salário: {}, por hora ganha: {}, de inss será pago {}, totalizando:".format(nlista[dec2],dec2+1, slista[dec2], valorhr, inss, total))