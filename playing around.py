# Databricks notebook source
import random 
random.random()*10

# COMMAND ----------

# MAGIC %sql
# MAGIC select round(12.4);

# COMMAND ----------

# MAGIC %sh
# MAGIC cd ..
# MAGIC ls
# MAGIC cd databrciks-course-rep
# MAGIC ls

# COMMAND ----------

dbutils.fs.ls

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls /databricks-datasets/

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets')

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets'):
    if(files.name.endswith('/')):
        print(files)

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls dbfs:/FileStore/tables/circuits.csv

# COMMAND ----------


