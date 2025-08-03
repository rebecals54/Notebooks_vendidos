# Notebooks Sold - Descriptive Analysis (SQL) #

## Descriptive Analysis (SQL)

### Practical examples:

###  Average monthly sales of a company.
* Total number of customers served during a period.
* Age distribution of students in a school.
* Percentage of defective products in a batch.

### Main tools of descriptive analysis:

* **Means, medians, and modes**
* **Percentages and proportions**
* **Charts and tables** (bar charts, pie charts, histograms, etc.)
* **Measures of dispersion** (standard deviation, variance, range)

### Main goal:

Answer the question: “What do the data tell us?” 

---
 ## Main SQL Fundamentals ##

1. **SELECT Command**
   Used to retrieve data from one or more tables.

```sql
SELECT name, age FROM customers;
```

2. **WHERE Clause**
   Filters records based on a condition.

```sql
SELECT * FROM products WHERE price > 100;
```

3. **ORDER BY Clause**
   Sorts the results (ascending or descending).

```sql
SELECT name, price FROM products ORDER BY price DESC;
```


