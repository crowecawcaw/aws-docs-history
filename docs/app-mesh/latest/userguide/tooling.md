# App Mesh tooling

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

App Mesh gives customers the ability to interact with its APIs indirectly using tools such as:

- CloudFormation
- AWS Cloud Development Kit (AWS CDK)
- App Mesh Controller for Kubernetes
- Terraform

## App Mesh and CloudFormation

CloudFormation is a service that lets you create a template with all the resources you need for your
application, and then CloudFormation will configure and provision the resouces for you. It will also configure
all the dependencies, so you can focus more on you application and less on managing resources.

For more information and examples on using CloudFormation with App Mesh, see the [CloudFormation
documentation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.md").

## App Mesh and AWS CDK

AWS CDK is a development framework for using code to define your cloud infrastructure and using CloudFormation
to provision it. AWS CDK supports multiple programming languages including TypeScript, JavaScript,
Python, Java, and C#/.Net.

For more information on using AWS CDK with App Mesh, see the [AWS CDK documentation](../../../cdk/api/latest/docs/aws-appmesh-readme.md "../../../cdk/api/latest/docs/aws-appmesh-readme.md").

## App Mesh controller for Kubernetes

The App Mesh controller for Kubernetes helps you to manage your App Mesh resources for a Kubernetes
cluster and inject sidecars into pods. This controller is specifically for use with Amazon EKS and allows
you to manage your resources in a manner that is native to Kubernetes.

For more information on the App Mesh controller, see the [App Mesh Controller
documentation](https://aws.github.io/aws-app-mesh-controller-for-k8s/ "https://aws.github.io/aws-app-mesh-controller-for-k8s/").

## App Mesh and Terraform

[Terraform](https://www.terraform.io/ "https://www.terraform.io/") is an open-source infrastructure as code
software tool. Terraform can manage cloud services using thier CLI and interacts with APIs using
declaritive configuration files.

To see more about using App Mesh with Terraform, check out the [Terraform documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/appmesh_mesh "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/appmesh_mesh").
