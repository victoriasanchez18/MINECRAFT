# ==========================================
#        BIENVENIDO A AVENTURA
# ==========================================

print("====================================")
print("        BIENVENIDO A AVENTURA")
print("====================================")
print("Explora, consigue recursos y derrota")
print("enemigos para convertirte en héroe.")
print("====================================")

# ---------- CLASE PADRE ----------
class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def mostrar_info(self):
        print("\nNombre:", self.nombre)
        print("Vida:", self.vida)

# ---------- CLASE HIJA ----------
class Guerrero(Personaje):
    def __init__(self, nombre, vida, inventario):
        super().__init__(nombre, vida)
        self.inventario = inventario
        self.espada = False

    def mostrar_inventario(self):
        print("\n========== INVENTARIO ==========")
        print(self.inventario)
        print("Espada:", "Sí" if self.espada else "No")

    def usar_pocion(self):
        if "pocion" in self.inventario:
            self.inventario.remove("pocion")
            self.vida += 20

            if self.vida > 100:
                self.vida = 100

            print("🧪 Usaste una poción.")
            print("Tu vida ahora es:", self.vida)
        else:
            print("❌ No tienes pociones.")

    def fabricar_espada(self):
        if "madera" in self.inventario and "piedra" in self.inventario:
            self.inventario.remove("madera")
            self.inventario.remove("piedra")
            self.espada = True
            print("⚔️ ¡Fabricaste una espada!")
        else:
            print("❌ Necesitas madera y piedra.")

# ---------- TUPLA ----------
lugares = ("Bosque", "Cueva", "Montaña")

# ---------- FUNCIÓN ----------
def menu():
    print("\n========== MENÚ ==========")
    print("1. Ver personaje")
    print("2. Ver inventario")
    print("3. Explorar")
    print("4. Fabricar espada")
    print("5. Usar poción")
    print("6. Pelear")
    print("7. Salir")

# ---------- EXPLORAR ----------
def explorar(jugador):
    print("\n========== EXPLORACIÓN ==========")

    for i, lugar in enumerate(lugares, 1):
        print(i, ".", lugar)

    try:
        opcion = int(input("¿A dónde quieres ir?: "))

        if opcion >= 1 and opcion <= 3:
            lugar = lugares[opcion - 1]
            print("\n🌎 Explorando:", lugar)

            jugador.inventario.append("piedra")
            print("⛏️ Encontraste una piedra.")

            jugador.inventario.append("madera")
            print("🪵 Encontraste madera.")

        else:
            print("❌ Lugar no válido.")

    except ValueError:
        print("❌ Debes ingresar un número.")

# ---------- PELEA ----------
def pelear(jugador):

    print("\n========== COMBATE ==========")
    print("👹 ¡Apareció un enemigo!")

    enemigo_vida = 30

    # FUNCIÓN ANÓNIMA
    calcular_dano = lambda ataque: ataque + 5 if jugador.espada else ataque

    while enemigo_vida > 0 and jugador.vida > 0:

        print("\nTu vida:", jugador.vida)
        print("Vida del enemigo:", enemigo_vida)

        print("\n1. Atacar")
        print("2. Usar poción")
        print("3. Escapar")

        try:
            opcion = int(input("Elige: "))

            if opcion == 1:

                dano = calcular_dano(10)
                enemigo_vida -= dano

                print("⚔️ Atacaste al enemigo.")
                print("Daño:", dano)

                if enemigo_vida <= 0:
                    print("🎉 ¡Derrotaste al enemigo!")
                    jugador.inventario.append("moneda")
                    print("🪙 Encontraste una moneda.")

                else:
                    jugador.vida -= 8
                    print("👹 El enemigo te atacó.")
                    print("Perdiste 8 de vida.")

            elif opcion == 2:
                jugador.usar_pocion()

            elif opcion == 3:
                print("🏃 Escapaste del combate.")
                break

            else:
                print("Opción no válida.")

        except ValueError:
            print("❌ Debes ingresar un número.")

# ---------- CREAR JUGADOR ----------
jugador = Guerrero(
    "Alex",
    100,
    ["pocion"]
)

# ---------- JUEGO PRINCIPAL ----------
jugando = True

while jugando:

    if jugador.vida <= 0:
        print("\n💀 Has perdido.")
        print("Fin del juego.")
        break

    menu()

    try:
        opcion = int(input("\nElige una opción: "))

        if opcion == 1:
            jugador.mostrar_info()

        elif opcion == 2:
            jugador.mostrar_inventario()

        elif opcion == 3:
            explorar(jugador)

        elif opcion == 4:
            jugador.fabricar_espada()

        elif opcion == 5:
            jugador.usar_pocion()

        elif opcion == 6:
            pelear(jugador)

        elif opcion == 7:
            print("\n👋 Gracias por jugar.")
            print("¡Hasta la próxima aventura!")
            jugando = False

        else:
            print("❌ Opción no válida.")

    except ValueError:
        print("❌ Error: debes escribir un número.")

