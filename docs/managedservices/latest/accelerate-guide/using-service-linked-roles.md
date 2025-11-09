# Using service-linked roles for AMS Accelerate

AMS Accelerate uses AWS Identity and Access Management (IAM)
[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role").
A service-linked role (SLR) is a unique type of IAM role that is linked directly to AMS Accelerate. Service-linked roles are predefined by AMS Accelerate and
include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AMS Accelerate easier because you don’t have to
manually add the necessary permissions. AMS Accelerate defines the permissions of its
service-linked roles, and unless defined otherwise, only AMS Accelerate can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see
[AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and
look for the services that have **Yes**in the **Service-linked roles** column. Choose a
**Yes** with a link to view the service-linked role documentation for that
service.

## Deployment toolkit service-linked role for AMS Accelerate

AMS Accelerate uses the service-linked role (SLR) named **AWSServiceRoleForAWSManagedServicesDeploymentToolkit** – this role deploys AMS Accelerate infrastructure into customer accounts.

###### Note

This policy has recently been updated; for details, see [Accelerate updates to service-linked roles](#slr-updates "#slr-updates").

### AMS Accelerate deployment toolkit SLR

The AWSServiceRoleForAWSManagedServicesDeploymentToolkit service-linked role trusts the following services to assume the role:

- `deploymenttoolkit.managedservices.amazonaws.com`

The policy named
[AWSManagedServicesDeploymentToolkitPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-DeploymentToolkitPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-DeploymentToolkitPolicy")
allows AMS Accelerate to perform actions on the following resources:

- `arn:aws*:s3:::ams-cdktoolkit*`
- `arn:aws*:cloudformation:*:*:stack/ams-cdk-toolkit*`
- `arn:aws:ecr:*:*:repository/ams-cdktoolkit*`

This SLR grants Amazon S3 permissions to create and manage the deployment bucket used by AMS to upload resources, like CloudFormation templates or Lambda
asset bundles, into the account for component deployments. This SLR grants CloudFormation permissions to deploy the CloudFormation stack that defines the deployment buckets.
For details or to download the policy, see

[AWSManagedServices_DeploymentToolkitPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-DeploymentToolkitPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-DeploymentToolkitPolicy").

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see
[Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

### Creating an deployment toolkit SLR for AMS Accelerate

You don't need to manually create a service-linked role. When you Onboard to AMS in the AWS Management Console, the AWS CLI, or the AWS API, AMS Accelerate
creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you were using the AMS Accelerate service before June 09, 2022, when it began supporting service-linked roles,
then AMS Accelerate created the AWSServiceRoleForAWSManagedServicesDeploymentToolkit role in your account. To learn more, see
[A new role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account.
When you Onboard to AMS, AMS Accelerate creates the service-linked role for you again.

### Editing an deployment toolkit SLR for AMS Accelerate

AMS Accelerate does not allow you to edit the AWSServiceRoleForAWSManagedServicesDeploymentToolkit service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role")
in the _IAM User Guide_.

### Deleting an deployment toolkit SLR for AMS Accelerate

You don't need to manually delete the AWSServiceRoleForAWSManagedServicesDeploymentToolkit role. When you Offboard from AMS in the AWS Management Console, the AWS CLI, or the AWS API, AMS Accelerate
cleans up the resources and deletes the service-linked role for you.

You can also use the IAM console, the AWS CLI or the AWS API to manually delete the service-linked role. To do this, you must first manually clean
up the resources for your service-linked role and then you can manually delete it.

###### Note

If the AMS Accelerate service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

**To delete AMS Accelerate resources used by the AWSServiceRoleForAWSManagedServicesDeploymentToolkit service-linked role**

Delete `ams-cdk-toolkit` stack from all Regions your account was onboarded to in AMS (you might have to manually empty the S3 buckets first).

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAWSManagedServicesDeploymentToolkit
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Detective controls service-linked role for AMS Accelerate

AMS Accelerate uses the service-linked role (SLR) named **AWSServiceRoleForManagedServices_DetectiveControlsConfig** – AWS Managed Services uses this service-linked role to deploy config-recorder, config rules and S3 bucket detective controls..

Attached to the **AWSServiceRoleForManagedServices_DetectiveControlsConfig** service-linked role is the following managed policy:
[AWSManagedServices_DetectiveControlsConfig_ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-DetectiveControlsConfig "security-iam-awsmanpol.md#security-iam-awsmanpol-DetectiveControlsConfig").
For updates to this policy, see [Accelerate updates to AWS managed policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

### Permissions for detective controls SLR for AMS Accelerate

The AWSServiceRoleForManagedServices_DetectiveControlsConfig service-linked role trusts the following services to assume the role:

- `detectivecontrols.managedservices.amazonaws.com`

Attached to this role is the
`AWSManagedServices_DetectiveControlsConfig_ServiceRolePolicy` AWS managed policy
(see [AWS managed policy: AWSManagedServices_DetectiveControlsConfig_ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-DetectiveControlsConfig "security-iam-awsmanpol.md#security-iam-awsmanpol-DetectiveControlsConfig")
The service uses the role to create configure AMS Detective Controls in your account, which requires deployment of resources like s3 buckets, config rules and an aggregator.
You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role.
For more information, see
[Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions")
in the _AWS Identity and Access Management_ User Guide.

### Creating a detective controls SLR for AMS Accelerate

You don't need to manually create a service-linked role. When you Onboard to AMS in the AWS Management Console, the AWS CLI, or the AWS API, AMS Accelerate
creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you were using the
AMS Accelerate service before June 09, 2022, when it began supporting service-linked roles then AMS Accelerate created the AWSServiceRoleForManagedServices_DetectiveControlsConfig role in your account.
To learn more, see
[A new role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account.
When you Onboard to AMS, AMS Accelerate creates the service-linked role for you again.

### Editing a detective controls SLR for AMS Accelerate

AMS Accelerate does not allow you to edit the AWSServiceRoleForManagedServices_DetectiveControlsConfig service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

### Deleting a detective controls SLR for AMS Accelerate

You don't need to manually delete the AWSServiceRoleForManagedServices_DetectiveControlsConfig role. When you Offboard from AMS in the AWS Management Console, the AWS CLI, or the AWS API, AMS Accelerate
cleans up the resources and deletes the service-linked role for you.

You can also use the IAM console, the AWS CLI or the AWS API to manually delete the service-linked role. To do this, you must first manually clean
up the resources for your service-linked role and then you can manually delete it.

###### Note

If the AMS Accelerate service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

**To delete AMS Accelerate resources used by the AWSServiceRoleForManagedServices_DetectiveControlsConfig service-linked role**

Delete `ams-detective-controls-config-recorder`, `ams-detective-controls-config-rules-cdk` and `ams-detective-controls-infrastructure-cdk`
stacks from all Regions your account was onboarded to in AMS (you might have to manually empty the S3 buckets first).

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForManagedServices_DetectiveControlsConfig
service-linked role. For more information, see
[Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Amazon EventBridge rule service-linked role for AMS Accelerate

AMS Accelerate uses the service-linked role (SLR) named **AWSServiceRoleForManagedServices_Events**. This role trusts one of the AWS Managed Services service principals (events.managedservices.amazonaws.com) to assume the role for you.
The service uses the role to create Amazon EventBridge managed rule. This rule is the infrastructure required in your AWS account to deliver alarm state change
information from your account to AWS Managed Services.

### Permissions for EventBridge SLR for AMS Accelerate

The AWSServiceRoleForManagedServices_Events service-linked role trusts the following services to assume the role:

- `events.managedservices.amazonaws.com`

Attached to this role is the `AWSManagedServices_EventsServiceRolePolicy` AWS managed policy
(see [AWS managed policy: AWSManagedServices_EventsServiceRolePolicy](security-iam-awsmanpol.md#EventsServiceRolePolicy "security-iam-awsmanpol.md#EventsServiceRolePolicy")).
The service uses the role to deliver alarm state change information from your account to AMS.
You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role.
For more information, see
[Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions")
in the _AWS Identity and Access Management User Guide_.

You can download the JSON AWSManagedServices_EventsServiceRolePolicy in this ZIP: [EventsServiceRolePolicy.zip](samples/EventsServiceRolePolicy.md "samples/EventsServiceRolePolicy.md").

### Creating an EventBridge SLR for AMS Accelerate

You don't need to manually create a service-linked role. When you Onboard to AMS in the AWS Management Console, the AWS CLI, or the AWS API, AMS Accelerate
creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you were using the
AMS Accelerate service before February 7, 2023, when it began supporting service-linked roles then AMS Accelerate created the AWSServiceRoleForManagedServices_Events role in your account.
To learn more, see
[A new role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account.
When you Onboard to AMS, AMS Accelerate creates the service-linked role for you again.

### Editing an EventBridge SLR for AMS Accelerate

AMS Accelerate does not allow you to edit the AWSServiceRoleForManagedServices_Events service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role")
in the _IAM User Guide_.

### Deleting an EventBridge SLR for AMS Accelerate

You don't need to manually delete the AWSServiceRoleForManagedServices_Events role. When you Offboard from AMS in the AWS Management Console, the AWS CLI, or the AWS API, AMS Accelerate
cleans up the resources and deletes the service-linked role for you.

You can also use the IAM console, the AWS CLI or the AWS API to manually delete the service-linked role. To do this, you must first manually clean
up the resources for your service-linked role and then you can manually delete it.

###### Note

If the AMS Accelerate service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

**To delete AMS Accelerate resources used by the AWSServiceRoleForManagedServices_Events service-linked role**

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForManagedServices_Events service-linked role. For more information, see
[Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Contacts service-linked role for AMS Accelerate

AMS Accelerate uses the service-linked role (SLR) named **AWSServiceRoleForManagedServices_Contacts** – This role facilitates automated notifications when incidents occur by allowing the service to read the existing tags of the affected
resource and retrieve the configured email of the appropriate point of contact.

This is the only service that uses this service-linked role.

Attached to the **AWSServiceRoleForManagedServices_Contacts** service-linked role is the following managed policy:
[AWSManagedServices_ContactsServiceRolePolicy](security-iam-awsmanpol.md#ContactsServiceManagedPolicy "security-iam-awsmanpol.md#ContactsServiceManagedPolicy").
For updates to this policy, see [Accelerate updates to AWS managed policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

### Permissions for Contacts SLR for AMS Accelerate

The AWSServiceRoleForManagedServices_Contacts service-linked role trusts the following services to assume the role:

- `contacts-service.managedservices.amazonaws.com`

Attached to this role is the `AWSManagedServices_ContactsServiceRolePolicy` AWS managed policy
(see [AWS managed policy: AWSManagedServices_ContactsServiceRolePolicy](security-iam-awsmanpol.md#ContactsServiceManagedPolicy "security-iam-awsmanpol.md#ContactsServiceManagedPolicy")).
The service uses the role to read the tags on any AWS resource and find the email contained in the tag, of the appropriate point of contact
for when incidents occur. This role facilitates automated notifications when incidents occur by allowing AMS to read that tag on an affected
resource and retrieve the email. For more information, see
[Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions")
in the _AWS Identity and Access Management_ User Guide.

###### Important

Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. AMS uses tags to provide you
with administration services. Tags are not intended to be used for private or sensitive data.

The role permissions policy named AWSManagedServices_ContactsServiceRolePolicy allows AMS Accelerate to complete the following actions on the specified resources:

- Action: Allows the Contacts Service to read the tags specifically set up to contain the email for AMS to send incident notifications on any AWS resource.

You can download the JSON AWSManagedServices_ContactsServiceRolePolicy in this ZIP: [ContactsServicePolicy.zip](samples/ContactsServicePolicy.md "samples/ContactsServicePolicy.md").

### Creating a Contacts SLR for AMS Accelerate

You don't need to manually create a service-linked role. When you Onboard to AMS in the AWS Management Console, the AWS CLI, or the AWS API, AMS Accelerate
creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you were using the AMS Accelerate service before February 16, 2023, when it began supporting
service-linked roles then AMS Accelerate created the AWSServiceRoleForManagedServices_Contacts role in your account. To learn more, see
[A new role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account.
When you Onboard to AMS, AMS Accelerate creates the service-linked role for you again.

### Editing a Contacts SLR for AMS Accelerate

AMS Accelerate does not allow you to edit the AWSServiceRoleForManagedServices_Contacts service-linked role. After you create a service-linked role, you cannot change
the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role")
in the _IAM User Guide_.

### Deleting a Contacts SLR for AMS Accelerate

You don't need to manually delete the AWSServiceRoleForManagedServices_Contacts role. When you Offboard from AMS in the AWS Management Console, the AWS CLI, or the AWS API, AMS Accelerate
cleans up the resources and deletes the service-linked role for you.

You can also use the IAM console, the AWS CLI or the AWS API to manually delete the service-linked role. To do this, you must first manually clean
up the resources for your service-linked role and then you can manually delete it.

###### Note

If the AMS Accelerate service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a
few minutes and try the operation again.

**To delete AMS Accelerate resources used by the AWSServiceRoleForManagedServices_Contacts service-linked role**

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForManagedServices_Contacts service-linked role. For more information, see
[Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported regions for AMS Accelerate service-linked roles

AMS Accelerate supports using service-linked roles in all of the regions where the service is available. For more information, see [AWS regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

## Accelerate updates to service-linked roles

View details about updates to Accelerate service-linked roles since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Accelerate [Document history for AMS Accelerate User Guide](doc-history.md "doc-history.md") page.

| Change                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Date              |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Updated policy –<br>[Deployment Toolkit](#slr-deploy-acc "#slr-deploy-acc")                               | • These new permissions were added for resource `arn:aws:ecr:*:*:repository/ams-cdktoolkit*`:<br>`<br>ecr:BatchGetRepositoryScanningConfiguration<br>ecr:PutImageScanningConfiguration<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | April 4, 2024     |
| Updated policy –<br>[Deployment Toolkit](#slr-deploy-acc "#slr-deploy-acc")                               | • These new permissions were added for resource `arn:aws:cloudformation:*:*:stack/ams-cdk-toolkit*`:<br>`<br>cloudformation:DeleteChangeSet<br>cloudformation:DescribeStackEvents<br>cloudformation:GetTemplate<br>cloudformation:TagResource<br>cloudformation:UntagResource<br>`<br>• These new permissions were added for resource `arn:aws:ecr:*:*:repository/ams-cdktoolkit*`:<br>`<br>ecr:CreateRepository<br>ecr:DeleteLifecyclePolicy<br>ecr:DeleteRepository<br>ecr:DeleteRepositoryPolicy<br>ecr:DescribeRepositories<br>ecr:GetLifecyclePolicy<br>ecr:ListTagsForResource<br>ecr:PutImageTagMutability<br>ecr:PutLifecyclePolicy<br>ecr:SetRepositoryPolicy<br>ecr:TagResource<br>ecr:UntagResource<br>`<br>• Also, some existing actions with wildcard were scoped down to individual actions:<br>`<br>• s3:DeleteObject*<br>+ s3:DeleteObject<br>+ s3:DeleteObjectTagging<br>+ s3:DeleteObjectVersion<br>+ s3:DeleteObjectVersionTagging<br>• s3:GetObject*<br>+ s3:GetObject<br>+ s3:GetObjectAcl<br>+ s3:GetObjectAttributes<br>+ s3:GetObjectLegalHold<br>+ s3:GetObjectRetention<br>+ s3:GetObjectTagging<br>+ s3:GetObjectVersion<br>+ s3:GetObjectVersionAcl<br>+ s3:GetObjectVersionAttributes<br>+ s3:GetObjectVersionForReplication<br>+ s3:GetObjectVersionTagging<br>+ s3:GetObjectVersionTorrent<br>• cloudformation:UpdateTermination*<br>+ cloudformation:UpdateTerminationProtection<br>` | May 09, 2023      |
| Updated policy –<br>[Detective Controls](#slr-deploy-detect-controls "#slr-deploy-detect-controls")       | • The CloudFormation actions have been scoped down further after confirmation with security and access team<br>• The Lambda actions have been removed from the policy as they don’t impact onboarding/off boarding                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | April 10, 2023    |
| Updated policy –<br>[Detective Controls](#slr-deploy-detect-controls "#slr-deploy-detect-controls")       | Updated the policy and added the permissions boundary policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | March 21, 2023    |
| New service-linked role – [Contacts SLR](#slr-contacts-service "#slr-contacts-service")                   | Accelerate added a new service-linked role for the Contacts service.<br>This role facilitates automated notifications when incidents occur by allowing the service to read the existing tags of the affected<br>resource and retrieve the configured email of the appropriate point of contact.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | February 16, 2023 |
| New service-linked role – [EventBridge](#slr-evb-rule "#slr-evb-rule")                                    | Accelerate added a new service-linked role for an Amazon EventBridge rule.<br>This role trusts one of the AWS Managed Services service principals (events.managedservices.amazonaws.com) to assume the role for you.<br>The service uses the role to create Amazon EventBridge managed rule. This rule is the infrastructure required in your AWS account to deliver alarm state change<br>information from your account to AWS Managed Services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | February 7, 2023  |
| Updated service-linked role – [Deployment Toolkit](#slr-deploy-acc "#slr-deploy-acc")                     | Accelerate updated AWSServiceRoleForAWSManagedServicesDeploymentToolkit with new S3 permissions.<br>These new permissions were added:<br>`<br>"s3:GetLifecycleConfiguration",<br>"s3:GetBucketLogging",<br>"s3:ListBucket",<br>"s3:GetBucketVersioning",<br>"s3:PutLifecycleConfiguration",<br>"s3:GetBucketLocation",<br>"s3:GetObject*"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | January 30, 2023  |
| Accelerate started tracking changes                                                                       | Accelerate started tracking changes for its service-linked roles.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | November 30, 2022 |
| New service-linked role – [Detective Controls](#slr-deploy-detect-controls "#slr-deploy-detect-controls") | Accelerate added a new service-linked role to deploy Accelerate detective controls.<br>AWS Managed Services uses this service-linked role to deploy config-recorder, config rules and S3 bucket detective controls.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | October 13, 2022  |
| New service-linked role – [Deployment Toolkit](#slr-deploy-acc "#slr-deploy-acc")                         | Accelerate added a new service-linked role to deploy Accelerate infrastructure.<br>this role deploys AMS Accelerate infrastructure into customer accounts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | June 09, 2022     |
