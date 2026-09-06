

# Adding custom instructions to a Topic
<a name="topics-custom-instructions"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  Amazon Quick administrators and authors  | 

Custom instructions are persistent natural language rules that guide the AI engine in interpreting domain-specific terminology and cross-dataset logic. Without them, the engine interprets terms literally. For example, "this year" defaults to the calendar year. However, if your organization runs on a fiscal year starting April 1, you need an instruction to override that default.

Custom instructions are especially useful for:
+ **Disambiguation rules.** When the same business term could map to multiple datasets or fields, tell the AI which one to prefer. For example: "When the user asks about 'sales', use SALES\_FACT. When the user asks about 'returns' or 'refunds', use RETURNS\_FACT."
+ **Cross-dataset definitions.** Define metrics that span multiple datasets. For example: "Net Revenue = SUM(SALES\_FACT.total\_amount) - SUM(RETURNS\_FACT.refund\_amount)."
+ **Default join behavior.** Specify the join direction that preserves intended semantics. For example: "Prefer LEFT JOIN from fact tables to dimension tables so that facts without matching dimension records are not silently dropped."
+ **Custom date logic.** For example: "Fiscal year starts April 1. Interpret 'this year' using fiscal year boundaries."

**To add custom instructions**

1. Open the Topic that you want to configure.

1. Navigate to the **Custom instructions** tab.

1. Choose **Edit**.

1. Enter your instructions as natural language rules. Use bullet-point style for clarity.

1. Choose **Save changes**.

## Example custom instructions
<a name="topics-custom-instructions-example"></a>

The following example shows a production-ready set of topic-level instructions for a retail analytics Topic:

```
Disambiguation:
- "sales", "revenue", "orders" -> use SALES_FACT
- "returns", "refunds" -> use RETURNS_FACT
- "net sales", "net revenue" -> join SALES_FACT LEFT JOIN RETURNS_FACT on order_line_id

Cross-dataset metrics:
- Net Revenue = SUM(SALES_FACT.total_amount) - SUM(RETURNS_FACT.refund_amount)
- Return Rate = COUNT(RETURNS_FACT.return_id) / COUNT(SALES_FACT.order_line_id)

Default joins:
- SALES_FACT LEFT JOIN CUSTOMER_DIM on customer_id
- SALES_FACT LEFT JOIN PRODUCT_DIM on product_id

Date handling:
- Fiscal year starts April 1. Interpret "this year" using fiscal year boundaries.
- YTD: current fiscal year up to and including today.
```

## Best practices for custom instructions
<a name="topics-custom-instructions-best-practices"></a>
+ Keep instructions concise. Prefer bullet-point rule lists over prose paragraphs.
+ Use topic-level instructions for cross-dataset logic only. Single-dataset semantics (grain, keys, aggregation rules) belong in the dataset's own enrichment metadata.
+ Avoid contradictions between dataset-level and topic-level instructions.
+ Test your instructions by asking questions in chat and reviewing the generated SQL in the Explanation panel.