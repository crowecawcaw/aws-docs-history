Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Define primary key and foreign

key constraints

Define primary key and foreign key constraints between tables wherever appropriate.
Even though they are informational only, the query optimizer uses those constraints to
generate more efficient query plans.

Do not define primary key and foreign key constraints unless your application
enforces the constraints. Amazon Redshift does not enforce unique, primary-key, and foreign-key
constraints.

See [Table constraints](t_Defining_constraints.md "t_Defining_constraints.md")
for additional information about how Amazon Redshift uses constraints.
