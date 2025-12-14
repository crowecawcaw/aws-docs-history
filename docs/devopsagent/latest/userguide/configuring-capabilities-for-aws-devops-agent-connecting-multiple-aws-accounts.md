# Connecting multiple AWS Accounts

Secondary AWS accounts allow AWS DevOps Agent to investigate resources across multiple AWS accounts in your organization. When your applications span multiple accounts, adding secondary accounts ensures the agent has visibility into all relevant resources during incident investigations. Greater access to the accounts and resources composing an application ensures greater investigation accuracy.

## Prerequisites

Before adding a secondary AWS account, ensure you have:

- Access to the AWS DevOps Agent console in the primary account
- Administrative access to the secondary AWS account
- IAM permissions to create roles in the secondary account

## Adding a secondary AWS account

In addition to the steps below, you can use the [CLI onboarding guide](getting-started-with-aws-devops-agent-cli-onboarding-guide.md "getting-started-with-aws-devops-agent-cli-onboarding-guide.md") to programmatically add secondary accounts.

### Step 1: Start the secondary account configuration

1. Sign in to the AWS Management Console and navigate to the AWS DevOps Agent console
2. Select your Agent Space
3. Go to the **Capabilities** tab
4. In the **Cloud** section, locate the **Secondary sources** subsection
5. Click **Add**

### Step 2: Specify the role name

1. In the **Name your role** field, enter a name for the role you'll create in the secondary account
2. Note this name—you'll use it again when creating the role in the secondary account
3. Copy the trust policy provided in the console and save it in a scratch space

### Step 3: Create the role in the secondary account

1. Open a new browser tab and sign in to the IAM console in the secondary AWS account
2. Navigate to **IAM >\*\***Roles** > **Create role\*\*
3. Select **Custom trust policy**
4. Paste the trust policy you copied from Step 2
5. Click **Next**

### Step 4: Attach the AWS managed policy

1. In the **Permissions policies** section, search for **AIOpsAssistantPolicy**
2. Select the checkbox next to the **AIOpsAssistantPolicy** managed policy
3. Click **Next**

### Step 5: Name and create the role

1. In the **Role name** field, enter the same role name you provided in Step 2
2. (Optional) Add a description to help identify the role's purpose
3. Review the trust policy and attached permissions
4. Click **Create role**

### Step 6: Attach the inline policy

1. In the IAM console, locate and select the role you just created
2. Go to the **Permissions** tab
3. Click **Add permissions** > **Create inline policy**
4. Switch to the **JSON** tab
5. Paste the policy you saved in Step 2
6. Paste the policy into the JSON editor in the IAM console
7. Click **Next**
8. Provide a name for the inline policy (for example, "DevOpsAgentInlinePolicy")
9. Click **Create policy**

### Step 7: Complete the configuration

1. Return to the AWS DevOps Agent console in the primary account
2. Click **Next** to complete the secondary account configuration
3. Verify the connection status shows as **Active**

## Understanding the required policies

AWS DevOps Agent requires three policy components to access resources in a secondary account:

- **Trust policy** – Allows AWS DevOps Agent in the primary account to assume the role in the secondary account. This establishes the trust relationship between accounts.
- **AIOpsAssistantPolicy (AWS managed policy)** – Provides the core read-only permissions AWS DevOps Agent needs to investigate resources in the secondary account. This policy is maintained by AWS and updated as new capabilities are added.
- **Inline policy** – Provides additional permissions specific to your Agent Space configuration. This policy is generated based on your Agent Space settings and may include permissions for specific integrations or features.

In the primary account, the AWS DevOps Agent IAM Role must be able to assume the role created in the secondary account.

## Managing secondary accounts

- **Viewing connected accounts** – In the **Capabilities** tab, the **Secondary sources** subsection lists all connected secondary accounts with their connection status.
- **Updating the IAM role** – If you need to modify permissions, update the inline policy attached to the role in the secondary account. Changes take effect immediately.
- **Removing a secondary account** – To disconnect a secondary account, select it in the **Secondary sources** list and click **Remove**. This does not delete the IAM role in the secondary account.
