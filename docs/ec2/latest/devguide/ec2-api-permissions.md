

# Granting required permissions for Amazon EC2 resources
<a name="ec2-api-permissions"></a>

By default, users, groups, and roles don't have permission to create or modify Amazon EC2 resources, or perform tasks using the Amazon EC2 API. To create or modify EC2 resources and perform tasks, see [Identity and access management for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-iam.html) in the *Amazon EC2 User Guide*.

When you make an API request, the parameters that you specify in the request determine the required permissions for your EC2 resources. If the user, group, or role that makes the request doesn’t have the required permission, the request fails. For example, to use `RunInstances` to launch an instance in a subnet (by specifying the `SubnetId` parameter), a user must have permission to use the VPC.

*Resource-level permissions* refers to the ability to specify which resources users are allowed to perform actions on. Amazon EC2 has partial support for resource-level permissions. This means that for certain Amazon EC2 actions, you can control when users are allowed to use those actions based on conditions that have to be fulfilled, or specific resources that users are allowed to use. For example, you can grant users permission to launch instances, but only of a specific type, and only using a specific AMI.

For more information about the resources that are created or modified by the Amazon EC2 actions, and the ARNs and Amazon EC2 condition keys that you can use in an IAM policy statement, see [Actions, resources, and condition keys for Amazon EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html) in the *Service Authorization Reference*.

For example policies, see [IAM policies for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html) in the *Amazon EC2 User Guide*.