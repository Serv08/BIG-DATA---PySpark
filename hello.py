from pyspark import SparkContext 

# Create SparkContext instance
sc = SparkContext(appName="CSV Parallelization")

# Load dataset in Python as RDD
filePath = "Nutritional Facts for Most Common Foods/nutrients_csvfile.csv"
dataSetRDD = sc.textFile(filePath, minPartitions=10)
# print(type(dataSetRDD))

# Choose (at least) 2 from the basic RDD transformation: map(), filter(), flatMap(), union()

# Return value using RDD actions: collect(), take(), first(), count()

# If datasets contain  value that groups data together, use: sortByKey(), groupByKey()
# Then apply setp 2 and 3

