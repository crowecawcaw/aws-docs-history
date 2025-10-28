# Role Manager FAQs

Refer to the following FAQ items for answers to commonly asked questions about
Amazon SageMaker Role Manager.

A: You can access Amazon SageMaker Role Manager through multiple location in the Amazon SageMaker AI console.
For information about accessing role manager and using it to create a role, see
[Using the role manager (console)](role-manager-tutorial.md "role-manager-tutorial.md").

A: Personas are preconfigured groups of permissions based on common machine
learning (ML) responsibitilies. For example, the data science persona suggests
permissions for general machine learning development and experimentation in a
SageMaker AI environment, while the MLOps persona suggests permissions for ML activities
related to operations.

A: ML activities are common AWS tasks related to machine learning with SageMaker AI
that require specific IAM permissions. Each persona suggests related ML
activities when creating a role with Amazon SageMaker Role Manager. ML activities include tasks such
as Amazon S3 full access or searching and visualizing experiments. For more
information, see [ML activity reference](role-manager-ml-activities.md "role-manager-ml-activities.md").

A: Yes. Roles created using the Amazon SageMaker Role Manager are IAM roles with customized
access policies. You can view created roles in the **Roles**
section of the [IAM console](https://console.aws.amazon.com/iamv2/ "https://console.aws.amazon.com/iamv2/").

A: You can view created roles in the **Roles** section of the
[IAM console](https://console.aws.amazon.com/iamv2/ "https://console.aws.amazon.com/iamv2/"). By default, the
prefix `"sagemaker-"` is added to every role name for easier search
in the IAM console. For example, if you named your role `test-123`
during role creation, your role shows up as `sagemaker-test-123` in
the IAM console.

A: Yes. You can modify the roles and policies created by Amazon SageMaker Role Manager through the
[IAM console](https://console.aws.amazon.com/iamv2/ "https://console.aws.amazon.com/iamv2/"). For more
information, see [Modifying a
role](../../../IAM/latest/UserGuide/id_roles_manage_modify.md "../../../IAM/latest/UserGuide/id_roles_manage_modify.md") in the _AWS Identity and Access Management User
Guide_.

A: Yes. You can attach any AWS or customer-managed IAM policies from your
account to the role that you create using Amazon SageMaker Role Manager.

A: The maximum limit for attaching managed policies to an IAM role or user
is 20. The maximum character size limit for managed policies is 6,144. For more
information, see [IAM object quotas](../../../IAM/latest/UserGuide/reference_iam-quotas.md#reference_iam-quotas-entities "../../../IAM/latest/UserGuide/reference_iam-quotas.md#reference_iam-quotas-entities") and [IAM and AWS Security Token Service
quotas name requirements, and character limits](../../../IAM/latest/UserGuide/reference_iam-quotas.md "../../../IAM/latest/UserGuide/reference_iam-quotas.md").

A: Any conditions that you provide in [Step 1. Enter role information](role-manager-tutorial.md#role-manager-tutorial-enter-role-information "role-manager-tutorial.md#role-manager-tutorial-enter-role-information") of the
Amazon SageMaker Role Manager, such as subnets, security groups, or KMS keys, are automatically
passed to any ML activities selected in [Step 2. Configure ML activities](role-manager-tutorial.md#role-manager-tutorial-configure-ml-activities "role-manager-tutorial.md#role-manager-tutorial-configure-ml-activities"). You can
also add additional conditions to ML activities if necessary. For example, you
might also add `InstanceTypes` or
`IntercontainerTrafficEncryption` conditions to the Manage
Training Jobs activity.

A:You can add tags to your role in [Step 3: Add additional policies and tags](role-manager-tutorial.md#role-manager-tutorial-add-policies-and-tags "role-manager-tutorial.md#role-manager-tutorial-add-policies-and-tags") of the
Amazon SageMaker Role Manager. To successfully manage AWS resources using tags, you must add the
same tag to both the role and any associated policies. For example, you can add
a tag to a role and to an Amazon S3 bucket. Then, because the role passes the tag to
the SageMaker AI session, only a user with that role can access that S3 bucket. You can
add tags to a policy through the [IAM
console](https://console.aws.amazon.com/iamv2/ "https://console.aws.amazon.com/iamv2/"). For more information, see [Tagging IAM roles](../../../IAM/latest/UserGuide/id_tags_roles.md "../../../IAM/latest/UserGuide/id_tags_roles.md") in
the _AWS Identity and Access Management User Guide_.

A: No. However, after creating a service role in the role manager, you can go
to the IAM console to edit the role and add a human access role in IAM
console.

A: A user federation role is directly assumed by a user to access AWS
resources such as access to the AWS Management Console. A SageMaker AI execution role is assumed by
the SageMaker AI service to perform a function on behalf of a user or an automation
tool. For example, when a user opens a Studio Classic instance, Studio Classic assumes
the execution role associated with the user profile in order to access AWS
resources on the behalf of the user. If the user profile does not specify an
execution role, then the execution role is specified at the Amazon SageMaker AI domain
level.

A: If you use a custom web application to access Studio Classic, then you have a
hybrid user federation role and SageMaker AI execution role. Be sure that this role has
least privilege permissions for both what the user can do and what Studio Classic
can do on the associated user’s behalf.

A: AWS IAM Identity Center Studio Classic Cloud Applications use a Studio Classic execution role to
grant permissions to federated users. This execution role can be specified at
the Studio Classic IAM Identity Center user profile level or the default domain level. User
identities and groups must be synchronized into IAM Identity Center and the
Studio Classic user profile must be created with IAM Identity Center user assignment using [CreateUserProfile](../APIReference/API_CreateUserProfile.md "../APIReference/API_CreateUserProfile.md"). For more information, see [Launch Studio Classic
with IAM Identity Center](role-manager-launch-notebook.md#role-manager-launch-notebook-iam-identity-center "role-manager-launch-notebook.md#role-manager-launch-notebook-iam-identity-center").
