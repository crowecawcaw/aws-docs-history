# Validating the synchronization of Amazon WorkSpaces

from AWS Config

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
