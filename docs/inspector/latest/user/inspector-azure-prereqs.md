

# Prerequisites for integrating Amazon Inspector with Microsoft Azure
<a name="inspector-azure-prereqs"></a>

Before you create a connector, verify that your AWS account and Azure environment meet the following requirements. The Azure setup script handles most Azure configuration automatically (app registration, Event Hub, diagnostic settings, Azure role assignments, and Microsoft Graph API permissions).

IAM Outbound Identity Federation and OIDC provider  
Your AWS account must have an IAM Token Issuer URL configured for outbound identity federation. This enables Amazon Inspector to securely authenticate to your Azure environment using short-lived tokens.  
For VM scanning, you must also have an IAM OIDC identity provider configured with the issuer URL `sts.windows.net/{{tenant-id}}/`. This provider enables the Amazon Inspector VM Scanner agent on your Azure VMs to authenticate back to AWS using `sts:AssumeRoleWithWebIdentity`. Without this provider, the VM scanner cannot send telemetry to Amazon Inspector.  
If you have already configured outbound identity federation for another AWS security service (such as AWS Security Hub CSPM or AWS Security Hub CSPM CSPM), you do not need to configure it again. For more information, see [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.  
On the Azure side, the setup script creates the federated identity credential that trusts the AWS STS OIDC issuer. You do not need to configure this manually.

Service-linked role  
The API creates the Amazon Inspector service-linked role on behalf of the customer during connector creation. No manual SLR provisioning is required.

Config connector  
A connector ARN is required when creating a connector via API. The Config connector captures Azure resource configuration changes. In the console, you can either select an existing connector or create a new one during connector creation.

Console IAM permissions  
The IAM principal (user or role) that creates the connector requires the following permissions:  

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "config:GetConnector",
        "config:ListConnectors",
        "config:PutConnector",
        "inspector2:CreateConnector",
        "inspector2:DeleteConnector",
        "inspector2:ListConnectors",
        "inspector2:ListTagsForResource",
        "inspector2:TagResource",
        "inspector2:UntagResource",
        "inspector2:UpdateConnector"
      ],
      "Resource": "*"
    }
  ]
}
```

In addition to the requirements above, VM scanning requires:
+ Amazon EC2 Systems Manager configured in the same Region as the connector
+ Amazon EC2 Systems Manager Automation permissions for managed deployment of the Amazon Inspector VM Scanner agent

Before you run the Azure setup script, ensure that you have the following:

Azure tenant  
A Microsoft Azure commercial tenant. Azure Government and Azure China are not supported.

Microsoft Entra ID log availability  
Resource recording requires Microsoft Graph audit logs and sign-in logs from your Microsoft Entra ID tenant. Some Microsoft Entra ID logs require Microsoft Entra ID P1 or P2 licensing.  
If the tenant lacks required logs, resource recording might report partial failures. The app registration and Azure role assignments do not supply missing log data.

Azure role  
The person configuring Azure must have the Global Administrator role in the Azure tenant.

Azure CLI  
The Azure CLI installed and authenticated (`az login`).

**Note**  
The person who sets up the Azure environment does not need to be the same person who creates the connector in the Amazon Inspector console.