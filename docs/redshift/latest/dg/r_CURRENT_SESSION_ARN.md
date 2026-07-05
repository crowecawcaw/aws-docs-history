Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# CURRENT\_SESSION\_ARN

Returns the ARN of the currently authorized global user. Global users present with the same identity across Redshift accounts, clusters, and
Serverless workgroups. Global users log in through IAM Identity Center, or through IAM-based session authentication. Data lake users are global
AWS users.

This function is typically used in the context of using multi-dialect AWS Glue views. For more information about identity management with IAM Identity Center and Redshift,
see [Connect Redshift with IAM Identity Center to give users a single sign-on experience](../mgmt/redshift-iam-access-control-idp-connect.md "../mgmt/redshift-iam-access-control-idp-connect.md"). For more information
about multi-dialect Glue views [Creating views in
the AWS Glue Data Catalog](data-catalog-views-overview.md "data-catalog-views-overview.md").

## Syntax

```
current_session_arn()
```

## Return type

Returns a VARCHAR string of the globally authenticated user or a null value.

## Usage notes

Local users aren't supported and result in a null response.

## Example

The following query returns the name of the current session ARN:

```
SELECT current_session_arn();

current_session_arn
--------------
arn:aws:iam::123456789012:user/user
(1 row)
```
