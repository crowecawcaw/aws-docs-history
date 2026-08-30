# Workflow linters in HealthOmics

HealthOmics automatically lints WDL and Nextflow DSL2 workflows during creation. The built-in linters detect
errors in your workflow definition files that can cause runs to fail. Lint findings appear in the
`statusMessage` field of the **GetWorkflow** response.

For WDL workflows, lint findings are blocking — the workflow does not transition to ACTIVE if
errors are detected. For Nextflow DSL2 workflows, lint findings are non-blocking — the workflow
transitions to ACTIVE regardless of findings.

HealthOmics also provides external linters that you can run locally before you create a workflow.
These linters can include additional HealthOmics-specific rules.

## Built-in linters

HealthOmics runs built-in linters server-side when you call `CreateWorkflow` or
`CreateWorkflowVersion`.

### WDL built-in linting

For WDL, HealthOmics automatically runs a linter when you create the workflow. WDL linting is
blocking — if the linter detects errors, the workflow does not transition to ACTIVE. You
can find the linter output in the `statusMessage` field of the `GetWorkflow`
response. Use the following CLI command to retrieve the status output (use the workflow ID of the
WDL workflow that you created):

```
aws omics get-workflow
   —id `123456`
   —query 'statusMessage'
```

### Nextflow built-in linting

HealthOmics runs the Nextflow inbuilt strict DSL2 linter (nf-lang/v2) automatically during
`CreateWorkflow` and `CreateWorkflowVersion` for all supported
Nextflow DSL2 versions:

- Nextflow v22.04 (DSL2 only)
- Nextflow v23.10
- Nextflow v24.10
- Nextflow v25.10
- Nextflow v26.04

###### Note

The built-in linter applies only to DSL2 workflows. DSL1 workflows are not linted.

The Nextflow linter operates in non-blocking mode. Findings don't prevent the workflow from
becoming ACTIVE. You can review findings at any time without interrupting your workflow creation process.

###### Note

The built-in Nextflow linter validates your workflow definition syntax at creation time. It is
distinct from the strict syntax _parser_ available for Nextflow v26.04, which is
controlled by `engineSettings.syntaxVersion` and affects runtime behavior. The linter runs
at creation time across all DSL2 versions, regardless of which parser the workflow uses at runtime.

#### To retrieve Nextflow lint output

Lint findings appear as structured JSON in the `statusMessage` field of the
`GetWorkflow` response. Use the following CLI command to retrieve the lint output:

```
aws omics get-workflow --id `1234567` --query 'statusMessage'
```

The following example shows the JSON output from the Nextflow linter:

```
{
  "advisory": "Linting findings are from the strict Nextflow DSL2 (nf-lang/v2) linter and reflect the syntax that will be required in Nextflow 25/26 strict mode. On Nextflow 23/24 (legacy grammar) findings are advisory only.",
  "summary": {
    "errors": 2,
    "filesWithErrors": 1,
    "filesWithoutErrors": 0,
    "filesFormatted": 0,
    "warnings": 0,
    "filesWithWarnings": 0,
    "filesWithoutWarnings": 2
  },
  "errors": [
    {
      "filename": "nextflow-lint-legacy.nf",
      "startLine": 24,
      "startColumn": 5,
      "message": "`for` loops are no longer supported"
    },
    {
      "filename": "nextflow-lint-legacy.nf",
      "startLine": 24,
      "startColumn": 10,
      "message": "`i` is not defined"
    }
  ],
  "warnings": []
}
```

#### Lint output fields

The JSON output contains the following fields:

- `advisory` – Explains version-specific applicability of the findings.
  On Nextflow v22.04, v23.10, and v24.10 (legacy grammar), findings are advisory only. On Nextflow v25.10 and v26.04,
  findings reflect strict mode syntax requirements.
- `summary` – Contains aggregate counts of errors and warnings across
  all files in the workflow.
- `errors` – An array of error objects. Each error contains
  `filename`, `startLine`, `startColumn`, and
  `message`.
- `warnings` – An array of warning objects. Each warning contains the
  same fields as error objects.
- `truncated` – A conditional flag that appears when the lint output
  exceeds field size limits. When truncation occurs, warnings are dropped first. The
  workflow remains ACTIVE with a valid trimmed report.

#### Recommendations

We recommend the following workflow to address lint findings:

1. Review the lint findings in the `statusMessage` field.
2. Fix the errors in your workflow definition file.
3. Re-create the workflow to generate a clean lint report.

## External linters

The following external linters are available:

- **WDL** – A public Amazon ECR image to run a [WDL linter](https://gallery.ecr.aws/aws-genomics/healthomics-linter "https://gallery.ecr.aws/aws-genomics/healthomics-linter") on Amazon ECR Public Gallery.
- **Nextflow** – A public Amazon ECR image to run [Linter rules for Nextflow](https://gallery.ecr.aws/aws-genomics/linter-rules-for-nextflow "https://gallery.ecr.aws/aws-genomics/linter-rules-for-nextflow") on Amazon ECR Public Gallery. You
  can access the source code from the [linter-rules-for-nextflow](https://github.com/awslabs/linter-rules-for-nextflow "https://github.com/awslabs/linter-rules-for-nextflow") repository on GitHub.
- **CWL** – Not available.

The following list describes the distinction between built-in and external linters:

- **Built-in linters** – Run server-side during
  `CreateWorkflow` and `CreateWorkflowVersion`. For WDL, findings are
  blocking. For Nextflow DSL2, findings are non-blocking. Apply to WDL and Nextflow DSL2
  workflows only.
- **External linters** – Run locally before workflow
  creation. Can include additional HealthOmics-specific compatibility rules. Available as public Amazon ECR images.
