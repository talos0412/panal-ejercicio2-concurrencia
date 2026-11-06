import time
import threading

def recolectar_nectar(abeja, flor, tiempo):
    print(f"{abeja} está recolectando néctar de la {flor}.")
    time.sleep(tiempo)
    print(f"{abeja} ha terminado de recolectar néctar de la {flor}.")
    
if __name__ == "__main__":
    ab1="Abeja Obrera #1"
    ab2="Abeja Obrera #2"
    ab3="Abeja Obrera #3"

    t1 = threading.Thread(target=recolectar_nectar, args=(ab1, "Rosa", 2))
    t2 = threading.Thread(target=recolectar_nectar, args=(ab2, "Girasol", 3))
    t3 = threading.Thread(target=recolectar_nectar, args=(ab3, "Tulipán", 1))

    print("Iniciando la recolección en enjambre de néctar...")
    inicio=time.time()
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    fin=time.time()
    print(f"Tiempo total de recolección: {fin - inicio:.2f} segundos.")