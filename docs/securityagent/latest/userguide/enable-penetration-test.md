

# Enable penetration test
<a name="enable-penetration-test"></a>

Configure AWS Security Agent to run autonomous penetration tests on your applications. This setup enables AWS Security Agent to access your AWS resources, verify domain ownership, and perform comprehensive security testing that identifies exploitable vulnerabilities in your web applications and APIs.

Enabling penetration testing allows AWS Security Agent to continuously validate your application security without the delays of manual testing. By configuring the necessary AWS integrations, you ensure AWS Security Agent can test both public and private applications, log findings to CloudWatch, and access credentials for authenticated testing.

In this procedure, you’ll configure target domains, optionally set up VPC, CloudWatch logging, credentials storage, and Lambda functions for testing, configure S3 integrations for providing additional context, and set up service access through IAM roles.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:
+ AWS account with administrative permissions to create IAM roles
+ Domain ownership verification capability (DNS or HTTP record modification)
+ Target domains or applications to test
+ (Optional) VPC configuration details if testing private applications
+ (Optional) S3 bucket if providing additional artifacts to AWS Security Agent

## Step 1: Configure domain
<a name="_step_1_configure_domain"></a>

In the first step of the wizard, specify the target domains you want to test and how AWS Security Agent should verify ownership.

1. In the **Target domains** section, enter your domain in the **Domain** field.

1. Select a **Verification method**:
   +  **DNS\_TXT** – Prove domain ownership by adding a TXT record to your domain’s DNS configuration.
   +  **HTTP\_ROUTE** – Prove domain ownership by hosting a verification file at a specific URL on your domain.
   +  **PRIVATE\_VPC** - Only usable for private VPC penetration testing. Verifies that the domain resolves to an IP in a private CIDR range
   + For more information, see [Enable an application domain for penetration testing](enable-test-domain.md).

1. Choose **Add another domain** to add additional domains (up to 20 total).

1. Choose **Next** to proceed to domain verification.

## Step 2: Verify domains
<a name="_step_2_verify_domains"></a>

In the second step of the wizard, verify ownership of each domain you configured. AWS Security Agent requires verified ownership before it can perform penetration testing.

1. Review the domains listed in the **Target domains** table.

1. For each domain, select it and trigger verification based on your chosen method:
   +  **Route 53 domains (same AWS account)**: Choose **One-click verification**. AWS Security Agent automatically creates the DNS record and completes verification.
   +  **DNS TXT (other DNS providers)**: Copy the verification token, add the TXT record with your DNS registrar, then select the domain and choose **Verify**.
   +  **HTTP route**: Place the verification token at the required route path on your web server, then select the domain and choose **Verify**. For details, see [Enable an application domain for penetration testing](enable-test-domain.md).

1. Choose **Next** to proceed to optional configuration.

**Note**  
Sub-domains of a verified domain do not require individual verification when using DNS TXT or HTTP route verification. For Private VPC verification, the target endpoint domain name must match the full domain name configured for verification.

**Note**  
For private domains inside a VPC, you can proceed even if the domain verification status is UNREACHABLE. AWS Security Agent will attempt domain verification for private endpoints at the start of each penetration test run.

## Step 3: (Optional) Configure additional capabilities
<a name="_step_3_optional_configure_additional_capabilities"></a>

The third step of the wizard lets you configure optional AWS resources to expand your penetration testing scope. All sections in this step are optional and collapsed by default.

### (Optional) Configure VPC settings
<a name="_optional_configure_vpc_settings"></a>

If you plan to test private target domains hosted within a VPC, configure VPC settings for AWS Security Agent. This section is optional and collapsed by default.

1. Expand the **VPCs** section.

1. In the **VPC** dropdown, select the VPC that hosts your private target domains.

1. In the **Subnet** dropdown, select the VPC subnets that AWS Security Agent should use:
**Tip**  
For high availability, select multiple subnets from multiple Availability Zones. Ensure your subnets include a NAT gateway for outbound connectivity.

1. In the **Security group** dropdown, select the VPC security groups that AWS Security Agent should use:
**Important**  
Ensure your security groups allow outbound connections for AWS Security Agent to perform penetration testing.

### (Optional) Configure CloudWatch logging
<a name="_optional_configure_cloudwatch_logging"></a>

Configure CloudWatch to store logs from your penetration test runs. This section is optional and collapsed by default.

1. Expand the **CloudWatch logs** section.

1. In the **Log Groups** dropdown, select existing CloudWatch log groups

1. If not selecting any log group, AWS Security Agent will create a log group named `/aws/securityagent/<agent name>/<pentest id>` with appropriate permissions.

**Note**  
Ensure your IAM role has permissions to write to the selected CloudWatch log group.

### (Optional) Configure Secrets for test credentials
<a name="_optional_configure_secrets_for_test_credentials"></a>

If your application requires authentication credentials for testing, AWS Security Agent can securely retrieve them from AWS Secrets Manager. This section is optional and collapsed by default.

1. Expand the **Secrets** section.

1. Select the AWS Secrets Manager secrets that contain credentials for your application.

1. When configuring a penetration test in the web application, you can reference these secrets for authenticated testing.

**Important**  
Credentials are encrypted and stored in AWS Secrets Manager. Ensure your IAM role has permissions to access Secrets Manager for AWS Security Agent to use these credentials during testing.

### (Optional) Configure Lambda functions for test credentials
<a name="_optional_configure_lambda_functions_for_test_credentials"></a>

Configure Lambda functions that can provide credentials for your application during testing. This section is optional and collapsed by default.

1. Expand the **Lambda functions** section.

1. Select the Lambda functions that can provide authentication credentials for your application.

1. AWS Security Agent will invoke these functions during penetration tests to obtain credentials dynamically.

**Note**  
Ensure your IAM role has permissions to invoke the specified Lambda functions. Lambda functions should return credentials in the expected format for AWS Security Agent to use during testing.

### (Optional) Configure S3 bucket
<a name="_optional_configure_s3_bucket"></a>

Provide S3 bucket details if you plan to upload documents or artifacts to provide as input to AWS Security Agent. This section is optional and collapsed by default.

1. Expand the **S3 buckets** section.

1. In the **Bucket** field, enter or search for your S3 bucket name.

**Note**  
You can also connect GitHub repositories later or upload files directly in the web application. Information provided can ensure thorough coverage, reduce false positives, and deliver actionable results.

### (Optional) Configure service access
<a name="_optional_configure_service_access"></a>

AWS Security Agent requires an IAM role to access your AWS resources (VPC, CloudWatch log groups, Secrets Manager, Lambda functions, etc.) for penetration testing. This section is optional and collapsed by default.

1. Expand the **Service access** section.

1. By default, AWS Security Agent uses a default IAM role with the required permissions for penetration testing.

1. To customize the IAM role, select one of the following options:

   1.  **Create default role** – AWS Security Agent automatically creates a new IAM role with the necessary permissions

   1.  **Use an existing service role** – Select an existing IAM role from the dropdown menu

1. If using an existing role:

   1. Choose the dropdown menu under **Choose an existing role** 

   1. Select your IAM role from the list

   1. Choose the refresh icon to update the list if needed

**Note**  
The default IAM role includes permissions for accessing VPC resources, CloudWatch log groups, Secrets Manager, Lambda functions, and other services required for penetration testing. It is recommended to use the default IAM role unless you have specific security requirements.

## Step 4: Save and enable penetration testing
<a name="_step_4_save_and_enable_penetration_testing"></a>

After configuring all required settings, enable penetration testing for your AWS Security Agent agent.

1. Review all configuration sections to ensure accuracy.

1. Choose **Save**.

1. AWS Security Agent validates your configuration and creates the necessary AWS resources.

## Next steps
<a name="_next_steps"></a>

After enabling penetration testing:
+ Configure penetration test scopes in the AWS Security Agent web application
+ Set up notification preferences for test findings
+ Review and respond to penetration test findings as they are discovered
+ (Optional) Configure additional repositories for findings remediation

For more information about running and managing penetration tests, see the AWS Security Agent web application documentation.