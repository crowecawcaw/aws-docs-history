

# Preventing data exfiltration in a private VPC
<a name="S3-buckets-preventing-exfiltration"></a>

To prevent users from exfiltrating data from secure S3 buckets into their own S3 buckets in their account, you can attach a VPC endpoint to secure your private VPC. The following steps show how to create a VPC endpoint for the S3 service that supports access to S3 buckets within your account, as well as any additional accounts that have cross-account buckets. 

1. Open the Amazon VPC Console:

   1. Sign in to the AWS Management Console. 

   1. Open the Amazon VPC console at [ https://console.aws.amazon.com/vpcconsole/](https://console.aws.amazon.com/vpcconsole).

1. Create a VPC Endpoint for S3:

   1. In the left navigation pane, choose **Endpoints**.

   1. Choose **Create Endpoint**.

   1. For **Service category**, ensure that **AWS services** is selected. 

   1. In the **Service Name** field, enter `com.amazonaws.{{<region>}}.s3` (replace `{{<region>}}` with your AWS region) or search for "S3".

   1. Select the S3 service from the list.

1. Configure Endpoint Settings: 

   1. For **VPC**, select the VPC where you want to create the endpoint.

   1. For **Subnets**, select both the private subnets used for the VDI Subnets during deployment.

   1. For **Enable DNS name**, ensure that the option is checked. This allows the private DNS hostname to be resolved to the endpoint network interfaces.

1. Configure the Policy to Restrict Access: 

   1. Under **Policy**, choose **Custom**.

   1. In the policy editor, enter a policy that restricts access to resources within your account or a specific account. Here's an example policy (replace {{amzn-s3-demo-bucket}} with your S3 bucket name and {{111122223333}} and {{444455556666}} with the appropriate AWS account IDs that you want to have access): 
**Note**  
This example policy uses `s3:*` and does not restrict S3 control plane operations such as event notification configuration, replication, or inventory. These operations could allow object metadata (such as bucket names and object keys) to be sent to cross-account destinations. If this is a concern, add explicit Deny statements for the relevant S3 control plane actions in the VPC endpoint policy.

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": "*",
                  "Action": "s3:*",
                  "Resource": [
                      "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                      "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
                  ],
                  "Condition": {
                      "StringEquals": {
                          "aws:PrincipalAccount": [
                              "{{111122223333}}",
                              "{{444455556666}}"
                          ]
                      }
                  }
              }
          ]
      }
      ```

------

1. Create the Endpoint:

   1. Review your settings.

   1. Choose **Create endpoint**.

1. Verify the Endpoint:

   1. Once the endpoint is created, navigate to the **Endpoints** section in the VPC console.

   1. Select the newly created endpoint.

   1. Verify that the **State** is **Available**.

By following these steps, you create a VPC endpoint that allows S3 access that is restricted to resources within your account or a specified account ID.