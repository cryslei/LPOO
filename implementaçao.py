import random
class Pessoa:
    def __init__(self,nome):
        self.nome = nome
class Inscricao:
    def __init__(self):
        self.valor = 0
class InscricaoDeAluno(Inscricao):
    def __init__(self,universidade):
        super().__init__()
        self.valor = 50
        self.universidade = universidade
class InscricaoDeProfessor(Inscricao):
    def __init__(self,universidade):
        super().__init__()
        self.valor = 100
        self.universidade = universidade
class InscricaoDeProfissional(Inscricao):
    def __init__(self,empresa):
        super().__init__()
        self.valor = 200
        self.empresa = empresa
class Encoinfo:
    def __init__(self):
        self.inscritos = []
class Inscrito:
    def __init__(self,pessoa,inscricao):
        self.pessoa = pessoa
        self.inscricao = inscricao
class Atendente(Pessoa):
    def __init__(self,nome,encoinfo):
        super().__init__(nome)
        self.encoinfo = encoinfo
    def atender (self,pessoa,inscricao):
        if len(self.encoinfo.inscritos) < 50:
            self.encoinfo.inscritos.append(Inscrito(pessoa,inscricao))
        else:
            self.emitir_relatorio()
    def emitir_relatorio(self):
        ca = 0
        cprof = 0
        cprofi = 0
        for i in self.encoinfo.inscritos:
            if type(i.inscricao) == InscricaoDeAluno:
                ca+=1
            elif type(i.inscricao) == InscricaoDeProfessor:
                cprof+=1
            else:
                cprofi+=1
        largura = 40
        print('=' * (largura-11))
        print('** Relatório **'.center(largura))
        largura_matricula = int(.33 * largura)
        largura_nome = int(.33 * largura)
        largura_funcao = int(.33 * largura)
        print('+{}+{}+{}+'.format('-' * largura_matricula,'-' * largura_nome, '-' * largura_funcao))
        print(' |{:^{lm}}|{:^{ln}}|{:^{lf}}|'.format('Aluno', 'Professor', 'Profissional',lm=largura_matricula+3, ln=largura_nome+2, lf=largura_funcao+1))
        print('+{}+{}+{}+'.format('-' * largura_matricula,'-' * largura_nome, '-' * largura_funcao))
        print(' |{:^{lm}}|{:^{ln}}|{:^{lf}}|'.format(ca,cprof,cprofi,lm=largura_matricula+5, ln=largura_nome+6, lf=largura_funcao+5))
        print('+{}+{}+{}+'.format('-' * largura_matricula,'-' * largura_nome, '-' * largura_funcao))

def cadastro(atendente,tipo):
    if tipo == 1:
        atendente.atender(p,InscricaoDeAluno('ULBRA'))
    elif tipo == 2:
        atendente.atender(p,InscricaoDeProfessor('uft'))
    else:
        atendente.atender(p,InscricaoDeProfissional('ULBRA'))
e = Encoinfo()
a = Atendente('Maria',e)
a2 = Atendente('José',e)
a3 = Atendente('Carlos',e)
contAt1= 0
contAt2= 0
contAt3= 0
for n in range(1,52):
    p =Pessoa('joao'+str(n))
    x = random.randint(0,100)
    tipo = random.randint(1,3)
    if x <= 33:
        cadastro(a,tipo)
        contAt1+=1
    elif x > 33 and x <= 66:
        cadastro(a2,tipo)
        contAt2+=1
    elif x > 66:
        cadastro(a3,tipo)
        contAt3+=1
largura = 40
print('** Pessoas Atendidas por bancada **'.center(largura))
largura_matricula = int(.33 * largura)
largura_nome = int(.33 * largura)
largura_funcao = int(.33 * largura)
print('+{}+{}+{}+'.format('-' * largura_matricula,'-' * largura_nome, '-' * largura_funcao))
print(' |{:^{lm}}|{:^{ln}}|{:^{lf}}|'.format(a.nome, a2.nome, a3.nome,lm=largura_matricula+3, ln=largura_nome+4, lf=largura_funcao+2))
print('+{}+{}+{}+'.format('-' * largura_matricula,'-' * largura_nome, '-' * largura_funcao))
print(' |{:^{lm}}|{:^{ln}}|{:^{lf}}|'.format(contAt1,contAt2,contAt3,lm=largura_matricula+5, ln=largura_nome+6, lf=largura_funcao+5))
print('+{}+{}+{}+'.format('-' * largura_matricula,'-' * largura_nome, '-' * largura_funcao))

