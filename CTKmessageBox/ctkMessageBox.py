import tkinter as tk
from tkinter import ttk

# Funciones para cambiar el tema
def set_dark_theme():
    style.configure("TNotebook", background="#2c2f33")
    style.configure("TNotebook.Tab", background="#23272a", foreground="black")
    style.map("TNotebook.Tab", background=[("selected", "#7289da")], foreground=[("selected", "black")])
    style.configure("TFrame", background="#2c2f33")
    style.configure("Treeview.Heading", background="#23272a", foreground="white")
    style.configure("Treeview", background="#2c2f33", foreground="white", fieldbackground="#2c2f33")
    label_info.configure(background="#2c2f33", foreground="white")
    form_container.configure(style="TFrame")
    for widget in form_container.winfo_children():
        if isinstance(widget, tk.Label):
            widget.configure(background="#2c2f33", foreground="white")

def set_light_theme():
    style.configure("TNotebook", background="#f0f0f0")
    style.configure("TNotebook.Tab", background="#d9d9d9", foreground="black")
    style.map("TNotebook.Tab", background=[("selected", "#ffffff")], foreground=[("selected", "black")])
    style.configure("TFrame", background="#f0f0f0")
    style.configure("Treeview.Heading", background="#d9d9d9", foreground="black")
    style.configure("Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff")
    label_info.configure(background="#f0f0f0", foreground="black")
    form_container.configure(style="TFrame")
    for widget in form_container.winfo_children():
        if isinstance(widget, tk.Label):
            widget.configure(background="#f0f0f0", foreground="black")

# Crear la ventana principal
app = tk.Tk()
app.geometry("700x450")
app.title("Aplicación con Pestañas Verticales")

# Crear el menú
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

# Crear el submenú de temas
theme_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Tema", menu=theme_menu)
theme_menu.add_command(label="Oscuro", command=set_dark_theme)
theme_menu.add_command(label="Claro", command=set_light_theme)

# Aplicar estilos personalizados
style = ttk.Style()

# Estilo general del Notebook
style.configure("TNotebook", tabposition='wn', background="#2c2f33")

# Estilo de las pestañas con ancho fijo y colores mejorados
style.configure("TNotebook.Tab",
                font=("Arial", 11, "bold"),
                padding=[20, 12],
                width=15,  # Ancho uniforme para todas las pestañas
                background="#23272a",
                foreground="black",
                borderwidth=1)

# Estilo de la pestaña seleccionada
style.map("TNotebook.Tab",
          background=[("selected", "#7289da")],  # Azul en pestaña seleccionada
          foreground=[("selected", "black")])    # Texto negro en pestaña activa

# Crear el Notebook con pestañas verticales
notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill="both", padx=5, pady=5)

# Crear frames para cada pestaña
frame_table = ttk.Frame(notebook, style="TFrame")
frame_form = ttk.Frame(notebook, style="TFrame")
frame_info = ttk.Frame(notebook, style="TFrame")

# Agregar pestañas con el mismo ancho
notebook.add(frame_table, text=" Tabla ")
notebook.add(frame_form, text=" Formulario ")
notebook.add(frame_info, text=" Información ")

# Estilizar los frames internos
style.configure("TFrame", background="#2c2f33")

# ----- Contenido de la pestaña de Tabla -----
columns = ("ID", "Nombre", "Edad")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=8)

# Configurar encabezados de tabla con bordes simulados
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Edad", text="Edad")

# Aplicar estilo con bordes inferiores
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#23272a", foreground="white")
style.configure("Treeview", rowheight=30, font=("Arial", 11), background="#2c2f33", foreground="white", fieldbackground="#2c2f33")

# Insertar datos de ejemplo
data = [
    (1, "Juan", 25),
    (2, "María", 30),
    (3, "Carlos", 22),
]
for item in data:
    tree.insert("", "end", values=item)

tree.pack(expand=True, fill="both", padx=20, pady=20)

# ----- Contenido de la pestaña de Formulario -----
frame_form.configure(padding=20)

# Contenedor centrado para el formulario
form_container = ttk.Frame(frame_form, padding=40, style="TFrame")
form_container.place(relx=0.5, rely=0.5, anchor="center")

# Estilo del formulario tipo inicio de sesión web
ttk.Label(form_container, text="Inicio de Sesión", font=("Arial", 16, "bold"), background="#2c2f33", foreground="white").pack(pady=10)

ttk.Label(form_container, text="Usuario", font=("Arial", 12, "bold"), background="#2c2f33", foreground="white").pack(pady=5, anchor="w")
entry_user = ttk.Entry(form_container, font=("Arial", 11), width=30)
entry_user.pack(pady=5, padx=10)

ttk.Label(form_container, text="Contraseña", font=("Arial", 12, "bold"), background="#2c2f33", foreground="white").pack(pady=5, anchor="w")
entry_pass = ttk.Entry(form_container, font=("Arial", 11), width=30, show="*")
entry_pass.pack(pady=5, padx=10)

btn_login = ttk.Button(form_container, text="Iniciar Sesión", style="TButton")
btn_login.pack(pady=20)

# ----- Contenido de la pestaña de Información -----
info_text = """Esta es una aplicación de ejemplo
con pestañas verticales usando tkinter y ttk.
Puedes navegar entre las pestañas para ver diferentes contenidos."""

label_info = ttk.Label(frame_info, text=info_text, justify="left", font=("Arial", 12), wraplength=400, background="#2c2f33", foreground="white")
label_info.pack(padx=20, pady=20, anchor="w")

# Iniciar la aplicación
app.mainloop()
