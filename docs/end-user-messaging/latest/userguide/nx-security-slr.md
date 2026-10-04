

# Using service-linked roles for AWS End User Messaging
<a name="nx-security-slr"></a>

AWS End User Messaging uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS End User Messaging. Service-linked roles are predefined by AWS End User Messaging and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AWS End User Messaging easier because you do not have to manually add the necessary permissions. AWS End User Messaging defines the permissions of its service-linked roles, and unless defined otherwise, only AWS End User Messaging can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This protects your AWS End User Messaging resources because you cannot inadvertently remove permission to access the resources.