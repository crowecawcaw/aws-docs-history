

# Blueprint schemas

This page describes the blueprint schema format that Amazon Textract accepts, and provides example schemas for three common document types: a W-2, a commercial invoice, and a bank statement. Each example can be passed straight to `aws textract create-blueprint --schema`. Pair each one with a sample document you already have so you can see the output before adapting the schema to your own documents.

## Blueprint schema
<a name="insights-blueprint-schema-reference"></a>

Every blueprint, however you create it, is validated against the following JSON Schema. A blueprint that does not match it is rejected with `ValidationException`.

```json
{
  "type": "object",
  "$defs": {
    "enumType": {
      "type": "array",
      "minItems": 1,
      "maxItems": 20,
      "items": {
        "type": "string"
      }
    },
    "definitionsType": {
      "type": "object",
      "patternProperties": {
        "^.*$": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string"
            },
            "inferenceType": {
              "type": "string",
              "enum": [
                "explicit",
                "inferred"
              ]
            },
            "additionalProperties": {
              "type": "boolean",
              "enum": [
                false
              ]
            },
            "properties": {
              "$ref": "#/$defs/propertiesType"
            }
          },
          "additionalProperties": false,
          "required": [
            "properties"
          ]
        }
      }
    },
    "itemsType": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "$ref": {
          "type": "string"
        },
        "items": {
          "$ref": "#/$defs/itemsType"
        },
        "enum": {
          "$ref": "#/$defs/enumType"
        }
      },
      "additionalProperties": false
    },
    "propertiesType": {
      "type": "object",
      "minProperties": 1,
      "maxProperties": 100,
      "patternProperties": {
        "^.*$": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string"
            },
            "inferenceType": {
              "type": "string",
              "enum": [
                "explicit",
                "inferred"
              ]
            },
            "description": {
              "type": "string"
            },
            "items": {
              "$ref": "#/$defs/itemsType"
            },
            "$ref": {
              "type": "string"
            },
            "enum": {
              "$ref": "#/$defs/enumType"
            }
          },
          "additionalProperties": false
        }
      }
    }
  },
  "properties": {
    "$schema": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "class": {
      "type": "string"
    },
    "type": {
      "type": "string",
      "enum": [
        "object"
      ]
    },
    "additionalProperties": {
      "type": "boolean",
      "enum": [
        false
      ]
    },
    "$defs": {
      "$ref": "#/$defs/definitionsType"
    },
    "properties": {
      "$ref": "#/$defs/propertiesType"
    }
  },
  "additionalProperties": false,
  "required": [
    "properties"
  ]
}
```

What the schema allows at each level:


| **Level** | **Allowed keys** | **Notes** | 
| --- | --- | --- | 
| Root | `properties`, `class`, `description`, `$defs`, `$schema`, `type` | Only `properties` is required. `type` must be `"object"` when present. | 
| Field (under `properties`) | `type`, `inferenceType`, `description`, `items`, `$ref`, `enum` | `inferenceType` is `explicit` or `inferred`. Each `properties` object has 1 to 100 fields. | 
| List items (under `items`) | `type`, `$ref`, `items`, `enum` |  | 
| Custom type (under `$defs`) | `properties`, `type` | `properties` is required. A custom type has no `description`; describe it on the field that refers to it. | 
| `enum` | 1 to 20 strings |  | 

The service also rejects a blueprint that breaks any of these rules, which the JSON Schema does not express:
+ At most 100 leaf fields and at most 30 list leaf fields in one blueprint.
+ Field names and custom type names are 1 to 60 characters and cannot contain `/`.
+ `description` (root or field) is at most 600 characters, `class` is at most 60 characters, and each `enum` value is at most 60 characters.
+ One level of nesting: a custom type cannot contain a table or another custom type.
+ No lists inside a table row, and no lists of lists.
+ A field with `$ref` has only `$ref` and `description`.
+ No `inferenceType` on a table field or on a custom type.
+ `enum` on a list field goes inside `items`.
+ Custom type names cannot be type names such as `string`, `number`, `integer`, `int`, `float`, `boolean`, `bool` or `enum`.

## How to use an example schema
<a name="insights-use-example-schema"></a>

To use one of the example schemas on this page, do the following:
+ Save one of the following example schemas to a file, for example `invoice-schema.json`.
+ Create the blueprint:

  ```
  aws textract create-blueprint \
    --blueprint-name "my-invoice-blueprint" \
    --schema file://invoice-schema.json \
    --region us-east-1
  ```
+ Attach the returned ARN to a project, or pass the blueprint ARN on a job with `--blueprints`. See [Creating blueprints](insights-creating-blueprints.md) and [Running jobs with inline blueprints](insights-inline-blueprints.md).

For the schema conventions used in the following examples — `class`, `description`, `properties`, explicit versus inferred, and the `$defs`/`$ref` table pattern — see [Creating blueprints](insights-creating-blueprints.md).

## Examples
<a name="insights-blueprint-schema-examples"></a>

### W-2: Wage and Tax Statement
<a name="insights-schema-w2"></a>

A flat, scalar-only schema for the IRS Form W-2 an employer issues to an employee. It is a good starting point because every field maps to a labeled box on a standardized form. Use any blank or filled IRS Form W-2 as a sample document.

```json
{
  "class": "W2",
  "description": "IRS Form W-2 Wage and Tax Statement issued by an employer to an employee for a tax year",
  "properties": {
    "EmployeeSSN": { "type": "string", "inferenceType": "explicit", "description": "Employee Social Security Number (box a)" },
    "EmployerEIN": { "type": "string", "inferenceType": "explicit", "description": "Employer Identification Number (box b)" },
    "EmployerName": { "type": "string", "inferenceType": "explicit", "description": "Employer name, address and ZIP code (box c)" },
    "EmployeeName": { "type": "string", "inferenceType": "explicit", "description": "Employee first name, last name and address (box e/f)" },
    "WagesTipsOtherComp": { "type": "number", "inferenceType": "explicit", "description": "Wages, tips, other compensation (box 1)" },
    "FederalIncomeTaxWithheld": { "type": "number", "inferenceType": "explicit", "description": "Federal income tax withheld (box 2)" },
    "SocialSecurityWages": { "type": "number", "inferenceType": "explicit", "description": "Social security wages (box 3)" },
    "SocialSecurityTaxWithheld": { "type": "number", "inferenceType": "explicit", "description": "Social security tax withheld (box 4)" },
    "MedicareWages": { "type": "number", "inferenceType": "explicit", "description": "Medicare wages and tips (box 5)" },
    "MedicareTaxWithheld": { "type": "number", "inferenceType": "explicit", "description": "Medicare tax withheld (box 6)" },
    "TaxYear": { "type": "string", "inferenceType": "explicit", "description": "Tax year printed on the form" }
  }
}
```

If you only need the standard W-2 fields, you can skip the custom blueprint and use the public blueprint `arn:aws:textract:us-east-1:aws:blueprint/public-w2-form` instead. See [Custom extraction with blueprints](insights-custom-extraction.md).

### Invoice: Commercial Invoice
<a name="insights-schema-invoice"></a>

A vendor invoice with header fields plus a repeating line-items table. This schema shows scalar extraction and table extraction together. The table is modeled with `$defs` \+ `$ref`. Use any standard vendor invoice PDF as a sample document.

```json
{
  "class": "Invoice",
  "description": "A commercial invoice issued by a vendor to a customer requesting payment for goods or services",
  "$defs": {
    "LineItem": {
      "properties": {
        "Description": { "type": "string", "inferenceType": "explicit", "description": "Description of the item or service" },
        "Quantity": { "type": "number", "inferenceType": "explicit", "description": "Quantity ordered" },
        "UnitPrice": { "type": "number", "inferenceType": "explicit", "description": "Price per unit" },
        "Amount": { "type": "number", "inferenceType": "explicit", "description": "Line total for this item" }
      }
    }
  },
  "properties": {
    "InvoiceNumber": { "type": "string", "inferenceType": "explicit", "description": "Unique invoice identifier" },
    "InvoiceDate": { "type": "string", "inferenceType": "explicit", "description": "Date the invoice was issued" },
    "DueDate": { "type": "string", "inferenceType": "explicit", "description": "Date payment is due" },
    "VendorName": { "type": "string", "inferenceType": "explicit", "description": "Name of the vendor or supplier issuing the invoice" },
    "VendorAddress": { "type": "string", "inferenceType": "explicit", "description": "Billing address of the vendor" },
    "BillToName": { "type": "string", "inferenceType": "explicit", "description": "Name of the customer being billed" },
    "PurchaseOrderNumber": { "type": "string", "inferenceType": "explicit", "description": "Associated purchase order number, if present" },
    "Subtotal": { "type": "number", "inferenceType": "explicit", "description": "Sum of line items before tax" },
    "TaxAmount": { "type": "number", "inferenceType": "explicit", "description": "Total tax charged" },
    "TotalDue": { "type": "number", "inferenceType": "explicit", "description": "Total amount due including tax" },
    "Currency": { "type": "string", "inferenceType": "inferred", "description": "Currency of the amounts (for example, USD)" },
    "LineItems": { "type": "array", "items": { "$ref": "#/$defs/LineItem" } }
  }
}
```

`LineItems` is an array of `LineItem` rows. Each row's fields are defined once in `$defs.LineItem.properties` and referenced with `{ "$ref": "#/$defs/LineItem" }`. `Currency` uses `inferred` because the currency code is often derived from context rather than printed as a standalone field.

### Bank Statement: Monthly Account Statement
<a name="insights-schema-bank-statement"></a>

A monthly checking or savings statement: account header fields plus a repeating transactions table, using the same `$defs`/`$ref` table pattern as the invoice. Use any monthly bank statement PDF as a sample document, and mask the account number if you share it.

```json
{
  "class": "BankStatement",
  "description": "A monthly bank account statement for a checking or savings account",
  "$defs": {
    "Transaction": {
      "properties": {
        "Date": { "type": "string", "inferenceType": "explicit", "description": "Transaction date" },
        "Description": { "type": "string", "inferenceType": "explicit", "description": "Transaction description or payee" },
        "Amount": { "type": "number", "inferenceType": "explicit", "description": "Transaction amount (negative for debits)" },
        "Balance": { "type": "number", "inferenceType": "explicit", "description": "Running balance after this transaction" }
      }
    }
  },
  "properties": {
    "BankName": { "type": "string", "inferenceType": "explicit", "description": "Name of the issuing bank" },
    "AccountHolderName": { "type": "string", "inferenceType": "explicit", "description": "Name of the account holder" },
    "AccountNumber": { "type": "string", "inferenceType": "explicit", "description": "Bank account number (often masked)" },
    "StatementPeriodStart": { "type": "string", "inferenceType": "explicit", "description": "Start date of the statement period" },
    "StatementPeriodEnd": { "type": "string", "inferenceType": "explicit", "description": "End date of the statement period" },
    "OpeningBalance": { "type": "number", "inferenceType": "explicit", "description": "Balance at the start of the period" },
    "ClosingBalance": { "type": "number", "inferenceType": "explicit", "description": "Balance at the end of the period" },
    "TotalDeposits": { "type": "number", "inferenceType": "explicit", "description": "Sum of deposits/credits during the period" },
    "TotalWithdrawals": { "type": "number", "inferenceType": "explicit", "description": "Sum of withdrawals/debits during the period" },
    "Transactions": { "type": "array", "items": { "$ref": "#/$defs/Transaction" } }
  }
}
```

If you only need standard bank-statement fields, you can use the public blueprint `arn:aws:textract:us-east-1:aws:blueprint/public-bank-statement` instead of a custom schema.

## Adapting the examples
<a name="insights-adapting-examples"></a>

When you adapt an example schema to your own documents, consider the following:
+ **Field naming** — property keys become the output field names. Pick names that match how your downstream code expects them.
+ **explicit versus inferred** — use `explicit` for values printed on the page (an invoice number, a dollar amount, a printed date, even when the description asks for a different format) and `inferred` for values the model must deduce or calculate (a currency code, a computed flag).
+ **Tables must use $defs \+ $ref** — an inline `{ "type": "object", "properties": {...} }` inside `items` is rejected with `ValidationException: Blueprint has invalid schema`.
+ **Schema size** — the `--schema` string has a maximum size. See [Limits and quotas](insights-quotas.md).

For the full schema reference and the blueprint management commands, see [Creating blueprints](insights-creating-blueprints.md).