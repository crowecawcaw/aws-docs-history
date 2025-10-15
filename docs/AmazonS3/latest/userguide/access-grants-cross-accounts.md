# S3 Access Grants cross-account access

With S3 Access Grants, you can grant Amazon S3 data access to the following: 


* AWS Identity and Access Management (IAM) identities within your account
* IAM identities in other AWS accounts
* Directory users or groups in your AWS IAM Identity Center instance
First, configure cross-account access for the other account. This includes granting access to
 your S3 Access Grants instance by using a resource policy. Then, grant access to your S3 data
 (buckets, prefixes, or objects) by using grants. 

After you configure cross-account access, the other account can request temporary access
 credentials to your Amazon S3 data from S3 Access Grants. The following image shows the user flow for
 cross-account S3 access through S3 Access Grants:


![S3 Access Grants cross-account user flow](../../../images/AmazonS3/latest/userguide/images/access-grants-cross-account.png)

1. Users or applications in a second account (B) request credentials from the S3 Access Grants instance in
 your account (A), where the Amazon S3 data is stored. For more information, see [Request access to Amazon S3 data through
 S3 Access Grants](access-grants-credentials.md "access-grants-credentials.md").
2. The S3 Access Grants instance in your account (A) returns temporary credentials if there is a grant that gives the second account access to your Amazon S3 data. For more information on access grants, see [Working with grants in S3 Access Grants](access-grants-grant.md "access-grants-grant.md").
3. Users or applications in the second account (B) use the S3 Access Grants-vended credentials to access the S3 data in your account (A).

###### Configuring S3 Access Grants cross-account access


To grant cross-account S3 access through S3 Access Grants, follow these steps:



* **Step 1:** Configure an S3 Access Grants instance in your account, for
 example, account ID `111122223333`, where the S3 data is
 stored.
* **Step 2:** Configure the resource policy for the S3 Access Grants instance
 in your account `111122223333` to give access to the second
 account, for example, account ID `444455556666`.
* **Step 3:** Configure the IAM permissions for the IAM Principal in the second account `444455556666` to request credentials from the S3 Access Grants instance in your account `111122223333`.
* **Step 4:** Create a grant in your account `111122223333` that gives the IAM Principal in the second account `444455556666` access to some of the S3 data in your account `111122223333`.

## Step 1: Configure an S3 Access Grants instance in your account


First, you must have an S3 Access Grants instance in your account `111122223333`
 to manage access to your Amazon S3 data. You must create an S3 Access Grants instance in each
 AWS Region where the S3 data that you want to share is stored. If you are sharing data
 in more than one AWS Region, then repeat each of these configuration steps for each
 AWS Region. If you already have an S3 Access Grants instance in the AWS Region where your S3
 data is stored, proceed to the next step. If you haven’t configured an S3 Access Grants instance,
 see [Working with S3 Access Grants instances](access-grants-instance.md "access-grants-instance.md") to
 complete this step. 


## Step 2: Configure the resource policy for
 your S3 Access Grants instance to grant cross-account access


After you create an S3 Access Grants instance in your account `111122223333` for
 cross-account access, configure the resource-based policy for the S3 Access Grants instance in
 your account `111122223333` to grant cross-account access. The
 S3 Access Grants instance itself supports resource-based policies. With the correct resource-based
 policy in place, you can grant access for AWS Identity and Access Management (IAM) users or roles from other
 AWS accounts to your S3 Access Grants instance. Cross-account access only grants these
 permissions (actions):



* `s3:GetAccessGrantsInstanceForPrefix` — the user, role,
 or app can retrieve the S3 Access Grants instance that contains a particular prefix.
* `s3:ListAccessGrants`
* `s3:ListAccessLocations`
* `s3:ListCallerAccessGrants`
* `s3:GetDataAccess` — the user, role, or app can request
 temporary credentials based on the access you were granted through S3 Access Grants. Use
 these credentials to access the S3 data to which you have been granted access.

You can choose which of these permissions to include in the resource policy. This resource
 policy on the S3 Access Grants instance is a normal resource-based policy and supports everything
 that the [IAM policy language](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html") supports. In the same policy, you can grant access to
 specific IAM identities in your account `111122223333`, for
 example, by using the `aws:PrincipalArn` condition, but you don't have to do
 that with S3 Access Grants. Instead, within your S3 Access Grants instance, you can create grants for
 individual IAM identities from your account, as well as for the other account. By
 managing each access grant through S3 Access Grants, you can scale your permissions.


If you already use [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html "https://docs.aws.amazon.com/ram/latest/userguide/what-is.html") (AWS RAM), you can use it to share your [`s3:AccessGrants`](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-s3 "https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-s3") resources with other accounts or within
 your organization. See [Working with shared AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with.html "https://docs.aws.amazon.com/ram/latest/userguide/working-with.html") for more information. If you don't use AWS RAM, you can also add the resource policy by using the
 S3 Access Grants API operations or the AWS Command Line Interface (AWS CLI). 


We recommend that you use the AWS Resource Access Manager (AWS RAM) Console to share your
 `s3:AccessGrants` resources with other accounts or within your
 organization. To share S3 Access Grants cross-account, do the following:

###### To configure the S3 Access Grants instance resource policy:

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Select the AWS Region from the AWS Region selector.
3. From the left navigation pane, select **Access Grants**.
4. On the Access Grants instance page, in the **Instance in this account**
 section, select **Share instance**. This will redirect
 you to the AWS RAM Console.
5. Select **Create resource share**.
6. Follow the AWS RAM steps to create the resource share. For more information, see [Creating a resource share in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html "https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html").
To install the AWS CLI, see [Installing the
 AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html") in the *AWS Command Line Interface User Guide*. 

You can add the resource policy by using the `put-access-grants-instance-resource-policy` CLI command.

If you want to grant cross-account access for the S3 Access Grants instance is in your account `111122223333` to the second account `444455556666`, the resource policy for the S3 Access Grants instance in your account `111122223333` should give the second account `444455556666` permission to perform the following actions: 


* `s3:ListAccessGrants`
* `s3:ListAccessGrantsLocations`
* `s3:GetDataAccess`
* `s3:GetAccessGrantsInstanceForPrefix`
In the S3 Access Grants instance resource policy, specify the ARN of your S3 Access Grants instance as the `Resource`, and the second account `444455556666` as the `Principal`. To use the following example, replace the `user input
 placeholders` with your own information.


```
{
"Version": "2012-10-17",		 	 	 
"Statement": [
{
	"Effect": "Allow", 
	"Principal": {
	"AWS": "`444455556666`"
}, 
	"Action": [
		"s3:ListAccessGrants",
		"s3:ListAccessGrantsLocations",
		"s3:GetDataAccess",
		"s3:GetAccessGrantsInstanceForPrefix"
	],
	"Resource": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default"
} ]
}
```
To add or update the S3 Access Grants instance resource policy, use the following command. When you
 use the following example command, replace the ``user input
 placeholders`` with your own information.

###### Example Add or update the S3 Access Grants instance resource policy


```

	aws s3control put-access-grants-instance-resource-policy \
	--account-id `111122223333` \
	--policy file://resourcePolicy.json \
	--region `us-east-2`
	{
		"Policy": "{\n 
		  \"Version\": \"2012-10-17\",\n 
		  \"Statement\": [{\n  
			\"Effect\": \"Allow\",\n
			\"Principal\": {\n
			  \"AWS\": \"`444455556666`\"\n
			},\n  
			\"Action\": [\n
			  \"s3:ListAccessGrants\",\n
			  \"s3:ListAccessGrantsLocations\",\n
			  \"s3:GetDataAccess\",\n
			  \"s3:GetAccessGrantsInstanceForPrefix\",\n
			  \"s3:ListCallerAccessGrants"\n
			],\n
			\"Resource\": \"arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default\"\n
		   }\n  
		  ]\n
		  }\n",
		"CreatedAt": "2023-06-16T00:07:47.473000+00:00"
	}

```
###### Example Get an S3 Access Grants resource policy

You can also use the CLI to get or delete a resource policy for an S3 Access Grants instance.

To get an S3 Access Grants resource policy, use the following example command. To use this example
 command, replace the ``user input
 placeholders`` with your own information.


```
aws s3control get-access-grants-instance-resource-policy \
--account-id `111122223333` \
--region `us-east-2`

{
"Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::`111122223333`:root\"},\"Action\":[\"s3:ListAccessGrants\",\"s3:ListAccessGrantsLocations\",\"s3:GetDataAccess\",\"s3:GetAccessGrantsInstanceForPrefix\",\"s3:ListCallerAccessGrants\"],\"Resource\":\"arn:aws:
s3:`us-east-2`:`111122223333`:access-grants/default\"}]}",
"CreatedAt": "2023-06-16T00:07:47.473000+00:00"
}
```
###### Example Delete an S3 Access Grants resource policy

To delete an S3 Access Grants resource policy, use the following example command. To use this example
 command, replace the ``user input
 placeholders`` with your own information.


```
aws s3control delete-access-grants-instance-resource-policy \
--account-id `111122223333` \
--region `us-east-2`

// No response body
```
You can add the resource policy by using the [PutAccessGrantsInstanceResourcePolicy API](../API/API_control_PutAccessGrantsInstanceResourcePolicy.md "../API/API_control_PutAccessGrantsInstanceResourcePolicy.md").

If you want to grant cross-account access for the S3 Access Grants instance is in your account `111122223333` to the second account `444455556666`, the resource policy for the S3 Access Grants instance in your account `111122223333` should give the second account `444455556666` permission to perform the following actions: 


* `s3:ListAccessGrants`
* `s3:ListAccessGrantsLocations`
* `s3:GetDataAccess`
* `s3:GetAccessGrantsInstanceForPrefix`
In the S3 Access Grants instance resource policy, specify the ARN of your S3 Access Grants instance as the `Resource`, and the second account `444455556666` as the `Principal`. To use the following example, replace the `user input
 placeholders` with your own information.


```
{
"Version": "2012-10-17",		 	 	 
"Statement": [
{
	"Effect": "Allow", 
	"Principal": {
	"AWS": "`444455556666`"
}, 
	"Action": [
		"s3:ListAccessGrants",
		"s3:ListAccessGrantsLocations",
		"s3:GetDataAccess",
		"s3:GetAccessGrantsInstanceForPrefix"
	],
	"Resource": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default"
} ]
}
```
You can then use the [PutAccessGrantsInstanceResourcePolicy API](../API/API_control_PutAccessGrantsInstanceResourcePolicy.md "../API/API_control_PutAccessGrantsInstanceResourcePolicy.md") to configure the policy.

For information on the REST
 API support to update, get, or delete a resource policy for an S3 Access Grants instance, see the following sections in the
 *Amazon Simple Storage Service API Reference*:


* [PutAccessGrantsInstanceResourcePolicy](../API/API_control_PutAccessGrantsInstanceResourcePolicy.md "../API/API_control_PutAccessGrantsInstanceResourcePolicy.md")
* [GetAccessGrantsInstanceResourcePolicy](../API/API_control_GetAccessGrantsInstanceResourcePolicy.md "../API/API_control_GetAccessGrantsInstanceResourcePolicy.md")
* [DeleteAccessGrantsInstanceResourcePolicy](../API/API_control_DeleteAccessGrantsInstanceResourcePolicy.md "../API/API_control_DeleteAccessGrantsInstanceResourcePolicy.md")
This section provides you with the AWS SDK examples of how to configure your S3 Access Grants
 resource policy to grant a second AWS account access to some of your S3 data. 


Java
Add, update, get, or delete a resource policy to manage cross-account access to your S3 Access Grants instance. 


###### Example Add or update an S3 Access Grants instance resource policy

If you want to grant cross-account access for the S3 Access Grants instance is in your account `111122223333` to the second account `444455556666`, the resource policy for the S3 Access Grants instance in your account `111122223333` should give the second account `444455556666` permission to perform the following actions: 


* `s3:ListAccessGrants`
* `s3:ListAccessGrantsLocations`
* `s3:GetDataAccess`
* `s3:GetAccessGrantsInstanceForPrefix`
In the S3 Access Grants instance resource policy, specify the ARN of your S3 Access Grants instance as the `Resource`, and the second account `444455556666` as the `Principal`. To use the following example, replace the `user input
 placeholders` with your own information.


```
{
"Version": "2012-10-17",		 	 	 
"Statement": [
{
	"Effect": "Allow", 
	"Principal": {
	"AWS": "`444455556666`"
}, 
	"Action": [
		"s3:ListAccessGrants",
		"s3:ListAccessGrantsLocations",
		"s3:GetDataAccess",
		"s3:GetAccessGrantsInstanceForPrefix"
	],
	"Resource": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default"
} ]
}
```
To add or update an S3 Access Grants instance resource policy, use the following code
 example:


```
public void putAccessGrantsInstanceResourcePolicy() {
	PutAccessGrantsInstanceResourcePolicyRequest putRequest = PutAccessGrantsInstanceResourcePolicyRequest.builder()
	.accountId(`111122223333`)
	.policy(RESOURCE_POLICY)
	.build();
	PutAccessGrantsInstanceResourcePolicyResponse putResponse = s3Control.putAccessGrantsInstanceResourcePolicy(putRequest);
	LOGGER.info("PutAccessGrantsInstanceResourcePolicyResponse: " + putResponse);
	}
```
Response:


```
PutAccessGrantsInstanceResourcePolicyResponse(
	Policy={
	"Version": "2012-10-17",		 	 	 
	"Statement": [{
	"Effect": "Allow",
	"Principal": {
	"AWS": "``444455556666``"
	},
	"Action": [
	"s3:ListAccessGrants",
	"s3:ListAccessGrantsLocations",
	"s3:GetDataAccess",
	"s3:GetAccessGrantsInstanceForPrefix",
	"s3:ListCallerAccessGrants"
	],
	"Resource": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default"
	}]
	}
	)
```

###### Example Get an S3 Access Grants resource policy

To get an S3 Access Grants resource policy, use the following code example. To use the following
 example command, replace the ``user input
 placeholders`` with your own
 information.


```
public void getAccessGrantsInstanceResourcePolicy() {
	GetAccessGrantsInstanceResourcePolicyRequest getRequest = GetAccessGrantsInstanceResourcePolicyRequest.builder()
	.accountId(`111122223333`)
	.build();
	GetAccessGrantsInstanceResourcePolicyResponse getResponse = s3Control.getAccessGrantsInstanceResourcePolicy(getRequest);
	LOGGER.info("GetAccessGrantsInstanceResourcePolicyResponse: " + getResponse);
	}
```
Response:


```
GetAccessGrantsInstanceResourcePolicyResponse(
	Policy={"Version": "2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::`444455556666`:root"},"Action":["s3:ListAccessGrants","s3:ListAccessGrantsLocations","s3:GetDataAccess","s3:GetAccessGrantsInstanceForPrefix","s3:ListCallerAccessGrants"],"Resource":"arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default"}]},
	CreatedAt=2023-06-15T22:54:44.319Z
	)
```

###### Example Delete an S3 Access Grants resource policy

To delete an S3 Access Grants resource policy, use the following code example. To use the
 following example command, replace the ``user
 input placeholders`` with your own
 information.


```
public void deleteAccessGrantsInstanceResourcePolicy() {
	DeleteAccessGrantsInstanceResourcePolicyRequest deleteRequest = DeleteAccessGrantsInstanceResourcePolicyRequest.builder()
	.accountId(`111122223333`)
	.build();
	DeleteAccessGrantsInstanceResourcePolicyResponse deleteResponse = s3Control.putAccessGrantsInstanceResourcePolicy(deleteRequest);
	LOGGER.info("DeleteAccessGrantsInstanceResourcePolicyResponse: " + deleteResponse);
	}
```
Response:


```
DeleteAccessGrantsInstanceResourcePolicyResponse()
```



## Step 3: Grant IAM identities in a second account permission to call the S3 Access Grants instance in your account


After the owner of the Amazon S3 data has configured the cross-account policy for the S3 Access Grants
 instance in account `111122223333`, the owner of the second account
 `444455556666` must create an identity-based policy for its
 IAM users or roles, and the owner must give them access to the S3 Access Grants instance. In the
 identity-based policy, include one or more of the following actions, depending on what’s
 granted in the S3 Access Grants instance resource policy and the permissions you want to
 grant:



* `s3:ListAccessGrants`
* `s3:ListAccessGrantsLocations`
* `s3:GetDataAccess`
* `s3:GetAccessGrantsInstanceForPrefix`
* `s3:ListCallerAccessGrants`

Following the [AWS
 cross-account access pattern](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html"), the IAM users or roles in the second account
 `444455556666` must explicitly have one or more of these
 permissions. For example, grant the `s3:GetDataAccess` permission so that the
 IAM user or role can call the S3 Access Grants instance in account
 `111122223333` to request credentials. 


To use this example command, replace the ``user input placeholders`` with your own information.



```
{
	"Version": "2012-10-17",		 	 	 
	"Statement": [
	{
		"Effect": "Allow", 
		"Action": [
			"s3:GetDataAccess",
		],
			"Resource": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default"
		} 
	]
}
```

For information on editing IAM identity-based policy, see [Editing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html") in the *AWS Identity and Access Management guide*.


## Step 4:
 Create
 a grant in the S3 Access Grants instance of your account that gives the IAM identity in the
 second account access to some of your S3 data


For the final configuration step, you can create a grant in the S3 Access Grants instance in
 your account 111122223333 that gives access to the IAM identity in the
 second account 444455556666 to some of the S3 data in your account. You can do
 this by using the Amazon S3 Console, CLI, API, and SDKs. For more information, see [Create grants](access-grants-grant-create.md "access-grants-grant-create.md"). 


In the grant, specify the AWS ARN of the IAM identity from the second account, and
 specify which location in your S3 data (a bucket, prefix, or object) that you are
 granting access to. This location must already be registered with your S3 Access Grants instance.
 For more information, see [Register a location](access-grants-location-register.md "access-grants-location-register.md"). You can optionally specify a subprefix.
 For example, if the location you are granting access to is a bucket, and you want to
 limit the access further to a specific object in that bucket, then pass the object key
 name in the `S3SubPrefix` field. Or if you want to limit access to the
 objects in the bucket with key names that start with a specific prefix, such as
 `2024-03-research-results/`, then pass
 `S3SubPrefix=2024-03-research-results/`. 


The following is an example CLI command for creating an access grant for an identity
 in the second account. See [Create grants](access-grants-grant-create.md "access-grants-grant-create.md") for more information. To use this example
 command, replace the ``user input placeholders``
 with your own information.



```
aws s3control create-access-grant \
--account-id `111122223333` \
--access-grants-location-id default \
--access-grants-location-configuration S3SubPrefix=`prefixA*` \
--permission READ \
--grantee GranteeType=IAM,GranteeIdentifier=arn:aws:iam::`444455556666`:`role/data-consumer-1`
```

After configuring cross-account access, the user or role in the second account can do the
 following: 


* Calls `ListAccessGrantsInstances` to list the S3 Access Grants instances shared with it
 through AWS RAM. For more information, see [Get the details of an S3 Access Grants instance](access-grants-instance-view.md "access-grants-instance-view.md").
* Requests temporary credentials from S3 Access Grants. For more information on how to make these requests, see [Request access to Amazon S3 data through
 S3 Access Grants](access-grants-credentials.md "access-grants-credentials.md").
