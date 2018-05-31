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
        self.valor = 80
        self.universidade = universidade
class InscricaoDeProfissional(Inscricao):
    def __init__(self,empresa):
        super().__init__()
        self.valor = 120
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
        if len(self.encoinfo.inscritos) < 100:
            self.encoinfo.inscritos.append(Inscrito(pessoa,inscricao))
        else:
            self.emitir_relatorio()
    def emitir_relatorio(self):
        ca = 0
        cprof = 0
        cprofi = 0
        total = 0
        totalAluno = 0
        totalProfessor =0
        totalProfissional = 0
##        lista =[0,0,0]
        for i in self.encoinfo.inscritos:
            if type(i.inscricao) == InscricaoDeAluno:
                totalAluno+= i.inscricao.valor
                ca+=1
            elif type(i.inscricao) == InscricaoDeProfessor:
                totalProfessor+= i.inscricao.valor
                cprof+=1
            else:
                totalProfissional+= i.inscricao.valor
                cprofi+=1
            total +=  i.inscricao.valor

        largura = 120
        print('=' * 60)
        print('** Relatório **'.center(largura))
        largura_nome = int(.20 * largura)
        largura_qnt = int(.16* largura)
        largura_aluno = int(.10 * largura)
        largura_prof = int(.13* largura)
        largura_profi = int(.13 * largura)
        largura_total = int(.10 * largura)
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_nome,'-' * largura_qnt, '-' * largura_aluno, '-' * largura_prof, '-' * largura_profi))
        print(' |{:^{na}}|{:^{qa}}|{:^{a}}|{:^{p}}|{:^{pf}}|'.format('Nome Atendente','Qnt. Atendidas','Aluno','Professor','Profissional',na=largura_nome,qa=largura_qnt,a=largura_aluno+4,p=largura_prof+2,pf=largura_profi+1))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_nome, '-' * largura_qnt, '-' * largura_aluno,'-' * largura_prof, '-' * largura_profi))
        print(' |{:^{na}}|{:^{qa}}|{:^{a}}|{:^{p}}|{:^{pf}}|'.format(a.nome,contAt1,listaAt1[0],listaAt1[1],listaAt1[2],'',na=largura_nome+7,qa=largura_qnt+8,a=largura_aluno+4,p=largura_prof+7,pf=largura_profi+7))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_nome, '-' * largura_qnt, '-' * largura_aluno,'-' * largura_prof, '-' * largura_profi))
        print(' |{:^{na}}|{:^{qa}}|{:^{a}}|{:^{p}}|{:^{pf}}|'.format(a2.nome,contAt2,listaAt2[0],listaAt2[1],listaAt2[2],'',na=largura_nome+7,qa=largura_qnt+8,a=largura_aluno+4,p=largura_prof+7,pf=largura_profi+7))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_nome, '-' * largura_qnt, '-' * largura_aluno,'-' * largura_prof, '-' * largura_profi))
        print(' |{:^{na}}|{:^{qa}}|{:^{a}}|{:^{p}}|{:^{pf}}|'.format(a3.nome,contAt3,listaAt3[0],listaAt3[1],listaAt3[2],'',na=largura_nome+7,qa=largura_qnt+8,a=largura_aluno+4,p=largura_prof+7,pf=largura_profi+7))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_nome, '-' * largura_qnt, '-' * largura_aluno,'-' * largura_prof, '-' * largura_profi))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_nome, '-' * largura_qnt, '-' * largura_aluno,'-' * largura_prof, '-' * largura_profi))
        print(' |{:^{na}}|{:^{qa}}|{:^{a}}|{:^{p}}|{:^{pf}}|'.format('Total',100,ca,cprof,cprofi,na=largura_nome+7,qa=largura_qnt+8,a=largura_aluno+4,p=largura_prof+7,pf=largura_profi+7))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_nome, '-' * largura_qnt, '-' * largura_aluno,'-' * largura_prof, '-' * largura_profi))
        
        print(' |{:^{na}}|{:^{qa}}|{:^{a}}|{:^{p}}|{:^{pf}}|'.format('Total Pago',total,totalAluno,totalProfessor,totalProfissional,na=largura_nome+3,qa=largura_qnt+5,a=largura_aluno+4,p=largura_prof+7,pf=largura_profi+4))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_nome, '-' * largura_qnt, '-' * largura_aluno,'-' * largura_prof, '-' * largura_profi))
        
def cadastro(atendente,tipo,lista):
    if tipo <= 70:
        atendente.atender(p,InscricaoDeAluno('ULBRA'))
        lista[0]+=1
    elif tipo >=70 and tipo<= 90:
        atendente.atender(p,InscricaoDeProfessor('uft'))
        lista[1]+=1
    else:
        atendente.atender(p,InscricaoDeProfissional('ULBRA'))
        lista[2]+=1
e = Encoinfo()
a = Atendente('Maria',e)
a2 = Atendente('José',e)
a3 = Atendente('Carlos',e)
contAt1= 0
contAt2= 0
contAt3= 0
contAtaluno = 0
contAtProf = 0
contAtProfi = 0
listaAt1 =[0,0,0]
listaAt2 =[0,0,0]
listaAt3 =[0,0,0]
for n in range(1,102):
    p =Pessoa('joao'+str(n))
    x = random.randint(0,100)
    tipo = random.randint(0,100)
    if x <= 33:
        cadastro(a,tipo,listaAt1)
        contAt1+=1
    elif x > 33 and x <= 66:
        cadastro(a2,tipo,listaAt2)
        contAt2+=1
    elif x > 66:
        cadastro(a3,tipo,listaAt3)
        contAt3+=1
