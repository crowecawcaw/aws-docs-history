# Adding, updating, and removing tags

When you sign in to your organization's management account, you can add tags to the
resources in your organization.

## Adding tags to a resource when you create it

###### Minimum permissions

To add tags to a resource when you create it, you need the following
permissions:

- Permission to create a resource of the specified type
- `organizations:TagResource`
- `organizations:ListTagsForResource`
  – required only when using the Organizations console

You can include tag keys and values that are attached to the following
resources as you create them.

- AWS account
  - [Created
    account](orgs_manage_accounts_create.md "orgs_manage_accounts_create.md")
  - [Invited
    account](orgs_manage_accounts_invite-account.md "orgs_manage_accounts_invite-account.md")

- [Organizational unit (OU)](create_ou.md "create_ou.md")
- Policy
  - [Service control policy](orgs_policies_create.md#create-an-scp "orgs_policies_create.md#create-an-scp")
  - [Resource control policy](orgs_policies_create.md#create-an-rcp "orgs_policies_create.md#create-an-rcp")
  - [Declarative policy](orgs_policies_create.md#create-declarative-policy-procedure "orgs_policies_create.md#create-declarative-policy-procedure")
  - [Backup
    policy](orgs_policies_create.md#create-backup-policy-procedure "orgs_policies_create.md#create-backup-policy-procedure")
  - [Tag
    policy](orgs_policies_create.md#create-tag-policy-procedure "orgs_policies_create.md#create-tag-policy-procedure")
  - [Chat applications policy](orgs_policies_create.md#create-chatbot-policy-procedure "orgs_policies_create.md#create-chatbot-policy-procedure")
  - [AI services
    opt-out policy](orgs_policies_create.md#create-ai-opt-out-policy-procedure "orgs_policies_create.md#create-ai-opt-out-policy-procedure")

The organization root is created when you initially create the organization, so
you can only add tags to it as an existing resource.

## Adding or updating tags for an existing

resource

You can also add new tags or update the values of tags attached to existing
resources.

###### Minimum permissions

To add or update tags to resources in your organization, you need the
following permissions:

- `organizations:TagResource`
- `organizations:ListTagsForResource`
  – required only when using the Organizations console
  To remove tags from resources in your organization, you need the following
  permissions:

- `organizations:UntagResource`

AWS Management Console

###### To add, update, or remove tags for an existing resource

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. Navigate to and choose the account, Root, OU, or policy, and
   click on its name to open its detail page.
3. On the **Tags** tab, choose **Manage
   tags**.
4. You can add new tags, modify the values of existing tags, or
   remove tags.

To add a tag, choose **Add tag**, and then
enter a **Key** and, optionally, a
**Value** for the tag.

To remove a tag, choose **Remove**.

Tag keys and values are case sensitive. Use the capitalization
that you want to standardize on. You must also comply with the
requirements of any tag policies that apply. 5. Repeat the previous step as many times as you need. 6. Choose **Save changes**.

AWS CLI & AWS SDKs

###### To add or update tags to an existing resource

You can use one of the following commands to add tags to the
taggable resources in your organization:

- AWS CLI: [tag-resource](../../../cli/latest/reference/organizations/tag-resource.md "../../../cli/latest/reference/organizations/tag-resource.md")
- AWS SDKs: [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")

###### To delete tags from a resource in your organization

You can use one of the following commands to delete tags:

- AWS CLI: [untag-resource](../../../cli/latest/reference/organizations/untag-resource.md "../../../cli/latest/reference/organizations/untag-resource.md")
- AWS SDKs: [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
