

# Using IAM Identity Center with Amazon Managed Workflows for Apache Airflow

When you enable IAM Identity Center integration, Amazon Managed Workflows for Apache Airflow uses IAM Identity Center to authenticate and authorize you. Sign in to the Apache Airflow UI with your corporate identity provider through the IAM Identity Center device code flow. Amazon MWAA evaluates authorization per request using IAM policies attached to IAM Identity Center Permission Sets.

**Regional availability**  
Amazon MWAA is gradually releasing IAM Identity Center integration to AWS Regions. If the feature isn't available in your Region yet, the Amazon MWAA console doesn't show the **Identity Center configuration** section, and you can't enable IAM Identity Center integration from the console.

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
+ The IAM Identity Center instance must be in the same AWS Region as the Amazon MWAA environment. If the IAM Identity Center instance is in a different Region, users can't sign in to the Apache Airflow UI. For more information, see [Troubleshooting](#iic-integration-troubleshooting).
+ IAM Identity Center integration works with both the public network and private network access modes. If your environment uses a private Apache Airflow webserver, the Amazon VPC must allow the webserver to reach the following IAM Identity Center endpoints. For each endpoint, create the Amazon VPC endpoint, or give the webserver outbound internet access through a NAT gateway. In the following list, {{region}} is the AWS Region of your IAM Identity Center instance, which is the same Region as your environment. For more information about access modes, see [Apache Airflow access modes](configuring-networking.md).
  + `oidc.{{region}}.amazonaws.com` (Amazon VPC endpoint service name `com.amazonaws.{{region}}.sso-oidc`), for the device code sign-in.
  + `portal.sso.{{region}}.amazonaws.com` (Amazon VPC endpoint service name `com.amazonaws.{{region}}.sso`), to get the credentials for your Permission Set role.
  + `identitystore.{{region}}.amazonaws.com` (Amazon VPC endpoint service name `com.amazonaws.{{region}}.identitystore`), to look up your user name and group memberships.

  Amazon MWAA already provides the connectivity for authorization checks, so you don't need to configure anything for them.

## How it works
<a name="iic-integration-how-it-works"></a>

When you open the Apache Airflow UI, Amazon MWAA displays a sign-in page that starts the IAM Identity Center device code flow. You complete authentication in a separate browser tab using your corporate credentials, and confirm a one-time code. After successful authentication, Amazon MWAA obtains temporary IAM Identity Center credentials scoped to your assigned Permission Set and grants you access to the Apache Airflow UI.

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

To enable IAM Identity Center on an existing environment using the Amazon MWAA console, open the **Update environment** wizard. Expand the **Identity Center configuration** section (visible only for environments on Apache Airflow 3.3.1 or later, in AWS Regions where IAM Identity Center integration is available) and provide the access portal URL and Identity Store ID fields. For field descriptions, refer to [Step two: Configure advanced settings](create-environment.md#create-environment-start-advanced). 

To enable IAM Identity Center using the AWS CLI:

```shell
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
Every Permission Set policy must include the following `identitystore` statement. Amazon MWAA needs it to look up your display name and group memberships; without it, sign-in fails. In the following statement, replace these values:  
{{idc-account-id}} – The ID of the AWS account that contains your IAM Identity Center instance.
{{d-1234567890}} – Your Identity Store ID. This is the same Identity Store ID that you configure on the environment.

```json
{
  "Sid": "AllowIdentityStoreLookup",
  "Effect": "Allow",
  "Action": [
    "identitystore:GetUserId",
    "identitystore:DescribeUser",
    "identitystore:ListGroupMembershipsForMember",
    "identitystore:DescribeGroup"
  ],
  "Resource": [
    "arn:aws:identitystore::{{idc-account-id}}:identitystore/{{d-1234567890}}",
    "arn:aws:identitystore:::user/*",
    "arn:aws:identitystore:::group/*",
    "arn:aws:identitystore:::membership/*"
  ]
}
```
The identity store ARN must match your identity store exactly. If the account ID or the identity store ID is wrong, or if you omit the ARN, sign-in fails. The identity store ARN is the only resource in this statement that you can scope to your identity store. User, group, and membership ARNs in IAM Identity Center don't include an account ID or identity store ID (for example, `arn:aws:identitystore:::user/{{user-id}}`), so you can't narrow them to a single identity store.  
Don't replace these wildcards with specific user or group ARNs. At each sign-in, Amazon MWAA looks up the signed-in user and every group that the user belongs to. If a user or group isn't listed in the policy, the lookup fails, which can prevent the user from signing in or from getting access to their teams.

**Additional requirements when your IAM Identity Center identity store uses a customer managed AWS KMS key**  
If your IAM Identity Center identity store is encrypted with a customer managed AWS KMS key, complete two additional steps. Without them, the `identitystore` API calls that look up your display name and group memberships fail during sign-in with the error: "Could not look up your user information from IAM Identity Center."  
To check whether your identity store uses a customer managed AWS KMS key, open the IAM Identity Center console, choose **Settings**, then **Management**. If the console shows a AWS KMS key ARN on **Key for encrypting IAM Identity Center data at rest**, complete both of the following steps. If the default AWS managed key is shown, you do not need to make any additional changes.  
**Step 1: Add AWS KMS permissions to every Permission Set inline policy.** The Permission Set role makes direct `identitystore` API calls using your federated credentials. The following IAM inline policy statement grants the Permission Set role permission to decrypt data using your AWS KMS key. Add it to the inline policy, replacing the placeholder values with your AWS KMS key ARN:  

```json
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

```json
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

```json
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
      "Resource": [
        "arn:aws:identitystore::{{idc-account-id}}:identitystore/{{d-1234567890}}",
        "arn:aws:identitystore:::user/*",
        "arn:aws:identitystore:::group/*",
        "arn:aws:identitystore:::membership/*"
      ]
    }
  ]
}
```

**Example Restrict to DAG read access (list and view)**  <a name="iic-policy-example-dag-read"></a>
Always include `LIST` alongside `GET`. The DAG list page uses `ResourceAction=LIST`; a policy that grants only `GET` shows zero DAGs.  

```json
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
      "Resource": [
        "arn:aws:identitystore::{{idc-account-id}}:identitystore/{{d-1234567890}}",
        "arn:aws:identitystore:::user/*",
        "arn:aws:identitystore:::group/*",
        "arn:aws:identitystore:::membership/*"
      ]
    }
  ]
}
```

**Example Restrict to a specific DAG**  <a name="iic-policy-example-specific-dag"></a>
Use two separate statements. The first allows `GET` and `LIST` without a `ResourceId`. This is required for the DAG list page (`LIST`) and for home page dashboard widgets that query run counts and metrics across all DAGs (`GET` with no DAG ID). The second allows all actions on the specific DAG identified by `ResourceId`. Do not combine `ResourceId` with `LIST` in the same `StringEquals` block, because `LIST` calls do not supply a `ResourceId` and the condition never matches.  

```json
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
      "Resource": [
        "arn:aws:identitystore::{{idc-account-id}}:identitystore/{{d-1234567890}}",
        "arn:aws:identitystore:::user/*",
        "arn:aws:identitystore:::group/*",
        "arn:aws:identitystore:::membership/*"
      ]
    }
  ]
}
```

**Example Restrict by team using `airflow:TeamNames`**  <a name="iic-policy-example-team-names"></a>
Use `ForAnyValue:StringEquals` (the multi-value operator) for `airflow:TeamNames`. This condition matches if the user belongs to *any* of the listed groups (OR logic). Using the single-value `StringEquals` operator causes the condition to never match when a user belongs to more than one team.  

```json
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
      "Resource": [
        "arn:aws:identitystore::{{idc-account-id}}:identitystore/{{d-1234567890}}",
        "arn:aws:identitystore:::user/*",
        "arn:aws:identitystore:::group/*",
        "arn:aws:identitystore:::membership/*"
      ]
    }
  ]
}
```

## Teams and the `airflow:TeamNames` condition key
<a name="iic-team-based-access"></a>

The `airflow:TeamNames` condition key contains the display names of the IAM Identity Center groups that the user belongs to. It's available whether or not the environment has teams, but it works differently in each case:
+ **Environments with teams** – Apache Airflow isolates DAGs, connections, and variables by team automatically. Each team maps to the IAM Identity Center group whose display name matches the team name. You don't need `airflow:TeamNames` conditions for this isolation. A policy can narrow access further, but it can't give a user access to a team they don't belong to. This isolation applies to users in the Apache Airflow UI and API. It doesn't separate DAG code from different teams. For more information, see [Security considerations for DAG authors](multi-team-environments.md#multi-team-concepts-security).
+ **Environments without teams** – Use `airflow:TeamNames` to restrict access by IAM Identity Center group membership, as shown in the *Restrict by team* example in [Configuring access with Permission Sets](#iic-integration-permission-sets).

For more information, see [Multi-team environments](multi-team-environments.md).

## Logging in to Apache Airflow with IAM Identity Center
<a name="iic-integration-login"></a>

### Accessing the Apache Airflow UI
<a name="iic-integration-login-access"></a>

There are two ways to access the Apache Airflow UI when IAM Identity Center integration is enabled:

Amazon MWAA console link  
Choose **Open Airflow UI** on the environment page in the Amazon MWAA console. This path requires your IAM Identity Center Permission Set to include the following IAM statements, which grant access to the Amazon MWAA console. Replace the Region, account ID, and environment name in the environment ARN with your own values:  

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowMwaaConsoleGetEnvironment",
      "Effect": "Allow",
      "Action": "airflow:GetEnvironment",
      "Resource": "arn:aws:airflow:{{us-east-1}}:{{123456789012}}:environment/{{my-env}}"
    },
    {
      "Sid": "AllowMwaaConsoleListEnvironments",
      "Effect": "Allow",
      "Action": "airflow:ListEnvironments",
      "Resource": "*"
    }
  ]
}
```
To allow access to more than one environment, add each environment ARN to the `Resource` element of the `GetEnvironment` statement. The `ListEnvironments` action doesn't support resource-level permissions, so its statement must use `"Resource": "*"`. This statement lets the user list environment names in the account. It doesn't grant access to environment details or to the Apache Airflow UI.  
**Console visibility**  
The Amazon MWAA console lists all environments in the account, regardless of whether you have Apache Airflow UI access to each one. Authorization for Apache Airflow resources is enforced only after you open the environment and log in.

Direct Apache Airflow URL  
Administrators can share the direct Apache Airflow URL with users. Users navigate to the URL and the Apache Airflow webserver automatically initiates the IAM Identity Center device code login flow. No Amazon MWAA console access is required. The environment URL has the format: `https://{{<env-id>}}.{{<region>}}.airflow.amazonaws.com/`

**To log in to Apache Airflow using IAM Identity Center**

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console and choose your environment.

1. Choose **Open Airflow UI**.

1. On the **Sign in to Airflow** page, choose **Sign in with IAM Identity Center**.

   Note the one-time code on the page (for example, `SMCL-BTVJ`), and keep this browser tab open.

1. Choose **Open Identity Provider**. The IAM Identity Center access portal opens in a new browser tab. If you already have an active SSO session, IAM Identity Center skips the identity provider sign-in. Otherwise, sign in with your corporate identity provider.

1. In the IAM Identity Center access portal, check that the code matches the one-time code on the **Sign in to Airflow** page, and then confirm the request.
**Important**  
Confirm the code only if you started this sign-in yourself and the codes match. If the codes don't match, or you didn't start a sign-in, don't confirm the request.

1. Return to the **Sign in to Airflow** tab, and wait while IAM Identity Center verifies the code. The page redirects you automatically.

1. If you have multiple Permission Sets assigned for this AWS account, the **Select Your Role** page appears. Select the role for the Permission Set that you want to use during this session, and then choose **Continue**. If you have only one Permission Set, Amazon MWAA selects it automatically and this page doesn't appear.

1. You are now logged in to the Apache Airflow UI as yourself.

If you open the direct Apache Airflow URL instead, the Apache Airflow webserver starts the IAM Identity Center device code login flow, and you don't need Amazon MWAA console access. Skip the first two steps and continue from the **Sign in to Airflow** page.

### Session duration
<a name="iic-integration-session"></a>

Two independent settings determine how long a sign-in lasts:
+ **Apache Airflow session duration** – The `aws_mwaa.session_duration_minutes` Apache Airflow configuration option sets how long each sign-in lasts in your browser. The default is 720 minutes (12 hours). You can lower or raise it by setting the option on your environment. For example, set it to `60` for one-hour sessions. For more information, see [Using Apache Airflow configuration options on Amazon MWAA](configuring-env-variables.md).
+ **Permission Set session duration** – You set this in IAM Identity Center when you create the Permission Set. It limits how long Amazon MWAA can renew your IAM Identity Center credentials in the background. When the Permission Set session ends, you sign in again, regardless of the Apache Airflow session duration.

While your Permission Set session is active, Amazon MWAA renews your IAM Identity Center credentials in the background, so you aren't interrupted. If you set the Apache Airflow session duration longer than the Permission Set session duration, the longer value has no effect. You are redirected to sign in when the Permission Set session ends.

### Logout
<a name="iic-integration-logout"></a>

Choosing **Sign out** in Apache Airflow ends your Apache Airflow session only. Your IAM Identity Center and corporate identity provider sessions remain active. Re-logging in immediately might complete without re-entering credentials, depending on the identity provider session duration.

To fully sign out of IAM Identity Center, log out from the IAM Identity Center access portal (`https://{{<alias>}}.awsapps.com/start`) or your corporate identity provider portal. Signing out of IAM Identity Center also invalidates your Apache Airflow session.

## Known limitations
<a name="iic-integration-limitations"></a>
+ **One-way enablement.** Once IAM Identity Center integration is enabled on an environment, it cannot be disabled. Use the parallel-environment approach described in [Recommended: create a new environment](#iic-integration-enabling-new-env) for a safe migration path.
+ **Apache Airflow 3.3.1 or later required.** IAM Identity Center integration is not available on earlier Apache Airflow versions. The console version gate enforces this.
+ **Same Region required.** The IAM Identity Center instance must be in the same AWS Region as the Amazon MWAA environment. Cross-Region IAM Identity Center instances aren't supported.
+ **Role selection for multi-Permission-Set users.** Users with more than one Permission Set assigned in IAM Identity Center must select a role during login. To eliminate this step, assign a single dedicated Permission Set per user for Amazon MWAA access.
+ **`InvokeRestApi` is not supported.** On environments with IAM Identity Center integration enabled, calls to the Amazon MWAA `InvokeRestApi` operation return an error. This affects programmatic access to the Apache Airflow REST API through the AWS CLI or AWS SDKs, such as scripts and CI/CD pipelines that start DAG runs, check DAG run status, or retrieve task logs.

  You can still perform these actions through the Apache Airflow UI. If your workflows depend on programmatic access to the Apache Airflow REST API, keep those workflows on an environment without IAM Identity Center integration enabled.

  IAM Identity Center integration cannot be disabled after you enable it. Evaluate this limitation before you enable IAM Identity Center on an existing environment.

## Troubleshooting
<a name="iic-integration-troubleshooting"></a>

Sign-in shows "Could not connect to AWS IAM Identity Center. This is likely a temporary issue. Please try again."  
**Root cause:** Amazon MWAA can't reach the IAM Identity Center instance configured on the environment. The most common cause is that the IAM Identity Center instance is in a different AWS Region than the Amazon MWAA environment. IAM Identity Center integration requires both to be in the same Region, and retrying doesn't help in this case. On an environment with a private Apache Airflow webserver, the Amazon VPC might also not allow the webserver to communicate with IAM Identity Center. A temporary network or service issue can also cause this error. If the connection is lost while you wait for the sign-in to complete, the page shows "An error occurred. Please restart the sign-in process." instead.  
**Resolution:**  

1. In the IAM Identity Center console, check which AWS Region your IAM Identity Center instance is in, and compare it with the Region of the Amazon MWAA environment.

1. If the Regions are different, create an Amazon MWAA environment with IAM Identity Center integration in the same Region as your IAM Identity Center instance. Before you start, review the considerations in [Recommended: create a new environment](#iic-integration-enabling-new-env).

1. If the Regions match and your environment uses a private Apache Airflow webserver, search the `airflow-{{environment-name}}-WebServer` log group for `StartDeviceAuthorization request failed`. If you find it, check that the Amazon VPC allows the webserver to reach `oidc.{{region}}.amazonaws.com`. Create the Amazon VPC endpoint `com.amazonaws.{{region}}.sso-oidc`, or give the webserver outbound internet access through a NAT gateway. Also check your route tables, security groups, and network ACLs.

1. If the Regions match and the network allows access, wait a few minutes and try to sign in again. If the error continues, verify the access portal URL and Identity Store ID as described in the next entry, and then contact AWS Support.

Apache Airflow shows "Unable to start sign-in"  
**Root cause:** The IAM Identity Center configuration on the environment is incorrect. The access portal URL or Identity Store ID is invalid, the IAM Identity Center instance is not reachable, or the OIDC client registration has not completed.  
**Resolution:**  

1. In the Amazon MWAA console, open the environment and verify the **AWS access portal URL** and **Identity Store ID** under **Identity Center configuration** match the values shown in the IAM Identity Center console under **Settings**.

1. If either value is incorrect, use `UpdateEnvironment` to provide the correct values. The update takes 20 to 30 minutes for a forced update.

1. If the values are correct, verify that the IAM Identity Center instance is organization-level and that the Amazon MWAA environment's AWS account is accessible in the IAM Identity Center organization.

User has no roles after IAM Identity Center authentication  
After you authenticate, Apache Airflow shows "Your account does not have access to this Airflow environment. Contact your administrator."  
**Root cause:** One of the following:  
+ No Permission Set is assigned to the user for this AWS account in IAM Identity Center.
+ The environment uses a private Apache Airflow webserver, and the Amazon VPC doesn't allow the webserver to reach `portal.sso.{{region}}.amazonaws.com`. The webserver can't get the list of roles or their credentials, so the sign-in looks the same as a missing assignment.
**Resolution:**  

1. In the IAM Identity Center console, assign the appropriate Permission Set to the user or their group. The change takes effect on the user's next Apache Airflow login, after IAM Identity Center provisions the role.

1. If the Permission Set is already assigned and your environment uses a private Apache Airflow webserver, search the `airflow-{{environment-name}}-WebServer` log group for `GetRoleCredentials failed`. If you find it, create the Amazon VPC endpoint `com.amazonaws.{{region}}.sso`, or give the webserver outbound internet access through a NAT gateway.

Sign-in fails with "An internal error occurred" after you select a role  
**Root cause:** The environment uses a private Apache Airflow webserver, and the Amazon VPC doesn't allow the webserver to reach `identitystore.{{region}}.amazonaws.com`. Amazon MWAA can get your role credentials, but can't look up your user name and group memberships. If the lookup is denied instead, the error is "Could not look up your user information from IAM Identity Center". For that error, see the `identitystore` permissions in [Configuring access with Permission Sets](#iic-integration-permission-sets).  
**Resolution:** Search the `airflow-{{environment-name}}-WebServer` log group for `identitystore lookup failed`. If you find it, create the Amazon VPC endpoint `com.amazonaws.{{region}}.identitystore`, or give the webserver outbound internet access through a NAT gateway.

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