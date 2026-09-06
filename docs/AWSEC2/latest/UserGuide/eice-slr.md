

# Service-linked role for EC2 Instance Connect Endpoint
<a name="eice-slr"></a>

Amazon EC2 uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Amazon EC2. Service-linked roles are predefined by Amazon EC2 and include all the permissions that Amazon EC2 requires to call other AWS services on your behalf. For more information, see [Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html) in the *IAM User Guide*.

## Service-linked role permissions for EC2 Instance Connect Endpoint
<a name="slr-permissions"></a>

Amazon EC2 uses **AWSServiceRoleForEC2InstanceConnect** to create and manage network interfaces in your account that are required by EC2 Instance Connect Endpoint.

The **AWSServiceRoleForEC2InstanceConnect** service-linked role trusts the following service to assume the role: 
+ `ec2-instance-connect.amazonaws.com`

The **AWSServiceRoleForEC2InstanceConnect** service-linked role uses the following managed policy:
+ **Ec2InstanceConnectEndpoint**

To view the permissions for the managed policy, see [Ec2InstanceConnectEndpoint](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/Ec2InstanceConnectEndpoint.html) in the *AWS Managed Policy Reference*.

## Create a service-linked role for EC2 Instance Connect Endpoint
<a name="create-slr"></a>

You don't need to manually create this service-linked role. When you create an EC2 Instance Connect Endpoint, Amazon EC2 creates the service-linked role for you.

## Edit a service-linked role for EC2 Instance Connect Endpoint
<a name="edit-slr"></a>

EC2 Instance Connect Endpoint doesn't allow you to edit the **AWSServiceRoleForEC2InstanceConnect** service-linked role.

## Delete a service-linked role for EC2 Instance Connect Endpoint
<a name="delete-slr"></a>

If you no longer need to use EC2 Instance Connect Endpoint, we recommend that you delete the **AWSServiceRoleForEC2InstanceConnect** service-linked role.

You must delete all EC2 Instance Connect Endpoint resources before you can delete the service-linked role.

To delete the service-linked role, see [Delete a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete-slr) in the *IAM User Guide*.

You must configure permissions to allow an IAM entity (a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions) in the *IAM User Guide*.