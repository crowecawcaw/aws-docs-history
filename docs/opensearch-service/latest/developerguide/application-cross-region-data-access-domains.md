# Cross-region data access to OpenSearch domains

You can configure your OpenSearch UI applications in one AWS Region to access
OpenSearch domains in different AWS Regions. This enables you to create unified
dashboards that aggregate data from OpenSearch domains across multiple AWS Regions
within the same partition. Cross-region data source support requires fine-grained access
control to be enabled on the target domain. Fine-grained access control provides an additional
authorization layer beyond the domain access policy, allowing you to control access to
individual indices, documents, and fields.

## Key concepts

Application Region

The AWS Region where your OpenSearch UI application is
hosted.

Target Region

The AWS Region where the OpenSearch domain resides. This can be
any Region within the same partition, regardless of whether
OpenSearch UI is available in that Region.

Cross-account role

An IAM role in the target account that is used during data source
association only. OpenSearch UI assumes this role to call
`es:DescribeDomain`, which retrieves the domain endpoint and
verifies that fine-grained access control is enabled. This role is only
required when the domain is in a different account from the application.
For more information, see [Cross-account data access to OpenSearch domains](application-cross-account-data-access-domains.md "application-cross-account-data-access-domains.md").

IAM Identity Center application role

An IAM role in the application account that is used for IAM Identity Center user
data plane access.

Supported Regions (for VPC domains)

For VPC domains, you must allowlist the AWS Regions where your
OpenSearch UI applications are hosted when authorizing the VPC
endpoint. This allowlisting is required so that OpenSearch UI can
make calls to the VPC domain.

## Prerequisites

Before you set up cross-region data access, ensure that you have the
following:

- AWS CLI installed and configured
- Access to the AWS account in both the application Region and the target
  Region
- OpenSearch domains with fine-grained access control enabled.
  Multi-region data source association is only supported for domains with
  fine-grained access control enabled.
- For cross-account scenarios: Access to both the source and target
  AWS accounts
- For IAM Identity Center flows: An AWS IAM Identity Center organization instance. The OpenSearch UI
  application must be in the same Region as the IAM Identity Center instance.

## Scenarios

Choose the scenario that matches your authentication method and domain
configuration:

- [Scenario 1: IAM user accessing a public domain in a different Region](#cross-region-scenario-1 "#cross-region-scenario-1")
- [Scenario 2: IAM Identity Center user accessing a public domain in a different Region](#cross-region-scenario-2 "#cross-region-scenario-2")
- [Scenario 3: IAM user accessing a VPC domain in a different Region](#cross-region-scenario-3 "#cross-region-scenario-3")
- [Scenario 4: IAM Identity Center user accessing a VPC domain in a different Region](#cross-region-scenario-4 "#cross-region-scenario-4")

Each scenario covers same-account cross-region access. For cross-account
cross-region access, combine the steps in these scenarios with the cross-account
role setup described in [Cross-account data access to OpenSearch domains](application-cross-account-data-access-domains.md "application-cross-account-data-access-domains.md").

## Scenario 1: IAM user accessing a public domain in a different Region

In this scenario, you create an OpenSearch UI application in one Region and
connect it to a public OpenSearch domain in a different Region within the same
account.

### Step 1: Create the OpenSearch domain (target Region)

Create an OpenSearch domain in the target Region with fine-grained access
control enabled. Scope the access policy to the account root or specific IAM
principals.

```
aws opensearch create-domain \
  --domain-name `domain-name` \
  --engine-version OpenSearch_2.19 \
  --cluster-config InstanceType=m5.large.search,InstanceCount=1 \
  --ebs-options "EBSEnabled=true,VolumeType=gp3,VolumeSize=100" \
  --advanced-security-options '{"Enabled":true,"InternalUserDatabaseEnabled":true,"MasterUserOptions":{"MasterUserName":"`admin`","MasterUserPassword":"`master-password`"}}' \
  --node-to-node-encryption-options '{"Enabled":true}' \
  --encryption-at-rest-options '{"Enabled":true}' \
  --domain-endpoint-options '{"EnforceHTTPS":true,"TLSSecurityPolicy":"Policy-Min-TLS-1-2-2019-07"}' \
  --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::`account-id`:root"},"Action":"es:ESHttp*","Resource":"arn:aws:es:`target-region`:`account-id`:domain/`domain-name`/*"}]}' \
  --region `target-region`
```

Wait for the domain status to become `Active` before
proceeding.

### Step 2: Create the OpenSearch UI application (application Region)

Create the application in the application Region with the cross-region data
source. The Region is extracted from the data source ARN
automatically.

```
aws opensearch create-application \
  --region `application-region` \
  --name "`cross-region-iam-app`" \
  --data-sources '[{
    "dataSourceArn":"arn:aws:es:`target-region`:`account-id`:domain/`domain-name`",
    "dataSourceDescription":"`Cross-region domain`"
  }]' \
  --app-configs '[{"key":"opensearchDashboards.dashboardAdmin.users","value":"[\"`test-user`\"]"}]'
```

### Step 3: Verify and access

Retrieve the application details to get the endpoint URL:

```
aws opensearch get-application \
  --region `application-region` \
  --id `application-id`
```

- Navigate to the application endpoint URL from the response.
- Sign in with IAM credentials.
- The IAM user signs data plane requests with their own
  credentials.
- The target domain's access policy and backend role mappings control
  what data the user can access.

## Scenario 2: IAM Identity Center user accessing a public domain in a different Region

In this scenario, you create an OpenSearch UI application with IAM Identity Center
authentication in one Region and connect it to a public OpenSearch domain in a
different Region within the same account.

### Step 1: Create the OpenSearch domain with IAM Identity Center enabled (target Region)

Create an OpenSearch domain in the target Region with fine-grained access
control and IAM Identity Center integration enabled. Use the
`--identity-center-options` parameter with
`IdentityCenterInstanceRegion` to specify the Region where your
IAM Identity Center instance is located. This Region should be the same as where the
OpenSearch UI application is hosted.

```
aws opensearch create-domain \
  --domain-name `domain-name` \
  --engine-version OpenSearch_2.19 \
  --cluster-config InstanceType=m5.large.search,InstanceCount=1 \
  --ebs-options "EBSEnabled=true,VolumeType=gp3,VolumeSize=100" \
  --advanced-security-options '{"Enabled":true,"InternalUserDatabaseEnabled":true,"MasterUserOptions":{"MasterUserName":"`admin`","MasterUserPassword":"`master-password`"}}' \
  --node-to-node-encryption-options '{"Enabled":true}' \
  --encryption-at-rest-options '{"Enabled":true}' \
  --domain-endpoint-options '{"EnforceHTTPS":true,"TLSSecurityPolicy":"Policy-Min-TLS-1-2-2019-07"}' \
  --identity-center-options '{"EnabledAPIAccess":true,"IdentityCenterInstanceARN":"arn:aws:sso:::instance/ssoins-`instance-id`","IdentityCenterInstanceRegion":"`idc-region`","RolesKey":"GroupId","SubjectKey":"UserId"}' \
  --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::`account-id`:role/`NeoIdCAppRole`"},"Action":"es:ESHttp*","Resource":"arn:aws:es:`target-region`:`account-id`:domain/`domain-name`/*"}]}' \
  --region `target-region`
```

Wait for the domain status to become `Active` before
proceeding.

### Step 2: Create the IAM role for IAM Identity Center application

Create an IAM role that OpenSearch UI uses for IAM Identity Center user data plane
access.

###### To create the IAM Identity Center application role

1. Create a trust policy with only the
   `sts:AssumeRole` statement. You will update this policy to
   add the `sts:SetContext` statement after creating the
   application in the next step.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "application.opensearchservice.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

2. Create a permissions policy:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "OpenSearchDomain",
    "Effect": "Allow",
    "Action": ["es:ESHttp*"],
    "Resource": "arn:aws:es:`target-region`:`account-id`:domain/`domain-name`/*"
  }]
}
```

3. Create the role and attach the policies:

```
aws iam create-role \
  --role-name `NeoIdCAppRole` \
  --assume-role-policy-document file://`neoidc-trust-policy.json`

aws iam put-role-policy \
  --role-name `NeoIdCAppRole` \
  --policy-name `NeoIdCAppPermissions` \
  --policy-document file://`neoidc-permissions-policy.json`
```

### Step 3: Create the OpenSearch UI application with IAM Identity Center (application Region)

###### Note

Ensure that the IAM Identity Center instance is located in the same Region as the
OpenSearch UI application Region.

```
aws opensearch create-application \
  --region `application-region` \
  --name "`cross-region-idc-app`" \
  --iam-identity-center-options '{
    "enabled":true,
    "iamIdentityCenterInstanceArn":"arn:aws:sso:::instance/ssoins-`instance-id`",
    "iamRoleForIdentityCenterApplicationArn":"arn:aws:iam::`account-id`:role/`NeoIdCAppRole`"
  }' \
  --data-sources '[{
    "dataSourceArn":"arn:aws:es:`target-region`:`account-id`:domain/`domain-name`",
    "dataSourceDescription":"`Cross-region domain`"
  }]' \
  --app-configs '[{"key":"opensearchDashboards.dashboardAdmin.users","value":"[\"`test-user`\"]"}]'
```

After the application is created, note the SSO application ID from the
response. Then update the trust policy on the IAM Identity Center application role to add
the `sts:SetContext` statement:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "application.opensearchservice.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    },
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "application.opensearchservice.amazonaws.com"
      },
      "Action": "sts:SetContext",
      "Condition": {
        "ForAllValues:ArnEquals": {
          "sts:RequestContextProviders": "arn:aws:iam::aws:contextProvider/IdentityCenter"
        }
      }
    }
  ]
}
```

```
aws iam update-assume-role-policy \
  --role-name `NeoIdCAppRole` \
  --policy-document file://`updated-trust-policy.json`
```

### Step 4: Create and assign IAM Identity Center users and groups

###### Create an IAM Identity Center user

Run the following command. Replace the `placeholder
 values` with your own information.

```
aws identitystore create-user \
  --identity-store-id `d-directory-id` \
  --user-name `user-email` \
  --display-name "`display-name`" \
  --name Formatted=string,FamilyName=`last-name`,GivenName=`first-name` \
  --emails Value=`user-email`,Type=work,Primary=true
```

###### Create an IAM Identity Center group and add the user

Run the following commands:

```
aws identitystore create-group \
  --identity-store-id `d-directory-id` \
  --display-name "`OpenSearchUsers`" \
  --description "`Users with OpenSearch access`"

aws identitystore create-group-membership \
  --identity-store-id `d-directory-id` \
  --group-id `group-id` \
  --member-id UserId=`user-id`
```

###### Assign the user or group to the application

Run the following command:

```
aws sso-admin create-application-assignment \
  --application-arn "arn:aws:sso::`account-id`:application/ssoins-`instance-id`/apl-`application-id`" \
  --principal-id `user-id-or-group-id` \
  --principal-type `USER`
```

###### Configure backend role mapping on the target domain

Map the IAM Identity Center group to an OpenSearch security role on the target
domain:

```
curl -XPATCH "https://`domain-endpoint`/_plugins/_security/api/rolesmapping/all_access" \
  -u `admin`:`master-password` \
  -H 'Content-Type: application/json' \
  -d '[{"op": "add", "path": "/backend_roles", "value": ["`group-id`"]}]'
```

### Step 5: Verify and access

Retrieve the application details to get the endpoint URL:

```
aws opensearch get-application \
  --region `application-region` \
  --id `application-id`
```

- Navigate to the application endpoint URL.
- Sign in with IAM Identity Center user credentials.
- IAM Identity Center users' data requests are signed with the IAM Identity Center application
  role.
- Backend role mappings on the domain control data access
  permissions.

## Scenario 3: IAM user accessing a VPC domain in a different Region

In this scenario, you create an OpenSearch UI application in one Region and
connect it to a VPC OpenSearch domain in a different Region within the same
account. VPC domains require additional network configuration and explicit VPC
endpoint authorization with cross-region support.

### Step 1: Set up the VPC (target Region)

Skip this step if a VPC already exists in the target Region.

```
# Create VPC
aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --region `target-region`

# Create subnet
aws ec2 create-subnet \
  --vpc-id `vpc-id` \
  --cidr-block 10.0.1.0/24 \
  --availability-zone `target-region`a \
  --region `target-region`

# Create security group
aws ec2 create-security-group \
  --group-name `opensearch-vpc-sg` \
  --description "Security group for OpenSearch VPC domain" \
  --vpc-id `vpc-id` \
  --region `target-region`

# Allow inbound HTTPS
aws ec2 authorize-security-group-ingress \
  --group-id `security-group-id` \
  --protocol tcp \
  --port 443 \
  --cidr 10.0.0.0/16 \
  --region `target-region`
```

Learn more about [VPC domain creation](vpc.md "vpc.md").

### Step 2: Create the VPC domain (target Region)

```
aws opensearch create-domain \
  --domain-name `vpc-domain-name` \
  --engine-version OpenSearch_2.19 \
  --cluster-config InstanceType=m5.large.search,InstanceCount=1 \
  --ebs-options "EBSEnabled=true,VolumeType=gp3,VolumeSize=100" \
  --vpc-options "SubnetIds=`subnet-id`,SecurityGroupIds=`security-group-id`" \
  --advanced-security-options '{"Enabled":true,"InternalUserDatabaseEnabled":true,"MasterUserOptions":{"MasterUserName":"`admin`","MasterUserPassword":"`master-password`"}}' \
  --node-to-node-encryption-options '{"Enabled":true}' \
  --encryption-at-rest-options '{"Enabled":true}' \
  --domain-endpoint-options '{"EnforceHTTPS":true,"TLSSecurityPolicy":"Policy-Min-TLS-1-2-2019-07"}' \
  --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::`account-id`:root"},"Action":"es:ESHttp*","Resource":"arn:aws:es:`target-region`:`account-id`:domain/`vpc-domain-name`/*"}]}' \
  --region `target-region`
```

Wait for the domain status to become `Active` before
proceeding.

### Step 3: Authorize the VPC endpoint for the OpenSearch UI service principal with cross-region support (target Region)

```
# Authorize the service principal with cross-region support
aws opensearch authorize-vpc-endpoint-access \
  --domain-name `vpc-domain-name` \
  --service "application.opensearchservice.amazonaws.com" \
  --service-options '{"SupportedRegions":["`target-region`","`application-region`"]}' \
  --region `target-region`

# Verify authorization
aws opensearch list-vpc-endpoint-access \
  --domain-name `vpc-domain-name` \
  --region `target-region`
```

Expected response:

```
{
  "AuthorizedPrincipalList": [
    {
      "PrincipalType": "AWS_SERVICE",
      "Principal": "application.opensearchservice.amazonaws.com",
      "ServiceOptions": {
        "SupportedRegions": ["`target-region`", "`application-region`"]
      }
    }
  ]
}
```

### Step 4: Create the OpenSearch UI application (application Region)

```
aws opensearch create-application \
  --region `application-region` \
  --name "`cross-region-vpc-iam-app`" \
  --data-sources '[{
    "dataSourceArn":"arn:aws:es:`target-region`:`account-id`:domain/`vpc-domain-name`",
    "dataSourceDescription":"`Cross-region VPC domain`"
  }]' \
  --app-configs '[{"key":"opensearchDashboards.dashboardAdmin.users","value":"[\"`test-user`\"]"}]'
```

### Step 5: Verify and access

Retrieve the application details to get the endpoint URL:

```
aws opensearch get-application \
  --region `application-region` \
  --id `application-id`
```

- Navigate to the application endpoint URL from the response.
- Sign in with IAM credentials.
- The IAM user signs data plane requests with their own
  credentials.
- The target domain's access policy and backend role mappings control
  what data the user can access.

## Scenario 4: IAM Identity Center user accessing a VPC domain in a different Region

In this scenario, you create an OpenSearch UI application with IAM Identity Center
authentication in one Region and connect it to a VPC OpenSearch domain in a
different Region within the same account.

### Step 1: Set up the VPC (target Region)

Skip this step if a VPC already exists in the target Region.

```
# Create VPC
aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --region `target-region`

# Create subnet
aws ec2 create-subnet \
  --vpc-id `vpc-id` \
  --cidr-block 10.0.1.0/24 \
  --availability-zone `target-region`a \
  --region `target-region`

# Create security group
aws ec2 create-security-group \
  --group-name `opensearch-vpc-sg` \
  --description "Security group for OpenSearch VPC domain" \
  --vpc-id `vpc-id` \
  --region `target-region`

# Allow inbound HTTPS
aws ec2 authorize-security-group-ingress \
  --group-id `security-group-id` \
  --protocol tcp \
  --port 443 \
  --cidr 10.0.0.0/16 \
  --region `target-region`
```

Learn more about [VPC domain creation](vpc.md "vpc.md").

### Step 2: Create the VPC domain with IAM Identity Center enabled (target Region)

Create an OpenSearch domain in the target Region with fine-grained access
control, IAM Identity Center integration, and VPC configuration enabled. Update the access
policy to allow the IAM Identity Center application role and add the
`--identity-center-options` parameter:

```
aws opensearch create-domain \
  --domain-name `vpc-domain-name` \
  --engine-version OpenSearch_2.19 \
  --cluster-config InstanceType=m5.large.search,InstanceCount=1 \
  --ebs-options "EBSEnabled=true,VolumeType=gp3,VolumeSize=100" \
  --vpc-options "SubnetIds=`subnet-id`,SecurityGroupIds=`security-group-id`" \
  --advanced-security-options '{"Enabled":true,"InternalUserDatabaseEnabled":true,"MasterUserOptions":{"MasterUserName":"`admin`","MasterUserPassword":"`master-password`"}}' \
  --node-to-node-encryption-options '{"Enabled":true}' \
  --encryption-at-rest-options '{"Enabled":true}' \
  --domain-endpoint-options '{"EnforceHTTPS":true,"TLSSecurityPolicy":"Policy-Min-TLS-1-2-2019-07"}' \
  --identity-center-options '{"EnabledAPIAccess":true,"IdentityCenterInstanceARN":"arn:aws:sso:::instance/ssoins-`instance-id`","IdentityCenterInstanceRegion":"`idc-region`","RolesKey":"GroupId","SubjectKey":"UserId"}' \
  --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::`account-id`:role/`NeoIdCAppRole`"},"Action":"es:ESHttp*","Resource":"arn:aws:es:`target-region`:`account-id`:domain/`vpc-domain-name`/*"}]}' \
  --region `target-region`
```

Wait for the domain status to become `Active` before
proceeding.

### Step 3: Authorize the VPC endpoint for the OpenSearch UI service principal with cross-region support (target Region)

###### Important

This is a critical step that is unique to VPC domains with cross-region
access. The OpenSearch UI service must be explicitly authorized to access
the VPC endpoint, and you must include the application Region in the
`SupportedRegions` list.

```
# Authorize the service principal with cross-region support
aws opensearch authorize-vpc-endpoint-access \
  --domain-name `vpc-domain-name` \
  --service "application.opensearchservice.amazonaws.com" \
  --service-options '{"SupportedRegions":["`target-region`","`application-region`"]}' \
  --region `target-region`

# Verify authorization
aws opensearch list-vpc-endpoint-access \
  --domain-name `vpc-domain-name` \
  --region `target-region`
```

Expected response:

```
{
  "AuthorizedPrincipalList": [
    {
      "PrincipalType": "AWS_SERVICE",
      "Principal": "application.opensearchservice.amazonaws.com",
      "ServiceOptions": {
        "SupportedRegions": ["`target-region`", "`application-region`"]
      }
    }
  ]
}
```

### Step 4: Create the IAM role for IAM Identity Center application

Create an IAM role that OpenSearch UI uses for IAM Identity Center user data plane
access.

###### To create the IAM Identity Center application role

1. Create a trust policy with only the
   `sts:AssumeRole` statement. You will update this policy to
   add the `sts:SetContext` statement after creating the
   application in the next step.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "application.opensearchservice.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

2. Create a permissions policy:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "OpenSearchDomain",
    "Effect": "Allow",
    "Action": ["es:ESHttp*"],
    "Resource": "arn:aws:es:`target-region`:`account-id`:domain/`vpc-domain-name`/*"
  }]
}
```

3. Create the role and attach the policies:

```
aws iam create-role \
  --role-name `NeoIdCAppRole` \
  --assume-role-policy-document file://`neoidc-trust-policy.json`

aws iam put-role-policy \
  --role-name `NeoIdCAppRole` \
  --policy-name `NeoIdCAppPermissions` \
  --policy-document file://`neoidc-permissions-policy.json`
```

### Step 5: Create the OpenSearch UI application with IAM Identity Center (application Region)

```
aws opensearch create-application \
  --region `application-region` \
  --name "`cross-region-vpc-idc-app`" \
  --iam-identity-center-options '{
    "enabled":true,
    "iamIdentityCenterInstanceArn":"arn:aws:sso:::instance/ssoins-`instance-id`",
    "iamRoleForIdentityCenterApplicationArn":"arn:aws:iam::`account-id`:role/`NeoIdCAppRole`"
  }' \
  --data-sources '[{
    "dataSourceArn":"arn:aws:es:`target-region`:`account-id`:domain/`vpc-domain-name`",
    "dataSourceDescription":"`Cross-region VPC domain`"
  }]' \
  --app-configs '[{"key":"opensearchDashboards.dashboardAdmin.users","value":"[\"`test-user`\"]"}]'
```

After the application is created, note the SSO application ID from the
response. Then update the trust policy on the IAM Identity Center application role to add
the `sts:SetContext` statement:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "application.opensearchservice.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    },
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "application.opensearchservice.amazonaws.com"
      },
      "Action": "sts:SetContext",
      "Condition": {
        "ForAllValues:ArnEquals": {
          "sts:RequestContextProviders": "arn:aws:iam::aws:contextProvider/IdentityCenter"
        }
      }
    }
  ]
}
```

```
aws iam update-assume-role-policy \
  --role-name `NeoIdCAppRole` \
  --policy-document file://`updated-trust-policy.json`
```

### Step 6: Create and assign IAM Identity Center users and groups

Follow the same steps as [Step 4: Create and assign IAM Identity Center users and groups](#cross-region-scenario-2-step-4 "#cross-region-scenario-2-step-4") to create users, groups, assign
them to the application, and configure backend role mapping on the target
domain.

### Step 7: Verify and access

Retrieve the application details to get the endpoint URL:

```
aws opensearch get-application \
  --region `application-region` \
  --id `application-id`
```

- Navigate to the application endpoint URL.
- Sign in with IAM Identity Center user credentials.
- IAM Identity Center users' data requests are signed with the IAM Identity Center application
  role.
- Backend role mappings on the domain control data access
  permissions.

## Managing applications

###### Update an application with cross-region data sources

Run the following command. Replace the `placeholder
 values` with your own information.

```
aws opensearch update-application \
  --region `application-region` \
  --id `application-id` \
  --data-sources '[{
    "dataSourceArn":"arn:aws:es:`target-region-1`:`account-id`:domain/`domain-1`",
    "dataSourceDescription":"`Domain in target Region 1`"
  },{
    "dataSourceArn":"arn:aws:es:`target-region-2`:`account-id`:domain/`domain-2`",
    "dataSourceDescription":"`Domain in target Region 2`"
  }]'
```

###### Important

The update operation replaces the entire data sources array. Include all data
sources that you want to keep.

###### List applications

Run the following command:

```
aws opensearch list-applications \
  --region `application-region`
```

###### Delete an application

Run the following command:

```
aws opensearch delete-application \
  --region `application-region` \
  --id `application-id`
```

###### Revoke VPC endpoint access for specific Regions

To revoke cross-region access for specific AWS Regions while keeping
others, use the `--service-options` parameter with the Regions to
revoke:

```
aws opensearch revoke-vpc-endpoint-access \
  --domain-name `vpc-domain-name` \
  --service "application.opensearchservice.amazonaws.com" \
  --service-options '{"SupportedRegions":["`region-to-revoke`"]}' \
  --region `target-region`
```

## Quick reference

The following tables summarize the key differences between domain types,
authentication methods, and same-region versus cross-region access.

Public domain compared to VPC domain| Aspect | Public domain | VPC domain |
| --- | --- | --- |
| VPC endpoint authorization | Not required | Required – must authorize<br>`application.opensearchservice.amazonaws.com` with<br>`SupportedRegions` |
| Network setup | None | VPC, subnet, security group with HTTPS (443) inbound |
| IAM access policy | Required | Required |

IAM user compared to IAM Identity Center user| Aspect | IAM user | IAM Identity Center user |
| --- | --- | --- |
| Data plane credentials | User's own IAM credentials | IAM Identity Center application role |
| Access control | Domain access policy and backend role mappings | Domain access policy and backend role mappings |
| Application Region constraint | Any Region | Must be in the same Region as the IAM Identity Center instance |
| Domain configuration | Standard | Requires `--identity-center-options` with<br>`IdentityCenterInstanceRegion` |
| Additional setup | None | IAM Identity Center application role, user/group creation, application<br>assignment, backend role mapping |

Same-region compared to cross-region| Aspect | Same-region | Cross-region |
| --- | --- | --- |
| Data source ARN | Same Region as application | Different Region from application (same partition) |
| VPC endpoint authorization | Omit `--service-options` | Include `--service-options` with<br>`SupportedRegions` |
| IAM Identity Center domain configuration | `IdentityCenterInstanceRegion` optional | `IdentityCenterInstanceRegion` required |
| Cross-partition support | N/A | Not supported – data sources must be in the same<br>partition |

## Important notes

- Cross-region data source association requires fine-grained access control
  to be enabled on the target domain.
- Cross-region data sources must be within the same partition.
  Cross-partition access (for example, from `aws` to
  `aws-cn`) is not supported.
- The data source Region is extracted from the data source ARN
  automatically. No additional Region parameter is needed in the
  `CreateApplication` or `UpdateApplication`
  APIs.
- For same-account cross-region data sources,
  `iamRoleForDataSourceArn` is not required. It is only needed
  for cross-account data sources.
- For VPC domains, you must include the application Region in the
  `SupportedRegions` parameter when calling
  `AuthorizeVpcEndpointAccess`. Omitting
  `--service-options` authorizes only same-Region access.
- For IAM Identity Center flows, the OpenSearch UI application must be in the same
  Region as the IAM Identity Center instance.
- For IAM Identity Center flows with cross-region domains, the target domain must
  include `IdentityCenterInstanceRegion` in
  `--identity-center-options` to enable cross-region token
  introspection.
- Supported engine versions: OpenSearch 1.3 and above.

## Troubleshooting

| Issue                                                            | Resolution                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Application creation fails with "Unable to access domain"        | Verify that the domain exists in the target Region and that<br>fine-grained access control is enabled. For cross-account scenarios,<br>verify the cross-account role has the<br>`es:DescribeDomain` permission and the trust policy<br>allows the source account.                     |
| VPC domain access fails for cross-region                         | Ensure that the VPC endpoint is authorized for<br>`application.opensearchservice.amazonaws.com` with the<br>application Region included in<br>`SupportedRegions`.                                                                                                                     |
| Data plane access denied for IAM user                            | Check that the target domain access policy allows the IAM<br>user or role principal, and that the fine-grained access control<br>backend role mappings grant the appropriate permissions.                                                                                             |
| Data plane access denied for IAM Identity Center user            | Verify that the backend role mapping includes the IAM Identity Center group<br>ID, the domain policy allows the IAM Identity Center application role, and<br>`IdentityCenterInstanceRegion` is correctly set to the<br>same Region as the OpenSearch UI application on the<br>domain. |
| Cross-partition data source rejected                             | Cross-partition access is not supported. Ensure the data source<br>ARN is in the same partition as the application.                                                                                                                                                                   |
| IAM Identity Center authentication fails for cross-region domain | Verify that `IdentityCenterInstanceRegion` is set to<br>the correct Region where your IAM Identity Center instance is enabled. The<br>OpenSearch UI application must also be in this same<br>Region.                                                                                  |
