# Use search paths in path extractors

The SerDe property syntax for path extractor contains a
`<path_extractor_expression>`:

```
"ion.`<column_name>`.path_extractor" = "`<path_extractor_expression>`"
```

You can use the `<path_extractor_expression>` to
specify a search path that parses the Amazon Ion document and finds matching data. The
search path is enclosed in parenthesis and can contain one or more of the following
components separated by spaces.

- Wild card – Matches all values.
- Index – Matches the value at the
  specified numerical index. Indices are zero-based.
- Text – Matches all values whose field
  names match are equivalent to the specified text.
- Annotations – Matches values specified
  by a wrapped path component that has the annotations specified.
  The following example shows an Amazon Ion document and some example search
  paths.

```
-- Amazon Ion document
{
    foo: ["foo1", "foo2"] ,
    bar: "myBarValue",
    bar: A::"annotatedValue"
}

-- Example search paths
(foo 0)       # matches "foo1"
(1)           # matches "myBarValue"
(*)           # matches ["foo1", "foo2"], "myBarValue" and A::"annotatedValue"
()            # matches {foo: ["foo1", "foo2"] , bar: "myBarValue", bar: A::"annotatedValue"}
(bar)         # matches "myBarValue" and A::"annotatedValue"
(A::bar)      # matches A::"annotatedValue"
```
