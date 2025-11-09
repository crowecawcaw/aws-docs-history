# Workflow linters in HealthOmics

After you create a workflow, we recommend that you run a linter on the workflow before you start the first run.
The linter detects errors that can cause the run to fail.

For WDL, HealthOmics automatically runs a linter when you create the workflow. The linter output is available in the
`statusMessage` field of the **get-workflow** response. Use the following CLI command to retrieve the status output (use
the workflow ID of the WDL workflow that you created):

```
aws omics get-workflow
   —id `123456`
   —query 'statusMessage'
```

HealthOmics provides linters that you can run on the workflow defnition before you create the workflow.
Run these linters on existing pipelines that you're migrating to HealthOmics.

- **WDL** – A public Amazon ECR image to run a [WDL linter](https://gallery.ecr.aws/aws-genomics/healthomics-linter "https://gallery.ecr.aws/aws-genomics/healthomics-linter").

- **Nextflow** – A public Amazon ECR image to run [Linter rules for Nextflow](https://gallery.ecr.aws/aws-genomics/linter-rules-for-nextflow " https://gallery.ecr.aws/aws-genomics/linter-rules-for-nextflow"). You
  can access the source code for this linter from [GitHub](https://github.com/awslabs/linter-rules-for-nextflow "https://github.com/awslabs/linter-rules-for-nextflow").
- **CWL** – not available
