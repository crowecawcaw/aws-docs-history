# Using service-linked roles for
 CloudTrail

AWS CloudTrail uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
 linked directly to CloudTrail. Service-linked roles are predefined by CloudTrail and
 include all the permissions that the service requires to call other AWS services on your
 behalf.

###### Topics

* [Using roles for creating and managing CloudTrail organization trails and CloudTrail Lake organization event data stores in CloudTrail](using-service-linked-roles-create-slr-for-org-trails.md "using-service-linked-roles-create-slr-for-org-trails.md")
* [Supported Regions for CloudTrail
 service-linked roles](#slr-regions-create-slr-for-org-trails "#slr-regions-create-slr-for-org-trails")
* [Using roles for creating and managing CloudTrail event context in CloudTrail](using-service-linked-roles-create-slr-for-context-management.md "using-service-linked-roles-create-slr-for-context-management.md")
* [Supported Regions for CloudTrail
 service-linked roles](#slr-regions-create-slr-for-context-management "#slr-regions-create-slr-for-context-management")

## Supported Regions for CloudTrail
 service-linked roles


CloudTrail supports using service-linked roles in all of the AWS Regions where CloudTrail and Organizations
 are both available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html "https://docs.aws.amazon.com/general/latest/gr/rande.html") in the *AWS General Reference*.


## Supported Regions for CloudTrail
 service-linked roles


CloudTrail supports using service-linked roles in all of the Regions where CloudTrail and EventBridge are available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html "https://docs.aws.amazon.com/general/latest/gr/rande.html").
