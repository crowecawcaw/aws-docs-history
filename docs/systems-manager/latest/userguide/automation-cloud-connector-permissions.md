

# Permissions for automations that use a Cloud Connector

When an automation targets Microsoft Azure or Google Cloud resources through a Cloud Connector, Automation uses an IAM role (the automation assume role) to reach your Azure or Google Cloud resources, and the person who starts the automation needs IAM permissions to start it and read the connector. Runbook steps that call Azure or Google Cloud also rely on roles that you grant in those clouds. This topic describes each set of permissions.

## Permissions for the automation assume role
<a name="automation-cloud-connector-permissions-assume-role"></a>

When an execution has an `AutomationAssumeRole`, Automation assumes that role, and the role assumes the connector's federation role to obtain Azure or Google Cloud credentials. Automation uses these credentials both to find the resources that the Cloud Connector target matches and when a step calls Azure or Google Cloud. If an execution has no `AutomationAssumeRole`, the identity of the person who starts the automation assumes the federation role instead. There is no fallback between the two.

Use the automation assume role that Systems Manager created when you enabled node management (**Install and configure SSM Agent**) for the connector. Its name uses the pattern `SSM-AzureAssumeRole-{{connector-name}}-{{connector-id-prefix}}` (for Google Cloud, `SSM-GCPAssumeRole-...`), where {{connector-id-prefix}} is the first 8 characters of the connector ID. The role is in the `/service-role/` IAM path and has the tag `caller=SSM`. In the Automation console, the runbook's assume-role input (for example `AutomationAssumeRole`) is filled in with this role when your AWS account has exactly one matching role. For the full trust and permissions policies, see [Automation assume role](cloud-connector-automation-assume-role.md).

Systems Manager creates this role only when you enable node management and keep the default **Automation execution role**. A connector created without node management has no such role. To create it, enable node management for the connector on the **Hybrid and Multicloud nodes** page and keep the default role, or create only the role with the command line. For both methods, see [Create the automation assume role](#automation-cloud-connector-permissions-create-role). You can also use another role, as described later in this topic.

The role works because the connector's federation role trusts roles in the same AWS account whose path is `/service-role/`, whose name starts with `SSM-AzureAssumeRole` or `SSM-AzureDispatchRole` (for Google Cloud, `SSM-GCPAssumeRole` or `SSM-GCPDispatchRole`), and that have the tag `caller=SSM`.

This role already grants what Automation needs for a Cloud Connector target and for runbook steps that call Azure or Google Cloud: `sts:AssumeRole` on the federation role, `ssm:GetCloudConnector` on the connector, and `iam:ListRoleTags` on itself. Automation reads the role's own tags and adds them to the web identity token.

Add permissions to the role for anything else your runbook does on AWS, such as the actions an `aws:executeAwsApi` step calls. An `aws:executeAutomation` step needs `ssm:StartAutomationExecution` and `iam:PassRole`. Rate control needs nothing extra, because Automation starts the child automations itself. To add these permissions, you can attach a customer managed policy to the role. Systems Manager doesn't change the role's policies after it creates the role, so the permissions that you add remain. The following example policy adds `ec2:DescribeInstances`. Its `Resource` is `*` because `ec2:DescribeInstances` doesn't support resource-level permissions.

```json
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeInstances",
            "Resource": "*"
        }
    ]
}
```

**Important**  
Don't rename the role, change its `/service-role/` path, or remove the `caller=SSM` tag. If you do, the federation role stops trusting it.

**Note**  
Keep the role's tags few. For Google Cloud, too many tags cause the error `The tags on role {{arn}} are too large to include in a federation token. Reduce the number or length of tags on that role and retry: {{message}}`.

You can also use another role that the federation role trusts, such as a role that you chose under **Additional trusted roles** when you created the connector. For more information, see [Use another role](#automation-cloud-connector-permissions-other-role).

## Create the automation assume role
<a name="automation-cloud-connector-permissions-create-role"></a>

Systems Manager creates the automation assume role only when you enable node management for the connector and keep the default **Automation execution role**. If you created the connector without node management, or chose your own role when you enabled it, create the role with one of the following methods.

Enable node management (console)  
If node management isn't enabled for the connector, open the connector on the **Hybrid and Multicloud nodes** page of the Systems Manager console, and then choose **Install and configure SSM Agent**. For **Automation execution role**, choose **Create an Automation execution role with recommended permissions**. Systems Manager creates the role with the name, path, tag, and permissions that Automation needs to use the connector.  
Node management also installs SSM Agent on the connector's VMs and registers them as managed nodes, through a State Manager association. For more information, see [Enable VM onboarding](cloud-connector-enable-vm-onboarding.md).

Create only the role (command line)  
To create the role without node management, use the following procedure with the AWS CLI or AWS Tools for PowerShell. The federation role trusts a role by its name only when the role is in the `/service-role/` path, and you can't set a role's path in the IAM console.

**To create the automation assume role (command line)**

1. Install and configure the AWS CLI or the AWS Tools for PowerShell, if you haven't already.

   For information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Installing the AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html).

1. Get the ARN of the connector's federation role. In the Systems Manager console, the connector's page in **Hybrid and Multicloud nodes** shows it as **IAM role**. You can also run the following AWS CLI command. Replace {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} with the connector ID.

------
#### [ Linux & macOS ]

   ```sh
   aws ssm get-cloud-connector \
       --cloud-connector-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
       --query RoleArn \
       --output text
   ```

------
#### [ Windows ]

   ```sh
   aws ssm get-cloud-connector ^
       --cloud-connector-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} ^
       --query RoleArn ^
       --output text
   ```

------

1. Create a file named `trust-policy.json` with the following JSON trust policy. With this policy, Systems Manager can assume the role in your AWS account. Replace `{{111122223333}}` with your AWS account ID.

   ```json
   {
       "Version": "2012-10-17", 		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "sts:AssumeRole",
               "Principal": {
                   "Service": "ssm.amazonaws.com"
               },
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": "111122223333"
                   }
               }
           }
       ]
   }
   ```

1. Create the role in the `/service-role/` path with the tag `caller=SSM`. For an Azure connector, start the role name with `SSM-AzureAssumeRole-`. For a Google Cloud connector, start it with `SSM-GCPAssumeRole-`. To have the Automation console fill in the role, use the pattern `SSM-AzureAssumeRole-{{connector-name}}-{{connector-id-prefix}}`. Here, {{connector-id-prefix}} is the first 8 characters of the connector ID. Replace each {{example resource placeholder}} with your own information.

------
#### [ Linux & macOS ]

   ```sh
   aws iam create-role \
       --role-name {{SSM-AzureAssumeRole-MyConnector-a1b2c3d4}} \
       --path /service-role/ \
       --assume-role-policy-document file://trust-policy.json \
       --tags Key=caller,Value=SSM
   ```

------
#### [ Windows ]

   ```sh
   aws iam create-role ^
       --role-name {{SSM-AzureAssumeRole-MyConnector-a1b2c3d4}} ^
       --path /service-role/ ^
       --assume-role-policy-document file://trust-policy.json ^
       --tags Key=caller,Value=SSM
   ```

------
#### [ PowerShell ]

   ```powershell
   New-IAMRole `
       -RoleName "{{SSM-AzureAssumeRole-MyConnector-a1b2c3d4}}" `
       -Path "/service-role/" `
       -AssumeRolePolicyDocument (Get-Content -Raw trust-policy.json) `
       -Tag @{"Key"="caller";"Value"="SSM"}
   ```

------

1. Create a file named `permissions-policy.json` with the following JSON policy. With this policy, the role can assume the connector's federation role, read the connector, and read its own tags. Replace the `sts:AssumeRole` resource with the federation role ARN from step 2, and `{{us-east-1}}` with the connector's AWS Region. Replace `{{111122223333}}` with your AWS account ID, `{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}` with the connector ID, and `{{SSM-AzureAssumeRole-MyConnector-a1b2c3d4}}` with the name of the role.

   ```json
   {
       "Version": "2012-10-17", 		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "sts:AssumeRole",
               "Resource": "arn:aws:iam::111122223333:role/service-role/SSM-AzureRole-MyConnector"
           },
           {
               "Effect": "Allow",
               "Action": "ssm:GetCloudConnector",
               "Resource": "arn:aws:ssm:us-east-1:111122223333:cloud-connector/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
           },
           {
               "Effect": "Allow",
               "Action": "iam:ListRoleTags",
               "Resource": "arn:aws:iam::111122223333:role/service-role/SSM-AzureAssumeRole-MyConnector-a1b2c3d4"
           }
       ]
   }
   ```

1. Add the policy to the role as an inline policy. Replace each {{example resource placeholder}} with your own information.

------
#### [ Linux & macOS ]

   ```sh
   aws iam put-role-policy \
       --role-name {{SSM-AzureAssumeRole-MyConnector-a1b2c3d4}} \
       --policy-name {{CloudConnectorAccess}} \
       --policy-document file://permissions-policy.json
   ```

------
#### [ Windows ]

   ```sh
   aws iam put-role-policy ^
       --role-name {{SSM-AzureAssumeRole-MyConnector-a1b2c3d4}} ^
       --policy-name {{CloudConnectorAccess}} ^
       --policy-document file://permissions-policy.json
   ```

------
#### [ PowerShell ]

   ```powershell
   Write-IAMRolePolicy `
       -RoleName "{{SSM-AzureAssumeRole-MyConnector-a1b2c3d4}}" `
       -PolicyName "{{CloudConnectorAccess}}" `
       -PolicyDocument (Get-Content -Raw permissions-policy.json)
   ```

------

1. Add the permissions that your runbook needs on AWS, as described in [Permissions for the automation assume role](#automation-cloud-connector-permissions-assume-role).

The person who starts the automation also needs `iam:PassRole` on the role. For more information, see [Permissions for the person who runs the automation](#automation-cloud-connector-permissions-caller).

## Use another role
<a name="automation-cloud-connector-permissions-other-role"></a>

To run an automation with a role other than the one that node management creates, the connector's federation role must trust that role. The federation role that connector setup creates trusts the following roles in the same AWS account:
+ Roles that you chose under **Additional trusted roles** when you created the connector. Connector setup offers this field only when you have it create the federation role. For Azure, see [Set up a Cloud Connector for Microsoft Azure in Systems Manager](systems-manager-cloud-connector.md). For Google Cloud, see [Set up a Cloud Connector for Google Cloud Platform in Systems Manager](systems-manager-cloud-connector-gcp.md).
+ Roles that you add to the federation role's trust policy, as described in the following procedure. Use this method to trust a role after you create the connector.
+ Roles that meet all of the following conditions. To create one, see [Create the automation assume role](#automation-cloud-connector-permissions-create-role).
  + The role's path is `/service-role/`. You can't set a role's path in the IAM console, so create the role with the AWS CLI or an API.
  + The role's name starts with `SSM-AzureAssumeRole` for an Azure connector, or `SSM-GCPAssumeRole` for a Google Cloud connector.
  + The role has the tag `caller=SSM`.
  + The role allows `sts:AssumeRole` on the federation role.

In each case, the role must also trust Systems Manager and allow `ssm:GetCloudConnector` on the connector and `iam:ListRoleTags` on itself. Automation uses the role to call both actions. For an example permissions policy, see the `permissions-policy.json` step in [Create the automation assume role](#automation-cloud-connector-permissions-create-role).

An execution has one `AutomationAssumeRole`. For a runbook that uses both an Azure connector and a Google Cloud connector, both federation roles must trust that role. For example, choose the same role under **Additional trusted roles** for both connectors. The name conditions can't cover both connectors, because no role name can start with both `SSM-AzureAssumeRole` and `SSM-GCPAssumeRole`.

**Important**  
A role that a federation role trusts can get credentials for the connector's Azure subscriptions or Google Cloud projects, and so can anyone who can assume that role. Trust only roles that need that access.

**To add a role to the federation role's trust policy**

1. Find the name of the connector's federation role. In the Systems Manager console, the connector's page in **Hybrid and Multicloud nodes** shows the role's ARN as **IAM role**. The name is the last part of the ARN.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, and then choose the federation role.

1. Choose the **Trust relationships** tab, and then choose **Edit trust policy**.

1. Add the following statement to the `Statement` list, and keep the existing statements. Replace `{{111122223333}}` with your AWS account ID and `{{MyAutomationRole}}` with the name of your role. If the role has a path, include it in the ARN.

   ```json
   {
       "Effect": "Allow",
       "Action": "sts:AssumeRole",
       "Principal": {
           "AWS": "arn:aws:iam::111122223333:role/MyAutomationRole"
       }
   }
   ```

1. Choose **Update policy**.

1. Make sure that your role trusts Systems Manager and has the permissions described earlier in this section.

## Permissions for the person who runs the automation
<a name="automation-cloud-connector-permissions-caller"></a>

The person who starts the automation needs the following permissions.
+ `ssm:StartAutomationExecution` – To start the automation.
+ `iam:PassRole` – To pass the automation assume role to Automation.
+ `ssm:GetCloudConnector` – Automation reads the connector with the caller's credentials.
+ `ssm:DescribeInstanceInformation` – Needed when `SsmManagedNodeFilter` is `MANAGED` or `UNMANAGED`.

The Automation console also uses `ssm:ListCloudConnectors` (for the connector list), `ssm:GetCloudConnector` (for connector details), `ssm:DescribeDocument` (for the runbook's cloud providers), and `iam:ListRoles` (to fill in the assume role). The following example policy grants these permissions. Replace `{{111122223333}}` with your AWS account ID.

```json
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ssm:StartAutomationExecution",
            "Resource": "arn:aws:ssm:*:*:automation-definition/*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::111122223333:role/service-role/SSM-*AssumeRole-*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ssm.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetCloudConnector",
                "ssm:ListCloudConnectors",
                "ssm:DescribeInstanceInformation",
                "ssm:DescribeDocument",
                "iam:ListRoles"
            ],
            "Resource": "*"
        }
    ]
}
```

## Permissions in Azure and Google Cloud
<a name="automation-cloud-connector-permissions-cloud"></a>

Connector setup grants the connector's identity a limited set of permissions in your cloud. Runbook steps that need more fail with an authorization error until you grant more.

For Microsoft Azure, connector setup assigns the connector's Azure application a custom role named `AWSSSMVMExtensionRole-{{subscription-id}}` (or `AWSSSMVMExtensionRole-{{tenant-id}}` on the tenant root management group for a whole-tenant connector). It allows reading VMs and running commands on them. Steps that need other Azure permissions fail with an Azure authorization error (`AuthorizationFailed`) until you assign another Azure role to the connector's Azure application. Assigning roles in Azure requires the Owner or User Access Administrator role. Don't edit `AWSSSMVMExtensionRole-*`, because running connector setup again resets it.

For Google Cloud, runbooks can do what the roles granted to the connector's service account at connector setup allow. To allow more, grant more roles to that service account in Google Cloud IAM.