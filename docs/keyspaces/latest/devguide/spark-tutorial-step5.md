# Step 5: Write and read Amazon Keyspaces data using the

Apache Cassandra Spark Connector

In this step, you start by loading the data from the sample file into a
`DataFrame` with the Spark Cassandra Connector. Next, you
write the data from the `DataFrame` into your Amazon Keyspaces table. You can also
use this part independently, for example, to migrate data into an Amazon Keyspaces table. Finally,
you read the data from your table into a `DataFrame` using the Spark
Cassandra Connector. You can also use this part independently, for example, to read data
from an Amazon Keyspaces table to perform data analytics with Apache Spark.

1. Start the Spark Shell as shown in the following example. Note that this
   example is using SigV4 authentication.

```
./spark-shell --files application.conf --conf spark.cassandra.connection.config.profile.path=application.conf --packages software.aws.mcs:aws-sigv4-auth-cassandra-java-driver-plugin:4.0.5,com.datastax.spark:spark-cassandra-connector_2.12:3.1.0 --conf spark.sql.extensions=com.datastax.spark.connector.CassandraSparkExtensions
```

2. Import the Spark Cassandra Connector with the following code.

```
import org.apache.spark.sql.cassandra._
```

3. To read data from the CSV file and store it in a `DataFrame`, you
   can use the following code example.

```
var df = spark.read.option("header","true").option("inferSchema","true").csv("keyspaces_sample_table.csv")
```

You can display the result with the following command.

```
scala> df.show();
```

The output should look similar to this.

````
`+----------------+----+-----------+----+------------------+--------------------+-------------+
| award|year| category|rank| author| book_title| publisher| +----------------+----+-----------+----+------------------+--------------------+-------------+
|Kwesi Manu Prize|2020| Fiction| 1| Akua Mansa| Where did you go?|SomePublisher|
|Kwesi Manu Prize|2020| Fiction| 2| John Stiles| Yesterday|Example Books|
|Kwesi Manu Prize|2020| Fiction| 3| Nikki Wolf|Moving to the Cha...| AnyPublisher|
| Wolf|2020|Non-Fiction| 1| Wang Xiulan| History of Ideas|Example Books|
| Wolf|2020|Non-Fiction| 2|Ana Carolina Silva| Science Today|SomePublisher|
| Wolf|2020|Non-Fiction| 3| Shirley Rodriguez|The Future of Sea...| AnyPublisher|
| Richard Roe|2020| Fiction| 1| Alejandro Rosalez| Long Summer|SomePublisher|
| Richard Roe|2020| Fiction| 2| Arnav Desai| The Key|Example Books|
| Richard Roe|2020| Fiction| 3| Mateo Jackson| Inside the Whale| AnyPublisher| +----------------+----+-----------+----+------------------+--------------------+-------------+` ``` You can confirm the schema of the data in the `DataFrame` as shown in the following example. ``` scala> df.printSchema ``` The output should look like this. ``` `root
|-- award: string (nullable = true) |-- year: integer (nullable = true) |-- category: string (nullable = true) |-- rank: integer (nullable = true) |-- author: string (nullable = true) |-- book_title: string (nullable = true) |-- publisher: string (nullable = true)` ``` 4. Use the following command to write the data in the `DataFrame` to the Amazon Keyspaces table. ``` df.write.cassandraFormat("book_awards", "catalog").mode("APPEND").save() ``` 5. To confirm that the data was saved, you can read it back to a dataframe, as shown in the following example. ``` var newDf = spark.read.cassandraFormat("book_awards", "catalog").load() ``` Then you can show the data that is now contained in the dataframe. ``` scala> newDf.show() ``` The output of that command should look like this. ``` `+--------------------+------------------+----------------+-----------+-------------+----+----+
| book_title| author| award| category| publisher|rank|year| +--------------------+------------------+----------------+-----------+-------------+----+----+
| Long Summer| Alejandro Rosalez| Richard Roe| Fiction|SomePublisher| 1|2020|
| History of Ideas| Wang Xiulan| Wolf|Non-Fiction|Example Books| 1|2020|
| Where did you go?| Akua Mansa|Kwesi Manu Prize| Fiction|SomePublisher| 1|2020|
| Inside the Whale| Mateo Jackson| Richard Roe| Fiction| AnyPublisher| 3|2020|
| Yesterday| John Stiles|Kwesi Manu Prize| Fiction|Example Books| 2|2020|
|Moving to the Cha...| Nikki Wolf|Kwesi Manu Prize| Fiction| AnyPublisher| 3|2020|
|The Future of Sea...| Shirley Rodriguez| Wolf|Non-Fiction| AnyPublisher| 3|2020|
| Science Today|Ana Carolina Silva| Wolf|Non-Fiction|SomePublisher| 2|2020|
| The Key| Arnav Desai| Richard Roe| Fiction|Example Books| 2|2020| +--------------------+------------------+----------------+-----------+-------------+----+----+` ```
````
