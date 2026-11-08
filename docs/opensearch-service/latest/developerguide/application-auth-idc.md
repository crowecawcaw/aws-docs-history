

# AWS IAM Identity Center authentication for OpenSearch UI
<a name="application-auth-idc"></a>

With AWS IAM Identity Center, your team gets a browser-based single sign-on experience. Your users sign in with their AWS IAM Identity Center credentials instead of generating presigned URLs.

## Prerequisites
<a name="application-auth-idc-prerequisites"></a>
+ An AWS account with both the base and the AWS IAM Identity Center IAM permissions. For more information about the required permissions, see [IAM policy reference for OpenSearch UI](application-iam-policy-reference.md).
+ AWS IAM Identity Center enabled in your account or organization. Note whether you have an organization instance or an account instance, because this affects some configuration steps.
+ An IAM role with both the required permissions policy and a trust policy. You create this role in [Step 2: Create the IAM role](#application-auth-idc-role).
+ At least one OpenSearch domain or serverless collection in the AWS Region.
+ At least one user or group created in AWS IAM Identity Center.

## Additional prerequisite for an organization instance that uses a customer managed key
<a name="application-auth-idc-cmk"></a>

If your organization instance of AWS IAM Identity Center uses a customer managed key for encryption at rest, you must grant OpenSearch UI permission to decrypt identity data with that key. Without this permission, single sign-on fails with `AccessDeniedException` while OpenSearch UI validates the authorization code.

To check whether your instance uses a customer managed key, open the AWS IAM Identity Center console, choose **Settings**, choose the **Management** tab, and review **Key for encrypting IAM Identity Center data at rest**. If it shows a customer managed key ARN rather than an AWS owned key, add the following statements to the key policy in the management account where AWS IAM Identity Center is enabled. Replace {{organization-id}} with your AWS Organizations organization ID, in the format `o-xxxxxxxxxx`.

```
{
    "Sid": "Allow_AWS_app_admins_in_the_same_AWS_organization_to_use_the_KMS_key",
    "Effect": "Allow",
    "Principal": "*",
    "Action": [
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:PrincipalOrgID": "{{organization-id}}"
        },
        "StringLike": {
            "kms:ViaService": [
                "sso.*.amazonaws.com",
                "identitystore.*.amazonaws.com"
            ]
        }
    }
},
{
    "Sid": "Allow_managed_apps_to_use_the_KMS_Key",
    "Effect": "Allow",
    "Principal": "*",
    "Action": [
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "Bool": {
            "aws:PrincipalIsAWSService": "true"
        },
        "StringLike": {
            "kms:ViaService": [
                "sso.*.amazonaws.com",
                "identitystore.*.amazonaws.com"
            ]
        },
        "StringEquals": {
            "aws:SourceOrgID": "{{organization-id}}"
        }
    }
}
```

For more information, see [Customer managed keys](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-customer-managed-keys.html) in the *AWS IAM Identity Center User Guide*.

## Step 1: Verify that AWS IAM Identity Center is enabled
<a name="application-auth-idc-verify-enabled"></a>

**To verify that AWS IAM Identity Center is enabled**

1. Open the [AWS IAM Identity Center console](https://console.aws.amazon.com/singlesignon/).

1. If the console shows a dashboard with your instance details, AWS IAM Identity Center is enabled. Note whether the instance is an organization instance or an account instance.

1. If the console shows a setup page, enable AWS IAM Identity Center before you continue.

An organization instance works across all accounts in your AWS Organizations organization, and it is recommended for production use. An account instance is scoped to a single account, which suits testing and isolated setups. If your account belongs to an organization that someone else manages, ask your administrator whether AWS IAM Identity Center must be enabled at the organization level.

## Step 2: Create the IAM role
<a name="application-auth-idc-role"></a>

AWS IAM Identity Center assumes an IAM role when users access your OpenSearch UI application. That role needs a permissions policy, which defines what the role can do, and a trust policy, which defines who can assume the role.

Use the following permissions policy. Replace the placeholder values with your own information.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "opensearch:ApplicationAccessAll",
            "Resource": "arn:aws:opensearch:{{region}}:{{account-id}}:application/*"
        }
    ]
}
```

Use the following trust policy, which allows AWS IAM Identity Center to assume the role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "sso.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

To create the role and attach the permissions policy with the AWS CLI, run the following commands:

```
aws iam create-role \
    --role-name OpenSearchUI-IDC-Role \
    --assume-role-policy-document '{
      "Version":"2012-10-17",
      "Statement":[{
        "Effect":"Allow",
        "Principal":{"Service":"sso.amazonaws.com"},
        "Action":"sts:AssumeRole"
      }]
    }'

aws iam put-role-policy \
    --role-name OpenSearchUI-IDC-Role \
    --policy-name OpenSearchAppAccess \
    --policy-document '{
      "Version":"2012-10-17",
      "Statement":[{
        "Effect":"Allow",
        "Action":"opensearch:ApplicationAccessAll",
        "Resource":"arn:aws:opensearch:{{region}}:{{account-id}}:application/*"
      }]
    }'
```

Note the role ARN. You specify it in the next step. The ARN has the format `arn:aws:iam::{{account-id}}:role/OpenSearchUI-IDC-Role`.

## Step 3: Create the application with AWS IAM Identity Center enabled
<a name="application-auth-idc-create"></a>

**To start creating the application**

1. Open the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/home).

1. On the navigation menu, choose **OpenSearch UI (Dashboards)**.

1. Choose **Create application**.

1. Enter a name for the application.

1. Add at least one data source, either an OpenSearch domain or a serverless collection.

Continue in the same form to turn on single sign-on and finish creating the application.

**To enable AWS IAM Identity Center and create the application**

1. Select the **Authentication with IAM Identity Center** check box.

1. Select the IAM role that you created in [Step 2: Create the IAM role](#application-auth-idc-role).

1. (Optional) Configure dashboard administrators.

1. Choose **Create**.

To create the same application with the AWS CLI, run the following command. Replace the placeholder values with your own information.

```
aws opensearch create-application \
    --name "{{application-name}}" \
    --iam-identity-center-options '{
      "enabled": true,
      "iamRoleForIdentityCenterApplicationArn": "arn:aws:iam::{{account-id}}:role/OpenSearchUI-IDC-Role"
    }' \
    --data-sources '[{
      "dataSourceArn": "arn:aws:es:{{region}}:{{account-id}}:domain/{{domain-name}}"
    }]' \
    --region {{region}}
```

## Step 4: Assign users in AWS IAM Identity Center
<a name="application-auth-idc-assign"></a>

**To assign users or groups to the application**

1. Open the [AWS IAM Identity Center console](https://console.aws.amazon.com/singlesignon/).

1. On the navigation menu, choose **Applications**.

1. Choose the application that OpenSearch UI registered automatically. Its name matches your OpenSearch UI application name.

1. Choose **Assign users and groups**.

1. Select the users or groups that need access, and then choose **Assign**.

## Step 5: Verify the setup
<a name="application-auth-idc-verify"></a>

**To verify the setup**

1. In the Amazon OpenSearch Service console, confirm that the application status is **Active**, which indicates that the application is ready to use.

1. Confirm that **Authentication with IAM Identity Center** is enabled on the application details page.

1. Copy the application URL from the application details page.

1. Open the application URL in a browser. You are redirected to the AWS IAM Identity Center sign-in page.

1. Sign in with your AWS IAM Identity Center credentials. The OpenSearch UI workspace selector appears.

## Managing users and groups programmatically
<a name="application-auth-idc-assignments"></a>

When you create an OpenSearch UI application with AWS IAM Identity Center enabled, OpenSearch UI registers an AWS IAM Identity Center application. You must assign users to that application before they can sign in. There are two separate levels of access:

Application assignment  
Controls who can sign in to OpenSearch UI. You manage it with the `sso-admin` commands.

Application administrator  
Controls who can edit or delete the application and manage its workspaces. You manage it with `aws opensearch update-application`. For more information about application administrators, see [Managing application administrators](application-getting-started.md#managing-application-administrators).

You need three identifiers before you manage assignments.


| Identifier | How to get it | 
| --- | --- | 
| The AWS IAM Identity Center application ARN | aws opensearch get-application, in iamIdentityCenterOptions.iamIdentityCenterApplicationArn | 
| The identity store ID | aws sso-admin list-instances, in Instances[0].IdentityStoreId | 
| The user or group ID | aws identitystore list-users or aws identitystore list-groups | 

The following commands find a user by their user name, and a group by its display name. Replace the {{placeholder values}} with your own information:

```
aws identitystore list-users \
    --identity-store-id {{identity-store-id}} \
    --filters '[{"AttributePath":"UserName","AttributeValue":"{{user-name}}"}]' \
    --region {{region}} \
    --query 'Users[0].UserId' --output text

aws identitystore list-groups \
    --identity-store-id {{identity-store-id}} \
    --filters '[{"AttributePath":"DisplayName","AttributeValue":"{{group-name}}"}]' \
    --region {{region}} \
    --query 'Groups[0].GroupId' --output text
```

The following commands assign a user or a group to the application, and review or remove assignments. For a group, set `--principal-type` to `GROUP` and use the group ID that you found earlier as the principal ID:

```
aws sso-admin create-application-assignment \
    --application-arn {{identity-center-application-arn}} \
    --principal-id {{principal-id}} \
    --principal-type USER \
    --region {{region}}

aws sso-admin list-application-assignments \
    --application-arn {{identity-center-application-arn}} \
    --region {{region}}

aws sso-admin delete-application-assignment \
    --application-arn {{identity-center-application-arn}} \
    --principal-id {{principal-id}} \
    --principal-type USER \
    --region {{region}}
```

If a user or group does not exist in your identity store yet, create it with `aws identitystore create-user` or `aws identitystore create-group`, and add members with `aws identitystore create-group-membership`.

The following Python code example looks up a user by user name and assigns that user to the application with the AWS SDK for Python (Boto3):

```
import boto3

region = "{{region}}"
app_id = "{{application-id}}"

opensearch = boto3.client("opensearch", region_name=region)
sso_admin = boto3.client("sso-admin", region_name=region)
identity_store = boto3.client("identitystore", region_name=region)

app = opensearch.get_application(id=app_id)
idc_app_arn = app["iamIdentityCenterOptions"]["iamIdentityCenterApplicationArn"]

identity_store_id = sso_admin.list_instances()["Instances"][0]["IdentityStoreId"]

users = identity_store.list_users(
    IdentityStoreId=identity_store_id,
    Filters=[{"AttributePath": "UserName", "AttributeValue": "{{user-name}}"}],
)
user_id = users["Users"][0]["UserId"]

sso_admin.create_application_assignment(
    ApplicationArn=idc_app_arn,
    PrincipalId=user_id,
    PrincipalType="USER",
)
```

## Troubleshooting AWS IAM Identity Center authentication
<a name="application-auth-idc-troubleshooting"></a>

AWS IAM Identity Center authentication problems usually come from a trust policy that omits `sso.amazonaws.com`, a permissions policy that is missing required actions, or a user who is not assigned to the application. The following table lists common symptoms, their likely causes, and how to resolve each one.


| Symptom | Likely cause | Resolution | 
| --- | --- | --- | 
| A message that AWS IAM Identity Center is not enabled appears while you create the application | There is no instance in your account or organization | Enable AWS IAM Identity Center in the AWS IAM Identity Center console | 
| Single sign-on redirects but returns an error | The role trust policy does not include sso.amazonaws.com | Update the trust policy as described in [Step 2: Create the IAM role](#application-auth-idc-role) | 
| Sign-in succeeds but the user has no access | The user is not assigned to the application | Assign the user in the AWS IAM Identity Center console, as described in [Step 4: Assign users in AWS IAM Identity Center](#application-auth-idc-assign) | 
| Access is denied after sign-in | The role permissions policy is missing required actions | Confirm that the role has opensearch:ApplicationAccessAll and permission to access the data sources | 
| The application shows AWS IAM Identity Center as enabled, but sign-in fails | The role ARN does not match | Confirm that the role ARN in the application settings is the role that has the correct trust and permissions policies | 
| The application cannot be created with AWS IAM Identity Center | AWS IAM Identity Center permissions are missing | Confirm that your IAM principal has sso:CreateApplication, sso:PutApplicationGrant, and iam:PassRole | 
| The sign-in page appears but no user can sign in | No users are assigned in AWS IAM Identity Center | Assign users to the application in the AWS IAM Identity Center console | 
| Sign-in fails with a message that the authorization code cannot be validated, or with AccessDeniedException | AWS IAM Identity Center uses a customer managed key without the required key policy | Add the key policy statements described earlier in this topic | 
| A user cannot sign in shortly after being assigned | The assignment has not propagated yet | Wait one to two minutes, and then try again | 
| AccessDeniedException on create-application-assignment | The sso:CreateApplicationAssignment permission is missing | Add the AWS IAM Identity Center permissions listed in [IAM policy reference for OpenSearch UI](application-iam-policy-reference.md) | 
| ConflictException on an assignment | The user or group is already assigned | Confirm with list-application-assignments | 