class ContaBancaria:
    def __init__(self, titular='', saldo=0, ativo=False):
        self._titular = titular.capitalize()
        self._saldo = saldo
        self._ativo = ativo

    def __str__(self):
        return f'Titular: {self._titular}, Saldo: {self._saldo}, Ativo: {self._ativo}'
    
    def ativar_conta(self):
        self._ativo = True
    
conta1 = ContaBancaria('pâmela', 500)
conta1.ativar_conta()
conta2 = ContaBancaria('Rogério')

print(conta1)
print(conta2)