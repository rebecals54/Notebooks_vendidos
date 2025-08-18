
# 💻 Notebooks Sold – Descriptive Analysis (SQL + Python)

## ❓ O que influencia o preço de notebooks?

Este projeto busca responder à pergunta:
**“Quais fatores afetam o preço de um notebook?”**

Diversos aspectos podem impactar o valor de mercado de um notebook, entre eles:

* **Marca**: notebooks de marcas reconhecidas tendem a ser mais caros do que versões genéricas. Essa diferença muitas vezes está ligada ao valor da marca e às garantias oferecidas.
* **Configurações técnicas**:

  * Quantidade de **memória RAM**
  * Velocidade do **processador**
  * Capacidade do **HD/SSD**
* **Funcionalidades extras**: drivers de vídeo, softwares instalados, periféricos inclusos (monitor, teclado, mouse, câmera, etc.).
* **Design e estilo**: em alguns casos, consumidores pagam mais pelo aspecto visual e pela personalização (cores, estilos modernos).
* **Softwares pré-instalados**: quanto mais programas licenciados o equipamento possuir, maior tende a ser o preço final.

---

## 📊 Origem dos dados

Os dados foram **extraídos via Web Scraping** do site [Flipkart.com](https://www.flipkart.com/), utilizando a ferramenta **Instant Data Scraper**.
👉 Essa extensão é altamente recomendada, pois é simples de usar e não exige conhecimentos avançados em programação.

---

## 🔎 O que pode ser feito com os dados?

1. **Análise descritiva em SQL**

   * Cálculo de preço médio por marca
   * Participação de diferentes tipos de memória (DDR3, DDR4, DDR5)
   * Exploração dos fatores que mais impactam no preço

2. **Visualização em Python**

   * Criação de gráficos e dashboards para melhor interpretação dos dados

3. **Modelagem preditiva**

   * Desenvolvimento de um modelo de Machine Learning para **prever preços de notebooks** com base em suas especificações técnicas

---

## 🗂️ Estrutura dos dados

* **896 registros**
* **\~25 colunas** contendo informações como:

  * Marca
  * Modelo
  * Preço real
  * Tipo e quantidade de memória RAM
  * Capacidade de armazenamento
  * Processador
  * Recursos adicionais

---

## ⚙️ Análise em SQL

### 📌 Preço médio por marca

```sql
SELECT brand, AVG(price) AS avg_price
FROM notebooks
GROUP BY brand
ORDER BY avg_price DESC;
```

### 📌 Participação de cada tipo de memória

```sql
SELECT memory_type, COUNT(*) AS qtd_notebooks
FROM notebooks
GROUP BY memory_type;
```

---

## 📈 Exemplos de Resultados

* **Preço médio por marca (*avg\_price\_real*)**
  → Comparação entre marcas consolidadas e genéricas

* **Distribuição por tipo de memória (DDR3, DDR4, DDR5)**
  → Identificação da predominância tecnológica e impacto no valor final

