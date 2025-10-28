# Invoice and Receipt Response Objects

When you submit an invoice or a receipt to the AnalyzeExpense API, it returns a
series of ExpenseDocuments objects. Each ExpenseDocument is further separated into
`LineItemGroups` and `SummaryFields`. Most invoices and
receipts contain information such as the vendor name, receipt number, receipt date,
or total amount. AnalyzeExpense returns this information under
`SummaryFields`. Receipts and invoices also contain details about the
items purchased. The AnalyzeExpense API returns this information under
`LineItemGroups`. The `ExpenseIndex` field uniquely
identifies the expense, and associates the appropriate `SummaryFields`
and `LineItemGroups` detected in that expense. Finally, expense analysis
will return a `Block` object, giving you the same information as text
detection would on your document.

Certain information, such as addresses and names, can be difficult to discern
between based on a single response. Expense Analysis uses the object
`ExpenseGroupProperties` to help distinguish nebulous responses. This
object contains a type from the following list:

- VENDOR_REMIT_TO
- RECEIVER_SHIP_TO
- RECEIVER_SOLD_TO
- RECEIVER_BILL_TO
- VENDOR_SUPPLIER
  These types distinguish between the different groups of responses. Multiple
  elements belonging to the same group are connected via identification number, also
  returned in `ExpenseGroupProperties`.

The most granular level of data in the AnalyzeExpense response consists of
`Type`, `ValueDetection`, and `LabelDetection`
(Optional). The individual entities are:

- [Type](#how-it-works-type "#how-it-works-type"):
  Refers to what kind of information is detected on a high level.
- [LabelDetection](#how-it-works-labeldetection "#how-it-works-labeldetection"): Refers to the label of an
  associated value within the text of the document.
  `LabelDetection` is optional and only returned if the label
  is written.
- [ValueDetection](#how-it-works-valuedetection "#how-it-works-valuedetection"): Refers to the value of
  the label or type returned.
  The AnalyzeExpense API also detects `ITEM`, `QUANTITY`, and
  `PRICE` within line items as normalized fields. If there is other
  text in a line item on the receipt image such as SKU or detailed description, it
  will be included in the JSON as `EXPENSE_ROW`. This is shown in the
  following example:

```

               {
                                    "Type": {
                                        "Text": "EXPENSE_ROW",
                                        "Confidence": 99.95216369628906
                                    },
                                    "ValueDetection": {
                                        "Text": "Banana 5 $2.5",
                                        "Geometry": {
                                          …
                                        },
                                        "Confidence": 98.11214447021484
                                    }

```

The preceding example shows how the AnalyzeExpense API operation returns the
entire row on a receipt that contains line item information about 5 bananas sold for
$2.5.

## Type

Following is an example of the standard or normalized type of the key-value
pair:

```

               {
                    "PageNumber": 1,
                    "Type": {
                        "Text": "VENDOR_NAME",
                        "Confidence": 70.0
                    },
                    "ValueDetection": {
                        "Geometry": { ... },
                        "Text": "AMAZON",
                        "Confidence": 87.89806365966797
                    }
                }

```

The receipt did not have “Vendor Name” explicitly listed. However, the Analyze
Expense API recognized the value "AMAZON" as Type `VENDOR_NAME`.

## LabelDetection

Following is an example of text as it is shown on a customer document
page:

```

               {
                    "PageNumber": 1,
                    "Type": {
                        "Text": "OTHER",
                        "Confidence": 70.0
                    },
                    "LabelDetection": {
                        "Geometry": { ... },
                        "Text": "CASHIER",
                        "Confidence": 88.19171142578125
                    },
                    "ValueDetection": {
                        "Geometry": { ... },
                        "Text": "Mina",
                        "Confidence": 87.89806365966797
                    }
                }

```

The example document contained “CASHIER Mina.” The Analyze Expense API
extracted the as-is value and returns it under `LabelDetection`. For
implied values such as “Invoice Date,” where the “key” is not explicitly shown
in the receipt, `LabelDetection` will not be included in the
AnalyzeExpense element. In such cases, the AnalyzeExpense API operation does not
return `LabelDetection`.

## ValueDetection

The following is an example that shows the “value” of the key-value
pair.

```

               {
                    "PageNumber": 1,
                    "Type": {
                        "Text": "OTHER",
                        "Confidence": 70.0
                    },
                    "LabelDetection": {
                        "Geometry": { ... },
                        "Text": "CASHIER",
                        "Confidence": 88.19171142578125
                    },
                    "ValueDetection": {
                        "Geometry": { ... },
                        "Text": "Mina",
                        "Confidence": 87.89806365966797
                    }
                }

```

In the example, the document contained “CASHIER Mina”. The AnalyzeExpense API
detected the Cashier value as Mina and returned it under
`ValueDetection`.
