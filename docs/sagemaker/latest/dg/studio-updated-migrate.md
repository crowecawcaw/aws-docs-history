# Migration from Amazon SageMaker Studio Classic

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

When you open Amazon SageMaker Studio, the web-based UI is based on the chosen default experience.
Amazon SageMaker AI currently supports two different default experiences: the Amazon SageMaker Studio
experience and the Amazon SageMaker Studio Classic experience. To access the latest Amazon SageMaker Studio features,
you must migrate existing domains from the Amazon SageMaker Studio Classic experience. When you migrate your
default experience from Studio Classic to Studio, you don't lose any features, and can
still access the Studio Classic IDE within Studio. For information about the added benefits
of the Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

###### Note

- For existing customers that created their accounts before November 30, 2023,
  Studio Classic may be the default experience. You can enable Studio as your
  default experience using the AWS Command Line Interface (AWS CLI) or the Amazon SageMaker AI console. For more
  information about Studio Classic, see [Amazon SageMaker Studio Classic](studio.md "studio.md").
- For customers that created their accounts after November 30, 2023, we
  recommend using Studio as the default experience because it contains
  various integrated development environments (IDEs), including the Studio Classic
  IDE, and other new features.

JupyterLab 3 reached its end of maintenance date on May 15, 2024. After
December 31, 2024, you can only create new Studio Classic notebooks on JupyterLab 3
for a limited period. However after December 31, 2024, SageMaker AI will no longer
provide fixes for critical issues on Studio Classic notebooks on JupyterLab 3. We
recommend that you migrate your workloads to the new Studio experience,
which supports JupyterLab 4.

- If Studio is your default experience, the UI is similar to the images found
  in [Amazon SageMaker Studio UI overview](studio-updated-ui.md "studio-updated-ui.md").
- If Studio Classic is your default experience, the UI is similar to the images found in
  [Amazon SageMaker Studio Classic UI Overview](studio-ui.md "studio-ui.md").
  To migrate, you must update an existing domain. Migrating an existing domain from
  Studio Classic to Studio requires three distinct phases:

1. Migrate the UI from Studio Classic to Studio: One
   time, low lift task that requires creating a test domain to ensure Studio is
   compliant with your organization's network configurations before migrating the
   existing domain's UI from Studio Classic to Studio.
2. (Optional) Migrate custom images and lifecycle configuration
   scripts: Medium lift task for migrating your custom images and LCC
   scripts from Studio Classic to Studio.
3. (Optional) Migrate data from Studio Classic to
   Studio: Heavy lift task that requires using
   AWS DataSync to migrate data from the Studio Classic Amazon Elastic File System volume to
   either a target Amazon EFS or Amazon Elastic Block Store volume.
   1. (Optional) Migrate data flows from Data Wrangler in Studio Classic:
      One time, low lift task for migrating your data flows from Data Wrangler in Studio Classic to Studio,
      which you can then access in the latest version of Studio through SageMaker Canvas. For more information,
      see [Migrate data flows from Data Wrangler](studio-updated-migrate-data.md#studio-updated-migrate-flows "studio-updated-migrate-data.md#studio-updated-migrate-flows").
      The following topics show how to complete these phases to migrate an existing domain from
      Studio Classic to Studio.

## Automatic migration

Between July 2024 and August 2024, we are automatically upgrading the default landing
experience for users to the new Studio experience. This only changes the default
landing UI to the updated Studio UI. The Studio Classic application is still accessible
from the new Studio UI.

To ensure that migration works successfully for your users, see [Migrate the UI from Studio Classic to
Studio](studio-updated-migrate-ui.md "studio-updated-migrate-ui.md"). In
particular, ensure the following:

- the domain's execution role has the right permissions
- the default landing experience is set to Studio
- the domain's Amazon VPC, if applicable, is configured to Studio using the
  Studio VPC endpoint

However, if you need to continue having Studio Classic as your default UI for a limited
time, set the landing experience to Studio Classic explicitly. For more information, see [Set Studio Classic as the default
experience](studio-updated-migrate-ui.md#studio-updated-migrate-revert "studio-updated-migrate-ui.md#studio-updated-migrate-revert").

###### Topics

- [Complete prerequisites to migrate the
  Studio experience](studio-updated-migrate-prereq.md "studio-updated-migrate-prereq.md")
- [Migrate the UI from Studio Classic to
  Studio](studio-updated-migrate-ui.md "studio-updated-migrate-ui.md")
- [(Optional) Migrate custom images and lifecycle
  configurations](studio-updated-migrate-lcc.md "studio-updated-migrate-lcc.md")
- [(Optional) Migrate data from
  Studio Classic to Studio](studio-updated-migrate-data.md "studio-updated-migrate-data.md")
