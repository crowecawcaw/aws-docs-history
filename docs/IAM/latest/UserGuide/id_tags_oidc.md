# Tag OpenID Connect (OIDC) identity providers

You can use IAM tag key-values to add custom attributes to IAM OpenID Connect (OIDC)
identity providers. For example, to identify an OIDC identity provider, you can add the tag
key `google` and the tag value `oidc`. You can use
tags to control access to resources or to control what tags can be attached to an object. To
learn more about using tags to control access, see [Controlling access to and for IAM users and roles using
tags](access_iam-tags.md "access_iam-tags.md").

## Permissions required for tagging IAM OIDC

identity providers

You must configure permissions to allow an IAM entity (user or role) to tag IAM
OIDC identity providers. You can specify one or all of the following IAM tag actions
in an IAM policy:

- `iam:ListOpenIDConnectProviderTags`
- `iam:TagOpenIDConnectProvider`
- `iam:UntagOpenIDConnectProvider`

###### To allow an IAM entity to add, list, or remove a tag for an IAM OIDC identity

provider

Add the following statement to the permissions policy for the IAM entity that
needs to manage tags. Use your account number and replace
`<OIDCProviderName>` with the name of the OIDC
provider whose tags need to be managed. To learn how to create a policy using this
example JSON policy document, see [Creating policies using the JSON
editor](access_policies_create-console.md#access_policies_create-json-editor "access_policies_create-console.md#access_policies_create-json-editor").

```
{
    "Effect": "Allow",
    "Action": [
        "iam:ListOpenIDConnectProviderTags",
        "iam:TagOpenIDConnectProvider",
        "iam:UntagOpenIDConnectProvider"
    ],
    "Resource": "arn:aws:iam::`<account-number>`:oidc-provider/`<OIDCProviderName>`"
}
```

###### To allow an IAM entity (user or role) to add a tag to a specific IAM OIDC

identity provider

Add the following statement to the permissions policy for the IAM entity that
needs to add, but not remove, tags for a specific identity provider.

###### Note

The `iam:TagOpenIDConnectProvider` action requires that you also
include the `iam:ListOpenIDConnectProviderTags` action.

To use this policy, replace `<OIDCProviderName>` with the
name of the OIDC provider whose tags need to be managed. To learn how to create a policy
using this example JSON policy document, see [Creating policies using the JSON
editor](access_policies_create-console.md#access_policies_create-json-editor "access_policies_create-console.md#access_policies_create-json-editor").

```
{
    "Effect": "Allow",
    "Action": [
        "iam:ListOpenIDConnectProviderTags",
        "iam:TagOpenIDConnectProvider"
    ],
    "Resource": "arn:aws:iam::`<account-number>`:oidc-provider/`<OIDCProviderName>`"
}
```

Alternatively, you can use an AWS managed policy such as [IAMFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/IAMFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/IAMFullAccess") to provide full access to IAM.

## Managing tags on IAM OIDC identity

providers (console)

You can manage tags for IAM OIDC identity providers from the AWS Management Console.

###### To manage tags on OIDC identity providers (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the console, choose **Identity
   providers** and then choose the name of the identity provider that
   you want to edit.
3. Choose the **Tags** tab, then in the
   **Tags** section, choose **Manage tags**
   and then complete one of the following actions:
   - Choose **Add tag** if the OIDC identity provider does
     not yet have tags or to add a new tag.
   - Edit existing tag keys and values.
   - Choose **Remove tag** to remove a tag.

4. Then choose **Save changes**.

## Managing tags on IAM OIDC identity

providers (AWS CLI or AWS API)

You can list, attach, or remove tags for IAM OIDC identity providers. You can use
the AWS CLI or the AWS API to manage tags for IAM OIDC identity providers.

###### To list the tags currently attached to an IAM OIDC identity provider (AWS CLI or

AWS API)

- AWS CLI: [aws iam list-open-id-connect-provider-tags](../../../cli/latest/reference/iam/list-open-id-connect-provider-tags.md "../../../cli/latest/reference/iam/list-open-id-connect-provider-tags.md")
- AWS API: [ListOpenIDConnectProviderTags](../APIReference/API_ListOpenIDConnectProviderTags.md "../APIReference/API_ListOpenIDConnectProviderTags.md")

###### To attach tags to an IAM OIDC identity provider (AWS CLI or AWS API)

- AWS CLI: [aws iam
  tag-open-id-connect-provider](../../../cli/latest/reference/iam/tag-open-id-connect-provider.md "../../../cli/latest/reference/iam/tag-open-id-connect-provider.md")
- AWS API: [TagOpenIDConnectProvider](../APIReference/API_TagOpenIDConnectProvider.md "../APIReference/API_TagOpenIDConnectProvider.md")

###### To remove tags from an IAM OIDC identity provider (AWS CLI or AWS API)

- AWS CLI: [aws
  iam untag-open-id-connect-provider](../../../cli/latest/reference/iam/untag-open-id-connect-provider.md "../../../cli/latest/reference/iam/untag-open-id-connect-provider.md")
- AWS API: [UntagOpenIDConnectProvider](../APIReference/API_UntagOpenIDConnectProvider.md "../APIReference/API_UntagOpenIDConnectProvider.md")

For information about attaching tags to resources for other AWS services, see the
documentation for those services.

For information about using tags to set more granular permissions with IAM
permissions policies, see [IAM policy elements: Variables and tags](reference_policies_variables.md "reference_policies_variables.md").
