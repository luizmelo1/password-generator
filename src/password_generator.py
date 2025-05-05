import secrets
import tkinter as tk
from tkinter import ttk, messagebox

# Configurações de caracteres
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_characters = "!@#$%^&*()-_=+[]{}/;:,.<>?"
all_chars = upper_case + lower_case + numbers + special_characters
rng = secrets.SystemRandom()

def gerar_senha(tamanho):
    while True:
        senha = "".join(rng.choices(all_chars, k=tamanho))
        if (any(c in upper_case for c in senha) and \
           any(c in lower_case for c in senha) and \
           any(c in numbers for c in senha) and \
           any(c in special_characters for c in senha)):
            return senha

class AppSenhas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Senhas Seguras")
        self.root.geometry("450x400")
        
        # Variáveis de estado
        self.senhas_geradas = []
        self.contador = 1
        
        self.criar_interface()
        
    def criar_interface(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configurar expansão
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Seção de entrada
        lbl_instrucao = ttk.Label(main_frame, text="Digite a quantidade de caracteres que deseja:")
        lbl_instrucao.grid(row=0, column=0, sticky=tk.E, pady=5)
        
        self.entrada = ttk.Entry(main_frame, width=5)
        self.entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Botão de geração
        btn_gerar = ttk.Button(main_frame, text="Gerar Senha", command=self.gerar)
        btn_gerar.grid(row=0, column=2, padx=10, pady=5, sticky=tk.E)
        
        # Exibição da senha
        self.senha_atual = ttk.Entry(
            main_frame,
            width=35,
            font=('Arial', 12),
            state='readonly'
        )
        self.senha_atual.grid(row=1, column=0, columnspan=3, pady=10, sticky=tk.EW)
        
        # Botão de cópia
        btn_copiar = ttk.Button(main_frame, text="Copiar Senha", command=self.copiar)
        btn_copiar.grid(row=2, column=0, columnspan=3, pady=5, sticky=tk.EW)
        
        # Histórico com scrollbar
        frame_historico = ttk.Frame(main_frame)
        frame_historico.grid(row=3, column=0, columnspan=3, sticky=tk.NSEW, pady=5)
        
        self.historico = tk.Listbox(
            frame_historico,
            width=40,
            height=8,
            font=('Arial', 10)
        )
        
        scrollbar = ttk.Scrollbar(
            frame_historico,
            orient=tk.VERTICAL,
            command=self.historico.yview
        )
        self.historico.configure(yscrollcommand=scrollbar.set)
        
        # Layout do histórico
        self.historico.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Botão de saída
        btn_sair = ttk.Button(main_frame, text="Sair", command=self.sair)
        btn_sair.grid(row=4, column=2, sticky=tk.E, pady=10)

    def gerar(self):
        try:
            tamanho = int(self.entrada.get())
            if tamanho < 4:
                messagebox.showerror("Erro", "A senha deve ter pelo menos 4 caracteres!")
                return
                
            nova_senha = gerar_senha(tamanho)
            self.senha_atual.config(state='normal')
            self.senha_atual.delete(0, tk.END)
            self.senha_atual.insert(0, nova_senha)
            self.senha_atual.config(state='readonly')
            
            self.senhas_geradas.append(f"Senha {self.contador}: {nova_senha}")
            self.contador += 1
            self.historico.insert(tk.END, nova_senha)  # Adiciona no final da lista
            
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido!")

    def copiar(self):
        senha = self.senha_atual.get()
        if senha:
            self.root.clipboard_clear()
            self.root.clipboard_append(senha)
            messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")

    def sair(self):
        if self.senhas_geradas:
            messagebox.showinfo("Histórico Completo", "\n".join(self.senhas_geradas))
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppSenhas(root)
    root.mainloop()