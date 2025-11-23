# IAM temporary delegation for AWS Partners

## Overview

IAM temporary delegation enables AWS customers to seamlessly onboard and/or integrate AWS Partner products into their AWS environment through interactive, guided workflows. Customers can grant AWS Partners limited, temporary access to configure required AWS services, reducing onboarding friction and accelerating time to value.

IAM temporary delegation enables partners to:

- Streamline customer onboarding with automated resource provisioning
- Reduce integration complexity by eliminating manual configuration steps
- Build trust through transparent, customer-approved permissions
- Enable ongoing operations with long-term access patterns using permission boundaries

## How it works

1. _Partner creates a delegation request_ - Partners create a request specifying what permissions they need and for how long
2. _Customer reviews in AWS Console_ - Customer sees exactly what permissions partner is requesting and why
3. _Customer approves_ - Customer approves the request and releases an exchange token. The token is sent to partner on this specified SNS topic.
4. _Partner receives temporary credentials_ - Partners exchange the token for temporary AWS credentials
5. _Partner configures resources_ - Partners use the credentials to set up required resources in the customer's account

## Partner qualification

To qualify for temporary delegation integration, a partner must meet the following requirements:

- _ISV Accelerate participation_ – You must be enrolled in the [ISV Accelerate (ISVA)](https://aws.amazon.com/partners/programs/isv-accelerate/ "https://aws.amazon.com/partners/programs/isv-accelerate/") program.
- _AWS Marketplace listing_ – Your product must be listed in the AWS Marketplace with a "Deployed on AWS" badge.

## Onboarding process

Complete the following steps to integrate temporary delegation into your product:

1. _Step 1: Review requirements_

Review this documentation to understand the qualification requirements and complete the partner questionnaire below. 2. _Step 2: Submit your onboarding request_

Send an email to aws-iam-partner-onboarding@amazon.com or contact your AWS representative. Include your completed partner questionnaire with all required fields from the table below. 3. _Step 3: AWS validation and review_

AWS will:

    * Validate that you meet the qualification criteria
    * Review your policy templates and permission boundaries
    * Provide feedback on your submitted artifacts

4. _Step 4: Refine your policies_

Respond to AWS feedback and submit updated policy templates or permission boundaries as needed. 5. _Step 5: Complete registration_

Once approved, AWS will:

    * Enable API access for your specified accounts
    * Share ARNs for your policy template and permissions boundary (if applicable)

You will receive confirmation when onboarding is complete. You can then access temporary delegation APIs, CreateDelegationRequest and GetDelegatedAccessToken from your registered accounts and begin integrating delegation request workflows into your product.

## Partner questionnaire

The following table lists the information required for partner onboarding:

| Information                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 | Required |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Partner Central AccountID       | Account ID of your registered AWS account on [AWS Partner Central](https://partnercentral.awspartner.com/partnercentral2/s/login "https://partnercentral.awspartner.com/partnercentral2/s/login").                                                                                                                                                                                                                                          | Yes      |
| PartnerId                       | Partner ID provided by [AWS Partner Central](https://partnercentral.awspartner.com/partnercentral2/s/login "https://partnercentral.awspartner.com/partnercentral2/s/login").                                                                                                                                                                                                                                                                | No       |
| AWS Marketplace Product Id      | Product ID for your product provided by [AWS Partner Central](https://partnercentral.awspartner.com/partnercentral2/s/login "https://partnercentral.awspartner.com/partnercentral2/s/login").                                                                                                                                                                                                                                               | Yes      |
| AWS accountIDs                  | The list of your AWS Account IDs that you want to use to call temporary delegation APIs. This should include both your production and non-production/test accounts.                                                                                                                                                                                                                                                                         | Yes      |
| Partner name                    | This name is displayed to customers in the AWS Management Console when they review your temporary delegation request.                                                                                                                                                                                                                                                                                                                       | Yes      |
| Contact email(s)                | One or more email addresses that we can use to contact you about your integration.                                                                                                                                                                                                                                                                                                                                                          | Yes      |
| Requestor Domain                | Your domain (for example, www.example.com)                                                                                                                                                                                                                                                                                                                                                                                                  | Yes      |
| Integration description         | Brief description of the use case that you want to address using this feature. You can include reference links to your documentation or other public material.                                                                                                                                                                                                                                                                              | Yes      |
| Architecture diagram            | Architecture diagram illustrating your integration use case(s).                                                                                                                                                                                                                                                                                                                                                                             | No       |
| Policy template                 | You must register at least one policy template for this feature. The policy template defines the temporary permissions you want to request in customers' AWS accounts. For more information, see Policy template section.                                                                                                                                                                                                                   | Yes      |
| Policy template name            | Name of the policy template you want to register.                                                                                                                                                                                                                                                                                                                                                                                           | Yes      |
| Permissions Boundary            | If you want to create IAM roles in customers' accounts using temporary permissions, you must register a permission boundary with IAM. Permission boundaries will be attached to the IAM roles that you create to limit the maximum permissions on the role. You can use selected AWS managed policies as a permission boundary or register a new custom permission boundary (JSON). For more information, see Permissions Boundary section. | No       |
| Permission Boundary Name        | The name of your permission boundary. The format is: arn:aws:iam::partner:policy/permission_boundary/<partner_domain>/<policy_name>\_<date> The policy name must include the creation date as a suffix. The name cannot be updated once the permission boundary is created. If you are using an existing AWS managed policy, provide the managed policy ARN instead.                                                                        | No       |
| Permission Boundary Description | Description for the permission boundary. This description cannot be updated once the permission boundary is created.                                                                                                                                                                                                                                                                                                                        | No       |
