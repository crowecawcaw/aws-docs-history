

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CURRENT\_NAMESPACE
<a name="r_CURRENT_NAMESPACE"></a>

Returns the cluster namespace of the current Amazon Redshift cluster. Amazon Redshift cluster namespace is the unique ID of the Amazon Redshift cluster.

## Syntax
<a name="r_CURRENT_NAMESPACE-synopsis"></a>

```
current_namespace
```

## Return type
<a name="r_CURRENT_NAMESPACE-return-type"></a>

Returns a CHAR or VARCHAR string. 

## Example
<a name="r_CURRENT_NAMESPACE-example"></a>

The following query returns the name of the current namespace. 

```
select user, current_namespace; 
current_user | current_namespace
-------------+-------------------------------------
dwuser       | 86b5169f-01dc-4a6f-9fbb-e2e24359e9a8

(1 row)
```