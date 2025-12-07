# Connecting multiple AWS Accounts

Secondary AWS accounts allow AWS DevOps Agent to investigate resources across multiple AWS accounts in your organization. When your applications span multiple accounts, adding secondary accountsensures the agent has visibilityinto all relevant resources during incident investigations.

## Prerequisites

Before adding a secondary AWS account, ensure you have:

- Access to the AWS DevOps Agent console in the primary account
- Administrative access to the secondary AWS account
- IAM permissions to create roles in the secondary account

## Addinga secondary AWS account

### Step 1: Start the secondary account configuration

- Sign in to the AWS Management Console and navigate to the AWS DevOps Agent console
- Select your Agent Space
- Go to the **Capabilities** tab
- In the **Cloud** section, locate the **Secondary sources** subsection
- Click **Add**

### Step 2: Specify the role name

- In the **Name your role** field, enter a name for the role you'll create in the secondary account
- Note this name—you'll use it again when creating the role in the secondary account
- Copy the trust policy provided in the console and save it in a scratch space

### Step 3: Create the role in the secondary account

- Open a new browser tab and sign in to the IAM console in the secondary AWS account
- Navigate to **IAM >\*\***Roles**>**Create role\*\*
- Select **Custom trust policy**
- Paste the trust policy you copied from Step 2
- Click **Next**

### Step 4: Attach the AWS managed policy

- In the **Permissions policies** section, search for **AIOpsAssistantPolicy**
- Select the checkbox next to the **AIOpsAssistantPolicy** managed policy
- Click **Next**

### Step 5: Name and create the role

- In the **Role name** field, enter the same role name you provided in Step 2
- (Optional) Add a description to help identify the role's purpose
- Review the trust policy and attached permissions
- Click **Create role**

### Step 6: Attach the inline policy

- In the IAM console, locate and select the role you just created
- Go to the **Permissions** tab
- Click **Add permissions**>**Create inline policy**
- Switch to the **JSON** tab
- Paste the policy you saved in Step 2
- Paste the policy into the JSON editor in the IAM console
- Click **Next**
- Provide a name for the inline policy (for example, "DevOpsAgentInlinePolicy")
- Click **Create policy**

### Step 7: Complete the configuration

- Return to the AWS DevOps Agent console in the primary account
- Click **Next** to complete the secondary account configuration
- Verify the connection status shows as **Active**

## Understanding the required policies

AWS DevOps Agent requires three policy components to access resources in a secondary account:

- **Trust policy**– Allows AWS DevOps Agent in the primary account to assume the role in the secondary account. This establishes the trust relationship between accounts.
- **AIOpsAssistantPolicy (AWS managed policy)**– Provides the core read-only permissions AWS DevOps Agent needs to investigate resources in the secondary account. This policy is maintained by AWS and updated as new capabilities are added.
- **Inline policy**– Provides additional permissions specific to your Agent Space configuration. This policy is generated based on your Agent Space settings and may include permissions for specific integrations or features.

In the primary account, the AWS DevOps Agent IAM Role must be able to assume the role created in the secondary account.

## Managing secondary accounts

- **Viewing connected accounts**– In the **Capabilities** tab, the **Secondary sources** subsection lists all connected secondary accounts with their connection status.
- **Updating the IAM role**– If you need to modify permissions, update the inline policy attached to the role in the secondary account. Changes take effect immediately.
- **Removing a secondary account**– To disconnect a secondary account, select it in the **Secondary sources** list and click **Remove**. This does not delete the IAM role in the secondary account.

​
