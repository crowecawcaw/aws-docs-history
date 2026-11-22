

# Blueprint schema best practice

A blueprint schema lists the values to extract from one type of document. This section explains how a blueprint is structured and the practices that make it extract values reliably across every document of the type.

## What is a blueprint
<a name="insights-blueprint-schema-bp-what"></a>

A blueprint is a JSON schema that lists all the values you want to extract from one type of document. At the top level it has:
+ **class** – The name of the document type, for example `Invoice`.
+ **description** – One sentence on what documents of this type are.
+ **properties** – The fields to extract, one entry per field, keyed by the field name.
+ **$defs** – Custom types, groups of fields used by the fields above (see the following).

For each field it gives:
+ a **name**: its key under `properties`, which is also the key of the value in the output.
+ a **type**: string, number, boolean, or array (with items), or a `$ref` to a **custom type** (a group of fields defined under `$defs`, for example an address or the columns of one table row — a table is an array whose items is a `$ref` to a custom type).
+ a **description**: the extraction instruction — what the value is, where it is on the document, and in what format to return it.
+ **inferenceType**: explicit for values that appear directly in the document, inferred for values inferred from it, for example "is the document signed" or "provide the total of the expense column".
+ **enum** (optional): the fixed list of values a field can return, for example `"enum": ["M", "F", "X"]`.

**A blueprint describes a document type, not one document.** The same blueprint is applied to every document of the type, so names and descriptions must hold for all of them. Describe where a value is and what it looks like, never the value on your sample: not "the customer, for example Acme Corp" but "the customer named in the 'Bill To' block". When you need a format, describe it in words ("keeping capital letters", "only 'Copy' and its letter") or give an invented example ("for example '14:05'"). Labels and headings printed on every document of the type are fine to quote: they are part of the form.

### The parts of a field
<a name="insights-blueprint-schema-bp-parts"></a>


| **Part** | **What it does** | **Examples** | 
| --- | --- | --- | 
| `name` | The field's key under `properties`; also the key of the value in the output. | `transaction_date`, `employer_name`, `invoice_total`, `is_signed` | 
| `type` | The kind of value returned: string, number, boolean, array (with items), or a `$ref` to a custom type. | `"type": "string"`; `"type": "array", "items": {"type": "string"}`; `"$ref": "#/$defs/Address"`; `"type": "array", "items": {"$ref": "#/$defs/LineItem"}` | 
| `inferenceType` | `explicit` if the value is read from the document, `inferred` if it is inferred from it. | `explicit` for a printed date; `inferred` for "is the document signed" | 
| `enum` | Optional. The only values the field can return, when the set is closed. Goes next to `"type": "string"`; for a list of values, inside `items`. | `"enum": ["M", "F", "X"]`; `"enum": ["Cash", "Credit Card", "Debit Card", "Check", "Other"]` | 
| `description` | The extraction instruction: what the value is, where it is, its format, and what to leave out. | "Date after 'Invoice Date'. Format YYYY-MM-DD.", "Value in Box 2, without '$'.", "License class as printed, for example 'D' or 'DV'." | 

## A minimal example
<a name="insights-blueprint-schema-bp-minimal"></a>

An invoice, with regular fields, a custom type, and a table (the example at the end of this page shows a fuller invoice blueprint):

![A sample commercial invoice showing the header, the SOLD BY and BILL TO blocks, a line-item table, and a totals block.](https://docs.aws.amazon.com/textract/latest/dg/images/insights-blueprint-example-invoice.png)


```json
{
  "class": "Invoice",
  "description": "A commercial invoice from a seller to a buyer.",
  "type": "object",
  "properties": {
    "invoice_number": {"type": "string", "inferenceType": "explicit",
      "description": "Value under 'INVOICE NUMBER', exactly as printed."},
    "invoice_date": {"type": "string", "inferenceType": "explicit",
      "description": "Value under 'DATE'. Format YYYY-MM-DD."},
    "seller": {"$ref": "#/$defs/Party",
      "description": "The party under 'SOLD BY', not the brand in the logo."},
    "bill_to": {"$ref": "#/$defs/Party",
      "description": "The party under 'BILL TO'."},
    "line_items": {"type": "array", "items": {"$ref": "#/$defs/LineItem"},
      "description": "One entry per product row. Exclude the totals below."},
    "total": {"type": "number", "inferenceType": "explicit",
      "description": "Amount on the 'Total' line. Number without currency symbol or thousands separators."},
    "is_paid": {"type": "boolean", "inferenceType": "inferred",
      "description": "True if the invoice shows how it was paid."}
  },
  "$defs": {
    "Party": {
      "type": "object",
      "properties": {
        "name": {"type": "string", "inferenceType": "explicit",
          "description": "Company name, the first line of the block."},
        "city": {"type": "string", "inferenceType": "explicit",
          "description": "City of the address."},
        "phone": {"type": "string", "inferenceType": "explicit",
          "description": "Phone number exactly as printed."}
      }
    },
    "LineItem": {
      "type": "object",
      "properties": {
        "product_name": {"type": "string", "inferenceType": "explicit",
          "description": "PRODUCT column, without the 'Country of origin' line."},
        "quantity": {"type": "number", "inferenceType": "explicit",
          "description": "UNITS column."},
        "line_total": {"type": "number", "inferenceType": "explicit",
          "description": "TOTAL column. Number without currency symbol or thousands separators."}
      }
    }
  }
}
```

Expected output:

```json
{
  "invoice_number": "F1000869/27",
  "invoice_date": "2022-03-14",
  "seller": {"name": "NORTHWIND LIFT PARTS", "city": "Kent",
             "phone": "(253) 555-0148"},
  "bill_to": {"name": "CASCADE ACCESS SYSTEMS", "city": "Towson",
              "phone": "(410) 555-0192"},
  "line_items": [
    {"product_name": "Timing Belts", "quantity": 1, "line_total": 19.80},
    {"product_name": "Bracket Assembly", "quantity": 1, "line_total": 21.50},
    {"product_name": "Timing Pulleys", "quantity": 1, "line_total": 39.45}
  ],
  "total": 147.71,
  "is_paid": true
}
```

### Regular fields, custom types and tables
<a name="insights-blueprint-schema-bp-regular"></a>

The example combines the different kinds of field:
+ **Regular fields** (`invoice_number`, `invoice_date`, `total`, `is_paid`) have a basic type and return one value.
+ **A custom type** (`Party`) is a group of fields defined once under `$defs` and used by a field with `"$ref": "#/$defs/Party"`. Here it is used twice, for `seller` and `bill_to`; each returns an object with the same keys.
+ **A table** is an array whose items is a `$ref` to a custom type. The custom type (`LineItem`) describes **one row**: its fields are the columns, with explicit names (`product_name`, `quantity`, `line_total`). The table field (`line_items`, `"type": "array", "items": {"$ref": "#/$defs/LineItem"}`) returns one object per row, however many rows the document has.
+ The description of the table field says which rows to include and which to leave out (headers, subtotals, totals); the descriptions of the row's fields say which column each value comes from.
+ Group and table fields carry no `inferenceType` (a `$ref` field has only `$ref` and `description`); the fields inside the custom type carry it.

## Documents in other languages
<a name="insights-blueprint-schema-bp-languages"></a>

Blueprints work the same way for documents in any supported language (for more information, see [Supported languages](supported-languages.md)):
+ **Field names** are the keys of the output: write them in the language you want the keys in (`numero_factura` or `invoice_number`).
+ **Descriptions** can be in English or in the document's language. Either way, quote the document's labels as printed, in its language: "Valor bajo 'Total Factura'".

## How to create a blueprint
<a name="insights-blueprint-schema-bp-create"></a>

To create a blueprint, follow these steps:
+ **Check for a public blueprint** for the document type, and use or copy it if one fits (see the following section on starting from a public blueprint).
+ **Collect a few sample documents** of the type, including unusual ones (other layouts, empty fields, handwriting).
+ **List the values you need**, and only those: try to avoid adding fields that are not present in the document, as these can increase computation time.
+ **Name each field** clearly and explicitly.
+ **Choose the type** of each field; group related fields into custom types under `$defs` and define one custom type per table row.
+ **Write each description**: where the value is, its format, what to exclude, the empty-value rule.
+ **Set each field's `inferenceType`** to explicit if the value is printed on the document, or inferred if it is worked out from it. For an inferred field, the description says how to work it out: "True if subtotal \+ tax equals the total".
+ **Test on the samples** and refine the descriptions where the output is wrong or could be read two ways.

### Do's and don'ts
<a name="insights-blueprint-schema-bp-dos-donts"></a>


| **Area** | **Do** | **Don't** | 
| --- | --- | --- | 
| Names | Use clear, explicit names: `employer_name`, `transaction_date`. | Use vague names: `name`, `date`, `amount2`. | 
| Names | Name fields the way the document's readers would: `employer_name` or Employer name both work. | Use `/` in a name, or names that differ only by case: `currency` and `Currency`. | 
| Fields | Add only fields that appear on the document type. | Add fields that are never on the document. | 
| Fields | Keep one field per value. | Repeat a field under another name: `currency` and `Currency`. | 
| Template | Describe where the value is and what it looks like: "the customer in the 'Bill To' block". | Copy a value from your sample document: "for example 'Acme Corp'", "for example 'INV-2024-0042'". | 
| Descriptions | Add where the value is, its format, or how to tell it apart: "City of the seller's address". | Restate the name: `city`: "City." | 
| Location | Say where the value is: "Box 2", "under SOLD BY". | Leave it open when several values fit. | 
| Location | Anchor on a label or section: "after 'Invoice Date'". | Anchor on a page or position: "page 2", "top left". | 
| Location | Say which copy to use when content repeats. | Assume the right copy is picked. | 
| Format | Give the format, with an example: "YYYY-MM-DD". | Leave dates, amounts, and percentages unspecified. | 
| Format | Write "a number without currency symbol". | Mix "$1,234.00" and "1234" across documents. | 
| Types | Use string for IDs, even all-digit ones. | Use number for IDs: "004219" loses its zeros. | 
| Types | Use boolean for checkboxes. | Return "X" or "checked" as text. | 
| Types | When only one box of a group can be checked, use one string field with an enum of the options: `"enum": ["C Corporation", "S Corporation", "Partnership"]`. | Add a true/false field for each box: `is_c_corp`, `is_s_corp`, and so on. | 
| Tables | Describe the row once as a custom type under `$defs` (`LineItem`: name, quantity, price) and make the table an array of it: `"line_items": {"type": "array", "items": {"$ref": "#/$defs/LineItem"}}`. | Add a field per row and column: `item_1_name`, `item_1_price`, `item_2_name`, and so on. | 
| Tables | Exclude header, subtotal, and total rows. | Leave totals inside the row list. | 
| Empty values | Say what to return: "empty string if blank". | Leave '', null, 0 and "N/A" to chance. | 
| Inferred | Give the rule: "True if subtotal \+ tax equals the total". | Ask "is it valid?" with no rule. | 
| Inferred | Name the reference: "before today's date". | Rely on facts that are not on the document. | 
| Value lists | Put the valid values in enum when the set is closed: `"enum": ["M", "F", "X"]`. | Leave the labels open: the result might be "Brown", "brown eyes", or "BR". | 
| Value lists | Use enum only if every document uses one of its values, for example sex. Otherwise give examples in the description: "License class as printed, for example 'D' or 'DV'". | Use an enum that some documents break, for example `"enum": ["A", "B", "C"]` for license class when cards also show D or DV. | 
| Spelling | Say "exactly as printed" or "corrected". | Leave open whether typos are fixed. | 
| Testing | Try the blueprint on a few real documents. | Run it at scale untested. | 

The sections that follow go into each point in detail; the example at the end of this page then shows a complete blueprint.

## Limits and structure rules
<a name="insights-blueprint-schema-bp-limits"></a>


| **Limit** | **Maximum** | 
| --- | --- | 
| Leaf fields per blueprint (every string, number, or boolean value, including those inside custom types and tables) | 100 | 
| List leaf fields (columns of all tables plus lists of values, combined; they also count toward the 100) | 30 | 
| Field and custom type name length (no `/`) | 60 characters | 
| Description length (each field, and the root description) | 600 characters | 
| Class length | 60 characters | 
| Enum values per field | 20 values, each 1-60 characters, no `/` | 

The following structure rules also apply:
+ **One level of nesting.** A custom type's fields are string, number, boolean, or a list of values: no custom type (and so no table) inside another custom type. Flatten instead (street and city directly in `Party`, not an `Address` inside `Party`).
+ **No lists inside a table row** – A custom type used as a table row cannot contain an array. A list of values inside a group used with `$ref` is allowed (for example `tax_amounts` inside a payment group).
+ **No lists of lists** – An array whose items is another array.
+ **A `$ref` field has only `$ref` and `description`** – No type, inferenceType, enum, or items next to the `$ref`, in a field or in the items of a table.
+ **No `inferenceType` on a table or a custom type** – A table field (`"type": "array"` with items `$ref`) and a custom type under `$defs` carry no inferenceType; the fields inside the custom type carry it.
+ **enum on a list goes inside items** – `"type": "array", "items": {"type": "string", "enum": [...]}`, not enum next to `"type": "array"`.
+ **Custom type names are not type names** – String, number, integer, int, float, boolean, bool, and enum cannot be used as custom type names.

## Best practices in detail
<a name="insights-blueprint-schema-bp-detail"></a>

### 0. Start from a public blueprint when one fits
<a name="insights-blueprint-schema-bp-detail-0"></a>

AWS provides public blueprints for common document types such as invoices, receipts, payslips, bank checks, W-2, W-9, 1040, 1099 forms, driver's licenses, and insurance cards. See the list in [Custom extraction with blueprints](insights-custom-extraction.md).
+ **Use it as is** when its fields cover what you need: reference its ARN in the project or the job.
+ **Copy and modify it** when it is close but not complete. Public blueprints cannot be edited, so start a custom blueprint from its schema: add the fields you need, remove the ones you don't, and rewrite the descriptions using the practices below.
+ **Write your own** when no public blueprint is close.

A public blueprint is written for the document type in general. For example, public-invoice returns the vendor address as one string and has no fields for tracking number, payment method, shipping charges, or incoterms; the example adds them.

### 1. Say which value
<a name="insights-blueprint-schema-bp-detail-1"></a>

A description that fits more than one value on the page gives unpredictable results: which party, which column, which copy, which date.
+ Point to where the value is, using the document's own labels: "the company under 'SOLD BY'", "Box 2", "the 'Current' column, not 'YTD'".
+ Don't just restate the name: `city`: "City." adds nothing. Using the same word is fine when the description adds where the value is, its format, or how to tell it apart: "City of the seller's address, without state or ZIP". One or two sentences anchored on the document's labels are enough; a longer description without that does not help.
+ Anchor on labels, headings and sections, not on page numbers or positions ("page 2", "top left"): layouts differ between issuers and versions, and a value that is elsewhere on another document can come back empty. Write "in the 'Payment Summary' section" or "after 'Invoice Date'" instead. Name a page or position only when the layout is fixed, as on a standard form.
+ When the same content appears more than once (form copies, duplicated stubs), say which one to use: "use the first (top) copy".
+ Name the role, not just the thing: "Employer's name (not the employee's)", rather than "name".


| **Instead of** | **Write** | 
| --- | --- | 
| Name (the form has an employer and an employee) | Employer's name, first line of the employer block (not the employee's name) | 
| Value (the form has Present and Proposed columns) | Value in the 'Proposed' column of line 3 | 
| Vendor name (the logo and SOLD BY differ) | Company name under 'SOLD BY'. Use this block, not the brand in the logo. | 

### 2. State the output format for every non-trivial field
<a name="insights-blueprint-schema-bp-detail-2"></a>

Without a format, the same value can come back in several forms (03/14/2022, 2022-03-14, March 14, 2022).
+ **Dates:** one format everywhere, for example YYYY-MM-DD. If you need the date as printed, say "exactly as written".
+ **Amounts:** "a number without currency symbol or thousands separators", for example `total: 147.71`, not "$147.71". If you need the currency, add a separate field for it, for example `currency: "USD"`.
+ **Percentages:** "9.5 for '9.5 %'" or "0.095" — pick one and give an example.
+ **Identifiers** (SSN, EIN, phone, routing numbers): either "exactly as printed" or a pattern such as NNN-NN-NNNN.
+ **Times, heights, codes:** give an example ('09:48', '5'-08"', 'BRN').
+ **Names and addresses:** split into fields, or say how to join ("on one line, as printed"). Keep the document's own punctuation; added commas make the value differ from the page.


| **Instead of** | **Write** | 
| --- | --- | 
| Hour of death | Hour of death exactly as written, for example '2:45 P. M.' | 
| Height | Height exactly as printed, for example '6'-01"' | 
| Tax rate | Tax rate as the printed percentage, for example 9.5 for '9.5 %' (not 0.095) | 

### 3. Pick the right type
<a name="insights-blueprint-schema-bp-detail-3"></a>

Match each field to the type that fits its values:
+ **Identifiers are strings**, even when they are all digits: account, check, group, member, tracking, and routing numbers, ZIP codes. As numbers they lose leading zeros (004219 to 4219) and long ones lose digits.
+ **number** for amounts, quantities, rates, and hours.
+ **boolean** for checkboxes and yes/no facts, for example `retirement_plan`: "True if the 'Retirement plan' box in Box 13 is checked." For a question with a Yes box and a No box, say which one means true, for example `foreign_trust`: "Line 8: true if 'Yes' is checked, false if 'No' is checked." Otherwise a check mark in the No box can come back as true.
+ **A list of strings** (`"type": "array", "items": {"type": "string"}`) for repeated simple values (countries, restriction codes) instead of a joined string.
+ **One string field with an enum** for a group of checkboxes where only one can be checked, for example on a W-9 the field `federal_tax_classification` with `"enum": ["Individual or sole proprietor", "C Corporation", "S Corporation", "Partnership", "Trust or estate", "LLC", "Other", "None"]` and the description "Line 3: the checked box; 'None' if no box is checked." returns "S Corporation". This gives one answer instead of a true/false field per box.
+ **Custom types** (under `$defs`, used with `$ref`) for groups that belong together (an address, a party, pharmacy IDs) and for every table row.

### 4. Tables: one custom type per row, plus include/exclude rules
<a name="insights-blueprint-schema-bp-detail-4"></a>

Follow these practices for each table:
+ Define the row as a custom type and the table as a list of it.
+ Say what is **excluded**: header rows, section headings, subtotal or total rows, empty slots.
+ Keep totals as separate fields, so they are not mixed into the rows.
+ Say the order ("in document order", "top to bottom").
+ Prefer one table per printed table. Splitting one printed table into several by meaning (federal, state, and city taxes) means each row has to be classified; do that after extraction if you need it.
+ When a cell holds two values (product name \+ "Country of origin"), make two fields and say what each leaves out.


| **Instead of** | **Write** | 
| --- | --- | 
| Balance sheet line items | Balance sheet line items, excluding section headers and subtotal/total rows | 
| `state_row_1`, `state_row_2` | `"state_rows": {"type": "array", "items": {"$ref": "#/$defs/StateRow"}}` — "filled rows of boxes 14-16; omit a row whose boxes are all empty" | 

### 5. Say what to return when the value is missing
<a name="insights-blueprint-schema-bp-detail-5"></a>

An empty value can otherwise come back as "", null, 0, "N/A", or " ".
+ Strings: "empty string if blank or not printed". Lists: "empty list if printed as 'NONE'".
+ Say whether printed placeholders (N/A, NONE, --) are values or mean empty.
+ For checkboxes, say whether a printed text such as 'NA' next to the box counts.
+ An enum value cannot be empty, so an enum field cannot return an empty string. Add a value for the empty case, such as "None", and say when to use it.

### 6. Inferred fields: give the rule
<a name="insights-blueprint-schema-bp-detail-6"></a>

For an inferred field, give the model the rule to apply:
+ Write the rule: "True if subtotal \+ tax equals the total (within 0.01)", "ISO 4217 code of the amounts, inferred from symbols and addresses".
+ Name what a comparison is made against: "True if the expiration date is before today's date", not "Is expired".
+ A value read off the page is explicit, even when it is reformatted (for example a date); only values worked out from the page are inferred.

### 7. Don't contradict the documents
<a name="insights-blueprint-schema-bp-detail-7"></a>

An enum such as `"enum": ["A", "B", "C"]` for the license class fails on cards that show D or DV.
+ Only use enum when the list is truly closed (sex, checkbox options); otherwise give examples in the description ("for example 'D' or 'DV'").
+ Test the blueprint on a few documents of the type, including unusual ones, before using it at scale.

### 8. Keep the blueprint small and clean
<a name="insights-blueprint-schema-bp-detail-8"></a>

These practices keep a blueprint small and easy to maintain:
+ Only fields that exist on the document type. Seven address fields that repeat each other (vendor, supplier, remit-to, and so on) are harder to fill than one per party that the document actually shows.
+ No duplicate names, including case variants (`currency` and `Currency`).
+ Every custom type you define is used by some field; remove the ones nothing refers to.
+ Names are the keys of the output: snake\_case (`date_of_birth`), camelCase (`dateOfBirth`), and plain words (Date of birth) all work. Names cannot contain `/`.
+ When you update an existing blueprint, keep its naming style. If its names are already camelCase, leave them as they are: renaming a field changes the key your code reads.
+ Descriptions in sentence case; ALL CAPS adds nothing.
+ Use the document's own labels in descriptions (box numbers, line numbers, headings) — they are what the extraction looks for.
+ Give a clear class and a one-sentence root description (what the document is, who issues it). Keep guidance for a field in that field's description, not in the document description.

### 9. Transcribe or correct? Say so
<a name="insights-blueprint-schema-bp-detail-9"></a>

State in each description whether to transcribe a value or correct it:
+ "Exactly as printed (keep spelling errors)" — for example handwritten Anytwon.
+ If you want normalized values (corrected names, expanded codes such as BRN to Brown), say so in the description and in the field name.

## Example: commercial invoice
<a name="insights-blueprint-schema-bp-example"></a>

**Shows:** a commercial invoice for shipped goods, with every kind of field a blueprint can have. 15 top-level fields (2 with inferenceType = inferred), 3 custom types.

The blueprint uses every kind of field:
+ **string:** `invoice_number`, `invoice_date`, `payment_method`
+ **number:** `subtotal`, `total`, `shipping_charges`
+ **boolean:** `totals_match`
+ **enum:** `shipment.incoterms`, one of the eleven Incoterms codes, or None when no Incoterms line is printed
+ **list of values:** `tax_amounts`, one number per tax line
+ **custom type (group):** `seller` and `bill_to` both use `Party`; `shipment` uses `Shipment`
+ **table:** `line_items`, one `LineItem` per product row
+ **inferred fields:** `currency` and `totals_match`; every other field is explicit

![A sample commercial invoice showing the header, the SOLD BY and BILL TO blocks, a line-item table, and a totals block.](https://docs.aws.amazon.com/textract/latest/dg/images/insights-blueprint-example-invoice.png)


**Blueprint**

```json
{
  "class": "Invoice",
  "description": "A commercial invoice from a seller to a buyer listing the goods sold, with shipping, charges, tax and the total due.",
  "type": "object",
  "properties": {
    "invoice_number": {"type": "string", "inferenceType": "explicit",
      "description": "Value under 'INVOICE NUMBER', exactly as printed including letters and slashes."},
    "invoice_date": {"type": "string", "inferenceType": "explicit",
      "description": "Value under 'DATE'. Format YYYY-MM-DD."},
    "order_id": {"type": "string", "inferenceType": "explicit",
      "description": "Value under 'ORDER ID', exactly as printed, keeping the letter prefix and leading zeros. Empty string if not printed."},
    "seller": {"$ref": "#/$defs/Party",
      "description": "The party in the 'SOLD BY' block, not the brand in the logo."},
    "bill_to": {"$ref": "#/$defs/Party",
      "description": "The party in the 'BILL TO' block."},
    "shipment": {"$ref": "#/$defs/Shipment",
      "description": "Shipping details from the 'TRACKING NUMBER' and 'FORWARDING AGENT' boxes and the 'Incoterms:' line."},
    "line_items": {"type": "array", "items": {"$ref": "#/$defs/LineItem"},
      "description": "One entry per product row of the item table, in document order. Exclude the header row and the subtotal / charges / total rows below the table."},
    "subtotal": {"type": "number", "inferenceType": "explicit",
      "description": "Amount on the 'Sub total' line of the totals block, before shipping, insurance and tax. Number without currency symbol or thousands separators."},
    "shipping_charges": {"type": "number", "inferenceType": "explicit",
      "description": "Amount on the 'Shipping Charges' line of the totals block. Number without currency symbol or thousands separators."},
    "insurance_charges": {"type": "number", "inferenceType": "explicit",
      "description": "Amount on the 'Insurance' line of the totals block (0 if printed as USD 0.00). Number without currency symbol or thousands separators."},
    "tax_amounts": {"type": "array", "inferenceType": "explicit", "items": {"type": "number"},
      "description": "One entry per tax line of the totals block (for example 'Sales Tax'), top to bottom. Numbers without currency symbol or thousands separators. Empty list if no tax line is printed."},
    "total": {"type": "number", "inferenceType": "explicit",
      "description": "Amount on the 'Total' line of the totals block. Number without currency symbol or thousands separators."},
    "payment_method": {"type": "string", "inferenceType": "explicit",
      "description": "Value under 'PAID BY', as printed. Empty string if not printed."},
    "currency": {"type": "string", "inferenceType": "inferred",
      "description": "ISO 4217 currency code of the amounts, inferred from symbols and addresses, for example 'EUR'."},
    "totals_match": {"type": "boolean", "inferenceType": "inferred",
      "description": "True if the subtotal, shipping, insurance and tax amounts add up to the total (within 0.01); false otherwise."}
  },
  "$defs": {
    "Party": {
      "type": "object",
      "properties": {
        "name": {"type": "string", "inferenceType": "explicit",
          "description": "Company or person name, the first line of the block."},
        "address": {"type": "string", "inferenceType": "explicit",
          "description": "Street, city, state and ZIP, on one line, as printed."},
        "phone": {"type": "string", "inferenceType": "explicit",
          "description": "Phone number in the block, exactly as printed. Empty string if not printed."},
        "email": {"type": "string", "inferenceType": "explicit",
          "description": "Email address in the block. Empty string if not printed."},
        "eori_number": {"type": "string", "inferenceType": "explicit",
          "description": "EORI number after 'EORI:' in the block, without the label. Empty string if not printed."}
      }
    },
    "Shipment": {
      "type": "object",
      "properties": {
        "tracking_number": {"type": "string", "inferenceType": "explicit",
          "description": "Value under 'TRACKING NUMBER', as a string of digits (not a number, to keep all digits). Empty string if not printed."},
        "forwarding_agent": {"type": "string", "inferenceType": "explicit",
          "description": "The carrier named under 'FORWARDING AGENT'."},
        "incoterms": {"type": "string", "inferenceType": "explicit", "enum": ["EXW", "FCA", "CPT", "CIP", "DAP", "DPU", "DDP", "FAS", "FOB", "CFR", "CIF", "None"],
          "description": "Incoterms code after 'Incoterms:'. 'None' if no Incoterms line is printed."}
      }
    },
    "LineItem": {
      "type": "object",
      "properties": {
        "product_name": {"type": "string", "inferenceType": "explicit",
          "description": "First line of the PRODUCT cell, without the 'Country of origin' line."},
        "country_of_origin": {"type": "string", "inferenceType": "explicit",
          "description": "Country after 'Country of origin:' under the product name."},
        "hs_code": {"type": "string", "inferenceType": "explicit",
          "description": "Value in the 'HS CODE' column, exactly as printed, keeping the dot."},
        "quantity": {"type": "number", "inferenceType": "explicit",
          "description": "Value in the 'UNITS' column."},
        "unit_price": {"type": "number", "inferenceType": "explicit",
          "description": "Value in the 'UNIT PRICE' column. Number without currency symbol or thousands separators."},
        "amount": {"type": "number", "inferenceType": "explicit",
          "description": "Value in the 'TOTAL' column of the row. Number without currency symbol or thousands separators."}
      }
    }
  }
}
```

**Expected output**

```json
{
  "invoice_number": "F1000869/27",
  "invoice_date": "2022-03-14",
  "order_id": "X003678",
  "seller": {"name": "NORTHWIND LIFT PARTS", "address": "1820 Harbor Way, Kent, WA 98032", "phone": "(253) 555-0148", "email": "sales@northwindlift.example", "eori_number": "PT100005248965"},
  "bill_to": {"name": "CASCADE ACCESS SYSTEMS", "address": "77 Orchard Lane, Towson, MD 21204", "phone": "(410) 555-0192", "email": "ap@cascadeaccess.example", "eori_number": "PT100007731402"},
  "shipment": {"tracking_number": "65875423498564780", "forwarding_agent": "SwiftShip Freight", "incoterms": "FOB"},
  "line_items": [
    {"product_name": "Timing Belts", "country_of_origin": "US", "hs_code": "85041.2468", "quantity": 1, "unit_price": 19.8, "amount": 19.8},
    {"product_name": "Bracket Assembly", "country_of_origin": "US", "hs_code": "85041.2469", "quantity": 1, "unit_price": 21.5, "amount": 21.5},
    {"product_name": "Timing Pulleys", "country_of_origin": "US", "hs_code": "85825.2471", "quantity": 1, "unit_price": 39.45, "amount": 39.45}
  ],
  "subtotal": 80.75,
  "shipping_charges": 60.5,
  "insurance_charges": 0.0,
  "tax_amounts": [6.46],
  "total": 147.71,
  "payment_method": "DEBIT CARD",
  "currency": "USD",
  "totals_match": true
}
```