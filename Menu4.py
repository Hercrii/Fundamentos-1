import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class Usuario:
    def __init__(self, cedula, nombre, apellido, telefono, serial, semestre, promedio):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.serial = serial
        self.semestre = semestre
        self.promedio = promedio

class GestionUsuarios:
    usuarios = []

    @staticmethod
    def menu_principal():
        root = ctk.CTk()
        root.geometry("400x500")
        root.title("Menú Principal")

        ctk.CTkLabel(root, text="Gestión de Usuarios", font=("Arial", 16)).pack(pady=10)
        
        ctk.CTkButton(root, text="Registrar Usuario", command=GestionUsuarios.abrir_registro).pack(pady=5)
        ctk.CTkButton(root, text="Ver Usuarios", command=GestionUsuarios.ver_usuarios).pack(pady=5)
        ctk.CTkButton(root, text="Modificar Usuario", command=GestionUsuarios.modificar_usuario).pack(pady=5)
        ctk.CTkButton(root, text="Salir", command=root.quit).pack(pady=5)
        
        root.mainloop()
    
    @staticmethod
    def abrir_registro():
        registro_win = ctk.CTkToplevel()
        registro_win.geometry("400x500")
        registro_win.title("Registrar Usuario")
        
        campos = ["Cédula", "Nombre", "Apellido", "Teléfono", "Serial", "Semestre", "Promedio"]
        entradas = {}

        for campo in campos:
            ctk.CTkLabel(registro_win, text=f"{campo}:").pack()
            entrada = ctk.CTkEntry(registro_win)
            entrada.pack()
            entradas[campo.lower()] = entrada
        
        def registrar():
            usuario = Usuario(
                entradas["cédula"].get(), entradas["nombre"].get(), entradas["apellido"].get(),
                entradas["teléfono"].get(), entradas["serial"].get(), entradas["semestre"].get(), entradas["promedio"].get()
            )
            GestionUsuarios.usuarios.append(usuario)
            registro_win.destroy()
        
        ctk.CTkButton(registro_win, text="Guardar", command=registrar).pack(pady=10)

    @staticmethod
    def ver_usuarios():
        ver_win = ctk.CTkToplevel()
        ver_win.geometry("500x400")
        ver_win.title("Usuarios Registrados")
        
        for usuario in GestionUsuarios.usuarios:
            info = f"{usuario.cedula} - {usuario.nombre} {usuario.apellido} - Semestre: {usuario.semestre} - Promedio: {usuario.promedio}"
            ctk.CTkLabel(ver_win, text=info).pack()

    @staticmethod
    def modificar_usuario():
        mod_win = ctk.CTkToplevel()
        mod_win.geometry("400x300")
        mod_win.title("Modificar Usuario")
        
        ctk.CTkLabel(mod_win, text="Ingrese la cédula del usuario:").pack()
        entrada_cedula = ctk.CTkEntry(mod_win)
        entrada_cedula.pack()
        
        def modificar():
            cedula = entrada_cedula.get()
            usuario = next((u for u in GestionUsuarios.usuarios if u.cedula == cedula), None)
            if not usuario:
                ctk.CTkLabel(mod_win, text="Usuario no encontrado.", fg_color="red").pack()
                return
            
            mod_sub_win = ctk.CTkToplevel()
            mod_sub_win.geometry("400x300")
            mod_sub_win.title("Seleccionar campo a modificar")
            
            opciones = ["nombre", "apellido", "telefono", "serial", "semestre", "promedio"]
            variable = ctk.StringVar(value=opciones[0])
            dropdown = ctk.CTkComboBox(mod_sub_win, values=opciones, variable=variable)
            dropdown.pack()
            
            ctk.CTkLabel(mod_sub_win, text="Nuevo valor:").pack()
            nueva_entrada = ctk.CTkEntry(mod_sub_win)
            nueva_entrada.pack()
            
            def guardar_cambio():
                setattr(usuario, variable.get(), nueva_entrada.get())
                mod_sub_win.destroy()
                mod_win.destroy()
            
            ctk.CTkButton(mod_sub_win, text="Guardar", command=guardar_cambio).pack()
        
        ctk.CTkButton(mod_win, text="Buscar", command=modificar).pack(pady=5)

if __name__ == "__main__":
    GestionUsuarios.menu_principal()