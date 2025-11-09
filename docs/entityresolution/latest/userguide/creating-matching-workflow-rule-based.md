# Creating a rule-based matching

workflow

_[Rule-based
matching](glossary.md#rule-based-matching-defn "glossary.md#rule-based-matching-defn")_ is a hierarchical set of waterfall matching rules, suggested by
AWS Entity Resolution, based upon the data that you input and is completely configurable by you. The
rule-based matching workflow enables you to compare cleartext or hashed data to find exact
matches based on criteria that you customize.

When AWS Entity Resolution finds a match between two or more records in your data, it assigns:

- A [Match ID](glossary.md#match-id-defin "glossary.md#match-id-defin") to the
  records in the matched set of data
- The [Match rule](glossary.md#match-rule-defn "glossary.md#match-rule-defn")
  that generated the match.
  When you create a rule-based matching workflow in AWS Entity Resolution, you must choose either a
  **Simple** or **Advanced** rule type. The rule type
  determines the complexity of rule conditions you can create. You can't change the rule type
  after creating the workflow.

You can use the following chart to compare the two **Rule types** and
determine which one suits your use case.

| Rule type comparison chart                                                  | Use case | Advanced rule type       | Simple rule type |
| --------------------------------------------------------------------------- | -------- | ------------------------ | ---------------- |
| Schema mappings mapped one-to-one with input types                          | Yes      | No                       |
| Schema mapping with multiple data columns mapped to the same input<br>types | No       | Yes                      |
| Supports Exact and Fuzzy matching                                           | Yes      | No (Exact matching only) |
| Supports AND, OR, and parentheses operators                                 | Yes      | No (AND operator only)   |
| Supports batch workflows                                                    | Yes      | Yes                      |
| Supports incremental workflows                                              | Yes      | Yes                      |
| Supports real-time workflows                                                | No       | Yes                      |
| Supports ID mapping workflows                                               | No       | Yes                      |

After you have determined which rule type you want to use, use the following topics to
create a rule-based matching workflow with either the **Advanced** or
**Simple** rule type.

###### Topics

- [Creating a rule-based matching workflow with the
  Advanced rule type](rule-based-mw-advanced.md "rule-based-mw-advanced.md")
- [Creating a rule-based matching workflow with the
  Simple rule type](rule-based-mw-simple.md "rule-based-mw-simple.md")
