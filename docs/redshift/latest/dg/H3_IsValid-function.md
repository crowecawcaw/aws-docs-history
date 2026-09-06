

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# H3\_IsValid
<a name="H3_IsValid-function"></a>

H3\_IsValid returns true if the input represents an H3 cell ID, otherwise false. For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3).

## Syntax
<a name="H3_IsValid-function-syntax"></a>

```
H3_IsValid(index)
```

## Arguments
<a name="H3_IsValid-function-arguments"></a>

 *index*   
A value of data type `BIGINT` or `VARCHAR`, or an expression that evaluates to one of these data types.

## Return type
<a name="H3_IsValid-function-return"></a>

`BOOLEAN` – true if the input represents a valid H3 cell ID, false otherwise.

If *index* is NULL, then NULL is returned.

## Examples
<a name="H3_IsValid-function-examples"></a>

The following SQL inputs a VARCHAR that represents an H3 cell ID, and returns true.

```
SELECT H3_IsValid('8025fffffffffff');
```

```
 h3_isvalid
------------
 true
```

The following SQL inputs a BIGINT that represents an H3 cell ID, and returns true.

```
SELECT H3_IsValid(577129255373111295);
```

```
 h3_isvalid
------------
 true
```

The following SQL inputs an invalid H3 cell ID and returns false.

```
SELECT H3_IsValid('');
```

```
 h3_isvalid
------------
 false
```