# Tag customer managed

policies

You can use IAM tag key-value pairs to add custom attributes to your customer managed
policies. For example, to tag a policy with department information, you can add the tag key
`Department` and the tag value `eng`. Or, you
might want to tag policies to indicate that they are for a specific environment, such as
`Environment = lab`. You can use tags to control access to
resources or to control what tags can be attached to a resource. To learn more about using
tags to control access, see [Controlling access to and for IAM users and roles using
tags](access_iam-tags.md "access_iam-tags.md").

You can also use tags in AWS STS to add custom attributes when you assume a role or federate
a user. For more information, see [Pass session tags in AWS STS](id_session-tags.md "id_session-tags.md").

## Permissions required for

tagging customer managed policies

You must configure permissions to allow an IAM entity (users or roles) to tag
customer managed policies. You can specify one or all of the following IAM tag actions
in an IAM policy:

- `iam:ListPolicyTags`
- `iam:TagPolicy`
- `iam:UntagPolicy`

###### To allow an IAM entity (user or role) to add, list, or remove a tag for a

customer managed policy

Add the following statement to the permissions policy for the IAM entity that
needs to manage tags. Use your account number and replace
`<policyname>` with the name of the policy whose
tags need to be managed. To learn how to create a policy using this example JSON
policy document, see [Creating policies using the JSON
editor](access_policies_create-console.md#access_policies_create-json-editor "access_policies_create-console.md#access_policies_create-json-editor").

```
{
    "Effect": "Allow",
    "Action": [
        "iam:ListPolicyTags",
        "iam:TagPolicy",
        "iam:UntagPolicy"
    ],
    "Resource": "arn:aws:iam::`<account-number>`:policy/`<policyname>`"
}
```

###### To allow an IAM entity (user or role) to add a tag to a specific customer

managed policy

Add the following statement to the permissions policy for the IAM entity that
needs to add, but not remove, tags for a specific policy.

###### Note

The `iam:TagPolicy` action requires that you also include the
`iam:ListPolicyTags` action.

To use this policy, replace `<policyname>` with the name
of the policy whose tags need to be managed. To learn how to create a policy using this
example JSON policy document, see [Creating policies using the JSON
editor](access_policies_create-console.md#access_policies_create-json-editor "access_policies_create-console.md#access_policies_create-json-editor").

```
{
    "Effect": "Allow",
    "Action": [
        "iam:ListPolicyTags",
        "iam:TagPolicy"
    ],
    "Resource": "arn:aws:iam::`<account-number>`:policy/`<policyname>`"
}
```

Alternatively, you can use an AWS managed policy such as [IAMFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/IAMFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/IAMFullAccess") to provide full access to IAM.

## Managing tags on IAM

customer managed policies (console)

You can manage tags for IAM customer managed policies from the AWS Management Console.

###### To manage tags on customer managed policies (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the console, choose **Policies**
   and then choose the name of the customer managed policy that you want to
   edit.
3. Choose the **Tags** tab and then
   choose
   **Manage
   tags**.
4. Add or remove tags to complete the set of tags. Then choose **Save
   changes**.

## Managing tags on IAM

customer managed policies (AWS CLI or AWS API)

You can list, attach, or remove tags for IAM customer managed policies. You can use
the AWS CLI or the AWS API to manage tags for IAM customer managed policies.

###### To list the tags currently attached to an IAM customer managed policy (AWS CLI or

AWS API)

- AWS CLI: [aws iam
  list-policy-tags](../../../cli/latest/reference/iam/list-policy-tags.md "../../../cli/latest/reference/iam/list-policy-tags.md")
- AWS API: [ListPolicyTags](../APIReference/API_ListPolicyTags.md "../APIReference/API_ListPolicyTags.md")

###### To attach tags to an IAM customer managed policy(AWS CLI or AWS API)

- AWS CLI: [aws iam
  tag-policy](../../../cli/latest/reference/iam/tag-policy.md "../../../cli/latest/reference/iam/tag-policy.md")
- AWS API: [TagPolicy](../APIReference/API_TagPolicy.md "../APIReference/API_TagPolicy.md")

###### To remove tags from an IAM customer managed policy (AWS CLI or AWS API)

- AWS CLI: [aws iam
  untag-policy](../../../cli/latest/reference/iam/untag-policy.md "../../../cli/latest/reference/iam/untag-policy.md")
- AWS API: [UntagPolicy](../APIReference/API_UntagPolicy.md "../APIReference/API_UntagPolicy.md")

For information about attaching tags to resources for other AWS services, see the
documentation for those services.

For information about using tags to set more granular permissions with IAM
permissions policies, see [IAM policy elements: Variables and tags](reference_policies_variables.md "reference_policies_variables.md").
