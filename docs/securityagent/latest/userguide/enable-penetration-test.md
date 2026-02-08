# Enable penetration test

Configure AWS Security Agent to run autonomous penetration tests on your applications. This setup enables AWS Security Agent to access your AWS resources, verify domain ownership, and perform comprehensive security testing that identifies exploitable vulnerabilities in your web applications and APIs.

Enabling penetration testing allows AWS Security Agent to continuously validate your application security without the delays of manual testing. By configuring the necessary AWS integrations, you ensure AWS Security Agent can test both public and private applications, log findings to CloudWatch, and access credentials for authenticated testing.

In this procedure, you’ll configure target domains, optionally set up VPC, CloudWatch logging, credentials storage, and Lambda functions for testing, configure S3 integrations for providing additional context, and set up service access through IAM roles.

## Prerequisites

Before you begin, ensure you have:

- AWS account with administrative permissions to create IAM roles
- Domain ownership verification capability (DNS or HTTP record modification)
- Target domains or applications to test
- (Optional) VPC configuration details if testing private applications
- (Optional) S3 bucket if providing additional artifacts to AWS Security Agent

## Step 1: Add and verify target domains

AWS Security Agent requires verified ownership of all target domains before enabling penetration testing. This section is required and displays expanded by default.

1. In the **Target domains** section, enter your domain in the **Domain** field.
2. Select a **Verification method**:
   - **DNS txt record** – Add a TXT record to your domain’s DNS configuration
   - **HTTP record** – Host a verification file at a specific URL on your domain
   - For more information, see [Enable an application domain for penetration testing](enable-test-domain.md "enable-test-domain.md").

3. Click **Add new domain** to add additional domains.
4. Complete the verification process for each domain according to the method you selected. NOTE: Sub-domains that belong to your verified target domain do not require individual verification. You may perform penetration testing on all sub-domains that are part of your verified target domain.

###### Note

All target domains must be verified before AWS Security Agent can perform penetration testing on them. Once a domain is verified, you can also add subdomains of that domain to your penetration test scope without requiring further verification. For private domains inside a VPC, you would also be able to create or update pentests if the domain verification status is UNREACHABLE. AWS Security Agent will try to perform domain verification for the private endpoint at the start of a pentest run again.

## Step 2: (Optional) Configure VPC settings

If you plan to test private target domains hosted within a VPC, configure VPC settings for AWS Security Agent. This section is optional and collapsed by default.

1. Expand the **VPCs** section.
2. In the **VPC** dropdown, select the VPC that hosts your private target domains.
3. In the **Subnet** dropdown, select the VPC subnets that AWS Security Agent should use:

###### Tip

For high availability, select multiple subnets from multiple Availability Zones. Ensure your subnets include a NAT gateway for outbound connectivity. 4. In the **Security group** dropdown, select the VPC security groups that AWS Security Agent should use:

###### Important

Ensure your security groups allow outbound connections for AWS Security Agent to perform penetration testing.

## Step 3: (Optional) Configure CloudWatch logging

Configure CloudWatch to store logs from your penetration test runs. This section is optional and collapsed by default.

1. Expand the **CloudWatch logs** section.
2. In the **Log Groups** dropdown, select existing CloudWatch log groups
3. If not selecting any log group, AWS Security Agent will create a log group named `/aws/securityagent/<agent name>/<pentest id>` with appropriate permissions.

###### Note

Ensure your IAM role has permissions to write to the selected CloudWatch log group.

## Step 4: (Optional) Configure Secrets for test credentials

If your application requires authentication credentials for testing, AWS Security Agent can securely retrieve them from AWS Secrets Manager. This section is optional and collapsed by default.

1. Expand the **Secrets** section.
2. Select the AWS Secrets Manager secrets that contain credentials for your application.
3. When configuring a penetration test in the web application, you can reference these secrets for authenticated testing.

###### Important

Credentials are encrypted and stored in AWS Secrets Manager. Ensure your IAM role has permissions to access Secrets Manager for AWS Security Agent to use these credentials during testing.

## Step 5: (Optional) Configure Lambda functions for test credentials

Configure Lambda functions that can provide credentials for your application during testing. This section is optional and collapsed by default.

1. Expand the **Lambda functions** section.
2. Select the Lambda functions that can provide authentication credentials for your application.
3. AWS Security Agent will invoke these functions during penetration tests to obtain credentials dynamically.

###### Note

Ensure your IAM role has permissions to invoke the specified Lambda functions. Lambda functions should return credentials in the expected format for AWS Security Agent to use during testing.

## Step 6: (Optional) Configure S3 bucket

Provide S3 bucket details if you plan to upload documents or artifacts to provide as input to AWS Security Agent. This section is optional and collapsed by default.

1. Expand the **S3 buckets** section.
2. In the **Bucket** field, enter or search for your S3 bucket name.

###### Note

You can also connect GitHub repositories later or upload files directly in the web application. Information provided can ensure thorough coverage, reduce false positives, and deliver actionable results.

## Step 7: (Optional) Configure service access

AWS Security Agent requires an IAM role to access your AWS resources (VPC, CloudWatch log groups, Secrets Manager, Lambda functions, etc.) for penetration testing. This section is optional and collapsed by default.

1. Expand the **Service access** section.
2. By default, AWS Security Agent uses a default IAM role with the required permissions for penetration testing.
3. To customize the IAM role, select one of the following options:
   1. **Create default role** – AWS Security Agent automatically creates a new IAM role with the necessary permissions
   2. **Use an existing service role** – Select an existing IAM role from the dropdown menu

4. If using an existing role:
   1. Click the dropdown menu under **Choose an existing role**
   2. Select your IAM role from the list
   3. Click the refresh icon to update the list if needed

###### Note

The default IAM role includes permissions for accessing VPC resources, CloudWatch log groups, Secrets Manager, Lambda functions, and other services required for penetration testing. It is recommended to use the default IAM role unless you have specific security requirements.

## Step 8: Enable penetration testing

After configuring all required settings, enable penetration testing for your AWS Security Agent agent.

1. Review all configuration sections to ensure accuracy.
2. Click **Save** at the bottom of the page.
3. AWS Security Agent will validate your configuration and create the necessary AWS resources.

## Next steps

After enabling penetration testing:

- Configure penetration test scopes in the AWS Security Agent web application
- Set up notification preferences for test findings
- Review and respond to penetration test findings as they are discovered
- (Optional) Configure additional repositories for findings remediation

For more information about running and managing penetration tests, see the AWS Security Agent web application documentation.
