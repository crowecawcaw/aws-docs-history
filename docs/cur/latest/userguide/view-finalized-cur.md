# Viewing your finalized report

After issuing your invoice at the end of the month, AWS finalizes your report’s usage
charges. To determine if a line item on your report is final, review the
**bill/InvoiceId** column. If the line item is final, then the
**bill/InvoiceId** column is populated with an AWS invoice ID. If the
line item is not yet final, then the **bill/InvoiceId** column is
blank.

To determine if your entire report is finalized, review the
**bill/InvoiceId** column. If the report is final, then the
**bill/InvoiceId** column is populated with invoice ID values. If the
report is not yet final, then the **bill/InvoiceId** column is blank.

###### Note

After your report is finalized, AWS might update the report if AWS applies refunds,
credits, or support fees to your usage for the month. Because Developer, Business, and
Enterprise Support are calculated based on final usage charges, those are reflected on the
sixth or seventh of the month for the prior month’s report. AWS applies credits or refunds
based on the terms of your agreement or contract with AWS.
