def formula_winter():
    print("\nQual o bicarbonato? [Unidade = mEq/L]")
    resposta = input()
    bicarbonato = float(resposta)
    pco2 = (1.5 * bicarbonato) + 8
    print(f"\n-->PCo2 Esperada = {pco2 - 2} - {pco2 + 2} mmHg<--")


def referencia_gasometria():
    print("\n--> Referência Gasometria: <--")
    print("pH 7.35 - 7.45")
    print("pO2 80-100 mmHg")
    print("HCO3 22 - 26 mEg/L")
    print("PCO2 35 - 45 mmHg")


def referencia_hemograma():
    print("\nHemoglobina [M 13.5 a 18.0][F 12.0 a 16.0] g/dL")
    print("Hemácias [M 4.5 a 6.5] [F 4 a 5.6] mi/µL")
    print("\nHematócrito [H 40 a 54%] [F 36 a 47%]")
    print(" VCM 82 a 94 fL")
    print(" HCM 27 a 33 pg")
    print(" CHCM 32 a 37 g/dL")
    print(" RDW 11 a 16.5%")
    print("\nPlaquetas 150'000 a 400'000 /µL")
    print("\nLeucócitos Totais 4'400 a 11'000 /µL")
    print(" Basófilos 0 a 1% | 0 a 200/µL")
    print(" Eosinófilos 0 a 3% | 0 a 450/µL")
    print(" Mielócitos 0%")
    print(" Metamielócitos 0%")
    print(" Bastões 0 a 5% | 0 a 700/µL")
    print(" Segmentados 50 a 70% | 1800 a 7800/µL")
    print(" Linfócitos 30 a 45% | 1000 a 4800/µL")
    print(" Monócitos 0 a 6% | 0 a 800/µL")


def referencia_ureia_eletrolitos():
    print("\nNa+ 135 a 145 mEq/L")
    print("K 3.5 a 5 mEq/L")
    print("Cl 97 a 107 mEq/L")
    print("\nCreatitina [M ≤ 1.2 mg/dL] [F ≤ 1.1 mg/dL]")
    print("Ureia [M 19 a 43 mg/dL] [F 15 a 36 mg/dL]")


def escala_rass():
    print(
        "\nRASS +4: agressivo - muito agressivo e/ou violento; perigo iminente à equipe cuidadora"
    )
    print("RASS +3: muito agitado - puxa ou retira tubos e cateteres")
    print(
        "RASS +2: agitado - movimento não-intencionais incoordenados frequentes, mal acoplado ao ventilador"
    )
    print("RASS +1: inquieto - ansioso, porém sem movimentos agressivos e/ou vigorosos")
    print("RASS 0: alerta e calmo - estado basal normal")
    print(
        "RASS -1: sonolento - não está completamente alerta, mas é capaz de manter abertura ocular e/ou contato visual ao som da voz por mais de 10 segundos"
    )
    print(
        "RASS -2: sedação leve - desperta brevemente e estabelece contato visual por menos de 10 segundos"
    )
    print(
        "RASS -3: sedação moderada - movimentos e/ou abertura ocular ao estímulo verbal sem estabelecer contato visual"
    )
    print(
        "RASS -4: sedação profunda - não responde ao comando verbal, mas se movimenta ou abre os olhos por estímulo físico"
    )
    print("RASS -5: não despertável - não responde a estímulo sonoro ou físico")
    print("\nObjetivo: manter entre RASS -2 a +1")


function_list = [
    formula_winter,
    referencia_gasometria,
    referencia_hemograma,
    referencia_ureia_eletrolitos,
    escala_rass,
]
name_list = [
    "Fórmula de Winter",
    "Referência Gasometria",
    "Referência Hemograma",
    "Referência Ureia e Eletrólitos",
    "Escala RASS",
]

name_list, function_list = zip(*sorted(zip(name_list, function_list)))

while True:
    print("\nQual Calculadora Usar?")
    for i in range(len(name_list)):
        print(f"{i+1} - {name_list[i]}")

    resposta = input()
    try:
        resposta = int(resposta)
        function_list[resposta - 1]
    except (ValueError, IndexError) as e:
        print(f"\n--> Escreva um número entre 1 e {len(name_list)} <--")
        continue

    try:
        function_list[resposta - 1]()
        print("\nEscreva qualquer coisa para sair")
        resposta = input()

    except ValueError:
        print("\n--> Favor escrever um número <--")
