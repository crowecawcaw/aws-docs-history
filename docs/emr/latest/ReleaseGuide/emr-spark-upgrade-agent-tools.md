# Using Spark Upgrade Tools

## Available Upgrade Tools

The MCP service provides several tools to assist with Spark upgrades. The major tools are the following:

|     | Tool name                               | Tool Category   | Description                                                         |
| --- | --------------------------------------- | --------------- | ------------------------------------------------------------------- |
| 1   | **generate_spark_upgrade_plan**         | Planner         | Generate a EMR-EC2/EMR-S upgrade plan                               |
| 2   | **reuse_existing_spark_upgrade_plan**   | Planner         | Reuse existing local upgrade plan                                   |
| 3   | **update_build_configuration**          | Build           | Upgrade build configuration files                                   |
| 4   | **check_and_update_build_environment**  | Build           | Check/update Java environment for Spark upgrade                     |
| 5   | **compile_and_build_project**           | Build           | Provide guidance for compiling/building project                     |
| 6   | **run_validation_job**                  | Test            | Submit Spark app to EMR-EC2/EMR-S                                   |
| 7   | **check_job_status**                    | Test            | Check status of EMR-EC2 step or EMR-S job run                       |
| 8   | **check_and_update_python_environment** | Spark code edit | Check/update Python env for Spark upgrade                           |
| 9   | **fix_upgrade_failure**                 | Spark code edit | Analyze a failure and suggest fixes                                 |
| 10  | **get_data_quality_summary**            | Observablity    | Retrieve the data quality summary after the application is upgraded |
| 11  | **describe_upgrade_analysis**           | Observablity    | describe the given analysis                                         |
| 12  | **list_upgrade_analyses**               | Observablity    | list all analyses created by current account                        |

For a full list of all the upgrade tools provided by the SMUS Managed MCP server, you may list all tools from the server.
