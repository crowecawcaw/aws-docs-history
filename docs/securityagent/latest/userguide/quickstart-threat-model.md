# Quickstart: Run a threat model

This quickstart walks you through running your first threat model with AWS Security Agent. A threat model analyzes your application’s architecture and produces a **system overview** (how AWS Security Agent understands your system) and a set of **threats** (how it could be attacked, each with a severity level, STRIDE classification, and recommendations). You can run a threat model on design documents (**scope docs**) to define the focus, source code (**sources**) to provide context about your existing system, or both.

###### Note

You need access to the AWS Management Console to set up AWS Security Agent, and access to the web application to create and run threat models.

## Step 1: Set up AWS Security Agent in the AWS console

If you haven’t already set up AWS Security Agent, complete the initial setup:

1. Navigate to [AWS Security Agent](https://console.aws.amazon.com/securityagent/ "https://console.aws.amazon.com/securityagent/") in the AWS Management Console.
2. Select **Set up AWS Security Agent**.
3. Create an Agent Space. An agent space can be used by multiple users and should be specific for every application you want to secure. Enter a name and description for your first agent space. The name should identify the application you want to threat model.
4. Select **IAM-only access** under _User access configuration_.

   - This quickstart does not cover enabling single sign-on (SSO) with IAM Identity Center. This allows users to directly access the AWS Security Agent web application from the AWS Console.
   - If you want to enable users without AWS Management Console access to perform tasks such as starting a threat model, you should enable the IAM Identity Center integration.

5. Choose **Set up AWS Security Agent**.

###### Note

When you choose Set up, AWS Security Agent creates your Agent Space and establishes a web application where your users can carry out threat models and other security assessments.

## Step 2: Connect source code

###### Note

If you already have repositories or S3 buckets connected to your Agent Space (for example, through code review or penetration testing setup), you can skip this step and go directly to the web application. You can always run a threat model on uploaded scope docs without connecting any source code.

Connect repositories or S3 buckets that contain the source code you want the agent to use as context for understanding your existing system:

1. From the left sidebar, select **Agent Spaces** and then select your Agent Space.
2. Navigate to the **Integrations** section to connect your source code provider.
3. Alternatively, connect S3 buckets that contain your source code.

For the full integration flow, see [Connect AWS Security Agent to GitHub repositories](connect-github.md "connect-github.md").

## Step 3: Create and run a threat model

###### Note

You create and run threat models in the AWS Security Agent web application.

1. Launch the web application from the **Web app** tab in the AWS Management Console. Alternatively, if you have IAM Identity Center configured, log in directly.
2. In the left sidebar, choose **Threat models**.
3. Choose **Create threat model**.
4. Configure the threat model:

   1. Enter a **Title** that identifies the scope of this threat model (for example, "billing-service" or "checkout-api").
   2. Provide at least one input:

      - Under **Scope docs**, upload design documents (DOC, DOCX, JPEG, MD, PDF, PNG, or TXT), enter S3 URIs, or select Confluence pages.
      - Under **Sources**, select repositories from your connected integrations or enter S3 URIs containing source code.

      ###### Tip

      Provide **both** sources and scope docs to scope the threat model to a specific design (for example, a feature design document) while giving the agent your source code as context to understand your existing system.

   3. Select the **Service role** from your configured roles.
   4. (Optional) Select a **Log group** for CloudWatch logs.

5. Choose **Create threat model**.
6. On the threat model detail page, choose **Start run**.

## Step 4: Review threats

1. The run progresses through its analysis tasks. You can monitor progress on the **Preflight** tab and view task details on the **Logs** tab.
2. Once complete, the run status changes to **Completed**.
3. Select the **Overview** tab to review the system overview and severity distribution.
4. Select the **Threats** tab to review identified threats:

   1. Select a threat from the list to view its details in the side panel.
   2. Review the **Statement**, **Severity**, **STRIDE categories**, **Recommendation**, **Evidence**, and other fields.
   3. Update the threat status to **Resolved** or **Dismissed** as you address or triage each threat.

For more details, see [Create a threat model](perform-threat-model.md "perform-threat-model.md") and [Review threats from a threat model](review-threat-model-findings.md "review-threat-model-findings.md").
