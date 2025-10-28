# Roles in

different AWS account for cross-account access - optional

When your resources are located in secondary/resource accounts, you must
create roles in each of these accounts to enable AWS Resilience Hub to successfully
assess your application. The role creation procedure is similar to the
invoker role creation process, except for the trust policy
configuration.

###### Note

You must create the roles in secondary accounts where the resources
are located.

**Topics**

- [Creating a role in the IAM console for secondary/resource
  accounts](#security-iam-resilience-cross-create-roles-infra-account "#security-iam-resilience-cross-create-roles-infra-account")
- [Managing roles with the IAM API](#security-iam-resilience-cross-create-roles-infra-account-api "#security-iam-resilience-cross-create-roles-infra-account-api")
- [Defining trust policy using JSON file](#security-iam-resilience-cross-define-trust-policy-infra-account "#security-iam-resilience-cross-define-trust-policy-infra-account")

## Creating a role in the IAM console for secondary/resource

accounts

To enable AWS Resilience Hub to access AWS services and resources in other
AWS accounts, you must create roles in each of these accounts.

###### To create a role in the IAM console for the secondary/resource

accounts using IAM console

1. Open the IAM console at
   `https://console.aws.amazon.com/iam/`.
2. From the navigation pane, choose **Roles**
   and then choose **Create role**.
3. Select **Custom Trust Policy**, copy the
   following policy in the **Custom trust policy**
   window, and then choose **Next**.

###### Note

If your resources are in different accounts, you have to
create a role in each of those accounts and use the
secondary account trust policy for the other
accounts. 4. In the **Permissions policies** section of
**Add permissions** page, enter
`AWSResilienceHubAsssessmentExecutionPolicy` in
the **Filter policies by property or policy name and
press enter** box. 5. Select the policy and choose **Next**. 6. In **Role details** section, enter a unique
role name (such as `AWSResilienceHubAssessmentRole`)
in the **Role name** box. 7. (Optional) Enter a description about the role in the
**Description** box. 8. Choose **Create Role**.

To edit the use cases and permissions, in step 6, choose
**Edit** button that is located to the
right of **Step 1: Select trusted entities**
or **Step 2: Add permissions** sections.

In addition, you also need to add the `sts:assumeRole`
permission to the invoker role to enable it to assume the roles in your
secondary accounts.

Add the following policy to your invoker role for each of the
secondary roles you created:

```
{
    "Effect": "Allow",
    "Resource": [
      "arn:aws:iam::secondary_account_id_1:role/RoleInSecondaryAccount_1",
      "arn:aws:iam::secondary_account_id_2:role/RoleInSecondaryAccount_2",
      ...
      ],
      "Action": [
        "sts:AssumeRole"
      ]
}
```

### Managing roles with the IAM API

A role's trust policy gives the specified principal's permission
to assume the role. To create the roles using AWS Command Line Interface (AWS CLI), use
the `create-role` command. When using this command, you
can specify the trust policy inline. The following example shows how
to grant the AWS Resilience Hub service principal permission to assume your
role.

###### Note

The requirement to escape quotes (`' '`) in the
JSON string may vary based on your shell version.

**Sample
`create-role`**

```
aws iam create-role --role-name AWSResilienceHubAssessmentRole --assume-role-policy-document '{"Version": "2012-10-17",		 	 	 "Statement": [{"Effect": "Allow","Principal": {"AWS": ["arn:aws:iam::primary_account_id:role/InvokerRoleName"]},"Action": "sts:AssumeRole"}]}'
```

You can also define the trust policy for the role using a separate
JSON file. In the following example, `trust-policy.json`
is a file in the current directory.

### Defining trust policy using JSON file

You can define the trust policy for the role using a separate JSON
file and then run the `create-role` command. In the
following example, **`trust-policy.json`** is a file that
contains the trust policy in the current directory. This policy is
attached to a role by running **`create-role`** command. The output of
the `**create-role**`
command is shown in the **Sample
Output**. To add permissions to a role, use the
**attach-policy-to-role** command
and you can start by adding the
`AWSResilienceHubAsssessmentExecutionPolicy` managed
policy. For more information about this managed policy, see [AWSResilienceHubAsssessmentExecutionPolicy](security-iam-awsmanpol.md#security_iam_aws-assessment-policy "security-iam-awsmanpol.md#security_iam_aws-assessment-policy").

**Sample
`trust-policy.json`**

**Sample
`create-role`**

```
aws iam create-role --role-name AWSResilienceHubAssessmentRole --assume-role-policy-document file://trust-policy.json
```

**Sample Output**

**Sample
`attach-policy-to-role`**

`aws iam attach-role-policy --role-name
 AWSResilienceHubAssessmentRole --policy-arn
 arn:aws:iam::aws:policy/AWSResilienceHubAsssessmentExecutionPolicy`.
