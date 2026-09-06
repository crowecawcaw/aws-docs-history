

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Confirming the status of evidence finder
<a name="confirm-status-of-evidence-finder"></a>



After you submit your request to enable evidence finder, it takes up to 10 minutes to enable the feature and create an event data store. As soon as the event data store is created, all new evidence is ingested into the event data store moving forward. 

When evidence finder is enabled and the event data store is created, we backfill the newly created event data store with up to two years' worth of your past evidence. This process happens automatically and takes up to seven days to complete. 

Follow the steps on this page to check and understand the status of your request to enable evidence finder.

## Prerequisites
<a name="confirm-status-of-evidence-finder-prerequisites"></a>

Make sure that you followed the steps to enable evidence finder. For instructions, see [Enabling evidence finder](evidence-finder-settings-enable.md).

## Procedure
<a name="confirm-status-of-evidence-finder-procedure"></a>

You can check the current status of evidence finder using the Audit Manager console, the AWS CLI, or the Audit Manager API.

------
#### [ Audit Manager console ]

**To see the current status of evidence finder on the Audit Manager console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the left navigation pane, choose **Settings**.

1. Under **Enable evidence finder – optional**, review the current status.

   Each status is defined as follows:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/confirm-status-of-evidence-finder.html)

------
#### [ AWS CLI ]

**To see the current status of evidence finder in the AWS CLI**  
Run the [get-settings](https://docs.aws.amazon.com/cli/latest/reference/auditmanager/get-settings.html) command with the `--attribute` parameter set to `EVIDENCE_FINDER_ENABLEMENT`.

```
aws auditmanager get-settings --attribute EVIDENCE_FINDER_ENABLEMENT 
```

This returns the following information:

**enablementStatus**  
This attribute shows the current status of evidence finder.
+ `ENABLE_IN_PROGRESS` – You requested to enable evidence finder. An event data store is currently being created to support evidence finder queries.
+ `ENABLED` – An event data store was created and evidence finder is enabled. We recommend waiting seven days until the event data store is backfilled with your past evidence data. You can use evidence finder in the meantime, but not all data is available until the backfill is complete.
+ `DISABLE_IN_PROGRESS` – You requested to disable evidence finder, and your request is pending the event data store being deleted.
+ `DISABLED` – You permanently disabled evidence finder and the event data store is deleted. You can't re-enable evidence finder after this point.

**backfillStatus**  
This attribute shows the current status of the evidence data backfill. 
+ `NOT_STARTED` – The backfill hasn't started yet. 
+ `IN_PROGRESS` – The backfill is in progress. This takes up to seven days to complete, depending on the amount of evidence data. 
+ `COMPLETED` – The backfill is complete. All of your past evidence is now queryable. 

------
#### [ Audit Manager API ]

**To see the current status of evidence finder using the API**  
Call the [GetSettings](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetSettings.html) operation with the `attribute` parameter set to `EVIDENCE_FINDER_ENABLEMENT`. This returns the following information:

**enablementStatus**  
This attribute shows the current status of evidence finder.
+ `ENABLE_IN_PROGRESS` - You requested to enable evidence finder. An event data store is currently being created to support evidence finder queries.
+ `ENABLED` - An event data store was created and evidence finder is enabled. We recommend waiting seven days until the event data store is backfilled with your past evidence data. You can use evidence finder in the meantime, but not all data is available until the backfill is complete.
+ `DISABLE_IN_PROGRESS` - You requested to disable evidence finder, and your request is pending the deletion of the event data store.
+ `DISABLED` - You permanently disabled evidence finder and the event data store is deleted. You can't re-enable evidence finder after this point.

**backfillStatus**  
This attribute shows the current status of the evidence data backfill. 
+ `NOT_STARTED` means that the backfill hasn't started yet. 
+ `IN_PROGRESS` means that the backfill is in progress. This takes up to seven days to complete, depending on the amount of evidence data. 
+ `COMPLETED` means that the backfill is complete. All of your past evidence is now queryable.

For more information, see [evidenceFinderEnablement](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_EvidenceFinderEnablement.html) in the *Audit Manager API Reference*.

------

## Next steps
<a name="confirm-status-of-evidence-finder-next-steps"></a>

After evidence finder is successfully enabled, you can start using the feature. We recommend waiting seven days until the event data store is backfilled with your past evidence data. You can use evidence finder in the meantime, but not all data might be available until the backfill is complete. 

To get started with evidence finder, see [Searching for evidence in evidence finder](search-for-evidence-in-evidence-finder.md).

## Additional resources
<a name="confirm-status-of-evidence-finder-additional-resources"></a>
+ [Troubleshooting evidence finder issues](evidence-finder-issues.md)