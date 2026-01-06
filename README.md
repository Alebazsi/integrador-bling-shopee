# 🛒 Integrador de E-commerce: Bling para Shopee (Automação Python)

![Status do Projeto](https://img.shields.io/badge/Status-Concluído-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## 📄 Sobre o Projeto
Este projeto é uma solução de **ETL (Extract, Transform, Load)** desenvolvida para automatizar a migração de catálogo de produtos entre sistemas de ERP (Bling) e Marketplaces (Shopee).

O objetivo é eliminar o trabalho manual de cadastro, garantindo que milhares de produtos sejam formatados, precificados e validados em segundos, prontos para a importação em massa ("bulk upload").

## 🎯 Problema Resolvido
Lojistas perdem horas copiando e colando dados do Bling para a Shopee. Esse processo manual gera:
* Erros de digitação.
* Anúncio de produtos sem estoque (prejuízo na reputação).
* Falta de padronização nos títulos.

**Minha solução automatiza 100% deste fluxo.**

## ⚙️ Funcionalidades Técnicas

O script executa um pipeline de dados robusto:

1.  **Limpeza de Dados (Data Cleaning):** Remove espaços desnecessários e caracteres inválidos das descrições.
2.  **Precificação Dinâmica:** Aplica automaticamente uma regra de negócio (Markup) de **+10%** sobre o preço original para cobrir taxas do marketplace.
3.  **Validação de Segurança:**
    * 🚫 **Filtro de Estoque:** Impede a exportação de produtos com estoque zerado ou negativo.
    * 💰 **Trava de Preço:** Bloqueia produtos com preços inconsistentes (ex: R$ 0,00).
4.  **Formatação (Mapping):** Adequa os títulos ao limite de caracteres da Shopee e renomeia as colunas para o padrão exigido pela plataforma.

## 🛠️ Tecnologias Utilizadas
* **Python 3:** Linguagem principal.
* **Pandas:** Para manipulação e análise de dados de alta performance.
* **Openpyxl:** Para exportação e formatação de arquivos Excel (.xlsx).

## 🚀 Como Executar o Projeto

### Pré-requisitos
Você precisa ter o Python instalado. Clone este repositório e instale as dependências:

```bash
# 1. Clone o repositório
git clone [https://github.com/seu-usuario/integrador-bling-shopee.git](https://github.com/seu-usuario/integrador-bling-shopee.git)

# 2. Instale as bibliotecas necessárias
pip install pandas openpyxl