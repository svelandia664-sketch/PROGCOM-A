import tkinter as tk

# ══════════════════════════════════════════════════════════════════
#              DICCIONARIO COMPLETO DE 34 ERRORES
#         17 errores de Python  |  17 errores de Java
# ══════════════════════════════════════════════════════════════════

errores = [

    # ──────────────────────────────────────────────────────────────
    # 🐍  SECCIÓN PYTHON  (errores 01 al 17)
    # ──────────────────────────────────────────────────────────────
    {"num":"01","lenguaje":"Python","nombre":"KeyError",
     "descripcion":"Clave no existe en diccionario",
     "error":"d={'a':1}\nprint(d['b'])",
     "solucion":"print(d.get('b','No existe'))",
     "tip":"Usa get()"},

    {"num":"02","lenguaje":"Python","nombre":"IndexError",
     "descripcion":"Indice fuera de rango",
     "error":"l=[1,2]\nprint(l[5])",
     "solucion":"if 5<len(l): print(l[5])",
     "tip":"Valida tamaño"},

    {"num":"03","lenguaje":"Python","nombre":"TypeError",
     "descripcion":"Tipos incompatibles",
     "error":"'2'+2",
     "solucion":"int('2')+2",
     "tip":"Convierte tipos"},

    {"num":"04","lenguaje":"Python","nombre":"ZeroDivisionError",
     "descripcion":"Dividir entre cero",
     "error":"5/0",
     "solucion":"if x!=0: 5/x",
     "tip":"Evita dividir por 0"},

    {"num":"05","lenguaje":"Python","nombre":"NameError",
     "descripcion":"Variable no definida",
     "error":"print(x)",
     "solucion":"x=10\nprint(x)",
     "tip":"Declara variables"},

    {"num":"06","lenguaje":"Python","nombre":"AttributeError",
     "descripcion":"Metodo no existe",
     "error":"'hola'.append('x')",
     "solucion":"lista=[]\nlista.append('x')",
     "tip":"Revisa métodos"},

    {"num":"07","lenguaje":"Python","nombre":"ValueError",
     "descripcion":"Valor inválido",
     "error":"int('abc')",
     "solucion":"try:\n int('abc')\nexcept:\n print('Error')",
     "tip":"Usa try/except"},

    {"num":"08","lenguaje":"Python","nombre":"ImportError",
     "descripcion":"Modulo inexistente",
     "error":"import fake",
     "solucion":"pip install modulo",
     "tip":"Instala librerías"},

    {"num":"09","lenguaje":"Python","nombre":"IndentationError",
     "descripcion":"Indentación incorrecta",
     "error":"if True:\nprint('x')",
     "solucion":"if True:\n    print('x')",
     "tip":"Respeta espacios"},

    {"num":"10","lenguaje":"Python","nombre":"SyntaxError",
     "descripcion":"Error de sintaxis",
     "error":"if True print('x')",
     "solucion":"if True:\n print('x')",
     "tip":"Usa ':'"},

    {"num":"11","lenguaje":"Python","nombre":"TypeError None",
     "descripcion":"Operar con None",
     "error":"None+1",
     "solucion":"if x is not None: print(x+1)",
     "tip":"Valida None"},

    {"num":"12","lenguaje":"Python","nombre":"RecursionError",
     "descripcion":"Recursión infinita",
     "error":"def f(): f()",
     "solucion":"def f(n):\n if n==0: return\n f(n-1)",
     "tip":"Caso base"},

    {"num":"13","lenguaje":"Python","nombre":"MemoryError",
     "descripcion":"Sin memoria",
     "error":"a=[1]*10**10",
     "solucion":"usar generadores",
     "tip":"Optimiza memoria"},

    {"num":"14","lenguaje":"Python","nombre":"AssertionError",
     "descripcion":"Assert falla",
     "error":"assert False",
     "solucion":"assert 5>3",
     "tip":"Condición correcta"},

    {"num":"15","lenguaje":"Python","nombre":"FileNotFoundError",
     "descripcion":"Archivo no encontrado",
     "error":"open('archivo.txt')",
     "solucion":"import os\nif os.path.exists('archivo.txt'):\n    open('archivo.txt')",
     "tip":"Verifica existencia de archivo"},

    {"num":"16","lenguaje":"Python","nombre":"StopIteration",
     "descripcion":"Se agotaron los elementos del iterador",
     "error":"gen = iter([1,2])\nnext(gen)\nnext(gen)\nnext(gen)  # Error aquí",
     "solucion":"gen = iter([1,2])\nprint(next(gen, 'Agotado'))\nprint(next(gen, 'Agotado'))\nprint(next(gen, 'Agotado'))",
     "tip":"Usa next() con valor por defecto"},

    # ── 🆕 NUEVO ERROR PYTHON #17 ─────────────────────────────────
    {"num":"17","lenguaje":"Python","nombre":"OverflowError",
     "descripcion":"Resultado numérico demasiado grande para representarse",
     "error":"import math\nprint(math.exp(1000))  # resultado desborda float",
     "solucion":"import math\ntry:\n    resultado = math.exp(1000)\nexcept OverflowError:\n    print('Número demasiado grande')",
     "tip":"Usa try/except para capturar desbordamientos numéricos"},

    # ──────────────────────────────────────────────────────────────
    # ☕  SECCIÓN JAVA  (errores 18 al 34)
    # ──────────────────────────────────────────────────────────────
    {"num":"18","lenguaje":"Java","nombre":"NullPointerException",
     "descripcion":"Objeto null",
     "error":"s.length();",
     "solucion":"if(s!=null){ s.length(); }",
     "tip":"Verifica null"},

    {"num":"19","lenguaje":"Java","nombre":"ArrayIndexOutOfBounds",
     "descripcion":"Indice inválido",
     "error":"a[5];",
     "solucion":"if(i<a.length){...}",
     "tip":"Usa length"},

    {"num":"20","lenguaje":"Java","nombre":"NumberFormatException",
     "descripcion":"Texto a número",
     "error":"Integer.parseInt('a');",
     "solucion":"try{Integer.parseInt('a');} catch(NumberFormatException e){...}",
     "tip":"Valida datos"},

    {"num":"21","lenguaje":"Java","nombre":"ClassCastException",
     "descripcion":"Cast inválido",
     "error":"(Integer)'hola';",
     "solucion":"if(obj instanceof Integer){ Integer i=(Integer)obj; }",
     "tip":"Verifica tipo"},

    {"num":"22","lenguaje":"Java","nombre":"StackOverflowError",
     "descripcion":"Recursión infinita",
     "error":"f();",
     "solucion":"definir caso base",
     "tip":"Detener recursión"},

    {"num":"23","lenguaje":"Java","nombre":"ArithmeticException",
     "descripcion":"División por cero",
     "error":"5/0;",
     "solucion":"if(b!=0){5/b;}",
     "tip":"Evita 0"},

    {"num":"24","lenguaje":"Java","nombre":"IllegalArgumentException",
     "descripcion":"Argumento inválido",
     "error":"metodo(-1);",
     "solucion":"validar input",
     "tip":"Chequea valores"},

    {"num":"25","lenguaje":"Java","nombre":"IOException",
     "descripcion":"Error IO",
     "error":"leer archivo",
     "solucion":"try/catch",
     "tip":"Maneja archivos"},

    {"num":"26","lenguaje":"Java","nombre":"FileNotFoundException",
     "descripcion":"Archivo no existe",
     "error":"open('x')",
     "solucion":"verificar ruta",
     "tip":"Revisa path"},

    {"num":"27","lenguaje":"Java","nombre":"OutOfMemoryError",
     "descripcion":"Sin memoria",
     "error":"new int[999999999]",
     "solucion":"optimizar",
     "tip":"Cuida memoria"},

    {"num":"28","lenguaje":"Java","nombre":"NoSuchMethodError",
     "descripcion":"Método no existe",
     "error":"obj.x()",
     "solucion":"revisar métodos",
     "tip":"Compilar bien"},

    {"num":"29","lenguaje":"Java","nombre":"NoClassDefFoundError",
     "descripcion":"Clase no encontrada",
     "error":"new X()",
     "solucion":"classpath correcto",
     "tip":"Configura proyecto"},

    {"num":"30","lenguaje":"Java","nombre":"IllegalStateException",
     "descripcion":"Estado inválido",
     "error":"uso incorrecto",
     "solucion":"orden correcto",
     "tip":"Controla flujo"},

    {"num":"31","lenguaje":"Java","nombre":"IllegalMonitorStateException",
     "descripcion":"Uso incorrecto de monitor",
     "error":"o.notify();",
     "solucion":"synchronized(o){ o.notify(); }",
     "tip":"Usa dentro de synchronized"},

    {"num":"32","lenguaje":"Java","nombre":"UnsupportedOperationException",
     "descripcion":"Operación no soportada",
     "error":"list.add(x); // no soportado",
     "solucion":"usar ArrayList en vez de Arrays.asList",
     "tip":"Verifica soporte de operación"},

    {"num":"33","lenguaje":"Java","nombre":"ConcurrentModificationException",
     "descripcion":"Modificar lista mientras se itera",
     "error":"for(String s : lista){\n  lista.remove(s); // Error\n}",
     "solucion":"Iterator<String> it = lista.iterator();\nwhile(it.hasNext()){\n  it.next();\n  it.remove();\n}",
     "tip":"Usa Iterator para eliminar elementos"},

    # ── 🆕 NUEVO ERROR JAVA #34 ───────────────────────────────────
    {"num":"34","lenguaje":"Java","nombre":"StringIndexOutOfBoundsException",
     "descripcion":"Acceso a posición inválida dentro de un String",
     "error":"String s = \"Hola\";\nchar c = s.charAt(10); // Error: índice 10 no existe",
     "solucion":"String s = \"Hola\";\nif(10 < s.length()) {\n    char c = s.charAt(10);\n} else {\n    System.out.println(\"Índice fuera de rango\");\n}",
     "tip":"Verifica s.length() antes de usar charAt()"},
]

# ══════════════════════════════════════════════════════════════════
#                        INTERFAZ GRÁFICA
# ══════════════════════════════════════════════════════════════════
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Repositorio de 34 Errores — 🐍 Python  |  ☕ Java")
        self.geometry("1000x700")

        # ── Listbox con separadores visuales por lenguaje ──────────
        self.lista = tk.Listbox(self, width=38, font=("Courier", 10))
        self.lista.pack(side="left", fill="y")

        lenguaje_actual = None
        for e in errores:
            # Cabecera de sección al cambiar de lenguaje
            if e["lenguaje"] != lenguaje_actual:
                lenguaje_actual = e["lenguaje"]
                if lenguaje_actual == "Python":
                    self.lista.insert("end", "─── 🐍  PYTHON ──────────────────")
                    idx_cab = self.lista.size() - 1
                    self.lista.itemconfig(idx_cab, fg="white", bg="#1a3a6e")
                else:
                    self.lista.insert("end", "─── ☕  JAVA ────────────────────")
                    idx_cab = self.lista.size() - 1
                    self.lista.itemconfig(idx_cab, fg="white", bg="#5c2e00")
            self.lista.insert("end", f"  {e['num']} │ {e['nombre']}")
            idx = self.lista.size() - 1
            if e["lenguaje"] == "Python":
                self.lista.itemconfig(idx, fg="blue",
                                      selectforeground="white",
                                      selectbackground="#1a3a6e")
            else:
                self.lista.itemconfig(idx, fg="#8B4513",
                                      selectforeground="white",
                                      selectbackground="#5c2e00")

        # ── Panel de texto ─────────────────────────────────────────
        self.texto = tk.Text(self, wrap="word", font=("Courier", 11))
        self.texto.pack(side="right", fill="both", expand=True)

        # ── Canvas para íconos ─────────────────────────────────────
        self.canvas = tk.Canvas(self, width=150, height=150, bg="white")
        self.canvas.place(x=820, y=20)

        self.lista.bind("<<ListboxSelect>>", self.mostrar)

    def mostrar(self, event):
        sel = self.lista.curselection()
        if not sel:
            return

        # Ignorar clics en cabeceras de sección
        texto_sel = self.lista.get(sel[0])
        if "──" in texto_sel:
            return

        # Buscar el error correspondiente por número
        num = texto_sel.strip().split("│")[0].strip()
        e = next((x for x in errores if x["num"] == num), None)
        if not e:
            return

        # Etiqueta de lenguaje destacada
        if e["lenguaje"] == "Python":
            etiqueta = "🐍 PYTHON"
        else:
            etiqueta = "☕ JAVA"

        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END,
            f"{'═'*50}\n"
            f"  Lenguaje : {etiqueta}\n"
            f"  Error N° : {e['num']}\n"
            f"{'═'*50}\n\n"
            f"📌 Nombre      : {e['nombre']}\n"
            f"📋 Descripción : {e['descripcion']}\n\n"
            f"❌  Código con error:\n{e['error']}\n\n"
            f"✅  Corrección:\n{e['solucion']}\n\n"
            f"💡  Tip: {e['tip']}\n"
        )

        # Dibujo según lenguaje
        self.canvas.delete("all")
        if e["lenguaje"] == "Python":
            self.dibujar_python()
        else:
            self.dibujar_java()

    # ── Ícono Python ───────────────────────────────────────────────
    def dibujar_python(self):
        self.canvas.create_oval(30, 30, 120, 120, fill="lightblue", outline="blue", width=2)
        self.canvas.create_oval(50, 55, 68, 73, fill="black")   # ojo izquierdo
        self.canvas.create_oval(88, 55, 106, 73, fill="black")  # ojo derecho
        self.canvas.create_arc(50, 75, 110, 110, start=0, extent=-180, style="arc", width=3)
        self.canvas.create_text(75, 130, text="🐍 Python", font=("Arial", 13, "bold"), fill="blue")

    # ── Ícono Java ─────────────────────────────────────────────────
    def dibujar_java(self):
        self.canvas.create_rectangle(40, 65, 110, 115, fill="#6F3B00", outline="black", width=2)
        self.canvas.create_arc(30, 35, 120, 75, start=0, extent=180, style="arc", width=3)
        self.canvas.create_text(75, 55, text="☕", font=("Arial", 22))
        self.canvas.create_text(75, 130, text="☕ Java", font=("Arial", 13, "bold"), fill="#6F3B00")

# ══════════════════════════════════════════════════════════════════
#                          EJECUCIÓN
# ══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    App().mainloop()