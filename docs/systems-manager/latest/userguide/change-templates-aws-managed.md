AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Try out the AWS managed

`Hello World` change template

###### Change Manager availability change

AWS Systems Manager Change Manager will no longer be open to new customers
starting November 7, 2025. If you would like to use Change Manager, sign up prior to that
date. Existing customers can continue to use the service as normal. For more
information, see [AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

You can use the sample change template
`AWS-HelloWorldChangeTemplate`, which uses the sample Automation
runbook `AWS-HelloWorld`, to test the review and approval process
after you have finished setting up Change Manager, a tool in AWS Systems Manager. This template
is designed for testing or verifying your configured permissions, approver
assignments, and approval process. Approval to use this change template in your
organization or account has already been provided by AWS. Any change request
based on this change template, however, must still be approved by reviewers in
your organization or account.

Rather than make changes to a resource, the result of the runbook workflow
associated with this template is to print a message in the output of an
Automation step.

###### Before you begin

Before you begin, ensure you have completed the following tasks:

- If you're using AWS Organizations to manage change across an organization,
  complete the organization setup tasks described in [Setting up Change Manager for an
  organization (management account)](change-manager-organization-setup.md "change-manager-organization-setup.md").
- Configure Change Manager for your delegated administrator account or single account, as
  described in [Configuring Change Manager options and best
  practices](change-manager-account-setup.md "change-manager-account-setup.md").

###### Note

If you turned on the best practice option **Require
monitors for all templates** in your Change Manager settings,
turn it off temporarily while you test the Hello World
change template.

###### To try out the AWS managed Hello World change template

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Change Manager**.
3. Choose **Create request**.
4. Choose the change template named
   `AWS-HelloWorldChangeTemplate`, and then choose
   **Next**.
5. For **Name**, enter a name for the change request
   that makes its purpose easy to identify, such as
   `MyChangeRequestTest`.
6. For the remainder of the steps to create your change request, see
   [Creating change requests](change-requests-create.md "change-requests-create.md").

###### Next steps

For information about approving change requests, see [Reviewing and approving or rejecting
change requests](change-requests-review.md "change-requests-review.md").

To view the status and results of your change request, choose the name of
your change request on the **Requests** tab in Change Manager.
