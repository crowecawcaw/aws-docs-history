# Using Topics in Amazon Quick chat

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

You can use Topics in Amazon Quick chat to ask natural language questions that span
multiple datasets. The LLM-powered chat agent uses your defined relationships, dataset
enrichment metadata, and custom instructions to generate cross-dataset SQL queries and
return unified answers.

## How cross-dataset chat queries work

When you ask a natural language question against a Topic, the chat agent performs
the following steps:

1. **Intent parsing.** The agent identifies which
   columns map to your terms by matching against column names, descriptions, and
   synonyms from the enrichment metadata. It determines which datasets contain
   the relevant measures and dimensions.
2. **Relationship traversal.** Using the defined
   join keys and custom instructions, the agent determines the join path between
   identified datasets. It can traverse relationships to connect fact tables to
   the necessary dimension tables.
3. **SQL generation.** The agent constructs a SQL
   query with appropriate JOIN clauses, aggregation, and GROUP BY for the
   requested dimensions.
4. **Result presentation.** The answer is
   returned as a visualization or table, with the generated SQL available for
   inspection in the Explanation panel.

## Chat capabilities with Topics

The LLM-powered chat agent supports richer SQL generation than the defined
relationship path used in analysis sheets. When you configure a Topic for chat with
custom instructions, the agent can generate:

- Inner, left, right, and full outer joins
- Union queries across tables with the same schema
- Subqueries for negation patterns (for example, "customers who have never
  ordered")
- Cross-grain comparisons (for example, daily actuals versus monthly
  targets)
- Self-joins for recursive hierarchies (for example, employee-manager
  relationships)

The richer your enrichment metadata and custom instructions, the more accurately
the agent interprets ambiguous questions.

## Starting a chat with a Topic

To chat with a Topic:

- Navigate to the Topic and choose the chat icon. Your Topic is
  automatically available as the context.
- Or, from Amazon Quick chat, use the data filter to select
  **Specific data and apps** and choose your Topic.

Ask natural language questions that span multiple datasets. For example:

- "Show total sales by customer segment and store region"
- "What is the return rate by product category?"
- "Which stores are below 80% of their monthly target?"

Use the Explanation panel to view the generated SQL and verify that the correct
datasets and joins were used.

## Differences from legacy Topics in chat

The chat experience differs significantly between new Topics and legacy
Topics:

| Aspect                | New Topics                                                                          | Legacy Topics                                             |
| --------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------- |
| AI model              | LLM-powered chat agent                                                              | Legacy ML-based fuzzy search model                        |
| Cross-dataset queries | Yes — traverses relationships and generates<br>cross-dataset SQL with runtime joins | No — selects one dataset and queries only that<br>dataset |
| Join types            | Inner, left, right, full outer, union,<br>subquery                                  | Not applicable (single dataset)                           |
| SQL visibility        | Generated SQL shown in Explanation<br>panel                                         | Not available                                             |

###### Note

You can chat with both new Topics and legacy Topics. However, legacy Topics
use the legacy ML-based model and do not support cross-dataset queries. For
information about legacy Topics, see [Working with legacy Topics](legacy-topics.md "legacy-topics.md").
