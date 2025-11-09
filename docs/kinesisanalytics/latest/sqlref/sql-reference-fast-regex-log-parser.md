# FAST_REGEX_LOG_PARSER

```
FAST_REGEX_LOG_PARSE('input_string', 'fast_regex_pattern')
```

The FAST_REGEX_LOG_PARSE works by first decomposing the regular expression into a series of
regular expressions, one for each expression inside a group and one for each expression outside
a group. Any fixed length portions at the start of any expressions are moved to the end of the
previous expression. If any expression is entirely fixed length, it is merged with the previous
expression. The series of expressions is then evaluated using lazy semantics with no
backtracking. (In regular expression parsing parlance, "lazy" means don't parse more than you
need to at each step. "Greedy" means parse as much as you can at each step.)

The columns returned will be COLUMN1 through COLUMNn, where n is the number of groups in the
regular expression. The columns will be of type varchar(1024).  See sample usage below at First
FRLP Example and at Further FRLP Examples.

## FAST_REGEX_LOG_PARSER (FRLP)

FAST_REGEX_LOG_PARSER uses a lazy search - it stops at the first match. By contrast, the
[REGEX_LOG_PARSE](sql-reference-regex-log-parse.md "sql-reference-regex-log-parse.md") is greedy unless possessive quantifiers are used.

FAST_REGEX_LOG_PARSE scans the supplied input string for all the characters specified by
the Fast Regex pattern.  

- All characters in that input string must be accounted for by the characters and scan
  groups defined in the Fast Regex pattern. Scan groups define the fields-or-columns
  resulting when a scan is successful.
- If all characters in the input_string are accounted for when the Fast Regex pattern is
  applied, then FRLP creates an output field (column) from each parenthetical expression in
  that Fast Regex pattern, in left-to-right order. The first (leftmost) parenthetical
  expression creates the first output field, the next (second) parenthetical expression
  creates the second output field, up through the last parenthetical expression creating the
  last output field.
- If the input_string contains any characters not accounted for (matched) by applying
  Fast Regex pattern, then FRLP returns no fields at all.

## Character Class Symbols for Fast Regex

Fast Regex uses a different set of character class symbols from the regular regex
parser:

| Symbol or Construct                      | Meaning                              |
| ---------------------------------------- | ------------------------------------ | ----- |
| -                                        | Character range, including endpoints |
| [ charclasses ]                          | Character class                      |
| [^ charclasses ]                         | Negated character class              |
|                                          |                                      | Union |
| &                                        | Intersection                         |
| ?                                        | Zero or one occurrence               |
| \*                                       | Zero or more occurrences             |
| +                                        | One or more occurrences              |
| {n}                                      | n occurrences                        |
| {n,}                                     | n or more occurrences                |
| {n,m}                                    | n to m occurrences, including both   |
| .                                        | Any single character                 |
| #                                        | The empty language                   |
| @                                        | Any string                           |
| "<Unicode string without double-quotes>" | A string)                            |
| ( )                                      | The empty string)                    |
| ( unionexp )                             | Precedence override                  |
| < <identifier> >                         | Named pattern                        |
| <n-m>                                    | Numerical interval                   |
| charexp:=<Unicode character>             | A single non-reserved character      |
| \ <Unicode character>                    | A single character)                  |

We support the following POSIX standard identifiers as named patterns:

       <Digit>    -    "[0-9]"

       <Upper>    -    "[A-Z]"

       <Lower>    -    "[a-z]"

       <ASCII>    -    "[\u0000-\u007F]"

       <Alpha>    -    "<Lower>|<Upper>"

       <Alnum>    -    "<Alpha>|<Digit>"

       <Punct>    -    "[!\"#$%&'()\*+,-./:;<=>?@[\\\]^\_`{|}~]"

       <Blank>    -    "[ \t]"

       <Space>    -    "[ \t\n\f\r\u000B]"

       <Cntrl>    -    "[\u0000-\u001F\u007F]"

       <XDigit>    -    "0-9a-fA-F"

       <Print>    -    "<Alnum>|<Punct>"

       <Graph>    -    "<Print>"

First FRLP Example

This first example uses the Fast Regex pattern '(.\*)\_(.\_.\*)\_.\*'

```
select t.r."COLUMN1", t.r."COLUMN2" from
. . . . . . . . . . . . .> (values (FAST_REGEX_LOG_PARSE('Mary_had_a_little_lamb', '(.*)_(._.*)_.*'))) t(r);
+------------------------+-----------------------+
|         COLUMN1        |         COLUMN2       |
+------------------------+-----------------------+
| Mary_had               |     a_little_lamb     |
+------------------------+-----------------------+
1 row selected

```

1. The scan of input_string ('Mary_had_a_little_lamb') begins with the 1st group defined
   in Fast Regex pattern:  (.\*), which means "find any character 0 or more times."  

'**(.\*)**\_(.\_.\*)\_.\*' 2. This group specification, defining the first column to be parsed, asks the Fast Regex
Log Parser to accept input string characters starting from the input string's first
character until it finds the next group in the Fast Regex Pattern or the next literal
character or string that is not inside a group (not in parentheses). In this example, the
next literal character after the first group is an underscore:  

'(.\*)**\_**(.\_.\*)\_.\*' 3. The parser scans each character in the input string until it finds the next
specification in the Fast Regex pattern: an underscore:

'(.\*)\_**(.\_.\*)**\_.\*' 4. Group-2 thus begins with "a_l". Next, the parser needs to determine the end of this
group, using the remaining specification in the pattern:

'(.\*)\_(.\_.\*)**\_.\***'

###### Note

Character-strings or literals specified in the pattern but not inside a group must be
found in the input string but will not be included in any output field.

If the Fast Regex pattern had omitted the final asterisk, no results would be
obtained.

## Further FRLP Examples

The next example uses a "+", which means repeat the last expression 1 or more times ("\*"
means 0 or more times).

### Example A

In this case, the longest prefix is the first underscore. The first field/column group
will match on "Mary" and the second will not match.  

```
select t.r."COLUMN1", t.r."COLUMN2" from
      . . . . . . . . . . . . .> (values (FAST_REGEX_LOG_PARSE('Mary_had_a_little_lamb',
        '(.*)_+(._.*)'))) t(r);
      +----------+----------+
      | COLUMN1  | COLUMN2  |
      +----------+----------+
      +----------+----------+
      No rows selected
```

The preceding example returns no fields because the "+" required there be at least one
more underscore-in-a-row; and the input_string does not have that.

### Example B

In the following case, the '+' is superfluous because of the lazy semantics:

```
select t.r."COLUMN1", t.r."COLUMN2" from
      . . . . . . . . . . . . .> (values (FAST_REGEX_LOG_PARSE('Mary____had_a_little_lamb',
        '(.*)_+(.*)'))) t(r);
      +-------------------------+-------------------------+
      |         COLUMN1         |         COLUMN2         |
      +-------------------------+-------------------------+
      | Mary                    |    had_a_little_lamb    |
      +-------------------------+-------------------------+
      1 row selected
```

The preceding example succeeds in returning two fields because after finding the
multiple underscores required by the "\_+" specification, the group-2 specification (.\*)
accepts all remaining characters in the .input_string. Underscores do not appear trailing
"Mary" nor leading "had" because the "\_+" specification is not enclosed in
parentheses.

As mentioned in the introduction, "lazy" in regular expression parsing parlance means
don't parse more than you need to at each step;  "Greedy" means parse as much as you can at
each step.

The first case in this topic, A, fails because when it gets to the first underscore, the
regex processor has no way of knowing without backtracking that it can't use the underscore
to match "\_+", and FRLP doesn't backtrack, whereas [REGEX_LOG_PARSE](sql-reference-regex-log-parse.md "sql-reference-regex-log-parse.md")
does.  

The search directly above, B, gets turned into three searches:

```
(.*)_
_*(._
.*)

```

Notice that the second field group gets split between the second and third searches,
also that "\_+" is considered the same as "\_\_\*" (that is, it considers "underscore
repeat-underscore-1-or-more-times" the same as "underscore underscore
repeat-underscore-0-or-more-times".)

Case A demonstrates the main difference between REGEX_LOG_PARSE and
FAST_REGEX_LOG_PARSE, because the search in A would work under REGEX_LOG_PARSE because that
function would use backtracking.

### Example C

In the following example, the plus is not superfluous, because the "<Alpha> (any
alphabetic char) is fixed length thus will be used as a delimiter for the " +"
search.

```
select t.r."COLUMN1", t.r."COLUMN2" from
. . . . . . . . . . . . .> (values (FAST_REGEX_LOG_PARSE('Mary____had_a_little_lamb', '(.*)_+(<Alpha>.*)'))) t(r);
+----------------------------+----------------------------+
|          COLUMN1           |          COLUMN2           |
+----------------------------+----------------------------+
| Mary                       | had_a_little_lamb          |
+----------------------------+----------------------------+
1 row selected

'(.*) +(<Alpha>.*)' gets converted into three regular expressions:
'.* '
' *<Alpha>'
'.*$'
```

Each is matched in turn using lazy semantics.

The columns returned will be COLUMN1 through COLUMNn, where n is the number of groups in
the regular expression. The columns will be of type varchar(1024).
