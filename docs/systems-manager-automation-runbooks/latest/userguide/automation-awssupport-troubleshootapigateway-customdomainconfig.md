

# `AWSSupport-TroubleshootAPIGatewayCustomDomainConfig`
<a name="automation-awssupport-troubleshootapigateway-customdomainconfig"></a>

 **Description** 

The `AWSSupport-TroubleshootAPIGatewayCustomDomainConfig` runbook helps you identify issues with your custom domain name configuration in Amazon API Gateway. The runbook analyzes the following configuration steps:
+ A custom domain name is created in API Gateway.
+ A mapping exists between the custom domain name and the API in question.
+ A DNS record exists for the custom domain name and is pointing to the correct target.

**Important**  
This runbook does not support troubleshooting mTLS issues with API Gateway custom domain names.

**Important**  
This runbook only supports troubleshooting publicly resolvable custom domain names.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootAPIGatewayCustomDomainConfig) 

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `apigateway:GET`
+ `route53:ListResourceRecordSets`

Example IAM policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "apigateway:GET",
                "route53:ListResourceRecordSets"
            ],
            "Resource": "*"
        }
    ]
}
```

**Note**  
The IAM user or role that starts the runbook requires the following actions:  
`iam:ListRoles`
`iam:PassRole`
`ssm:DescribeAutomationExecutions`
`ssm:DescribeAutomationStepExecutions`
`ssm:DescribeDocument`
`ssm:GetAutomationExecution`
`ssm:GetDocument`
`ssm:ListDocuments`
`ssm:StartAutomationExecution`

 **Instructions** 

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-TroubleshootAPIGatewayCustomDomainConfig`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayCustomDomainConfig/description) in Systems Manager under Documents.

1. Select Execute automation.

1. For the input parameters, enter the following:
   + **AutomationAssumeRole (Optional):**

     The Amazon Resource Name (ARN) of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
   + **DomainName (Required):**

     The custom domain name created for your Amazon API Gateway API.
   + **ApiId (Required):**

     The API ID of your API Gateway.
   + **DNSServerIp (Optional):**

     IPv4 address of a DNS server to resolve the custom domain name and API Gateway domain name. If a value is not specified, the AWS DNS Server (169.254.169.253) will be used.
   + **HostedZoneId (Optional):**

     The Public Hosted Zone ID where the DNS record for the custom domain name is created in Amazon Route 53. If Route 53 is not used for DNS, the value is not required.

1. Select Execute.

1. The automation initiates.

1. The document performs the following steps:
   + **`CheckAPIExists`**:

     Checks the existence of Amazon API Gateway API.
   + **`GetDomainName`**:

     Gets details for the custom domain name configured in Amazon API Gateway.
   + **`GetMappings`**:

     Retrieves all Amazon API Gateway API mappings configured for the custom domain name and verifies if the specified API ID has a valid mapping with the correct stage and path configurations.
   + **`CheckDNSRecordExists`**:

     Checks the custom domain name DNS and returns the associated records.
   + **`ValidateDNSResults`**:

     Compares the DNS details (A or CNAME records) of the custom domain name to ensure the record points to the correct Amazon API Gateway distribution domain name.
   + **`Results`**:

     Formats the overall output of the Systems Manager Automation to return a structured summary of the custom domain configuration analysis results to the Systems Manager console.

1. After completion, review the Outputs section for the detailed results of the execution.

**References**

Systems Manager Automation
+ [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayCustomDomainConfig/description)
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/)