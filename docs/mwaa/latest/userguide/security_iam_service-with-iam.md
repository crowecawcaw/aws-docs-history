# How Amazon MWAA works with IAM

Amazon MWAA uses IAM identity-based policies to grant permissions to Amazon MWAA actions and resources.
For recommended examples of custom IAM policies you can use to control access to your Amazon MWAA resources,
refer to [Accessing an Amazon MWAA environment](access-policies.md "access-policies.md").

To get a high-level access of how Amazon MWAA and other AWS services work with IAM, refer to [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Amazon MWAA identity-based

policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources, as well as the conditions under which actions are allowed or denied. Amazon MWAA
supports specific actions, resources, and condition keys.

The following steps present how you can create a new JSON policy using the IAM console.
This policy provides read-only access to your Amazon MWAA resources.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter the following JSON policy document:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "airflow:ListEnvironments",
        "airflow:GetEnvironment",
        "airflow:ListTagsForResource"
      ],
      "Resource": "*"
    }
  ]
}
```

6. Choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 8. Choose **Create policy** to save your new policy.

To learn about all of the elements that you use in a JSON policy, refer to [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy statements must include either an `Action` element or a
`NotAction` element. The `Action` element lists the actions
allowed by the policy. The `NotAction` element lists the actions that are
not allowed.

The actions defined for Amazon MWAA reflect tasks that you can perform using Amazon MWAA.
Policy actions in Detective have the following prefix:
`airflow:`.

You can also use wildcards (\*) to specify multiple actions. Instead of listing these actions
separately, you can grant access to all actions that end with the word, for example, `environment`.

To get a list of Amazon MWAA actions, refer to [Actions Defined by Amazon Managed Workflows for Apache Airflow](../../../IAM/latest/UserGuide/list_mwaa.md#mwaa-actions-as-permissions "../../../IAM/latest/UserGuide/list_mwaa.md#mwaa-actions-as-permissions") in the
_IAM User Guide_.
