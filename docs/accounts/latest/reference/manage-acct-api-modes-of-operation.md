# Understanding API modes of operation

The API operations that work with an AWS account's attributes always work in one of two
modes of operation:

- **Standalone context** – this mode is used
  when a user or role in an account accesses or changes an account attribute in the
  **_same
  account_**. The standalone context mode is automatically used
  when you **_don't_** include the
  `AccountId` parameter when you call one of the Account Management AWS CLI or AWS
  SDK operations.
- **Organizations context** – this mode is used when a
  user or role in one account in an organization accesses or changes an account
  attribute in a different member account in the same organization. The organizations
  context mode is automatically used when you **_do_** include the `AccountId` parameter when
  you call one of the Account Management AWS CLI or AWS SDK operation. You can call the operations
  in this mode from only the management account of the organization, or the delegated
  admin account for Account Management.
  The AWS CLI and AWS SDK operations can work in either standalone or organizations
  context.

- If you **_don't_**
  include the `AccountId` parameter, then the operation runs in the
  standalone context and automatically applies the request to the account you used to
  make the request. This is true whether or not the account is a member of an
  organization.
- If you do include the `AccountId` parameter, then the operation runs in
  the organizations context, and the operation works on the specified Organizations
  account.
  - If the account calling the operation is the management account or the
    delegated admin account for the Account Management service, then you can specify any
    member account of that organization in the `AccountId` parameter
    to update the specified account.
  - The only account in an organization that can call one of the alternate
    contact operations and specify its own account number in the
    `AccountId` parameter is the account specified as the [delegated admin account](using-orgs-delegated-admin.md "using-orgs-delegated-admin.md") for
    the Account Management service. Any other account, including the management account,
    receives an `AccessDenied` exception.

- If you run an operation in standalone mode, then you must be permitted to run the
  operation with an IAM policy that includes a `Resource` element of
  either `"*"` to allow all resources, or an [ARN that uses the syntax for a standalone
  account](#account-arn-standalone "#account-arn-standalone").
- If you run an operation in organizations mode, then you must be permitted to run
  the operation with an IAM policy that includes a `Resource` element of
  either `"*"` to allow all resources, or an [ARN that uses the syntax for a member
  account in an organization](#account-arn-organizations "#account-arn-organizations").

## Granting permissions to update account attributes

As with most AWS operations, you grant permissions to add, update, or delete account
attributes for AWS accounts by using [IAM permission policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md"). When
you attach an IAM permission policy to an IAM principal (either a user or role), you
specify which actions that principal can perform on which resources, and under what
conditions.

The following are some Account Management specific considerations for creating a permissions
policy.

### Amazon Resource Name format for AWS accounts

- The [Amazon Resource Name
  (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") for an AWS account that you can include in the
  `resource` element of a policy statement is constructed
  differently based on whether the account you want to reference is a
  standalone account or an account that is in an organization. See the
  previous section on [Understanding API modes of operation](manage-acct-api-modes-of-operation.md "manage-acct-api-modes-of-operation.md").
  - An account ARN for a standalone account:

  ```
  arn:aws:account::`{AccountId}`:account
  ```

  You must use this format when you run an account attributes
  operation in standalone mode by not including the
  `AccountID` parameter.
  - An account ARN for a member account in an organization:

  ```
  arn:aws:account::`{ManagementAccountId}`:account/o-`{OrganizationId}`/`{AccountId}`
  ```

  You must use this format when you run an account attributes
  operation in organizations mode by including the
  `AccountID` parameter.

### Context keys for IAM policies

The Account Management service also provides several [Account Management
service-specific condition keys](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys") that provide fine-grained control over
the permissions you grant.

#### `account:AccountResourceOrgPaths`

The context key `account:AccountResourceOrgPaths` lets you specify
a path through your organization's hierarchy to a specific organizational unit
(OU). Only member accounts that are contained by that OU match the condition.
The following example snippet restricts the policy to apply to only accounts
that are in either of two specified OUs.

Because `account:AccountResourceOrgPaths` is a multi-valued string
type, you must use the [`ForAnyValue` or `ForAllValues` multi-value
string operators](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions"). Also, note that the prefix on the condition key is
`account`, even though you're referencing paths to OUs in an
organization.

```
"Condition": {
    "ForAnyValue:StringLike": {
        "account:AccountResourceOrgPaths": [
            "`o-aa111bb222`/`r-a1b2`/`ou-a1b2-f6g7h111`/*",
            "`o-aa111bb222`/`r-a1b2`/`ou-a1b2-f6g7h222`/*"
        ]
    }
}
```

#### `account:AccountResourceOrgTags`

The context key `account:AccountResourceOrgTags` lets you reference
the tags that can be attached to an account in an organization. A tag is a
key/value string pair that you can use to categorize and label the resources in
your account. For more information about tagging, see [Tag
Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") in the _AWS Resource Groups User Guide_.
For information about using tags as part of an attribute-based access control
strategy, see [What
is ABAC for AWS](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. The following example snippet restricts the
policy to apply to only accounts in an organization that have the tag with the
key `project` and a value of either `blue` or
`red`.

Because `account:AccountResourceOrgTags` is a multi-valued string
type, you must use the [`ForAnyValue` or `ForAllValues` multi-value
string operators](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions"). Also, note that the prefix on the condition key is
`account`, even though you're referencing the tags on an
organization's member account.

```
"Condition": {
    "ForAnyValue:StringLike": {
        "account:AccountResourceOrgTags/project": [
            "blue",
            "red"
        ]
    }
}
```

###### Note

You can attach tags to only an account in an organization. You can't
attach tags to a standalone AWS account.
