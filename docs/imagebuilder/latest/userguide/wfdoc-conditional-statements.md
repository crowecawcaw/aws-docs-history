# Use conditional statements in your workflow steps

Conditional statements begin with the `if` statement document attribute.
The ultimate purpose of the `if` statement is to determine whether to run the
step action or to skip it. If the `if` statement resolves to `true`,
then the step action runs. If it resolves to `false`, Image Builder skips the step action
and records a step status of `SKIPPED` in the log.

The `if` statement supports branching statements (`and`,
`or`) and conditional modifiers (`not`). It also supports the
following comparison operators that perform value comparisons (equal, less than, greater
than) based on the data types it compares (string or number).

###### Supported comparison operators

- `booleanEquals`
- `numberEquals`
- `numberGreaterThan`
- `numberGreaterThanEquals`
- `numberLessThan`
- `numberLessThanEquals`
- `stringEquals`

###### Rules for branching statements and conditional modifiers

The following rules apply for branching statements (`and`, `or`)
and conditional modifiers (`not`).

- Branching statements and conditional modifiers must appear on a line
  by themselves.
- Branching statements and conditional modifiers must follow level rules.

      + There can only be one statement at the parent level.
      + Each child branch or modifier starts a new level.

  For more information about levels, see [Nested levels in conditional statements](#wfdoc-conditional-structure "#wfdoc-conditional-structure").

- Each branching statement must have at least one child conditional statement,
  but no more than ten.
- Conditional modifiers operate on only one child conditional statement.

## Nested levels in conditional statements

Conditional statements operate at several levels in a section of their own.
For example, the `if` statement attribute appears at the same level
in your workflow document as the step name and action. This is the base of the
conditional statement.

You can specify up to four levels of conditional statements, but only one
statement can appear at the parent level. All other branching statements,
conditional modifiers, or conditional operators are indented from there,
one indent per level.

The following outline shows the maximum number of nested levels for a
conditional statement.

```
`base:
 parent:
 - child (level 2)
 - child (level 3)
 child (level 4)`
```

`if` attribute

The `if` attribute specifies the conditional statement as a document
attribute. This is level zero.

Parent level

This is the first level of nesting for conditional statements. There can
be only one statement at this level. If you don't need branching or modifiers,
this can be a conditional operator with no child statements. This level doesn't
use dash notation, except for conditional operators.

Child levels

Levels two through four are considered child levels. Child statements can
include branching statements, conditional modifiers, or conditional operators.

###### Example: Nested levels

The following example shows the maximum number of levels in a conditional statement.

```
`if:
 and: #first level
 - stringEquals: 'my_string' #second level
 value: 'my_string'
 - and: #also second level
 - numberEquals: '1' #third level
 value: 1
 - not: #also third level
 stringEquals: 'second_string' #fourth level
 value: "diff_string"`
```

###### Nesting rules

- Each branch or modifier at the child level starts
  a new level.
- Each level is indented.
- There can be a maximum of four levels, including one
  statement, modifier, or operator at the parent level, and
  up to three additional levels.

## Conditional statement examples

This group of examples show various aspects of conditional statements.

###### Branching: and

The `and` branching statement operates on a list of expressions
that are children of the branch, all of which must evaluate to `true`.
Image Builder evaluates the expressions in the order that they appear in the list. If any
expression evaluates to `false`, then processing stops and the branch
is considered `false`.

The following example evaluates to `true`, because both expressions
evaluate to `true`.

```
`if:
 and:
 - stringEquals: 'test_string'
 value: 'test_string'
 - numberEquals: 1
 value: 1`
```

###### Branching: or

The `or` branching statement operates on a list of expressions
that are children of the branch, at least one of which must evaluate to
`true`. Image Builder evaluates the expressions in the order that they
appear in the list. If any expression evaluates to `true`, then
processing stops and the branch is considered `true`.

The following example evaluates to `true`, even though the first
expression is `false`.

```
`if:
 or:
 - stringEquals: 'test_string'
 value: 'test_string_not_equal'
 - numberEquals: 1
 value: 1`
```

###### Conditional modifier: not

The `not` conditional modifier negates the conditional statements
that are children of the branch.

The following example evaluates to `true` when the `not`
modifier negates the `stringEquals` conditional statement.

```
`if:
 not:
 - stringEquals: 'test_string'
 value: 'test_string_not_equal'`
```

###### Conditional statement: booleanEquals

The `booleanEquals` comparison operator compares Boolean values
and returns true if the Boolean values exact match.

The following example determines if `collectImageScanFindings`
is enabled.

```
`if:
 - booleanEquals: true
 value: '$.imagebuilder.collectImageScanFindings'`
```

###### Conditional statement: stringEquals

The `stringEquals` comparison operator compares two strings
and returns true if the strings are an exact match. If either value
isn't a string, Image Builder converts it to a string before it compares.

The following example compares the platform system variable to determine if
the workflow is running on a Linux platform.

```
`if:
 - stringEquals: 'Linux'
 value: '$.imagebuilder.Platform'`
```

###### Conditional statement: numberEquals

The `numberEquals` comparison operator compares two numbers
and returns true if the numbers are equal. The numbers to compare must be
one of the following formats.

- Integer
- Float
- A string that matches the following regex pattern:
  `^-?[0-9]+(\.)?[0-9]+$`.

The following example comparisons all evaluate to `true`.

```
`if:
 # Value provider as a number
 numberEquals: 1
 value: '1'

 # Comparison value provided as a string
 numberEquals: '1'
 value: 1

 # Value provided as a string
 numberEquals: 1
 value: '1'

 # Floats are supported
 numberEquals: 5.0
 value: 5.0

 # Negative values are supported
 numberEquals: -1
 value: -1`
```
