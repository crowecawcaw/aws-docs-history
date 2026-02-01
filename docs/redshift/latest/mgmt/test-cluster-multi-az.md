Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Failing over Multi-AZ deployment

Your Multi-AZ data warehouse is a collection compute resources deployed simultaneously
in two Availability Zones. The compute resources deployed in the primary Availability
Zone are referred to as primary compute and those in the secondary Availability Zones
are referred as secondary compute. A Multi-AZ data warehouse can automatically recover
without any user intervention during an unlikely event such as an Availability Zone or
infrastructure failure. The recovery process involves failing over from primary compute
to secondary compute and designating secondary compute resources as primary.
Additionally, new secondary compute resources are provisioned in a third Availability
Zone. The automatic recovery process is measured in terms of RTO and RPO.

- **Recovery time objective (RTO)** — The
  time it takes a system to return to a working state after a disaster. In other
  words, RTO measures downtime.
- **Recovery point objective (RPO)** — The
  amount of data that can be lost (measured in time). For an Amazon Redshift Multi-AZ
  data warehouse, RPO is typically is zero as all the data is stored in Amazon Redshift
  Managed Storage (RMS), backed by Amazon Simple Storage Service, which is a highly durable and
  available by default.

###### Note

The performance of an individual query performance will not change after a
failover has occurred. The overall throughput of your data warehouse will be reduced
for a short time due to unavailability of compute resources in one of the
Availability Zones. However, Amazon Redshift will automatically acquire capacity in another
Availability Zone to ensure the same data warehouse processing capacity is
restored.

In addition to the automatic recovery process, you can also trigger this process
manually for your data warehouse using the **Failover primary compute**
option. You can use this approach to test how Multi-AZ would help your application for
higher high availability and better continuity.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Do one of the following:
   - On the navigation menu, choose **Clusters**.
     Under **Clusters**, choose a cluster. The
     cluster details page appears.
   - From the cluster dashboard, choose a cluster.

3. From **Actions**, choose **Failover primary
   compute**.
4. When prompted, click **Confirm**.

- From the AWS CLI, use the `failover-primary-compute` command
  as follows.

```
aws redshift failover-primary-compute
    --profile maz-test
    --endpoint-url  https://redshift.eu-west-1.amazonaws.com
    --region eu-west-1
    --cluster-identifier test-maz-11
```

After the above operation is confirmed, Amazon Redshift will perform the same steps as an
automatic recovery from an Availability Zone or infrastructure failure. The process will
cause compute nodes in the primary Availability Zone to become unavailable and compute
resources in the secondary Availability Zone will be designated as primary compute. When
the cluster recovery successfully completes, Multi-AZ deployment becomes available. Your
Multi-AZ data warehouse will also automatically provision new secondary compute in
another third Availability Zone as soon as it is available.

During this process, the cluster status on the console shows as modifying for the
entire time, as the cluster automatically recovers and reconfigures back to the Multi-AZ
deployment setup. The cluster can accept new connections immediately. Existing
connections and inflight queries might be dropped. You can retry them
immediately.
