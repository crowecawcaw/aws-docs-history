

# Creating a workflow job role for AWS Entity Resolution
<a name="create-workflow-job-role"></a>

AWS Entity Resolution uses a *workflow job role* to run a workflow. You can create this role using the console if you have the necessary IAM permissions. If you don't have `CreateRole` permissions, ask your administrator to create the role. 

**To create a workflow job role for AWS Entity Resolution**

1. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/) with your administrator account.

1. Under **Access management**, choose **Roles**.

   You can use **Roles** to create short-term credentials, which is recommended for increased security. You can also choose **Users** to create long-term credentials.

1. Choose **Create role**.

1. In the **Create role** wizard, for **Trusted entity type**, choose **Custom trust policy**.

1. Copy and paste the following custom trust policy into the JSON editor.

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
                   "Service": [
                       "entityresolution.amazonaws.com"
                   ]
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

------

1. Choose **Next**.

1. For **Add permissions**, choose **Create Policy**.

   A new tab appears.

   1. Copy and paste the following policy into the JSON editor.
**Note**  
The following example policy supports the permissions needed to read corresponding data resources like Amazon S3 and AWS Glue. However, you might need to modify this policy depending on how you've set up your data sources.  
You can use AWS Glue resources and underlying Amazon S3 resources from any Region in the AWS commercial partition where AWS Glue is supported – they don't need to be in the same Region as AWS Entity Resolution.  
You don't need to grant AWS KMS permissions if your data sources aren't encrypted or decrypted. 

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
                      "s3:ListBucket",
                      "s3:GetBucketLocation"
                  ],
                  "Resource": [
                      "arn:aws:s3:::{{{{input-buckets}}}}",
                      "arn:aws:s3:::{{{{input-buckets}}}}/*"
                  ],
                  "Condition": {
                      "StringEquals": {
                          "s3:ResourceAccount": [
                              "{{444455556666}}"
                          ]
                      }
                  }
              },
              {
                  "Effect": "Allow",
                  "Action": [
                      "s3:PutObject",
                      "s3:ListBucket",
                      "s3:GetBucketLocation"
                  ],
                  "Resource": [
                      "arn:aws:s3:::{{{{output-bucket}}}}",
                      "arn:aws:s3:::{{{{output-bucket}}}}/*"
                  ],
                  "Condition": {
                      "StringEquals": {
                          "s3:ResourceAccount": [
                              "{{444455556666}}"
                          ]
                      }
                  }
              },
              {
                  "Effect": "Allow",
                  "Action": [
                      "glue:GetDatabase",
                      "glue:GetTable",
                      "glue:GetPartition",
                      "glue:GetPartitions",
                      "glue:GetSchema",
                      "glue:GetSchemaVersion",
                      "glue:BatchGetPartition"
                  ],
                  "Resource": [
                      "arn:aws:glue:{{us-east-1}}:{{444455556666}}:database/{{input-databases}}",
                      "arn:aws:glue:{{us-east-1}}:{{444455556666}}:table/{{input-database}}/{{input-tables}}",
                      "arn:aws:glue:{{us-east-1}}:{{444455556666}}:catalog"
                  ]
              }
          ]
      }
      ```

------

      Replace each {{{{user input placeholder}}}} with your own information.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-workflow-job-role.html)

   1. (Optional) If the input Amazon S3 bucket is encrypted using the customer’s KMS key, add the following:

      ```
              {
                  "Effect": "Allow",
                  "Action": [
                      "kms:Decrypt"
                  ],
                  "Resource": [
                      "arn:aws:kms:{{{{aws-region}}}}:{{{{&ExampleAWSAccountNo1;}}}}:key/{{{{inputKeys}}}}"
                  ]
              }
      ```

      Replace each {{{{user input placeholder}}}} with your own information.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-workflow-job-role.html)

   1. (Optional) If the data being written into the output Amazon S3 bucket needs to be encrypted, add the following:

      ```
              {
                  "Effect": "Allow",
                  "Action": [
                      "kms:GenerateDataKey",
                      "kms:Encrypt"
                  ],
                  "Resource": [
                      "arn:aws:kms:{{{{aws-region}}}}:{{{{&ExampleAWSAccountNo1;}}}}:key/{{{{outputKeys}}}}"
                  ]
              }
      ```

      Replace each {{{{user input placeholder}}}} with your own information.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-workflow-job-role.html)

   1. (Optional) If you have a subscription with a provider service through AWS Data Exchange, and want to use an existing role for a provider service-based workflow, add the following:

      ```
              {
                  "Effect": "Allow",
                  "Sid": "DataExchangePermissions",
                  "Action": "dataexchange:SendApiAsset",
                  "Resource": [
                      "arn:aws:dataexchange:{{{{aws-region}}}}::data-sets/{{{{datasetId}}}}/revisions/{{{{revisionId}}}}/assets/{{{{assetId}}}}"
                  ]
              }
      ```

      Replace each {{{{user input placeholder}}}} with your own information.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-workflow-job-role.html)

1. Go back to your original tab and under **Add permissions**, enter the name of the policy that you just created. (You might need to reload the page.)

1. Select the check box next to the name of the policy that you created, and then choose **Next**.

1. For **Name, review, and create**, enter the **Role name** and **Description**.
**Note**  
The **Role name** must match the pattern in the `passRole` permissions granted to the member who can pass the `workflow job role` to create a matching workflow.  
For example, if you're using the `AWSEntityResolutionConsoleFullAccess` managed policy, remember to include `entityresolution` into your role name.

   1. Review **Select trusted entities**, and edit if necessary.

   1. Review the permissions in **Add permissions**, and edit if necessary.

   1. Review the **Tags**, and add tags if necessary.

   1. Choose **Create role**.

The workflow job role for AWS Entity Resolution has been created.