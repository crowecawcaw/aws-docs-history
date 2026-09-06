

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating the synchronization of Amazon WorkSpaces from AWS Config
<a name="validating-config"></a>

 Validate the synchronization of Amazon WorkSpaces in AWS Config by executing a scheduled job. 

**To validate the synchronization of Amazon WorkSpaces in AWS Config**

1. Execute the scheduled job **synchronize Amazon WorkSpaces** manually. 

1. Navigate to **AWS Config**, and then choose **WorkSpaces**. 

1. Validate the data.

**Note**  
Amazon WorkSpaces synchronization is only supported for stand-alone accounts, not for AWS Config Aggregator accounts.   
The **SyncUser** role must include the `DescribeWorkSpacesPolicy` for the synchronization to execute successfully. 