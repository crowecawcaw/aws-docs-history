# Collections of common errors in Amazon EMR

Sometimes, clusters fail or are slow to process data. The following sections list
common cluster issues. Errors include bootstrap failures and validation errors, with
suggestions on how to resolve them.

###### Topics

- [Error codes with ErrorDetail
  information in Amazon EMR](emr-troubleshoot-error-errordetail.md "emr-troubleshoot-error-errordetail.md")
- [Resource errors during Amazon EMR cluster operations](emr-troubleshoot-error-resource.md "emr-troubleshoot-error-resource.md")
- [Cluster input and output errors during Amazon EMR operations](emr-troubleshoot-errors-io.md "emr-troubleshoot-errors-io.md")
- [Permissions errors during Amazon EMR cluster operations](emr-troubleshoot-error-permissions.md "emr-troubleshoot-error-permissions.md")
- [Hive cluster errors](emr-troubleshoot-error-hive.md "emr-troubleshoot-error-hive.md")
- [VPC errors during Amazon EMR cluster operations](emr-troubleshoot-error-vpc.md "emr-troubleshoot-error-vpc.md")
- [Streaming Amazon EMR cluster errors](emr-troubleshoot-error-streaming.md "emr-troubleshoot-error-streaming.md")
- [Amazon EMR: Custom JAR cluster errors](emr-troubleshoot-error-custom-jar.md "emr-troubleshoot-error-custom-jar.md")
- [Amazon EMR AWS GovCloud (US-West) errors](emr-troubleshoot-error-govcloud.md "emr-troubleshoot-error-govcloud.md")
- [Find a missing cluster](#w227aac36c21c47 "#w227aac36c21c47")

## Find a missing cluster

If your cluster is missing from the console list or `ListClusters` API,
check the following:

- Confirm that the cluster age from time of completion is less than two months.
  Amazon EMR preserves metadata information for completed clusters for two months at no
  charge. You can't delete completed clusters from the console — instead,
  Amazon EMR purges completed clusters automatically after two months.
- Confirm that you have role permissions to view the cluster.
- Confirm that you are viewing the same AWS Region where the cluster resides.
