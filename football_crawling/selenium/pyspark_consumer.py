from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import udf, split, col
import os
import findspark
@udf(returnType=StringType())
def transform_raw_value_to_df(df):
    split_col = split(col("value"), ",")
    df = df.withColumn("Match_Date", split_col.getItem(0))
    df = df.withColumn("Leauge", split_col.getItem(1))
    df = df.withColumn("Home_Team", split_col.getItem(2))
    df = df.withColumn("Away_Team", split_col.getItem(3))
    df = df.withColumn("Home_Player1", split_col.getItem(4))
    df = df.withColumn("Home_Player2", split_col.getItem(5))
    df = df.withColumn("Home_Player3", split_col.getItem(6))
    df = df.withColumn("Home_Player4", split_col.getItem(7))
    df = df.withColumn("Home_Player5", split_col.getItem(8))
    df = df.withColumn("Home_Player6", split_col.getItem(9))
    df = df.withColumn("Home_Player7", split_col.getItem(10))
    df = df.withColumn("Home_Player8", split_col.getItem(11))
    df = df.withColumn("Home_Player9", split_col.getItem(12))
    df = df.withColumn("Home_Player10", split_col.getItem(13))
    df = df.withColumn("Home_Player11", split_col.getItem(14))
    df = df.withColumn("Away_Player1", split_col.getItem(15))
    df = df.withColumn("Away_Player2", split_col.getItem(16))
    df = df.withColumn("Away_Player3", split_col.getItem(17))
    df = df.withColumn("Away_Player4", split_col.getItem(18))
    df = df.withColumn("Away_Player5", split_col.getItem(19))
    df = df.withColumn("Away_Player6", split_col.getItem(20))
    df = df.withColumn("Away_Player7", split_col.getItem(21))
    df = df.withColumn("Away_Player8", split_col.getItem(22))
    df = df.withColumn("Away_Player9", split_col.getItem(23))
    df = df.withColumn("Away_Player10", split_col.getItem(24))
    df = df.withColumn("Away_Player11", split_col.getItem(25))
    df = df.withColumn("Home_Kit1", split_col.getItem(26))
    df = df.withColumn("Home_Kit2", split_col.getItem(27))
    df = df.withColumn("Home_Kit3", split_col.getItem(28))
    df = df.withColumn("Home_Kit4", split_col.getItem(29))
    df = df.withColumn("Home_Kit5", split_col.getItem(30))
    df = df.withColumn("Home_Kit6", split_col.getItem(31))
    df = df.withColumn("Home_Kit7", split_col.getItem(32))
    df = df.withColumn("Home_Kit8", split_col.getItem(33))
    df = df.withColumn("Home_Kit9", split_col.getItem(34))
    df = df.withColumn("Home_Kit10", split_col.getItem(35))
    df = df.withColumn("Home_Kit11", split_col.getItem(36))
    df = df.withColumn("Away_Kit1", split_col.getItem(37))
    df = df.withColumn("Away_Kit2", split_col.getItem(38))
    df = df.withColumn("Away_Kit3", split_col.getItem(39))
    df = df.withColumn("Away_Kit4", split_col.getItem(40))
    df = df.withColumn("Away_Kit5", split_col.getItem(41))
    df = df.withColumn("Away_Kit6", split_col.getItem(42))
    df = df.withColumn("Away_Kit7", split_col.getItem(43))
    df = df.withColumn("Away_Kit8", split_col.getItem(44))
    df = df.withColumn("Away_Kit9", split_col.getItem(45))
    df = df.withColumn("Away_Kit10", split_col.getItem(46))
    df = df.withColumn("Away_Kit11", split_col.getItem(47))
    df = df.drop("value")
    return df

if __name__ == "__main__":
    os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.5.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 pyspark-shell'
    findspark.find()
    spark = SparkSession.builder.appName("Kafka_Read_Up_Coming_Match").getOrCreate()
    kafka_params = {
        "kafka.bootstrap.servers": "localhost:9092",  # Replace with your Kafka broker host and port
        "subscribe": "UpComingMatch_Topic"  # Replace with your Kafka topic name
    }

    df = spark.readStream.format("kafka") \
        .options(**kafka_params) \
        .load()
    # df=df.withColumn("value",df["value"].cast("binary").cast("string")).select("data.*")
    df = df.selectExpr("CAST(value AS STRING)")
    df=df.select("value")

    query = df.writeStream\
            .format("csv")\
            .outputMode("append")\
            .option("checkpointLocation", "./output/checkpoint") \
            .option("path", "./output/csv") \
            .start()


    query.awaitTermination()