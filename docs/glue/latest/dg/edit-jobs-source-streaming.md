# Using a streaming data source

You can create streaming extract, transform, and load (ETL) jobs that run continuously
and consume data from streaming sources in Amazon Kinesis Data Streams, Apache Kafka, and Amazon Managed Streaming for Apache Kafka
(Amazon MSK).

###### To configure properties for a streaming data source

1. Go to the visual graph editor for a new or saved job.
2. Choose a data source node in the graph for Kafka or Kinesis Data Streams.
3. Choose the **Data source properties** tab, and then enter the following
   information:

Kinesis

    * **Kinesis source type**: Choose the option **Stream
     details** to use direct access to the streaming source or choose
     **Data Catalog table** to use the information stored there
     instead.


    If you choose **Stream details**, specify the following
     additional information.




    	+ **Location of data stream**: Choose whether the
    	 stream is associated with the current user, or if it is associated with a different user.
    	+ **Region**: Choose the AWS Region where the stream
    	 exists. This information is used to construct the ARN for accessing the
    	 data stream.
    	+ **Stream ARN**: Enter the Amazon Resource Name (ARN)
    	 for the Kinesis data stream. If the stream is located within the current
    	 account, you can choose the stream name from the drop-down list. You can
    	 use the search field to search for a data stream by its name or
    	 ARN.
    	+ **Data format**: Choose the format used by the data
    	 stream from the list.


    	AWS Glue automatically detects the schema from the
    	 streaming data.
    If you choose **Data Catalog table**, specify the
     following additional information.




    	+ **Database**: (Optional) Choose the database in the
    	 AWS Glue Data Catalog that contains the table associated with
    	 your streaming data source. You can use the search field to search for a
    	 database by its name.
    	+ **Table**: (Optional) Choose the table associated
    	 with the source data from the list. This table must already exist in the
    	 AWS Glue Data Catalog. You can use the search field to search for
    	 a table by its name.
    	+ **Detect schema**: Choose this option to have
    	 AWS Glue detect the schema from the streaming data, rather
    	 than using the schema information in a Data Catalog table. This option is
    	 enabled automatically if you choose the **Stream
    	 details** option.
    * **Starting position**: By default, the ETL job uses the
     **Earliest** option, which means it reads data starting
     with the oldest available record in the stream. You can instead choose
     **Latest**, which indicates the ETL job should start
     reading from just after the most recent record in the stream.
    * **Window size**: By default, your ETL job processes and
     writes out data in 100-second windows. This allows data to be processed
     efficiently and permits aggregations to be performed on data that arrives
     later than expected. You can modify this window size to increase timeliness or
     aggregation accuracy.


    AWS Glue streaming jobs use checkpoints rather than job bookmarks to track
     the data that has been read.
    * **Connection options**: Expand this section to add
     key-value pairs to specify additional connection options. For information
     about what options you can specify here, see ["connectionType": "kinesis"](aws-glue-programming-etl-connect.md#aws-glue-programming-etl-connect-kinesis "aws-glue-programming-etl-connect.md#aws-glue-programming-etl-connect-kinesis") in the
     *AWS Glue Developer Guide*.

Kafka

    * **Apache Kafka source**: Choose the option
     **Stream details** to use direct access to the streaming
     source or choose **Data Catalog table** to use the
     information stored there instead.


    If you choose **Data Catalog table**, specify the
     following additional information.




    	+ **Database**: (Optional) Choose the database in the
    	 AWS Glue Data Catalog that contains the table associated with
    	 your streaming data source. You can use the search field to search for a
    	 database by its name.
    	+ **Table**: (Optional) Choose the table associated
    	 with the source data from the list. This table must already exist in the
    	 AWS Glue Data Catalog. You can use the search field to search for
    	 a table by its name.
    	+ **Detect schema**: Choose this option to have
    	 AWS Glue detect the schema from the streaming data, rather
    	 than storing the schema information in a Data Catalog table. This option is
    	 enabled automatically if you choose the **Stream
    	 details** option.
    If you choose **Stream details**, specify the following
     additional information.




    	+ **Connection name**: Choose the AWS Glue
    	 connection that contains the access and authentication information for the
    	 Kafka data stream. You must use a connection with Kafka streaming data
    	 sources. If a connection doesn't exist, you can use the
    	 AWS Glue console to create a connection for your Kafka data
    	 stream.
    	+ **Topic name**: Enter the name of the topic to read
    	 from.
    	+ **Data format**: Choose the format to use when
    	 reading data from the Kafka event stream.
    * **Starting position**: By default, the ETL job uses the
     **Earliest** option, which means it reads data starting
     with the oldest available record in the stream. You can instead choose
     **Latest**, which indicates the ETL job should start
     reading from just after the most recent record in the stream.
    * **Window size**: By default, your ETL job processes and
     writes out data in 100-second windows. This allows data to be processed
     efficiently and permits aggregations to be performed on data that arrives
     later than expected. You can modify this window size to increase timeliness or
     aggregation accuracy.


    AWS Glue streaming jobs use checkpoints rather than job bookmarks to track
     the data that has been read.
    * **Connection options**: Expand this section to add
     key-value pairs to specify additional connection options. For information
     about what options you can specify here, see ["connectionType": "kafka"](aws-glue-programming-etl-connect.md#aws-glue-programming-etl-connect-kafka "aws-glue-programming-etl-connect.md#aws-glue-programming-etl-connect-kafka") in the
     *AWS Glue Developer Guide*.

###### Note

Data previews are not currently supported for streaming data sources.
