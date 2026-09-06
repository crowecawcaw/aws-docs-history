

# endsWith
<a name="endsWith-function"></a>

`endsWith` evaluates if the expression ends with a substring that you specify. If the expression ends with the substring, `endsWith` returns true, and otherwise it returns false.

## Syntax
<a name="endsWith-function-syntax"></a>

```
endsWith({{expression}}, {{substring}}, {{string-comparison-mode}})
```

## Arguments
<a name="endsWith-function-arguments"></a>

 *expression*   
The expression must be a string. It can be the name of a field that uses the string data type, a literal value like **'12 Main Street'**, or a call to another function that outputs a string.

 *substring*   
The set of characters to check against the *expression*. The substring can occur one or more times in the *expression*.

 *string-comparison-mode*   
(Optional) Specifies the string comparison mode to use:  
+ `CASE_SENSITIVE` – String comparisons are case-sensitive. 
+ `CASE_INSENSITIVE` – String comparisons are case-insensitive.
This value defaults to `CASE_SENSITIVE` when blank.

## Return type
<a name="endsWith-function-return-type"></a>

Boolean

## Examples
<a name="endsWith-function-example"></a>

### Default case sensitive example
<a name="endsWith-function-example-default-case-sensitive"></a>

The following case sensitive example evaluates if `state_nm` endsWith **"York"**.

```
endsWith({{state_nm}}, {{"York"}})
```

The following are the given field values.

```
New York
new york
```

For these field values, the following values are returned.

```
true
false
```

### Case insensitive example
<a name="endsWith-function-example-case-insensitive"></a>

The following case insensitive example evaluates if `state_nm` endsWith **"york"**.

```
endsWith({{state_nm}}, {{"york"}}, CASE_INSENSITIVE)
```

The following are the given field values.

```
New York
new york
```

For these field values, the following values are returned.

```
true
true
```

### Example with conditional statements
<a name="endsWith-function-example-conditional-statements"></a>

The `endsWith` function can be used as the conditional statement within the following If functions: [avgIf](https://docs.aws.amazon.com/quicksight/latest/user/avgIf-function.html), [minIf](https://docs.aws.amazon.com/quicksight/latest/user/minIf-function.html), [distinct\_countIf](https://docs.aws.amazon.com/quicksight/latest/user/distinct_countIf-function.html), [countIf](https://docs.aws.amazon.com/quicksight/latest/user/countIf-function.html), [maxIf](https://docs.aws.amazon.com/quicksight/latest/user/maxIf-function.html), [medianIf](https://docs.aws.amazon.com/quicksight/latest/user/medianIf-function.html), [stdevIf](https://docs.aws.amazon.com/quicksight/latest/user/stdevIf-function.html), [stdevpIf](https://docs.aws.amazon.com/quicksight/latest/user/stdevpIf-function.html), [sumIf](https://docs.aws.amazon.com/quicksight/latest/user/sumIf-function.html), [varIf](https://docs.aws.amazon.com/quicksight/latest/user/varIf-function.html), and [varpIf](https://docs.aws.amazon.com/quicksight/latest/user/varpIf-function.html). 

The following example sums `Sales` only if `state_nm` ends with **"York"**.

```
sumIf({{Sales}},endsWith({{state_nm}}, {{"York"}}))
```

### Does NOT contain example
<a name="endsWith-function-example-does-not-start-with"></a>

The conditional `NOT` operator can be used to evaluate if the expression does not start with the specified substring. 

```
NOT(endsWith({{state_nm}}, {{"York"}}))
```

### Example using numeric values
<a name="endsWith-function-example-numeric-values"></a>

Numeric values can be used in the expression or substring arguments by applying the `toString` function.

```
endsWith({{state_nm}}, toString({{5}}) )
```