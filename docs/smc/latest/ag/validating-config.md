End of support notice: On March 31, 2027, AWS
will end support for AWS Service Management Connector. After March 31, 2027, you will
no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources.
For more information, see [AWS Service Management Connector end of support](smc-end-of-support.md "smc-end-of-support.md").

# Validating the synchronization of Amazon WorkSpaces from AWS Config

Validate the synchronization of Amazon WorkSpaces in AWS Config by executing a scheduled job.

###### To validate the synchronization of Amazon WorkSpaces in AWS Config

1. Execute the scheduled job **synchronize Amazon WorkSpaces** manually.
2. Navigate to **AWS Config**, and then choose **WorkSpaces**.
3. Validate the data.

###### Note

Amazon WorkSpaces synchronization is only supported for stand-alone
accounts, not for AWS Config Aggregator accounts.

The **SyncUser**
role must include the `DescribeWorkSpacesPolicy`
for the synchronization to execute successfully.
