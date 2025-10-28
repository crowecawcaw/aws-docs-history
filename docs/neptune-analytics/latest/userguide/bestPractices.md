# Best practices

The following are some general recommendations for working with Neptune Analytics. Use this information as a reference to quickly find
recommendations for maximizing performance while using Neptune Analytics.

###### Contents

- [openCypher query best practices](best-practices-content.md "best-practices-content.md")
  - [Use the SET clause to remove multiple properties at once](best-practices-content.md#best-practices-content-1 "best-practices-content.md#best-practices-content-1")
  - [Use parameterized queries](best-practices-content.md#best-practices-content-2 "best-practices-content.md#best-practices-content-2")
  - [Use flattened maps instead of nested maps in UNWIND clause](best-practices-content.md#best-practices-content-3 "best-practices-content.md#best-practices-content-3")
  - [Place more restrictive nodes on the left side in
    Variable-Length Path (VLP) expressions](best-practices-content.md#best-practices-content-4 "best-practices-content.md#best-practices-content-4")
  - [Avoid redundant node label checks by using granular relationship names](best-practices-content.md#best-practices-content-5 "best-practices-content.md#best-practices-content-5")
  - [Specify edge labels where possible](best-practices-content.md#best-practices-content-6 "best-practices-content.md#best-practices-content-6")
  - [Avoid using the WITH clause when possible](best-practices-content.md#best-practices-content-7 "best-practices-content.md#best-practices-content-7")
  - [Place restrictive filters as early in the query as possible](best-practices-content.md#best-practices-content-8 "best-practices-content.md#best-practices-content-8")
  - [Explicitly check whether properties exist](best-practices-content.md#best-practices-content-9 "best-practices-content.md#best-practices-content-9")
  - [Do not use named path (unless it is required)](best-practices-content.md#best-practices-content-10 "best-practices-content.md#best-practices-content-10")
  - [Avoid COLLECT(DISTINCT())](best-practices-content.md#best-practices-content-11 "best-practices-content.md#best-practices-content-11")
  - [Prefer the properties function over individual property lookup when
    retrieving all property values](best-practices-content.md#best-practices-content-12 "best-practices-content.md#best-practices-content-12")
  - [Perform static computations outside of the query](best-practices-content.md#best-practices-content-13 "best-practices-content.md#best-practices-content-13")
  - [Batch inputs using UNWIND instead of individual statements](best-practices-content.md#best-practices-content-14 "best-practices-content.md#best-practices-content-14")
  - [Prefer using custom IDs for node](best-practices-content.md#best-practices-content-15 "best-practices-content.md#best-practices-content-15")
  - [Avoid doing ~id computations in the query](best-practices-content.md#best-practices-content-16 "best-practices-content.md#best-practices-content-16")
