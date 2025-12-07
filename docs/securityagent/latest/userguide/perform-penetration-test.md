# Create a penetration test

Set up automated penetration testing for your web applications by configuring test scope, target domains, and AWS resource access. Penetration tests help identify security vulnerabilities in running applications by simulating real-world attack scenarios against your verified domains.

AWS Security Agent performs comprehensive security testing against your web applications based on configured scope and permissions, providing detailed findings about exploitable vulnerabilities before attackers can discover them.

In this procedure, you’ll create a penetration test by configuring test details, defining the test scope, and setting up required permissions.

## Prerequisites

Before you begin, ensure you have:

- Access to the AWS Security Agent web application
- At least one verified domain for testing
- IAM role with appropriate permissions for AWS Security Agent
- CloudWatch log group configured for storing test logs
- Understanding of your application’s architecture and critical paths

## Start creating a penetration test

Navigate to the penetration test creation page in the Agent Web App.

1. Log in to the AWS Security Agent web application.
2. Navigate to the **Penetration tests** section.
3. Click **Create penetration test**.

###### Tip

Only verified domains can be included in penetration tests. Ask your admin to verify the domain in AWS management console. See [Enable an application domain for penetration testing](enable-test-domain.md "enable-test-domain.md").

## Name your penetration test

Provide a descriptive name that helps identify the purpose and scope of this penetration test.

1. In the **Penetration test name** field, enter a descriptive name for your penetration test.

###### Note

The name should clearly identify the application, environment, or component being tested. Maximum 100 characters.

## Configure penetration test scope

Define which domains and URL paths will be tested, and configure optional exclusions to control test boundaries.

### Add target domains

Specify the verified domains that will be actively tested for security vulnerabilities.

1. In the **Penetration test scope** section, locate **Target domains**.
2. Expand the **Verified domains** section to view available domains.
3. Click in the **Input URL** field and enter a target domain URL.

###### Important

Only verified domains can be tested. The URL must match a domain you’ve previously verified in AWS Security Agent. 4. To add multiple target domains:

    1. Click **Add domain**.
    2. Enter each additional domain URL.

5. To remove a target domain, click **Remove** next to the domain URL.

###### Tip

For best results, include all domains that are part of your application’s user flow, including subdomains for APIs, authentication services, and content delivery.

### Exclude risk types (optional)

Choose specific risk categories to exclude from testing if they’re not applicable to your application.

1. Locate the **Exclude risk types** field.
2. Click the dropdown to view available risk types.
3. Select one or more risk types to exclude from the penetration test.

###### Note

Excluding risk types limits the scope of testing. Only exclude risk types that are not relevant to your application or that you want to test separately.

### Add out-of-scope URL paths (optional)

Specify URL paths that should not be tested during the penetration test.

1. Locate the **Out-of-scope URL path** section.
2. Click in the input field and enter a URL path to exclude (for example, `/admin/delete` or `/api/reset`).
3. To add multiple out-of-scope paths:
   1. Click **Add another**.
   2. Enter each additional path.

4. To remove a path, click **Remove** next to the path.

###### Warning

Out-of-scope paths will not be tested for vulnerabilities. Ensure you only exclude paths that should not be accessed during testing, such as destructive operations or sensitive administrative functions.

### Add additional allowed domains (optional)

Specify domains that are required for the test but are not targets for vulnerability testing.

1. Locate the **Additional allowed domains** section.
2. Click in the input field and enter a domain that should be accessible during testing.

###### Note

Additional allowed domains might include authentication providers, external APIs, or third-party services required for your application to function. These domains will be accessible during testing but will not be actively tested for vulnerabilities. 3. To add multiple allowed domains:

    1. Click **Add another**.
    2. Enter each additional domain.

4. To remove a domain, click **Remove** next to the domain.

## Configure IAM Role

Set up AWS resource access for the penetration test by selecting the IAM role and CloudWatch log group.

1. In the **Permissions** section, locate the **Service roles** dropdown.
2. Select the IAM role that grants AWS Security Agent access to required AWS resources.

###### Important

The selected IAM role must have permissions to access VPC resources, CloudWatch Logs, and any other AWS services needed for the penetration test. Verify that the role has the correct trust relationship with AWS Security Agent. 3. Locate the **CloudWatch log group** dropdown. 4. Select the log group where penetration test logs will be stored.

###### Note

The selected CloudWatch log group will store detailed logs of the penetration test execution, including requests made, responses received, and vulnerabilities discovered.

## Automatic code remediation

Select the **Enable automatic remediation** checkbox.

###### Important

To remediate security findings in your source code repositories, AWS Security Agent may submit pull requests to your repositories. The pull requests may be visible to all users who have read access to the repositories.

## Configure VPC resources (optional)

If your target domains are private and hosted within a VPC, configure the VPC settings where AWS Security Agent should run penetration tests. This step is only necessary for applications that are not publicly accessible.

###### Note

Skip this step if your target domains are publicly accessible. VPC configuration is only required for testing private applications hosted within an Amazon Virtual Private Cloud.

Choose the VPC, subnets, and security groups for the penetration test environment.

1. In the **VPC** section, locate the **VPC ID** dropdown.
2. Select the VPC where your target domains are hosted.

###### Important

The selected VPC must contain the target domains you specified in Step 3. Ensure the VPC has appropriate routing and network configuration to allow AWS Security Agent to access your applications. 3. Locate the **Subnets** dropdown. 4. Select one or more subnets where the penetration test should run.

###### Note

Choose subnets that have network access to your target applications. The penetration test will execute from resources deployed in these subnets. 5. Locate the **Security group** dropdown. 6. Select the security group that controls network access for the penetration test.

###### Important

The selected security group must allow outbound traffic to your target domains and any additional allowed domains. Ensure the security group rules permit the necessary network access for comprehensive testing.

## Configure authentication credentials (optional)

If your target domains require authentication, provide credentials to allow AWS Security Agent to access protected areas of your application during penetration testing. This step is only necessary for applications that require user authentication.

###### Note

Skip this step if your target domains do not require authentication or if all areas you want tested are publicly accessible. Configure credentials only when you need AWS Security Agent to test authenticated sections of your application.

### Add credentials

Provide authentication credentials that AWS Security Agent will use to access your application.

1. In the **Credential #1** section, select a credential input method:
   - **Input credentials** - Enter your credentials directly into AWS Security Agent.
   - **Advanced setting** - For sensitive credential information, use advanced options such as AWS Secrets Manager or AWS Lambda functions. See [Provide authentication credentials for penetration testing](provide-testing-credentials.md "provide-testing-credentials.md") for details.

   ###### Tip

   For production environments or sensitive credentials, we recommend using the advanced setting option to securely reference credentials stored in AWS Secrets Manager or Systems Manager Parameter Store.

### Enter credential details

Provide the username and password for the authenticated account.

1. In the **User name** field, enter the username for authentication.
2. In the **Password** field, enter the password for authentication.

###### Important

Ensure the credentials you provide have appropriate access levels for the areas you want tested. The credentials should represent a typical user’s access level rather than administrative privileges.

### Select access domain

Specify which target domain will use these credentials for authentication.

1. In the **Access domain** dropdown, select the domain where these credentials will be used.

###### Note

If you have multiple target domains that require different credentials, you can add additional credential sets by clicking **Add another credential** after completing this credential configuration.

### Configure agent login prompt (optional)

Provide instructions to guide AWS Security Agent through your application’s authentication process.

1. Expand the **Agent login prompt** section if your authentication flow requires specific instructions.
2. Enter detailed instructions describing how to access your application using the provided credentials.

###### Note

The agent login prompt is useful for complex authentication flows, multi-step login processes, or applications with non-standard login procedures. Include step-by-step instructions such as "Navigate to /login, enter username in the 'Email' field, enter password, and click 'Sign In'."

### Add multiple credentials (optional)

If your application requires multiple sets of credentials or different domains need separate authentication, add additional credential sets.

1. After completing the first credential configuration, click **Add another credential**.
2. Repeat the credential configuration steps for each additional credential set.
3. To remove a credential set, click **Remove** next to the credential header.

###### Tip

Configure multiple credentials when testing different user roles, accessing multiple authenticated domains, or verifying role-based access controls in your application.

## Attach additional resources (optional)

Provide supplementary resources to help AWS Security Agent conduct more thorough and accurate penetration testing. Additional resources can include architecture diagrams, API documentation, configuration files, GitHub repositories, or S3-hosted materials that give context about your application.

###### Note

Additional resources are optional but recommended. Providing comprehensive information about your application helps ensure thorough test coverage, reduces false positives, and delivers more actionable results.

### Add resources to the penetration test

Select existing resources or upload new files that will help guide the penetration test.

1. In the **Connected resources** section, you can:
   - Click **Select from available** to choose from resources already connected to AWS Security Agent (such as GitHub repositories or S3 buckets).
   - Click **Upload** to add new files directly from your local system.

###### Tip

Useful resources include API documentation, architecture diagrams, OpenAPI/Swagger specifications, configuration files, authentication flow diagrams, and any other materials that describe your application’s structure and behavior.

### Select from available resources

Choose from resources that are already integrated with AWS Security Agent.

1. Click **Select from existing resources**.
2. Browse the list of available resources from connected sources such as:
   - GitHub repositories, under the **GitHub repositories tab**
   - S3 buckets
   - Previously uploaded files
   - Documentation repositories

3. Select the resources you want to include in the penetration test.
4. Click **Add to penetration test** to attach the selected resources.

We recommend selecting and adding relevant GitHub repositories to your pentest, so AWS Security Agent can develop an understanding of your application context, and generate ready-to-implement code fixes through pull requests (when enabled)

###### Note

Resources selected from available sources remain synchronized with their original location. If you update a GitHub repository or S3 file, the penetration test will use the updated version.

### Upload new resources

Upload files directly from your local system or provide plain text content to AWS Security Agent.

1. Click **Upload**.
2. Choose one of the following input methods:
   - **Upload local files** - Select one or more files from your local system.
   - **Paste plain text** - Type or paste text content directly into the input field. Click **Upload**.

3. Then click **Add** to complete uploading.
4. The uploaded resources will appear in the **Connected resources** table.

###### Tip

Use the plain text option when you want to quickly provide API endpoint lists, URL patterns, test instructions, or other text-based information without creating a separate file.

###### Important

Ensure uploaded files and pasted content do not contain sensitive information such as production credentials, private keys, or personally identifiable information (PII). Use sanitized versions of configuration files and documentation.

### Connect existing resources

Existing resources can be from what you’ve previously uploaded to AWS Security Agent, from your S3 bucket, and your integrated GitHub repositories. Click **Select from existing resources** to select them.

### Manage connected resources

Review, organize, and remove resources attached to the penetration test.

The **Connected resources** table displays all resources included in the penetration test with the following information:

- **Name** - The filename or resource identifier
- **Type** - The resource category (Uploaded files, S3 resources, GitHub repositories, etc.)

To manage resources:

1. Select one or more resources using the checkboxes.
2. Click **Remove from penetration test** to detach selected resources.

###### Note

You can sort the table by Name or Type by clicking the column headers. This helps organize resources when working with many files.

## Create the penetration test

Finalize and launch your penetration test configuration.

After configuring all settings, you’re ready to create the penetration test.

1. Review all configuration sections to ensure accuracy.
2. Choose one of the following options:
   - Click **Create penetration** to save the configuration without running it immediately.
   - Click **Create and execute** to save the configuration and immediately start the penetration test.
   - Click **Cancel** to discard the penetration test configuration.

###### Important

Before running a penetration test, verify that:

- All target domains are correctly verified and accessible
- IAM roles have appropriate permissions
- Out-of-scope paths are properly configured to prevent testing destructive operations
- You have authorization to perform security testing on all target domains

###### Note

After the penetration test starts, you can monitor its progress from the **Penetration test runs** section. The test may take several hours depending on the scope and complexity of your application.
