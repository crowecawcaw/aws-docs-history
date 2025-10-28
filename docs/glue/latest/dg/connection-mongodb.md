# Using a MongoDB or MongoDB Atlas connection

After you create a connection for MongoDB or MongoDB Atlas, you can use the connection in your ETL job.
You create a table in the AWS Glue Data Catalog and specify the MongoDB or MongoDB Atlas connection for the
`connection` attribute of the table.

AWS Glue stores your connection `url` and credentials in the MongoDB
connection. The connection URI formats are as follows:

- For MongoDB: mongodb://host:port/database. The host can be a hostname, IP address, or UNIX domain socket. If the connection string doesn't specify a port, it uses the default MongoDB port, 27017.
- For MongoDB Atlas: mongodb+srv://server.example.com/database. The host can be a hostname that follows corresponds to a DNS SRV record. The SRV format does not require a port and will use the default MongoDB port, 27017.
  Additionally, you can specify options in your job
  script. For more information, see [MongoDB connection option reference](aws-glue-programming-etl-connect-mongodb-home.md#aws-glue-programming-etl-connect-mongodb "aws-glue-programming-etl-connect-mongodb-home.md#aws-glue-programming-etl-connect-mongodb").
