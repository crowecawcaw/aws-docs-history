

# Import/export permissions
<a name="import-export-permissions"></a>

 Neptune Analytics Export writes data into customer-owned Amazon S3 buckets. To do that, you to provide an IAM role and AWS KMS policy to securely and successfully export data to the desired Amazon S3 destination. These two arguments are passed in via the following parameters in the `StartExportTask` API. 
+  `--destination` - The target Amazon S3 destination that Neptune Analytics will export data into. 
+  `--role-arn` will be assumed by the Neptune Analytics service, to upload data to your Amazon S3 bucket. The request will fail if this argument is missing. 
+  `--kms-key-identifier` is required to encrypt your data into your Amazon S3 bucket. The request will fail if the argument is missing. 

## Create and configure IAM role and AWS KMS key
<a name="create-iam-and-kms"></a>

1.  Go to the AWS IAM service console. 

1.  Create an inline policy, it should have at least the following permissions: 

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "VisualEditor0",
         "Effect": "Allow",
         "Action": [
           "kms:DescribeKey",
           "kms:Decrypt",
           "kms:GenerateDataKey"
         ],
         "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{key-id}}"
       },
       {
         "Sid": "VisualEditor1",
         "Effect": "Allow",
         "Action": [
           "s3:PutObject",
           "s3:GetObject",
           "s3:ListBucket"
         ],
         "Resource": [
           "arn:aws:s3:::{{amzn-s3-demo-bucket}}/",
           "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
         ]
       }
     ]
   }
   ```

------
   +  `kms:Decrypt`: To list and read the Amazon S3 objects when exporting data. The Neptune Analytics service requires this information to avoid duplicates during exports. 
   +  `kms:GenerateDataKey`: To encrypt the Amazon S3 objects when writing to the Amazon S3 location. 
   +  `kms:DescribeKey`: To validate if the customer-provided IAM role has permissions to access the AWS KMS key. 
   +  `s3:PutObject`: To put objects into the Amazon S3 location. 
   +  `s3:GetObject`: To get Amazon S3 objects for deduplication checks. 
   +  `s3:ListBucket`: To list Amazon S3 objects for deduplication checks. 

1.  Create an IAM role (choose custom trust policy), configure it's trust policy so that Neptune Analytics is able to assume this role: 

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "Statement1",
               "Effect": "Allow",
               "Principal": {
                   "Service": [
                       "neptune-graph.amazonaws.com"
                   ]
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

------

    Use the policy created in step 2. 

1.  Go to the AWS KMS console page. 

1.  Create a new AWS KMS key policy, add following key policy. The following policy can be optional, if the key policy already grants root account the following actions. Root account ARN is like `"AWS": "arn:aws:iam::[YOUR_ACCOUNT]:root"`. 

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Id": "key-consolepolicy-3",
       "Statement": [
           {
               "Sid": "Enable IAM User Permissions",
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "# Use the Above IAM Role"
                   ]
               },
               "Action": [
                   "kms:DescribeKey"
               ],
               "Resource": "*"
           },
           {
               "Sid": "Enable IAM User Permissions",
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "# Use the Above IAM Role"
                   ]
               },
               "Action": [
                   "kms:Decrypt",
                   "kms:GenerateDataKey"
               ],
               "Condition": {
                   "ForAllValues:StringEquals": {
                       "kms:EncryptionContextKeys": [
                           "aws:neptune-graph:graphId",
                           "aws:neptune-graph:graphExportId"
                       ]
                   }
               },
               "Resource": "*"
           }
       ]
   }
   ```

------

1.  Go to the Amazon S3 bucket and choose the **Properties** page. 

1.  Navigate to the **Default encryption** section and choose **Edit**. 

1.  Input the AWS KMS key created in step 5, and choose **Save**. 