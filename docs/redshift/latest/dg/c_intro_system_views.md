Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# System monitoring (provisioned only)

The following system tables and views can be queried on provisioned clusters.
STL and STV tables and views contain a subset of data found in several of the system
tables. These provide quicker and easier access to commonly queried data found in those
tables.

SVCS views provide details about queries on both the main and
concurrency scaling clusters. SVL views provide information only for queries run on the main cluster,
with the exception of SVL_STATEMENTTEXT. SVL_STATEMENTTEXT can contain information
for queries run on concurrency scaling clusters as well as the main cluster.

###### Topics

- [STL views for logging](c_intro_STL_tables.md "c_intro_STL_tables.md")
- [STV tables for snapshot data](c_intro_STV_tables.md "c_intro_STV_tables.md")
- [SVCS views for main and concurrency scaling clusters](svcs_views.md "svcs_views.md")
- [SVL views for main cluster](svl_views.md "svl_views.md")
