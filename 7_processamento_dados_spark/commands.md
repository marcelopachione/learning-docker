# Build Spark Containers
docker-compose up -d

# Execute Pyspark Job
docker cp -L pyspark_job.py 7_processamento_dados_spark-spark-master-1:/opt/bitnami/spark/pyspark_job.py

docker logs 7_processamento_dados_spark-spark-master-1

docker exec 7_processamento_dados_spark-spark-master-1 \
    spark-submit \
    --conf spark.jars.ivy=/tmp/.ivy2 \
    --master spark://66f027b45264:7077 pyspark_job.py

# Stop Containers
docker-compose down    