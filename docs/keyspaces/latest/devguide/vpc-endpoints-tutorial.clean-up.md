

# Step 7: (Optional) Clean up
<a name="vpc-endpoints-tutorial.clean-up"></a>

If you want to delete the resources that you have created in this tutorial, follow these procedures.

**To remove your VPC endpoint for Amazon Keyspaces**

1. Log in to your Amazon EC2 instance.

1. Determine the VPC endpoint ID that is used for Amazon Keyspaces. If you omit the `grep` parameters, VPC endpoint information is shown for all services.

   ```
   aws ec2 describe-vpc-endpoint-services | grep ServiceName | grep cassandra
    
   {
       "VpcEndpoint": {
           "PolicyDocument": "{\"Version\":\"2000-00-00",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"*\",\"Resource\":\"*\"}]}", 
           "VpcId": "vpc-a1234bcd", 
           "State": "available", 
           "ServiceName": "com.amazonaws.us-east-1.cassandra", 
           "RouteTableIds": [], 
           "VpcEndpointId": "vpce-1a23b4c5", 
           "CreationTimestamp": "2025-07-26T22:00:14Z"
       }
   }
   ```

   In the example output, the VPC endpoint ID is {{vpce-1a23b4c5}}. Make sure to replace this value with your own.

1. Delete the VPC endpoint.

   ```
   aws ec2 delete-vpc-endpoints --vpc-endpoint-ids {{vpce-1a23b4c5}}
    
   {
       "Unsuccessful": []
   }
   ```

   The empty array `[]` indicates success (there were no unsuccessful requests).

**To terminate your Amazon EC2 instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Choose your Amazon EC2 instance.

1. Choose **Actions**, choose **Instance State**, and then choose **Terminate**.

1. In the confirmation window, choose **Yes, Terminate**.