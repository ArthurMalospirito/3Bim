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
        print(f"elemento {no.valor} inserido")

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
            return self.top.valor
        else:
            return "A pilha está vazia"
        
    def tamanho(self):
        return self.size

if __name__ == "__main__":
    pilha = Pilha()
    print(pilha)
    pilha.push(No(1))
    pilha.push(No(3))
    pilha.push(No(4))
    pilha.pop()

    print(f"O tamanho da pilha é: {pilha.tamanho()}")
    print(f"O topo da pilha é: {pilha.topo()}")

    print(pilha)
 