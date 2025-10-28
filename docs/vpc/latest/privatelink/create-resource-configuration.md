# Create a resource configuration in

VPC Lattice

Use the console to create a resource configuration.

###### To create a resource configuration using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **PrivateLink and Lattice**,
   choose **Resource configurations**.
3. Choose **Create resource configuration**.
4. Enter a name that is unique within your AWS account. You can't change this
   name after the resource configuration is created.
5. For **Configuration type**, choose
   **Resource** for a single or child resource or
   **Resource group** for a group of child resources.
6. Choose a resource gateway that you previously created or create a one
   now.
7. Choose the identifier for the resource that you want this resource
   configuration to represent.
8. Choose the port ranges through which you want to share the resource.
9. For **Association settings**, specify whether this resource
   configuration can be associated with shareable service networks.
10. For **Share resource configuration**, choose the resource
    shares that identify the principals who can access this resource.
11. (Optional) For **Monitoring**, enable **Resource
    access logs** and the delivery destination if you want to monitor
    requests and responses to and from the resource configuration.
12. (Optional) To add a tag, choose **Add new tag** and enter the
    tag key and the tag value.
13. Choose **Create resource configuration**.

###### To create a resource configuration using the AWS CLI

Use the [create-resource-configuration](../../../cli/latest/reference/vpc-lattice/create-resource-configuration.md "../../../cli/latest/reference/vpc-lattice/create-resource-configuration.md") command.
