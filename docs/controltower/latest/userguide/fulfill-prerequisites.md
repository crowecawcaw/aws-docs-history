# If the account does not meet the

prerequisites

Remember that, as a prerequisite, accounts eligible to be enrolled into AWS Control Tower
governance must be part of the same overall organization. To fulfill this prerequisite
for account enrollment, you can follow these preparatory steps to move an account into
the same organization as AWS Control Tower.

###### Preparatory steps to bring an account into the same organization as

AWS Control Tower

1. Drop the account from its existing organization. You must provide a separate
   payment method if you use this approach.
2. Invite the account to join the AWS Control Tower organization. For more information,
   see [Inviting an AWS account to join your organization](../../../organizations/latest/userguide/orgs_manage_accounts_invites.md "../../../organizations/latest/userguide/orgs_manage_accounts_invites.md") in the
   _AWS Organizations User Guide_.
3. Accept the invitation. The account shows up in the root of the organization.
   This step moves the account into the same organization as AWS Control Tower. and
   establishes SCPs and consolidated billing.

###### Tip

You can send the invitation for the new organization before the account drops out
of the old organization. The invitation will be waiting when the account officially
drops out of its existing organization.

###### Steps to fulfill the remaining prerequisites:

1. Create the necessary `AWSControlTowerExecution` role.
2. Clear out the default VPC. (This part is optional. AWS Control Tower doesn't change
   your existing default VPC.)
3. Delete or modify any existing AWS Config configuration recorder or delivery channel
   through the AWS CLI or AWS CloudShell. For more information, see [Enroll accounts with AWS Config resources](enroll-account.md#example-config-cli-commands "enroll-account.md#example-config-cli-commands") and [Enroll accounts that have existing AWS Config
   resources](existing-config-resources.md "existing-config-resources.md")
   After you've completed these preparatory steps, you can enroll the account into
   AWS Control Tower. For more information, see [Steps to enroll an account manually](quick-account-provisioning.md#enrollment-steps "quick-account-provisioning.md#enrollment-steps"). This step brings the account into full AWS Control Tower
   governance.

###### Optional steps to deprovision an account, so it can be enrolled and keep its

stack

1. To keep the applied AWS CloudFormation stack, delete the stack instance from the stack
   sets, and choose **Retain stacks** for the instance.
2. Terminate the account provisioned product in AWS Service Catalog Account Factory. (This step
   only removes the provisioned product from AWS Control Tower. It doesn't delete the
   account.)
3. Set up the account with the necessary billing details, as required for any
   account that doesn't belong to an organization. Then remove the account from the
   organization. (You do this, so the account doesn't count against the total in
   your AWS Organizations quota.)
4. Clean up the account if resources remain, and then close it, following the
   account closure steps in [Unenroll an account](unmanage-account.md "unmanage-account.md").
5. If you have a **Suspended** OU with defined controls, you
   can move the account there instead of doing Step 1.
