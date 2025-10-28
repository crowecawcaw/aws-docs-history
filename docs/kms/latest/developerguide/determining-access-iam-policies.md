# Examining IAM policies

In addition to the key policy and grants, you can also use [IAM policies](iam-policies.md "iam-policies.md") to allow access to a KMS key. For more information about how IAM
policies and key policies work together, see [Troubleshooting AWS KMS permissions](policy-evaluation.md "policy-evaluation.md").

To determine which principals currently have access to a KMS key through IAM policies, you
can use the browser-based [IAM Policy
Simulator](https://policysim.aws.amazon.com/ "https://policysim.aws.amazon.com/") tool, or you can make requests to the IAM API.

###### Ways to examine IAM policies

- [Examining IAM policies with the
  IAM policy simulator](determining-access-iam-policies.md#determining-access-iam-policy-simulator "determining-access-iam-policies.md#determining-access-iam-policy-simulator")
- [Examining IAM policies with the IAM
  API](determining-access-iam-policies.md#determining-access-iam-api "determining-access-iam-policies.md#determining-access-iam-api")

## Examining IAM policies with the

IAM policy simulator

The IAM Policy Simulator can help you learn which principals have access to a KMS key
through an IAM policy.

###### To use the IAM policy simulator to determine access to a KMS key

1. Sign in to the AWS Management Console and then open the IAM Policy Simulator at [https://policysim.aws.amazon.com/](https://policysim.aws.amazon.com/ "https://policysim.aws.amazon.com/").
2. In the **Users, Groups, and Roles** pane, choose the user, group,
   or role whose policies you want to simulate.
3. (Optional) Clear the check box next to any policies that you want to omit from the
   simulation. To simulate all policies, leave all policies selected.
4. In the **Policy Simulator** pane, do the following:
   1. For **Select service**, choose **Key Management
      Service**.
   2. To simulate specific AWS KMS actions, for **Select actions**,
      choose the actions to simulate. To simulate all AWS KMS actions, choose
      **Select All**.

5. (Optional) The Policy Simulator simulates access to all KMS keys by default. To
   simulate access to a specific KMS key, choose **Simulation
   Settings**and then type the Amazon Resource Name (ARN) of the KMS key to
   simulate.
6. Choose **Run Simulation**.

You can view the results of the simulation in the **Results** section.
Repeat steps 2 through 6 for every user, group, and role in the AWS account.

## Examining IAM policies with the IAM

API

You can use the IAM API to examine IAM policies programmatically. The following
steps provide a general overview of how to do this:

1. For each AWS account listed as a principal in the key policy (that is, each [AWS account principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-accounts "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-accounts") specified in this format: `"Principal": {"AWS":
"arn:aws:iam::111122223333:root"}`), use the [ListUsers](../../../IAM/latest/APIReference/API_ListUsers.md "../../../IAM/latest/APIReference/API_ListUsers.md") and [ListRoles](../../../IAM/latest/APIReference/API_ListRoles.md "../../../IAM/latest/APIReference/API_ListRoles.md") operations in the IAM API to
   get all users and roles in the account.
2. For each user and role in the list, use the [SimulatePrincipalPolicy](../../../IAM/latest/APIReference/API_SimulatePrincipalPolicy.md "../../../IAM/latest/APIReference/API_SimulatePrincipalPolicy.md")
   operation in the IAM API, passing in the following parameters:
   - For `PolicySourceArn`, specify the Amazon Resource Name (ARN) of a
     user or role from your list. You can specify only one `PolicySourceArn`
     for each `SimulatePrincipalPolicy` request, so you must call this
     operation multiple times, once for each user and role in your list.
   - For the `ActionNames` list, specify every AWS KMS API action to
     simulate. To simulate all AWS KMS API actions, use `kms:*`. To test
     individual AWS KMS API actions, precede each API action with "`kms:`", for
     example "`kms:ListKeys`". For a complete list of AWS KMS API actions, see
     [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") in the
     _AWS Key Management Service API Reference_.
   - (Optional) To determine whether the users or roles have access to specific
     KMS keys, use the `ResourceArns` parameter to specify a list of the
     Amazon Resource Names (ARNs) of the KMS keys. To determine whether the users or
     roles have access to any KMS key, omit the `ResourceArns`
     parameter.

IAM responds to each `SimulatePrincipalPolicy` request with an
evaluation decision: `allowed`, `explicitDeny`, or
`implicitDeny`. For each response that contains an evaluation decision of
`allowed`, the response includes the name of the specific AWS KMS API operation
that is allowed. It also includes the ARN of the KMS key that was used in the evaluation, if
any.
