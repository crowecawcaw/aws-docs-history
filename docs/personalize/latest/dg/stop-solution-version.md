# Stopping the creation of a solution version

If your solution version has a status of CREATE_PENDING or CREATE_IN_PROGRESS, you can use
the Amazon Personalize console or the [StopSolutionVersionCreation](API_StopSolutionVersionCreation.md "API_StopSolutionVersionCreation.md") operation to stop creating the
solution version (stop training a model). You can't resume creating a solution version after
it has stopped. You are billed for resources used up to the point when the creation of the
solution version stopped.

Stopping the creation of a solution version ends model training, but doesn't delete the
solution version. You can still view the solution version details in the Amazon Personalize console and
with the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md") operation.

You can stop the solution version creation process with the Amazon Personalize console, the AWS Command Line Interface
(AWS CLI), or the AWS SDKs.

###### Topics

- [Stopping the creation of a solution version
  (console)](#stop-solution-version-console "#stop-solution-version-console")
- [Stopping the creation of a solution version
  (AWS CLI)](#stop-solution-version-cli "#stop-solution-version-cli")
- [Stopping the creation of a solution version
  (AWS SDKs)](#stop-solution-version-sdk "#stop-solution-version-sdk")

## Stopping the creation of a solution version

(console)

If your solution version has a status of CREATE_PENDING or CREATE_IN_PROGRESS, you can stop creating a solution version (stop training a model).

###### To stop creating a solution version (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign into your
   account.
2. On the **Dataset groups** page, choose the dataset group with the
   solution version that you want to stop.
3. In the navigation pane, choose **Solutions and recipes**.
4. On the **Solution and recipes** page, choose the solution with the
   solution version that you want to stop.
5. In **Solution versions**, choose the solution version that you want
   to stop.
6. On the solution version details page, choose **Stop creation**.
   Depending on the original state of the solution version, the solution version
   state changes as follows:
   - CREATE_PENDING changes to CREATE_STOPPED.
   - CREATE_IN_PROGRESS changes to CREATE_STOPPING and then
     CREATE_STOPPED.

## Stopping the creation of a solution version

(AWS CLI)

If your solution version has a status of CREATE_PENDING or CREATE_IN_PROGRESS, you can
stop creating a solution version (stop training a model). Use the following
`stop-solution-version-creation` command to stop creating the solution
version with the AWS CLI. Replace `solution version arn` with the Amazon
Resource Name (ARN) of the solution version that you want to stop. You are billed for
resources used up to the point that creation of the solution version stopped.

```
aws personalize stop-solution-version-creation \
    --solution-version-arn `solution version arn`
```

Check the training status of the solution version with the
`describe-solution-version` command.

```
aws personalize describe-solution-version \
    --solution-version-arn `solution version arn`
```

Depending on the original state of the solution version, the solution version state changes as follows:

- CREATE_PENDING changes to CREATE_STOPPED.
- CREATE_IN_PROGRESS changes to CREATE_STOPPING and then CREATE_STOPPED

## Stopping the creation of a solution version

(AWS SDKs)

If your solution version has a status of CREATE_PENDING or CREATE_IN_PROGRESS, you can
stop creating a solution version (stop training a model). The following code shows how
to stop creating a solution version with the AWS SDK for Python (Boto3) or AWS SDK for Java 2.x. You are
billed for resources used up to the point when creation of the solution version
stopped.

SDK for Python (Boto3)Use the following `stop_solution_version_creation`method to stop creation of a
solution version. Replace `solution_version_arn` with the Amazon
Resource Name (ARN) of the solution version that you want to stop. The method uses the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md") operation to retrieve the solution version's status.

```
import boto3

personalize = boto3.client('personalize')

response = personalize.stop_solution_version_creation(
    solutionVersionArn = `solution_version_arn`
)

# Use the solution version ARN to get the solution version status.
solution_version_description = personalize.describe_solution_version(
    solutionVersionArn = solution_version_arn)['solutionVersion']
print('Solution version status: ' + solution_version_description['status'])

```

SDK for Java 2.x
Use the following `stopSolutionVersionCreation` method to stop
creating a solution version. Pass as parameters an Amazon Personalize service client and
the Amazon Resource Name (ARN) of the solution version that you want to stop
creating. The following code uses the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md") operation to retrieve the solution version's status.

```
public static void stopSolutionVersionCreation(PersonalizeClient personalizeClient, String solutionVersionArn) {
    String solutionVersionStatus = "";

    StopSolutionVersionCreationRequest stopSolutionVersionCreationRequest = StopSolutionVersionCreationRequest.builder()
        .solutionVersionArn(solutionVersionArn)
        .build();

    personalizeClient.stopSolutionVersionCreation(stopSolutionVersionCreationRequest);

    // Use the solution version ARN to get the solution version status.
    DescribeSolutionVersionRequest describeSolutionVersionRequest = DescribeSolutionVersionRequest.builder()
        .solutionVersionArn(solutionVersionArn)
        .build();

    solutionVersionStatus = personalizeClient.describeSolutionVersion(describeSolutionVersionRequest)
        .solutionVersion()
        .status();
    System.out.println("Solution version status: " + solutionVersionStatus);
}
```

Depending on the original state of the solution version, the solution version state changes as follows:

- CREATE_PENDING changes to CREATE_STOPPED.
- CREATE_IN_PROGRESS changes to CREATE_STOPPING and then CREATE_STOPPED.
