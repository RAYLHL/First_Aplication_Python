#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular 
        self.saldo = saldo 
        self.ativo = False

    def __str__(self):
        status = 'Ativo ' if self.ativo else 'Não ativo'
        return f' Titular da conta: {self.titular}\n Saldo da conta: {self.saldo}\n {status}'
    
conta_bancaria = ContaBancaria('Rayltson',1000)

print(conta_bancaria)



#Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
#ja feito no de cima 

#Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular 
        self.saldo = saldo 
        self.ativo = True

    def __str__(self):
        status = "Ativa ✅" if self.ativo else "Inativa ❌"
        return f' Titular da conta: {self.titular}\n Saldo da conta: {self.saldo}\n Status: {status}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True
    
conta_bancaria = ContaBancaria('Rayltson',1000)
ContaBancaria.ativar_conta(conta_bancaria)
print(conta_bancaria)

#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.



#Crie uma instância da classe e imprima o valor da propriedade titular.




#Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.





#Crie um método de classe para a conta ClienteBanco.