# AssumeConsistentDataTypes hint

openCypher follows a paradigm where matches of numerical datatypes (e.g., int, byte, short, long, etc.) are
carried out under type promotion semantics. For instance, when looking up all properties with an input value
10 with short type, under type promotion semantics, it would also match properties that have 10 as a long value.
In some cases, type casting can induce overhead and result in query plans that are less efficient than they could
be if no type casting was performed. In particular in cases where datatypes are used consistently in the data
(e.g., if all person’s ages are stored as long value) performing type promotions causes overhead without impacting
the query result.

To allow optimization for cases when it is known that numeric property data values stored in the database are of
consistent type, a query hint called `assumeConsistentDataTypes` (with value `true/false`, with
the default being `false`) can be used. When this query hint is supplied with a value of `true`,
the engine assumes the only property values are always long or double and will skip the type promotion semantics.
Numerical values specified in the query are considered to be either long values (for non-floating point values)
and double (for floating point values).

If the data is consistently using a single datatype (e.g. all ages are stored as `long`), then using the
`assumeConsistentDataTypes` hint can optimize the query by skipping unnecessary equality checks
for different numeric types. However, if the data has inconsistent datatypes for the same property, then using
the hint may cause some results to be missed, as the query will only match the single datatype that the hint assumes.

```
# Database loaded with following openCypher CSV's

# File 1
:ID,age:Int
n1,20
n2,25

# File 2
:ID,age:Long
n3,25


# Example (no hint)
MATCH (n:Person)
WHERE n.age >= 25
RETURN n

# Result
n2
n3

Returns all person whose age is >= 25 and the values >= 25 can be with any of these datatypes
i.e. byte, short, int, long, double or float

-----------------------------------------------------------------------------------

# Example (with hint present)
USING QUERY:assumeConsistentDataTypes "true"
MATCH (n:Person)
WHERE n.age >= 25
RETURN n

# Result
n3

Returns only "n3" and not "n2". The reason is that even though the numerical value
matches (25), the datatype is "int" and is considered a non-match.

```

The difference can also be validated via the explain.

Without the explain:

```
# Query
MATCH (n)
WHERE n.age = 20
RETURN n

# Explain Snippet
╔═════╤══════════╤══════════╤══════════════════════════════╤═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╤════════╤════════════╤══════════════╤═════════╤══════════════╗
║ ID │ Out #1 │ Out #2 │ Name                   │ Arguments                                                                                                                            │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠═════╪══════════╪══════════╪══════════════════════════════╪═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╪════════╪════════════╪══════════════╪═════════╪══════════════╣
║ 0  │ 1      │ -      │ DFEPipelineScan (DFX)  │ pattern=Node(?n) with property 'age' as ?n_age2 and label 'ALL'                                                                      │ -    │ 0        │ 1         │ 0.00  │ 0.10      ║
║    │        │        │                        │ inlineFilters=[(?n_age2 IN ["20"^^xsd:byte, "20"^^xsd:int, "20"^^xsd:long, "20"^^xsd:short, "20.0"^^xsd:double, "20.0"^^xsd:float])] │      │          │           │       │           ║
║    │        │        │                        │ patternEstimate=1                                                                                                                    │      │          │           │       │           ║
╟─────┼──────────┼──────────┼──────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼────────┼────────────┼──────────────┼─────────┼──────────────╢

# The inFilters field contains all numeric types

```

With the hint:

```
# Query
MATCH (n)
WHERE n.age = 20
RETURN n

# Explain Snippet
╔═════╤══════════╤══════════╤══════════════════════════════╤═════════════════════════════════════════════════════════════════════════════════╤════════╤════════════╤══════════════╤═════════╤══════════════╗
║ ID │ Out #1 │ Out #2 │ Name                   │ Arguments                                                       │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠═════╪══════════╪══════════╪══════════════════════════════╪═════════════════════════════════════════════════════════════════════════════════╪════════╪════════════╪══════════════╪═════════╪══════════════╣
║ 0  │ 1      │ -      │ DFEPipelineScan (DFX)  │ pattern=Node(?n) with property 'age' as ?n_age2 and label 'ALL' │ -    │ 0        │ 1         │ 0.00  │ 0.07      ║
║    │        │        │                        │ inlineFilters=[(?n_age2 IN ["20"^^xsd:long])]                   │      │          │           │       │           ║
║    │        │        │                        │ patternEstimate=1                                               │      │          │           │       │           ║
╟─────┼──────────┼──────────┼──────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────┼────────┼────────────┼──────────────┼─────────┼──────────────╢

# The inFilters field only contains long datatype

```
