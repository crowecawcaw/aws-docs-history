# Viewing provisioned product information

Each provisioned product has a Provisioned product details page with information about the
provisioned product. The Provisioned product details page is available from the initial launch
until the deletion of the provisioned product.

###### To view details about a provisioned product

1. Navigate to the **Provisioned product list**.
2. Choose the provisioned product.

###### Note

If the provisioned product you launch is a stack set, you own the stack set.
Ownership of individual stacks depends whether or not you have access to the accounts
where the stacks were deployed. For more information, see [Working with AWS CloudFormation StackSets](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md").

## Viewing Provisioned Product Status

Each provisioned product changes state as AWS Service Catalog attempts to create and
configure AWS resources with the product template and parameters the user enters during
launch. If successful, the provisioned product advances from an initial status of **Under change** to **Available**.

You can see a provisioned product's status in the Provisioned product list and in the
Provisioned product details page. An **Available** status
indicates that the product launched successfully and is ready for use.

When you update a provisioned product to use a new version or different parameters, the
provisioned product's status is **Under change**. If the update
succeeds, the provisioned product's changes to an **Available**
status.

A deleted provisioned product has an **Under change** status
during the termination process. At the completion of the termination process, the provisioned
product no longer exists in the AWS Service Catalog.

The operations you can perform on a provisioned product depend on the provisioned
product's status. For example, you can update or delete provisioned products that are
available, but not for provisioned products in the process of change.

## Viewing Outputs

Provisioned products provide information, called outputs, when a product launches.

Outputs usually display URLs, IP addresses, and database connection strings after the
provisioned product launches. Each output has a key, value, and description.

How you use the information from outputs depends on the type of product you launch. For
example, if the product launches an EC2 instance, the provisioned product might generate the
IP address of the instance. You could use the IP address to connect to the instance with a
Remote Desktop Connection or SSH.

## Viewing AWS CloudFormation Events

AWS CloudFormation provides information during each step of the launch and update processes. You can
obtain the information using an AWS CloudFormation ARN.

If the provisioned product uses an AWS CloudFormation stack, you can find the ARN in the
Provisioned product details page. (Expand the **Events** tab to find the current list of
events.)

When an AWS CloudFormation stack's status changes, such as new resources or errors, AWS CloudFormation logs an event with the following information:

- **Date** – The time that the event occurred, in local time.
- **Status** – The condition of a resource in a provisioned product, as
  opposed to the [Viewing Provisioned Product Status](#enduser-viewstack-status "#enduser-viewstack-status").
- **Type** – The type of resource the event registers. For
  details on resource types, see [Resource Types](../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md "../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md") in the
  _AWS CloudFormation User Guide_.
- **Logical ID** – The name of the resource, as defined in the
  template.
- **Status reason** – Additional information about the provisioned product's
  status, if available.
- **Physical ID** – The physical identifier of the resource,
  which appears when you choose an event.

## Entering Parameters

Enter parameters to launch or update a provisioned product. If you enter an incorrect parameter value when
you launch orupdate a provisioned product, `*CREATE_Failed*` appears in the **Viewing
AWS CloudFormation Events** section.

## Viewing Tags

Tags are metadata for the provisioned product during launch. The
Provisioned product details page also shows tags from the product and portfolio.

## Viewing Support Details

If your AWS Service Catalog administrator provided support information in this optional section, an email
address or site link is available to access support for your provisioned product. This section may also contain
additional support information. Administrators are responsible for maintaining the accuracy and access of
support information.
