

# Create the policy
<a name="creating-the-role-v3"></a>

In this tutorial, you will create a policy for configuring shared storage encryption with an AWS KMS key.

**Create a policy.**

1. Go to the IAM Console: [https://console.aws.amazon.com/iam/home](https://console.aws.amazon.com/iam/home).

1. Choose **Policies**.

1. Choose **Create policy**.

1. Choose the **JSON** tab and paste in the following policy. Make sure to replace all occurrences of `{{123456789012}}` with your AWS account ID and the key Amazon Resource Name (ARN) and AWS Region with that of your own.

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
                   "kms:DescribeKey",
                   "kms:ReEncrypt*",
                   "kms:CreateGrant",
                   "kms:Decrypt"
               ],
               "Resource": [
                   "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{abcd1234-ef56-gh78-ij90-abcd1234efgh5678}}"
               ]
           }
       ]
   }
   ```

------

1. For this tutorial, name the policy `ParallelClusterKmsPolicy`, and then choose **Create Policy**.

1. Make a note of the policy ARN. You need it to configure your cluster.