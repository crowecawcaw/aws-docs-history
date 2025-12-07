# Spark Upgrade Agent Workflow In Details

To initiate the upgrade process, you will need the Spark application code cloned to your developer environment (locally or EC2 or
[Amazon SageMaker Unified Studio IDE Spaces](../../../sagemaker-unified-studio/latest/userguide/create-space.md "../../../sagemaker-unified-studio/latest/userguide/create-space.md")), preferably with Git version control initialized. Additionally, an EMR cluster running the target Spark version must be provisioned and accessible. Finally, a designated Amazon S3 bucket path should be configured to store deployment artifacts and upgrade summary throughout the upgrade process.

Once these requirements are established, you can submit a prompt like the following to kick off the upgrade workflow:

```
Upgrade my Spark application <local-project-path> from EMR version 6.0.0 to 7.12.0.
Use EMR-EC2 Cluster <cluster-id> to run the validation and s3 paths
s3://<please fill in your staging bucket path> to store updated application artifacts.
```

At this point, the agent will orchestrate the upgrade using specialized tools (for more
[details](emr-spark-upgrade-agent-tools.md "emr-spark-upgrade-agent-tools.md")). The workflow follows these steps:

1. **Generate Plan**: The agent will analyze your project structure and generate an upgrade plan. Review the plan and provide your consent to proceed.
2. **Plan Review and Customization**: When prompted to review the plan, you have several options:
   1. **Proceed as-is**: Accept the plan and continue with execution
   2. **Provide feedback**: Customize the plan by:
      1. Removing unnecessary steps - Example: Remove any integration test execution. Only compile/build locally, then proceed to EMR validation.
      2. Adding additional steps - Example: Add a step to run test file `tests/test_jobs/test_etl_job_x.py` before EMR validation.
      3. Modifying the upgrade approach - Example: Enforce Python 3.10 and Java 17 during the build and validation steps.

3. The agent will regenerate the plan based on your feedback and ask for consent again. This process continues until you approve the final plan
4. **Compile and Build**: The agent will make iterative changes to fix build errors until the application compiles and builds successfully.
5. **Run unit and Integration Tests**: If the project has tests, the agent will run the tests after a successful build. If any tests fail, the agent will modify the source code iteratively until the tests pass before proceeding to EMR validation.
6. **Runtime Fixes and Validation**: The agent will validate the application on the target EMR cluster and iteratively fix any runtime errors until validation is successful. Upon completion, you'll see a summary of all changes made for compatibility.
7. **Summary for the upgrade**: Once the upgrade is complete, the agent will provide a summary of all code and configuration changes, dependency version updates, and any detected data quality mismatches for your review.
