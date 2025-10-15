# Amazon S3 table bucket, table, and namespace naming rules

When you create a table bucket, you choose a bucket name and AWS Region, the name must be unique
 for your account in the chosen Region. After you create a table bucket, you can't change the bucket name
 or Region. Table bucket names must follow specific naming rules. For more information about naming rules
 for table buckets and the tables and namespaces within them, see the following topic.

###### Topics

* [Table bucket naming rules](#table-buckets-naming-rules "#table-buckets-naming-rules")
* [Naming rules for tables and namespaces](#naming-rules-table "#naming-rules-table")

## Table bucket naming rules


When you create Amazon S3 table buckets, you specify a table bucket name. Like other bucket types,
 table buckets can't be renamed. Unlike other bucket types, table buckets aren't in a global namespace,
 so each bucket name in your account needs to be unique only within your current AWS Region. 


For general purpose bucket naming rules, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md"). For directory bucket naming rules, see [Directory bucket naming rules](directory-bucket-naming-rules.md "directory-bucket-naming-rules.md").


The following naming rules apply for table buckets.



* Bucket names must be between 3 and 63 characters long.
* Bucket names can consist only of lowercase letters, numbers, and hyphens
 (`-`).
* Bucket names must begin and end with a letter or number.
* Bucket names must not contain any underscores (`_`) or periods
 (`.`).
* Bucket names must not start with any of the following reserved prefixes: 




	+ `xn--`
	+ `sthree-`
	+ `amzn-s3-demo-`
	+ `aws`
* Bucket names must not end with any of the following reserved suffixes:




	+ `-s3alias`
	+ `--ol-s3`
	+ `--x-s3`
	+ `--table-s3`

## Naming rules for tables and namespaces


The following naming rules apply to tables and namespaces within table buckets:



* Names must be between 1 and 255 characters long.
* Names can consist only of lowercase letters, numbers, and underscores (`_`).
* Names must begin and end with a letter or number.
* Names must not contain hyphens (`-`) or periods (`.`).
* A table name must be unique within a namespace.
* A namespace must be unique within a table bucket.
* Namespace names must not start with the reserved prefix `aws`.

###### Important

When creating tables, make sure that you use all lowercase letters in your table names and table
 definitions. For example, make sure that your column names are all lowercase. If your table name or
 table definition contains capital letters, the table isn't supported by AWS Lake Formation or the AWS Glue Data Catalog. In
 this case, your table won't be visible to AWS analytics services such as Amazon Athena, even if your table
 buckets are integrated with AWS analytics services. 

If your table definition contains capital letters, you receive the following error message when
 running a `SELECT` query in Athena: **`"GENERIC_INTERNAL_ERROR: Get table request
 failed: com.amazonaws.services.glue.model.ValidationException: Unsupported Federation Resource -
 Invalid table or column names."`**
