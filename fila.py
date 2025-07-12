class No:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Fila:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def enfileirar(self, no):
        if self.size<=0:
            self.first = no
        else:
            self.last.next = no
        self.last = no
        self.size += 1

    def __str__(self):
        if self.first is not None:
            no = self.first
            pilha_filagem = []
            while no is not None:
                pilha_filagem.append(f"{no.valor}")
                no = no.next
            return " -> ".join(pilha_filagem)
        else:
            return "A fila está vazia"
        
    def desenfileirar(self):
        if self.size>0:
            self.first = self.first.next
            self.size-=1

    def showFirst(self):
        if self.first is not None:
            return self.first.valor
        else:
            return "A fila está vazia"
        
    def showSize(self):
        return self.size


if __name__ == "__main__":
    fila = Fila()
    print(fila)
    fila.enfileirar(No(5))
    fila.enfileirar(No(4))
    fila.enfileirar(No(3))
    fila.enfileirar(No(2))
    fila.enfileirar(No(1))
    print(fila)
    print(f"O tamanho da fila é: {fila.showSize()}")
    print(f"O topo da fila é: {fila.showFirst()}")
    print('\n')
    fila.desenfileirar()
    print(fila)
    print(f"O tamanho da fila é: {fila.showSize()}")
    print(f"O topo da fila é: {fila.showFirst()}")