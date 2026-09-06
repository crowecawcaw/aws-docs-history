

# Editing the trust relationship for an existing IAM role
<a name="edit_trust"></a>

You can assign your existing IAM roles to your Directory Service users and groups. To do this, however, the role must have a trust relationship with Directory Service. When you use Directory Service to create a role using the procedure in [Creating a new IAM role](create_role.md), this trust relationship is automatically set.

**Note**  
You only need to establish this trust relationship for IAM roles that are not created by Directory Service.

**To establish a trust relationship for an existing IAM role to Directory Service**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the IAM console, under **Access management**, choose **Roles**.

   The console displays the roles for your account.

1. Choose the name of the role that you want to modify, and once on the role's page, select the **Trust relationships** tab.

1. Choose **Edit trust policy**.

1. Under **Edit trust policy**, paste the following, and then choose **Update policy**.

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
           "Service": "ds.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------

You can also update this policy document using the AWS CLI. For more information, see [update-trust](https://docs.aws.amazon.com/cli/latest/reference/ds/update-trust.html) in the *AWS CLI Command Reference*.