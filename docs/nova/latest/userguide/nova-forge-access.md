

# Nova Forge access and setup
<a name="nova-forge-access"></a>

To get onboarded to Nova Forge, follow this 2-step process:
+ Step 1: Subscribe to Nova Forge
+ Step 2: Set up HyperPod infrastructure

## Getting the Nova Forge documents
<a name="nova-forge-get-docs"></a>

To get the Nova Forge documents follow the below steps:

```
mkdir NovaForgeHyperpodCLI
cd NovaForgeHyperpodCLI
aws s3 cp s3://nova-forge-c7363-206080352451-us-east-1/v1/ ./ --recursive
pip install -e .
```

## Step 1: Subscribe to Nova Forge
<a name="nova-forge-step1"></a>

### Quick Summary:
<a name="nova-forge-quick-summary"></a>

1. Verify that you have administrator access to the Amazon Web Services account.

1. Navigate to the SageMaker AI console and request access to Nova Forge.

1. Wait for the Nova team to email a confirmation after your subscription request is approved.

1. Tag your SageMaker HyperPod execution role with the `forge-subscription` tag. This tag is required to access Nova Forge features and checkpoints. Add the following tag to your execution role:
   + Key: `forge-subscription`
   + Value: `true`

### Detailed Guide
<a name="nova-forge-detailed-guide"></a>

To subscribe to Nova Forge and effectively use the customization service, an Amazon Web Services customer must have admin access to their Amazon Web Services account or have their administrator grant them admin access. This document outlines the steps required to:
+ Secure admin access
+ Set up policies to subscribe to Nova Forge
+ Access customization recipes
+ Configure customization
+ Monitor the workflow
+ Evaluate the customized model checkpoint

### Option A
<a name="nova-forge-option-a"></a>

Flow 1: The account user must reach out to the account admin to request the following:
+ Add the `forge-subscription` tag to the account through IAM (see Appendix A for steps).
+ Add the `ListRoleTags` and `ListAttachedRolePolicies` permissions through IAM (see Appendix B for steps).

![Nova Forge subscription page showing not subscribed status with setup requirements banner.](http://docs.aws.amazon.com/nova/latest/userguide/images/Onboarding-option-a.png)


### Option B
<a name="nova-forge-option-b"></a>

Flow: The account user must reach out to the account admin to request admin access to the account.
+ Once admin access is granted, follow the steps in Flow 2.

### Flow 2. Amazon Web Services account with admin access
<a name="nova-forge-flow2"></a>
+ Add forge-subscription tag to account through IAM. See Steps in Appendix A

### Appendix A. Add forge-subscription policy to Amazon Web Services account
<a name="nova-forge-appendix-a"></a>

1. Go to the Amazon Web Services IAM Dashboard. Click on Roles on the left. Search for a role with Admin permissions and select it.  
![IAM console showing Roles page with admin search filter applied and one matching role displayed.](http://docs.aws.amazon.com/nova/latest/userguide/images/add-forge-sub-policy.png)

1. Select <AssumedRoleToUse>. Click on the Tags tab.  
![Tags tab showing two tags with key forge-subscription for the IAM role.](http://docs.aws.amazon.com/nova/latest/userguide/images/add-forge-sub-policy-2.png)

1. Click on Manage tabs. Add new tag. Type "forge-subscription" under Key and click on save changes  
![Tags container showing two tags with keys forge-subscription and prime-subscription, each with matching values.](http://docs.aws.amazon.com/nova/latest/userguide/images/add-forge-sub-tag-policy.png)

1. Ensure that you see forge-subscription as a key in Tags section  
![Tags section showing forge-subscription as a key in the IAM role details page.](http://docs.aws.amazon.com/nova/latest/userguide/images/forge-tag-policy-verify.png)

### Appendix B. Add ListRoleTags and ListAttachedPolicies policies to Amazon Web Services account for Non-Admin Role by Admin
<a name="nova-forge-appendix-b"></a>

1. Go to the Amazon Web Services IAM Dashboard. Click on Roles on the left. Search for <AssumedRoleToUse> (e.g., ForgeAccessRole) and click on the <AssumedRoleToUse> (e.g., ForgeAccessRole) role  
![IAM Roles page filtered by forge showing ForgeAccessRole in the results list.](http://docs.aws.amazon.com/nova/latest/userguide/images/forge-list-tags-policy.png)

1. Click on the <AssumedRoleToUse> (e.g., ForgeAccessRole) role and select Tags. Add a new tag with type "forge-subscription"  
![Tags tab showing forge-subscription key-value pair tag in ForgeAccessRole interface.](http://docs.aws.amazon.com/nova/latest/userguide/images/forge-tag-appendix.png)

1. Under Permissions, add new permission: Add Permissions → Create inline policy → Add the following policy listed below

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
![ForgeAccessRole details page showing creation date, permissions policies, and JSON policy document with VisualEditor and RolePlus actions.](http://docs.aws.amazon.com/nova/latest/userguide/images/forge-add-tag-polices-example.png)

## Step 2. Set up HyperPod infrastructure
<a name="nova-forge-step2"></a>

Set up the necessary SageMaker HyperPod infrastructure by following the [workshop instructions](https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US) for configuring the environment with Forge-enabled features.

## Content moderation settings
<a name="nova-forge-content-moderation"></a>

If you need access to Nova Forge, customizable content moderation settings (CCMS) are available for Amazon Nova Lite 1.0 and Pro 1.0 models. CCMS allows adjustment of content moderation controls to align with specific business requirements while maintaining essential responsible AI safeguards. To determine if a business model is appropriate for CCMS, contact an Amazon Web Services Account Manager.

For additional information on configuring and using CCMS with custom models, see the [Responsible AI Toolkit and Content Moderation section](nova-responsible-ai-toolkit.md).