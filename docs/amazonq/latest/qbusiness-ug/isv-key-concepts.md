# Key concepts

Amazon Q index

A comprehensive collection of a company's data that can be queried to
build enhanced application experiences. It serves as the foundation for
retrieving relevant content across various enterprise data sources.

Organizations that are Amazon Q Business customers and would like to connect
their data sources with a supported ISV can add the ISV as a _data
accessor_. For more information, see [Data
accessors](data-accessors.md "data-accessors.md").

`SearchRelevantContent` API operation

This API operation enables ISVs to access the Amazon Q index. It supports
keyword, semantic, and hybrid queries—allowing for flexible data
retrieval options.

AWS Identity and Access Management IAM Identity CenterManaged Application

Amazon Q Business manages end user access to a customer's Amazon Q index using
IAWS Identity and Access Management IAM Identity Center.

Resource-based policy

A resource-based policy is an IAM policy that's attached to a resource.
Amazon Q Business attaches [a
resource-based policy](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") to an Amazon Q Business application environment during the
data accessor setup. This policy grants the ISV's AWS account the
necessary permissions to access content for the customer's end users from
the customer's data sources through the `SearchRelevantContent`
API operation. By attaching a resource-based policy to the data accessor's
AWS account, it allows access to the Amazon Q index of the application environment.
For more information, see [Data
accessors](data-accessors.md "data-accessors.md").
