# Adding policies to your IAM role

To get started with Amazon SageMaker Feature Store you must have a role and add the required policy to your
role, `AmazonSageMakerFeatureStoreAccess`. The following is a walkthrough on how
to view the policies attached to a role and how to add a policy to your role. For
information on how to create a role, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md"). For information on how to get your execution role,
see [Get your execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role "sagemaker-roles.md#sagemaker-roles-get-execution-role").

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left of the IAM console, choose
   **Roles**.
3. In the search bar enter the role you are using for Amazon SageMaker Feature Store.

For examples on how to find your execution role ARN for a notebook within SageMaker AI,
see [Get your execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role "sagemaker-roles.md#sagemaker-roles-get-execution-role"). The role is at the end of
the execution role ARN. 4. After you enter the role in the search bar, choose the role.

Under **Permissions policies** you can view the policies attached
to the role. 5. After you choose the role, choose **Add permissions**, then
choose **Attach policies**. 6. In the search bar under **Other permissions policies** enter
`AmazonSageMakerFeatureStoreAccess` and press enter. If the policy
does not show, you may already have the policy attached, listed under your
**Current permissions policies**. 7. After you press enter, select the **check box** next to the
policy and then choose **Add permissions**. 8. After you have attached the policy to your role, the policy will appear under
**Permissions policies** for your IAM role.
