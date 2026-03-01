# Specifying DB parameters

DB parameter types include the following:

- Integer
- Boolean
- String
- Long
- Double
- Timestamp
- Object of other defined data types
- Array of values of type integer, Boolean, string, long, double, timestamp, or object
  You can also specify integer and Boolean parameters using expressions, formulas, and
  functions.

###### Contents

- [DB parameter formulas](USER_ParamValuesRef.md#USER_ParamFormulas "USER_ParamValuesRef.md#USER_ParamFormulas")
  - [DB parameter formula variables](USER_ParamValuesRef.md#USER_FormulaVariables "USER_ParamValuesRef.md#USER_FormulaVariables")
  - [DB parameter formula operators](USER_ParamValuesRef.md#USER_FormulaOperators "USER_ParamValuesRef.md#USER_FormulaOperators")

- [DB parameter functions](USER_ParamValuesRef.md#USER_ParamFunctions "USER_ParamValuesRef.md#USER_ParamFunctions")
- [DB parameter log expressions](USER_ParamValuesRef.md#USER_ParamLogExpressions "USER_ParamValuesRef.md#USER_ParamLogExpressions")
- [DB parameter value examples](USER_ParamValuesRef.md#USER_ParamValueExamples "USER_ParamValuesRef.md#USER_ParamValueExamples")

## DB parameter formulas

A DB parameter formula is an expression that resolves to an integer value or a Boolean
value. You enclose the expression in braces: {}. You can use a formula for either a
DB parameter value or as an argument to a DB parameter function.

**Syntax**

```
{*FormulaVariable*}
{*FormulaVariable***Integer*}
{*FormulaVariable***Integer*/*Integer*}
{*FormulaVariable*/*Integer*}
```

### DB parameter formula variables

Each formula variable returns an integer or a Boolean value. The names of the variables
are case-sensitive.

_AllocatedStorage_

Returns an integer representing the size, in bytes, of the data volume.

_DBInstanceClassMemory_

Returns an integer for the number of bytes of memory available to the database process.
This number is internally calculated by starting with the total
amount of memory for the DB instance class. From this, the calculation
subtracts memory reserved for the operating system and the RDS
processes that manage the instance. Therefore, the number is always
somewhat lower than the memory figures shown in the instance class
tables in [Amazon AuroraDB instance classes](Concepts.md "Concepts.md"). The exact value
depends on a combination of factors. These include instance class,
DB engine, and whether it applies to an RDS instance or an instance
that's part of an Aurora cluster.

_DBInstanceVCPU_

Returns an integer representing the number of virtual central processing units (vCPUs)
used by Amazon RDS to manage the instance.

_EndPointPort_

Returns an integer representing the port used when connecting to the DB instance.

_TrueIfReplica_

Returns `1` if the DB instance is a read replica and `0` if it is not.
This is the default value for the `read_only` parameter
in Aurora MySQL.

### DB parameter formula operators

DB parameter formulas support two operators: division and multiplication.

_Division operator: /_

Divides the dividend by the divisor, returning an integer quotient. Decimals in the
quotient are truncated, not rounded.

Syntax

```
*dividend* / *divisor*
```

The dividend and divisor arguments must be integer expressions.

\*Multiplication operator: \*\*

Multiplies the expressions, returning the product of the expressions. Decimals in the
expressions are truncated, not rounded.

Syntax

```
*expression* * *expression*
```

Both expressions must be integers.

## DB parameter functions

You specify the arguments of DB parameter functions as either integers or formulas. Each
function must have at least one argument. Specify multiple arguments as a
comma-separated list. The list can't have any empty members, such as
_argument1_,,_argument3_. Function names
are case-insensitive.

_IF_

Returns an argument.

Syntax

```
IF(*argument1*, *argument2*, *argument3*)
```

Returns the second argument if the first argument evaluates to true. Returns the third argument otherwise.

_GREATEST_

Returns the largest value from a list of integers or parameter formulas.

Syntax

```
GREATEST(*argument1*, *argument2*,...*argumentn*)
```

Returns an integer.

_LEAST_

Returns the smallest value from a list of integers or parameter formulas.

Syntax

```
LEAST(*argument1*, *argument2*,...*argumentn*)
```

Returns an integer.

_SUM_

Adds the values of the specified integers or parameter formulas.

Syntax

```
SUM(*argument1*, *argument2*,...*argumentn*)
```

Returns an integer.

## DB parameter log expressions

You can set an integer DB parameter value to a log expression. You enclose the expression
in braces: {}. For example:

```
{log(DBInstanceClassMemory/8187281418)*1000}
```

The `log` function represents log base 2. This example also uses the
`DBInstanceClassMemory` formula variable. See [DB parameter formula variables](#USER_FormulaVariables "#USER_FormulaVariables").

## DB parameter value examples

These examples show using formulas, functions, and expressions for the values of DB
parameters.

###### Warning

Improperly setting parameters in a DB parameter group can have unintended adverse effects.
These might include degraded performance and system instability. Use caution
when modifying database parameters and back up your data before modifying your
DB parameter group. Try out parameter group changes on a test DB instance,
created using point-in-time-restores, before applying those parameter group
changes to your production DB instances.

###### Example using the DB parameter function LEAST

You can specify the `LEAST` function in an Aurora MySQL
`table_definition_cache` parameter value. Use it to set the
number of table definitions that can be stored in the definition cache to the
lesser of `DBInstanceClassMemory`/393040 or 20,000.

```
LEAST({DBInstanceClassMemory/393040}, 20000)
```
