

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# COLLATE function
<a name="r_COLLATE"></a>

The COLLATE function overrides the collation of a string column or expression. 

For information on how to create tables using database collation, see [CREATE TABLE](r_CREATE_TABLE_NEW.md).

For information on how to create databases using database collation, see [CREATE DATABASE](r_CREATE_DATABASE.md).

## Syntax
<a name="r_COLLATE-synopsis"></a>

```
COLLATE( string, 'case_sensitive' | 'cs' | 'case_insensitive' | 'ci');
```

## Arguments
<a name="r_COLLATE-argument"></a>

 *string*   
A string column or expression that you want to override.

 *'case\_sensitive'* \| *'cs'* \| *'case\_insensitive'* \| *'ci'*   
A string constant of a collation name. Amazon Redshift only supports the following values for this parameter:  
+  *case\_sensitive* 
+  *cs* 
+  *case\_insensitive* 
+  *ci* 
*case\_sensitive* and *cs* are interchangeable and yield the same results. Similarly, *case\_insensitive* and *ci* are interchangeable and yield the same results.

## Return type
<a name="r_COLLATE-return-type"></a>

The COLLATE function returns `VARCHAR`, `CHAR`, or `SUPER` depending on the first input expression type. This function only changes the collation of the first input argument and won't change its output value.

## Examples
<a name="r_COLLATE-example"></a>

To create table T and define col1 in table T as `case_sensitive`, use the following example.

```
CREATE TABLE T ( col1 Varchar(20) COLLATE case_sensitive );

INSERT INTO T VALUES ('john'),('JOHN');
```

 When you run the first query, Amazon Redshift only returns `john`. After the COLLATE function runs on col1, the collation becomes `case_insensitive`. The second query returns both `john` and `JOHN`. 

```
SELECT * FROM T WHERE col1 = 'john';

+------+
| col1 |
+------+
| john |
+------+

SELECT * FROM T WHERE COLLATE(col1, 'case_insensitive') = 'john';

+------+
| col1 |
+------+
| john |
| JOHN |
+------+
```

To create table A and define col1 in table A as `case_insensitive`, use the following example.

```
CREATE TABLE A ( col1 Varchar(20) COLLATE case_insensitive );

INSERT INTO A VALUES ('john'),('JOHN');
```

 When you run the first query, Amazon Redshift returns both `john` and `JOHN`. After the COLLATE function runs on col1, the collation becomes `case_sensitive`. The second query returns only `john`. 

```
SELECT * FROM A WHERE col1 = 'john';

+------+
| col1 |
+------+
| john |
| JOHN |
+------+

SELECT * FROM A WHERE COLLATE(col1, 'case_sensitive') = 'john';

+------+
| col1 |
+------+
| john |
+------+
```