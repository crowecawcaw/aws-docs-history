

# Confidence score best practice

When you process a document with a blueprint, every extracted field in the custom output comes with a **confidence score**. The score is a number between 0 and 1 that estimates how likely the extracted value is to be correct. Use it to decide which values to accept automatically and which ones to route for manual review.

Confidence scores are estimates, not guarantees. A high score does not prove that a value is correct, and a low score does not prove that it is wrong.

## Where confidence appears in the response
<a name="insights-confidence-bp-where"></a>

The custom output result (see [Custom extraction with blueprints](insights-custom-extraction.md)) has two parts that mirror each other:
+ `inference_result` holds the extracted values, shaped like your blueprint.
+ `explainability_info` holds the same fields, in the same structure, with a confidence score and the location of each value on the page.

For example, an invoice blueprint returns the vendor name and a checkbox like this:

```json
{
  "inference_result": {
    "vendor": {
      "vendor_name": "AnyCompany Office Supplies, Inc."
    },
    "paid_in_full_checkbox": false
  },
  "explainability_info": [
    {
      "vendor": {
        "vendor_name": {
          "value": "AnyCompany Office Supplies, Inc.",
          "type": "string",
          "success": true,
          "confidence": 0.98,
          "geometry": [
            {
              "page": 1,
              "boundingBox": { "left": 0.0467, "top": 0.0620,
                               "width": 0.4300, "height": 0.0400 }
            }
          ]
        }
      },
      "paid_in_full_checkbox": {
        "value": false,
        "type": "boolean",
        "success": true,
        "confidence": 0.56,
        "geometry": [ "..." ]
      }
    }
  ]
}
```

Every leaf field, meaning every value of type string, number, or boolean, has its own confidence. To find it, follow the same path in `explainability_info` that you used in `inference_result`, including list indexes. Lists and custom types have no score of their own; only the leaf values inside them do.


| **Field** | **Description** | 
| --- | --- | 
| `value` | The extracted value. Same as the value in `inference_result`. | 
| `type` | The blueprint type of the field: string, number, or boolean. | 
| `confidence` | The confidence score for this field, from 0 to 1. | 
| `geometry` | Where the value was found. Each entry has a page number (starting at 1) and a `boundingBox` whose `left`, `top`, `width`, and `height` are fractions of the page width and height. A field can have more than one entry when the same value appears in several places, for example on each copy of a multi-copy form. | 
| `success` | Whether extraction completed for this field. | 

The response also contains `matched_blueprint.confidence`. That score describes how well the document matched the blueprint. It is separate from the field-level scores and does not tell you anything about individual values.

## What the score means
<a name="insights-confidence-bp-meaning"></a>

The confidence score is **per field**. It answers one question: how sure is the model that this specific value, inferred from this document, is correct?
+ It is **not** a document-level score.
+ It is **not** a probability you can rely on exactly. A field scored 0.80 is not guaranteed to be right 80% of the time. Treat the score as a ranking signal: higher scores are more likely to be correct than lower scores.
+ It is computed for the value that was returned.

## When confidence is high and when it is low
<a name="insights-confidence-bp-high-low"></a>

The following figure shows a sample invoice processed with the blueprint in this section. It outlines the high-confidence typed fields near the top and the low-confidence handwritten and checkbox fields near the bottom. The walkthrough table later in this section lists each field, its score, and why it scored as it did, so you do not need the figure to follow the example.

![A sample vendor invoice with high-confidence typed fields outlined near the top and low-confidence handwritten and checkbox fields outlined near the bottom.](https://docs.aws.amazon.com/textract/latest/dg/images/insights-confidence-annotated-invoice.png)


The invoice was processed with this blueprint:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "description": "A vendor invoice with payment status and a signed receipt section",
  "class": "Invoice",
  "type": "object",
  "properties": {
    "vendor_name": {
      "type": "string",
      "inferenceType": "explicit",
      "description": "The name of the company that issued the invoice, printed at the top of the page"
    },
    "invoice_number": {
      "type": "string",
      "inferenceType": "explicit",
      "description": "The value under the Invoice number label, exactly as printed"
    },
    "invoice_date": {
      "type": "string",
      "inferenceType": "explicit",
      "description": "The value under the Invoice date label, exactly as printed"
    },
    "due_date": {
      "type": "string",
      "inferenceType": "explicit",
      "description": "The value under the Due date label, exactly as printed"
    },
    "invoice_date_iso": {
      "type": "string",
      "inferenceType": "explicit",
      "description": "The value under the Invoice date label, in YYYY-MM-DD format"
    },
    "payment_terms_days": {
      "type": "number",
      "inferenceType": "inferred",
      "description": "The number of days from the invoice date to the due date"
    },
    "customer_name": {
      "type": "string",
      "inferenceType": "explicit",
      "description": "The company name on the first line under the Bill to label"
    },
    "customer_address": {
      "type": "string",
      "inferenceType": "explicit",
      "description": "The street address, city, state, and ZIP code under the Bill to label, on one line"
    },
    "customer_email": {
      "type": "string",
      "inferenceType": "explicit",
      "description": "The email address under the Contact email label"
    },
    "total_due": {
      "type": "number",
      "inferenceType": "explicit",
      "description": "The amount next to the Total due label, without a currency symbol"
    },
    "paid_in_full": {
      "type": "boolean",
      "inferenceType": "explicit",
      "description": "Is the Paid in full checkbox under Payment status marked?"
    },
    "partially_paid": {
      "type": "boolean",
      "inferenceType": "explicit",
      "description": "Is the Partially paid checkbox under Payment status marked?"
    },
    "received_by": {
      "type": "string",
      "inferenceType": "explicit",
      "description": "The name written by hand under the Received by (print name) label"
    },
    "date_received": {
      "type": "string",
      "inferenceType": "explicit",
      "description": "The date written by hand under the Date received label, exactly as written"
    }
  }
}
```

The following example shows the response for this invoice. All monetary amounts in this example are in US dollars (USD).

```json
{
  "inference_result": {
    "vendor_name": "AnyCompany Office Supplies, Inc.",
    "invoice_number": "INV-2026-0418",
    "invoice_date": "03/14/2026",
    "due_date": "04/13/2026",
    "invoice_date_iso": "2026-03-14",
    "payment_terms_days": 30,
    "customer_name": "Example Corp.",
    "customer_address": "456 Main Avenue, Sampleville, OR 97201",
    "customer_email": "pat.illingworth@example.com",
    "total_due": 432.50,
    "paid_in_full": false,
    "partially_paid": false,
    "received_by": "Jordan Rivera",
    "date_received": "3/18/26"
  },
  "explainability_info": [
    {
      "vendor_name": {
        "value": "AnyCompany Office Supplies, Inc.", "type": "string", "success": true, "confidence": 0.98,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.0467, "top": 0.0971, "width": 0.4280, "height": 0.0485 } } ]
      },
      "invoice_number": {
        "value": "INV-2026-0418", "type": "string", "success": true, "confidence": 0.97,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.0467, "top": 0.3015, "width": 0.1253, "height": 0.0265 } } ]
      },
      "invoice_date": {
        "value": "03/14/2026", "type": "string", "success": true, "confidence": 0.97,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.2800, "top": 0.3015, "width": 0.0920, "height": 0.0294 } } ]
      },
      "due_date": {
        "value": "04/13/2026", "type": "string", "success": true, "confidence": 0.96,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.4800, "top": 0.3015, "width": 0.0920, "height": 0.0294 } } ]
      },
      "invoice_date_iso": {
        "value": "2026-03-14", "type": "string", "success": true, "confidence": 0.93,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.2800, "top": 0.3015, "width": 0.0920, "height": 0.0294 } } ]
      },
      "payment_terms_days": {
        "value": 30, "type": "number", "success": true, "confidence": 0.88,
        "geometry": [
          { "page": 1, "boundingBox": { "left": 0.2800, "top": 0.3015, "width": 0.0920, "height": 0.0294 } },
          { "page": 1, "boundingBox": { "left": 0.4800, "top": 0.3015, "width": 0.0920, "height": 0.0294 } }
        ]
      },
      "customer_name": {
        "value": "Example Corp.", "type": "string", "success": true, "confidence": 0.97,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.0467, "top": 0.4412, "width": 0.1173, "height": 0.0338 } } ]
      },
      "customer_address": {
        "value": "456 Main Avenue, Sampleville, OR 97201", "type": "string", "success": true, "confidence": 0.95,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.0467, "top": 0.4926, "width": 0.3313, "height": 0.0338 } } ]
      },
      "customer_email": {
        "value": "pat.illingworth@example.com", "type": "string", "success": true, "confidence": 0.96,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.4800, "top": 0.4412, "width": 0.2600, "height": 0.0338 } } ]
      },
      "total_due": {
        "value": 432.50, "type": "number", "success": true, "confidence": 0.97,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.8333, "top": 0.6147, "width": 0.0720, "height": 0.0294 } } ]
      },
      "paid_in_full": {
        "value": false, "type": "boolean", "success": true, "confidence": 0.56,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.0440, "top": 0.6559, "width": 0.1052, "height": 0.0500 } } ]
      },
      "partially_paid": {
        "value": false, "type": "boolean", "success": true, "confidence": 0.63,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.2773, "top": 0.6559, "width": 0.1245, "height": 0.0500 } } ]
      },
      "received_by": {
        "value": "Jordan Rivera", "type": "string", "success": true, "confidence": 0.61,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.0499, "top": 0.8643, "width": 0.1983, "height": 0.0746 } } ]
      },
      "date_received": {
        "value": "3/18/26", "type": "string", "success": true, "confidence": 0.66,
        "geometry": [ { "page": 1, "boundingBox": { "left": 0.4793, "top": 0.8607, "width": 0.1120, "height": 0.0798 } } ]
      }
    }
  ]
}
```

Read each score together with the blueprint field it belongs to. The score is for the field as a whole: the field's description, what the document shows for it, and the value that was returned.


| **Fields** | **Score** | **What the blueprint asks for, and what the document shows** | 
| --- | --- | --- | 
| `vendor_name`, `invoice_number`, `invoice_date`, `due_date`, `customer_name`, `customer_address`, `customer_email`, `total_due` | 0.95 to 0.98 | Explicit fields. Each description points to one value next to a matching label. The value is printed, and the returned value is that text as the description asks for it. | 
| `invoice_date_iso`, `payment_terms_days` | 0.93, 0.88 | Derived values. The value is not printed on the page as returned. `invoice_date_iso` is an explicit field that returns the printed invoice date in a different format, and `payment_terms_days` is an inferred field calculated from the invoice date and the due date. The score covers both reading the source values and deriving the result. The geometry of a derived value points to the source values it was derived from, so `payment_terms_days` has two entries. These fields are not outlined in the figure. | 
| `received_by`, `date_received` | 0.61, 0.66 | The descriptions are just as specific, but the values are written by hand in pencil. | 
| `paid_in_full`, `partially_paid` | 0.56, 0.63 | Each description asks whether a box is marked. The Paid in full box holds only a faint partial stroke, so the page does not clearly show whether it is marked. | 

### Common causes of low confidence
<a name="insights-confidence-bp-causes"></a>

Confidence is commonly low in these cases:
+ **Checkboxes and other selection marks.** Marks that are faint, partial, outside the box, or crossed out.
+ **Poor image quality.** Blur, low resolution, skew, stamps, or handwriting over printed text.
+ **Overlapping or crowded layout.** Text that runs into a neighboring cell or label.
+ **Ambiguous field definitions.** A blueprint field whose name and description could match more than one value on the page.

## Getting more reliable confidence scores
<a name="insights-confidence-bp-reliable"></a>

You can make confidence scores more useful by improving the inputs they are computed from:
+ **Review image quality.** Use the original digital file when you have one. For scans and photos, check that text is sharp and the page is straight, and that stamps, shadows, or folds do not cover the fields you extract.
+ **Remove ambiguity from the blueprint.** Each field should match exactly one value in the document. When a document has similar values, such as two addresses or several dates, give each field a name and description that tell them apart. For example, `customer_address` asks for "the address under the Bill to label", not just "address".
+ **Write detailed descriptions.** Say where the value is (the label or section it appears under), what it looks like, and the format you want back. A detailed description helps the model find the right value and return it in the form you expect.

## Choosing a confidence threshold
<a name="insights-confidence-bp-threshold"></a>

A common way to use confidence scores is to set a threshold. Values that score at or above the threshold are accepted automatically, and values that score below it are sent for manual review.

The threshold is a trade-off between review cost and missed errors:
+ **A higher threshold** sends more values to review. Fewer errors are accepted without review, but review cost goes up.
+ **A lower threshold** sends fewer values to review. Review cost goes down, but more errors are accepted without review.

A threshold does not sort values into right and wrong. Some values below it are correct and are reviewed anyway, and some values above it might still be wrong. Tuning the threshold on your own data tells you how many of each to expect.

There is no single threshold that works for every customer. The right value depends on your documents, your blueprint, and how costly an undetected error is compared with a review. Tune the threshold on your own data:
+ Process a representative sample of your documents.
+ Have a person check the extracted values and record which ones are correct.
+ For several candidate thresholds, count how many values would be sent to review and how many errors would be accepted automatically.
+ Choose the threshold that gives a balance that meets your requirements.
+ Re-check the threshold when you change your blueprint or start processing a new type of document.

A single threshold for all fields is a reasonable starting point. If some fields consistently score lower than others, or some fields are more costly to get wrong, setting a separate threshold for those fields can help. For example, if a checkbox field in your documents scores lower than your typed fields, a separate threshold for that field keeps it from sending more values to review than you need, without lowering the threshold for every other field.