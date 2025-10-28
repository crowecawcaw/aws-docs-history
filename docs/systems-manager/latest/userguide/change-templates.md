# Working with change templates

###### Change Manager availability change

AWS Systems Manager Change Manager will no longer be open to new customers
starting November 7, 2025. If you would like to use Change Manager, sign up prior to that
date. Existing customers can continue to use the service as normal. For more
information, see [AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

A change template is a collection of configuration settings in Change Manager that define such
things as required approvals, available runbooks, and notification options for
change requests.

###### Note

AWS provides a sample [Hello
World](change-templates-aws-managed.md "change-templates-aws-managed.md") change template you can use to try out Change Manager, a tool in
AWS Systems Manager. However, you create your own change templates to define the changes
you want to allow to the resources in your organization or account.

The changes that are made when a runbook workflow runs are based on the contents
an Automation runbook. In each change template you create, you can include one or
more Automation runbooks that the user making a change request can choose from to
run during the update. You can also create change templates that allow requesters
to choose any available Automation runbook for the change request.

To create a change template, you can use the **Builder** option
in the **Create template** console page to build a change template.
Alternatively, using the **Editor** option, you can manually author
JSON or YAML content with the configuration you want for your runbook workflow. You
can also use a command line tool to create a change template, with JSON content for
the change template stored in an external file.

###### Topics

- [Try out the AWS managed
  Hello World change template](change-templates-aws-managed.md "change-templates-aws-managed.md")
- [Creating change templates](change-templates-create.md "change-templates-create.md")
- [Reviewing and approving or rejecting
  change templates](change-templates-review.md "change-templates-review.md")
- [Deleting change templates](change-templates-delete.md "change-templates-delete.md")
