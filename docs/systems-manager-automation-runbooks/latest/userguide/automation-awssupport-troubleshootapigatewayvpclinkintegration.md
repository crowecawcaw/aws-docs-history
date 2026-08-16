# `AWSSupport-TroubleshootAPIGatewayVpcLinkIntegration`

## Description

The `AWSSupport-TroubleshootAPIGatewayVpcLinkIntegration` runbook helps you troubleshoot Amazon API Gateway integrations that use an Amazon Virtual Private Cloud (Amazon VPC) link. Use this runbook to identify configuration issues across integration components without inspecting each resource separately. The runbook supports REST APIs and HTTP APIs, and performs the following checks:

- **API and integration discovery** – Identifies the API type and matches the resource path and HTTP method to the configured integration.
- **Amazon VPC link validation** – Verifies that the integration uses an Amazon VPC link and checks whether the link is available.
- **Backend analysis** – Examines Elastic Load Balancing resources or AWS Cloud Map service discovery resources associated with the integration.
- **Network configuration** – Evaluates subnet routing, security groups, and network ACLs between an HTTP API Amazon VPC link and its load balancer.
- **Listener and target health** – Validates listener configuration, target groups, target health, and supported Network Load Balancer and Application Load Balancer architectures.
- **TLS certificate validation** – Checks certificate status, trust, chain validity, expiration, and hostname coverage when the integration uses TLS.

###### Limitations

This runbook has the following limitations:

- The runbook provides detailed backend analysis only for integrations that use the `VPC_LINK` connection type.
- For HTTP APIs, the runbook analyzes integrations with an Elastic Load Balancing listener or AWS Cloud Map service discovery service.
- The runbook validates standard HTTP and HTTPS listener configurations on ports 80 and 443. It doesn't validate custom listener ports.
- The runbook doesn't support cross-account Amazon VPC link configurations.
- For Amazon VPC links associated with HTTP APIs, the runbook evaluates security group and network ACL connectivity only on TCP port 443.

###### Prerequisites

Before you run the automation, ensure that the IAM role specified in `AutomationAssumeRole` has the listed permissions. If you don't specify a role, you must have these permissions.

## How it works

The runbook performs the following validation and analysis:

- Identifies whether the specified API is a REST API or HTTP API.
- Matches the supplied resource path and HTTP method to the applicable resource, route, and integration.
- Retrieves the integration and Amazon VPC link configuration, and verifies the Amazon VPC link status.
- Analyzes the associated load balancer or AWS Cloud Map service discovery configuration.
- Validates network, listener, certificate, target group, and target health configuration when applicable.
- Generates a report with detected issues, configuration details, recommendations, and relevant AWS CLI commands.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootAPIGatewayVpcLinkIntegration "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootAPIGatewayVpcLinkIntegration")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `apigateway:GET`
- `elasticloadbalancing:DescribeLoadBalancers`
- `elasticloadbalancing:DescribeListeners`
- `elasticloadbalancing:DescribeRules`
- `elasticloadbalancing:DescribeTargetGroups`
- `elasticloadbalancing:DescribeTargetHealth`
- `ec2:DescribeNetworkInterfaces`
- `ec2:DescribeRouteTables`
- `ec2:DescribeSubnets`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribePrefixLists`
- `ec2:DescribeNetworkAcls`
- `servicediscovery:GetService`
- `servicediscovery:GetNamespace`
- `acm:DescribeCertificate`

Example IAM policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "APIGatewayReadAccess",
            "Effect": "Allow",
            "Action": "apigateway:GET",
            "Resource": [
                "arn:aws:apigateway:*::/restapis/*",
                "arn:aws:apigateway:*::/apis/*",
                "arn:aws:apigateway:*::/vpclinks/*"
            ]
        },
        {
            "Sid": "LoadBalancerReadAccess",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeListeners",
                "elasticloadbalancing:DescribeRules",
                "elasticloadbalancing:DescribeTargetGroups",
                "elasticloadbalancing:DescribeTargetHealth"
            ],
            "Resource": "*"
        },
        {
            "Sid": "EC2NetworkReadAccess",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribePrefixLists",
                "ec2:DescribeNetworkAcls"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ServiceDiscoveryReadAccess",
            "Effect": "Allow",
            "Action": [
                "servicediscovery:GetService",
                "servicediscovery:GetNamespace"
            ],
            "Resource": [
                "arn:aws:servicediscovery:*:`ACCOUNTID`:service/*",
                "arn:aws:servicediscovery:*:`ACCOUNTID`:namespace/*"
            ]
        },
        {
            "Sid": "CertificateReadAccess",
            "Effect": "Allow",
            "Action": "acm:DescribeCertificate",
            "Resource": "arn:aws:acm:*:`ACCOUNTID`:certificate/*"
        }
    ]
}

```

## Instructions

Follow these steps to configure the automation:

1. Open [AWSSupport-TroubleshootAPIGatewayVpcLinkIntegration](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayVpcLinkIntegration/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayVpcLinkIntegration/description") in the Systems Manager console under **Documents**.
2. Choose **Execute automation**.
3. For the input parameters, enter the following:

   - **AutomationAssumeRole (Optional)**

   The Amazon Resource Name (ARN) of the IAM role that Systems Manager Automation uses to perform actions on your behalf. If you don't specify a role, Systems Manager Automation uses your permissions.
   - **ApiId (Required)**

   The 10-character ID of the API Gateway REST API or HTTP API that you want to troubleshoot.
   - **ApiResourcePath (Required)**

   The API resource path with the Amazon VPC link integration. Exclude the stage and custom domain base path. For example, `/users/{id}`, `/api/v1/products`, or `/health`. Use `/` for the root path or `$default` for the HTTP API default route.
   - **ApiMethod (Required)**

   The HTTP method configured for the resource path. Allowed values: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS`, and `ANY`. For an HTTP API `$default` route, choose `ANY`.

4. Choose **Execute**.
5. The automation initiates.
6. The runbook performs the following steps. Conditional branches might skip steps that don't apply to the integration:

   - **`ExtractApiTypeAndIntegrationParams`** – Identifies the API type and matches the supplied path and method to a REST API resource or HTTP API route.
   - **`GetApiIntegration`** – Retrieves the integration type, URI, connection type, connection ID, and TLS configuration.
   - **`BranchOnConnectionType`** – Continues detailed analysis when the integration uses an Amazon VPC link. Otherwise, the runbook generates the report.
   - **`GetVpcLinkDetails`** – Retrieves the Amazon VPC link status, target ARNs, security groups, and subnets.
   - **`BranchOnVpcLinkStatus`** – Continues analysis when the Amazon VPC link is available. Otherwise, the runbook generates the report.
   - **`BranchOnAPIType`** – Routes REST APIs to load balancer analysis and HTTP APIs to backend integration analysis.
   - **`BranchOnIntegrationType`** – Routes HTTP APIs to load balancer analysis or AWS Cloud Map service discovery analysis.
   - **`GetLoadBalancerDetails`** – Retrieves the load balancer state, type, scheme, Amazon VPC, security groups, subnets, and PrivateLink security group setting.
   - **`GetServiceDiscoveryDetails`** – Retrieves the AWS Cloud Map service and namespace details for a service discovery backend.
   - **`BranchOnLoadBalancerAvailability`** – Continues load balancer analysis when its state is `active`. Otherwise, the runbook generates the report.
   - **`BranchOnVPCLinkVersion`** – Routes Amazon VPC links for REST APIs to listener validation and Amazon VPC links for HTTP APIs to network configuration validation.
   - **`VerifySubnetAndSecurityGroupConfig`** – Validates subnet routing, security group rules, and network ACLs between an Amazon VPC link for HTTP APIs and its load balancer.
   - **`DescribeAndValidateListenerConfig`** – Retrieves listener details and validates protocol and port compatibility with the integration endpoint.
   - **`BranchOnCertificateRequired`** – Routes TLS listeners to certificate validation. Other listeners continue to target group analysis.
   - **`DescribeAndValidateCertificate`** – Uses AWS Certificate Manager (ACM) data to validate certificate status, trust, chain, expiration, and hostname coverage.
   - **`DescribeTargetsAndTargetGroups`** – Retrieves the listener target group and evaluates target health and target type.
   - **`BranchOnTargetHealth`** – Continues when all targets are healthy. Otherwise, the runbook generates the report.
   - **`BranchOnTargetType`** – Routes an Application Load Balancer target to additional listener analysis when the parent load balancer type is Network Load Balancer.
   - **`VerifyTargetALBListeners`** – Validates Network Load Balancer and target Application Load Balancer protocol, port, health check, target health, and certificate compatibility.
   - **`GenerateReport`** – Consolidates findings into a report with configuration details, detected issues, recommendations, and relevant references.

7. After completion, review the **Outputs** section for the detailed report and overall status.

## References

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayVpcLinkIntegration/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayVpcLinkIntegration/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
