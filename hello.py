from pyspark import SparkContext, SparkConf

# Create SparkContext instance
# sc = SparkContext(appName="CSV Parallelization")
sc = SparkContext()

# Load dataset in Python as RDD
filePath = "Nutritional Facts for Most Common Foods/nutrients_csvfile.csv"
dataSetRDD = sc.textFile(filePath, minPartitions=10)
print("Data type is ", type(dataSetRDD))

# Choose (at least) 2 from the basic RDD transformation: map(), filter(), flatMap(), union()
# mapRDD = map(lambda x:)

# Return value using RDD actions: collect(), take(), first(), count()


# If datasets contain  value that groups data together, use: sortByKey(), groupByKey()
# Then apply setp 2 and 3

