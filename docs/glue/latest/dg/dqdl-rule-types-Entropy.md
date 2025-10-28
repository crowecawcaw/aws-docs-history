# Entropy

Checks whether the _entropy_ value of a column matches
a given expression. Entropy measures the level of information that's contained in a message.
Given the probability distribution over values in a column, entropy describes how many bits
are required to identify a value.

**Syntax**

```
Entropy `<COL_NAME>` `<EXPRESSION>`
```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

**Supported column types**: Any column type

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Column entropy**

The following example rule checks that the column named `Feedback` has an
entropy value greater than one.

```
Entropy "Star_Rating" > 1
Entropy "First_Name" > 1  where "Customer_ID < 10"
```

**Sample dynamic rules**

- `Entropy "colA" < max(last(10))`
- `Entropy "colA" between min(last(10)) and max(last(10))`
