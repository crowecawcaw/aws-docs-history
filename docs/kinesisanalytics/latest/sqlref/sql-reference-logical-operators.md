# Logical Operators

Logical operators let you establish conditions and test their results.

| Operator             | Unary/Binary | Description                                          | Operands                                    |
| -------------------- | ------------ | ---------------------------------------------------- | ------------------------------------------- |
| NOT                  | U            | Logical negation                                     | Boolean                                     |
| AND                  | B            | Conjunction                                          | Boolean                                     |
| OR                   | B            | Disjunction                                          | Boolean                                     |
| IS                   | B            | Logical assertion                                    | Boolean                                     |
| IS NOT UNKNOWN       | U            | Negated unknown comparison:<br><expr> IS NOT UNKNOWN | Boolean                                     |
| IS NULL              | U            | Null comparison:<br><expr> IS NULL                   | Any                                         |
| IS NOT NULL          | U            | Negated null comparison:<br><expr> IS NOT NULL       | Any                                         |
| =                    | B            | Equality                                             | Any                                         |
| !=                   | B            | Inequality                                           | Any                                         |
| <>                   | B            | Inequality                                           | Any                                         |
| >                    | B            | Greater than                                         | Ordered types (Numeric, String, Date, Time) |
| >=                   | B            | Greater than or equal to (not less than)             | Ordered types                               |
| <                    | B            | Less than                                            | Ordered types                               |
| <=                   | B            | Less than or equal to (not more than)                | Ordered types                               |
| BETWEEN              | Ternary      | Range comparison:<br>col1 BETWEEN expr1 AND expr2    | Ordered types                               |
| IS DISTINCT FROM     | B            | Distinction                                          | Any                                         |
| IS NOT DISTINCT FROM | B            | Negated distinction                                  | Any                                         |

## Three State Boolean Logic

SQL boolean values have three possible states rather than the usual two: TRUE, FALSE, and
UNKNOWN, the last of which is equivalent to a boolean NULL. TRUE and FALSE operands generally
function according to normal two-state boolean logic, but additional rules apply when pairing
them with UNKNOWN operands, as the tables that follow will show.

###### Note

UNKOWN represents "maybe TRUE, maybe FALSE" or, to put it another way, "not definitely
TRUE and not definitely FALSE." This understanding may help you clarify why some of the
expressions in the tables evaluate as they do.

| Negation (NOT) | Operation | Result |
| -------------- | --------- | ------ |
| NOT TRUE       | FALSE     |
| NOT FALSE      | TRUE      |
| NOT UNKNOWN    | UNKNOWN   |

| Conjunction (AND)   | Operation | Result |
| ------------------- | --------- | ------ |
| TRUE AND TRUE       | TRUE      |
| TRUE AND FALSE      | FALSE     |
| TRUE AND UNKNOWN    | UNKNOWN   |
| FALSE AND TRUE      | FALSE     |
| FALSE AND FALSE     | FALSE     |
| FALSE AND UNKNOWN   | FALSE     |
| UNKNOWN AND TRUE    | UNKNOWN   |
| UNKNOWN AND FALSE   | FALSE     |
| UNKNOWN AND UNKNOWN | UNKNOWN   |

| Disjunction (OR)   | Operation | Result |
| ------------------ | --------- | ------ |
| TRUE OR TRUE       | TRUE      |
| TRUE OR FALSE      | TRUE      |
| TRUE OR UNKNOWN    | TRUE      |
| FALSE OR TRUE      | TRUE      |
| FALSE OR FALSE     | FALSE     |
| FALSE OR UNKNOWN   | UNKNOWN   |
| UNKNOWN OR TRUE    | TRUE      |
| UNKNOWN OR FALSE   | UNKNOWN   |
| UNKNOWN OR UNKNOWN | UNKNOWN   |

| Assertion (IS)     | Operation | Result |
| ------------------ | --------- | ------ |
| TRUE IS TRUE       | TRUE      |
| TRUE IS FALSE      | FALSE     |
| TRUE IS UNKNOWN    | FALSE     |
| FALSE IS TRUE      | FALSE     |
| FALSE IS FALSE     | TRUE      |
| FALSE IS UNKNOWN   | FALSE     |
| UNKNOWN IS TRUE    | FALSE     |
| UNKNOWN IS FALSE   | FALSE     |
| UNKNOWN IS UNKNOWN | TRUE      |

| IS NOT UNKNOWN         | Operation | Result |
| ---------------------- | --------- | ------ |
| TRUE IS NOT UNKNOWN    | TRUE      |
| FALSE IS NOT UNKNOWN   | TRUE      |
| UNKNOWN IS NOT UNKNOWN | FALSE     |

IS NOT UNKNOWN is a special operator in and of itself. The expression "x IS NOT UNKNOWN"
is equivalent to "(x IS TRUE) OR (x IS FALSE)", not "x IS (NOT UNKNOWN)". Thus, substituting
in the table above:

| x       | Operation              | Result |         | Result of substituting for x in "(x IS TRUE) OR (x IS FALSE)"                                            |
| ------- | ---------------------- | ------ | ------- | -------------------------------------------------------------------------------------------------------- |
| TRUE    | TRUE IS NOT UNKNOWN    | TRUE   | becomes | "(TRUE IS TRUE) OR (TRUE IS FALSE)" -<br>• hence TRUE                                                    |
| FALSE   | FALSE IS NOT UNKNOWN   | TRUE   | becomes | "(FALSE IS TRUE) OR (FALSE IS FALSE)" -<br>• hence TRUE                                                  |
| UNKNOWN | UNKNOWN IS NOT UNKNOWN | FALSE  | becomes | "(UNKNOWN IS TRUE) OR (UNKNOWN IS FALSE)" -<br>• hence FALSE,<br>since UNKNOWN is neither TRUE not FALSE |

Since IS NOT UNKNOWN is a special operator, the operations above are not transitive around
the word IS:

| Operation              | Result |
| ---------------------- | ------ |
| NOT UNKNOWN IS TRUE    | FALSE  |
| NOT UNKNOWN IS FALSE   | FALSE  |
| NOT UNKNOWN IS UNKNOWN | TRUE   |

| IS NULL and IS NOT NULL | Operation | Result |
| ----------------------- | --------- | ------ |
| UNKNOWN IS NULL         | TRUE      |
| UNKNOWN IS NOT NULL     | FALSE     |
| NULL IS NULL            | TRUE      |
| NULL IS NOT NULL        | FALSE     |

| IS DISTINCT FROM and IS NOT DISTINCT FROM | Operation | Result |
| ----------------------------------------- | --------- | ------ |
| UNKNOWN IS DISTINCT FROM TRUE             | TRUE      |
| UNKNOWN IS DISTINCT FROM FALSE            | TRUE      |
| UNKNOWN IS DISTINCT FROM UNKNOWN          | FALSE     |
| UNKNOWN IS NOT DISTINCT FROM TRUE         | FALSE     |
| UNKNOWN IS NOT DISTINCT FROM FALSE        | FALSE     |
| UNKNOWN IS NOT DISTINCT FROM UNKNOWN      | TRUE      |

Informally, "x IS DISTINCT FROM y" is similar to "x <> y", except that it is true
even when either x or y (but not both) is NULL. DISTINCT FROM is the opposite of identical,
whose usual meaning is that a value (true, false, or unknown) is identical to itself, and
distinct from every other value. The IS and IS NOT operators treat UNKOWN in a special way,
because it represents "maybe TRUE, maybe FALSE".

## Other Logical Operators

For all other operators, passing a NULL or UNKNOWN operand will cause the result to be
UNKNOWN (which is the same as NULL).

| Examples                                                            | Operation | Result |
| ------------------------------------------------------------------- | --------- | ------ |
| TRUE AND CAST( NULL AS BOOLEAN)                                     | UNKNOWN   |
| FALSE AND CAST( NULL AS BOOLEAN)                                    | FALSE     |
| 1 > 2                                                               | FALSE     |
| 1 < 2                                                               | TRUE      |
| 'foo' = 'bar'                                                       | FALSE     |
| 'foo' <> 'bar'                                                      | TRUE      |
| 'foo' <= 'bar'                                                      | FALSE     |
| 'foo' <= 'bar'                                                      | TRUE      |
| 3 BETWEEN 1 AND 5                                                   | TRUE      |
| 1 BETWEEN 3 AND 5                                                   | FALSE     |
| 3 BETWEEN 3 AND 5                                                   | TRUE      |
| 5 BETWEEN 3 AND 5                                                   | TRUE      |
| 1 IS DISTINCT FROM 1.0                                              | FALSE     |
| CAST( NULL AS INTEGER ) IS NOT DISTINCT FROM CAST (NULL AS INTEGER) | TRUE      |
