class No:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, no):
        no.next = self.top
        self.top = no
        self.size += 1

    def __str__(self):
        if self.top is not None:
            no = self.top
            pilha_listagem = []
            while no is not None:
                pilha_listagem.append(f"{no.valor}")
                no = no.next
            return "\n-----\n".join(pilha_listagem)
        else:
            return "a pilha está vazia"
        
    def pop(self):
        if self.size>0:
            self.top = self.top.next
            self.size-=1

    def topo(self):
        if self.top is not None:
            return self.top
        else:
            return "A pilha está vazia"
        
    def tamanho(self):
        return self.size
 

notacaoPolonesa =input("Digite a notação polonesa (separe os elementos com espaço) \n")
notacaoDecomposta =[]

valor=""

for elemento in notacaoPolonesa:
    
    if elemento==notacaoPolonesa[-1]:
        valor+=elemento
        notacaoDecomposta.append(valor)
        valor=""
    else:
        if elemento==" ":
            notacaoDecomposta.append(valor)
            valor=""
        else:
            valor+=elemento

listaChar = ("*","/","+","-")
pilhaElementos = Pilha()

for item in notacaoDecomposta:

    ultimo=0
    penultimo=0

    if item in listaChar:
        ultimo=pilhaElementos.topo()
        penultimo=ultimo.next

        pilhaElementos.pop()
        pilhaElementos.pop()

        match item:
            case "*":

                pilhaElementos.push(No(penultimo.valor*ultimo.valor))
            
            case "+":

                pilhaElementos.push(No(penultimo.valor+ultimo.valor))

            case "-":

                pilhaElementos.push(No(penultimo.valor-ultimo.valor))

            case "/":

                pilhaElementos.push(No(penultimo.valor/ultimo.valor))

            case _:
                print("Operação não suportada")            
    else:
        pilhaElementos.push(No(float(item)))

print(f"\n ----------------------------------\n")
print(f"O resultado da operação é: {pilhaElementos.topo().valor}")