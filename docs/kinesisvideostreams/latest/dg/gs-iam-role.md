

# Create an IAM permissions policy
<a name="gs-iam-role"></a>

Follow these procedures to create an IAM policy. This permissions policy allows selective access control (a subset of supported operations) for an AWS resource. In this case, the AWS resources are the video streams that you want the Amazon Kinesis Video Streams Edge Agent to stream to. The resources also include the AWS Secrets Manager secrets that the Amazon Kinesis Video Streams Edge Agent can retrieve. For more information, see [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

**Create a policy by using the JSON policy editor**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Policies**.

   If this is your first time choosing **Policies**, the **Welcome to Managed Policies** page appears. Choose **Get Started**.

1. At the top of the page, choose **Create policy**.

1. In the **Policy editor** section, choose the **JSON** option.

1. Enter the following JSON policy document:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "cloudwatch:PutMetricData",
                   "kinesisvideo:ListStreams",
                   "iot:Connect",
                   "iot:Publish",
                   "iot:Subscribe",
                   "iot:Receive"
               ],
               "Resource": [
                   "*"
               ] 
           },
           {
               "Effect": "Allow",
               "Action": [
                   "kinesisvideo:DescribeStream",
                   "kinesisvideo:PutMedia",
                   "kinesisvideo:TagStream",
                   "kinesisvideo:GetDataEndpoint"
               ],
                "Resource": [ 
                   "{{arn:aws:kinesisvideo:*:*:stream/streamName1/*}}",
                   "{{arn:aws:kinesisvideo:*:*:stream/streamName2/*}}"
               ]
           },
           {
               "Effect": "Allow",
               "Action": "secretsmanager:GetSecretValue",
               "Resource": [
                    "{{arn:aws:secretsmanager:*:*:secret:*}}",
                    "{{arn:aws:secretsmanager:*:*:secret:*}}"
               ]
           }
       ]
   }
   ```

------
**Note**  
Replace `arn:aws:kinesisvideo:*:*:stream/streamName1/*` and `arn:aws:kinesisvideo:*:*:stream/streamName2/*` with the ARNs for the video streams, and replace `arn:aws:secretsmanager:*:*:secret:*` with the ARNs that contain the MediaURI secrets that you created in [Create resources for your IP camera RTSP URLs](gs-create-resources-standalone.md). Use the ARNs for the secrets that you want the Amazon Kinesis Video Streams Edge Agent to access.

1. Choose **Next**.
**Note**  
You can switch between the **Visual** and **JSON** editor options anytime. However, if you make changes or choose **Next** in the **Visual** editor, IAM might restructure your policy to optimize it for the visual editor. For more information, see [Policy restructuring](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_policies.html#troubleshoot_viseditor-restructure) in the IAM User Guide.

1. On the **Review and create** page, enter a **Policy name** and an optional **Description** for the policy that you are creating. Review **Permissions defined in this policy** to see the permissions that are granted by your policy. 

1. Choose **Create policy** to save your new policy.