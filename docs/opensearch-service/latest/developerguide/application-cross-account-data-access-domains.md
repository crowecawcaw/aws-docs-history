# Cross-account data access to OpenSearch domains

You can configure your OpenSearch UI applications in one account to access
OpenSearch domains in different accounts. When you create an OpenSearch UI application
with cross-account data sources, you provide an `iamRoleForDataSourceArn`
that points to an IAM role in the target account. OpenSearch UI validates the request
by assuming this role and calling `es:DescribeDomain` to verify domain
accessibility. The cross-account role is used only during data source association. Data
plane access is controlled separately by the target domain's access policy.

Cross-account data source support requires fine-grained access control to be
enabled on the target domain. Fine-grained access control provides an additional
authorization layer beyond the domain access policy, allowing you to control access to
individual indices, documents, and fields.

## Key concepts

Source account

The AWS account that hosts your OpenSearch UI application.

Target account

The AWS account where the OpenSearch domain resides.

Cross-account role

An IAM role in the target account that is used during data source
association only. OpenSearch UI assumes this role to call
`es:DescribeDomain`, which retrieves the domain endpoint and
verifies that fine-grained access control is enabled. This is a discovery
and validation step, not a security boundary. The cross-account role is
never used for data plane access. After association, all data plane
requests are authorized by the domain's access policy and backend role
mappings, independent of the cross-account role.

IAM Identity Center application role

An IAM role in the source account that is used for IAM Identity Center user data
plane access.

## How cross-account role assumption works

When you create or update an OpenSearch UI application with a cross-account data
source, OpenSearch UI assumes the cross-account role in the target account using
Forwarded Access Sessions ([FAS](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md")). FAS propagates the calling principal's own IAM
identity to the `sts:AssumeRole` call. This means:

- The target account's trust policy controls which source account principals
  can assume the cross-account role.
- The assumed role session carries the identity of the caller who initiated
  the `CreateApplication` or `UpdateApplication`
  request.
- The cross-account role is assumed only during association to call
  `es:DescribeDomain`. It is not used for any subsequent data plane
  operations.

For data plane access:

- IAM users sign requests with their own IAM credentials. The target
  domain's access policy authorizes these requests directly.
- IAM Identity Center users have their requests signed with the IAM Identity Center application role
  (`iamRoleForIdentityCenterApplicationArn`) in the source account.
  The target domain's access policy and backend role mappings authorize these
  requests.

## Prerequisites

Before you set up cross-account data access, ensure that you have the
following:

- AWS CLI installed and configured
- Access to both the source and target AWS accounts
- OpenSearch domains with [fine-grained access control](fgac.md "fgac.md") enabled.
  Cross-account data source association is not supported for domains without
  fine-grained access control.
- For IAM Identity Center flows: An AWS IAM Identity Center organization instance

## Scenarios

Choose the scenario that matches your authentication method and domain
configuration:

- [Scenario 1: IAM user accessing a public domain](#cross-account-scenario-1 "#cross-account-scenario-1")
- [Scenario 2: IAM Identity Center user accessing a public domain](#cross-account-scenario-2 "#cross-account-scenario-2")
- [Scenario 3: IAM user accessing a VPC domain](#cross-account-scenario-3 "#cross-account-scenario-3")
- [Scenario 4: IAM Identity Center user accessing a VPC domain](#cross-account-scenario-4 "#cross-account-scenario-4")

## Scenario 1: IAM user accessing a public domain

### Step 1: Create the cross-account IAM role (target account)

Create an IAM role in the target account that allows the source account to
assume it for domain validation.

###### To create the cross-account role

1. Create a trust policy that allows the source account to assume the
   role:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::`source-account-id`:root"
    },
    "Action": "sts:AssumeRole"
  }]
}
```

2. Create the role:

```
aws iam create-role \
  --role-name `OpenSearchUIAccessRole` \
  --assume-role-policy-document file://`trust-policy.json`
```

3. Create a permissions policy with only the
   `es:DescribeDomain` action:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "es:DescribeDomain",
    "Resource": "arn:aws:es:`region`:`target-account-id`:domain/*"
  }]
}
```

4. Attach the permissions policy to the role:

```
aws iam put-role-policy \
  --role-name `OpenSearchUIAccessRole` \
  --policy-name `ValidationOnly` \
  --policy-document file://`permissions-policy.json`
```

### Step 2: Create the OpenSearch domain (target account)

Create an OpenSearch domain in the target account with fine-grained access
control and encryption enabled:

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
  --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::`source-account-id`:root"},"Action":"es:ESHttp*","Resource":"arn:aws:es:`region`:`target-account-id`:domain/`domain-name`/*"}]}' \
  --region `region`
```

###### Note

This access policy scopes data plane access to IAM principals from the
source account. For more restrictive access, replace the account root
principal with specific IAM user or role ARNs. Fine-grained access control
provides an additional authorization layer for controlling access to
indices and documents.

Wait for the domain status to become `Active` before
proceeding.

### Step 3: Create the OpenSearch UI application (source account)

Create the application in the source account with the cross-account data
source:

```
aws opensearch create-application \
  --region `region` \
  --name "`cross-account-iam-app`" \
  --data-sources '[{
    "dataSourceArn":"arn:aws:es:`region`:`target-account-id`:domain/`domain-name`",
    "dataSourceDescription":"`Cross-account domain`",
    "iamRoleForDataSourceArn":"arn:aws:iam::`target-account-id`:role/`OpenSearchUIAccessRole`"
  }]' \
  --app-configs '[{"key":"opensearchDashboards.dashboardAdmin.users","value":"[\"*\"]"}]'
```

### Step 4: Verify and access

Retrieve the application details to get the endpoint URL:

```
aws opensearch get-application \
  --region `region` \
  --id `application-id`
```

- Navigate to the application endpoint URL from the response.
- Sign in with IAM credentials.
- The IAM user signs data plane requests with their own
  credentials.
- The target domain access policy controls what data the user can
  access.

## Scenario 2: IAM Identity Center user accessing a public domain

### Step 1: Create the cross-account IAM role (target account)

Create an IAM role in the target account that allows the source account to
assume it for domain validation.

###### To create the cross-account role

1. Create a trust policy that allows the source account to assume the
   role:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::`source-account-id`:root"
    },
    "Action": "sts:AssumeRole"
  }]
}
```

2. Create the role:

```
aws iam create-role \
  --role-name `OpenSearchUIAccessRole` \
  --assume-role-policy-document file://`trust-policy.json`
```

3. Create a permissions policy with only the
   `es:DescribeDomain` action:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "es:DescribeDomain",
    "Resource": "arn:aws:es:`region`:`target-account-id`:domain/*"
  }]
}
```

4. Attach the permissions policy to the role:

```
aws iam put-role-policy \
  --role-name `OpenSearchUIAccessRole` \
  --policy-name `ValidationOnly` \
  --policy-document file://`permissions-policy.json`
```

### Step 2: Create the OpenSearch domain (target account)

Create an OpenSearch domain in the target account. Use the same command as
[Step 2: Create the OpenSearch domain (target account)](#scenario-1-step-2 "#scenario-1-step-2"), but update the access policy to allow the
IAM Identity Center application role from the source account:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::`source-account-id`:role/`NeoIdCAppRole`"
    },
    "Action": "es:ESHttp*",
    "Resource": "arn:aws:es:`region`:`target-account-id`:domain/`domain-name`/*"
  }]
}
```

Wait for the domain status to become `Active` before
proceeding.

### Step 3: Create the IAM role for IAM Identity Center application (source account)

Create an IAM role in the source account that OpenSearch UI uses for
IAM Identity Center user data plane access.

###### To create the IAM Identity Center application role

1. Create a trust policy:

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

2. Create a permissions policy:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "OpenSearchDomain",
    "Effect": "Allow",
    "Action": ["es:ESHttp*"],
    "Resource": "*"
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

### Step 4: Create the OpenSearch UI application with IAM Identity Center (source account)

```
aws opensearch create-application \
  --region `region` \
  --name "`cross-account-idc-app`" \
  --iam-identity-center-options '{
    "enabled":true,
    "iamIdentityCenterInstanceArn":"arn:aws:sso:::instance/ssoins-`instance-id`",
    "iamRoleForIdentityCenterApplicationArn":"arn:aws:iam::`source-account-id`:role/`NeoIdCAppRole`"
  }' \
  --data-sources '[{
    "dataSourceArn":"arn:aws:es:`region`:`target-account-id`:domain/`domain-name`",
    "dataSourceDescription":"`Cross-account domain`",
    "iamRoleForDataSourceArn":"arn:aws:iam::`target-account-id`:role/`OpenSearchUIAccessRole`"
  }]' \
  --app-configs '[{"key":"opensearchDashboards.dashboardAdmin.users","value":"[\"*\"]"}]'
```

### Step 5: Create and assign IAM Identity Center users and groups

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
  --application-arn "arn:aws:sso:::`source-account-id`:application/ssoins-`instance-id`/apl-`application-id`" \
  --principal-id `user-id-or-group-id` \
  --principal-type `USER`
```

###### Configure backend role mapping on the target domain

Map the IAM Identity Center group to an OpenSearch security role on the target
domain:

```
curl -XPUT "https://`domain-endpoint`/_plugins/_security/api/rolesmapping/all_access" \
  -u `admin`:`master-password` \
  -H 'Content-Type: application/json' \
  -d '{
    "backend_roles": ["`group-id`"],
    "hosts": [],
    "users": []
  }'
```

### Step 6: Verify and access

```
aws opensearch get-application \
  --region `region` \
  --id `application-id`
```

- Navigate to the application endpoint URL.
- Sign in with IAM Identity Center user credentials.
- IAM Identity Center users' data requests are signed with the IAM Identity Center application role,
  not the cross-account role.
- Backend role mappings on the domain control data access
  permissions.

## Scenario 3: IAM user accessing a VPC domain

### Step 1: Create the cross-account IAM role (target account)

Create an IAM role in the target account that allows the source account to
assume it for domain validation.

###### To create the cross-account role

1. Create a trust policy that allows the source account to assume the
   role:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::`source-account-id`:root"
    },
    "Action": "sts:AssumeRole"
  }]
}
```

2. Create the role:

```
aws iam create-role \
  --role-name `OpenSearchUIAccessRole` \
  --assume-role-policy-document file://`trust-policy.json`
```

3. Create a permissions policy with only the
   `es:DescribeDomain` action:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "es:DescribeDomain",
    "Resource": "arn:aws:es:`region`:`target-account-id`:domain/*"
  }]
}
```

4. Attach the permissions policy to the role:

```
aws iam put-role-policy \
  --role-name `OpenSearchUIAccessRole` \
  --policy-name `ValidationOnly` \
  --policy-document file://`permissions-policy.json`
```

### Step 2: Set up the VPC (target account)

Skip this step if a VPC already exists in the target account.

```
# Create VPC
aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --region `region`

# Create subnet
aws ec2 create-subnet \
  --vpc-id `vpc-id` \
  --cidr-block 10.0.1.0/24 \
  --availability-zone `region`a \
  --region `region`

# Create security group
aws ec2 create-security-group \
  --group-name `opensearch-vpc-sg` \
  --description "Security group for OpenSearch VPC domain" \
  --vpc-id `vpc-id` \
  --region `region`

# Allow inbound HTTPS
aws ec2 authorize-security-group-ingress \
  --group-id `security-group-id` \
  --protocol tcp \
  --port 443 \
  --cidr 10.0.0.0/16 \
  --region `region`
```

Learn more about [VPC domain creation](vpc.md "vpc.md").

### Step 3: Create the VPC domain (target account)

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
  --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::`source-account-id`:root"},"Action":"es:ESHttp*","Resource":"arn:aws:es:`region`:`target-account-id`:domain/`vpc-domain-name`/*"}]}' \
  --region `region`
```

###### Note

This access policy scopes data plane access to IAM principals from the
source account. For more restrictive access, replace the account root
principal with specific IAM user or role ARNs. Fine-grained access control
provides an additional authorization layer for controlling access to
indices and documents.

Wait for the domain status to become `Active` before
proceeding.

### Step 4: Authorize the VPC endpoint for the OpenSearch UI service principal (target account)

###### Important

This is a critical step that is unique to VPC domains. The OpenSearch UI
service must be explicitly authorized to access the VPC endpoint.

```
# Authorize the service principal
aws opensearch authorize-vpc-endpoint-access \
  --domain-name `vpc-domain-name` \
  --service "application.opensearchservice.amazonaws.com" \
  --region `region`

# Verify authorization
aws opensearch list-vpc-endpoint-access \
  --domain-name `vpc-domain-name` \
  --region `region`
```

Expected response:

```
{
  "AuthorizedPrincipalList": [
    {
      "PrincipalType": "AWS_SERVICE",
      "Principal": "application.opensearchservice.amazonaws.com"
    }
  ]
}
```

### Step 5: Create the OpenSearch UI application (source account)

```
aws opensearch create-application \
  --region `region` \
  --name "`cross-account-vpc-iam-app`" \
  --data-sources '[{
    "dataSourceArn":"arn:aws:es:`region`:`target-account-id`:domain/`vpc-domain-name`",
    "dataSourceDescription":"`Cross-account VPC domain`",
    "iamRoleForDataSourceArn":"arn:aws:iam::`target-account-id`:role/`OpenSearchUIAccessRole`"
  }]' \
  --app-configs '[{"key":"opensearchDashboards.dashboardAdmin.users","value":"[\"*\"]"}]'
```

### Step 6: Verify and access

Retrieve the application details to get the endpoint URL:

```
aws opensearch get-application \
  --region `region` \
  --id `application-id`
```

- Navigate to the application endpoint URL from the response.
- Sign in with IAM credentials.
- The IAM user signs data plane requests with their own
  credentials.
- The target domain access policy controls what data the user can
  access.

## Scenario 4: IAM Identity Center user accessing a VPC domain

### Step 1: Create the cross-account IAM role (target account)

Create an IAM role in the target account that allows the source account to
assume it for domain validation.

###### To create the cross-account role

1. Create a trust policy that allows the source account to assume the
   role:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::`source-account-id`:root"
    },
    "Action": "sts:AssumeRole"
  }]
}
```

2. Create the role:

```
aws iam create-role \
  --role-name `OpenSearchUIAccessRole` \
  --assume-role-policy-document file://`trust-policy.json`
```

3. Create a permissions policy with only the
   `es:DescribeDomain` action:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "es:DescribeDomain",
    "Resource": "arn:aws:es:`region`:`target-account-id`:domain/*"
  }]
}
```

4. Attach the permissions policy to the role:

```
aws iam put-role-policy \
  --role-name `OpenSearchUIAccessRole` \
  --policy-name `ValidationOnly` \
  --policy-document file://`permissions-policy.json`
```

### Step 2: Set up the VPC (target account)

Skip this step if a VPC already exists in the target account.

```
# Create VPC
aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --region `region`

# Create subnet
aws ec2 create-subnet \
  --vpc-id `vpc-id` \
  --cidr-block 10.0.1.0/24 \
  --availability-zone `region`a \
  --region `region`

# Create security group
aws ec2 create-security-group \
  --group-name `opensearch-vpc-sg` \
  --description "Security group for OpenSearch VPC domain" \
  --vpc-id `vpc-id` \
  --region `region`

# Allow inbound HTTPS
aws ec2 authorize-security-group-ingress \
  --group-id `security-group-id` \
  --protocol tcp \
  --port 443 \
  --cidr 10.0.0.0/16 \
  --region `region`
```

Learn more about [VPC domain creation](vpc.md "vpc.md").

### Step 3: Create the VPC domain (target account)

Use the same command as [Step 3: Create the VPC domain (target account)](#scenario-3-step-3 "#scenario-3-step-3"), but update the
access policy to allow the IAM Identity Center application role from the source account:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::`source-account-id`:role/`NeoIdCAppRole`"
    },
    "Action": "es:ESHttp*",
    "Resource": "arn:aws:es:`region`:`target-account-id`:domain/`vpc-domain-name`/*"
  }]
}
```

Wait for the domain status to become `Active` before
proceeding.

### Step 4: Authorize the VPC endpoint for the OpenSearch UI service principal (target account)

###### Important

This is a critical step that is unique to VPC domains. The OpenSearch UI
service must be explicitly authorized to access the VPC endpoint.

```
# Authorize the service principal
aws opensearch authorize-vpc-endpoint-access \
  --domain-name `vpc-domain-name` \
  --service "application.opensearchservice.amazonaws.com" \
  --region `region`

# Verify authorization
aws opensearch list-vpc-endpoint-access \
  --domain-name `vpc-domain-name` \
  --region `region`
```

Expected response:

```
{
  "AuthorizedPrincipalList": [
    {
      "PrincipalType": "AWS_SERVICE",
      "Principal": "application.opensearchservice.amazonaws.com"
    }
  ]
}
```

### Step 5: Create the IAM role for IAM Identity Center application (source account)

Create an IAM role in the source account that OpenSearch UI uses for
IAM Identity Center user data plane access.

###### To create the IAM Identity Center application role

1. Create a trust policy:

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

2. Create a permissions policy:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "OpenSearchDomain",
    "Effect": "Allow",
    "Action": ["es:ESHttp*"],
    "Resource": "*"
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

### Step 6: Create the OpenSearch UI application with IAM Identity Center (source account)

```
aws opensearch create-application \
  --region `region` \
  --name "`cross-account-vpc-idc-app`" \
  --iam-identity-center-options '{
    "enabled":true,
    "iamIdentityCenterInstanceArn":"arn:aws:sso:::instance/ssoins-`instance-id`",
    "iamRoleForIdentityCenterApplicationArn":"arn:aws:iam::`source-account-id`:role/`NeoIdCAppRole`"
  }' \
  --data-sources '[{
    "dataSourceArn":"arn:aws:es:`region`:`target-account-id`:domain/`vpc-domain-name`",
    "dataSourceDescription":"`Cross-account VPC domain`",
    "iamRoleForDataSourceArn":"arn:aws:iam::`target-account-id`:role/`OpenSearchUIAccessRole`"
  }]' \
  --app-configs '[{"key":"opensearchDashboards.dashboardAdmin.users","value":"[\"*\"]"}]'
```

### Step 7: Create and assign IAM Identity Center users and groups

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
  --application-arn "arn:aws:sso:::`source-account-id`:application/ssoins-`instance-id`/apl-`application-id`" \
  --principal-id `user-id-or-group-id` \
  --principal-type `USER`
```

###### Configure backend role mapping on the target domain

Map the IAM Identity Center group to an OpenSearch security role on the target
domain:

```
curl -XPUT "https://`domain-endpoint`/_plugins/_security/api/rolesmapping/all_access" \
  -u `admin`:`master-password` \
  -H 'Content-Type: application/json' \
  -d '{
    "backend_roles": ["`group-id`"],
    "hosts": [],
    "users": []
  }'
```

### Step 8: Verify and access

```
aws opensearch get-application \
  --region `region` \
  --id `application-id`
```

- Navigate to the application endpoint URL.
- Sign in with IAM Identity Center user credentials.
- IAM Identity Center users' data requests are signed with the IAM Identity Center application role,
  not the cross-account role.
- Backend role mappings on the domain control data access
  permissions.

## Managing applications

###### Update an application with cross-account data sources

Run the following command. Replace the `placeholder
 values` with your own information.

```
aws opensearch update-application \
  --region `region` \
  --id `application-id` \
  --data-sources '[{
    "dataSourceArn":"arn:aws:es:`region`:`target-account-id`:domain/`domain-1`",
    "dataSourceDescription":"`First cross-account domain`",
    "iamRoleForDataSourceArn":"arn:aws:iam::`target-account-id`:role/`OpenSearchUIAccessRole`"
  },{
    "dataSourceArn":"arn:aws:es:`region`:`target-account-id`:domain/`domain-2`",
    "dataSourceDescription":"`Second cross-account domain`",
    "iamRoleForDataSourceArn":"arn:aws:iam::`target-account-id`:role/`OpenSearchUIAccessRole`"
  }]'
```

###### Important

The update operation replaces the entire data sources array. Include all data
sources that you want to keep.

###### List applications

Run the following command:

```
aws opensearch list-applications \
  --region `region`
```

###### Delete an application

Run the following command:

```
aws opensearch delete-application \
  --region `region` \
  --id `application-id`
```

###### Revoke VPC endpoint access

Run the following command:

```
aws opensearch revoke-vpc-endpoint-access \
  --domain-name `vpc-domain-name` \
  --service "application.opensearchservice.amazonaws.com" \
  --region `region`
```

## Quick reference

The following tables summarize the key differences between domain types and
authentication methods.

Public domain compared to VPC domain| Aspect | Public domain | VPC domain |
| --- | --- | --- |
| VPC endpoint authorization | Not required | Required – must authorize<br>`application.opensearchservice.amazonaws.com` |
| Network setup | None | VPC, subnet, security group with HTTPS (443) inbound |
| IAM access policy | Required | Required |
| Cross-account role | Required for cross-account | Required for cross-account |

IAM user compared to IAM Identity Center user| Aspect | IAM user | IAM Identity Center user |
| --- | --- | --- |
| Data plane credentials | User's own IAM credentials | IAM Identity Center application role |
| Access control | Domain access policy | Domain access policy and backend role mappings |
| Additional setup | None | IAM Identity Center application role, user/group creation, application<br>assignment, backend role mapping |
| OpenSearch UI application configuration | No IAM Identity Center options | `--iam-identity-center-options` required |

## Important notes

- The `iamRoleForDataSourceArn` must be in the same account as
  the `dataSourceArn`.
- The `iamRoleForDataSourceArn` is only required for
  cross-account data sources. Omit it for same-account data sources.
- The cross-account role only needs the `es:DescribeDomain`
  permission. It is never used for data plane access.
- For VPC domains, both the IAM policy and VPC endpoint authorization
  must be configured.
- Supported engine versions: OpenSearch 1.3 and above.
- Cross-account data source association requires fine-grained access control
  to be enabled on the target domain.

## Troubleshooting

| Issue                                                     | Resolution                                                                                                                                                        |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Application creation fails with "Unable to access domain" | Verify that the cross-account role has the<br>`es:DescribeDomain` permission and that the trust policy<br>allows the source account.                              |
| VPC domain association fails                              | Ensure that the VPC endpoint is authorized for<br>`application.opensearchservice.amazonaws.com`.                                                                  |
| Data plane access denied for IAM user                     | Check that the target domain access policy allows the IAM<br>user or role principal.                                                                              |
| Data plane access denied for IAM Identity Center user     | Verify that the backend role mapping includes the IAM Identity Center group<br>ID, and that the domain policy allows the IAM Identity Center application<br>role. |
| Account mismatch error                                    | Ensure that `iamRoleForDataSourceArn` is in the same<br>account as the domain in `dataSourceArn`.                                                                 |
