# CLI commands

The CI/CD CLI provides four core commands that cover the deployment lifecycle:

| Command                      | Description                                                                                                                                                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aws-smus-cicd-cli describe` | Validates the manifest, checks that target projects exist, and confirms the execution role has required permissions. Use `--connect` to validate against live AWS environments.                                                         |
| `aws-smus-cicd-cli bundle`   | Reads from the source target and packages application code, workflow definitions, and configurations into an immutable, versioned archive.                                                                                              |
| `aws-smus-cicd-cli deploy`   | Deploys bundle contents to the destination target. Provisions resources in dependency order — for example, uploading scripts to S3 before creating Glue jobs that reference them. Use `--dry-run` to preview changes without deploying. |
| `aws-smus-cicd-cli test`     | Runs post-deployment validation to confirm that services are running and ready for workloads in the target environment.                                                                                                                 |

Additional commands:

| Command                     | Description                                                                               |
| --------------------------- | ----------------------------------------------------------------------------------------- |
| `aws-smus-cicd-cli create`  | Generates a starter manifest from an existing Amazon SageMaker Unified Studio project.    |
| `aws-smus-cicd-cli run`     | Triggers Airflow workflow execution on MWAA or Airflow Serverless connections.            |
| `aws-smus-cicd-cli monitor` | Monitors workflow execution status in real time.                                          |
| `aws-smus-cicd-cli logs`    | Fetches and streams workflow execution logs.                                              |
| `aws-smus-cicd-cli destroy` | Removes deployed resources and projects. Use for failure recovery or environment cleanup. |
