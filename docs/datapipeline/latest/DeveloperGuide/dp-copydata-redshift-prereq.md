AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Set up Pipeline, Create a Security Group, and

Create an Amazon Redshift Cluster

###### To set up for the tutorial

1. Complete the tasks in [Setting up for AWS Data Pipeline](dp-get-setup.md "dp-get-setup.md").
2. Create a security group.
   1. Open the Amazon EC2 console.
   2. In the navigation pane, click **Security Groups**.
   3. Click **Create Security Group**.
   4. Specify a name and description for the security group.
   5. [EC2-Classic] Select `No VPC` for **VPC**.
   6. [EC2-VPC] Select the ID of your VPC for **VPC**.
   7. Click **Create**.

3. [EC2-Classic] Create an Amazon Redshift cluster security group and specify the Amazon EC2 security group.
   1. Open the Amazon Redshift console.
   2. In the navigation pane, click **Security Groups**.
   3. Click **Create Cluster Security Group**.
   4. In the **Create Cluster Security Group** dialog box,
      specify a name and description for the cluster security group.
   5. Click the name of the new cluster security group.
   6. Click **Add Connection Type**.
   7. In the **Add Connection Type** dialog box, select
      **EC2 Security Group** from **Connection Type**,
      select the security group that you created from **EC2 Security Group Name**,
      and then click **Authorize**.

4. [EC2-VPC] Create an Amazon Redshift cluster security group and specify the VPC security group.
   1. Open the Amazon EC2 console.
   2. In the navigation pane, click **Security Groups**.
   3. Click **Create Security Group**.
   4. In the **Create Security Group** dialog box,
      specify a name and description for the security group, and
      select the ID of your VPC for **VPC**.
   5. Click **Add Rule**. Specify the type, protocol, and port range,
      and start typing the ID of the security group in **Source**.
      Select the security group that you created in the second step.
   6. Click **Create**.

5. The following is a summary of the steps.

If you have an existing Amazon Redshift cluster, make a note of the cluster ID.

To create a new cluster and load sample data, follow the steps in [Getting Started with Amazon Redshift](../../../redshift/latest/gsg/getting-started.md "../../../redshift/latest/gsg/getting-started.md"). For
more information about creating clusters, see [Creating a
Cluster](../../../redshift/latest/mgmt/managing-clusters-console.md#create-cluster "../../../redshift/latest/mgmt/managing-clusters-console.md#create-cluster") in the _Amazon Redshift Management Guide_.

    1. Open the Amazon Redshift console.
    2. Click **Launch Cluster**.
    3. Provide the required details for your cluster, and then click **Continue**.
    4. Provide the node configuration, and then click **Continue**.
    5. On the page for additional configuration information, select the cluster security group that you created,
     and then click **Continue**.
    6. Review the specifications for your cluster, and then click **Launch Cluster**.
