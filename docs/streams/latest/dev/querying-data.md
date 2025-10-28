# Query your data streams in the Kinesis console

The Data Analytics tab in the Kinesis Data Streams Console lets you query your data
streams using SQL. To use this capability, follow these steps:

1. Sign in to the AWS Management Console and open the Kinesis console at
   [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. Choose the active data stream that you want to query with SQL and then choose
   the **Data analytics** tab.
3. In the **Data analytics** tab, you can perform stream
   inspection and visualization with a Managed Apache Flink Studio notebook. You
   can perform ad-hoc SQL queries to inspect your data stream and view results in
   seconds using Apache Zeppelin. In the **Data analytics** tab,
   choose **I agree** and then choose **Create
   notebook** to create a notebook.
4. After the notebook is created, choose **Open in Apache
   Zeppelin**. This will open your notebook in a new tab. A notebook
   is an interactive interface where you can submit your SQL queries. Choose the
   note that contains the name of your stream.
5. You will see a note with a sample `SELECT` query to output the data
   in the stream already running. This lets you view the schema for your data
   stream.
6. To try out other queries such as tumbling or sliding windows, choose
   **View sample queries** in the **Data
   analytics** tab. Copy the query, modify it to suit your data stream
   schema, and then run it in a new paragraph in your Zeppelin note.
