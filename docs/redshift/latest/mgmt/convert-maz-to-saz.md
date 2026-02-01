Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Converting a Multi-AZ data warehouse to a Single-AZ

data warehouse

By converting a Multi-AZ data warehouse to a Single-AZ data warehouse, your data
warehouse will not get the 99.99% SLA guarantee which Multi-AZ offers. The performance
of an individual query will remain same but the overall throughput will be affected
because compute resources in the second Availability Zone won't be available. You
have the option to enable concurrency scaling to automatically scale throughput for
consistent performance even with Single-AZ.

###### Note

Amazon Redshift will not allow you to split existing compute resources while converting
from Single-AZ to Multi-AZ, or vice versa. This operation isn't supported to
maintain consistent individual query performance.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Provisioned clusters
   dashboard**, and choose **Clusters**. The
   clusters for your account in the current AWS Region are listed. A
   subset of properties of each cluster is displayed in columns in the
   list.
3. Choose the cluster you want to convert to a Multi-AZ deployment. The
   cluster details page appears.
4. For **Actions**, choose **Deactivate
   Multi-AZ**. The modification summary appears. Click
   **Deactivate Multi-AZ**.

- From the AWS CLI, use the `modify-cluster` command and the
  `no-multi-az` parameter as follows.

```
aws redshift modify-cluster
    --profile maz-test
    --endpoint-url  https://redshift.eu-west-1.amazonaws.com
    --region eu-west-1
    --cluster-identifier test-maz-11
    --no-multi-az
```

Once your data warehouse is converted to Single-AZ, it will lose the 99.99 SLA
guarantee. Overall throughput will also be impacted. When the changes are saved, you can
view the details in the cluster details page.
