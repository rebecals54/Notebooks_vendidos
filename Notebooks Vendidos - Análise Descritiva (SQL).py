# Databricks notebook source
# MAGIC %md
# MAGIC >**What Factors Affect Laptop Computer Prices?**
# MAGIC * Several different factors can affect laptop computer prices. These factors include the brand of computer and the number of options and add-ons included in the computer package. In addition, the amount of memory and the speed of the processor can also affect pricing. Though less common, some consumers spend additional money to purchase a computer based on the overall “look” and design of the system.
# MAGIC * In many cases, name brand computers are more expensive than generic versions. This price increase often has more to do with name recognition than any actual superiority of the product. One major difference between name brand and generic systems is that in most cases, name brand computers offer better warranties than generic versions. Having the option of returning a computer that is malfunctioning is often enough of an incentive to encourage many consumers to spend more money.
# MAGIC * Functionality is an important factor in determining laptop computer prices. A computer with more memory often performs better for a longer time than a computer with less memory. In addition, hard drive space is also crucial, and the size of the hard drive usually affects pricing. Many consumers may also look for digital video drivers and other types of recording devices that may affect the laptop computer prices.
# MAGIC * Most computers come with some software pre-installed. In most cases, the more software that is installed on a computer, the more expensive it is. This is especially true if the installed programs are from well-established and recognizable software publishers. Those considering purchasing a new laptop computer should be aware that many of the pre-installed programs may be trial versions only, and will expire within a certain time period. In order to keep the programs, a code will need to be purchased, and then a permanent version of the software can be downloaded.
# MAGIC -Many consumers who are purchasing a new computer are buying an entire package. In addition to the computer itself, these systems typically include a monitor, keyboard, and mouse. Some packages may even include a printer or digital camera. The number of extras included in a computer package usually affects laptop computer prices.
# MAGIC * Some industry leaders in computer manufacturing make it a selling point to offer computers in sleek styling and in a variety of colors. They may also offer unusual or contemporary system design. Though this is less important to many consumers, for those who do value “looks,” this type of system may be well worth the extra cost.

# COMMAND ----------

# MAGIC %md
# MAGIC >**From where I did get this data?**
# MAGIC * Scrapped this data from flipkart.com
# MAGIC * used an automated chrome web extension tool called Instant Data Scrapper
# MAGIC highly recommend you to use this beautiful tool to get the data from anywhere on the web. it's very easy to use, no coding knowledge is required.

# COMMAND ----------

# MAGIC %md
# MAGIC >**What you can do?**
# MAGIC * Visualize this data, and prepare high-quality charts as much as you can.
# MAGIC
# MAGIC * Build a model to predict the price
# MAGIC
# MAGIC * Columns description: pls refer to the data columns section.

# COMMAND ----------

# MAGIC %md #Análise Descritiva (SQL)

# COMMAND ----------

# MAGIC %md ##Exploração/ Desenvolvimento##

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER VIEW VW_cleaned_laptop_data AS
# MAGIC SELECT *,
# MAGIC (latest_price * 0.064) AS latest_price_real,
# MAGIC (old_price * 0.064) AS old_price_real,
# MAGIC (discount / 100) AS discount_percentage
# MAGIC FROM cleaned_laptop_data

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from VW_cleaned_laptop_data

# COMMAND ----------

# MAGIC %md Média de Preço das Marcas
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     CASE WHEN brand = 'lenovo' THEN 'Lenovo' ELSE brand END AS brand_current,
# MAGIC     AVG(latest_price_real) AS avg_price_real
# MAGIC FROM 
# MAGIC     VW_cleaned_laptop_data
# MAGIC GROUP BY 
# MAGIC     CASE WHEN brand = 'lenovo' THEN 'Lenovo' ELSE brand END 
# MAGIC ORDER BY 
# MAGIC     avg_price_real DESC

# COMMAND ----------

# MAGIC %md Participação das Memórias (DDR3, DDR4 e DDR5)
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     CASE 
# MAGIC         WHEN ram_type IN ('LPDDR4', 'LPDDR4X', 'LDDR4') THEN 'DDR4' 
# MAGIC         WHEN ram_type IN ('LPDDR3', 'LDDR3') THEN 'DDR3' 
# MAGIC         ELSE ram_type 
# MAGIC     END AS ram_type_current,
# MAGIC     sum(latest_price_real) AS sum_price_real
# MAGIC FROM 
# MAGIC     VW_cleaned_laptop_data
# MAGIC GROUP BY 
# MAGIC     CASE 
# MAGIC         WHEN ram_type IN ('LPDDR4', 'LPDDR4X', 'LDDR4') THEN 'DDR4' 
# MAGIC         WHEN ram_type IN ('LPDDR3', 'LDDR3') THEN 'DDR3' 
# MAGIC         ELSE ram_type 
# MAGIC     END
# MAGIC ORDER BY 
# MAGIC     CASE 
# MAGIC         WHEN ram_type IN ('LPDDR4', 'LPDDR4X', 'LDDR4') THEN 'DDR4' 
# MAGIC         WHEN ram_type IN ('LPDDR3', 'LDDR3') THEN 'DDR3' 
# MAGIC         ELSE ram_type 
# MAGIC     END

# COMMAND ----------

# MAGIC %md
# MAGIC