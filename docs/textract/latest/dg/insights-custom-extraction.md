

# Custom extraction with blueprints

A blueprint tells Amazon Textract Insights which fields to extract from a document and returns the result as structured data keyed by your field names. Attach one or more blueprints to a project, or pass them inline on a job, to get custom extraction results in addition to (or instead of) extraction.

Blueprints come in two kinds: **public blueprints** that AWS maintains for common document types, and **custom blueprints** that you define with your own schema.

Without splitting enabled, custom extraction has a maximum number of pages supported per document. For longer files, enable splitting so the file is divided into individual documents before blueprints are applied. See [Splitting multi-document files](insights-splitting.md) and [Limits and quotas](insights-quotas.md).

## Public blueprints
<a name="insights-public-blueprints"></a>

Public blueprints are managed by AWS and cover widely used document types. You do not create or version them; you reference them by ARN. Each public blueprint ARN has the form:

```
arn:aws:textract:<region>:aws:blueprint/<name>
```

For example, the W-2 blueprint in US East (N. Virginia) is `arn:aws:textract:us-east-1:aws:blueprint/public-w2-form`.

To list the public blueprints available in an AWS Region, call `ListBlueprints` with the service resource owner:

```bash
aws textract list-blueprints \
  --resource-owner SERVICE \
  --region us-east-1
```

The following public blueprints are currently available.


**Public blueprints**  

| **Document type** | **Blueprint ARN** | 
| --- | --- | 
| `Bank-Statement` | `arn:aws:textract:<region>:aws:blueprint/public-bank-statement` | 
| `Birth-Certificate` | `arn:aws:textract:<region>:aws:blueprint/public-birth-certificate` | 
| `Cable-Bill` | `arn:aws:textract:<region>:aws:blueprint/public-cable-bill` | 
| `Canada-Driver-License` | `arn:aws:textract:<region>:aws:blueprint/public-canada-driver-license` | 
| `Covid-Vaccination-Card` | `arn:aws:textract:<region>:aws:blueprint/public-covid-vaccination-card` | 
| `Credit-Card-Statement` | `arn:aws:textract:<region>:aws:blueprint/public-credit-card-statement` | 
| `Death-Certificate` | `arn:aws:textract:<region>:aws:blueprint/public-death-certificate` | 
| `Demographic-Addendum` | `arn:aws:textract:<region>:aws:blueprint/public-demographic-addendum` | 
| `Dental-Insurance-Card` | `arn:aws:textract:<region>:aws:blueprint/public-dental-insurance-card` | 
| `Electricity-Bill` | `arn:aws:textract:<region>:aws:blueprint/public-electricity-bill` | 
| `Form-1005` | `arn:aws:textract:<region>:aws:blueprint/public-form-1005` | 
| `Form-1040` | `arn:aws:textract:<region>:aws:blueprint/public-form-1040` | 
| `Form-1040-Schedule-C` | `arn:aws:textract:<region>:aws:blueprint/public-form-1040-schedule-c` | 
| `Form-1098` | `arn:aws:textract:<region>:aws:blueprint/public-form-1098` | 
| `Form-1099-INT` | `arn:aws:textract:<region>:aws:blueprint/public-form-1099-int` | 
| `Form-1099-MISC` | `arn:aws:textract:<region>:aws:blueprint/public-form-1099-misc` | 
| `Form-940` | `arn:aws:textract:<region>:aws:blueprint/public-form-940` | 
| `Form-941` | `arn:aws:textract:<region>:aws:blueprint/public-form-941` | 
| `Form-W9` | `arn:aws:textract:<region>:aws:blueprint/public-form-w9` | 
| `HOA-Statement` | `arn:aws:textract:<region>:aws:blueprint/public-hoa-statement` | 
| `Invoice` | `arn:aws:textract:<region>:aws:blueprint/public-invoice` | 
| `Payslip` | `arn:aws:textract:<region>:aws:blueprint/public-payslip` | 
| `Prescription-Label` | `arn:aws:textract:<region>:aws:blueprint/public-prescription-label` | 
| `Property_Tax_Statement` | `arn:aws:textract:<region>:aws:blueprint/public-property-tax-statement` | 
| `Receipt` | `arn:aws:textract:<region>:aws:blueprint/public-receipt` | 
| `US-Bank-Check` | `arn:aws:textract:<region>:aws:blueprint/public-us-bank-check` | 
| `US-College-ID` | `arn:aws:textract:<region>:aws:blueprint/public-us-college-id` | 
| `US-Driver-License` | `arn:aws:textract:<region>:aws:blueprint/public-us-driver-license` | 
| `US-Marriage-Certificate` | `arn:aws:textract:<region>:aws:blueprint/public-us-marriage-certificate` | 
| `US-Medical-Insurance-Card` | `arn:aws:textract:<region>:aws:blueprint/public-us-medical-insurance-card` | 
| `US-Passport` | `arn:aws:textract:<region>:aws:blueprint/public-us-passport` | 
| `US-Vehicle-Title-Document` | `arn:aws:textract:<region>:aws:blueprint/public-us-vehicle-title-document` | 
| `W2-Form` | `arn:aws:textract:<region>:aws:blueprint/public-w2-form` | 
| `Water-And-Sewer-Bill` | `arn:aws:textract:<region>:aws:blueprint/public-water-and-sewer-bill` | 
| `Workers-Compensation-Form` | `arn:aws:textract:<region>:aws:blueprint/public-workers-compensation-form` | 

Replace `<region>` with the AWS Region you call, for example `us-east-1`.

## Custom blueprints
<a name="insights-custom-blueprints"></a>

When no public blueprint matches your document, or you need a different set of fields, define a custom blueprint with your own JSON schema. The schema lists the fields to extract, their data types, and natural-language descriptions that guide the model. For the schema format and the commands to create, update, get, list, and delete blueprints, see [Creating blueprints](insights-creating-blueprints.md). For how to adapt the examples on this page to real documents, see [Blueprint schemas](insights-blueprint-schemas.md).

## Custom extraction result.json field reference
<a name="insights-custom-extraction-result"></a>

When a document matches a blueprint, Amazon Textract Insights writes a custom extraction result.json at `<prefix>/<job-id>/<asset-id>/custom/<n>/result.json`, where `<n>` is the index of the matched sub-document. The file has the following top-level structure.


**Top-level fields in custom extraction result.json**  

| **Field** | **Description** | 
| --- | --- | 
| `matched_blueprint` | The blueprint that matched this document: `arn`, `name`, and `confidence` (0–1). | 
| `document_class` | The document class, with `type` set to the matched blueprint's class. | 
| `split_document` | `page_indices`, the input pages that make up this sub-document. | 
| `inference_result` | The extracted field values, keyed by your schema. Scalar fields hold strings, numbers, or booleans; tables are arrays of row objects; nested groups are objects. A field that was not found holds an empty string (`""`). | 
| `explainability_info` | An array that mirrors `inference_result`, adding a `confidence` and `location` for every leaf field. | 

### inference\_result
<a name="insights-inference-result"></a>

`inference_result` is keyed exactly by the property names in your blueprint schema. The following example is trimmed custom extraction results from the public W-2 blueprint, with sample values replaced by placeholders.

```json
{
  "matched_blueprint": {
    "arn": "arn:aws:textract:us-east-1:aws:blueprint/public-w2-form",
    "name": "W2-Form",
    "confidence": 1
  },
  "document_class": { "type": "W2" },
  "split_document": { "page_indices": [0, 1] },
  "inference_result": {
    "employee_general_info": {
      "first_name": "Jane",
      "employee_last_name": "Doe",
      "employee_address": "123 Any Street, Anytown, WA 98101",
      "employee_zip_code": 98101,
      "ssn": "123-45-6789"
    },
    "employer_info": {
      "employer_name": "Example Corp",
      "ein": "12-3456789",
      "control_number": ""
    },
    "federal_wage_info": {
      "wages_tips_other_compensation": 68450,
      "social_security_wages": 68450
    }
  }
}
```

Note how `control_number` was not present on the document and is returned as an empty string.

### explainability\_info
<a name="insights-explainability-info"></a>

`explainability_info` is an array whose entries mirror the shape of `inference_result`. Each leaf field is replaced by an object with the following keys.


**Keys on an explainability\_info leaf field**  

| **Field** | **Description** | 
| --- | --- | 
| `success` | `true` when the field was processed. | 
| `confidence` | Model confidence for the value, from 0 to 1. | 
| `type` | The field's schema type, for example `string` or `number`. | 
| `value` | The extracted value (empty string when not found). | 
| `geometry` | An array of locations on the page. Each entry has `boundingBox` (`top`, `left`, `width`, `height` as ratios of page size), `vertices`, `page` (1-based), and `word_references` (`word_index`, `page_index`). | 

The following is a single leaf from `explainability_info`, trimmed.

```json
{
  "employer_info": {
    "employer_name": {
      "success": true,
      "confidence": 0.9030104875564575,
      "type": "string",
      "value": "Example Corp",
      "geometry": [
        {
          "boundingBox": { "top": 0.1274, "left": 0.0660, "width": 0.1928, "height": 0.0100 },
          "page": 1,
          "word_references": [ { "word_index": 29, "page_index": 0 } ]
        }
      ]
    }
  }
}
```

### Confidence-based routing
<a name="insights-confidence-routing"></a>

Because `explainability_info` carries a confidence per field, you can route individual fields to human review rather than accepting or rejecting the whole document. A common pattern is to pick a confidence threshold, pass fields at or above it straight to downstream processing, and queue fields below it for a human to confirm. Field confidences vary within a single document, so this lets you auto-process high-confidence fields while catching the few that need attention.

For how to detect and mask personal data in output, see [Detecting and redacting sensitive data](insights-detecting-redacting.md). For request parameters and errors, see the Amazon Textract Insights API Reference.