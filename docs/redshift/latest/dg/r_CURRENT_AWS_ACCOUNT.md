

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CURRENT\_AWS\_ACCOUNT
<a name="r_CURRENT_AWS_ACCOUNT"></a>

Returns the AWS account associated with the Amazon Redshift cluster that submitted a query.

## Syntax
<a name="r_CURRENT_AWS_ACCOUNT-synopsis"></a>

```
current_aws_account
```

## Return type
<a name="r_CURRENT_AWS_ACCOUNT-return-type"></a>

Returns an integer. 

## Example
<a name="r_CURRENT_AWS_ACCOUNT-example"></a>

The following query returns the name of the current database. 

```
select user, current_aws_account; 
current_user | current_account
-------------+--------------- 
dwuser       | 987654321

(1 row)
```