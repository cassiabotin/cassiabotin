import tkinter as tk
from tkinter import messagebox
 
 
# ==== Classes ====
 
class Cliente:
    def __init__(self, nome, cpf, idade, telefone, endereco, email):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
 
 
class Processo:
    def __init__(self, numero, descricao, cliente_cpf):
        self.numero = numero
        self.descricao = descricao
        self.cliente_cpf = cliente_cpf
 
 
class Pagamento:
    def __init__(self, cliente_cpf, valor, descricao):
        self.cliente_cpf = cliente_cpf
        self.valor = valor
        self.descricao = descricao
 
 
# ==== Listas de dados ====
 
clientes = []
processos = []
pagamentos = []
 
 
# ==== Funções do sistema ====
 
# ----- Clientes -----
 
def cadastrar_cliente():
    janela = tk.Toplevel()
    janela.title("Cadastrar Cliente")
    janela.geometry("400x450")
 
    labels = ["Nome", "CPF", "Idade", "Telefone", "Endereço", "Email"]
    entradas = []
 
    for label in labels:
        tk.Label(janela, text=label).pack()
        entrada = tk.Entry(janela)
        entrada.pack()
        entradas.append(entrada)
 
    def salvar_cliente():
        try:
            nome = entradas[0].get()
            cpf = entradas[1].get()
            idade = int(entradas[2].get())
            telefone = entradas[3].get()
            endereco = entradas[4].get()
            email = entradas[5].get()
 
            if not nome or not cpf:
                messagebox.showerror("Erro", "Nome e CPF são obrigatórios!")
                return
 
            cliente = Cliente(nome, cpf, idade, telefone, endereco, email)
            clientes.append(cliente)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            janela.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número inteiro.")
 
    tk.Button(janela, text="Salvar Cliente", command=salvar_cliente).pack(pady=10)
 
 
def buscar_cliente():
    janela = tk.Toplevel()
    janela.title("Buscar Cliente")
    janela.geometry("400x300")
 
    tk.Label(janela, text="Digite o CPF do cliente:").pack(pady=5)
    entrada_cpf = tk.Entry(janela)
    entrada_cpf.pack()
 
    def buscar():
        cpf = entrada_cpf.get().strip()
        encontrado = None
        for cliente in clientes:
            if cliente.cpf == cpf:
                encontrado = cliente
                break
 
        if encontrado:
            info = f"""
            Nome: {encontrado.nome}
            CPF: {encontrado.cpf}
            Idade: {encontrado.idade}
            Telefone: {encontrado.telefone}
            Endereço: {encontrado.endereco}
Email: {encontrado.email}
"""
            messagebox.showinfo("Cliente Encontrado", info)
        else:
            messagebox.showerror("Erro", "Cliente não encontrado.")
 
    tk.Button(janela, text="Buscar", command=buscar).pack(pady=10)
 
 
# ----- Processos -----
 
def cadastrar_processo():
    janela = tk.Toplevel()
    janela.title("Cadastrar Processo")
    janela.geometry("400x350")
 
    tk.Label(janela, text="Número do Processo:").pack()
    entrada_numero = tk.Entry(janela)
    entrada_numero.pack()
 
    tk.Label(janela, text="Descrição do Processo:").pack()
    entrada_descricao = tk.Entry(janela)
    entrada_descricao.pack()
 
    tk.Label(janela, text="CPF do Cliente:").pack()
    entrada_cpf = tk.Entry(janela)
    entrada_cpf.pack()
 
    def salvar_processo():
        numero = entrada_numero.get().strip()
        descricao = entrada_descricao.get().strip()
        cpf = entrada_cpf.get().strip()
 
        if not numero or not descricao or not cpf:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
 
        cliente_existe = any(cliente.cpf == cpf for cliente in clientes)
 
        if not cliente_existe:
            messagebox.showerror("Erro", "CPF do cliente não encontrado.")
            return
 
        processo = Processo(numero, descricao, cpf)
        processos.append(processo)
        messagebox.showinfo("Sucesso", "Processo cadastrado com sucesso!")
        janela.destroy()
 
    tk.Button(janela, text="Salvar Processo", command=salvar_processo).pack(pady=10)
 
 
def buscar_processo():
    janela = tk.Toplevel()
    janela.title("Buscar Processo")
    janela.geometry("400x300")
 
    tk.Label(janela, text="Digite o número do processo:").pack(pady=5)
    entrada_numero = tk.Entry(janela)
    entrada_numero.pack()
 
    def buscar():
        numero = entrada_numero.get().strip()
        encontrado = None
        for processo in processos:
            if processo.numero == numero:
                encontrado = processo
                break
 
        if encontrado:
            info = f"""
Número: {encontrado.numero}
Descrição: {encontrado.descricao}
CPF do Cliente: {encontrado.cliente_cpf}
"""
            messagebox.showinfo("Processo Encontrado", info)
        else:
            messagebox.showerror("Erro", "Processo não encontrado.")
 
    tk.Button(janela, text="Buscar", command=buscar).pack(pady=10)
 
 
# ----- Pagamentos -----
 
def cadastrar_pagamento():
    janela = tk.Toplevel()
    janela.title("Cadastrar Pagamento")
    janela.geometry("400x350")
 
    tk.Label(janela, text="CPF do Cliente:").pack()
    entrada_cpf = tk.Entry(janela)
    entrada_cpf.pack()
 
    tk.Label(janela, text="Valor do Pagamento:").pack()
    entrada_valor = tk.Entry(janela)
    entrada_valor.pack()
 
    tk.Label(janela, text="Descrição do Pagamento:").pack()
    entrada_descricao = tk.Entry(janela)
    entrada_descricao.pack()
 
    def salvar_pagamento():
        cpf = entrada_cpf.get().strip()
        try:
            valor = float(entrada_valor.get().strip())
        except ValueError:
            messagebox.showerror("Erro", "Valor deve ser numérico.")
            return
        descricao = entrada_descricao.get().strip()
 
        cliente_existe = any(cliente.cpf == cpf for cliente in clientes)
 
        if not cliente_existe:
            messagebox.showerror("Erro", "CPF do cliente não encontrado.")
            return
 
        pagamento = Pagamento(cpf, valor, descricao)
        pagamentos.append(pagamento)
        messagebox.showinfo("Sucesso", "Pagamento cadastrado com sucesso!")
        janela.destroy()
 
    tk.Button(janela, text="Salvar Pagamento", command=salvar_pagamento).pack(pady=10)
 
# ==== NOVA FUNÇÃO ADICIONADA ====
def buscar_pagamentos_por_cpf():
    janela = tk.Toplevel()
    janela.title("Buscar Pagamentos por CPF")
    janela.geometry("400x300")
 
    tk.Label(janela, text="Digite o CPF do cliente:").pack(pady=5)
    entrada_cpf = tk.Entry(janela)
    entrada_cpf.pack()
 
    def buscar():
        cpf = entrada_cpf.get().strip()
        pagamentos_encontrados = []
        for pagamento in pagamentos:
            if pagamento.cliente_cpf == cpf:
                pagamentos_encontrados.append(pagamento)
 
        if pagamentos_encontrados:
            nome_cliente = "Nome não encontrado"
            for cliente in clientes:
                if cliente.cpf == cpf:
                    nome_cliente = cliente.nome
                    break
            
            info = f"Pagamentos para o cliente: {nome_cliente} (CPF: {cpf})\n"
            info += "--------------------------------------\n"
            total_pago = 0
            for pag in pagamentos_encontrados:
                info += f"Valor: R$ {pag.valor:.2f}\n"
                info += f"Descrição: {pag.descricao}\n"
                info += "--------------------------------------\n"
                total_pago += pag.valor
            
            info += f"\nTOTAL PAGO: R$ {total_pago:.2f}"
 
            messagebox.showinfo("Pagamentos Encontrados", info)
        else:
            messagebox.showerror("Erro", "Nenhum pagamento encontrado para este CPF.")
 
    tk.Button(janela, text="Buscar", command=buscar).pack(pady=10)
 
 
# ==== Janela Principal ====
 
janela = tk.Tk()
janela.title("Sistema - Escritório de Advocacia")
janela.geometry("500x500")
janela.resizable(False, False)
 
tk.Label(
    janela,
    text="Sistema de Gestão Jurídica",
    font=("Arial", 16, "bold")
).pack(pady=20)
 
tk.Button(janela, text="Cadastrar Cliente", width=30, command=cadastrar_cliente).pack(pady=5)
tk.Button(janela, text="Buscar Cliente (CPF)", width=30, command=buscar_cliente).pack(pady=5)
 
tk.Button(janela, text="Cadastrar Processo", width=30, command=cadastrar_processo).pack(pady=5)
tk.Button(janela, text="Buscar Processo", width=30, command=buscar_processo).pack(pady=5)
 
tk.Button(janela, text="Cadastrar Pagamento", width=30, command=cadastrar_pagamento).pack(pady=5)
# ==== NOVO BOTÃO ADICIONADO ====
tk.Button(janela, text="Buscar Pagamentos (CPF)", width=30, command=buscar_pagamentos_por_cpf).pack(pady=5)
 
 
tk.Button(janela, text="Sair", width=30, command=janela.destroy).pack(pady=30)
 
janela.mainloop()