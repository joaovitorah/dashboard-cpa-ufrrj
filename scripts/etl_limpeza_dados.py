import pandas as pd
import numpy as np
import hashlib
import os

ARQUIVO_ENTRADA = 'dados_brutos/base_cotic_2024.xlsx'  
ARQUIVO_SAIDA = 'dados_tratados/base_cpa_final.csv'    

COLS_SENSIVEIS = ['nome_completo', 'cpf', 'email', 'telefone', 'data_nascimento']

COL_ID_ORIGINAL = 'matricula' 

def gerar_hash_anonimo(valor):
    """
    Transforma uma matrícula (ex: 20201010) em um código único criptografado.
    Isso permite contar respondentes únicos sem identificar a pessoa.
    """
    if pd.isna(valor):
        return "N/A"
    valor_str = str(valor).strip()
    # Cria um hash SHA256
    hash_obj = hashlib.sha256(valor_str.encode())
    return hash_obj.hexdigest()[:15] 

def limpar_texto(texto):
    """Padroniza textos: Maiúsculas, sem espaços extras."""
    if pd.isna(texto):
        return "NAO INFORMADO"
    return str(texto).upper().strip()


def executar_etl():
    print(f"🔄 Iniciando leitura do arquivo: {ARQUIVO_ENTRADA}...")
    
    try:
       
        if ARQUIVO_ENTRADA.endswith('.xlsx'):
            df = pd.read_excel(ARQUIVO_ENTRADA)
        else:
            df = pd.read_csv(ARQUIVO_ENTRADA, encoding='utf-8', sep=';')
            
        print(f"📊 Dados carregados. Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")


        print("🔒 Aplicando anonimização e remoção de dados sensíveis...")
        

        if COL_ID_ORIGINAL in df.columns:
            df['id_respondente'] = df[COL_ID_ORIGINAL].apply(gerar_hash_anonimo)
            cols_remover = COLS_SENSIVEIS + [COL_ID_ORIGINAL]
        else:
            cols_remover = COLS_SENSIVEIS


        cols_existentes_remover = [c for c in cols_remover if c in df.columns]
        df.drop(columns=cols_existentes_remover, inplace=True)


        print("🧹 Padronizando nomes de cursos, campi e unidades...")
        

        cols_filtro = ['curso', 'campus', 'instituto', 'modalidade']
        
        for col in cols_filtro:
            if col in df.columns:
                df[col] = df[col].apply(limpar_texto)

        cols_questoes = [c for c in df.columns if c.startswith('Q')]
    
        for col in cols_questoes:
            df[col] = pd.to_numeric(df[col], errors='coerce')


        print(f"💾 Salvando arquivo tratado em: {ARQUIVO_SAIDA}...")
        

        os.makedirs(os.path.dirname(ARQUIVO_SAIDA), exist_ok=True)
        

        df.to_csv(ARQUIVO_SAIDA, index=False, sep=';', encoding='utf-8-sig')
        
        print("✅ ETL Concluído com Sucesso!")

    except Exception as e:
        print(f"❌ Erro crítico no processo: {e}")


if __name__ == "__main__":
    executar_etl()
