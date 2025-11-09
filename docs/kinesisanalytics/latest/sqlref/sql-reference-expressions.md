# Expressions and Literals

###### Value expressions

Value expressions are defined by the following syntax:

```
value-expression := <character-expression > | <number-expression> | <datetime-expression> | <interval-expression> | <boolean-expression>
```

###### Character (string) expressions

Character expressions are defined by the following syntax:

```
character-expression := <character-literal>
                  | <character-expression> || <character-expression>
                  | <character-function> ( <parameters> )

 character-literal  := <quote> { <character> }* <quote>
 string-literal     := <quote> { <character> }* <quote>
 character-function   :=   CAST | COALESCE | CURRENT_PATH
                  | FIRST_VALUE  | INITCAP | LAST_VALUE
                  | LOWER | MAX | MIN | NULLIF
                  | OVERLAY | SUBSTRING| SYSTEM_USER
                  | TRIM | UPPER
                  | <user-defined-function>

```

Note that Amazon Kinesis Data Analytics streaming SQL supports unicode character literals, such as
u&'foo'. As in the use of regular literals, you can escape single quotes in these, such
as u&'can''t'. Unlike regular literals, you can have unicode escapes: e.g.,
u&'\0009' is a string consisting only of a tab character. You can escape a \ with
another \, such as u&'back\\slash'. Amazon Kinesis Data Analytics also supports alternate escape characters,
such as u&'!0009!!' uescape '!' is a tab character.

###### Numeric expressions

Numeric expressions are defined by the following syntax:

```
number-expression := <number-literal>
                  | <number-unary-oper> <number-expression>
                  | <number-expression> <number-operator> <number-expression>
                  | <number-function> [ ( <parameters> ) ]
 number-literal :=   <UNSIGNED_INTEGER_LITERAL> | <DECIMAL_NUMERIC_LITERAL>
                           | <APPROX_NUMERIC_LITERAL>
```

```
--Note: An <APPROX_NUMERIC_LITERAL> is a number in scientific notation, such as with an
--exponent, such as 1e2 or -1.5E-6.
number-unary-oper := + | -
 number-operator      :=   + | - | / | *

 number-function      :=   ABS | AVG | CAST | CEIL
                          | CEILING | CHAR_LENGTH
                          | CHARACTER_LENGTH | COALESCE
                          | COUNT | EXP | EXTRACT
                          | FIRST_VALUE
                          | FLOOR | LAST_VALUE
                          | LN | LOG10
                          | MAX | MIN  | MOD
                          | NULLIF
                          | POSITION | POWER
                          | SUM| <user-defined-function>
```

###### Date / Time expressions

Date / Time expressions are defined by the following syntax:

```
datetime-expression := <datetime-literal>
                          | <datetime-expression> [ + | - ] <number-expression>
                          | <datetime-function> [ ( <parameters> ) ]
 datetime-literal    :=  <left_brace> { <character-literal> } *  <right_brace>
                          |  <DATE> { <character-literal> } *
                          |  <TIME> { <character-literal> } *
                          |  <TIMESTAMP> { <character-literal> } *
 datetime-function   :=    CAST | CEIL | CEILING
                          | CURRENT_DATE | CURRENT_ROW_TIMESTAMP
                          | CURRENT_ROW_TIMESTAMP
                          | FIRST_VALUE| FLOOR
                          | LAST_VALUE | LOCALTIME
                          | LOCALTIMESTAMP | MAX | MIN
                          | NULLIF | ROWTIME
                          | <user-defined-function>
 <time unit>         :=  YEAR | MONTH | DAY | HOUR | MINUTE | SECOND
```

###### Interval Expression

Interval expressions are defined by the following syntax:

```
interval-expression := <interval-literal>
                          | <interval-function>
 interval-literal    :=    <INTERVAL> ( <MINUS> | <PLUS> ) <QUOTED_STRING> <IntervalQualifier>
 IntervalQualifier  :=  <YEAR> ( <UNSIGNED_INTEGER_LITERAL> )
                          | <YEAR> ( <UNSIGNED_INTEGER_LITERAL> ) <TO> <MONTH>
                          |  <MONTH> [ ( <UNSIGNED_INTEGER_LITERAL> ) ]
                          |  <DAY> [ (  <UNSIGNED_INTEGER_LITERAL> )  ]
                          |  <DAY> [ (  <UNSIGNED_INTEGER_LITERAL> )  ] <TO>
                                    { <HOUR> | <MINUTE> | <SECOND> [ ( <UNSIGNED_INTEGER_LITERAL> ) ] }
                          |  <HOUR> [ (  <UNSIGNED_INTEGER_LITERAL> ) ]
                          |  <HOUR> [ (  <UNSIGNED_INTEGER_LITERAL> ) ] <TO>
                                    { <MINUTE> | <SECOND> [ <UNSIGNED_INTEGER_LITERAL> ] }
                          |  <MINUTE> [ ( <UNSIGNED_INTEGER_LITERAL> )  ]
                          |  <MINUTE> [ ( <UNSIGNED_INTEGER_LITERAL> )  ] <TO>
                                     <SECOND> [ ( <UNSIGNED_INTEGER_LITERAL> ) ]
                          |  <SECOND> [ ( <UNSIGNED_INTEGER_LITERAL> )  ]
 interval-function   :=    ABS  | CAST | FIRST_VALUE
                          | LAST_VALUE | MAX | MIN
                          | NULLIF| <user-defined-function>
```

###### Boolean expression

Boolean expressions are defined by the following syntax:

```
boolean-expression := <boolean-literal>
                  | <boolean-expression> <boolean-operator> <boolean-expression>
                  | <boolean-unary-oper> <boolean-expression>
                         | <boolean-function> ( <parameters> )
                         | ( <boolean-expression> )
 boolean-literal    :=  TRUE | FALSE
 boolean-operator   :=  AND | OR
 boolean-unary-oper :=  NOT
 boolean-function   :=    CAST | FIRST_VALUE | LAST_VALUE
                         | NULLIF | <user-defined-function>
```
