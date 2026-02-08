# CSV upload for dependent field options

When you configure dependent field options for case templates, you can upload a CSV file. The file contains your field option mappings. This approach saves time compared to manually entering each relationship through the Amazon Connect admin website. This capability is useful when you have large datasets of hierarchical relationships. Examples include geographic hierarchies (Country → State → City) or product categorizations (Category → Subcategory).

## What is CSV upload for dependent field options?

CSV upload is a bulk configuration method for dependent field options in Amazon Connect Cases. Dependent field options create cascading dropdown menus. The available choices in one field (the target field) depend on the value selected in another field (the source field).

You can prepare your mappings in a CSV file and upload it. This saves time compared to manually configuring each source-target value relationship through the Amazon Connect admin website. The system parses your CSV file and validates the field names and values against your case template. The system then pre-populates the rule creation form with your data. You create the rule using the standard workflow.

## How CSV upload works?

### CSV file structure

The CSV file uses a four-column format with the following headers:

- **Parent Field Name** - The name of the source field that controls the relationship
- **Child Field Name** - The name of the target field whose options depend on the source field
- **Parent Value** - A specific value from the source field
- **Child Value** - An option that appears in the target field when the parent value is selected

Each row in your CSV represents one source-target value relationship. You can include multiple field pairs in a single CSV file by using different parent-child field name combinations. For example, you can include both Country-State relationships and Product Category-Subcategory relationships in the same file. The number of entries you can save depends on your account's quota limits.

You can download a CSV template from the Amazon Connect admin website. The template provides the correct format with placeholder headers.

### Upload and validation process

When you upload a CSV file, the system performs several validation checks:

- **File format validation** - Verifies the CSV structure and required columns
- **Field existence** - Confirms that the field names in your CSV match fields in your selected case template
- **Field type validation** - Ensures both source and target fields are single-select type fields
- **Value validation** - Checks that source field values exist in your template and identifies any child field values that don't exist

The system displays an error if source field values in your CSV do not exist in the template. If child field values do not exist, the system skips those values and shows an informational message.

After validation, the system groups your CSV rows by unique field pairs. The system displays each detected pair as a selectable option. If your CSV contains multiple field pairs, you select which pair to configure.

### Creating rules from CSV data

After you select a field pair from your uploaded CSV, the rule creation form automatically populates with the field names and value mappings from your file.

You must explicitly create the rule after the form is populated. The upload process does not automatically create rules. If you upload a new CSV file before creating the rule, the new file's data overwrites the previously populated options.

Each CSV upload creates one rule at a time. If your CSV contains multiple field pairs, you create rules for each pair separately. Select different pairs and complete the rule creation workflow for each.

### Limits and requirements

CSV upload has the following limits and requirements:

- **Single-select fields only** - Both source and target fields must be single-select type fields
- **Existing fields required** - All field names in your CSV must match fields that already exist

## Additional resources

Use the following APIs to programmatically create field options conditions:

- [CreateCaseRule](../APIReference/API_connect-cases_CreateCaseRule.md "../APIReference/API_connect-cases_CreateCaseRule.md"): Creates the field options condition using the "fieldOptions" rule type.
- [CreateTemplate](../APIReference/API_connect-cases_UpdateTemplate.md "../APIReference/API_connect-cases_UpdateTemplate.md") or [UpdateTemplate](../APIReference/API_connect-cases_UpdateTemplate.md "../APIReference/API_connect-cases_UpdateTemplate.md"): Associate the field options condition with the case template.
