# Get the bootstrap brokers using the AWS Management Console

This process describes how to get bootstrap brokers for a cluster using the AWS Management Console. The
term _bootstrap brokers_ refers to a list of brokers that an
Apache Kafka client can use as a starting point to connect to the cluster. This list
doesn't necessarily include all of the brokers in a cluster.

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. The table shows all the clusters for the current region under this account.
   Choose the name of a cluster to view its description.
3. On the **Cluster summary** page, choose **View
   client information**. This shows you the bootstrap brokers, as
   well as the Apache ZooKeeper connection string.
