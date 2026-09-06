

# Literals
<a name="sql-ref-literals-spark"></a>

A literal or constant is a fixed data value, composed of a sequence of characters or a numeric constant. 

AWS Clean Rooms Spark SQL supports several types of literals, including:
+ Numeric literals for integer, decimal, and floating-point numbers. 
+ Character literals, also referred to as strings, character strings, or character constants, used to specify a character string value.
+ Date, time, and timestamp literals, used with datetime data types. For more information, see [Date, time, and timestamp literals](Date_and_time_literals.md).
+ Interval literals. For more information, see [Interval literals](Interval_literals.md).
+ Boolean literals. For more information, see [Boolean literals](Boolean_literals-spark.md).
+ Null literals, used to specify a null value.
+ Only TAB, CARRIAGE RETURN (CR), and LINE FEED (LF) Unicode control characters from the Unicode general category (Cc) are supported.

AWS Clean Rooms Spark SQL doesn't support direct references to string literals in the SELECT clause, but they can be used within functions such as CAST.

## \+ (Concatenation) operator
<a name="DATE-CONCATENATE_function"></a>

Concatenates numeric literals, string literals, and/or datetime and interval literals. They are on either side of the \+ symbol and return different types based on the inputs on either side of the \+ symbol. 

### Syntax
<a name="Concatenation-operator-syntax"></a>

```
{{numeric}} + {{string}}
```

```
{{date}} + {{time}}
```

```
{{date}} + {{timetz}}
```

The order of the arguments can be reversed.

### Arguments
<a name="Concatenation-operator-arguments"></a>

{{numeric literals}}  
Literals or constants that represent numbers can be integer or floating-point.

{{string literals}}  
Strings, character strings, or character constants

{{date}}  
A DATE column or an expression that implicitly converts to a DATE.

{{time}}  
A TIME column or an expression that implicitly converts to a TIME.

{{timetz}}  
A TIMETZ column or an expression that implicitly converts to a TIMETZ.

### Example
<a name="Concatenation-operator-example"></a>

The following example table TIME\_TEST has a column TIME\_VAL (type TIME) with three values inserted.

```
select date '2000-01-02' + time_val as ts from time_test;
```