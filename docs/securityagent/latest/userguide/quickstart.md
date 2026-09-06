

# Quickstart: Run a penetration test
<a name="quickstart"></a>

This quickstart walks you through running your first penetration test (pentest) with AWS Security Agent. A penetration test exercises your deployed application against a verified target domain and returns security findings, each with a severity rating and supporting evidence. It covers a publicly accessible application; to test one hosted in a private VPC, see [Enable penetration test](enable-penetration-test.md).

**Note**  
You need access to the AWS Management Console to set up AWS Security Agent and define the test scope, and access to the web application to create and run penetration tests.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, make sure you have:
+ Access to the AWS Management Console with permissions to set up AWS Security Agent.
+ A live target domain that hosts the application you want to test.
+ The ability to add a DNS record for that domain, or a Route 53 hosted zone in the same AWS account, so you can verify ownership.
+ (Optional) A source code repository (GitHub, GitLab, or Bitbucket) for your application, to give the agent more context.

## Step 1: Set up AWS Security Agent in the AWS console
<a name="_step_1_set_up_aws_security_agent_in_the_aws_console"></a>

If you haven’t already set up AWS Security Agent, complete the initial setup:

1. Navigate to [AWS Security Agent](https://console.aws.amazon.com/securityagent/) in the AWS Management Console.

1. Select **Set up AWS Security Agent**.

1. Create an Agent Space. An Agent Space can be used by multiple users and should be specific for every application you want to secure. Enter a name and description for your first Agent Space. This name appears to users in the web application. The name should identify the application you want to secure.

1. Select **IAM-only access** under *User access configuration*.
   + This quickstart does not cover enabling single sign-on (SSO) with IAM Identity Center. With IAM Identity Center enabled, you can access the web application directly from the AWS Console.
   + To let users without AWS Management Console access use AWS Security Agent, enable the IAM Identity Center integration. For details, see [Grant users access to the AWS Security Agent web application](grant-user-access.md).

1. Choose **Set up AWS Security Agent**.

**Note**  
When you choose Set up, AWS Security Agent creates your Agent Space and establishes a web application where users can run penetration tests, code reviews, threat models, and design reviews.

## Step 2: Enable penetration testing and verify your domain
<a name="step-2-enable-penetration-testing-and-verify-your-domain"></a>

**Note**  
In the AWS console you define the scope of what can be tested. Users then run specific penetration tests within that scope from the web application.

1. From the left sidebar, select **Agent Spaces**, then select the Agent Space you created in Step 1.

1. Select the **Penetration test** tab, then choose **Set up penetration test** to open the wizard.

1.  **Configure domain** - Enter the target domain you want to test and select a verification method, **DNS TXT Record** or **HTTP Route**. The domain must be live and host the application you want to test. Choose **Next**.

1.  **Verify domains** - Verify ownership of each domain in the **Target domains** table. AWS Security Agent runs tests only against verified domains. For detailed steps and the exact values to copy, see [Enable an application domain for penetration testing](enable-test-domain.md).
   +  **Route 53 domains in the same AWS account** - Select the domain and choose **One-click verification**. AWS Security Agent creates the DNS record and completes verification for you.
   +  **DNS TXT record (other DNS providers)** - In the **Target domains** table, copy the **Record name** and **Record value**, add them as a TXT record with your DNS provider, then select the domain and choose **Verify**. DNS changes can take time to propagate, so verification might not complete immediately.
   +  **HTTP route** - Create a file at `.well-known/aws/securityagent-domain-verification.json` on your web server, add the verification token in the format `{"tokens": ["<token>"]}`, then select the domain and choose **Verify**.

1. (Optional) **Configure additional capabilities** - Add optional resources such as CloudWatch log groups and credentials. The **Service access** section is pre-configured: AWS Security Agent creates a service role with the required permissions unless you choose an existing IAM role.

## Step 3: Connect source code (optional)
<a name="step-3-connect-source-code-optional"></a>

Connecting a source code provider gives AWS Security Agent context about your application and improves penetration testing coverage. This step is optional.

1. On the **Penetration test** tab, choose **Add** on the **Connect a source code provider for penetration testing** banner at the top of the page.

1. Register and connect your provider, then select the repositories to make available for penetration testing.

For the full integration flow, see [Connect AWS Security Agent to GitHub repositories](connect-github.md) or the connect topic for your provider.

## Step 4: Create and run a penetration test
<a name="step-4-create-and-run-a-penetration-test"></a>

**Note**  
You create and run penetration tests in the AWS Security Agent web application. We recommend running tests against a test environment that closely mirrors production.

1. Launch the web application: select the **Web app** tab, then **Admin access**.

1. In the left sidebar, choose **Penetration tests**, then **Create a penetration test**.

1.  **Penetration test details** - Set up the test scope and log source:

   1. Enter a **Pentest name**.

   1. Under **Target URLs**, select or enter a verified domain to test (for example, `https://example.com`). Only verified domains can be tested, and sub-domains are covered automatically.

   1. (Optional) Under **Accessible URLs**, add domains the agent must reach for login and navigation but should not attack, such as identity providers, CDNs, or APIs outside your target domain. AWS Security Agent can reach these domains but does not test them; only your target domains are attacked.

   1. Review the **Networking config rules** to confirm which endpoints can and cannot receive traffic during the test.

   1. Under **Permissions**, select a **Service role** and, optionally, a **CloudWatch log group**. Choose **Next**.

1. (Optional) **VPC Resources** - Configure a VPC if your target is on a private network that isn’t publicly reachable. See [Enable penetration test](enable-penetration-test.md).

1. (Optional) **Authentication Resources** - Provide credentials so the agent can reach authenticated, non-public paths. We recommend adding these to broaden coverage and surface vulnerabilities behind a login.

1. (Optional) **Additional configuration** - Add application context such as files, GitHub repositories, or S3 sources to improve finding quality. You can also enable automatic code remediation and set other run options here.

1. Choose **Create and execute** to start the test now, or **Create pentest** to save it and run it later.

## Step 5: Review penetration test findings
<a name="step-5-review-penetration-test-findings"></a>

1. A penetration test can take several hours to complete. Most complete within 16 hours, depending on the size and complexity of your application.

1. The run begins with a **Preflight** phase that validates the setup before testing starts: it sets up logging infrastructure, checks that your target endpoints are reachable, and prepares the testing environment. If a preflight check fails (for example, a target domain that can’t be resolved), the run stops before testing begins. Open the **Preflight** tab to see which check failed, resolve it, and start a new run.

1. When the run completes, open it and review the **Run overview**, **Logs**, and **Findings** tabs.

1. On the **Findings** tab, select a finding to view its description, severity, risk type, and supporting evidence.

For more details, see [Create a penetration test](perform-penetration-test.md) and [Review findings from a penetration test](review-penetration-findings.md).