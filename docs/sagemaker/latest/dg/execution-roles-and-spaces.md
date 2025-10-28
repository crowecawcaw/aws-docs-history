# Understanding domain space permissions and

execution roles

For many SageMaker AI applications, when you start up a SageMaker AI application within a domain, a
space is created for the application. When a user profile creates a space, that space assumes an
AWS Identity and Access Management (IAM) role that defines the permissions granted to that space. The following page
gives information about space types and the execution roles that define permissions for the
space.

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an IAM identity that
you can create in your account that has specific permissions. An IAM role is similar to
an IAM user in that it is an AWS identity with permissions policies that determine
what the identity can and cannot do in AWS. However, instead of being uniquely associated
with one person, a role is intended to be assumable by anyone who needs it. Also, a role
does not have standard long-term credentials such as a password or access keys associated
with it. Instead, when you assume a role, it provides you with temporary security credentials
for your role session.

###### Note

When you start up Amazon SageMaker Canvas or RStudio, it does not create a space that assumes an IAM
role. Instead, you change the role associated with the user profile to manage their
permissions for the application. For information on obtaining a SageMaker AI user profile’s role, see
[Get user execution
role](sagemaker-roles.md#sagemaker-roles-get-execution-role-user "sagemaker-roles.md#sagemaker-roles-get-execution-role-user").

For SageMaker Canvas, see [Amazon SageMaker Canvas setup and permissions management (for IT
administrators)](canvas-setting-up.md "canvas-setting-up.md").

For RStudio, see [Create Amazon SageMaker AI domain with RStudio App](rstudio-create-cli.md#rstudio-create-cli-domain "rstudio-create-cli.md#rstudio-create-cli-domain").

Users can access their SageMaker AI applications within a shared or private space.

**Shared spaces**

- There can only be one space associated with an application. A shared space can be
  accessed by all of the user profiles within the domain. This grants all user profiles in
  the domain access to the same underlying file storage system for the application.
- The shared space will be granted the permissions defined by the **space default execution role**. If you wish to modify the shared space's
  execution role, you must modify the space default execution role.

For information on obtaining the space default execution role, see [Get space execution
role](sagemaker-roles.md#sagemaker-roles-get-execution-role-space "sagemaker-roles.md#sagemaker-roles-get-execution-role-space").

For information on modifying your execution role, see [Modify permissions to
execution role](sagemaker-roles.md#sagemaker-roles-modify-to-execution-role "sagemaker-roles.md#sagemaker-roles-modify-to-execution-role").

- For information about shared spaces, see [Collaboration with shared spaces](domain-space.md "domain-space.md").
- To create a shared space, see [Create a shared space](domain-space-create.md#domain-space-create-app "domain-space-create.md#domain-space-create-app").
  **Private spaces**

- There can only be one space associated with an application. A private space can only be
  accessed by the user profile who created it. This space cannot be shared with other
  users.
- The private space will assume the **user profile execution
  role** of the user profile that created it. If you wish to modify the private
  space's execution role, you must modify the user profile's execution role.

For information on obtaining the user profile's execution role, see [Get user execution
role](sagemaker-roles.md#sagemaker-roles-get-execution-role-user "sagemaker-roles.md#sagemaker-roles-get-execution-role-user").

For information on modifying your execution role, see [Modify permissions to
execution role](sagemaker-roles.md#sagemaker-roles-modify-to-execution-role "sagemaker-roles.md#sagemaker-roles-modify-to-execution-role").

- All applications that support spaces also support private spaces.
- A private space for Studio Classic is already created for each user profile by
  default.

###### Topics

- [SageMaker AI execution roles](#sagemaker-execution-roles "#sagemaker-execution-roles")
- [Example of flexible permissions with
  execution roles](#sagemaker-execution-roles-example "#sagemaker-execution-roles-example")

## SageMaker AI execution roles

A SageMaker AI execution role is an [AWS Identity and Access Management (IAM)
role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that is assigned to an IAM identity that is performing executions in SageMaker AI. An
[IAM identity](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md")
provides access to an AWS account and represents a human user or programmatic workload that
can be authenticated and then authorized to perform actions in AWS, that grants permissions
to SageMaker AI to access other AWS resources on your behalf. This role allows SageMaker AI to perform
actions like launching compute instances, accessing data and model artifacts stored in Amazon S3,
or writing logs to CloudWatch. SageMaker AI assumes the execution role at runtime and is temporarily granted
the permissions defined in the role's policy. The role should contain the necessary
permissions that define the actions the identity can perform and resources the identity has
access to. You can assign roles to various identities to provide a flexible and granular
approach to managing permissions and access within your domain. For more information on
domains, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md"). For
example, you can assign IAM roles to the:

- **Domain execution role** to grant broad permissions to
  all of the user profiles within the domain.
- **Space execution role** to grant broad permissions for a
  shared spaces within the domain. All user profiles in the domain can access shared
  spaces and will use the space's execution role while within the shared space.
- **User profile execution role** to grant fine-grained
  permissions for specific user profiles. A private space created by a user profile will
  assume that user profile's execution role.

This enables you to grant the necessary permissions to the domain while still
maintaining the principle of least-privilege permissions for user profiles, to adhere to the
[security best
practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _AWS IAM Identity Center User
Guide_.

Any changes or modifications to the execution roles may take a few minutes to propagate.
For more information, see [Change your execution
role](sagemaker-roles.md#sagemaker-roles-change-execution-role "sagemaker-roles.md#sagemaker-roles-change-execution-role") or [Modify permissions to
execution role](sagemaker-roles.md#sagemaker-roles-modify-to-execution-role "sagemaker-roles.md#sagemaker-roles-modify-to-execution-role"), respectively.

## Example of flexible permissions with

execution roles

With [IAM
roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") you can manage and grant permissions on broad and granular levels. The
following example includes granting permissions on a space-level and a user-level.

Suppose you are an administrator setting up a domain for a team of data scientists.
You can allow the user profiles within the domain to have full access to Amazon Simple Storage Service (Amazon S3)
buckets, run SageMaker training jobs, and deploy models using an application in a _shared space_. In this example, you can create an IAM role called
"DataScienceTeamRole" with broad permissions. Then you can assign "DataScienceTeamRole" as the
_space default execution role_, granting broad permissions
for your team. When a user profile creates a _shared space_,
that space will assume the _space default execution role_.
For information on assigning an execution role to an existing domain, see [Get space execution
role](sagemaker-roles.md#sagemaker-roles-get-execution-role-space "sagemaker-roles.md#sagemaker-roles-get-execution-role-space").

Instead of allowing any individual user profile working in their own _private space_ to have full access to Amazon S3 buckets, you can restrict
a user profile’s permissions and not allow them to alter the Amazon S3 buckets. In this example,
you can give them read access to Amazon S3 buckets to retrieve data, run SageMaker training jobs, and
deploy models in their _private space_. You can create a
user-level execution role called "DataScientistRole" with the relatively more limited
permissions. Then you can assign "DataScientistRole" to the _user
profile execution role_, granting the necessary permissions to perform their
specific data science tasks within the defined scope. When a user profile creates a _private space_, that space will assume the _user execution role_. For information on assigning an execution role to an
existing user profile, see [Get user execution
role](sagemaker-roles.md#sagemaker-roles-get-execution-role-user "sagemaker-roles.md#sagemaker-roles-get-execution-role-user").

For information on SageMaker AI execution roles and adding additional permissions to them, see
[How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md").
