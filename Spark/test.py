import findspark
findspark.init()

# PySpark is the Spark API for Python. In this lab, we use PySpark to initialize the spark context. 
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Creating a spark context class
sc = SparkContext()

# Creating a spark session
#spark = SparkSession \
#    .builder \
#    .appName("Python Spark DataFrames basic example") \
#    .config("spark.some.config.option", "some-value") \
#    .getOrCreate()
