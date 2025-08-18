""" """
print(" --- CALCULADORA DE PROPINA --- ")
monto_total = int(input("Ingrese el monto total de la cuenta: $"))
propina_10 = (monto_total * 10) / 100
propina_15 = (monto_total * 15) / 100

total_propina10 = monto_total + propina_10
total_propina15 = monto_total + propina_15

print(" ")
print(f"-Propina sugerida 10%:  ${propina_10}")
print(f"  Total a pagar con 10% de propina: ${total_propina10}")
print(" ")
print(f"-Propina sugerida 15%:  ${propina_15}")
print(f" Total a pagar con 15% de propina: ${total_propina15}")
print(" ")