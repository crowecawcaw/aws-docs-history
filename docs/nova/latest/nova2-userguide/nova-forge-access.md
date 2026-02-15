# Nova Forge access and setup

To get onboarded to Nova Forge, follow this 2-step process:

- Step 1: Subscribe to Nova Forge
- Step 2: Set up HyperPod infrastructure

## Step 1: Subscribe to Nova Forge

### Quick Summary:

1. Verify that you have administrator access to the Amazon Web Services account.
2. Navigate to the SageMaker AI AI console and request access to Nova Forge.
3. Wait for the Nova team to email a confirmation after your subscription request is approved.
4. Tag your execution role with the `forge-subscription` tag. This tag is required to access Nova Forge features and checkpoints. Add the following tag to your execution role:
   - Key: `forge-subscription`
   - Value: `true`

### Detailed Guide

To subscribe to Nova Forge and effectively use the customization service, an Amazon Web Services customer must have admin access to their Amazon Web Services account or have their administrator grant them admin access. This document outlines the steps required to:

- Secure admin access
- Set up policies to subscribe to Nova Forge
- Access customization recipes
- Configure customization
- Monitor the workflow
- Evaluate the customized model checkpoint

### Option A

Flow 1: The account user must reach out to the account admin to request the following:

- Add the `forge-subscription` tag to the account through IAM (see Appendix A for steps).
- Add the `ListRoleTags` and `ListAttachedRolePolicies` permissions through IAM (see Appendix B for steps).

### Option B

Flow: The account user must reach out to the account admin to request admin access to the account.

- Once admin access is granted, follow the steps in Flow 2.

### Flow 2. Amazon Web Services account w/ admin access

- Add forge-subscription tag to account through IAM. See Steps in Appendix A

### Appendix A. Add forge-subscription policy to Amazon Web Services account

1. Go to the Amazon Web Services IAM Dashboard. Click on Roles on the left. Search for admin and click on the admin role
2. Select <AssumedRoleToUse> (e.g., libsAdminAccess). Click on the Tags tab.
3. Click on Manage tabs. Add new tag. Type "forge-subscription" under Key and click on save changes
4. Ensure that you see forge-subscription as a key in Tags section

### Appendix B. Add ListRoleTags and ListAttachedPolicies policies to Amazon Web Services account for Non-Admin Role by Admin

1. Go to the Amazon Web Services IAM Dashboard. Click on Roles on the left. Search for <AssumedRoleToUse> (e.g., ForgeAccessRole) and click on the <AssumedRoleToUse> (e.g., ForgeAccessRole) role
2. Click on the <AssumedRoleToUse> (e.g., ForgeAccessRole) role and select Tags. Add a new tag with type "forge-subscription"
3. Under Permissions, add new permission: Add Permissions → Create inline policy → Add the following policy listed below

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:ListRoleTags",
                "iam:ListAttachedRolePolicies"
            ],
            "Resource": "*"
        }
    ]
}

```

## Step 2. Set up HyperPod infrastructure

Set up the necessary infrastructure by following the [workshop instructions](https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US") for configuring the environment with Forge-enabled features.

## Content moderation settings

If you need access to Nova Forge, customizable content moderation settings (CCMS) are available for Amazon Nova Lite 1.0 and Pro 1.0 models. CCMS allows adjustment of content moderation controls to align with specific business requirements while maintaining essential responsible AI safeguards. To determine if a business model is appropriate for CCMS, contact an AWS Account Manager.

For additional information on configuring and using CCMS with custom models, see the [Responsible AI Toolkit and Content Moderation section](nova-responsible-ai-toolkit.md "nova-responsible-ai-toolkit.md").
