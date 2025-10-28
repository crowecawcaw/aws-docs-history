# Using the SAP OData state management script

To use the SAP OData state management script in your AWS Glue job, follow these steps:

- Download the state management script: `s3://aws-blogs-artifacts-public/artifacts/BDB-4789/sap_odata_state_management.zip` from the public Amazon S3 bucket.
- Upload the script to an Amazon S3 bucket that your AWS Glue job has permissions to access.
- Reference the script in your AWS Glue job: When creating or updating your AWS Glue job, pass the `'--extra-py-files'` option referencing the script path in your Amazon S3 bucket. For example: `--extra-py-files s3://your-bucket/path/to/sap_odata_state_management.py`
- Import and use the state management library in your AWS Glue job scripts.

## Delta-token based Incremental Transfer example

Here's an example of how to use the state management script for delta-token based incremental transfers:

```
from sap_odata_state_management import StateManagerFactory, StateManagerType, StateType

# Initialize the state manager
state_manager = StateManagerFactory.create_manager(
    manager_type=StateManagerType.JOB_TAG,
    state_type=StateType.DELTA_TOKEN,
    options={
        "job_name": args['JOB_NAME'],
        "logger": logger
    }
)

# Get connector options (including delta token if available)
key = "SAPODataNode"
connector_options = state_manager.get_connector_options(key)

# Use the connector options in your Glue job
df = glueContext.create_dynamic_frame.from_options(
    connection_type="SAPOData",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "ENABLE_CDC": "true",
        **connector_options
    }
)

# Process your data here...

# Update the state after processing
state_manager.update_state(key, sapodata_df.toDF())
```

## Timestamp based Incremental Transfer example

Here's an example of how to use the state management script for delta-token based incremental transfers:

```
from sap_odata_state_management import StateManagerFactory, StateManagerType, StateType

# Initialize the state manager
state_manager = StateManagerFactory.create_manager(
    manager_type=StateManagerType.JOB_TAG,
    state_type=StateType.DELTA_TOKEN,
    options={
        "job_name": args['JOB_NAME'],
        "logger": logger
    }
)

# Get connector options (including delta token if available)
key = "SAPODataNode"
connector_options = state_manager.get_connector_options(key)

# Use the connector options in your Glue job
df = glueContext.create_dynamic_frame.from_options(
    connection_type="SAPOData",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "ENABLE_CDC": "true",
        **connector_options
    }
)

# Process your data here...

# Update the state after processing
state_manager.update_state(key, sapodata_df.toDF())
```

In both examples, the state management script handles the complexities of storing the state(either delta token or timestamp) between job runs. It automatically retrieves the last know state when getting connector options and updates the state after processing, ensuring the each job run only processes new or changed data.
