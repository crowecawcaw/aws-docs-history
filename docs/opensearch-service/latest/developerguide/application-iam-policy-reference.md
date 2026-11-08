

# IAM policy reference for OpenSearch UI
<a name="application-iam-policy-reference"></a>

The permissions that OpenSearch UI requires fall into two groups: base permissions, which every application requires regardless of authentication method, and permissions that are required only when the application uses AWS IAM Identity Center.

## Base permissions
<a name="application-iam-policy-reference-base"></a>

The following table lists the application management actions and the resources that each one applies to.


| Action | Purpose | Resource | 
| --- | --- | --- | 
| es:CreateApplication | Create an application | The application ARN, with a wildcard | 
| es:GetApplication | View application details in the AWS Management Console | The ARN of a specific application | 
| es:UpdateApplication | Modify application settings | The ARN of a specific application | 
| es:DeleteApplication | Delete an application | The ARN of a specific application | 
| es:ListApplications | List applications | The application ARN, with a wildcard | 

The following table lists the tag management actions.


| Action | Purpose | 
| --- | --- | 
| es:AddTags | Add tags to an application | 
| es:ListTags | List the tags on an application | 
| es:RemoveTags | Remove tags from an application | 

The following table lists the actions for associating data sources and accessing their data.


| Action | Purpose | 
| --- | --- | 
| aoss:BatchGetCollection | Associate serverless collections | 
| es:DescribeDomain | Associate OpenSearch domains | 
| es:GetDirectQueryDataSource | Associate direct query data sources | 
| opensearch:ApplicationAccessAll | Access the application interface | 
| aoss:APIAccessAll | Access data in a serverless collection | 
| es:ESHttp\* | Access data in a domain over HTTP | 
| opensearch:\*DirectQuery\* | Access direct query data sources | 

OpenSearch UI also requires `iam:CreateServiceLinkedRole` on `arn:aws:iam::*:role/aws-service-role/opensearchservice.amazonaws.com/*`, which allows OpenSearch UI to publish metrics to Amazon CloudWatch.

## Permissions for AWS IAM Identity Center
<a name="application-iam-policy-reference-idc"></a>

Add the following permissions, on top of the base permissions, when the application uses AWS IAM Identity Center.


| Action | Purpose | 
| --- | --- | 
| sso:CreateApplication | Register the application with AWS IAM Identity Center | 
| sso:DeleteApplication | Remove the registration | 
| sso:PutApplicationGrant | Configure grants for the application | 
| sso:PutApplicationAuthenticationMethod | Set the authentication method | 
| sso:PutApplicationAccessScope | Configure access scopes | 
| sso:PutApplicationAssignmentConfiguration | Configure user assignment settings | 
| sso:CreateApplicationAssignment | Assign a user or a group to the application | 
| sso:ListApplicationAssignments | Review the users and groups assigned to the application | 
| sso:DeleteApplicationAssignment | Remove a user or a group from the application | 
| sso:GetApplicationGrant | Read the grant configuration | 
| sso:ListInstances | List the AWS IAM Identity Center instances in the account | 
| iam:PassRole | Pass the IAM role to the AWS IAM Identity Center application | 
| iam:CreateRole | Create the IAM role, if you create a new one | 
| iam:AttachRolePolicy | Attach policies to the role | 

## Minimum policy to access an application
<a name="application-iam-policy-reference-minimum"></a>

The following IAM policy grants a user access to an OpenSearch UI application. Replace the placeholder values with your own information:

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

To scope the policy to a single application, replace the wildcard with the application ID.

## Policy for an administrator who uses AWS IAM Identity Center
<a name="application-iam-policy-reference-admin"></a>

The following IAM policy covers creating and managing applications with AWS IAM Identity Center. Replace the placeholder values with your own information, and scope the resources as narrowly as your use case allows:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ApplicationManagement",
            "Effect": "Allow",
            "Action": [
                "es:CreateApplication",
                "es:GetApplication",
                "es:UpdateApplication",
                "es:DeleteApplication",
                "es:ListApplications",
                "es:AddTags",
                "es:ListTags",
                "es:RemoveTags"
            ],
            "Resource": "arn:aws:opensearch:{{region}}:{{account-id}}:application/*"
        },
        {
            "Sid": "DataSourceAccess",
            "Effect": "Allow",
            "Action": [
                "aoss:BatchGetCollection",
                "es:DescribeDomain",
                "es:GetDirectQueryDataSource"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ApplicationUIAccess",
            "Effect": "Allow",
            "Action": "opensearch:ApplicationAccessAll",
            "Resource": "arn:aws:opensearch:{{region}}:{{account-id}}:application/*"
        },
        {
            "Sid": "IdentityCenterIntegration",
            "Effect": "Allow",
            "Action": [
                "sso:CreateApplication",
                "sso:DeleteApplication",
                "sso:PutApplicationGrant",
                "sso:PutApplicationAuthenticationMethod",
                "sso:PutApplicationAccessScope",
                "sso:PutApplicationAssignmentConfiguration",
                "sso:CreateApplicationAssignment",
                "sso:ListApplicationAssignments",
                "sso:DeleteApplicationAssignment",
                "sso:GetApplicationGrant",
                "sso:ListInstances"
            ],
            "Resource": "*"
        },
        {
            "Sid": "PassRoleForIdentityCenter",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{account-id}}:role/{{role-name}}"
        },
        {
            "Sid": "CreateRoleForIdentityCenter",
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:iam::{{account-id}}:role/{{role-name}}"
        },
        {
            "Sid": "ServiceLinkedRole",
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/opensearchservice.amazonaws.com/*"
        }
    ]
}
```

## Common mistakes
<a name="application-iam-policy-reference-mistakes"></a>

The following table lists common permission mistakes and how to correct them.


| Mistake | Why it fails | Correct action | 
| --- | --- | --- | 
| Using es:ApplicationLogin | This action does not grant access to the interface | Use opensearch:ApplicationAccessAll | 
| Using aoss:DashboardsAccessAll | It requires a resource of \*, which is broader than necessary | Use opensearch:ApplicationAccessAll with a scoped resource | 
| Omitting iam:PassRole when you configure AWS IAM Identity Center | The IAM role cannot be associated with the AWS IAM Identity Center application | Add iam:PassRole, scoped to the role ARN | 