Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Managing workload exclusions from Autonomics

You can exclude specific provisioned endpoints or serverless workgroups from influencing autonomics decisions like distribution key and sort key through a denylist feature. This allows you to control which workloads Amazon Redshift considers when making optimization decisions for your Redshift Managed Storage (RMS) data.

**Using the denylist**

You can manage the denylist through the Autonomics section in the Amazon Redshift console:

1. **Add or remove items**

Add specific provisioned endpoints or serverless workgroups to the denylist, and remove them when needed. 2. **View and search**

View all denylisted items and search for specific endpoints or workgroups in the denylist.
The denylist is particularly useful when you run data marketplaces, share data with external users, or have multiple business units, where you want to prevent certain usage patterns from influencing optimization decisions suitable for your workload. For example, if workgroup A runs workload A, and workgroup B runs workload B on a shared table T, the sort key of T will be determined by both workloads A and B. If you want that only workload A should influence the sort key decision, then add workgroup B to the deny list of the endpoint or workgroup which owns table T. By default, Amazon Redshift Autonomics considers query patterns from the producer and all consumer clusters/workgroups unless specifically excluded through the denylist.

###### Note

You can denylist resources across different AWS Regions within the same account. Cross-account denylisting is not yet supported.

## Managing denylist resources in the Amazon Redshift console

On the Amazon Redshift Serverless console, complete the following steps:

1. Choose Clusters or Serverless workgroups.
2. Navigate to a specific cluster or workgroup details page.
3. Choose Autonomics in the tabs section.
4. Under the Autonomics tab, you can view and manage your denylist.
5. For managing cross-region denylist, choose the corresponding AWS Region.

## Adding denylist resources

1. Navigate to the Autonomics tab of the selected cluster or workgroup, select the AWS Region, and choose Add resources.
2. Select one or more Provisioned clusters or Serverless workgroups to add to denylist and choose Add.
3. The table shows the list of denylist resources.

## Remove denylist resources

1. Navigate to the Autonomics tab of the selected cluster or workgroup, select the AWS Region.
2. Choose the cluster or workgroup you want to delete from the list and select Remove.
3. A confirmation dialog box opens. Select Remove to confirm.
