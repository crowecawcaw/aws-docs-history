

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# AWS Systems Manager Change Manager in ServiceNow
<a name="sn-config-change-mgr"></a>

AWS Service Management Connector includes a curated version of the Change Manager integration. To allow the Connector to synchronize change templates, the change templates should be: 
+ An Approved status in AWS
+ At least one Automation Runbook associated with it
+ Enabled as auto-approval

For more information, see [AWS Systems Manager Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html).

You can also view resources affected by the changes that were executed on their AWS accounts from the AWS CloudTrail events available on the AWS change request.

**Note**  
Currently, only the first level events that occurred in the execution of an automation document will be tracked and synched. Steps which have nested automations will not have the events synced. This can however be traced separately in the AWS CloudTrail console using Lake feature by their unique automation execution ID. 

## Fields mapped from AWS Change Request Ops Item records to ServiceNow Change Request records
<a name="fields-change-request"></a>

This table shows how AWS Change Request Ops items map to ServiceNow Change Request.


| AWS Change Request Ops Item | ServiceNow Change Request | 
| --- | --- | 
| AWS Account | x\_126749\_aws\_sc\_awsaccount | 
| AWS Request ID | x\_126749\_aws\_sc\_awsrequestid | 
| AWS Region | x\_126749\_aws\_sc\_awsregion | 
| AWS Status | x\_126749\_aws\_sc\_awsstatus | 