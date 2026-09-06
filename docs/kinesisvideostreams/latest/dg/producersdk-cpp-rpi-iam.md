

# Create an IAM user with permission to write to Kinesis Video Streams
<a name="producersdk-cpp-rpi-iam"></a>

If you haven't already done so, set up an AWS Identity and Access Management (IAM) user with permissions to write to a Kinesis video stream.

These procedures are meant to help you quickly get started using an AWS access key pair. Devices can use X.509 certificates to connect to AWS IoT. See [Controlling access to Kinesis Video Streams resources using AWS IoT](how-iot.md) for more information about how to configure your device to use certificate-based authentication.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation menu on the left, choose **Users**.

1. To create a new user, choose **Add user**.

1. Provide a descriptive **User name** for the user, such as **kinesis-video-raspberry-pi-producer**.

1. Under **Access type**, choose **Programmatic access**.

1. Choose **Next: Permissions**.

1. Under **Set permissions for kinesis-video-raspberry-pi-producer**, choose **Attach existing policies directly**.

1. Choose **Create policy**. The **Create policy** page opens in a new web browser tab.

1. Choose the **JSON** tab.

1. Copy the following JSON policy and paste it into the text area. This policy gives your user permission to create and write data to Kinesis video streams.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [{
       "Effect": "Allow",
         "Action": [
         "kinesisvideo:DescribeStream",
         "kinesisvideo:CreateStream",
         "kinesisvideo:GetDataEndpoint",
         "kinesisvideo:PutMedia"
       ],
       "Resource": [
         "*"
       ]
     }]
   }
   ```

------

1. Choose **Review policy**.

1. Provide a **Name** for your policy, such as **kinesis-video-stream-write-policy**.

1. Choose **Create policy**.

1. Return to the **Add user** tab in your browser, and choose **Refresh**.

1. In the search box, type the name of the policy you created.

1. Select the check box next to your new policy in the list.

1. Choose **Next: Review**.

1. Choose **Create user**.

1. The console displays the **Access key ID** for your new user. Choose **Show** to display the **Secret access key**. Record these values; they are required when you configure the application.