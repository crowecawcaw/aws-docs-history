# Customize accounts with Account Factory

Customization (AFC)

AWS Control Tower allows you to customize new and existing AWS accounts when you provision their
resources from the AWS Control Tower console. After you set up Account Factory customization,
AWS Control Tower automates this process for future provisioning, so you don't have to maintain any
pipelines. Customized accounts are available for use immediately after the resources are
provisioned.

**Provision new accounts with blueprints**

Your customized accounts are provisioned in the AWS Control Tower Account Factory, through AWS CloudFormation templates, or with Terraform.
You'll define a template that serves as customized account _blueprint_. Your blueprint describes the specific resources and
configurations you require when an account is provisioned. Pre-defined blueprints, built and
managed by AWS partners, also are available. For more information about partner-managed
blueprints, see the [AWS Service Catalog Getting
Started Library](../../../servicecatalog/latest/adminguide/getting-started-library.md "../../../servicecatalog/latest/adminguide/getting-started-library.md").

**Apply blueprints to existing accounts**

You can apply customized blueprints to existing accounts, also, by following the
**Update account** steps in the AWS Control Tower console. For details, see
[Update the account in the
console](updating-account-factory-accounts.md#update-account-in-console "updating-account-factory-accounts.md#update-account-in-console").

**Definition: Your hub account**

Your account blueprints are stored in an AWS account, which for our purposes is referred
to as a _hub account_. Blueprints are stored in the form of
an Service Catalog product. We call this product a blueprint, to distinguish it from any other Service Catalog
products. To learn more about how to create Service Catalog products, see [Creating
products](../../../servicecatalog/latest/adminguide/productmgmt-cloudresource.md "../../../servicecatalog/latest/adminguide/productmgmt-cloudresource.md") in the _AWS Service Catalog Administrator
Guide_.

###### Note

AWS Control Tower contains _proactive controls_, which monitor
AWS CloudFormation resources in AWS Control Tower. Optionally, you can activate these controls in your landing
zone. When you apply proactive controls, they check to make sure that the resources
you're about to deploy to your accounts are compliant with your organization's policies
and procedures. For more information about proactive controls, see [Proactive controls](proactive-controls.md "proactive-controls.md").

For more information about working with AFC, see [Automate account customization using Account Factory Customization in
AWS Control Tower](https://aws.amazon.com/blogs/mt/automate-account-customization-using-account-factory-customization-in-aws-control-tower/ "https://aws.amazon.com/blogs/mt/automate-account-customization-using-account-factory-customization-in-aws-control-tower/").

###### Prerequisites

Before you begin to create customized accounts with AWS Control Tower Account Factory, you must have
an AWS Control Tower landing zone environment deployed, and you must have an organizational unit
(OU) registered with AWS Control Tower, where your newly created accounts will be placed.

###### Preparation for customization

- _Designate a hub account:_ You may create a new account to serve as the hub account, or you may use an
  existing AWS account. We strongly recommend that you do not use the AWS Control Tower
  management account as your blueprint hub account.
- _Add the necessary role:_ If you plan to enroll AWS accounts into AWS Control Tower and customize them, you must
  first add the `AWSControlTowerExecution` role to those accounts, as you
  would for any other account you are enrolling into AWS Control Tower.
- _Configure partner blueprints (optional):_ If you plan to use partner blueprints that have marketplace subscription
  requirements, you must configure these from your AWS Control Tower management account before
  you deploy the partner blueprints as account factory customization
  blueprints.

###### Topics

- [Set up for customization](afc-setup-steps.md "afc-setup-steps.md")
- [Create a customized account from a
  blueprint](create-afc-customized-account.md "create-afc-customized-account.md")
- [Customize accounts with AFC as you enroll them](enroll-and-customize.md "enroll-and-customize.md")
- [Add a blueprint to an AWS Control Tower
  account](add-blueprint-to-account.md "add-blueprint-to-account.md")
- [Update a blueprint](update-a-blueprint.md "update-a-blueprint.md")
- [Remove a blueprint from an account](remove-a-blueprint.md "remove-a-blueprint.md")
- [Partner blueprints](partner-blueprints.md "partner-blueprints.md")
- [Considerations for Account Factory Customizations (AFC)](#af-limitations "#af-limitations")
- [In case of a blueprint error](#af-error "#af-error")
- [Customizing your policy document for AFC
  blueprints based on CloudFormation](#custom-policy-document "#custom-policy-document")
- [Additional permissions required for creating a Terraform-based Service Catalog product](#custom-policy-document-tf "#custom-policy-document-tf")
- [Transition to the AWS Service Catalog
  External product type](#service-catalog-external-product-type "#service-catalog-external-product-type")

###### Note

One blueprint may be deployed per AWS Control Tower account.

## Considerations for Account Factory Customizations (AFC)

- AFC supports customization using a single AWS Service Catalog blueprint product only.
- The AWS Service Catalog blueprint products must be created in the hub account, and in the
  same Region as the AWS Control Tower landing zone home Region.
- The `AWSControlTowerBlueprintAccess` IAM role must be created
  with the proper name, permissions, and trust policy.
- AWS Control Tower supports two deployment options for blueprints: deploy to the home
  Region only, or deploy to all Regions governed by AWS Control Tower. Selection of Regions
  is not available.
- When you update a blueprint in a member account, the blueprint hub account ID
  and the AWS Service Catalog blueprint product cannot be changed.
- AWS Control Tower doesn't support removing an existing blueprint and adding a new
  blueprint in a single blueprint update operation. You can remove a blueprint and
  then add a new blueprint in separate operations.
- AWS Control Tower changes behavior, based on whether you are creating or enrolling
  customized accounts, or non-customized accounts. If you are not creating or
  enrolling customized accounts with blueprints, AWS Control Tower creates an Account Factory
  provisioned product (through Service Catalog) in the AWS Control Tower management account. If you
  are specifying customization when creating or enrolling accounts with
  blueprints, AWS Control Tower does not create an Account Factory provisioned product in the
  AWS Control Tower management account.

## In case of a blueprint error

**Error while applying a blueprint**

If an error occurs during the process of applying a blueprint to an
account—either a new account or an existing account that you are enrolling into
AWS Control Tower—the recovery procedure is the same. The account will exist, but it is
not customized, and it is not enrolled into AWS Control Tower. To continue, follow the steps to
enroll the account into AWS Control Tower, and add the blueprint at time of enrollment.

**Error while creating the
`AWSControlTowerBlueprintAccess` role, and
workarounds**

When you create the `AWSControlTowerBlueprintAccess` role from an AWS Control Tower
account, you must be signed in as the principal using the
`AWSControlTowerExecution` role. If you are signed in as any other, the
`CreateRole` operation is prevented by an SCP, as shown in the artifact
that follows:

```
{
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::*:role/AWSControlTowerExecution",
                        "arn:aws:iam::*:role/stacksets-exec-*"
                    ]
                }
            },
            "Action": [
                "iam:AttachRolePolicy",
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:DeleteRolePermissionsBoundary",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy",
                "iam:PutRolePermissionsBoundary",
                "iam:PutRolePolicy",
                "iam:UpdateAssumeRolePolicy",
                "iam:UpdateRole",
                "iam:UpdateRoleDescription"
            ],
            "Resource": [
                "arn:aws:iam::*:role/aws-controltower-*",
                "arn:aws:iam::*:role/*AWSControlTower*",
                "arn:aws:iam::*:role/stacksets-exec-*"
            ],
            "Effect": "Deny",
            "Sid": "GRIAMROLEPOLICY"
        }
```

The following workarounds are available:

- (Most recommended) Assume the `AWSControlTowerExecution` role and
  create the `AWSControlTowerBlueprintAccess` role. If you choose this
  workaround, be sure to sign out from the `AWSControlTowerExecution`
  role immediately afterward, to prevent unintended changes to resources.
- Sign into an account that is not enrolled in AWS Control Tower, and therefore not
  subject to this SCP.
- Temporarily edit this SCP to permit the operation.
- (Strongly not recommended) Use your AWS Control Tower management account as your hub
  account, so it is not subject to the SCP.

## Customizing your policy document for AFC

blueprints based on CloudFormation

When you enable a blueprint through account factory, AWS Control Tower directs AWS CloudFormation to create
a StackSet on your behalf. AWS CloudFormation requires access to your managed account to create AWS CloudFormation
stacks in the StackSet. Although AWS CloudFormation already has administrator privileges in the
managed account through the `AWSControlTowerExecution` role, this role is not
assumable by AWS CloudFormation.

As part of enabling a blueprint, AWS Control Tower creates a role in the member account, which
AWS CloudFormation may assume to complete the StackSet management tasks. The simplest way to enable
your customized blueprint through account factory is to use an _allow-all_ policy, because those policies are compatible with any
blueprint template.

However, best practices suggest that you must restrict the permissions for AWS CloudFormation in
the target account. You can provide a customized policy, which AWS Control Tower applies to the
role it creates for AWS CloudFormation to use. For example, if your blueprint creates an SSM
Parameter called _something-important_, you could
provide the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCloudFormationActionsOnStacks",
 "Effect": "Allow",
 "Action": "cloudformation:*",
 "Resource": "arn:aws:cloudformation:*:*:stack/*"
 },
 {
 "Sid": "AllowSsmParameterActions",
 "Effect": "Allow",
 "Action": [
 "ssm:PutParameter",
 "ssm:DeleteParameter",
 "ssm:GetParameter",
 "ssm:GetParameters"
 ],
 "Resource": "arn:*:ssm:*:*:parameter/something-important"
 }
 ]
}`

```

The `AllowCloudFormationActionsOnStacks` statement is required for all AFC
custom policies; AWS CloudFormation uses this role to create stack instances, therefore it requires
permission to perform AWS CloudFormation actions on stacks. The `AllowSsmParameterActions`
section is specific to the template being enabled.

**Resolve permission issues**

When you enable a blueprint with a restricted policy, you may find that there are
insufficient permissions to enable the blueprint. To resolve these issues, revise your
policy document and update the member account's blueprint preferences to use the
corrected policy. To check that the policy is sufficient to enable the blueprint, ensure
that the AWS CloudFormation permissions are granted, and that you can create a stack directly using
that role.

## Additional permissions required for creating a Terraform-based Service Catalog product

When you're creating an AWS Service Catalog External product with a Terraform configuration file for AFC,
AWS Service Catalog requires certain permissions
to be added to your AFC custom IAM policy, in addition to permissions required to create
the resources defined in your template. If you choose the default full
**Admin** policy, you do not need to add these extra
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "resource-groups:CreateGroup",
 "resource-groups:ListGroupResources",
 "resource-groups:DeleteGroup",
 "resource-groups:Tag"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "tag:GetResources",
 "tag:GetTagKeys",
 "tag:GetTagValues",
 "tag:TagResources",
 "tag:UntagResources"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": "s3:GetObject",
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "s3:ExistingObjectTag/servicecatalog:provisioning": "true"
 }
 }
 }
 ]
}`

```

For more information about creating Terraform products using the External product type in AWS Service Catalog, see [Step 5:
Create launch roles](../../../servicecatalog/latest/adminguide/getstarted-launchrole-Terraform.md "../../../servicecatalog/latest/adminguide/getstarted-launchrole-Terraform.md") in the Service Catalog Administrator Guide.

## Transition to the AWS Service Catalog

External product type

AWS Service Catalog changed support for _Terraform Open Source_ products
and provisioned products to a new product type, called
_External_. To learn more about this transition, review [Updating existing Terraform Open Source products and provisioned products to
the External product type](../../../servicecatalog/latest/adminguide/update_terraform_open_source_to_external.md "../../../servicecatalog/latest/adminguide/update_terraform_open_source_to_external.md") in the _AWS Service Catalog administrator
guide_.

This change effects existing accounts that you created or enrolled with AWS Control Tower
account factory customization. To transition these accounts to the
_External_ product type, you need to make changes in both
AWS Service Catalog and AWS Control Tower.

###### To transition to the External product type

1. Upgrade your existing Terraform Reference Engine for AWS Service Catalog to include
   support for both _External_ and _Terraform Open
   Source_ product types. For instructions about updating your
   Terraform Reference Engine, review the [AWS Service Catalog GitHub Repository](https://github.com/aws-samples/service-catalog-engine-for-terraform-os "https://github.com/aws-samples/service-catalog-engine-for-terraform-os").
2. In AWS Service Catalog, duplicate any existing _Terraform Open
   Source_ products (blueprints), with the duplicates using the
   new _External_ product type. **Do not
   terminate the existing Terraform Open Source blueprints**.
3. In AWS Control Tower, update each account using a _Terraform Open
   Source_ blueprint to use the new _External_
   blueprint.
   1. To update a blueprint, you must first remove the
      _Terraform Open Source_ blueprint completely.
      For more details, review [Remove a blueprint from an account](remove-a-blueprint.md "remove-a-blueprint.md").
   2. Add the new _External_ blueprint to the same
      account. For more details, review [Add a blueprint to an AWS Control Tower account](add-blueprint-to-account.md "add-blueprint-to-account.md").

4. After all accounts using _Terraform Open Source_
   blueprints are updated to _External_ blueprints, return
   to AWS Service Catalog and terminate any products that use _Terraform Open
   Source_ as the product type.
5. Going forward, all accounts created or enrolled using AWS Control Tower account
   factory customization must reference blueprints using the
   _AWS CloudFormation_ or _External_ product
   type.

For blueprints created using the _External_ product
type, AWS Control Tower only supports account customizations that use Terraform
templates and the Terraform reference engine. To learn more, review [Set up for customization](afc-setup-steps.md "afc-setup-steps.md").

###### Note

AWS Control Tower does not support _Terraform Open Source_ as a
product type when creating new accounts. To learn more about these changes,
review [Updating existing Terraform Open Source products and provisioned products
to the _External_ product type](../../../servicecatalog/latest/adminguide/update_terraform_open_source_to_external.md "../../../servicecatalog/latest/adminguide/update_terraform_open_source_to_external.md") in the
_AWS Service Catalog administrator guide_. AWS Service Catalog will support
customers through this product type transition, as needed. Contact your account
representative to request assistance.
