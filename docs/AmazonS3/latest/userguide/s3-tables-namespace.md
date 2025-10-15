# Table namespaces

When you create tables within your Amazon S3 table bucket, you organize them into logical groupings
 called *namespaces*. Unlike S3 tables and table buckets, namespaces
 aren't resources. Namespaces are constructs that help you organize and manage your tables in a scalable
 manner. For example, all the tables belonging to the human resources department in a company could be
 grouped under a common namespace value of `hr`.

To control access to specific namespaces, you can use table bucket resource policies. For more
 information, see [Resource-based policies for
 S3 Tables](s3-tables-resource-based-policies.md "s3-tables-resource-based-policies.md").

The following rules apply to table namespaces:


* Each namespace must be unique within a table bucket.
* You can create up to 10,000 namespaces per table bucket.
* Each table name must be unique within a namespace.
* Each table can have only one level of namespaces. Namespaces can't be nested.
* Each table belongs to a single namespace.
* You can move your tables between namespaces.
Table namespaces are referred to as databases in various AWS services and query engines. The following table maps the terminology used for S3 Tables namespaces to some common engines and services.



| **Service or Engine** | **Terminology** |
| --- | --- |
| AWS Lake Formation | Database |
| AWS Glue Data Catalog | Database |
| Athena | Database |
| Spark | Namespace |

###### Topics

* [Creating a namespace](s3-tables-namespace-create.md "s3-tables-namespace-create.md")
* [Delete a namespace](s3-tables-namespace-delete.md "s3-tables-namespace-delete.md")
