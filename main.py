import pandas as pd

# 1. DADOS (Simulação)
data_bling = {
    'ID': [101, 102, 103],
    'Descrição': ['Camiseta Algodão - Azul - G', ' Calça Jeans Slim ', 'Meias Térmicas Pack x3'],
    'Preço': ['R$ 89,90', 'R$ 149,00', 'R$ 35,00'],
    'Estoque': [15, 0, 50],
    'Imagens': ['img1.jpg', 'img2.jpg', 'img3.jpg']
}

df_bling = pd.DataFrame(data_bling)

# --- FUNÇÕES ---

def limpar_preco(preco_str):
    return float(preco_str.replace('R$', '').replace(',', '.').strip())

def transformar_dados(df):
    print("Iniciando transformação...")
    df_novo = df.copy()
    df_novo['Descrição'] = df_novo['Descrição'].str.strip()
    df_novo['Preço_Limpo'] = df_novo['Preço'].apply(limpar_preco)
    df_novo['Preço_Shopee'] = (df_novo['Preço_Limpo'] * 1.10).round(2)
    return df_novo

def validar_e_filtrar(df):
    """Filtra produtos sem estoque ou preço zerado"""
    print("\n--- Validando Estoque e Segurança ---")
    inicial = len(df)
    
    # REGRA: Só passa quem tem estoque MAIOR que 0
    df_validado = df.loc[df['Estoque'] > 0].copy()
    
    removidos = inicial - len(df_validado)
    print(f"⚠️  {removidos} produtos removidos (Sem estoque).")
    return df_validado

def formatar_para_shopee(df):
    df['Nome do Produto'] = df['Descrição'].str.slice(0, 120)
    shopee_template = pd.DataFrame({
        'SKU': df['ID'],
        'Nome do Produto': df['Nome do Produto'],
        'Descrição': 'Produto oficial. Envio imediato.',
        'Preço': df['Preço_Shopee'],
        'Estoque': df['Estoque'],
        'Imagens': df['Imagens']
    })
    return shopee_template

# --- EXECUÇÃO ---

# 1. Transformar
df_transformado = transformar_dados(df_bling)

# 2. Validar (O PULO DO GATO ESTÁ AQUI)
df_seguro = validar_e_filtrar(df_transformado)

# 3. Formatar
df_final = formatar_para_shopee(df_seguro)

# 4. Exportar
print("\n--- Dados Finais (Aprovados) ---")
print(df_final[['Nome do Produto', 'Preço', 'Estoque']])

df_final.to_excel("carga_shopee_final.xlsx", index=False)
print("\n✅ Sucesso! Arquivo Excel gerado.")







# ---- Desenvolvido por Izabela Rosa ---- #
            # Foco em automação #