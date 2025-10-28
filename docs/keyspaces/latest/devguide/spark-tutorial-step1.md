# Step 1: Configure Amazon Keyspaces for integration with the

Apache Cassandra Spark Connector

In this step, you confirm that the partitioner for your account is compatible with the Apache Spark Connector and setup the required IAM permissions. The following best practices help you to provision sufficient read/write capacity for the table.

1. Confirm that the `Murmur3Partitioner` partitioner is the default partitioner for your account. This partitioner is compatible with the Spark
   Cassandra Connector. For more information on partitioners and how to change
   them, see [Working with partitioners in Amazon Keyspaces](working-with-partitioners.md "working-with-partitioners.md").
2. Setup your IAM permissions for Amazon Keyspaces, using interface VPC endpoints, with Apache Spark.
   - Assign read/write access to the user table and read access to the system tables as shown in the IAM policy example listed below.
   - Populating the system.peers table with your available interface VPC endpoints is required for clients accessing Amazon Keyspaces with
     Spark over [VPC endpoints](vpc-endpoints.md "vpc-endpoints.md").

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "cassandra:Select",
            "cassandra:Modify"
         ],
         "Resource":[
            "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/mykeyspace/table/mytable",
            "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/system*"
         ]
      },
      {
         "Sid":"ListVPCEndpoints",
         "Effect":"Allow",
         "Action":[
            "ec2:DescribeNetworkInterfaces",
            "ec2:DescribeVpcEndpoints"
         ],
         "Resource":"*"
      }
   ]
}
```

3. Consider the following best practices to configure sufficient read/write
   throughput capacity for your Amazon Keyspaces table to support the traffic from the Spark
   Cassandra Connector.
   - Start using on-demand capacity to help you test the
     scenario.
   - To optimize the cost of table throughput for production environments,
     use a rate limiter for traffic from the connector, and configure your
     table to use provisioned capacity with automatic scaling. For more
     information, see [Manage throughput capacity automatically with Amazon Keyspaces auto scaling](autoscaling.md "autoscaling.md").
   - You can use a fixed rate limiter that comes with the Cassandra driver.
     There are some [rate limiters tailored to Amazon Keyspaces](https://github.com/aws-samples/amazon-keyspaces-java-driver-helpers "https://github.com/aws-samples/amazon-keyspaces-java-driver-helpers") in the [AWS samples](https://github.com/aws-samples "https://github.com/aws-samples")
     repo.
   - For more information about capacity management, see [Configure read/write capacity modes in Amazon Keyspaces](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md").
