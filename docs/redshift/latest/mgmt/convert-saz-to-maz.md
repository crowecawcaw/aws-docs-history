Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Converting a Single-AZ data warehouse to a Multi-AZ

data warehouse

By converting a Single-AZ data warehouse to a Multi-AZ data warehouse, your data
warehouse will be highly available with 99.99% SLA guarantee. The performance of an
individual query will remain same even with a Multi-AZ data warehouse. For higher
concurrency workloads, you will see a boost in overall throughput as Amazon Redshift can execute
requests using compute resources in two Availability Zones.

###### Note

Amazon Redshift will not allow you to split existing compute resources while converting
from Single-AZ to Multi-AZ, or vice versa. This operation isn't supported to
maintain consistent individual query performance.

###### To convert a Single-AZ cluster to a Multi-AZ data warehouse using the

console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Provisioned clusters
   dashboard**, and choose **Clusters**. The
   clusters for your account in the current AWS Region are listed. A
   subset of properties of each cluster is displayed in columns in the
   list.
3. Choose the cluster you want to convert to a Multi-AZ deployment. The
   cluster details page appears.
4. For **Actions**, choose **Activate
   Multi-AZ**. The modification summary appears. Click
   **Activate Multi-AZ**.
5. When there is an error, do one of the following, then click
   **Activate Multi-AZ**.
   - Cluster encryption — Choose
     **Properties** to edit the encryption
     settings in the Database configuration section under the
     Properties tab of the cluster details page.
   - Subnet group — Choose **Subnet group**
     to edit the cluster subnet group settings by clicking the subnet
     group link. If you choose another cluster subnet group, make
     sure that there are 3 Availability Zones in the subnet group you
     selected.
   - Port settings — Choose **Properties**
     to edit the port setting in the Database configuration section
     under the Properties tab of the cluster details page.

6. You can use your SQL client to load and query data.

- From the AWS CLI, use the `modify-cluster` command and the
  `multi-az` parameter as follows.

```
aws redshift modify-cluster
    --profile maz-test
    --endpoint-url https://redshift.eu-west-1.amazonaws.com
    --region eu-west-1
    --cluster-identifier test-maz-11
    --multi-az
```

You can't use STL, SVCS, SVL, SVV, or STV views with Multi-AZ deployments because they
only support system monitoring views (SYS\_\* views). Change your monitoring queries to
use system monitoring views (SYS\_\* views).
