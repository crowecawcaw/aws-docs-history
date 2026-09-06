

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Security in AWS Transform MGN
<a name="security"></a>

**Topics**
+ [Overview](#security-overview)
+ [Identity and access management for AWS Transform MGN](identity-access-management.md)
+ [Managing access using policies](security_iam_access-manage.md)
+ [Using service-linked roles for AWS Transform MGN](using-service-linked-roles.md)
+ [Policy structure](#iam-policy-structure)
+ [Resilience in AWS Transform MGN](disaster-recovery-resiliency.md)
+ [Infrastructure security in AWS Transform MGN](infrastructure-security.md)
+ [Compliance validation for AWS Transform MGN](compliance-validation.md)
+ [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md)

## Overview
<a name="security-overview"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations. 

Security is a shared responsibility between AWS and you. The [shared responsibility model ](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud: 
+  **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) . To learn about the compliance programs that apply to AWS Transform MGN, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/). .  
+  **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations 

This documentation helps you understand how to apply the shared responsibility model when using AWS Transform MGN. It shows you how to configure AWS Transform MGN to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your AWS Transform MGN resources. 

The customer is responsible for making sure that no misconfigurations are present during and after the migration process, including: 

1. Access to replication servers should be allowed only from source servers CIDR range by applying proper security groups rules on replication servers. 

1. After the migration, the customer should make sure that only allowed ports are exposed to the public internet. 

1. Hardening of OS packages and other software deployed in the servers is completely under the customer’s responsibility and we recommend the following: 

   1. Packages should be up to date and free of known vulnerabilities.

   1. Only necessary OS/application services should be up and running.

1. Enabling the Anti-DDOS protection (AWS Shield) in the customer's AWS Account to eliminate the risk of denial of service attacks on the replication servers as well as the migrated servers. 

## Policy structure
<a name="iam-policy-structure"></a>

An IAM policy is a JSON document that consists of one or more statements. Each statement is structured as follows. 

```
{
        "Statement": [
                {
                        "Effect": "{{effect}}",
                        "Action": "{{action}}",
                        "Resource": "{{arn}}",
                        "Condition": {
                                "{{condition}}": {
                                        "{{key}}":"{{value}}"
                                }
                        }
                }
        ]
}
```

There are various elements that make up a statement:
+  **Effect:** The effect can be `Allow` or `Deny`. By default, IAM users don't have permission to use resources and API actions, so all requests are denied. An explicit allow overrides the default. An explicit deny overrides any allows. 
+ **Action**: The action is the specific AWS Transform MGN API action for which you are granting or denying permission. 
+ **Resource**: The resource that's affected by the action. For AWS Transform MGN, you must specify "\*" as the resource. 
+ **Condition**: Conditions are optional. They can be used to control when your policy is in effect. 