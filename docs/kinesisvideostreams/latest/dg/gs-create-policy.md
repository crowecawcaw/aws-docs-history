

# Create the AWS IoT policy
<a name="gs-create-policy"></a>

Follow these procedures to create an AWS IoT policy that will be attached to the device certificate. This gives permissions to AWS IoT capabilities and allows the assumption of the role alias using the certificate.

With AWS IoT Core policies, you can control access to the AWS IoT Core data plane. The AWS IoT Core data plane consists of operations that you can use to do the following:
+ Connect to the AWS IoT Core message broker
+ Send and receive MQTT messages
+ Get or update a thing's device shadow

For more information, see [AWS IoT Core policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html).

**Use AWS IoT policy editor to create an AWS IoT policy**

1. Sign in to the AWS Management Console and open the AWS IoT Core console at [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/).

1. On the left navigation, select **Security** and then choose **Policies**.

1. Choose **Create policy**.

1. Enter a name for your policy.  
**Example**  

   An example of a policy name is **KvsEdgeAccessIoTPolicy**.

1. (Optional) Add metadata to the policy by attaching tags as key-value pairs.

   For more information about using tags in IAM, see [Tagging your AWS IoT resources](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot.html) in the *AWS IoT Core Developer Guide*. 

1. Choose the **JSON** tab.

1. Paste the following JSON policy document:

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
                   "sts:AssumeRoleWithWebIdentity"
               ],
               "Resource": "arn:aws:iot:us-west-2:123456789012:rolealias/{{your-role-alias}}"
           }
       ]
   }
   ```

------
**Note**  
Replace `your-role-alias-arn` with the ARN of the role alias that you created in [Create the AWS IoT role alias](gs-create-role-alias.md).

1. Choose **Create** to save your work.