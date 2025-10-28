# Delete an AWS Transit Gateway Flow Logs record

You can delete a transit gateway flow log using the Amazon VPC console.

These
procedures disable the flow log service for a resource. Deleting a flow log does not
delete the existing log streams from CloudWatch Logs or log files from Amazon S3. Existing flow log
data must be deleted using the respective service's console. In addition, deleting a
flow log that publishes to Amazon S3 does not remove the bucket policies and log file
access control lists (ACLs).

###### To delete a transit gateway flow log

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit
   gateways**.
3. Choose a **Transit gateway ID**.
4. In the Flow logs section, choose the flow logs that you want to
   delete.
5. Choose **Actions**, and then choose **Delete flow
   logs**.
6. Confirm that you want to delete the flow by choosing
   **Delete**.
