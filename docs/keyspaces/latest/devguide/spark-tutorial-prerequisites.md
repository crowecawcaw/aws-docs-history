# Prerequisites for establishing

connections to Amazon Keyspaces with the Spark Cassandra Connector

Before you connect to Amazon Keyspaces with the Spark Cassandra Connector, you need to make sure
that you've installed the following. The compatibility of Amazon Keyspaces with the Spark Cassandra
Connector has been tested with the following recommended versions:

- Java version 8
- Scala 2.12
- Spark 3.4
- Cassandra Connector 2.5 and higher
- Cassandra driver 4.12

1. To install Scala, follow the instructions at [https://www.scala-lang.org/download/scala2.html](https://www.scala-lang.org/download/scala2.html "https://www.scala-lang.org/download/scala2.html").
2. To install Spark 3.4.1, follow this example.

```
curl -o spark-3.4.1-bin-hadoop3.tgz -k https://dlcdn.apache.org/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz

# now to untar
tar -zxvf spark-3.4.1-bin-hadoop3.tgz

# set this variable.
export SPARK_HOME=$PWD/spark-3.4.1-bin-hadoop3
```

```

```
