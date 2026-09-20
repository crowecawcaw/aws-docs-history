

# Create a penetration test
<a name="perform-penetration-test"></a>

Set up automated penetration testing for your web applications by configuring test scope, target domains, and AWS resource access. Penetration tests help identify security vulnerabilities in running applications by simulating real-world attack scenarios against your verified domains.

AWS Security Agent performs comprehensive security testing against your web applications based on configured scope and permissions, providing detailed findings about exploitable vulnerabilities before attackers can discover them.

In this procedure, you’ll create a penetration test by configuring test details, defining the test scope, and setting up required permissions.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:
+ Access to the AWS Security Agent web application
+ At least one verified domain for testing
+ IAM role with appropriate permissions for AWS Security Agent
+ Understanding of your application’s architecture and critical paths

## Start creating a penetration test
<a name="_start_creating_a_penetration_test"></a>

Navigate to the penetration test creation page in the web application.

1. Log in to the AWS Security Agent web application.

1. Navigate to the **Penetration tests** section.

1. Choose **Create a penetration test**.

**Tip**  
Only verified domains can be included in penetration tests. Ask your admin to verify the domain in AWS management console. See [Enable an application domain for penetration testing](enable-test-domain.md).

When you complete the **Credentials** and **Network configuration** steps, AWS Security Agent tests more of your application and stays away from anything you do not want reached. The wizard has five steps:

1.  **Penetration test details** – Name the test, set the target URLs, and choose the service role and log group.

1. (Optional) **VPC Resources** – Configure network access for a target that is not publicly reachable.

1. (Optional) **Credentials** – Add the credentials the agent uses to sign in, and test that each one works.

1.  **Network configuration** – Review every domain the test may reach, including the domains discovered while your credentials were signed in.

1. (Optional) **Additional configuration** – Add application context and set run options.

Choose **Save & Next** to move to the next step. Each **Save & Next** saves your progress, so you can leave the wizard and come back later.

A test you started but did not finish appears in the **Penetration tests** list with a **Draft** badge. Choose **Continue setup** on that test to return to the wizard. You cannot start a draft until you finish the wizard and create the test.

## Name your penetration test
<a name="_name_your_penetration_test"></a>

Provide a descriptive name that helps identify the purpose and scope of this penetration test.

1. In the **Penetration test name** field, enter a descriptive name for your penetration test.  
**Example**  

   The name should clearly identify the application, environment, or component being tested. Maximum 100 characters.

## Configure penetration test scope
<a name="_configure_penetration_test_scope"></a>

Define which domains the penetration test is allowed to attack.

The **Penetration testing scope** section holds the target URLs. Its **Advanced network access** subsection holds custom HTTP headers.

You classify the other domains the test may reach on the **Network configuration** step, after the agent has tested your credentials. For more information, see [Review network scope](#pentest-network-scope).

### Add target domains
<a name="_add_target_domains"></a>

Specify the verified domains that will be actively tested for security vulnerabilities.

1. In the **Penetration testing scope** section, locate **Target URLs**.

1. Expand the **Verified domains** section to view available domains.

1. In the **Target URL** field, enter a target domain URL.
**Important**  
Only verified domains can be tested. The URL must be under a domain you’ve previously verified in AWS Security Agent. Sub-domains of a verified domain do not require separate verification.
**Non-standard ports**  
If your application serves traffic on a non-standard port, include the port in the URL. For example, `https://example.com:8443`. Domain verification applies to the host. You don’t need to verify the domain again to test a different port.

1. To add multiple target domains:

   1. Choose **Add domain**.

   1. Enter each additional domain URL.

1. To remove a target domain, choose **Remove** next to the domain URL.

**Tip**  
For best results, include all domains that are part of your application’s user flow, including subdomains for APIs, authentication services, and content delivery. Sub-domains of a verified parent domain do not require separate verification.

### Add custom HTTP headers (optional)
<a name="_add_custom_http_headers_optional"></a>

Specify custom HTTP headers that will be added to any requests made by AWS Security Agent during penetration testing.

1. Expand **Advanced network access**, then locate the **Custom HTTP headers** section.

1. In the **Custom HTTP headers** input field, enter a header name and value that will be associated with outbound requests.
**Note**  
By default, AWS Security Agent adds a custom header for **User-Agent** set to **securityagent** unless a different custom **User-Agent** header value is specified.

1. To add multiple custom headers:

   1. Choose **Add header**.

   1. Enter each additional custom header.

1. To remove a custom header, choose **Remove** next to the header.

## Configure IAM Role
<a name="_configure_iam_role"></a>

Select the pre-configured service role for this penetration test. AWS Security Agent uses an Agent Space-based permission model where administrators configure IAM roles when setting up your Agent Space. You select from roles that are already configured and ready to use.

1. In the **Permissions** section, locate the **Service roles** dropdown.

1. Select the IAM role that grants AWS Security Agent access to required AWS resources.
**Important**  
The selected IAM role must have permissions to access VPC resources, CloudWatch Logs, and any other AWS services needed for the penetration test. Verify that the role has the correct trust relationship with AWS Security Agent.

1. Locate the **CloudWatch log group** dropdown.

1. Select the log group where penetration test logs will be stored. (optional)
**Note**  
The selected CloudWatch log group will store detailed logs of the penetration test execution, including requests made, responses received, and vulnerabilities discovered.  
If you don’t select a log group, a new CloudWatch log group will be automatically created with the `/aws/securityagent` prefix to store the penetration test logs.

## Automatic code remediation
<a name="_automatic_code_remediation"></a>

Select the **Enable automatic remediation** checkbox.

**Important**  
To remediate security findings in your source code repositories, AWS Security Agent may submit pull requests to your repositories. The pull requests may be visible to all users who have read access to the repositories.

## Configure VPC resources (optional)
<a name="_configure_vpc_resources_optional"></a>

If your target domains are private and hosted within a VPC, configure the VPC settings where AWS Security Agent should run penetration tests. This step is only necessary for applications that are not publicly accessible.

**Note**  
Skip this step if your target domains are publicly accessible. VPC configuration is only required for testing private applications hosted within an Amazon Virtual Private Cloud.

Choose the VPC, subnets, and security groups for the penetration test environment.

1. In the **VPC** section, locate the **VPC ID** dropdown.

1. Select the VPC where your target domains are hosted.
**Important**  
The selected VPC must contain the target domains you specified in Step 3. Ensure the VPC has appropriate routing and network configuration to allow AWS Security Agent to access your applications.

1. Locate the **Subnets** dropdown.

1. Select one or more subnets where the penetration test should run.
**Note**  
Choose subnets that have network access to your target applications. The penetration test will execute from resources deployed in these subnets.

1. Locate the **Security group** dropdown.

1. Select the security group that controls network access for the penetration test.
**Important**  
The selected security group must allow outbound traffic to your target domains and any accessible domains. Ensure the security group rules permit the necessary network access for comprehensive testing.

## Configure authentication credentials (optional)
<a name="_configure_authentication_credentials_optional"></a>

If your target domains require authentication, provide credentials to allow AWS Security Agent to access protected areas of your application during penetration testing. This step is only necessary for applications that require user authentication.

**Note**  
Skip this step if your target domains do not require authentication or if all areas you want tested are publicly accessible. Configure credentials only when you need AWS Security Agent to test authenticated sections of your application.

Credentials appear in a table on the **Credentials** step. The table lists each credential’s name, test status, and authentication type.

**Important**  
When AWS Security Agent signs in with your credentials, it tests everything your application exposes to that signed-in user. Authenticated paths can reach shared services and third-party domains that you are not authorized to test. Only provide credentials for applications you are authorized to test.  
Test against a non-production environment, and do not provide credentials that have access to production systems. For more information, see [Use non-production environments for penetration testing](https://docs.aws.amazon.com/securityagent/latest/userguide/security-best-practices.html#_use_non_production_environments_for_penetration_testing).

### Add credentials
<a name="_add_credentials"></a>

Provide authentication credentials that AWS Security Agent will use to access your application.

1. On the **Credentials** step, choose **Add credential**.

1. In the **Credential name** field, enter a name that is unique within this penetration test. AWS Security Agent uses this name to report the credential’s test results and findings.

1. Select a credential input method:
   +  **Input credentials** - Enter your credentials directly into AWS Security Agent.
   +  **Advanced setting** - For sensitive credential information, use advanced options such as AWS Secrets Manager or AWS Lambda functions. See [Provide authentication credentials for penetration testing](provide-testing-credentials.md) for details.
**Tip**  
For production environments or sensitive credentials, we recommend using the advanced setting option to securely reference credentials stored in AWS Secrets Manager or Systems Manager Parameter Store.

1. For **Input credentials**, enter the **Username** and **Password** for the authenticated account. Use an account whose access matches a typical user rather than an administrator.

1. In the **Access URL** dropdown, select the URL where these credentials will be used. You can select only a URL that is already in **Target URLs**. To use a different URL, add it as a target URL first.

1. Under **Agent Space login prompt**, enter instructions that describe how to sign in with these credentials. A login prompt is required for each credential, because it tells AWS Security Agent how to reach your login, complete it, and confirm that it worked. To start from a worked example, choose one of the buttons below the field, such as **Website login** or **API request**, then edit the inserted text. Choosing an example replaces whatever is in the field.

1. Choose **Save**, or choose **Save and test** to save the credential and immediately test it.

To change a credential later, choose the edit icon in its row. To delete one, choose the remove icon.

### Test credentials
<a name="_test_credentials"></a>

Test a credential to confirm that AWS Security Agent can sign in with it before the penetration test runs. Testing also discovers the domains your application reaches while signed in. AWS Security Agent then suggests those domains on the **Network configuration** step.

1. In the credential’s row, choose **Test**. To test every credential at once, choose **Test all credentials**.

1. Watch the **Status** column. A credential moves through **Starting** and **In progress** to one of these results:
   +  **Success** – AWS Security Agent signed in with the credential.
   +  **Failed** – Sign-in did not succeed. Choose the status to see the reason.
   +  **Timed out** – AWS Security Agent could not complete the sign-in in time. A test that cannot sign in stops after 15 minutes.
   +  **Unverified** – The credential has not been tested, or you changed it after its last test.

1. To see what the agent did during a test, choose **View logs** in the credential’s row.

Most sign-in tests finish in 2 to 3 minutes. A test keeps running if you leave the **Credentials** step, so you can continue through the wizard while it finishes.

If a credential fails, check that the username and password are correct and that the login prompt describes the steps to reach and complete your login. Then edit the credential and test it again.

A timeout here does not stop you from starting the penetration test. During the penetration test, the agent gets an hour to sign in, four times what it gets for a credential test. A sign-in that was only slow often succeeds with that extra time.

When you leave the **Credentials** step with credentials that have not been tested, AWS Security Agent asks whether to test them. Choose **Test credentials** to test the remaining ones, or **Skip testing** to continue without testing. An untested credential discovers nothing, so any domain reachable only behind it is missing from the suggestions on the **Network configuration** step and you must add it yourself.

### Add multiple credentials (optional)
<a name="_add_multiple_credentials_optional"></a>

If your application requires multiple sets of credentials or different domains need separate authentication, add additional credential sets.

1. Choose **Add credential** again for each additional credential.

1. Repeat the credential configuration steps for each one.

1. To remove a credential, choose the remove icon in its row.

**Tip**  
Configure multiple credentials when testing different user roles, accessing multiple authenticated domains, or verifying role-based access controls in your application.

## Review network scope
<a name="pentest-network-scope"></a>

On the **Network configuration** step, classify every domain the penetration test may reach. If you tested credentials on the previous step, the domains your application reached while signed in are already listed for you and marked **Suggested**. Review each one, then add anything the tests did not reach.

Every domain has one of three classifications:
+  **Target** – A URL the penetration test is allowed to attack. Target URLs come from the **Penetration test details** step and are marked with a **Target** badge. To change one, go back to that step.
+  **Accessible** – A URL the penetration test can access but must not attack. Use this for a hosted login page, a content delivery network (CDN), or another supporting service your application depends on.
+  **Out of scope** – A URL the penetration test must not access at all.

<a name="add-out-of-scope-url-paths-optional"></a>By default, only your target URLs are reachable. Add an accessible entry for anything else your application needs. An entry can be a whole domain, such as `auth.example.com`, or a specific path, such as `https://example.com/callback`. An out-of-scope entry always takes precedence over an accessible one.

<a name="add-accessible-domains-optional"></a>Accessible domains do not require ownership verification, even if they belong to a different domain than your target. Only target domains require verified ownership. AWS Security Agent does not penetration test accessible domains; it uses them only for login and navigation.

**Non-standard ports for accessible domains**  
To make a non-standard port accessible, enter a full URL that includes the scheme and the port. For example, `https://auth.example.com:8443`. If you enter a domain without a scheme, such as `auth.example.com:8443`, AWS Security Agent allows the domain only on standard ports.

### Classify a domain
<a name="_classify_a_domain"></a>

1. On the **Network configuration** step, review the **Network scope** table.

1. For each domain, select **Accessible** or **Out of scope**.

1. To add a domain the tests did not discover, choose **Add domain**, then enter the URL and select its classification.

1. To remove a domain you added, choose the remove icon in its row. You cannot remove a target URL here.

**Warning**  
Mark as out of scope any path that should not be accessed during testing, such as a destructive operation or a sensitive administrative function. AWS Security Agent excludes the specified path and all paths nested beneath it. For example, if you mark `https://example.com/admin` as out of scope, `https://example.com/admin/tools` is also out of scope.

To review the same domains grouped by classification instead of in a table, choose **Grouped** in **Domain view**. In grouped view, choose **Edit** to make changes, then choose **Save**.

The **Derived examples** list at the bottom of the section shows endpoints that cannot receive traffic from the penetration test, based on how you classified each domain. Use it to confirm your classifications before you continue.

## Attach additional resources (optional)
<a name="_attach_additional_resources_optional"></a>

Provide supplementary resources to help AWS Security Agent conduct more thorough and accurate penetration testing. Additional resources can include architecture diagrams, API documentation, configuration files, GitHub repositories, or S3-hosted materials that give context about your application.

**Note**  
Additional resources are optional but recommended. Providing comprehensive information about your application helps ensure thorough test coverage, reduces false positives, and delivers more actionable results.

### Add resources to the penetration test
<a name="_add_resources_to_the_penetration_test"></a>

Select existing resources or upload new files that will help guide the penetration test.

1. In the **Connected resources** section, you can:
   + Choose **Select from available** to choose from resources already connected to AWS Security Agent (such as GitHub repositories or S3 buckets).
   + Choose **Upload** to add new files directly from your local system.

**Tip**  
Useful resources include API documentation, architecture diagrams, OpenAPI/Swagger specifications, configuration files, authentication flow diagrams, and any other materials that describe your application’s structure and behavior.

### Select from available resources
<a name="_select_from_available_resources"></a>

Choose from resources that are already integrated with AWS Security Agent.

1. Choose **Select from existing resources**.

1. Browse the list of available resources from connected sources such as:
   + GitHub repositories, under the **GitHub repositories tab** 
   + S3 buckets
   + Previously uploaded files
   + Documentation repositories

1. Select the resources you want to include in the penetration test.

1. Choose **Add to penetration test** to attach the selected resources.

**Example**  
We recommend selecting and adding relevant GitHub repositories to your penetration test, so AWS Security Agent can develop an understanding of your application context, and generate ready-to-implement code fixes through pull requests (when enabled)

**Tip**  
When you select a repository, you can specify a branch. By default, the service uses the primary branch. To use a different branch, enter the branch name in the field next to the repository.

**Note**  
Resources selected from available sources remain synchronized with their original location. If you update a GitHub repository or S3 file, the penetration test will use the updated version.

**Note**  
If you have a private VPC associated with your penetration test and a GitHub repository configured, ensure that GitHub is accessible through your private VPC for pulling GitHub resources. In most cases, you need to either ensure that outbound traffic through [VPC NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) is allowed by default or configure specific rules to allow outbound traffic for GitHub IPs (see [GitHub Meta API Endpoint](https://api.github.com/meta))

### Upload new resources
<a name="_upload_new_resources"></a>

Upload files directly from your local system or provide plain text content to AWS Security Agent.

1. Choose **Upload**.

1. Choose one of the following input methods:
   +  **Upload local files** - Select one or more files from your local system.
   +  **Paste plain text** - Type or paste text content directly into the input field. Choose **Upload**.

1. Then choose **Add** to complete uploading.

1. The uploaded resources appear in the **Connected resources** table.

**Tip**  
Use the plain text option when you want to quickly provide API endpoint lists, URL patterns, test instructions, or other text-based information without creating a separate file.

**Important**  
Ensure uploaded files and pasted content do not contain sensitive information such as production credentials, private keys, or personally identifiable information (PII). Use sanitized versions of configuration files and documentation.

### Connect existing resources
<a name="_connect_existing_resources"></a>

Existing resources can be from what you’ve previously uploaded to AWS Security Agent, from your S3 bucket, and your integrated GitHub repositories. Choose **Select from existing resources** to select them.

### Manage connected resources
<a name="_manage_connected_resources"></a>

Review, organize, and remove resources attached to the penetration test.

The **Connected resources** table displays all resources included in the penetration test with the following information:
+  **Name** - The filename or resource identifier
+  **Type** - The resource category (Uploaded files, S3 resources, GitHub repositories, etc.)

To manage resources:

1. Select one or more resources using the checkboxes.

1. Choose **Remove from penetration test** to detach selected resources.

**Note**  
You can sort the table by Name or Type by clicking the column headers. This helps organize resources when working with many files.

## Set a maximum task-hours limit
<a name="_set_a_maximum_task_hours_limit"></a>

Limit how much work AWS Security Agent performs for a penetration test by setting a maximum number of task hours. Task hours measure the cumulative time the agent spends actively working on the test, including time across parallel testing. Task hours are not the same as elapsed wall-clock time, because AWS Security Agent runs multiple tasks at once. Total task hours is also the unit that AWS Security Agent bills for a run, so setting a limit caps how much a test can cost. The smallest limit you can set is 20 hours.

1. (Optional) In the **Max task hours** section, choose a limit:
   + Choose a preset value, such as **20** or **30** hours.
   + Choose **No limit** to run the test to completion without a task-hours limit.
   + Choose **Custom** to enter your own value. A custom limit must be at least 20 hours.

**Tip**  
For larger applications, or to get the most complete results, set a higher limit such as **30** hours or more. AWS Security Agent bills only for the task hours a run actually uses, so a higher limit does not increase cost unless the test needs the extra time.

**Note**  
When a test reaches its maximum task hours, AWS Security Agent stops working on the test and keeps the findings already discovered. The run finishes with a status of **Completed**. You can review these findings or create and run a new test.

## Exclude risk types (optional)
<a name="_exclude_risk_types_optional"></a>

Choose specific risk categories to exclude from testing if they’re not applicable to your application.

1. On the **Additional configuration** step, locate the **Exclude risk types** field.

1. Choose the dropdown to view available risk types.

1. Select one or more risk types to exclude from the penetration test.
**Note**  
Excluding risk types limits the scope of testing. Only exclude risk types that are not relevant to your application or that you want to test separately.

## Create the penetration test
<a name="_create_the_penetration_test"></a>

Finalize and launch your penetration test configuration.

After configuring all settings, you’re ready to create the penetration test.

1. Review all configuration sections to ensure accuracy.

1. Choose one of the following options:
   + Choose **Create penetration** to save the configuration without running it immediately.
   + Choose **Create and execute** to save the configuration and immediately start the penetration test.
   + Choose **Cancel** to discard the penetration test configuration.

**Important**  
Before running a penetration test, verify that:  
All target domains are correctly verified and accessible
IAM roles have appropriate permissions
Out-of-scope paths are properly configured to prevent testing destructive operations
You have authorization to perform security testing on all target domains

**Note**  
After the penetration test starts, you can monitor its progress from the **Penetration test runs** section. The test can take several hours to complete, depending on the scope and complexity of your application. If you set a maximum task-hours limit, AWS Security Agent stops the test when it reaches that limit. AWS Security Agent preserves the findings discovered so far.