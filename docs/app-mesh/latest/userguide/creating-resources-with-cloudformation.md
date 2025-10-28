# Creating App Mesh resources with

AWS CloudFormation

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

App Mesh is integrated with AWS CloudFormation, a service that helps you model and set up your
AWS resources so that you can spend less time creating and managing your resources and
infrastructure. You create a template that describes all the AWS resources that you
want, for example an App Mesh mesh, and AWS CloudFormation takes care of provisioning and configuring
those resources for you.

When you use AWS CloudFormation, you can reuse your template to set up your App Mesh resources
consistently and repeatedly. Just describe your resources once, and then provision the
same resources over and over in multiple AWS accounts and Regions.

## App Mesh and AWS CloudFormation templates

To provision and configure resources for App Mesh and related services, you must
understand [AWS CloudFormation
templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates are formatted text files in JSON or YAML. These
templates describe the resources that you want to provision in your AWS CloudFormation stacks. If
you're unfamiliar with JSON or YAML, you can use AWS CloudFormation Designer to help you get
started with AWS CloudFormation templates. For more information, see [What is AWS CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the
_AWS CloudFormation User Guide_.

App Mesh supports creating meshes, routes, virtual nodes, virtual routers, and
virtual services

in AWS CloudFormation. For more information, including examples of JSON and YAML templates for
your App Mesh resources, see [App Mesh resource type
reference](../../../AWSCloudFormation/latest/UserGuide/AWS_AppMesh.md "../../../AWSCloudFormation/latest/UserGuide/AWS_AppMesh.md") in the _AWS CloudFormation User Guide_.

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User
  Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation Command Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
