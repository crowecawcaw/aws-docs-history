

# Using service-linked roles for Amazon ECS
<a name="using-service-linked-roles"></a>

Amazon Elastic Container Service uses AWS Identity and Access Management (IAM) [ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Amazon ECS. Service-linked roles are predefined by Amazon ECS and include all the permissions that the service requires to call other AWS services on your behalf.

**Topics**
+ [Using roles to allow Amazon ECS to manage clusters](using-service-linked-roles-for-clusters.md)
+ [Using roles to manage Amazon ECS Managed Instances](using-service-linked-roles-instances.md)