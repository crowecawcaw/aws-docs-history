# Attribute-based access control

In AWS Lake Formation, you can grant access on AWS Glue Data Catalog objects such as catalogs, databases,
tables, and data filters using attributes that are IAM tags and session tags associated with
IAM entities such as roles and users.

For more information about using session tags, see [assume-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role.html")
in the AWS CLI user guide.

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes. AWS calls these attributes _tags_. You can use ABAC to
grant access to principals within the same account or in another account on the Data Catalog
resources. Any IAM principal with matching IAM tag or session tag keys and values gains
access to the resource. You must have grantable permissions on the resources to make these
grants.

ABAC allows you to grant access to multiple users at the same time. When new users join the
organization, their access to data can be automatically determined based on their attributes,
such as their job function or department, without requiring administrators to manually assign
specific roles or permissions. By using attributes instead of roles, ABAC provides a more
streamlined and maintainable way to manage data access across diverse systems and environments,
ultimately enhancing data governance and compliance.

For more information about defining attributes,
see [Define permissions based on attributes with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md").

For information on limitations, considerations, and supported AWS Regions, see [Attribute-based access control considerations,
limitations, and supported regions](abac-considerations.md "abac-considerations.md").

###### Topics

- [Prerequisites for granting permissions using attributes](abac-prerequisites.md "abac-prerequisites.md")
- [Granting permissions using attribute-based access control](abac-granting-permissions.md "abac-granting-permissions.md")
