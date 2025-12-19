import requests
import pandas as pd

def get_data(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(endpoint)
        cep_info = response.json()

        if response.status_code == 200:
            return cep_info
        else:
            print(f"Erro ao buscar CEP {cep}: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Erro na requisição para o CEP {cep}: {e}")
        return None
    except requests.exceptions.Timeout as e:
        print(f"Timeout na requisição para o CEP {cep}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro desconhecido na requisição para o CEP {cep}: {e}")
        return None    



users_path = "01-bronze-raw/users.csv"

users_df = pd.read_csv(users_path)

cep_lists = users_df["cep"].tolist()

cep_info_list = []


for cep in cep_lists:
    cep_info = get_data(cep)
    print(cep_info)
    if "erro" in cep_info:
        continue
    cep_info_list.append(cep_info)
    print(f"CEP {cep} processado com sucesso.")

cep_info_df = pd.DataFrame(cep_info_list)

cep_info_df.to_csv("01-bronze-raw/cep_info.csv", index=False)
print("Informações de CEP salvas em '01-bronze-raw/cep_info.csv'")