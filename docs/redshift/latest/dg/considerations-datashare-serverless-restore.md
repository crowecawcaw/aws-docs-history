

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Considerations for data sharing in Amazon Redshift Serverless restore
<a name="considerations-datashare-serverless-restore"></a>

Consider following when working with datashares during Amazon Redshift Serverless restore operations:

**Restore snapshot to a Amazon Redshift Serverless producer namespace:**
+ Restoring a snapshot to a Amazon Redshift Serverless producer namespace replaces the current datashares with the datashares in the snapshot. However, a datashare permission will only be maintained if ALL of the following conditions are met:
  + The snapshot is taken on the same namespace the customer is restoring to, AND
  + The datashare permission exists on the current namespace, AND
  + The datashare permission existed on the namespace when the snapshot was taken.
+ If a datashare was granted to a consumer when taking the snapshot, but was dropped or the grant was revoked on the latest namespace, the datashare will be restored. However, datashare permissions granted to consumer clusters are no longer valid after restore. To revive datashare access, re-grant usage permissions of datashares to desired consumer clusters.
+ If a datashare is granted to a consumer on the latest namespace, but was not granted when taking the snapshot, the datashare access won't be maintained after restore.
+ Datashare authorization/association scope won't change on the namespace after restore. For example, before restore if a datashare is associated to the entire AWS account, after restore the association scope will remain at account level regardless of the association scope when taking the snapshot.
+ Restoring from a snapshot will revert the publicly accessible setting to its state at the time the snapshot was created, regardless of any subsequent changes.

**Restore snapshot to a Amazon Redshift Serverless consumer namespace:**
+ Restoring a consumer namespace preserves datashare access without requiring the producer administrator to re-grant usage. However, if the database created from the datashare no longer exists after restore, the consumer must recreate it from the datashare.