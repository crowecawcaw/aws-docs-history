

# Using service-linked roles for AWS Marketplace
<a name="buyer-using-service-linked-roles"></a>

AWS Marketplace uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS Marketplace. Service-linked roles are predefined by AWS Marketplace and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AWS Marketplace easier because you don't have to add the necessary permissions manually. AWS Marketplace defines the permissions of its service-linked roles, and unless defined otherwise, only AWS Marketplace can assume its roles. The defined permissions include the trust policy and the permissions policy. That permissions policy can't be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html), and look for the services with **Yes ** in the **Service-linked roles** column. Choose a **Yes ** with a link to view the service-linked role documentation for that service.

## Supported Regions for AWS Marketplace service-linked roles
<a name="buyer-slr-regions"></a>

AWS Marketplace supports using service-linked roles in all of the AWS Regions where the service is available. For more information, see [AWS Marketplace Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/aws-marketplace.html#aws-marketplace_region).