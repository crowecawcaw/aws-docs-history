

# Creating blueprints

A custom blueprint is a JSON schema that lists the fields you want Amazon Textract Insights to extract from a document. You create a blueprint once, then attach it to a project or pass it inline on a job. This page describes the schema format and the commands that manage blueprints.

## Schema format
<a name="insights-blueprint-schema-format"></a>

A blueprint schema is a JSON object with three parts.


| **Key** | **Description** | 
| --- | --- | 
| `class` | A short label for the document type, for example `Invoice`. | 
| `description` | A one-line description of the document. | 
| `properties` | A map of the fields to extract. Each entry is a field definition. | 

Each field in `properties` carries three keys.


| **Key** | **Description** | 
| --- | --- | 
| `type` | The field's data type: `string`, `number`, `boolean`, or `array`. | 
| `inferenceType` | `explicit` or `inferred` (see the next section). | 
| `description` | Natural-language guidance the model uses to locate the value. | 

The following is a minimal, scalar-only schema.

```json
{
  "class": "W2",
  "description": "IRS Form W-2 Wage and Tax Statement issued by an employer to an employee for a tax year",
  "properties": {
    "EmployeeSSN": { "type": "string", "inferenceType": "explicit", "description": "Employee Social Security Number (box a)" },
    "EmployerEIN": { "type": "string", "inferenceType": "explicit", "description": "Employer Identification Number (box b)" },
    "WagesTipsOtherComp": { "type": "number", "inferenceType": "explicit", "description": "Wages, tips, other compensation (box 1)" },
    "TaxYear": { "type": "string", "inferenceType": "explicit", "description": "Tax year printed on the form" }
  }
}
```

The property keys become the field names in the output `inference_result`. Choose names that match how your downstream code expects them.

**Note**  
Field descriptions act as instructions to the model. Allow only trusted sources to author or change blueprint schemas and descriptions.

## Explicit versus inferred fields
<a name="insights-explicit-inferred"></a>

The `inferenceType` tells the model whether a value is read verbatim off the page or derived.
+ **explicit** — the value is written on the document, such as an invoice number or a dollar amount. Use `explicit` for most fields, including a printed date you want returned in a different format: name the label and the format in the description, for example "The value under the Invoice date label, in YYYY-MM-DD format".
+ **inferred** — the value is not printed on the document and has to be deduced or calculated, such as a currency code the model deduces from context or a computed flag.

## Writing good descriptions
<a name="insights-blueprint-descriptions"></a>

The model uses each field's description to find the value, so be specific. Include box or line numbers, expected formats, and common synonyms. For example, "Social security tax withheld (box 4)" locates a value more reliably than "tax withheld". Clear, specific descriptions are the main lever for extraction quality.

## Tables and repeating rows
<a name="insights-blueprint-tables"></a>

Model a table as an array whose items reference a row type defined in a top-level `$defs` map. A `$defs` entry is a `properties` object only — it has no `type` or `inferenceType` on the entry itself.

```json
{
  "class": "Invoice",
  "description": "A commercial invoice issued by a vendor to a customer",
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
    "TotalDue": { "type": "number", "inferenceType": "explicit", "description": "Total amount due including tax" },
    "LineItems": { "type": "array", "items": { "$ref": "#/$defs/LineItem" } }
  }
}
```

Each `LineItem` row's fields are defined once in `$defs.LineItem.properties` and referenced from the array with `{ "$ref": "#/$defs/LineItem" }`. In the output, `LineItems` is an array of objects, one per detected row.

### Inline object pitfall
<a name="insights-inline-object-pitfall"></a>

Do not define a table row with an inline `{ "type": "object", "properties": { ... } }` inside `items`. An inline object type is rejected:

```
ValidationException: Blueprint has invalid schema
```

Always use the `$defs` \+ `$ref` pattern shown earlier for tables and nested groups.

## Schema size limit
<a name="insights-blueprint-schema-size"></a>

The schema string passed to `--schema` has a maximum size. See [Limits and quotas](insights-quotas.md).

## Managing blueprints
<a name="insights-managing-blueprints"></a>

Blueprints are managed with the `CreateBlueprint`, `UpdateBlueprint`, `GetBlueprint`, `ListBlueprints`, and `DeleteBlueprint` operations. All examples use account 111122223333 and AWS Region us-east-1.

### Create a blueprint
<a name="insights-create-a-blueprint"></a>

Save the schema to a file and create the blueprint. `CreateBlueprint` returns the new blueprint ARN.

```
aws textract create-blueprint \
  --blueprint-name "my-invoice-blueprint" \
  --schema file://invoice-schema.json \
  --region us-east-1
```

To tag a blueprint when you create it, add `--tags`. Tags apply to the blueprint as a whole, not to individual versions. See [Tagging Amazon Textract Insights resources](insights-tagging.md).

### Update a blueprint
<a name="insights-update-a-blueprint"></a>

`UpdateBlueprint` replaces the current schema with a new one.

```
aws textract update-blueprint \
  --blueprint-arn "arn:aws:textract:us-east-1:111122223333:blueprint/my-invoice-blueprint" \
  --schema file://invoice-schema-v2.json \
  --region us-east-1
```

### Get a blueprint
<a name="insights-get-a-blueprint"></a>

`GetBlueprint` without a version returns the current schema.

```
aws textract get-blueprint \
  --blueprint-arn "arn:aws:textract:us-east-1:111122223333:blueprint/my-invoice-blueprint" \
  --region us-east-1
```

### List your blueprints
<a name="insights-list-your-blueprints"></a>

`ListBlueprints` with the default resource owner lists the blueprints in your account.

```
aws textract list-blueprints \
  --resource-owner ACCOUNT \
  --region us-east-1
```

### Delete a blueprint
<a name="insights-delete-a-blueprint"></a>

`DeleteBlueprint` removes a blueprint. A blueprint that still has numbered versions, or that is referenced by a project, cannot be deleted; see [Blueprint versioning](insights-blueprint-versioning.md).

```
aws textract delete-blueprint \
  --blueprint-arn "arn:aws:textract:us-east-1:111122223333:blueprint/my-invoice-blueprint" \
  --region us-east-1
```

For ready-to-use schemas you can adapt, see [Blueprint schemas](insights-blueprint-schemas.md). To pin a specific version of a blueprint in a project, see [Blueprint versioning](insights-blueprint-versioning.md). For request parameters and errors, see the Amazon Textract Insights API Reference.