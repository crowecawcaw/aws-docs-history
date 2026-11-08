

# Using IAM Identity Center with Amazon Managed Workflows for Apache Airflow
<a name="identity-center-integration"></a>

When you enable IAM Identity Center integration, Amazon Managed Workflows for Apache Airflow uses IAM Identity Center to authenticate and authorize you. Sign in to the Apache Airflow UI with your corporate identity provider through the IAM Identity Center device code flow. Amazon MWAA evaluates authorization per request using IAM policies attached to IAM Identity Center Permission Sets.

**Version requirement**  
IAM Identity Center integration requires Apache Airflow version 3.3.1 or later. The Amazon MWAA console hides the IAM Identity Center configuration section for environments running earlier versions.

**Topics**
+ [Prerequisites](#iic-integration-prerequisites)
+ [How it works](#iic-integration-how-it-works)
+ [Enabling IAM Identity Center integration](#iic-integration-enabling)
+ [Configuring access with Permission Sets](#iic-integration-permission-sets)
+ [Teams and the `airflow:TeamNames` condition key](#iic-team-based-access)
+ [Logging in to Apache Airflow with IAM Identity Center](#iic-integration-login)
+ [Known limitations](#iic-integration-limitations)
+ [Troubleshooting](#iic-integration-troubleshooting)

## Prerequisites
<a name="iic-integration-prerequisites"></a>
+ Apache Airflow version 3.3.1 or later.
+ An *organization-level* IAM Identity Center instance. Account-level IAM Identity Center does not support Permission Sets and is not compatible with this feature.
+ Users and groups synced into IAM Identity Center from your corporate identity provider (for example, Okta, Azure AD, or Ping) through SAML or federation, or managed directly in the IAM Identity Center directory.
+ The Amazon MWAA environment's AWS account must be accessible in your IAM Identity Center organization.

## How it works
<a name="iic-integration-how-it-works"></a>

When you open the Apache Airflow UI, Amazon MWAA redirects you to an IAM Identity Center device authorization page. You complete authentication in a separate browser tab using your corporate credentials. After successful authentication, Amazon MWAA obtains temporary IAM Identity Center credentials scoped to your assigned Permission Set and grants you access to the Apache Airflow UI.

Amazon MWAA evaluates authorization on each Apache Airflow UI action using the `airflow:AccessAirflowResource` IAM action and the condition keys described in [Configuring access with Permission Sets](#iic-integration-permission-sets). You attach the policies to IAM Identity Center Permission Sets, not to individual IAM users or roles, which centralizes access governance in IAM Identity Center.

**Apache Airflow Security menu**  
When IAM Identity Center integration is enabled, the Apache Airflow Security menu, including the List Roles, Users, and Permissions pages, is not available. Access control is managed entirely through IAM Identity Center Permission Sets.

## Enabling IAM Identity Center integration
<a name="iic-integration-enabling"></a>

### Recommended: create a new environment
<a name="iic-integration-enabling-new-env"></a>

We recommend creating a new environment with IAM Identity Center integration enabled from the start and migrating users to it. This approach lets existing users continue working on the original environment while you validate the IAM Identity Center setup, without disrupting access to your production environment.

**To migrate to a new environment with IAM Identity Center enabled**

1. Create a new environment with IAM Identity Center enabled, using the same Amazon S3 bucket, DAGs, and Amazon VPC as the existing environment. For steps to configure IAM Identity Center during environment creation, refer to [Step two: Configure advanced settings](create-environment.md#create-environment-start-advanced).

1. Configure Permission Sets and validate access for a subset of users. For more information, refer to [Configuring access with Permission Sets](#iic-integration-permission-sets).

1. Cut traffic over by updating bookmarks or the Amazon MWAA console URL to point to the new environment.

1. Decommission the original environment once all users have migrated.

### Alternative: enable IAM Identity Center on an existing environment
<a name="iic-integration-enabling-existing-env"></a>

**Irreversible action**  
Once IAM Identity Center integration is enabled on an environment, it cannot be disabled. If you need a rollback path, use the recommended parallel-environment approach described in [Recommended: create a new environment](#iic-integration-enabling-new-env).

To enable IAM Identity Center on an existing environment using the Amazon MWAA console, open the **Update environment** wizard. Expand the **Identity Center configuration** section (visible only for environments on Apache Airflow 3.3.1 or later) and provide the access portal URL and Identity Store ID fields. For field descriptions, refer to [Step two: Configure advanced settings](create-environment.md#create-environment-start-advanced). 

To enable IAM Identity Center using the AWS CLI:

```
aws mwaa update-environment \
  --name {{my-env}} \
  --identity-center-configuration '{
    "startUrl": "https://{{d-xxxxxxxxxx}}.awsapps.com/start",
    "identityStoreId": "{{d-xxxxxxxxxx}}"
  }'
```

The update takes 20 to 30 minutes for a forced update, which temporarily takes the environment offline. During a graceful update, your DAGs and tasks continue to run.

`startUrl`  
The IAM Identity Center access portal URL. Found in the IAM Identity Center console under **Settings**. Example: `https://d-xxxxxxxxxx.awsapps.com/start`.

`identityStoreId`  
The IAM Identity Center Identity Store ID. Found in the IAM Identity Center console under **Settings**. Example: `d-xxxxxxxxxx`.

## Configuring access with Permission Sets
<a name="iic-integration-permission-sets"></a>

Authorization in IAM Identity Center-enabled Amazon MWAA environments is controlled by IAM policies attached to IAM Identity Center Permission Sets. You use the `airflow:AccessAirflowResource` action together with the condition keys described in the following table.

**Required identitystore permissions**  
Every Permission Set policy must include the following `identitystore` statement. Amazon MWAA needs it to look up your display name and group memberships; without it, sign-in fails.  

```
{
  "Sid": "AllowIdentityStoreLookup",
  "Effect": "Allow",
  "Action": [
    "identitystore:GetUserId",
    "identitystore:DescribeUser",
    "identitystore:ListGroupMembershipsForMember",
    "identitystore:DescribeGroup"
  ],
  "Resource": "*"
}
```

**Additional requirements when your IAM Identity Center identity store uses a customer managed AWS KMS key**  
If your IAM Identity Center identity store is encrypted with a customer managed AWS KMS key, complete two additional steps. Without them, the `identitystore` API calls that look up your display name and group memberships fail during sign-in with the error: "Could not look up your user information from IAM Identity Center."  
To check whether your identity store uses a customer managed AWS KMS key, open the IAM Identity Center console, choose **Settings**, then **Management**. If the console shows a AWS KMS key ARN on **Key for encrypting IAM Identity Center data at rest**, complete both of the following steps. If the default AWS managed key is shown, you do not need to make any additional changes.  
**Step 1: Add AWS KMS permissions to every Permission Set inline policy.** The Permission Set role makes direct `identitystore` API calls using your federated credentials. The following IAM inline policy statement grants the Permission Set role permission to decrypt data using your AWS KMS key. Add it to the inline policy, replacing the placeholder values with your AWS KMS key ARN:  

```
{
  "Sid": "AllowKMSDecryptForIDC",
  "Effect": "Allow",
  "Action": [
    "kms:Decrypt",
    "kms:DescribeKey"
  ],
  "Resource": "arn:aws:kms:{{key-region}}:{{idc-account-id}}:key/{{key-id}}"
}
```
Where: {{key-region}} is the AWS Region of the AWS KMS key, {{idc-account-id}} is the account ID of the IAM Identity Center organization management account, and {{key-id}} is the ID of your customer managed AWS KMS key. The AWS KMS key ARN is shown in the IAM Identity Center console under **Settings**, then **Management**. The key lives in the IAM Identity Center organization management account. This may be a different account from your Amazon MWAA environment account.  
**Step 2: Add the Permission Set role to the AWS KMS key policy.** Because the key lives in the IAM Identity Center organization management account, add an explicit cross-account entry to the AWS KMS key policy. The following AWS KMS key policy statement grants the Permission Set role in your Amazon MWAA environment account permission to use the key. Replace {{account-id}} with your Amazon MWAA environment account ID, {{sso-region}} with the AWS Region of the Permission Set role, {{permission-set-name-suffix}} with the suffix of the Permission Set role name, {{key-region}} with the AWS Region of the AWS KMS key, {{idc-account-id}} with the IAM Identity Center organization management account ID, and {{key-id}} with the AWS KMS key ID. To find the role name suffix, open the IAM console in your Amazon MWAA environment account after the Permission Set is provisioned and search for `AWSReservedSSO_{{PermissionSetName}}`:  

```
{
  "Sid": "AllowMWAAPermissionSetRole",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::{{account-id}}:role/aws-reserved/sso.amazonaws.com/{{sso-region}}/AWSReservedSSO_{{permission-set-name-suffix}}"
  },
  "Action": [
    "kms:Decrypt",
    "kms:DescribeKey"
  ],
  "Resource": "arn:aws:kms:{{key-region}}:{{idc-account-id}}:key/{{key-id}}"
}
```
Add one entry for each Permission Set for each Amazon MWAA environment account. After updating the key policy, re-provision the Permission Set to the environment account for the changes to take effect.


**Supported condition keys for `airflow:AccessAirflowResource`**  

| Condition key | Type | Description | 
| --- | --- | --- | 
| airflow:ResourceType | String | The type of Apache Airflow resource. Supported values: DAG, Connection, Variable, Pool, Asset, AssetAlias, Configuration, View, CustomView. | 
| airflow:ResourceAction | String | The action being performed. Supported values: GET, POST, PUT, DELETE, LIST. | 
| airflow:ResourceId | String | The ID of a specific resource. For example, a DAG ID. | 
| airflow:DagAccessEntity | String | The sub-resource within a DAG being accessed. Only applies when airflow:ResourceType is DAG. Supported values for Apache Airflow 3.3.1: AUDIT\_LOG, CODE, DEPENDENCIES, HITL\_DETAIL, RUN, TASK, TASK\_INSTANCE, TASK\_LOGS, VERSION, WARNING, XCOM. These values are defined by Apache Airflow core and may change in future Apache Airflow versions. | 
| airflow:TeamNames | ArrayOfString | The list of IAM Identity Center groups the user belongs to, populated automatically from IAM Identity Center when the user assumes a Permission Set role. Use ForAnyValue:StringEquals when writing conditions on this key. | 

**Required ResourceActions for DAG access**  
The Apache Airflow UI makes two distinct types of DAG authorization calls:  
`ResourceAction=LIST` (no `ResourceId`): Used by the DAG list page. A policy that grants only `GET` shows zero DAGs on the list page.
`ResourceAction=GET` (no `ResourceId`): Used by home page dashboard widgets (recent run counts, metrics, and deadline data) that query across all DAGs without specifying a DAG ID. A policy that grants only `LIST` causes the home page to return an access denied error.
Always include both `GET` and `LIST` in any Permission Set that needs DAG access.

Policy changes take effect within a few minutes without any environment update.

The following examples show common Permission Set policy patterns. For additional examples, refer to [IAM Identity Center Permission Set policy examples](access-policies.md#iic-permission-set-policy-examples).

**Example Grant full Apache Airflow access**  <a name="iic-policy-example-full-access"></a>

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAllAirflowResources",
      "Effect": "Allow",
      "Action": "airflow:AccessAirflowResource",
      "Resource": "arn:aws:airflow:{{us-east-1}}:{{123456789012}}:environment/{{my-env}}"
    },
    {
      "Sid": "AllowIdentityStoreLookup",
      "Effect": "Allow",
      "Action": [
        "identitystore:GetUserId",
        "identitystore:DescribeUser",
        "identitystore:ListGroupMembershipsForMember",
        "identitystore:DescribeGroup"
      ],
      "Resource": "*"
    }
  ]
}
```

**Example Restrict to DAG read access (list and view)**  <a name="iic-policy-example-dag-read"></a>
Always include `LIST` alongside `GET`. The DAG list page uses `ResourceAction=LIST`; a policy that grants only `GET` shows zero DAGs.  

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowDagRead",
      "Effect": "Allow",
      "Action": "airflow:AccessAirflowResource",
      "Resource": "arn:aws:airflow:{{us-east-1}}:{{123456789012}}:environment/{{my-env}}",
      "Condition": {
        "StringEquals": {
          "airflow:ResourceType": "DAG",
          "airflow:ResourceAction": ["GET", "LIST"]
        }
      }
    },
    {
      "Sid": "AllowIdentityStoreLookup",
      "Effect": "Allow",
      "Action": [
        "identitystore:GetUserId",
        "identitystore:DescribeUser",
        "identitystore:ListGroupMembershipsForMember",
        "identitystore:DescribeGroup"
      ],
      "Resource": "*"
    }
  ]
}
```

**Example Restrict to a specific DAG**  <a name="iic-policy-example-specific-dag"></a>
Use two separate statements. The first allows `GET` and `LIST` without a `ResourceId`. This is required for the DAG list page (`LIST`) and for home page dashboard widgets that query run counts and metrics across all DAGs (`GET` with no DAG ID). The second allows all actions on the specific DAG identified by `ResourceId`. Do not combine `ResourceId` with `LIST` in the same `StringEquals` block, because `LIST` calls do not supply a `ResourceId` and the condition never matches.  

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowDagGetAndList",
      "Effect": "Allow",
      "Action": "airflow:AccessAirflowResource",
      "Resource": "arn:aws:airflow:{{us-east-1}}:{{123456789012}}:environment/{{my-env}}",
      "Condition": {
        "StringEquals": {
          "airflow:ResourceType": "DAG",
          "airflow:ResourceAction": ["GET", "LIST"]
        }
      }
    },
    {
      "Sid": "AllowSpecificDagAllActions",
      "Effect": "Allow",
      "Action": "airflow:AccessAirflowResource",
      "Resource": "arn:aws:airflow:{{us-east-1}}:{{123456789012}}:environment/{{my-env}}",
      "Condition": {
        "StringEquals": {
          "airflow:ResourceType": "DAG",
          "airflow:ResourceId": "{{my_etl_dag}}"
        }
      }
    },
    {
      "Sid": "AllowIdentityStoreLookup",
      "Effect": "Allow",
      "Action": [
        "identitystore:GetUserId",
        "identitystore:DescribeUser",
        "identitystore:ListGroupMembershipsForMember",
        "identitystore:DescribeGroup"
      ],
      "Resource": "*"
    }
  ]
}
```

**Example Restrict by team using `airflow:TeamNames`**  <a name="iic-policy-example-team-names"></a>
Use `ForAnyValue:StringEquals` (the multi-value operator) for `airflow:TeamNames`. This condition matches if the user belongs to *any* of the listed groups (OR logic). Using the single-value `StringEquals` operator causes the condition to never match when a user belongs to more than one team.  

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowTeamAccess",
      "Effect": "Allow",
      "Action": "airflow:AccessAirflowResource",
      "Resource": "arn:aws:airflow:{{us-east-1}}:{{123456789012}}:environment/{{my-env}}",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "airflow:TeamNames": ["{{platform-team}}", "{{data-eng}}"]
        }
      }
    },
    {
      "Sid": "AllowIdentityStoreLookup",
      "Effect": "Allow",
      "Action": [
        "identitystore:GetUserId",
        "identitystore:DescribeUser",
        "identitystore:ListGroupMembershipsForMember",
        "identitystore:DescribeGroup"
      ],
      "Resource": "*"
    }
  ]
}
```

## Teams and the `airflow:TeamNames` condition key
<a name="iic-team-based-access"></a>

The `airflow:TeamNames` condition key contains the display names of the IAM Identity Center groups that the user belongs to. It's available whether or not the environment has teams, but it works differently in each case:
+ **Environments with teams** – Apache Airflow isolates DAGs, connections, and variables by team automatically. Each team maps to the IAM Identity Center group whose display name matches the team name. You don't need `airflow:TeamNames` conditions for this isolation. A policy can narrow access further, but it can't give a user access to a team they don't belong to.
+ **Environments without teams** – Use `airflow:TeamNames` to restrict access by IAM Identity Center group membership, as shown in the *Restrict by team* example in [Configuring access with Permission Sets](#iic-integration-permission-sets).

For more information, see [Multi-team environments](multi-team-environments.md).

## Logging in to Apache Airflow with IAM Identity Center
<a name="iic-integration-login"></a>

### Accessing the Apache Airflow UI
<a name="iic-integration-login-access"></a>

There are two ways to access the Apache Airflow UI when IAM Identity Center integration is enabled:

Amazon MWAA console link  
Choose **Open Airflow UI** on the environment page in the Amazon MWAA console. This path requires your IAM Identity Center Permission Set to include the following IAM statement, which grants access to the Amazon MWAA console:  

```
{
  "Sid": "AllowMwaaConsoleRead",
  "Effect": "Allow",
  "Action": [
    "airflow:GetEnvironment",
    "airflow:ListEnvironments"
  ],
  "Resource": "*"
}
```
**Console visibility**  
The Amazon MWAA console lists all environments in the account, regardless of whether you have Apache Airflow UI access to each one. Authorization for Apache Airflow resources is enforced only after you open the environment and log in.

Direct Apache Airflow URL  
Administrators can share the direct Apache Airflow URL with users. Users navigate to the URL and the Apache Airflow webserver automatically initiates the IAM Identity Center device code login flow. No Amazon MWAA console access is required. The environment URL has the format: `https://{{<env-id>}}.{{<region>}}.airflow.amazonaws.com/`

**To log in to Apache Airflow using IAM Identity Center**

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console and choose your environment.

1. Choose **Open Airflow UI**.

1. On the device authorization page, note the verification URL and the one-time code (for example, `SMCL-BTVJ`).

1. Open the verification URL in a new browser tab. If you already have an active SSO session, the identity provider authentication step is skipped and you land directly on the code confirmation screen. Otherwise, authenticate with your corporate identity provider.

1. Enter the one-time code and confirm.

1. If you have multiple Permission Sets assigned for this AWS account, select the role for the Permission Set you want to use during this session. If you have only one Permission Set, it is selected automatically and this step is not shown.

1. You are now logged in to the Apache Airflow UI as yourself.

You can also navigate to the Apache Airflow URL directly. Amazon MWAA redirects you to the AWS Console for authentication and then continues with the steps above.

### Session duration
<a name="iic-integration-session"></a>

Session duration is controlled by the Apache Airflow configuration option `aws_mwaa.session_duration_minutes`, the same as non-IAM Identity Center environments. IAM Identity Center credentials are refreshed in the background, so you are not interrupted during an active session.

### Logout
<a name="iic-integration-logout"></a>

Choosing **Sign out** in Apache Airflow ends your Apache Airflow session only. Your IAM Identity Center and corporate identity provider sessions remain active. Re-logging in immediately might complete without re-entering credentials, depending on the identity provider session duration.

To fully sign out of IAM Identity Center, log out from the IAM Identity Center access portal (`https://{{<alias>}}.awsapps.com/start`) or your corporate identity provider portal. Signing out of IAM Identity Center also invalidates your Apache Airflow session.

## Known limitations
<a name="iic-integration-limitations"></a>
+ **One-way enablement.** Once IAM Identity Center integration is enabled on an environment, it cannot be disabled. Use the parallel-environment approach described in [Recommended: create a new environment](#iic-integration-enabling-new-env) for a safe migration path.
+ **Apache Airflow 3.3.1 or later required.** IAM Identity Center integration is not available on earlier Apache Airflow versions. The console version gate enforces this.
+ **Role selection for multi-Permission-Set users.** Users with more than one Permission Set assigned in IAM Identity Center must select a role during login. To eliminate this step, assign a single dedicated Permission Set per user for Amazon MWAA access.

## Troubleshooting
<a name="iic-integration-troubleshooting"></a>

Apache Airflow shows "Unable to start sign-in"  
**Root cause:** The IAM Identity Center configuration on the environment is incorrect. The access portal URL or Identity Store ID is invalid, the IAM Identity Center instance is not reachable, or the OIDC client registration has not completed.  
**Resolution:**  

1. In the Amazon MWAA console, open the environment and verify the **AWS access portal URL** and **Identity Store ID** under **Identity Center configuration** match the values shown in the IAM Identity Center console under **Settings**.

1. If either value is incorrect, use `UpdateEnvironment` to provide the correct values. The update takes 20 to 30 minutes for a forced update.

1. If the values are correct, verify that the IAM Identity Center instance is organization-level and that the Amazon MWAA environment's AWS account is accessible in the IAM Identity Center organization.

User has no roles after IAM Identity Center authentication  
**Root cause:** No Permission Set is assigned to the user for this AWS account in IAM Identity Center.  
**Resolution:** In the IAM Identity Center console, assign the appropriate Permission Set to the user or their group. The change takes effect on the user's next Apache Airflow login, after IAM Identity Center provisions the role.

All Apache Airflow actions denied ("Access Denied")  
**Root cause:** The IAM policies of the selected Permission Set do not include `airflow:AccessAirflowResource`, or condition key values do not match.  
**Resolution:** In the IAM console, find the rendered role of the Permission Set (`AWSReservedSSO_{{<name>}}_{{<id>}}`) and use IAM Policy Simulator to test `airflow:AccessAirflowResource` on the environment ARN. Common mistakes:  
+ Condition value case mismatch (for example, `dag` instead of `DAG`).
+ `StringEquals` used on `airflow:TeamNames` instead of `ForAnyValue:StringEquals`.
+ Policy applied to a different Permission Set than the one the user selected.
+ Only `LIST` granted without `GET` (or vice versa). The home page dashboard widgets use `ResourceAction=GET` with no `ResourceId`; without it, the home page returns 403 even if the DAG list page works. Always grant `"airflow:ResourceAction": ["GET", "LIST"]` together.

DAG list shows zero DAGs, or home page shows "Access Denied"  
**Root cause:** The Permission Set policy is missing `GET`, `LIST`, or both for `airflow:ResourceType=DAG`. The DAG list page uses `ResourceAction=LIST`; home page dashboard widgets use `ResourceAction=GET` with no `ResourceId`. A policy granting only `GET` shows zero DAGs. A policy granting only `LIST` causes a 403 on the home page.  
**Resolution:** Include both `GET` and `LIST` in the `airflow:ResourceAction` condition for any Permission Set that needs DAG access: `"airflow:ResourceAction": ["GET", "LIST"]`.

`airflow:TeamNames` condition not matching  
**Root cause:** Policy uses `StringEquals` (single-value operator) instead of `ForAnyValue:StringEquals` (multi-value operator).  
**Resolution:** Update the policy to use `ForAnyValue:StringEquals` with `airflow:TeamNames` (plural).