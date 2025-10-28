AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Specify custom IAM roles

By default, AWS Data Pipeline passes `DataPipelineDefaultRole` as the
Amazon EMR service role and `DataPipelineDefaultResourceRole` as the
Amazon EC2 instance profile to create resources on your behalf. However, you can
create a custom Amazon EMR service role and a custom instance profile and use
them instead. AWS Data Pipeline should have sufficient permissions to create clusters
using the custom role, and you must add AWS Data Pipeline as a trusted entity.

The following example object specifies custom roles for the Amazon EMR
cluster:

```
{
   "id":"MyEmrCluster",
   "type":"EmrCluster",
   "hadoopVersion":"2.`x`",
   "keyPair":"my-key-pair",
   "masterInstanceType":"m3.xlarge",
   "coreInstanceType":"m3.large",
   "coreInstanceCount":"10",
   "taskInstanceType":"m3.large",
   "taskInstanceCount":"10",
   "role":"emrServiceRole",
   "resourceRole":"emrInstanceProfile"
}
```
