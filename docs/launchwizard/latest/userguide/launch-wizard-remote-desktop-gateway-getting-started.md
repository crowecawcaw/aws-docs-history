# Get Started with AWS Launch Wizard for Remote Desktop Gateway

This section contains information to help you set up your environment to deploy RD Gateway
with Launch Wizard. When your environment is set up, you can deploy RD Gateway application with Launch Wizard by
following the steps and parameter specification details provided in this section.

###### Topics to help you get started:

- [Access AWS Launch Wizard](#launch-wizard-remote-desktop-gateway-access "#launch-wizard-remote-desktop-gateway-access")
- [Specialized knowledge](#launch-wizard-remote-desktop-gateway-specialized-knowledge "#launch-wizard-remote-desktop-gateway-specialized-knowledge")
- [Service Quotas](#launch-wizard-remote-desktop-gateway-resource-quotas "#launch-wizard-remote-desktop-gateway-resource-quotas")
- [Amazon Elastic Compute Cloud key pairs](#launch-wizard-remote-desktop-gateway-key-pairs "#launch-wizard-remote-desktop-gateway-key-pairs")
- [AWS Identity and Access Management permissions](#launch-wizard-remote-desktop-gateway-iam-permissions "#launch-wizard-remote-desktop-gateway-iam-permissions")

## Access AWS Launch Wizard

You can launch AWS Launch Wizard from the AWS Launch Wizard console located at [https://console.aws.amazon.com/launchwizard](https://console.aws.amazon.com/launchwizard "https://console.aws.amazon.com/launchwizard").

## Specialized knowledge

This deployment requires a moderate level of familiarity with AWS services. If you’re new
to AWS, see [Getting Started Resource
Center](https://aws.amazon.com/getting-started "https://aws.amazon.com/getting-started") and [AWS Training and
Certification](https://aws.amazon.com/training "https://aws.amazon.com/training"). These sites provide materials for learning how to design, deploy, and
operate your infrastructure and applications on the AWS Cloud.

This Launch Wizard assumes familiarity with Remote Desktop Gateway.

## Service Quotas

If necessary, [request service quota
increases](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") for the following resources. You might need to request increases if your
existing deployment currently uses these resources and if this Launch Wizard deployment could result in
exceeding the default quotas. The [Service Quotas
console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") displays your usage and quotas for some aspects of some services. For more
information, see [What
is Service Quotas?](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md") and [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

Existing VPC Service Quotas:

| Resource                                                 | Default quota     | This deployment uses |
| -------------------------------------------------------- | ----------------- | -------------------- |
| Elastic IP Addresses                                     | 5 per Region      | 2                    |
| AWS Identity and Access Management (IAM) security groups | 300 per account   | 1                    |
| IAM roles                                                | 1,000 per account | 1                    |
| Auto Scaling groups                                      | 200 per Region    | 1                    |
| Amazon EC2 On-Demand Instances (Standard)                | 5 per Region      | 1-4                  |

New VPC Service Quotas:

| Resource                                                 | Default quota     | This deployment uses |
| -------------------------------------------------------- | ----------------- | -------------------- |
| VPCs                                                     | 5 per Region      | 1                    |
| Elastic IP Addresses                                     | 5 per Region      | 2                    |
| Internet Gateway                                         | 5 per Region      | 1                    |
| AWS Identity and Access Management (IAM) security groups | 300 per account   | 1                    |
| IAM roles                                                | 1,000 per account | 1                    |
| Auto Scaling groups                                      | 200 per Region    | 1                    |
| Amazon EC2 On-Demand Instances (Standard)                | 5 per Region      | 1-4                  |

## Amazon Elastic Compute Cloud key pairs

Ensure that at least one Amazon EC2 key pair exists in your AWS account in the Region where you
plan to deploy the Launch Wizard application. Note the key pair name because you will use it during
deployment. To create a key pair, see [Amazon EC2 key pairs and EC2 instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").

For testing or proof-of-concept purposes, we recommend creating a new key pair instead of
using one that’s already being used by a production instance.

## AWS Identity and Access Management permissions

Before deploying the Launch Wizard application, you must sign in to the AWS Management Console with IAM
permissions for the resources that the templates deploy. The _AdministratorAccess_ managed policy within IAM provides sufficient permissions,
although your organization may choose to use a custom policy with more restrictions. For more
information, see [AWS managed policies for job
functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md").
