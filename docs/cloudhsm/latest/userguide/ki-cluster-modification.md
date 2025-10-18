# Known issues for AWS CloudHSM cluster modification

The following issues impact customers attempting to use the modify-cluster API to change the HSM type of a cluster.

###### Topics

* [Issue: Login latency increases due to increased PBKDF2 iterations](#ki-cluster-modification-1 "#ki-cluster-modification-1")
* [Issue: Unable to modify HSM type due to token key creation](#ki-cluster-modification-2 "#ki-cluster-modification-2")

## Issue: Login latency increases due to increased PBKDF2 iterations



* **Impact:** Clusters with a large amount of users will experience an extended migration period. This is due to changes in the 
 backup restoration process performing PBKDF2 operations per user when restoring an hsm1.medium backup to hsm2m.medium for the first time.
* **Workaround:** Design your applications to be resilient to an extended migration period.
* **Resolution status:** No resolution status.

## Issue: Unable to modify HSM type due to token key creation



* **Impact:** Customers performing token key based workloads will be unable to start their migration. This is done because the HSM will be placed 
 into a limited-write mode to prevent dataloss scenarios during the HSM type modification.
* **Workaround:** Stop creating and deleting token keys and then wait 7 days. Alternatively, please reach out to support if you




	+ Cannot handle blocking token key migrations and cannot do a blue/green deployment.
	+ Can handle blocking token key operations for the duration of the migration, but can’t wait the full 7 day period.
* **Resolution status:** This issue has been resolved. Customers performing token key based workloads can now begin the migration. Token key creations and deletions will be blocked for the duration of the migration.
