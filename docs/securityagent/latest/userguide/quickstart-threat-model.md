

# Quickstart: Run a threat model
<a name="quickstart-threat-model"></a>

This quickstart walks you through running your first threat model with AWS Security Agent. A threat model analyzes your application’s architecture and produces a **system overview** (how AWS Security Agent understands your system) and a set of **threats** (how it could be attacked, each with a severity level, STRIDE classification, and recommendations). You can run a threat model on design documents (**scope docs**) to define the focus, source code (**sources**) to provide context about your existing system, or both.

**Note**  
You need access to the AWS Management Console to set up AWS Security Agent, and access to the web application to create and run threat models.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, make sure you have:
+ Access to the AWS Management Console with permissions to set up AWS Security Agent.
+ At least one input for the agent to analyze: design documents to upload as scope docs, or a source code repository (GitHub, GitLab, or Bitbucket) or Amazon S3 source to provide as context.

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

## Step 2: Connect source code
<a name="step-2-connect-source-code"></a>

**Note**  
If you already have repositories or S3 buckets connected to your Agent Space (for example, through code review or penetration testing setup), you can skip this step and go directly to the web application. You can always run a threat model on uploaded scope docs without connecting any source code.

Connect repositories or S3 buckets that contain the source code you want the agent to use as context for understanding your existing system:

1. From the left sidebar, select **Agent Spaces** and then select your Agent Space.

1. Navigate to the **Integrations** section to connect your source code provider.

1. Alternatively, connect S3 buckets that contain your source code.

For the full integration flow, see [Connect AWS Security Agent to GitHub repositories](connect-github.md).

## Step 3: Create and run a threat model
<a name="step-3-create-and-run-a-threat-model"></a>

**Note**  
You create and run threat models in the AWS Security Agent web application.

1. Launch the web application from the **Web app** tab in the AWS Management Console. Alternatively, if you have IAM Identity Center configured, log in directly.

1. In the left sidebar, choose **Threat models**.

1. Choose **Create threat model**.

1. Configure the threat model:

   1. Enter a **Title** that identifies the scope of this threat model (for example, "billing-service" or "checkout-api").

   1. Provide at least one input:
      + Under **Scope docs**, upload design documents (DOC, DOCX, JPEG, MD, PDF, PNG, or TXT), enter S3 URIs, or select Confluence pages.
      + Under **Sources**, select repositories from your connected integrations or enter S3 URIs containing source code.
**Tip**  
Provide **both** sources and scope docs to scope the threat model to a specific design (for example, a feature design document) while giving the agent your source code as context to understand your existing system.

   1. Select the **Service role** from your configured roles.

   1. (Optional) Select a **Log group** for CloudWatch logs.

1. Choose **Create threat model**.

1. On the threat model detail page, choose **Start run**.

## Step 4: Review threats
<a name="step-4-review-threats"></a>

1. The run progresses through its analysis tasks. You can monitor progress on the **Preflight** tab and view task details on the **Logs** tab.

1. Once complete, the run status changes to **Completed**.

1. Select the **Overview** tab to review the system overview and severity distribution.

1. Select the **Threats** tab to review identified threats:

   1. Select a threat from the list to view its details in the side panel.

   1. Review the **Statement**, **Severity**, **STRIDE categories**, **Recommendation**, **Evidence**, and other fields.

   1. Update the threat status to **Resolved** or **Dismissed** as you address or triage each threat.

For more details, see [Create a threat model](perform-threat-model.md) and [Review threats from a threat model](review-threat-model-findings.md).