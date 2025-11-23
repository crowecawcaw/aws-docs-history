# S3 Path

One of the properties of a `Project` is `s3`. You can access
various S3 paths that exist within your project.

```

# S3 path of project root directory
proj.s3.root
# S3 path of datalake consumer Glue DB directory (requires DataLake environment)
proj.s3.datalake_consumer_glue_db
# S3 path of Athena workgroup directory (requires DataLake environment)
proj.s3.datalake_athena_workgroup
# S3 path of workflows output directory (requires Workflows environment)
proj.s3.workflow_output_directory
# S3 path of workflows temp storage directory (requires Workflows environment)
proj.s3.workflow_temp_storage
# S3 path of EMR EC2 log destination directory (requires EMR EC2 environment)
proj.s3.emr_ec2_log_destination
# S3 path of EMR EC2 log bootstrap directory (requires EMR EC2 environment)
proj.s3.emr_ec2_certificates
# S3 path of EMR EC2 log bootstrap directory (requires EMR EC2 environment)
proj.s3.emr_ec2_log_bootstrap

```

## Other

Environment S3 Paths

You can also access the S3 path of a different environment by providing an
environment ID.

```

proj.s3.environment_path(environment_id="env_1234")

```
