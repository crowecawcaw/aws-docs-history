

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STV\_SLICES
<a name="r_STV_SLICES"></a>

Use the STV\_SLICES table to view the current mapping of a slice to a node.

 The information in STV\_SLICES is used mainly for investigation purposes.

STV\_SLICES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data). 

## Table columns
<a name="r_STV_SLICES-table-columns2"></a>


| Column name | Data type | Description | 
| --- | --- | --- | 
| node | integer | Cluster node where the slice is located. | 
| slice | integer | Node slice. | 
| localslice | integer | This information is for internal use only. | 
| type | character(1) | This information is for internal use only. | 

## Sample query
<a name="r_STV_SLICES-sample-query2"></a>

To view which cluster nodes are managing which slices, type the following query:

```
select node, slice from stv_slices;
```

This query returns the following sample output:

```
 node | slice
------+-------
    0 |     2
    0 |     3
    0 |     1
    0 |     0
(4 rows)
```