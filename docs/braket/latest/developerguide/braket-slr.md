# Amazon Braket service-linked role

When you enable Amazon Braket, a _service-linked role_ is created in your account.

A service-linked role is a unique type of IAM role that, in this case, is linked directly to Amazon Braket.
The Amazon Braket service-linked role is predefined to include all the permissions that Braket requires when
calling other AWS services on your behalf.

A service-linked role makes setting up Amazon Braket easier because you don't have to add the necessary
permissions manually. Amazon Braket defines the permissions of its service-linked roles. Unless you change these
definitions, only Amazon Braket can assume its roles. The defined permissions include the
_trust policy_ and the _permissions policy_. The permissions policy cannot
be attached to any other IAM entity.

The service-linked role that Amazon Braket sets up is part of the AWS Identity and Access Management (IAM)
[service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts")
capability. For information about other AWS services that support service-linked roles, see
[AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

For more information on the AWS managed policy for service-linked roles, see
[AmazonBraketServiceRolePolicy](security-iam-aws-managed-policies.md#about-amazonbraketservicerolepolicy "security-iam-aws-managed-policies.md#about-amazonbraketservicerolepolicy").
