# Create a

Amazon MSK cluster with tiered storage with the AWS Management Console

This process describes how to create a tiered storage Amazon MSK cluster using the AWS Management Console.

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/ "https://console.aws.amazon.com/msk/").
2. Choose **Create cluster**.
3. Choose **Custom create** for tiered storage.
4. Specify a name for the cluster.
5. In the **Cluster type**, select
   **Provisioned**.
6. Choose an Amazon Kafka version that supports tiered storage for Amazon MSK to
   use to create the cluster.
7. Specify a size of broker other than
   **kafka.t3.small**.
8. Select the number of brokers that you want Amazon MSK to create in each
   Availability Zone. The minimum is one broker per Availability Zone, and the
   maximum is 30 brokers per cluster.
9. Specify the number of zones that brokers are distributed across.
10. Specify the number of Apache Kafka brokers that are deployed per
    zone.
11. Select **Storage options**. This includes
    **Tiered storage and EBS storage** to enable tiered
    storage mode.
12. Follow the remaining steps in the cluster creation wizard. When complete,
    **Tiered storage and EBS storage** appears as the
    cluster storage mode in the **Review and create**
    view.
13. Select **Create cluster**.
