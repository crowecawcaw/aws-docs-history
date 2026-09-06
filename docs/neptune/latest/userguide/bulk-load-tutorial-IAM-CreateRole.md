

# Creating an IAM role to allow Amazon Neptune to access Amazon S3 resources
<a name="bulk-load-tutorial-IAM-CreateRole"></a>

Use the `AmazonS3ReadOnlyAccess` managed IAM policy to create a new IAM role that will allow Amazon Neptune access to Amazon S3 resources.

**To create a new IAM role that allows Neptune access to Amazon S3**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. Under **AWS service**, choose **S3**.

1. Choose **Next: Permissions**.

1. Use the filter box to filter by the term **S3** and check the box next to **AmazonS3ReadOnlyAccess**.
**Note**  
This policy grants `s3:Get*` and `s3:List*` permissions to all buckets. Later steps restrict access to the role using the trust policy.  
The loader only requires `s3:Get*` and `s3:List*` permissions to the bucket you are loading from, so you can also restrict these permissions by the Amazon S3 resource.  
If your S3 bucket is encrypted, you need to add `kms:Decrypt` permissions

1. Choose **Next: Review**.

1. Set **Role Name** to a name for your IAM role, for example: `NeptuneLoadFromS3`. You can also add an optional **Role Description** value, such as "Allows Neptune to access Amazon S3 resources on your behalf."

1. Choose **Create Role**.

1. In the navigation pane, choose **Roles**.

1. In the **Search** field, enter the name of the role you created, and choose the role when it appears in the list.

1. On the **Trust Relationships** tab, choose **Edit trust relationship**.

1. In the text field, paste the following trust policy.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "",
         "Effect": "Allow",
         "Principal": {
           "Service": [
             "rds.amazonaws.com"
           ]
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------

1. Choose **Update trust policy**.

1. Complete the steps in [Adding the IAM Role to an Amazon Neptune Cluster](bulk-load-tutorial-IAM-add-role-cluster.md).