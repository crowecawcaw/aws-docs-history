Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Dynamic data masking

###### Note

Amazon Redshift automatically masks certain system table columns when logging information
about queries made to Data Catalog views to prevent exposure of sensitive metadata. For
more information, see
[Secure logging](../mgmt/db-auditing-secure-logging.md "../mgmt/db-auditing-secure-logging.md") in the _Amazon Redshift Management Guide_.

Using dynamic data masking (DDM) in Amazon Redshift, you can protect sensitive data in your data warehouse.
You can manipulate how Amazon Redshift shows sensitive data to the user at query time, without
transforming it in the database. You control access to data through masking policies that apply
custom obfuscation rules to a given user or role. In that way, you can respond to changing privacy
requirements without altering underlying data or editing SQL queries.

Dynamic data masking policies hide, obfuscate, or pseudonymize data that matches a given
format. When attached to a table, the masking expression is applied to one or more of
its columns. You can further modify masking policies to only apply them to certain
users, or to user-defined roles that you can create with [Role-based access control (RBAC)](t_Roles.md "t_Roles.md"). Additionally, you can apply DDM on the cell level by using
conditional columns when creating your masking policy. For more information about
conditional masking, see [Conditional dynamic data masking](t_ddm-conditional.md "t_ddm-conditional.md").

You can apply multiple masking policies with varying levels of obfuscation to the same
column in a table and assign them to different roles. To avoid conflicts when you have
different roles with different policies applying to one column, you can set priorities
for each application. In that way, you can control what data a given user or role can
access. DDM policies can partially or completely redact data, or hash it by
using user-defined functions written in SQL, Python, or with AWS Lambda.
By masking data using hashes, you can apply joins on
this data without access to potentially sensitive information.
