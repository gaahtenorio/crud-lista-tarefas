import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk

# Conexão com o banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua-senha",
    database="lista_tarefas"
)
cursor = db.cursor()

# ---------- FUNÇÕES CRUD ----------
def adicionar_tarefa():
    titulo = entry_titulo.get()
    descricao = entry_descricao.get()
    if titulo.strip() == "":
        messagebox.showwarning("Aviso", "O título não pode ficar vazio")
        return
    sql = "INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s)"
    val = (titulo, descricao)
    cursor.execute(sql, val)
    db.commit()
    messagebox.showinfo("Sucesso", "Tarefa adicionada")
    listar_tarefas()

def listar_tarefas():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT id, titulo, status FROM tarefas")
    for tarefa in cursor.fetchall():
        tree.insert("", END, values=tarefa)

def atualizar_tarefa():
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma tarefa")
        return
    tarefa_id = tree.item(selecionado[0])['values'][0]
    titulo = entry_titulo.get()
    descricao = entry_descricao.get()
    status = var_status.get()
    sql = "UPDATE tarefas SET titulo=%s, descricao=%s, status=%s WHERE id=%s"
    val = (titulo, descricao, status, tarefa_id)
    cursor.execute(sql, val)
    db.commit()
    messagebox.showinfo("Sucesso", "Tarefa atualizada")
    listar_tarefas()

def deletar_tarefa():
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma tarefa")
        return
    tarefa_id = tree.item(selecionado[0])['values'][0]
    sql = "DELETE FROM tarefas WHERE id=%s"
    cursor.execute(sql, (tarefa_id,))
    db.commit()
    messagebox.showinfo("Sucesso", "Tarefa deletada")
    listar_tarefas()

def marcar_concluida():
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma tarefa")
        return
    tarefa_id = tree.item(selecionado[0])['values'][0]
    sql = "UPDATE tarefas SET status='concluída' WHERE id=%s"
    cursor.execute(sql, (tarefa_id,))
    db.commit()
    messagebox.showinfo("Sucesso", "Tarefa marcada como concluída")
    listar_tarefas()

def preencher_campos(event):
    selecionado = tree.selection()
    if not selecionado:
        return
    tarefa_id = tree.item(selecionado[0])['values'][0]
    cursor.execute("SELECT titulo, descricao, status FROM tarefas WHERE id=%s", (tarefa_id,))
    tarefa = cursor.fetchone()
    entry_titulo.delete(0, END)
    entry_titulo.insert(0, tarefa[0])
    entry_descricao.delete(0, END)
    entry_descricao.insert(0, tarefa[1])
    var_status.set(tarefa[2])

# ---------- INTERFACE GRÁFICA ----------
root = Tk()
root.title("Lista de Tarefas")
root.geometry("600x450")
root.configure(bg="#1e3f66")  # cor azul de fundo

# Títulos e campos
Label(root, text="Título:", bg="#1e3f66", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
entry_titulo = Entry(root, width=50, font=("Arial", 12))
entry_titulo.pack(pady=5)

Label(root, text="Descrição:", bg="#1e3f66", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
entry_descricao = Entry(root, width=50, font=("Arial", 12))
entry_descricao.pack(pady=5)

var_status = StringVar(value="pendente")
Label(root, text="Status:", bg="#1e3f66", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
status_menu = OptionMenu(root, var_status, "pendente", "concluída")
status_menu.config(width=20, font=("Arial", 12))
status_menu.pack(pady=5)

# Botões
frame_botoes = Frame(root, bg="#1e3f66")
frame_botoes.pack(pady=10)

Button(frame_botoes, text="Adicionar", command=adicionar_tarefa, width=15, bg="#3b6ea5", fg="white").grid(row=0, column=0, padx=5, pady=2)
Button(frame_botoes, text="Atualizar", command=atualizar_tarefa, width=15, bg="#3b6ea5", fg="white").grid(row=0, column=1, padx=5, pady=2)
Button(frame_botoes, text="Deletar", command=deletar_tarefa, width=15, bg="#3b6ea5", fg="white").grid(row=0, column=2, padx=5, pady=2)
Button(frame_botoes, text="Marcar Concluída", command=marcar_concluida, width=15, bg="#3b6ea5", fg="white").grid(row=0, column=3, padx=5, pady=2)

# Lista de tarefas usando Treeview (mais bonita que Listbox)
tree = ttk.Treeview(root, columns=("ID", "Título", "Status"), show="headings", height=10)
tree.heading("ID", text="ID")
tree.heading("Título", text="Título")
tree.heading("Status", text="Status")
tree.column("ID", width=50, anchor=CENTER)
tree.column("Título", width=350)
tree.column("Status", width=100, anchor=CENTER)
tree.pack(pady=10)
tree.bind("<<TreeviewSelect>>", preencher_campos)

# Customizando cores da Treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#cce0ff", foreground="black", rowheight=25, fieldbackground="#cce0ff")
style.map("Treeview", background=[("selected", "#1e90ff")], foreground=[("selected", "white")])

listar_tarefas()
root.mainloop()
