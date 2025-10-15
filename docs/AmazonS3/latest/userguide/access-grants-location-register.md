# Register a location

After you [create an Amazon S3 Access Grants
 instance](access-grants-instance-create.md "access-grants-instance-create.md") in an AWS Region in your account, you register an S3 location in that
 instance. An S3 Access Grants location maps the default S3 location (`s3://`), a bucket, or a prefix to an AWS Identity and Access Management (IAM) role. S3 Access Grants assumes this IAM role to vend temporary credentials to the grantee that is accessing that particular location. You must first register at least one location in your S3 Access Grants instance before you can create an access grant. 


###### Recommended use case


We recommend that you register the default location (`s3://`) and map it to an IAM role. The location at the default S3 path (`s3://`) covers access to all of your S3 buckets in
 that AWS Region of your account. When you create an access grant, you can narrow the grant scope to a bucket, a prefix, or an object within the default location. 


###### Complex access-management use cases


More complex access-management use cases might require you to register more than the default location. Some examples of such use cases are:



* Suppose that the `amzn-s3-demo-bucket` is a registered location in your S3 Access Grants instance with an IAM role mapped to it, but this IAM role is denied access to a particular prefix within the bucket. In this case, you can register the prefix that the IAM role does not have access to as a separate location and map that location to a different IAM role with the necessary access.
* Suppose that you want to create grants that restrict access to only the users within a virtual private cloud (VPC) endpoint. In this case, you can register a location for a bucket in which the IAM role restricts access to the VPC endpoint. Later, when a grantee asks S3 Access Grants for credentials, S3 Access Grants assumes the location’s IAM role to vend the temporary credentials. This credential will deny access to the specific bucket unless the caller is within the VPC endpoint. This deny permission is applied in addition to the regular READ, WRITE, or READWRITE permission specified in the grant.
When you register a location, you must also specify the IAM role that S3 Access Grants assumes to vend temporary credentials and to scope the permissions for a specific grant. 

If your use case requires you to register multiple locations in your S3 Access Grants instance, you can register any of the following:



| S3 URI | IAM role | Description |
| --- | --- | --- |
| `s3://` | ``Default-IAM-role`` | The default location, `s3://`, includes all buckets in the
 AWS Region. |
| `s3://``amzn-s3-demo-bucket1``/` | ``IAM-role-For-bucket`` | This location includes all objects in the specified bucket. |
| `s3://``amzn-s3-demo-bucket1``/`prefix-name`` | ``IAM-role-For-prefix`` | This location includes all objects in the bucket with an object key name that starts with this prefix. |

Before you can register a specific bucket or prefix, make sure that you do the following:


* Create one or more buckets that contain the data that you want to grant access to.
 These buckets must be located in the same AWS Region as your S3 Access Grants instance. For more
 information, see [Creating a
 bucket](create-bucket-overview.md "create-bucket-overview.md"). 


Adding a prefix is an optional step. Prefixes are strings at the beginning of an object key name. You can use them to organize objects in your bucket as well as for access management. To add a prefix to a bucket, see [Creating object key
 names](object-keys.md "object-keys.md").
* Create an IAM role that has permission to access your S3 data in the AWS Region. For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html") in the *AWS IAM Identity Center user guide*.
* In the IAM role trust policy, give the S3 Access Grants service (`access-grants.s3.amazonaws.com`) principal access to the IAM role that you created. To do so, you can create a JSON file that contains the
 following statements. To add the trust policy to your account, see [Create a role using custom trust policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html").


*TestRolePolicy.json*



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "TestRolePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "access-grants.s3.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole", 
 "sts:SetSourceIdentity"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333",
 "aws:SourceArn": "arn:aws:s3::111122223333:access-grants/default"
 }
 }
 }
 ]
}`

```





Alternatively, for an IAM Identity Center use case, use the following policy which includes a second statement:
* Create an IAM policy to attach Amazon S3 permissions to the IAM role that you created. See the
 following example `iam-policy.json` file and replace the
 ``user input placeholders`` with your
 own information. 


###### Note



	+ If you use server-side encryption with AWS Key Management Service (AWS KMS) keys to encrypt your data, the
	 following example includes the necessary AWS KMS permissions for the IAM role in the
	 policy. If you do not use this feature, you can remove these permissions from
	 your IAM policy.
	+ You can restrict the IAM role to access S3 data only if the credentials are vended by S3 Access Grants. This example shows you how to add a `Condition` statement for a specific S3 Access Grants instance. To use this `Condition`, replace the S3 Access Grants instance ARN in the `Condition` statement with your S3 Access Grants instance ARN, which has the format: 
	 `arn:aws:s3:`region`:`accountId`:access-grants/default`
*iam-policy.json*



```

{
   "Version":"2012-10-17",		 	 	 
   "Statement": [
       {
         "Sid": "ObjectLevelReadPermissions",
         "Effect":"Allow",
         "Action":[
            "s3:GetObject",
            "s3:GetObjectVersion",
            "s3:GetObjectAcl",
            "s3:GetObjectVersionAcl",
            "s3:ListMultipartUploadParts"
         ],
         "Resource":[ 
            "arn:aws:s3:::*"  
         ],
         "Condition":{
            "StringEquals": { "aws:ResourceAccount": "`accountId`" },
            "ArnEquals": {
                "s3:AccessGrantsInstanceArn": ["arn:aws:s3:`region`:`accountId`:access-grants/default"]
            }
        } 
      },
      {
         "Sid": "ObjectLevelWritePermissions",
         "Effect":"Allow",
         "Action":[
            "s3:PutObject",
            "s3:PutObjectAcl",
            "s3:PutObjectVersionAcl",
            "s3:DeleteObject",
            "s3:DeleteObjectVersion",
            "s3:AbortMultipartUpload"
         ],
         "Resource":[
            "arn:aws:s3:::*"  
         ],
         "Condition":{
            "StringEquals": { "aws:ResourceAccount": "`accountId`" },
            "ArnEquals": {
                "s3:AccessGrantsInstanceArn": ["arn:aws:s3:`AWS Region`:`accountId`:access-grants/default"]
            }
         } 
      },
      {
         "Sid": "BucketLevelReadPermissions",
         "Effect":"Allow",
         "Action":[
            "s3:ListBucket"
         ],
         "Resource":[
            "arn:aws:s3:::*"
         ],
         "Condition":{
            "StringEquals": { "aws:ResourceAccount": "`accountId`" },
            "ArnEquals": {
                "s3:AccessGrantsInstanceArn": ["arn:aws:s3:`AWS Region`:`accountId`:access-grants/default"]
            }
         }     
      },
	  //Optionally add the following section if you use SSE-KMS encryption
      {
         "Sid": "KMSPermissions",
         "Effect":"Allow",
         "Action":[
            "kms:Decrypt",
            "kms:GenerateDataKey"
         ],
         "Resource":[
            "*"
         ]
      }
   ]
}

```
You can register a location in your S3 Access Grants instance by using the Amazon S3 console, the
 AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, or the AWS SDKs.

###### Note


 After you register the first location in your S3 Access Grants instance, your instance still does not have any individual access grants in it. To create an access grant, see [Create grants](access-grants-grant-create.md "access-grants-grant-create.md").
 

Before you can grant access to your S3 data with S3 Access Grants, you must have at least
 one registered location. 

###### To register a location in your S3 Access Grants instance

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Access
 Grants**.
3. On the **S3 Access Grants** page, choose the Region that contains
 the S3 Access Grants instance that you want to work with.


If you're using S3 Access Grants instance for the first time, make sure that you
 have completed [Step 1 -
 create an S3 Access Grants instance](access-grants-instance-create.md "access-grants-instance-create.md") and navigated to **Step
 2** of the **Set up Access Grants instance**
 wizard. If you already have an S3 Access Grants instance, choose **View
 details**, and then from the **Locations**
 tab, choose **Register location**.


	1. For the **Location scope**, choose
	 **Browse S3** or enter the S3 URI path to the
	 location that you want to register. For S3 URI formats, see the
	 [location formats](#location-types "#location-types") table.
	 After you enter a URI, you can choose **View** to
	 browse the location.
	2. For the **IAM role**, choose one of the
	 following: 
	
	
	
	
		* **Choose from existing IAM
		 roles**
		
		
		Choose an IAM role from the dropdown list. After you
		 choose a role, choose **View** to make sure
		 that this role has the necessary permissions to manage the
		 location that you're registering. Specifically, make sure
		 that this role grants S3 Access Grants the permissions
		 `sts:AssumeRole` and
		 `sts:SetSourceIdentity`.
		* **Enter IAM role ARN**
		
		
		Navigate to the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). Copy the Amazon
		 Resource Name (ARN) of the IAM role and paste it in this box.
	3. To finish, choose **Next** or **Register
	 location**.
4. Troubleshooting:



###### Cannot register location



	* The location might already be registered.
	
	
	You might not have the
	 `s3:CreateAccessGrantsLocation`
	 permission to register locations. Contact your account
	 administrator.
To install the AWS CLI, see [Installing the
 AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html") in the *AWS Command Line Interface User Guide*. 

You can register the default location, `s3://`, or a custom location in
 your S3 Access Grants instance. Make sure that you first create an IAM role with principal
 access to the location, and then make sure that you grant S3 Access Grants permission to
 assume this role. 

To use the following example commands, replace the ``user input
 placeholders`` with your own information.

###### Example Create a resource policy

Create a policy that allows S3 Access Grants to assume the IAM role. To do so, you can
 create a JSON file that contains the following statements. To add the resource
 policy to your account, see [Create and attach
 your first customer managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html").

*TestRolePolicy.json*


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "Stmt1234567891011",
 "Action": ["sts:AssumeRole", "sts:SetSourceIdentity"],
 "Effect": "Allow",
 "Principal": {"Service": "access-grants.s3.amazonaws.com"}
 }
 ]
}`

```




###### Example Create the role

Run the following IAM command to create the role.


```
aws iam create-role --role-name `accessGrantsTestRole` \
 --region `us-east-2` \
 --assume-role-policy-document file://`TestRolePolicy.json`

```
Running the `create-role` command returns the policy: 


```
{
    "Role": {
        "Path": "/",
        "RoleName": "accessGrantsTestRole",
        "RoleId": "AROASRDGX4WM4GH55GIDA",
        "Arn": "arn:aws:iam::`111122223333`:role/accessGrantsTestRole",
        "CreateDate": "2023-05-31T18:11:06+00:00",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",		 	 	 
            "Statement": [
                {
                    "Sid": "Stmt1685556427189",
                    "Action": [
                        "sts:AssumeRole",
                        "sts:SetSourceIdentity"
                    ],
                    "Effect": "Allow",
                    "Principal": {
                        "Service":"access-grants.s3.amazonaws.com"
                    }
                }
            ]
        }
    }
}

```
Create an IAM policy to attach Amazon S3 permissions to the IAM role. See the
 following example `iam-policy.json` file and replace the
 ``user input placeholders`` with your
 own information. 

###### Note

If you use server-side encryption with AWS Key Management Service (AWS KMS) keys to encrypt your data, the
 following example adds the necessary AWS KMS permissions for the IAM role in the
 policy. If you do not use this feature, you can remove these permissions from
 your IAM policy. 

To make sure that the IAM role can only be used to access data in S3 if the credentials
 are vended out by S3 Access Grants, this example shows you how to add a
 `Condition` statement that specifies the S3 Access Grants instance
 (`s3:AccessGrantsInstance:
 `InstanceArn``) in your IAM policy. When using following example policy, replace the ``user input placeholders`` with your own information.

*iam-policy.json*


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "ObjectLevelReadPermissions",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:GetObjectAcl",
 "s3:GetObjectVersionAcl",
 "s3:ListMultipartUploadParts"
 ],
 "Resource": [ 
 "arn:aws:s3:::*" 
 ],
 "Condition": {
 "StringEquals": { "aws:ResourceAccount": "`111122223333`" },
 "ArnEquals": {
 "s3:AccessGrantsInstanceArn": ["arn:aws:s3:us-east-1::access-grants/default"]
 }
 } 
 },
 {
 "Sid": "ObjectLevelWritePermissions",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl",
 "s3:PutObjectVersionAcl",
 "s3:DeleteObject",
 "s3:DeleteObjectVersion",
 "s3:AbortMultipartUpload"
 ],
 "Resource": [
 "arn:aws:s3:::*" 
 ],
 "Condition": {
 "StringEquals": { "aws:ResourceAccount": "`111122223333`" },
 "ArnEquals": {
 "s3:AccessGrantsInstanceArn": ["arn:aws:s3:us-east-1::access-grants/default"]
 }
 } 
 },
 {
 "Sid": "BucketLevelReadPermissions",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ],
 "Condition": {
 "StringEquals": { "aws:ResourceAccount": "`111122223333`" },
 "ArnEquals": {
 "s3:AccessGrantsInstanceArn": ["arn:aws:s3:us-east-1::access-grants/default"]
 }
 } 
 },
 {
 "Sid": "KMSPermissions",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.us-east-1.amazonaws.com"
 }
 }
 }
 ]
}`

```




Run the following command:


```
aws iam put-role-policy \
--role-name accessGrantsTestRole \
--policy-name accessGrantsTestRole \
--policy-document file://iam-policy.json
```
###### Example Register the default location


```
aws s3control create-access-grants-location \
 --account-id `111122223333` \
 --location-scope `s3://` \
 --iam-role-arn arn:aws:iam::`111122223333`:role/`accessGrantsTestRole`
```
Response:


```
{"CreatedAt": "2023-05-31T18:23:48.107000+00:00",
    "AccessGrantsLocationId": "default",
    "AccessGrantsLocationArn": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/location/default",
    "LocationScope": "s3://" 
    "IAMRoleArn": "arn:aws:iam::`111122223333`:role/accessGrantsTestRole"
}

```
###### Example Register a custom location


```
aws s3control create-access-grants-location \
 --account-id `111122223333` \
 --location-scope `s3://DOC-BUCKET-EXAMPLE/` \
 --iam-role-arn arn:aws:iam::`123456789012`:role/`accessGrantsTestRole`
```
Response:


```
{"CreatedAt": "2023-05-31T18:23:48.107000+00:00",
    "AccessGrantsLocationId": "635f1139-1af2-4e43-8131-a4de006eb456",
    "AccessGrantsLocationArn": "arn:aws:s3:`us-east-2`: `111122223333`:access-grants/default/location/635f1139-1af2-4e43-8131-a4de006eb888",
    "LocationScope": "s3://DOC-BUCKET-EXAMPLE/",
    "IAMRoleArn": "arn:aws:iam::`111122223333`:role/accessGrantsTestRole"
}
```
For information about Amazon S3 REST API support for managing an S3 Access Grants instance, see
 the following sections in the *Amazon Simple Storage Service API Reference*:


* [CreateAccessGrantsLocation](../API/API_control_CreateAccessGrantsLocation.md "../API/API_control_CreateAccessGrantsLocation.md")
* [DeleteAccessGrantsLocation](../API/API_control_DeleteAccessGrantsLocation.md "../API/API_control_DeleteAccessGrantsLocation.md")
* [GetAccessGrantsLocation](../API/API_control_GetAccessGrantsLocation.md "../API/API_control_GetAccessGrantsLocation.md")
* [ListAccessGrantsLocations](../API/API_control_ListAccessGrantsLocations.md "../API/API_control_ListAccessGrantsLocations.md")
* [UpdateAccessGrantsLocation](../API/API_control_UpdateAccessGrantsLocation.md "../API/API_control_UpdateAccessGrantsLocation.md")
This section provides examples of how to register locations by using the AWS
 SDKs.

To use the following examples, replace the ``user input
 placeholders`` with your own information.


Java
You can register the default location, `s3://`, or a custom
 location in your S3 Access Grants instance. Make sure that you first create an
 IAM role with principal access to the location, and then make sure
 that you grant S3 Access Grants permission to assume this role. 


To use the following example commands, replace the ``user input placeholders`` with your own information.


###### Example Register a default location

Request:


```
public void createAccessGrantsLocation() {
CreateAccessGrantsLocationRequest createRequest = CreateAccessGrantsLocationRequest.builder()
.accountId("`111122223333`")
.locationScope("`s3://`")
.iamRoleArn("arn:aws:iam::`123456789012`:role/`accessGrantsTestRole`")
.build();
CreateAccessGrantsLocationResponse createResponse = s3Control.createAccessGrantsLocation(createRequest);
LOGGER.info("CreateAccessGrantsLocationResponse: " + createResponse);
}
```
Response:


```
CreateAccessGrantsLocationResponse(
CreatedAt=2023-06-07T04:35:11.027Z,
AccessGrantsLocationId=default,
AccessGrantsLocationArn=arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/location/default,
LocationScope=s3://,
IAMRoleArn=arn:aws:iam::`111122223333`:role/accessGrantsTestRole
)
```

###### Example Register a custom location

Request:


```
public void createAccessGrantsLocation() {
CreateAccessGrantsLocationRequest createRequest = CreateAccessGrantsLocationRequest.builder()
.accountId("`111122223333`")
.locationScope("`s3://DOC-BUCKET-EXAMPLE/`")
.iamRoleArn("arn:aws:iam::`111122223333`:role/`accessGrantsTestRole`")
.build();
CreateAccessGrantsLocationResponse createResponse = s3Control.createAccessGrantsLocation(createRequest);
LOGGER.info("CreateAccessGrantsLocationResponse: " + createResponse);
}
```
Response:


```
CreateAccessGrantsLocationResponse(
CreatedAt=2023-06-07T04:35:10.027Z,
AccessGrantsLocationId=18cfe6fb-eb5a-4ac5-aba9-8d79f04c2012,
AccessGrantsLocationArn=arn:aws:s3:us-east-2:`111122223333`:access-grants/default/location/18cfe6fb-eb5a-4ac5-aba9-8d79f04c2666,
LocationScope= s3://test-bucket-access-grants-user123/,
IAMRoleArn=arn:aws:iam::`111122223333`:role/accessGrantsTestRole
)
```
