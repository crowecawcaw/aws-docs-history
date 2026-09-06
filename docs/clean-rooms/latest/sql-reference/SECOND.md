

# SECOND function
<a name="SECOND"></a>

The SECOND function is a time extraction function that takes a time or timestamp as input and returns the second component (a value between 0 and 60).

## Syntax
<a name="SECOND-syntax"></a>

```
second(timestamp)
```

## Arguments
<a name="SECOND-arguments"></a>

*timestamp*  
A TIMESTAMP expression.

## Returns
<a name="SECOND-returns"></a>

The SECOND function returns an INTEGER.

## Example
<a name="SECOND-example"></a>

The following example extracts the second component (`59`) from the input timestamp `'2009-07-30 12:58:59'`.

```
SELECT second('2009-07-30 12:58:59');
 59
```