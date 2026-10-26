import sys
from variant_mod import *

def main():
    step = 3
    if len(sys.argv) >1 :
        arg = sys.argv[1]
        if not arg.isdigit():
             print(f'{arg} — это не число. Шаг установлен по умолчанию: 3')
             step = 3
        else:
            step = int(arg)
            if step <=0:
                print("Шаг должен быть положительным числом. Шаг установлен: 3")
                step = 3
       
        

    weights = [100.1, 99.5, 96.8, 101.2, 103.5, 100.0, 98.9, 100.4, 101.8]
    good_weight, bad_weight = reject_defective_items(weights)
    distribution = get_weight_distribution(weights)
    sample = get_sample_pack(weights,step)

    print("=== ВЕСОВОЙ КОНТРОЛЬ КОНВЕЙЕРА === ")
    print(f'Годная продукция {good_weight}\n Брак: {bad_weight}')
    print(f'Распределение {distribution}')
    print(f'Контрольная выборка (каждая {step}-я): {sample}')

if __name__ == "__main__":
    main()