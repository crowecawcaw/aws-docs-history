# Tag account access manager instances

You must configure permissions to allow an IAM entity (roles or users) to tag account access manager
instances. You can specify one or all of the following account-access tag actions in an IAM
policy:

- `account-access:TagResource`
- `account-access:ListTagsForResource`
- `account-access:UntagResource`
  **To allow an IAM entity (role or user) to add, list, or remove a tag
  for an account access manager instance**

Add the following statement to the permissions policy for the IAM entity that needs to
manage tags. Use your account number and instance IDs of your IAM Identity Center and account access manager instances to
replace the placeholders. To learn how to create a policy using this example JSON policy
document, see [Create IAM policies (console)](access_policies_create-console.md "access_policies_create-console.md").

```
{
    "Effect": "Allow",
    "Action": [
        "account-access:TagResource",
        "account-access:ListTagsForResource",
        "account-access:UntagResource"
    ],
    "Resource": "<account_access_manager_ARN>"
}
```

**To allow an IAM entity (role or user) to add a tag to a specific
account access manager instance**

Add the following statement to the permissions policy for the IAM entity that needs to
add, but not remove, tags for a specific account access manager instance.

###### Note

The `account-access:TagResource` action requires that you also include the
`account-access:ListTagsForResource` action.

Use your account number and instance IDs of your IAM Identity Center and account access manager instances to replace
the placeholders. To learn how to create a policy using this example JSON policy document, see
[Create IAM policies (console)](access_policies_create-console.md "access_policies_create-console.md").

```
{
    "Effect": "Allow",
    "Action": [
        "account-access:TagResource",
        "account-access:ListTagsForResource"
    ],
    "Resource": "<account_access_manager_ARN>"
}
```

## Managing tags on account access manager (console)

You can manage tags for an account access manager instance from the AWS Management Console.

###### To manage tags on account access manager (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the console, choose **Account access manager**,
   and then choose the **Settings** tab.
3. In the **Tags** section, you can see currently configured
   tags. Choose **Manage tags** and then complete one of the
   following actions:

   - Choose **Add new tag** to add a new tag.
   - Edit existing tag keys and values.
   - Choose **Remove** to remove a tag.

4. Add or remove tags to complete the set of tags. Then choose **Save
   changes**.

## Managing tags on account access manager (AWS CLI or AWS API)

You can list, attach, or remove tags for account access manager instances using the AWS CLI or AWS
API.

**To list the tags currently attached to an account access manager instance (AWS CLI or
AWS API)**

- AWS CLI: `aws account-access list-tags-for-resource`
- AWS API: `account-access:ListTagsForResource`

**To attach tags to an account access manager instance (AWS CLI or AWS
API)**

- AWS CLI: `aws account-access tag-resource`
- AWS API: `TagResource`

**To remove tags from an account access manager instance (AWS CLI or AWS
API)**

- AWS CLI: `aws account-access untag-resource`
- AWS API: `UntagResource`

For information about attaching tags to resources for other AWS services, see the
documentation for those services.

For information about using tags to set more granular permissions with IAM permissions
policies, see [IAM policy elements: Variables and tags](reference_policies_variables.md "reference_policies_variables.md").
