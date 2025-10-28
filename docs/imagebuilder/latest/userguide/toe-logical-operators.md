# Use logical operators in

AWSTOE component documents

You can use the following logical operators to add or modify conditional
expressions in your component document. AWSTOE evaluates conditional expressions
in the order that the conditions are specified. For more information about comparison
operators for component documents, see [Use comparison operators in
AWSTOE component documents](toe-comparison-operators.md "toe-comparison-operators.md").

**and**

With the `and` operator, you can evaluate two or more
comparisons as a single expression. The expression evaluates to `true`
when all of the conditions in the list are true. Otherwise, the expression
evaluates to `false`.

###### Examples:

The following example performs two comparisons – a string and
a number. Both comparisons are true, so the expression evaluates to
true.

```
and:
  - stringEquals: 'test_string'
    value: 'test_string'
  - numberEquals: 1
    value: 1
```

The following example also performs two comparisons. The first comparison
is false, at which point evaluation stops and the second comparison
is skipped. The expression evaluates to `false`.

```
and:
  - stringEquals: 'test_string'
    value: 'Hello world!'
  - numberEquals: 1
    value: 1
```

**or**

With the `or` operator, you can evaluate two or more
comparisons as a single expression. The expression evaluates to `true`
when one of the specified comparisons is true. If none of the specified
comparisons evaluate to `true`, the expression evaluates to
`false`.

###### Examples:

The following example performs two comparisons – a string and
a number. The first comparison is true, so the expression evaluates
to `true` and the second comparison is skipped.

```
or:
  - stringEquals: 'test_string'
    value: 'test_string'
  - numberEquals: 1
    value: 3
```

The following example also performs two comparisons. The first comparison
is false, and evaluation continues. The second comparison is true, so the
expression evaluates to `true`.

```
or:
  - stringEquals: 'test_string'
    value: 'Hello world!'
  - numberEquals: 1
    value: 1
```

In the final example, both comparisons are false, so the expression
evaluates to `false`.

```
or:
  - stringEquals: 'test_string'
    value: 'Hello world!'
  - numberEquals: 1
    value: 3
```

**not**

With the `not` operator, you can negate a single comparison.
The expression evaluates to `true` if the comparison is false. If
the comparison is true, then the expression evaluates to `false`.

###### Examples:

The following example performs a string comparison. The comparison is
false, so the expression evaluates to `true`.

```
not:
  - stringEquals: 'test_string'
    value: 'Hello world!'
```

The following example also performs a string comparison. The comparison is
true, so the expression evaluates to `false`.

```
not:
  - stringEquals: 'test_string'
    value: 'test_string'
```
