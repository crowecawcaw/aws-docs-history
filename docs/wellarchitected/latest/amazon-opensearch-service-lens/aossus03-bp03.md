

# AOSSUS03-BP03 Take manual snapshots of your indices only when it is difficult to recreate the dataset
<a name="aossus03-bp03"></a>

 Reduce unnecessary snapshot creation, Amazon EBS, and Amazon S3 storage costs by taking manual snapshots only when it's difficult to recreate the dataset. 

 **Level of risk exposed if this best practice is not established:** Medium 

 **Desired outcome:** You take manual snapshots of indices only when it is difficult to recreate the dataset, reducing unnecessary snapshot creation and Amazon S3 storage. 

 **Benefits of establishing this best practice:** 
+  Reduced Amazon EBS and Amazon S3 storage costs 
+  Improved resource utilization and reduced waste 

## Implementation guidance
<a name="implementation-guidance-62"></a>

 Snapshots in Amazon OpenSearch Service serve as backups for a domain's indexes and state. Excessive snapshot leads to unnecessary storage and energy wastage. 

 Delete unneeded snapshots using `DELETE _snapshot/repository-name/snapshot-name`. 

## Resources
<a name="resources-62"></a>
+  [Deleting manual snapshots](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-snapshots.html#managedomains-snapshot-delete) 