# SEC03-BP01 Define access requirements

Each component or resource of your workload needs to be accessed by administrators, end
users, or other components. Have a clear definition of who or what should have access to each
component, choose the appropriate identity type and method of authentication and
authorization.

**Common anti-patterns:**

- Hard-coding or storing secrets in your application.
- Granting custom permissions for each user.
- Using long-lived credentials.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Each component or resource of your workload needs to be accessed by administrators, end
users, or other components. Have a clear definition of who or what should have access to each
component, choose the appropriate identity type and method of authentication and
authorization.

Regular access to AWS accounts within the organization should be provided using [federated access](https://aws.amazon.com/identity/federation/ "https://aws.amazon.com/identity/federation/") or a centralized
identity provider. You should also centralize your identity management and ensure that there
is an established practice to integrate AWS access to your employee access lifecycle. For
example, when an employee changes to a job role with a different access level, their group
membership should also change to reflect their new access requirements.

When defining access requirements for non-human identities, determine which applications
and components need access and how permissions are granted. Using IAM roles built with the
least privilege access model is a recommended approach. [AWS Managed
policies](../../../singlesignon/latest/userguide/security-iam-awsmanpol.md "../../../singlesignon/latest/userguide/security-iam-awsmanpol.md") provide predefined IAM policies that cover most common use cases.

AWS services, such as [AWS Secrets Manager](https://aws.amazon.com/blogs/security/identify-arrange-manage-secrets-easily-using-enhanced-search-in-aws-secrets-manager/ "https://aws.amazon.com/blogs/security/identify-arrange-manage-secrets-easily-using-enhanced-search-in-aws-secrets-manager/") and [AWS Systems Manager
Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md"), can help decouple secrets from the application or workload securely. In Secrets Manager, you can establish
automatic rotation for your credentials. You can use Systems Manager to reference parameters in your
scripts, commands, SSM documents, configuration, and automation workflows by using the unique
name that you specified when you created the parameter.

You can use
[AWS IAM Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md") to obtain
[temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") for workloads that run outside
of AWS. Your workloads can use the same
[IAM
policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") and
[IAM
roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that you use with AWS applications to access AWS
resources.

Where possible, prefer short-term temporary credentials over
long-term static credentials. For scenarios in which you need
users with programmatic access and long-term credentials,
use [access
key last used information](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey") to rotate and remove access keys.

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                                  | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM                                                          | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Login for AWS local development](../../../cli/latest/userguide/cli-configure-sign-in.md "../../../cli/latest/userguide/cli-configure-sign-in.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs, see [Login for AWS local development](../../../sdkref/latest/guide/access-login.md "../../../sdkref/latest/guide/access-login.md") in the<br>_AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                                                             |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

## Resources

**Related documents:**

- [Attribute-based
  access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md")
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/")
- [IAM
  Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md")
- [AWS Managed policies for IAM Identity Center](../../../singlesignon/latest/userguide/security-iam-awsmanpol.md "../../../singlesignon/latest/userguide/security-iam-awsmanpol.md")
- [AWS IAM policy conditions](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md")
- [IAM use cases](../../../IAM/latest/UserGuide/IAM_UseCases.md "../../../IAM/latest/UserGuide/IAM_UseCases.md")
- [Remove
  unnecessary credentials](../../../IAM/latest/UserGuide/best-practices.md#remove-credentials "../../../IAM/latest/UserGuide/best-practices.md#remove-credentials")
- [Working
  with Policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md")
- [How to control access to AWS resources based on AWS account, OU, or organization](https://aws.amazon.com/blogs/security/how-to-control-access-to-aws-resources-based-on-aws-account-ou-or-organization/ "https://aws.amazon.com/blogs/security/how-to-control-access-to-aws-resources-based-on-aws-account-ou-or-organization/")
- [Identify, arrange, and manage secrets easily using enhanced search in AWS Secrets Manager](https://aws.amazon.com/blogs/security/identify-arrange-manage-secrets-easily-using-enhanced-search-in-aws-secrets-manager/ "https://aws.amazon.com/blogs/security/identify-arrange-manage-secrets-easily-using-enhanced-search-in-aws-secrets-manager/")

**Related videos:**

- [Become an IAM
  Policy Master in 60 Minutes or Less](https://youtu.be/YQsK4MtsELU "https://youtu.be/YQsK4MtsELU")
- [Separation of
  Duties, Least Privilege, Delegation, and CI/CD](https://youtu.be/3H0i7VyTu70 "https://youtu.be/3H0i7VyTu70")
- [Streamlining
  identity and access management for innovation](https://www.youtube.com/watch?v=3qK0b1UkaE8 "https://www.youtube.com/watch?v=3qK0b1UkaE8")
