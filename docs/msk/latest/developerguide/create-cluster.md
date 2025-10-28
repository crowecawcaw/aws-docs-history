# Step 1: Create an MSK Provisioned cluster

In this step of [Getting Started Using Amazon MSK](getting-started.md "getting-started.md"), you create an Amazon MSK Provisioned cluster. You use the **Quick create** option in the AWS Management Console to create this cluster.

###### To create an Amazon MSK cluster using the AWS Management Console

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. Choose **Create cluster**.
3. For **Creation method**, leave the **Quick create** option selected. The **Quick create** option lets you create a cluster with default settings.
4. For **Cluster name**, enter a descriptive name for your cluster. For example, `MSKTutorialCluster`.
5. For **General cluster properties**, do the following:
   1. For **Cluster type**, choose **Provisioned**.
   2. Choose an **Apache Kafka version** to run on the brokers. Choose **View version compatibility** to see a comparison table.
   3. For **Broker type**, choose either Standard or Express brokers.
   4. Choose a **Broker size**.

6. From the table under **All cluster settings**, copy the values of the following settings and save them because you need them later in this tutorial:
   - VPC
   - Subnets
   - Security groups associated with VPC

7. Choose **Create cluster**.
8. Check the cluster **Status** on the **Cluster summary** page. The status changes from **Creating** to **Active** as Amazon MSK provisions the cluster. When the status is **Active**, you can connect to the cluster. For more information about cluster status, see [Understand MSK Provisioned cluster states](msk-cluster-states.md "msk-cluster-states.md").
   **Next Step**

[Step 2: Create an IAM role granting access to create topics on the Amazon MSK cluster](create-client-iam-role.md "create-client-iam-role.md")
