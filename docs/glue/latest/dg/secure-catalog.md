# Securing your Data Catalog using Lake Formation

AWS Lake Formation is a service that makes it easier to set up a secure data lake in AWS.
It provides a central place to create and securely manage your data lakes by defining fine-granied access control permissions.
Lake Formation uses the Data Catalog to store and retrieve metadata about your data lake, such as table definitions, schema information, and data access control settings.

You can register your Amazon S3 data location of the metadata table or database with Lake Formation and use it to define metadata-level permissions on the Data Catalog resources.
You can also use Lake Formation to manage storage access permissions on the underlying data stored in Amazon S3 on behalf of integrated analytical engines.

For more information see [What is AWS Lake Formation?](lake-formation/latest/dg/what-is-lake-formation.md "lake-formation/latest/dg/what-is-lake-formation.md").
