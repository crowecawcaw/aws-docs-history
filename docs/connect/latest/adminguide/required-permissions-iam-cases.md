

# Required permissions for using custom IAM policies to manage Connect Customer Cases

If you're using custom IAM policies to manage access to the Connect Customer Cases, your users need some or all of the permissions listed in this article, depending on the tasks they need to do.

## View Cases domain details
<a name="view-cases-domain-iam"></a>

There are two options for granting users IAM permissions to view Cases domain details on the Connect Customer console.

### Option 1: Minimum required IAM permissions
<a name="option1-view-cases-domain-iam"></a>

To view Cases domain details in the Connect Customer console, users must have the following IAM permissions:
+ `connect:ListInstances`
+ `ds:DescribeDirectories`
+ `connect:ListIntegrationAssociations`
+ `cases:GetDomain`

Following is a sample IAM policy with these permissions:

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowsViewingConnectConsole",
            "Effect": "Allow",
            "Action": [
                "connect:ListInstances",
                "ds:DescribeDirectories"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ListIntegrationAssociations",
            "Effect": "Allow",
            "Action": [
                "connect:ListIntegrationAssociations"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CasesGetDomain",
            "Effect": "Allow",
            "Action": [
                "cases:GetDomain"
            ],
            "Resource": "*"
        }
    ]
}
```

------

Note the following:
+ `cases:GetDomain` Action is required on Resource `*`
+ `connect:ListIntegrationAssociations` action supports the `instance` resource type. See the table in [Actions defined by Connect Customer](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html#amazonconnect-actions-as-permissions).

### Option 2: Update the existing Connect Customer policy with `cases:GetDomain` and `profile:SearchProfiles`
<a name="option2-view-cases-domain-iam"></a>

Include the [AmazonConnectReadOnlyAccess](security-iam-amazon-connect-permissions.md#amazonconnectreadonlyaccesspolicy) policy, and add `cases:GetDomain`, as shown in the following example. 

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CasesGetDomain",
            "Effect": "Allow",
            "Action": [
                "cases:GetDomain"
            ],
            "Resource": "*"
        }        
    ]
}
```

------

## Onboard to Cases
<a name="onboard-cases-iam"></a>

There are two options for granting users IAM permissions to onboard to Cases using the Connect Customer console.

### Option 1: Minimum required permissions
<a name="option1-onboard-cases-iam"></a>

To onboard to Cases by using the Connect Customer console, users must have the following IAM permissions:
+ `connect:ListInstances`
+ `ds:DescribeDirectories`
+ `connect:ListIntegrationAssociations`
+ `cases:GetDomain`
+ `cases:CreateDomain`
+ `connect:CreateIntegrationAssociation`
+ `connect:DescribeInstance`
+ `iam:PutRolePolicy`
+ `profile:SearchProfiles`

Following is a sample IAM policy with these permissions:

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowsViewingConnectConsole",
            "Effect": "Allow",
            "Action": [
                "connect:ListInstances",
                "ds:DescribeDirectories"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ListIntegrationAssociations",
            "Effect": "Allow",
            "Action": [
                "connect:ListIntegrationAssociations"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CasesGetDomain",
            "Effect": "Allow",
            "Action": [
                "cases:GetDomain"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CasesCreateDomain",
            "Effect": "Allow",
            "Action": [
                "cases:CreateDomain"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CreateIntegrationAssociationsAndDependencies",
            "Effect": "Allow",
            "Action": [
                "connect:CreateIntegrationAssociation",
                "connect:DescribeInstance"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AttachAnyPolicyToAmazonConnectRole",
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws:iam::*:role/aws-service-role/connect.amazonaws.com/AWSServiceRoleForAmazonConnect*"
        },
        {
            "Sid": "ProfileSearchProfiles",
            "Effect": "Allow",
            "Action": [
                "profile:SearchProfiles"
            ],
            "Resource": "*"
        }
    ]
}
```

------

Note the following:
+ `cases:GetDomain` Action is required on Resource `*`
+ You can scope the permissions to specific Connect Customer tasks by using the information in [Actions, resources, and condition keys for Connect Customer](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html).
+ `profile:SearchProfiles` Action is required because the `CreateCase` API calls the `SearchProfiles` API to search for customer profiles to validate against, and then associate the profile with the case.

### Option 2: Use a combination of existing policies
<a name="option2-onboard-cases-iam"></a>

The following combination of policies will also work:
+ **AmazonConnect\_FullAccess** policy
+ `iam:PutRolePolicy` to modify the service-linked role. For an example, see [AWS managed policy: AmazonConnect\_FullAccess policy](security-iam-amazon-connect-permissions.md#amazonconnectfullaccesspolicy). 
+ The following IAM policy:

------
#### [ JSON ]

****  

  ```json
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "CasesGetDomain",
              "Effect": "Allow",
              "Action": [
                  "cases:GetDomain",
                  "cases:CreateDomain"
              ],
              "Resource": "*"
          },
          {
              "Sid": "ProfileSearchProfiles",
              "Effect": "Allow",
              "Action": [
                  "profile:SearchProfiles"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

------

## Enable Cases when you create an instance
<a name="instance-creation-cases-iam"></a>

To enable Cases on the **Data storage** step of instance creation, users need the permissions for creating an instance in [Connect Customer console home page](security-iam-amazon-connect-permissions.md#console-home-page-permissions), plus the following permissions for the options they select.


| Option selected | Additional permissions | 
| --- | --- | 
| Enable Cases | `cases:CreateDomain`<br />`cases:GetDomain`<br />`connect:CreateIntegrationAssociation` | 
| Enable Cases event streams | `cases:PutCaseEventConfiguration`<br />`app-integrations:CreateEventIntegration`<br />`app-integrations:GetEventIntegration`<br />`connect:CreateIntegrationAssociation` | 
| Enable Cases event streams with Customer Profiles enabled | `events:CreateEventBus`<br />`events:DescribeRule`<br />`events:PutRule`<br />`events:PutTargets`<br />`iam:CreateRole`<br />`iam:CreatePolicy`<br />`iam:PassRole`<br />`app-integrations:CreateEventIntegration`<br />`app-integrations:GetEventIntegration`<br />`profile:PutIntegration` | 

Note the following:
+ `cases:PutCaseEventConfiguration` sets the event configuration to include all case fields. The user's policy must allow the action on the domain's field resource, `arn:aws:cases:{{region}}:{{account-id}}:domain/{{domain-id}}/field/*`. If the policy allows only specific fields, the request fails with an `AccessDeniedException`.
+ Scope `iam:PassRole` to `arn:aws:iam::{{account-id}}:role/service-role/AmazonConnectCasesEventBridgeRole-*` and add the condition `iam:PassedToService` = `events.amazonaws.com`.

## View and configure Cases integrations
<a name="configure-cases-integrations-iam"></a>

To view integration status on the **Cases** page, users need the permissions in [View Cases domain details](#view-cases-domain-iam), plus the following:
+ `cases:GetCaseEventConfiguration`
+ `events:DescribeRule`
+ `events:DescribeEventBus`
+ `app-integrations:GetEventIntegration`
+ `profile:ListAccountIntegrations`
+ `profile:ListIntegrations`
+ `profile:GetIntegration`

To choose **Configure**, users also need the permissions in [Enable Cases when you create an instance](#instance-creation-cases-iam) for the integration that they configure, except `cases:CreateDomain`.