# Performing safe canary updates

CloudWatch synthetics safe canary updates allows you to test the updates on your existing canaries before applying the changes. This feature helps you validate canary compatibility with new run times and other
configuration changes such as code or memory changes. This will help minimize potential monitoring disruptions caused by erroneous updates.

By using canary safe updates on runtime version updates, configuration changes, and code script modifications, you can mitigate risk, maintain uninterrupted monitoring, verify the changes before committing, update, and reduce downtime.

###### Topics

- [Prerequisites](#performing-safe-canary-upgrades-prereq "#performing-safe-canary-upgrades-prereq")
- [Best practices](#performing-safe-canary-upgrades-best-practices "#performing-safe-canary-upgrades-best-practices")
- [Testing canary using dry run](#performing-safe-canary-upgrades-getting-started "#performing-safe-canary-upgrades-getting-started")
- [Limitations](#performing-safe-canary-upgrades-limitations "#performing-safe-canary-upgrades-limitations")

## Prerequisites

Make sure the prequisites are complete.

- AWS account with CloudWatch synthetics permissions
- Existing canary on the supported runtime versions (see [Limitations](#performing-safe-canary-upgrades-limitations "#performing-safe-canary-upgrades-limitations") for compatible runtimes)
- Include compatible runtimes when performing a dry run (see [Limitations](#performing-safe-canary-upgrades-limitations "#performing-safe-canary-upgrades-limitations") for compatible runtimes)

## Best practices

Here are some best practices to follow while performing a canary .

- Execute a dry run to validate a runtime update
- Perform dry runs before production updates to canary
- Review canary logs and artifacts after a dry run
- Use dry runs to validate dependencies and library compatibility

## Testing canary using dry run

You can test the canary update using the following options:

**Using the AWS Management Console's Edit workflow**

1. Go the CloudWatch synthetics console.
2. Select the canary you want to update.
3. From the **Actions** drop down, choose **Edit**.

Update the canary with the changes you want to test. For example, changing runtime version or editing the script’s code. 4. Under **Canary script**, choose **Start Dry Run** to test and view the results immediately or choose **Validate and save later** at the bottom of the page to start the test and view the results later in your **Canary Details** page. 5. After the dry run succeeds, choose **Submit** to commit your canary updates.

**Using the AWS Management Console for updating canaries in a batch**

1. Go the CloudWatch synthetics console.
2. Choose the **Synthetics** list page.
3. Select upto five canaries for which you want to update the runtime.
4. From the **Actions** drop down, choose **Update Runtime**.
5. Choose **Start dry run for new runtime** to start the dry run and test your changes before an update.
6. On the **Synthetics** list page, you will see a text next to the **Runtime** version for the canary that displays the progress of the dry run (this is only displayed for dry runs involving a runtime update).

Once the dry run succeeds, you will see an **Initiate Update** text. 7. Choose **Initiate Update** to commit the runtime update. 8. If the dry run fails, you will see an **Update dry run failed** text. Choose the text to view the debug link to the canary details page.

**Using the AWS CLI or SDK**

The API starts the dry run for the provided canary name `MyCanary` and updates the runtime version to `syn-nodejs-puppeteer-10.0`.

```
aws synthetics start-canary-dry-run \
    --name MyCanary \
    --runtime-version syn-nodejs-puppeteer-10.0

      // Or if you wanted to update other configurations:

aws synthetics start-canary-dry-run \
    --name MyCanary \
    --execution-role-arn arn:aws:iam::123456789012:role/NewRole
```

The API will return the `DryRunId` inside the `DryRunConfigOutput`.

Call `GetCanary` with the provided `DryRunId` to receive the canary’s dry run configurations and an additional field `DryRunConfig` which contains the status of the dry run listed as `LastDryRunExecutionStatus`.

```
aws synthetics get-canary \
    --name MyCanary \
    --dry-run-id XXXX-XXXX-XXXX-XXXX
```

For more details, use `GetCanaryRuns` with the provided `DryRunId` to retrieve the run and additional information.

```
aws synthetics get-canary-runs \
    --name MyCanary \
    --dry-run-id XXXX-XXXX-XXXX-XXXX
```

After a successful dry run, you can then use `UpdateCanary` with the provided `DryRunId` in order to commit your changes.

```
aws synthetics update-canary \
    --name MyCanary \
    --dry-run-id XXXX-XXXX-XXXX-XXXX
```

When it fails for any reason (result from GetCanaryRuns will have the details), the result from `GetCanaryRuns` has an artifact location that contains logs to debug. When there are no logs, the dry run failed to be created. You can validate by using `GetCanary`.

```
aws synthetics get-canary \
    --name MyCanary \
    --dry-run-id XXXX-XXXX-XXXX-XXXX
```

The _State_, _StateReason_, and _StateReasonCode_ displays the status of the dry run.

**Using CloudFormation**

In your template for a Synthetics Canary, provide the field `DryRunAndUpdate` which accepts a boolean value `true` or `false`.

when the value is `true` every update executes a dry run to validate the changes before automatically updating the canary. When the dry run fails, the canary does not update and fails the deployment and CloudFormation deployment with a valid reason. To debug this issue, use the [AWS Synthetics console](CloudWatch_Synthetics_Canaries_Troubleshoot.md "CloudWatch_Synthetics_Canaries_Troubleshoot.md")
or if using an API, get the `ArtifactS3Location` using the `GetCanaryRuns` API, and download the `*-log.txt` files to review the canary log executions for errors. After validation, modify the CloudFormation template and retry the deployment or use the above API to validate.

When the value is `false`, synthetics will not execute a dry run to validate changes and will directly commit your updates.

For information on troubleshooting a failed canary, see [Troubleshooting a failed canary](CloudWatch_Synthetics_Canaries_Troubleshoot.md "CloudWatch_Synthetics_Canaries_Troubleshoot.md").

An example template.

```
SyntheticsCanary:
    Type: 'AWS::Synthetics::Canary'
    Properties:
      Name: MyCanary
      RuntimeVersion: syn-nodejs-puppeteer-10.0
      Schedule: {Expression: 'rate(5 minutes)', DurationInSeconds: 3600}
      ...
      DryRunAndUpdate: true
```

## Limitations

- Supports runtime versions – syn-nodejs-puppeteer-10.0+, syn-nodejs-playwright-2.0+, syn-python-selenium-5.1+, and syn-nodejs-3.0+
- You can only execute one dry run per canary at a time
- When a dry run fails, you cannot update the canary
- Dry run cannot test any **Schedule** field changes

###### Note

When you initiate a dry run with code changes for a Playwright canary and you want to update the canary without providing the associated `DryRunId`, you must explicitly specify the code parameters.
