

# Verify the workflow status
<a name="using-get-workflow"></a>

After you create your workflow, you can verify the status and view other details of the workflow using **get-workflow**, as shown.

```
aws omics get-workflow --id 1234567 
```

The response includes workflow details, including the status, as shown.

```
{
    "arn": "arn:aws:omics:us-west-2:....",
    "creationTime": "2022-07-06T00:27:05.542459" 
    "id": "1234567",
    "engine": "WDL",
    "status": "ACTIVE",
    "type": "PRIVATE",
    "main": "workflow-crambam.wdl",
    "name": "workflow_name",
    "storageType": "STATIC",
    "storageCapacity": "1200",
    "uuid": "64c9a39e-8302-cc45-0262-2ea7116d854f"   
  }
```

You can start a run using this workflow after the status transitions to `ACTIVE`.

**Note**  
For Nextflow DSL2 workflows, HealthOmics runs the built-in strict linter during creation. If the linter detects errors or warnings, the workflow still transitions to ACTIVE, with the `statusMessage` field containing structured lint results. If you start a run on a workflow with linter errors, your run may fail due to an incorrect workflow definition. For an example of the `GetWorkflow` response with lint findings, see [Workflow linters in HealthOmics](workflows-linter.md).