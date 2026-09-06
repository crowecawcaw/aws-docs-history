

# Cross account bucket access
<a name="S3-buckets-cross-account-access"></a>

RES has the ability to mount buckets from other AWS accounts, provided these buckets have the right permissions. In the following scenario, a RES environment in Account A wants to mount an S3 bucket in Account B.

**Step 1: Create an IAM Role in the account that RES is deployed in *(this will be referred to as Account A)*:**

1. Sign in to the AWS Management Console for the RES account that needs access to the S3 bucket (Account A).

1. Open the IAM Console:

   1. Navigate to the IAM dashboard.

   1. In the navigation pane, choose **Policies**.

1. Create a Policy: 

   1. Choose **Create policy**.

   1. Select the **JSON** tab.

   1. Paste the following JSON policy (replace `{{amzn-s3-demo-bucket}}` with the name of the S3 bucket located in Account B): 

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
                      "s3:GetObject",
                      "s3:PutObject",
                      "s3:ListBucket",
                      "s3:DeleteObject",
                      "s3:AbortMultipartUpload"
                  ],
                  "Resource": [
                      "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                      "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
                  ]
              }
          ]
      }
      ```

------

   1. Choose **Next**.

1. Review and create the policy: 

   1. Provide a name for the policy (for example, "S3AccessPolicy").

   1. Add an optional description to explain the purpose of the policy.

   1. Review the policy and choose **Create policy**.

1. Open the IAM Console:

   1. Navigate to the IAM dashboard.

   1. In the navigation pane, choose **Roles**.

1. Create a Role:

   1. Choose **Create role**.

   1. Choose **Custom trust policy** as the type of trusted entity.

   1. Paste the following JSON policy (replace `{{111122223333}}` with the actual account ID of Account A, and `{{{RES_ENVIRONMENT_NAME}}}` with the environment name of the RES deployment: 

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "AWS": "arn:aws:iam::{{111122223333}}:role/{{<ENVIRONMENT_NAME>}}-vdc-custom-credential-broker-lambda-role"
                  },
                  "Action": "sts:AssumeRole"
              }
          ]
      }
      ```

------

   1. Choose **Next**.

1. Attach Permissions Policies:

   1. Search for and select the policy you created earlier.

   1. Choose **Next**.

1. Tag, Review, and Create the Role: 

   1. Enter a role name (for example, "S3AccessRole").

   1. Under Step 3, choose **Add Tag**, then enter the following key and value:
      + Key: `res:Resource` 
      + Value: `s3-bucket-iam-role` 

   1. Review the role and choose **Create role**.

1. Use the IAM Role in RES:

   1. Copy the IAM role ARN that you created. 

   1. Sign in to the RES console.

   1. In the left navigation pane, choose **S3 Bucket**. 

   1. Choose **Add Bucket** and fill out the form with the cross-account S3 bucket ARN.

   1. Choose the **Advanced settings - optional** dropdown.

   1. Enter the role ARN in the IAM role ARN field.

   1. Choose **Add Bucket**.

**Step 2: Modify the bucket policy in Account B**

1. Sign in to the AWS Management Console for Account B.

1. Open the S3 Console: 

   1. Navigate to the S3 dashboard.

   1. Select the bucket you want to grant access to.

1. Edit the Bucket Policy:

   1. Select the **Permissions** tab and choose **Bucket policy**.

   1. Add the following policy to grant the IAM role from Account A access to the bucket (replace {{111122223333}} with the actual account ID of Account A and {{amzn-s3-demo-bucket}} with the name of the S3 bucket): 

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "AWS": "arn:aws:iam::{{111122223333}}:role/S3AccessRole"
                  },
                  "Action": [
                      "s3:GetObject",
                      "s3:PutObject",
                      "s3:ListBucket",
                      "s3:DeleteObject",
                      "s3:AbortMultipartUpload"
                  ],
                  "Resource": [
                      "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                      "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
                  ]
              }
          ]
      }
      ```

------

   1. Choose **Save**.