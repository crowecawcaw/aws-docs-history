Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Program your Managed Service for Apache Flink Python application

You code your Managed Service for Apache Flink for Python application using the Apache Flink Python Table API. The Apache Flink engine translates
Python Table API statements (running in the Python VM) into Java Table API statements (running in the Java VM).

You use the Python Table API by doing the following:

- Create a reference to the `StreamTableEnvironment`.
- Create `table` objects from your source streaming data by executing queries on the `StreamTableEnvironment`
  reference.
- Execute queries on your `table` objects to create output tables.
- Write your output tables to your destinations using a `StatementSet`.
  To get started using the Python Table API in Managed Service for Apache Flink, see [Get started with Amazon Managed Service for Apache Flink for Python](gs-python.md "gs-python.md").

## Read and write streaming data

To read and write streaming data, you execute SQL queries on the table environment.

### Create a table

The following code example demonstrates a user-defined function that creates a SQL query. The SQL query
creates a table that interacts with a Kinesis stream:

```
def create_table(table_name, stream_name, region, stream_initpos):
   return """ CREATE TABLE {0} (
                `record_id` VARCHAR(64) NOT NULL,
                `event_time` BIGINT NOT NULL,
                `record_number` BIGINT NOT NULL,
                `num_retries` BIGINT NOT NULL,
                `verified` BOOLEAN NOT NULL
              )
              PARTITIONED BY (record_id)
              WITH (
                'connector' = 'kinesis',
                'stream' = '{1}',
                'aws.region' = '{2}',
                'scan.stream.initpos' = '{3}',
                'sink.partitioner-field-delimiter' = ';',
                'sink.producer.collection-max-count' = '100',
                'format' = 'json',
                'json.timestamp-format.standard' = 'ISO-8601'
              ) """.format(table_name, stream_name, region, stream_initpos)
```

### Read streaming data

The following code example demonstrates how to use preceding `CreateTable`SQL query on a table environment reference
to read data:

```
   table_env.execute_sql(create_table(input_table, input_stream, input_region, stream_initpos))
```

### Write streaming data

The following code example demonstrates how to use the SQL query from the `CreateTable` example to create
an output table reference, and how to use a `StatementSet` to interact with the tables to write
data to a destination Kinesis stream:

```
   table_result = table_env.execute_sql("INSERT INTO {0} SELECT * FROM {1}"
                       .format(output_table_name, input_table_name))

```

## Read runtime properties

You can use runtime properties to configure your application without changing your application code.

You specify application properties for your application the same way as with a Managed Service for Apache Flink for Java application. You
can specify runtime properties in the following ways:

- Using the
  [CreateApplication](../apiv2/API_CreateApplication.md "../apiv2/API_CreateApplication.md")
  action.
- Using the
  [UpdateApplication](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md")
  action.
- Configuring your application by using the console.

You retrieve application properties in code by reading a json file called `application_properties.json` that
the Managed Service for Apache Flink runtime creates.

The following code example demonstrates reading application properties from the
`application_properties.json` file:

```
file_path = '/etc/flink/application_properties.json'
   if os.path.isfile(file_path):
       with open(file_path, 'r') as file:
           contents = file.read()
           properties = json.loads(contents)
```

The following user-defined function code example demonstrates reading a property group from the application properties object:
retrieves:

```
def property_map(properties, property_group_id):
   for prop in props:
       if prop["PropertyGroupId"] == property_group_id:
           return prop["PropertyMap"]
```

The following code example demonstrates reading a property called INPUT_STREAM_KEY from a property group that the previous example returns:

```
input_stream = input_property_map[INPUT_STREAM_KEY]
```

## Create your application's code package

Once you have created your Python application, you bundle your code file and dependencies into a zip file.

Your zip file must contain a python script with a `main` method, and can optionally
contain the following:

- Additional Python code files
- User-defined Java code in JAR files
- Java libraries in JAR files

###### Note

Your application zip file must contain all of the dependencies for your application. You can't reference
libraries from other sources for your application.
