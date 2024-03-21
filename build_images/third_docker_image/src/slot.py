from resources.test_modules import simu_data_api, DataClassWithoutSlots, DataClassWithSlots, ingest_data_noClass
import timeit
# Número de iterações para testar o desempenho
iterations = 10
num_rows = 1000

def main(iterations, rum_rows):
    # Gerando dados fictícios a partir da simulação da fonte da API
    fake_data = simu_data_api(num_rows)

    # Medindo o tempo para processar os dados sem slots e converter para JSON
    time_without_slots = timeit.timeit(lambda: DataClassWithoutSlots.ingest_data_Class(fake_data), number=iterations)


    # Medindo o tempo para processar os dados com slots e converter para JSON
    time_with_slots = timeit.timeit(lambda: DataClassWithSlots.ingest_data_ClassSlot(fake_data), number=iterations)


    # % dif
    percentage_difference = ((time_without_slots - time_with_slots) / time_without_slots) * 100

    # sem classes apenas f
    time_without_classes = timeit.timeit(lambda: ingest_data_noClass(fake_data), number=iterations)

    # Exibir os resultados
    print(f"Tempo sem slots (JSON): {time_without_slots} segundos")
    print(f"Tempo com slots (JSON): {time_with_slots} segundos")
    print(f"Diferença percentual: {percentage_difference:.2f}%")
    print("\n")
    print(f"Tempo sem classes de dados (JSON): {time_without_classes} segundos")
    return time_without_slots, time_with_slots, percentage_difference, time_without_classes



if __name__ == '__main__':
    main(iterations, num_rows)