

# Configure IAM roles for Transfer Family web apps
<a name="webapp-roles"></a>

You will need two roles: one to use as an identity bearer role for your web app, and a second to use for configuring an access grant. An identity bearer role is a role that includes an authenticated user's identity in its sessions. It's used to make requests to S3 Access Grants for data access on behalf of the user.

**Note**  
You can skip the procedure for creating an identity bearer role. For information about having the Transfer Family service create the identity bearer role, see [Create a Transfer Family web app](webapp-configure.md#web-app-create).  
You can skip the procedure for creating an access grants role. In the procedure for creating an access grant, in the step where you register an S3 location, choose **Create new role**. 

**Create an identity bearer role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Roles**, and then **Create role**.

1. Choose **Custom trust policy** and then paste in the following code.

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service":"transfer.amazonaws.com"
               },
               "Action": [
                   "sts:AssumeRole",
                   "sts:SetContext"
               ]
           }
       ]
   }
   ```

1. Choose **Next** and then skip **Add permissions** and select **Next** again.

1. Enter a name, for example `web-app-identity-bearer`.

1. Choose **Create role** to create the identity bearer role.

1. Choose the role that you just created from the list, then in the **Permissions policies** panel, choose **Add permissions** > **Create inline policy**.

1. In the **Policy editor**, select **JSON** and then paste in the following code block.

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "s3:GetDataAccess",
                   "s3:ListCallerAccessGrants",
                   "s3:ListAccessGrantsInstances"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

1. For the policy name, enter `AllowS3AccessGrants`, and then select **Create policy**.

Next, you create the role that S3 Access Grants assumes to vend temporary credentials to the grantee.

**Note**  
If you allow the service to create the identity bearer role for you, that role sets confused deputy protection. Therefore, its code is different from what is displayed here.

**Create an access grants role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Roles**, and then **Create role**. This role should have permission to access your S3 data in the AWS Region.

1. Choose **Custom trust policy**, and then paste in the following code.

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "access-grants.s3.amazonaws.com"
               },
               "Action": [
                   "sts:AssumeRole",
                   "sts:SetContext"
               ]
           }
       ]
   }
   ```

1. Choose **Next** add a minimal policy as described in [Register a location](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location-register.html). While not recommended, you can add the **AmazonS3FullAccess** managed policy, which may be too permissive for your needs.

1. Choose **Next**, and enter a name (for example `access-grants-location`).

1. Choose **Create role** to create the role.

**Note**  
If you allow the service to create the access grants role for you, that role sets confused deputy protection. Therefore, its code is different from what is displayed here.