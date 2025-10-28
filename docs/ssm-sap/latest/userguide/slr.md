# Using service linked roles for AWS Systems Manager for SAP

AWS Systems Manager for SAP uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked directly to Systems Manager for SAP. Service-linked roles are predefined by Systems Manager for SAP and include all of the permissions that the service requires to call other AWS services, including Amazon EC2, Systems Manager, IAM, Amazon CloudWatch, Amazon EventBridge, AWS Resource Groups, and AWS Service Catalog.

A service-linked role makes setting up Systems Manager for SAP easier because you don’t have to manually add the necessary permissions. Systems Manager for SAP defines the permissions of its service-linked roles, and unless you make changes to the configuration, only Systems Manager for SAP can assume its roles. Configurable permissions include the trust policy and the permissions policy. You can’t attach the permissions policy to any other IAM entity.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column. Follow the **Yes** link to view the service-linked role documentation for that service, if applicable.

## Service-linked role permissions for Systems Manager for SAP

Systems Manager for SAP uses the service-linked role named [AWSSSMForSAPServiceLinkedRolePolicy](../../../aws-managed-policy/latest/reference/AWSSSMForSAPServiceLinkedRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSSSMForSAPServiceLinkedRolePolicy.md") and associates it with the **AWSSSMForSAPServiceLinkedRolePolicy** IAM policy – Provides AWS Systems Manager for SAP the permissions required to manage and integrate SAP applications on AWS.

The policy enables Systems Manager for SAP to perform actions specified in the policy. These actions are from the following AWS services – Amazon EC2, Systems Manager, IAM, Amazon CloudWatch, Amazon EventBridge, AWS Resource Groups, and AWS Service Catalog.

**Permissions details**

This policy includes the following permissions.

- `cloudwatch` – Allows publication of Systems Manager for SAP metric data to Amazon CloudWatch.
- `ec2` – Allows
  - Description, start and stop of instances
  - Creation, deletion, and description of tags on EC2 instances that are with `SSMForSAPManaged:True`.
  - Creation and deletion of tags on EBS volumes attached to the EC2 instances tagged with `SSMForSAPManaged:True`.
  - Description of VPCs

- `eventbridge` – Allows Amazon EventBridge to create, update, and delete rules, and add or remove targets to the rules.
- `iam` – Allows creation of roles and instance profiles.
- `resource-groups` – Allows AWS Resource Groups to create and delete groups.
- `servicecatalog` – Allows AWS Service Catalog to create, update, and delete applications, and attribute groups. The permission also enables association/disassociation of attribute groups to applications.
- `ssm` – Allows SSM to describe documents, run commands, and return command details.
- `ce` - Allows AWS Cost Explorer to list and update cost allocation tags, start cost allocation backfill, and list cost allocation backfill history.

The [AWSSSMForSAPServiceLinkedRolePolicy](../../../aws-managed-policy/latest/reference/AWSSSMForSAPServiceLinkedRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSSSMForSAPServiceLinkedRolePolicy.md") service-linked role trusts the following services to assume the role:

- `ssm-sap.amazonaws.com`

To view the update history of this policy, see [Systems Manager for SAP updates to AWS managed policies](iam-policies.md#security-iam-awsmanpol-updates "iam-policies.md#security-iam-awsmanpol-updates").

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for Systems Manager for SAP

AWS Systems Manager for SAP uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked directly to Systems Manager for SAP. Service-linked roles are predefined by Systems Manager for SAP and include all of the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Systems Manager for SAP easier because you don’t have to manually add the necessary permissions. Systems Manager for SAP defines the permissions of its service-linked roles, and unless you make changes to the configuration, only Systems Manager for SAP can assume its roles. Configurable permissions include the trust policy and the permissions policy. You can’t attach the permissions policy to any other IAM entity.

If you delete this service-linked role, Systems Manager for SAP automatically creates this service-linked role for you when you resume using Systems Manager for SAP.

## Editing a service-linked role for Systems Manager for SAP

Systems Manager for SAP does not allow you to edit the **AWSServiceRoleForAWSSSMForSAP** service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using the Systems Manager for SAP console, CLI, or API.

## Deleting a service-linked role for Systems Manager for SAP

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the **AWSServiceRoleForAWSSSMForSAP** service-linked role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

When deleting Systems Manager for SAP resources used by the **AWSServiceRoleForAWSSSMForSAP** SLR, you cannot have any running assessments (tasks for generating recommendations). No background assessments can be running, either. If assessments are running, the SLR deletion fails in the IAM console. If the SLR deletion fails, you can retry the deletion after all background tasks have completed. You don’t need to clean up any created resources before you delete the SLR.

## Supported Regions for Systems Manager for SAP service-linked roles

Systems Manager for SAP supports using service-linked roles in all of the regions where the service is available. For more information, see [Service endpoints for Systems Manager for SAP](../../../general/latest/gr/ssm-sap.md#regionssm-sap "../../../general/latest/gr/ssm-sap.md#regionssm-sap").
