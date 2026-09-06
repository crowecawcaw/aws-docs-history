

# Prerequisites to configure Trusted Identity Propagation with EMR on EC2
<a name="emr-trusted-identity-prerequisites"></a>

The prerequisites show you how to configure using either the AWS Console or the AWS CLI to create an IAM Identity Center instance and create users with the goal of setting up trusted identity propagation. Then you set up AWS Lake Formation to manage permissions for your AWS Glue Data Catalog objects and Amazon Simple Storage Service data locations. Each section goes into detail, including showing how to register Amazon Simple Storage Service locations for use with EMR and IAM Identity Center.

All prerequisites can be set up using either the AWS Console or AWS CLI. This tutorial provides a CloudFront template, as well as AWS Console setup steps.

**Important**  
Runtime role-based access control and Amazon EMR integration with AWS IAM Identity Center (trusted identity propagation) do not support High Availability (HA) clusters.

## Creating an Identity Center instance and syncing users
<a name="emr-trusted-identity-create-idc-instance"></a>

In this tutorial, you create an IAM Identity Center instance and create users. This is optional if you have existing users. Although this tutorial demonstrates manual user creation, in a more typical use case you sync users to Identity Center from an external identity provider, such as Okta or Azure Entra ID. For information about syncing with external providers, see [IAM Identity Center identity source tutorials](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html) in the *AWS IAM Identity Center User Guide*.

**To create an identity center instance and users**

1. Log in to your AWS Management Console with administrator privileges.

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. **Enable IAM Identity Center**. The first step is to enable an instance of IAM Identity Center in the [supported Region](https://docs.aws.amazon.com/singlesignon/latest/userguide/regions.html). IAM Identity Center is region bound; all the data that you configure in IAM Identity Center is stored in the Region where you initially configure it. In the navigation bar at the top, you can see the current AWS Region — for example, US East (N. Virginia). You can use the selected Region or optionally select a Region that is closer to you.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-iam-id-center-enable.png)

1. From the IAM Identity Center page, choose **Enable in only this AWS account**. You also have the option to enable IAM Identity Center with AWS Organizations, but for this tutorial, use the single account option.

1. Create groups and users:

   1. In the navigation pane, choose **Groups** and then choose **Create group**.

   1. Enter a group name (for example, DataAnalysts or DataEngineers) and description, and then choose **Create group**.

   1. In the navigation pane, choose **Users** and then choose **Add user**.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-security-center-users.png)

   1. Specify the following user details:
      + Username
      + Password (for this tutorial, choose the one-time password option)
      + Email address
      + First name
      + Last name

      Choose **Next**.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-security-center-user-details.png)

   1. (Optional) On the **Add user to groups** page, select the group that you created, and then choose **Next**.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-add-user-to-group.png)

   1. Review the settings and choose **Add user**.

   1. If you chose to generate a one-time password, save the login information that appears. You can copy and share the sign-in instructions for the AWS access portal with the user, or email the instructions. This is the only time you can view and copy this password.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-generate-one-time.png)

   1. The user receives an invitation to access the AWS access portal. Accept the invitation and reset the password.

1. To add more users, repeat the user creation steps.

## Set up Lake Formation
<a name="emr-trusted-identity-lake-formation-setup"></a>

This section shows you how to set up AWS Lake Formation to manage permissions for your AWS Glue Data Catalog objects and Amazon Simple Storage Service data locations. You can find the comprehensive setup instructions in the [Set up Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin) documentation. This tutorial covers the essential setup needed for Amazon EMR with trusted-identity propagation.

1. Lake Formation starts with the **Use only IAM access control** settings enabled for compatibility with existing AWS Glue Data Catalog behavior. Follow these steps to disable those settings to enable fine-grained access control with Lake Formation permissions.
   + In the navigation pane, under **Administration**, choose **Data Catalog Settings**.
   + Clear both check boxes under **Default permissions for newly created databases and table** and proceed with the default for **Cross account version setting**, uncheck **Enhanced auditing** and click on **Save**.
   + Optional: In the navigation pane, under **Administration**, choose **Administrative roles and tasks**. If you see **IAMAllowedPrincipals** group under **Database creators**, select the **IAMAllowedPrincipals** group, and choose **Revoke**. The **Revoke permissions** dialog box appears, showing that **IAMAllowedPrincipals** has the **Create database** permission. Choose **Revoke**.

1. Connect Lake Formation with IAM Identity Center. In the left navigation pane, select **IAM Identity Center integration** and click on **Create** to connect to account instance of IAM Identity Center.

1. In order [to enable Lake Formation for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lf-enable.html) for row, column or cell-level permissions, under **Administration**, choose **Application integration settings**. Then select the checkbox **Allow external engines to filter data in Amazon S3 locations registered with Lake Formation**. Then provide `Amazon EMR` as the value for the session tag configuration, **AuthorizedSessionTagValue**. Lake Formation uses this session tag to authorize callers and provide access to the data lake. Provide your own AWS account ID under **AWS account IDs** field and click **Save**.

![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-app-integration-settings.png)


## Steps to create certificate for EMR cluster security configuration
<a name="emr-trusted-identity-create-certificate-security-config"></a>

In order to launch an Amazon EMR cluster with Trusted Identity Propagation setup, an [Identity Center enabled security configuration is required](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-idc-start.html#emr-idc-start-securityconfig). If you already do not have [certificates for encrypting data in transit](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-encryption-enable.html#emr-encryption-certificates), follow below steps to create a self-signed certificate for this tutorial:

We use [OpenSSL](https://www.openssl.org/) to generate a self-signed X.509 certificate with a 2048-bit RSA private key. The key allows access to the issuer's Amazon EMR cluster instances in the AWS Region being used. For a complete guide on creating and providing a certificate, refer to [Providing certificates for encrypting data in transit with Amazon EMR encryption](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-encryption-enable.html#emr-encryption-certificates).
+ Run the following commands:

  ```
  openssl req -x509 -newkey rsa:2048 -keyout privateKey.pem -out certificateChain.pem -days 365 -nodes -subj '/CN=*.us-east-1.compute.internal'
  cp certificateChain.pem trustedCertificates.pem
  zip -r -X my-certs.zip certificateChain.pem privateKey.pem trustedCertificates.pem
  ```
+ Upload `my-certs.zip` to an Amazon Simple Storage Service location that will be used to create the security configuration. The Amazon EMR service role should have access to the Amazon S3 location. The key allows access to the issuer's Amazon EMR cluster instances in the us-east-1 Region as specified by the `*.us-east-1.compute.internal` domain name as the common name. You can change this to the Region your cluster is in.

## Steps for Lake Formation set up
<a name="emr-trusted-identity-lake-formation-setup-steps"></a>

For the remaining steps, either deploy AWS CloudFormation Stack or follow instructions to perform the setup via AWS console.

### Deploy CloudFormation Stack
<a name="emr-trusted-identity-deploy-cfn-stack"></a>

Download this CloudFormation template [emr-tip.yaml](samples/emr-tip.yaml.zip) and use **Create Stack** on the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/) to create the solution resources. Refer to the following table for a list of important parameters.


**CloudFormation Stack Parameters**  

| Parameter Group | Description | Parameter Name | Expected Value | 
| --- | --- | --- | --- | 
| Choose components to provision | Choose the components you want to be provisioned. | CreateS3AGInstance | Yes/No. If you already have an S3 Access Grants instance, choose No. Otherwise, choose Yes to allow the stack create a new S3 Access Grants instance. The S3 Access Grants can be used to centrally manage access to your raw data that is not yet cataloged to the Data Catalog | 
| Identity Center Configuration | IAM Identity Center parameters | IDCGroup1Id | Group ID corresponding to Group1 from IAM Identity Center. | 
| Identity Center Configuration | IAM Identity Center parameters | IDCGroup2Id (optional) | Group ID corresponding to Group2 from IAM Identity Center. | 
| Identity Center Configuration | IAM Identity Center parameters | IDCGroup3Id (optional) | Group ID corresponding to Group3 from IAM Identity Center. | 
| Identity Center Configuration | IAM Identity Center parameters | IAMIDCInstanceArn | IAM Identity Center instance ARN. You can get this from the Settings section of IAM Identity Center. | 
| EMR Configuration | EMR parameters. Ignore if you chose parameter DeployEMRFlow as No. | SSlCertsS3BucketName | Bucket name where you copied the SSL certificates. Eg if your certs are located at s3://bucket\_name/certs/my-certs.zip then provide value bucket\_name here | 
| EMR Configuration | EMR parameters. Ignore if you chose parameter DeployEMRFlow as No. | SSlCertsPathtoZip | Path to SSL cert zip in your certs s3 bucket. Eg if your certs are located at s3://bucket\_name/certs/my-certs.zip then provide value certs/my-certs.zip here | 

The CloudFormation stack provisions the following resources:
+ A VPC with a public and private subnet.
+ Amazon EMR Studio with IAM Identity Center integration.
+ [Amazon Amazon EMR security configuration with IAM Identity Center integration](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-idc-start.html#emr-idc-start-securityconfig).
+ An Amazon EMR cluster that uses the Amazon EMR security group.
+ Registers the source Amazon Simple Storage Service bucket with AWS Lake Formation.
+ An AWS Glue database named `emr_tip_tutorial` and a table named `customer_parquet` under the database. The table points to the Amazon S3 location governed by Lake Formation.
+ Allows external engines to access data in Amazon S3 locations with full table access. This is required for Amazon EMR integration with Lake Formation for trusted identity propagation.
+ An S3 Access Grants instance.
+ S3 Access Grants for Identity Center Groups to the Amazon S3 bucket input and output prefixes. The user has read access to the input prefix and write access to the output prefix under the bucket.

Note the stack outputs on the CloudFormation console. You use these values in later steps. You can now move to the next tutorial to use identity based authorization to query [Parquet](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-trusted-identity-auth-parquet.html), Iceberg or Delta Lake tables.

### Setting up via the AWS Console
<a name="emr-trusted-identity-aws-console-setup"></a>

#### 1. AWS Lake Formation setup to configure the roles
<a name="lf-role-setup"></a>

To use AWS Lake Formation with Amazon EMR, create a custom role to register Amazon Simple Storage Service locations for your data source. You need to create a new custom role with Amazon S3 access. Do not use the default role, which is explained in more detail at [Setting up AWS Lake Formation with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-lf.html).

Use the following custom trust policy for the Lake Formation location registration role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "lakeformation.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```
+ If you don't already have a test data source location in Amazon S3, go to the [Amazon S3 console](https://console.aws.amazon.com/s3/) and create a new bucket. For example, you can name it `s3://tip-blog-s3-lf-` followed by your AWS account ID.
+ Navigate to the [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/)AWS Identity and Access Management console and create an IAM Role for Lake Formation Location Registration say `LFRole-data-access-permissions-check`. To create an IAM Role:

  1. Go to **Roles** → **Create role**

  1. Select **Custom trust policy** and paste the following trust relationship:

     ```
     {
         "Version": "2012-10-17",		 	 	 
         "Statement": [
             {
                 "Effect": "Allow",
                 "Principal": {
                     "Service": [
                         "lakeformation.amazonaws.com"
                     ]
                 },
                 "Action": "sts:AssumeRole"
             }
         ]
     }
     ```

  1. Attach below policies to your newly created role:
     + The following custom Amazon S3 policy (Replace the demo bucket names with your Amazon S3 bucket names that contain underlying data say `s3://tip-blog-s3-lf-<your_account_id>/`):

       ```
       {
           "Version": "2012-10-17",		 	 	 
           "Statement": [
               {
                   "Effect": "Allow",
                   "Action": [
                       "s3:PutObject",
                       "s3:GetObject",
                       "s3:DeleteObject",
                       "s3:ListBucket"
                   ],
                   "Resource": [
                       "arn:aws:s3:::amzn-s3-demo-bucket1",
                       "arn:aws:s3:::amzn-s3-demo-bucket2/*"
                   ]
               }
           ]
       }
       ```

  1. Open the [AWS Lake Formation console](https://console.aws.amazon.com/lakeformation/).
     + From the left menu open Data lake locations under **Administration** section then **Register location**.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-data-lake-locations.png)
     + Browse the Amazon S3 path you have created
     + Attach IAM role created above `LFRole-data-access` that has read/write access to the chosen Amazon S3 path.
     + Choose **Lake Formation** for Permission mode and click on **Register location**.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-data-lake-register.png)

#### 2. S3 Access Grants setup (Optional)
<a name="emr-trusted-identity-s3-access-grants-setup"></a>

**Note**  
Skip this step if you do not wish to use or test S3 Access grants for access control to raw files on S3. This step is not required for Lake Formation based access controls.

Steps for Amazon Simple Storage Service Access Grants set up. For more information, see [Working with S3 Access Grants instances](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance.html).

##### A. Create an S3 Access Grants instance
<a name="emr-trusted-identity-create-s3-access-grants"></a>

1. Open the Amazon S3 console at [Amazon S3 console](https://console.aws.amazon.com/s3/).

1. Make sure that this is the same AWS Region where your Amazon S3 data is located. You can create one S3 Access Grants instance per AWS Region per account.

1. In the left navigation panel, choose **Access Grants**.

1. On the S3 Access Grants page, choose **Create S3 Access Grants instance**.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-create-access-grants.png)

1. In the **Set up Access Grants instance** wizard, verify that you want to create the instance in the current AWS Region.

1. You can associate the IAM Identity Center instance with your S3 Access Grants instance. To do so, select **Add IAM Identity Center instance in region**. Then enter the IAM Identity Center instance Amazon Resource Name (ARN).

1. Get the Identity Center instance ARN from the IAM Identity Center console under **Settings** as shown in the picture below.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-access-grants-setup.png)

1. To create the S3 Access Grants instance, choose **Next**.

##### B. Register a location
<a name="emr-trusted-identity-register-location"></a>

1. Specify the Amazon S3 bucket location Scope.

1. Add an IAM role to allow S3 access grants to access your specified location scope. You can use the existing IAM roles if you already have one or create an IAM role adding all the necessary permissions specified in [Register locations for S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location-register.html). Specifically, make sure that this role grants S3 Access Grants the permissions `sts:AssumeRole` and `sts:SetSourceIdentity`.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-register-s3-bucket.png)

##### C. Create grants
<a name="emr-trusted-identity-create-grants"></a>

After you register the location in your S3 Access Grants instance, you can create an access grant.

1. On the create grants page add the Subprefix you want to provide access to specific users or groups.

1. Under **Permissions and access**, select the **Permission level**, either **Read**, **Write**, or both.

1. Then choose the **Grantee type**. You can choose **Directory identity** from IAM Identity Center. Choose **User** or **Group** under the Directory identity type and provide IAM Identity center group ID. For this tutorial we choose **Group**.

1. You can get the Identity center group Id from the IAM Identity Center console. Open IAM Identity Center, from the left panel choose **Groups** and click the general information drop down. Copy the Group ID and paste to S3 Access grant console.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-idc-persona.png)

Then choose **Create Grant**.

![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-create-grant.png)


#### 3. EMR Security Configuration
<a name="emr-trusted-identity-security-config"></a>

##### Steps EMR Security Configuration set up
<a name="emr-trusted-identity-steps-security-config"></a>
+ Create an EMR security configuration with IAM Identity Center enabled from the AWS Command Line Interface with the following code:

  ```
  aws emr create-security-configuration --name "IdentityCenterConfiguration-with-lf-tip" --region "us-west-2" --endpoint-url https://elasticmapreduce.us-east-1.amazonaws.com --security-configuration '{
          "AuthenticationConfiguration":{
              "IdentityCenterConfiguration":{
                  "EnableIdentityCenter":true,
                  "IdentityCenterApplicationAssignmentRequired":false,
                  "IdentityCenterInstanceARN": "arn:aws:sso:::instance/ssoins-xxxxxxxxxxxx",
                  "IAMRoleForEMRIdentityCenterApplicationARN": "arn:aws:iam::1xxxxxxxxx0:role/emr-idc-application"
              }
          },
          "AuthorizationConfiguration": {
              "LakeFormationConfiguration": {
                  "EnableLakeFormation": true
              }
          },
          "EncryptionConfiguration": {
              "EnableInTransitEncryption": true,
              "EnableAtRestEncryption": false,
              "InTransitEncryptionConfiguration": {
                  "TLSCertificateConfiguration": {
                      "CertificateProviderType": "PEM",
                      "S3Object": "s3://<amzn-s3-demo-bucket1>/path/my-certs.zip"
                  }
              }
          }
      }'
  ```  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-configure-authen-author.png)

#### 4. EMR Roles Setup
<a name="emr-trusted-identity-emr-roles-setup"></a>

Create below IAM roles for EMR request access to AWS IAM Identity Center on your behalf:

##### EMR Cluster Service role
<a name="emr-trusted-identity-emr-cluster-service-role"></a>

**To create an IAM Role:**

1. Go to **Roles** → **Create role** → select **AWS service** for trusted entity type and choose **EMR** under Use case. This will add [AmazonEMRServicePolicy\_v2](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEMRServicePolicy_v2.html) managed policy. Click **Next**.

1. Give a role name *tiptutorial-EMREC2ServiceRole* and click **Create**.

1. Add the below `ServiceRoleDefaultPolicy` as an inline policy:

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Condition": {
                   "StringEquals": {
                       "iam:PassedToService": "ec2.amazonaws.com"
                   }
               },
               "Action": "iam:PassRole",
               "Resource": "arn:aws:iam::xxxxxxxxxxxx:role/tiptutorial-EMREC2InstanceRole-AoRUJtqGunxx",
               "Effect": "Allow"
           }
       ]
   }
   ```

##### EMR Cluster Instance Profile role
<a name="emr-trusted-identity-emr-cluster-instance-profile"></a>

Create an Instance Profile role with the name example *tiptutorial-EMREC2InstanceRole* with `AmazonSSMManagedInstanceCore` AWS managed policy and add the following inline policies:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::emr-tip-integration/certs/my-certs.zip"
            ],
            "Effect": "Allow"
        }
    ]
}
```

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::tip-blog-s3-emrtorage-workspace-xxxxxxxxxxxx/logs/emr-ec2/*"
            ],
            "Effect": "Allow"
        }
    ]
}
```

##### EMR Studio service role
<a name="emr-trusted-identity-emr-studio-service-role"></a>

Create an EMR Studio Service role to let Studio access your AWS resources. Give it a name say *AmazonEMRStudio\_ServiceRole*:

1. Attach the Trust policy:

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "elasticmapreduce.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

1. Attach the following inline policies:

   **AllowEC2ReadOnlyActions**

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Action": [
                   "ec2:DescribeSecurityGroups",
                   "ec2:DescribeNetworkInterfaces",
                   "ec2:DescribeTags",
                   "ec2:DescribeInstances",
                   "ec2:DescribeSubnets",
                   "ec2:DescribeVpcs"
               ],
               "Resource": [
                   "*"
               ],
               "Effect": "Allow"
           }
       ]
   }
   ```

   **EMRSparkAI-Studio-Service-Policy**

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Action": [
                   "elasticmapreduce:ListInstances",
                   "elasticmapreduce:DescribeCluster",
                   "elasticmapreduce:ListSteps"
               ],
               "Resource": "*",
               "Effect": "Allow",
               "Sid": "AllowEMRReadOnlyActions"
           },
           {
               "Condition": {
                   "StringEquals": {
                       "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
                   }
               },
               "Action": [
                   "ec2:CreateNetworkInterfacePermission",
                   "ec2:DeleteNetworkInterface"
               ],
               "Resource": [
                   "arn:aws:ec2:*:*:network-interface/*"
               ],
               "Effect": "Allow",
               "Sid": "AllowEC2ENIActionsWithEMRTags"
           },
           {
               "Action": [
                   "ec2:ModifyNetworkInterfaceAttribute"
               ],
               "Resource": [
                   "arn:aws:ec2:*:*:instance/*",
                   "arn:aws:ec2:*:*:network-interface/*",
                   "arn:aws:ec2:*:*:security-group/*"
               ],
               "Effect": "Allow",
               "Sid": "AllowEC2ENIAttributeAction"
           },
           {
               "Condition": {
                   "StringEquals": {
                       "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
                   }
               },
               "Action": [
                   "ec2:AuthorizeSecurityGroupEgress",
                   "ec2:AuthorizeSecurityGroupIngress",
                   "ec2:RevokeSecurityGroupEgress",
                   "ec2:RevokeSecurityGroupIngress",
                   "ec2:DeleteNetworkInterfacePermission"
               ],
               "Resource": "*",
               "Effect": "Allow",
               "Sid": "AllowEC2SecurityGroupActionsWithEMRTags"
           },
           {
               "Condition": {
                   "StringEquals": {
                       "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true"
                   }
               },
               "Action": [
                   "ec2:CreateSecurityGroup"
               ],
               "Resource": [
                   "arn:aws:ec2:*:*:security-group/*"
               ],
               "Effect": "Allow",
               "Sid": "AllowDefaultEC2SecurityGroupsCreationWithEMRTags"
           },
           {
               "Condition": {
                   "StringEquals": {
                       "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
                   }
               },
               "Action": [
                   "ec2:CreateSecurityGroup"
               ],
               "Resource": [
                   "arn:aws:ec2:*:*:vpc/*"
               ],
               "Effect": "Allow",
               "Sid": "AllowDefaultEC2SecurityGroupsCreationInVPCWithEMRTags"
           },
           {
               "Condition": {
                   "StringEquals": {
                       "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true",
                       "ec2:CreateAction": "CreateSecurityGroup"
                   }
               },
               "Action": [
                   "ec2:CreateTags"
               ],
               "Resource": "arn:aws:ec2:*:*:security-group/*",
               "Effect": "Allow",
               "Sid": "AllowAddingEMRTagsDuringDefaultSecurityGroupCreation"
           },
           {
               "Condition": {
                   "StringEquals": {
                       "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true"
                   }
               },
               "Action": [
                   "ec2:CreateNetworkInterface"
               ],
               "Resource": [
                   "arn:aws:ec2:*:*:network-interface/*"
               ],
               "Effect": "Allow",
               "Sid": "AllowEC2ENICreationWithEMRTags"
           },
           {
               "Condition": {
                   "StringEquals": {
                       "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
                   }
               },
               "Action": [
                   "ec2:CreateNetworkInterface"
               ],
               "Resource": [
                   "arn:aws:ec2:*:*:subnet/*",
                   "arn:aws:ec2:*:*:security-group/*"
               ],
               "Effect": "Allow",
               "Sid": "AllowEC2ENICreationInSubnetAndSecurityGroupWithEMRTags"
           },
           {
               "Condition": {
                   "StringEquals": {
                       "ec2:CreateAction": "CreateNetworkInterface"
                   }
               },
               "Action": [
                   "ec2:CreateTags"
               ],
               "Resource": "arn:aws:ec2:*:*:network-interface/*",
               "Effect": "Allow",
               "Sid": "AllowAddingTagsDuringEC2ENICreation"
           },
           {
               "Action": [
                   "ec2:DescribeSecurityGroups",
                   "ec2:DescribeNetworkInterfaces",
                   "ec2:DescribeTags",
                   "ec2:DescribeInstances",
                   "ec2:DescribeSubnets",
                   "ec2:DescribeVpcs"
               ],
               "Resource": "*",
               "Effect": "Allow",
               "Sid": "AllowEC2ReadOnlyActions"
           },
           {
               "Condition": {
                   "StringEquals": {
                       "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
                   }
               },
               "Action": [
                   "secretsmanager:GetSecretValue"
               ],
               "Resource": "arn:aws:secretsmanager:*:*:secret:*",
               "Effect": "Allow",
               "Sid": "AllowSecretsManagerReadOnlyActionsWithEMRTags"
           },
           {
               "Action": [
                   "s3:PutObject",
                   "s3:GetObject",
                   "s3:GetEncryptionConfiguration",
                   "s3:ListBucket",
                   "s3:DeleteObject"
               ],
               "Resource": "arn:aws:s3:::*",
               "Effect": "Allow"
           }
       ]
   }
   ```

   **TIpStudioWorkspaceAccessPolicy**

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Action": [
                   "s3:GetObject",
                   "s3:ListBucket",
                   "s3:PutObject"
               ],
               "Resource": [
                   "arn:aws:s3:::tip-blog-s3-emrtorage-workspace-xxxxxxxxxxxx/*",
                   "arn:aws:s3:::tip-blog-s3-emrtorage-workspace-xxxxxxxxxxxx"
               ],
               "Effect": "Allow"
           }
       ]
   }
   ```

##### EMR Studio User role
<a name="emr-trusted-identity-emr-studio-user-role"></a>

Create an EMR Studio Userrole with the name example *AmazonEMRStudio\_ServiceRole* and attach the following inline policies:
+ TIPBlog-IDC-TrustedIdFed-Policy

  ```
  {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Action": [
                  "sso-oauth:CreateTokenWithIAM"
              ],
              "Resource": [
                  "*"
              ],
              "Effect": "Allow"
          },
          {
              "Action": [
                  "glue:CreateDatabase",
                  "glue:DeleteDatabase",
                  "glue:GetDatabase",
                  "glue:GetDatabases",
                  "glue:UpdateDatabase",
                  "glue:CreateTable",
                  "glue:DeleteTable",
                  "glue:BatchDeleteTable",
                  "glue:UpdateTable",
                  "glue:GetTable",
                  "glue:GetTables",
                  "glue:BatchCreatePartition",
                  "glue:CreatePartition",
                  "glue:DeletePartition",
                  "glue:BatchDeletePartition",
                  "glue:UpdatePartition",
                  "glue:GetPartition",
                  "glue:GetPartitions",
                  "glue:BatchGetPartition",
                  "lakeformation:GetDataAccess"
              ],
              "Resource": [
                  "*"
              ],
              "Effect": "Allow"
          },
          {
              "Action": [
                  "s3:GetDataAccess",
                  "s3:GetAccessGrantsInstanceForPrefix"
              ],
              "Resource": [
                  "*"
              ],
              "Effect": "Allow"
          },
          {
              "Action": [
                  "elasticmapreduce:ListInstances",
                  "elasticmapreduce:ListSteps",
                  "elasticmapreduce:DescribeCluster",
                  "elasticmapreduce:ListStudios",
                  "elasticmapreduce:ListEditors",
                  "elasticmapreduce:DescribeEditor",
                  "elasticmapreduce:AttachEditor",
                  "elasticmapreduce:CreateEditor",
                  "elasticmapreduce:DeleteEditor",
                  "elasticmapreduce:DetachEditor",
                  "elasticmapreduce:OpenEditorInConsole",
                  "elasticmapreduce:StartEditor",
                  "elasticmapreduce:StopEditor",
                  "elasticmapreduce:UpdateEditor",
                  "elasticmapreduce:ListClusters",
                  "elasticmapreduce:GetClusterSessionCredentials"
              ],
              "Resource": [
                  "*"
              ],
              "Effect": "Allow"
          },
          {
              "Action": [
                  "s3:PutObject",
                  "s3:GetObject",
                  "s3:GetEncryptionConfiguration",
                  "s3:ListBucket",
                  "s3:DeleteObject"
              ],
              "Resource": [
                  "arn:aws:s3:::emr-tip-integration-ice*"
              ],
              "Effect": "Allow"
          }
      ]
  }
  ```
+ TIPBlog-rs-iam-pass-role

  ```
  {
    "Version": "2012-10-17",		 	 	 
    "Statement": [
    {
      "Action": [
      "iam:PassRole"
      ],
      "Resource": "arn:aws:iam::448049786777:role/AmazonEMRStudio_ServiceRole_tipblog_xxxxxxxxxxxx",
      "Effect": "Allow"
    }
   ]
  }
  ```

#### 5. EMR Studio Set up
<a name="emr-trusted-identity-emr-studio-setup"></a>

##### Setup trusted identity enabled EMR Studio
<a name="emr-trusted-identity-create-emr-studio"></a>

**To create EMR Studio:**

1. Choose **Studio** from the left panel and click **Create studio**.

1. Choose **Custom** for setup options.

1. Provide Studio name and select existing location for S3 location for workspace storage.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-studio-settings.png)

1. Choose **IAM Identity Center** as Authentication method and attach the IAM user role. Select **Trusted identity propagation** to grant access for users who make requests to applications that are connected through Identity Center. Make sure the IAM role has the S3 access permission policy attached.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-studio-settings-authentication.png)

1. For Networking and security configuration, select VPC and subnets for your Studio to use when communicating with EMR clusters. Leave the defaults for the remaining sections.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-vpc-net.png)

1. Choose **Create Studio**.

##### Assign EMR Studio Users and Groups
<a name="emr-trusted-identity-assign-users-groups"></a>

1. Open your EMR studio.

1. To assign Identity Center users or groups to the studio as per your requirement, click **Assigned groups**.

1. Enter group names in the search bar, select the desired groups, then click **Assign**.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-assign-groups.png)