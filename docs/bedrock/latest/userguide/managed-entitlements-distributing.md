

# Distributing licenses
<a name="managed-entitlements-distributing"></a>

After you have subscribed to a third-party Bedrock model and verified that a license has been created, you can create grants to distribute access to other accounts in your organization.

## Understanding grant distribution options
<a name="managed-entitlements-grant-options"></a>

You can distribute licenses using three methods:

**Individual account grants**: Create a grant for a specific AWS account ID. This method gives you precise control over which accounts receive access to the model. The recipient account must accept and activate the grant before using the model.

**Organization grants**: Create a single grant to your entire AWS Organization ID. This method automatically distributes the license to all member accounts in your organization. New accounts that join the organization automatically receive the license. For organizations with all features enabled, grants are automatically accepted and appear in a Disabled state, ready for activation.

**Organizational unit grants**: Create a grant to a specific organizational unit (OU) within your organization. This method distributes the license to all accounts within the specified OU, providing a middle ground between individual account control and organization-wide distribution.

## Create Grants
<a name="managed-entitlements-create-grants"></a>

### Console
<a name="managed-entitlements-create-grants-console"></a>

**To create a grant to an individual account**

1. Sign in to your management account (or delegated administrator account).

1. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. Make sure you are in the us-east-1 Region.

1. In the navigation pane, choose **Granted Licenses**.

1. Choose the license ID of the license you want to share to open the **License overview** page.

1. In the **Grants** section, choose **Create grant**.

1. Under **Grant details**, enter a descriptive name for the grant in **Grant name**.

1. Under **AWS account ID or AWS Organization ID or AWS Organizational Unit ID**, enter the 12-digit AWS account ID of the recipient account.

1. Review your grant details.

1. Choose **Create grant**.

AWS License Manager creates the grant, and it appears in the recipient account in a Pending Acceptance or Disabled state, depending on your organization configuration.

**To create a grant to your organization**

1. Follow steps 1-6 from the previous procedure.

1. Under **Grant details**, enter a descriptive name for the grant in **Grant name**.

1. Under **AWS account ID or AWS Organization ID or AWS Organizational Unit ID**, enter your AWS Organization ID.
   + To find your organization ID, open the AWS Organizations console. The ID appears in the navigation pane and starts with "o-".

1. Review your grant details.

1. Choose **Create grant**.

The grant is created and automatically distributed to all member accounts in your organization. For organizations with all features enabled, grants are automatically accepted and appear in a Disabled state in each member account.

**To create a grant to an organizational unit**

1. Follow steps 1-6 from the create individual grant procedure.

1. Under **Grant details**, enter a descriptive name for the grant in **Grant name**.

1. Under **AWS account ID or AWS Organization ID or AWS Organizational Unit ID**, enter your organizational unit (OU) ID.
   + To find your OU ID, open the AWS Organizations console and navigate to your OU. The ID starts with "ou-".

1. Review your grant details.

1. Choose **Create grant**.

The grant is created and automatically distributed to all member accounts within the specified organizational unit.

### API
<a name="managed-entitlements-create-grants-api"></a>

Creates a grant to distribute a license to other AWS accounts, organizations, or organizational units through [CreateGrantAPI](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateGrant.html)

The following AWS CLI procedure creates a grant for your organization. The `create-grant` command uses these values:

`grant-name`  
A name for the grant.

`license-arn`  
The ARN of the license that you received when you subscribed. You can find it in the output of the `list-received-licenses` command.

`home-region`  
Always `us-east-1`, because all licenses for third-party Bedrock models are managed in that Region.

`allowed-operations`  
The operations that recipients can perform with the license. Use `CheckoutLicense` and `ExtendConsumptionLicense`.

`principals`  
The ARN of your organization. To distribute to an organizational unit (OU), use an OU ARN such as `arn:aws:organizations::444455556666:ou/o-exampleorgid/ou-examplerootid-exampleouid`. To distribute to one account, use the 12-digit account ID.

The example values in the following commands are fictitious. Replace them with your own values. If you receive an `AccessDenied` error, verify that your IAM identity has the `license-manager:CreateGrant` permission.

**To create a grant with the AWS CLI**

1. Find the license ARN.

   ```
   aws license-manager list-received-licenses --region us-east-1
   ```

1. Find your organization ID and management account ID.

   ```
   aws organizations describe-organization
   ```

1. Create the grant. The following command creates the grant by using the values described earlier in this section.

   ```
   aws license-manager create-grant \
       --region us-east-1 \
       --client-token "$(uuidgen)" \
       --grant-name "{{my-bedrock-org-grant}}" \
       --license-arn "{{arn:aws:license-manager::111122223333:license:l-0123456789EXAMPLE}}" \
       --principals "{{arn:aws:organizations::444455556666:organization/o-exampleorgid}}" \
       --home-region us-east-1 \
       --allowed-operations "CheckoutLicense" "ExtendConsumptionLicense"
   ```

1. Check the grant status. Replace {{my-grant-arn}} with the grant ARN from the previous step.

   ```
   aws license-manager get-grant --region us-east-1 --grant-arn "{{my-grant-arn}}"
   ```

   The grant is ready to activate when its status is no longer `PENDING_WORKFLOW`. This might take a few minutes, so repeat the command until the status changes.

## Tracking distributed grants
<a name="managed-entitlements-tracking-grants"></a>

As the grantor or administrator, you can track all grants you have created.

### Console
<a name="managed-entitlements-tracking-grants-console"></a>

**To view your distributed grants**

1. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, choose **Granted Licenses**.

1. Choose the license for which you want to review grants.

1. On the license details page, scroll to the **Grants** section.

1. You will see a list of all grants created for this license, including grant name, recipient, and status.

For organization-wide grants, you can view individual account-level grant statuses by choosing the grant name to see the grant details page.

### API
<a name="managed-entitlements-tracking-grants-api"></a>

You can also view distributed grants using the [ListDistributedGrants API.](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListDistributedGrants.html)