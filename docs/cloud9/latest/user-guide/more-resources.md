AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Working with resources

In addition to accessing AWS services that are listed by default in the AWS Explorer,
you can go to **Resources** and choose from hundreds of resources to add to the
interface. In AWS, a **resource** is an entity you can work with.
Some of the resources that are added include Amazon AppFlow, Amazon Kinesis Data Streams, AWS IAM roles, Amazon VPC, and
Amazon CloudFront distributions.

To view available resources, go to **Resources** and expand the
resource type to list the available resources for that type. For example, if you select the
`AWS::Lambda::Function` resource type, you can access the resources that define
different functions, their properties, and their attributes.

After adding a resource type to **Resources**, you can interact with it and
its resources in the following ways:

- View a list of existing resources that are available in the current AWS Region for
  this resource type.
- View a read-only version of the JSON file that describes a
  resource.
- Copy the resource identifier for the resource.
- View the AWS documentation that explains the purpose of the resource type and the
  schema (in JSON and YAML formats) for modeling a resource.

## IAM permissions for accessing resources

You require specific AWS Identity and Access Management permissions to access the resources associated with
AWS services. For example, an IAM entity, such as a user or a role, requires Lambda
permissions to access `AWS::Lambda::Function` resources.

In addition to permissions for service resources, an IAM entity requires permissions to
permit the AWS Toolkit to call AWS Cloud Control API operations. Cloud Control API
operations allow the IAM user or role to access and update the remote resources.

You can quickly grant permissions by attaching the AWS managed policy, **PowerUserAccess**, to the IAM entity that's calling these API
operations using the Toolkit interface. This managed
policy grants a range of permissions for performing application development tasks,
including calling API operations.

For specific permissions that define allowable API operations on remote resources, see the
[AWS Cloud Control API User Guide.](../../../cloudcontrolapi/latest/userguide/security.md "../../../cloudcontrolapi/latest/userguide/security.md")

## Interacting with existing resources

1. In the **AWS Explorer**, choose
   **Resources**.

A list of resource types is displayed under the **Resources** node. 2. There's documentation describing the syntax that defines the template for a resource
type. To access this documentation, open the context (right-click) menu for that resource
type and choose **View Documentation**.

###### Note

You might be asked to switch off your browser's popup blocker so you can access the
documentation page. 3. To view the resources that already exist for a resource type, expand the entry for
that type.

A list of available resources is displayed under their resource type. 4. To interact with a specific resource, open the context (right-click) menu for its name
and choose one of the following options:

    * **Copy Identifier**: Copy the identifier for the specific
     resource to the clipboard. For example, the `AWS::DynamoDB::Table` resource
     can be identified using the `TableName` property.
    * **Preview**: View a read-only version of the
     JSON-formatted template that describes the resource.
