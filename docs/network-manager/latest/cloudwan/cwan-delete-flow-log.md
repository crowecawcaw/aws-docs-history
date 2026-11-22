

# Delete an AWS Cloud WAN Flow Logs record

You can delete a Cloud WAN flow log using the Network Manager console. 

These procedures disable the flow log service for a resource. Deleting a flow log does not delete the existing log streams from CloudWatch Logs or log files from Amazon S3. Existing flow log data must be deleted using the respective service's console. In addition, deleting a flow log that publishes to Amazon S3 does not remove the bucket policies and log file access control lists (ACLs).

**To delete a Cloud WAN flow log**

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Choose either **Core networks** or **Attachments**, and then choose a core network or attachment.

1. In the Flow logs section, choose the flow logs that you want to delete.

1. Choose **Actions**, and then choose **Delete flow logs**.

1. Confirm that you want to delete the flow by choosing **Delete**.