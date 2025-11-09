# Verify the workflow status

After you create your workflow, you can verify the status and view other details
of the workflow using **get-workflow**, as shown.

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
