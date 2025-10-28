# Manually creating a solution version

After you complete [Configuring a custom solution in Amazon Personalize](customizing-solution-config.md "customizing-solution-config.md"), you are ready to start training:

- If your solution uses automatic training, the solution creates solution versions for you
  at the training frequency you specify. By default, all new solutions use automatic training to create a new solution version every 7 days. You can
  still manually create solution versions. For more information,
  see [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md").
- If you turn off auto training for your solution or you want to manually train,
  you can manually create a solution version. A _solution version_ refers to a trained machine learning model.
  You can create a solution version using the console, AWS Command Line Interface (AWS CLI), or AWS SDKs.
  If your solution version has a status of CREATE_PENDING or CREATE_IN_PROGRESS, you can use the
  [StopSolutionVersionCreation](API_StopSolutionVersionCreation.md "API_StopSolutionVersionCreation.md") operation to stop the solution version creation process.
  See [Stopping the creation of a solution version](stop-solution-version.md "stop-solution-version.md").
  If training does not complete because of an error, you are not charged for the training. If your solution version has a status of CREATE_PENDING or CREATE_IN_PROGRESS,
  you can stop the solution version creation process. To stop solution version creation, navigate to the
  solution version details page and choose **Stop**. For more information, see [Stopping the creation of a solution version](stop-solution-version.md "stop-solution-version.md").

###### Topics

- [Creating a solution version (console)](#create-solution-version-console "#create-solution-version-console")
- [Creating a solution version (AWS CLI)](#create-solution-version-cli "#create-solution-version-cli")
- [Creating a solution version (AWS SDKs)](#create-solution-version-sdk "#create-solution-version-sdk")

## Creating a solution version (console)

To manually create a new solution version with the Amazon Personalize console, you start training from the details page of your solution.

###### To create a new solution version

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign into your
   account.
2. Navigate to the dataset groups page and choose the dataset group with your new solution.
3. In the navigation pane, under **Custom resources**, choose **Solutions and recipes**.
4. On the **Solution and recipes** page, choose the solution you want to create a solution version for.
5. On the solution overview page, choose **Create solution version** to start training a new model.

On the solution details page, you can track training progress in the **Solution versions** section. When training is complete,
the status is **Active** you can evaluate it using metrics supplied by Amazon Personalize.
For more information, see [Evaluating an Amazon Personalize solution version with metrics](working-with-training-metrics.md "working-with-training-metrics.md").

When the solution version is ACTIVE, you are ready to use it to get recommendations. How you use an active solution version depends on how you get recommendations:

- For real-time recommendations, you deploy an ACTIVE solution version with an Amazon Personalize campaign. You use the campaign to get recommendations for your users.
  See [Deploying an Amazon Personalize solution version with a campaign](campaigns.md "campaigns.md").
- For batch recommendations, you specify an ACTIVE solution version when you create a batch inference job or batch
  segment job. See [Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md") or [Getting batch user segments](getting-user-segments.md "getting-user-segments.md").

## Creating a solution version (AWS CLI)

When your solution is ACTIVE, train the model by running the following
command. Replace `solution arn` with the solution Amazon Resource Name (ARN) from [Configuring a custom solution in Amazon Personalize](customizing-solution-config.md "customizing-solution-config.md").

```
aws personalize create-solution-version \
  --solution-arn `solution arn`
```

The solution version ARN is displayed, for example:

```
{
  "solutionVersionArn": "arn:aws:personalize:us-west-2:acct-id:solution/SolutionName/<version-id>"
}
```

Check the training status of the solution version by using the
`describe-solution-version` command. Provide the solution version ARN that
was returned in the previous step. For more information about the API, see [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md").

```
aws personalize describe-solution-version \
  --solution-version-arn `solution version arn`
```

The properties of the solution version and the training `status` are
displayed. Initially, the status shows as CREATE PENDING, for example:

```
{
  "solutionVersion": {
      "solutionVersionArn": "arn:aws:personalize:us-west-2:acct-id:solution/solutionName/<version-id>",
      ...,
      "status": "CREATE PENDING"
  }
}
```

Training is complete when the `status` is `ACTIVE` and you can evaluate it using metrics supplied by Amazon Personalize.
For more information, see [Evaluating an Amazon Personalize solution version with metrics](working-with-training-metrics.md "working-with-training-metrics.md"). If training does not complete because of an error, you are not charged for the training.

If your solution version has a status of CREATE_PENDING or CREATE_IN_PROGRESS, you can use the
[StopSolutionVersionCreation](API_StopSolutionVersionCreation.md "API_StopSolutionVersionCreation.md") operation to stop the solution version creation process.
See [Stopping the creation of a solution version](stop-solution-version.md "stop-solution-version.md").

When the solution version is ACTIVE, you are ready to use it to get recommendations. How you use an active solution version depends on how you get recommendations:

- For real-time recommendations, you deploy an ACTIVE solution version with an Amazon Personalize campaign. You use the campaign to get recommendations for your users.
  See [Deploying an Amazon Personalize solution version with a campaign](campaigns.md "campaigns.md").
- For batch recommendations, you specify an ACTIVE solution version when you create a batch inference job or batch
  segment job. See [Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md") or [Getting batch user segments](getting-user-segments.md "getting-user-segments.md").

## Creating a solution version (AWS SDKs)

When your solution is ACTIVE, use the following code to create a solution version. Specify the Amazon Resource Name (ARN) from
[Configuring a custom solution in Amazon Personalize](customizing-solution-config.md "customizing-solution-config.md"). Use the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md") operation to retrieve the solution version's status.

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')
# Store the solution ARN
solution_arn = '`solution arn`'

# Use the solution ARN to get the solution status.
solution_description = personalize.describe_solution(solutionArn = 'solution_arn')['solution']
print('Solution status: ' + solution_description['status'])

# Use the solution ARN to create a solution version.
print ('Creating solution version')
response = personalize.create_solution_version(solutionArn = solution_arn)
solution_version_arn = response['solutionVersionArn']
print('Solution version ARN: ' + solution_version_arn)

# Use the solution version ARN to get the solution version status.
solution_version_description = personalize.describe_solution_version(
    solutionVersionArn = solution_version_arn)['solutionVersion']
print('Solution version status: ' + solution_version_description['status'])

```

SDK for Java 2.x

```
public static String createPersonalizeSolutionVersion(PersonalizeClient personalizeClient, String solutionArn) {
        long maxTime = 0;
        long waitInMilliseconds = 30 * 1000; // 30 seconds
        String solutionStatus = "";
        String solutionVersionStatus = "";
        String solutionVersionArn = "";

        try {
            DescribeSolutionRequest describeSolutionRequest = DescribeSolutionRequest.builder()
                .solutionArn(solutionArn)
                .build();

            maxTime = Instant.now().getEpochSecond() + 3 * 60 * 60;

            // Wait until solution is active.
            while (Instant.now().getEpochSecond() < maxTime) {

                solutionStatus = personalizeClient.describeSolution(describeSolutionRequest).solution().status();
                System.out.println("Solution status: " + solutionStatus);

                if (solutionStatus.equals("ACTIVE") || solutionStatus.equals("CREATE FAILED")) {
                    break;
                }
                try {
                    Thread.sleep(waitInMilliseconds);
                } catch (InterruptedException e) {
                    System.out.println(e.getMessage());
                }
            }

            // Once the solution is active, start creating a solution version.

            if (solutionStatus.equals("ACTIVE")) {

                CreateSolutionVersionRequest createSolutionVersionRequest = CreateSolutionVersionRequest.builder()
                    .solutionArn(solutionArn)
                    .build();

                CreateSolutionVersionResponse createSolutionVersionResponse = personalizeClient.createSolutionVersion(createSolutionVersionRequest);
                solutionVersionArn = createSolutionVersionResponse.solutionVersionArn();

                System.out.println("Solution version ARN: " + solutionVersionArn);

                DescribeSolutionVersionRequest describeSolutionVersionRequest = DescribeSolutionVersionRequest.builder()
                    .solutionVersionArn(solutionVersionArn)
                    .build();

                maxTime = Instant.now().getEpochSecond() + 3 * 60 * 60;

                while (Instant.now().getEpochSecond() < maxTime) {

                    // Use the solution version ARN to get the solution version status.
                    solutionVersionStatus = personalizeClient.describeSolutionVersion(describeSolutionVersionRequest).solutionVersion().status();
                    System.out.println("Solution version status: " + solutionVersionStatus);

                    if (solutionVersionStatus.equals("ACTIVE") || solutionVersionStatus.equals("CREATE FAILED")) {
                        break;
                    }
                    try {
                        Thread.sleep(waitInMilliseconds);
                    } catch (InterruptedException e) {
                        System.out.println(e.getMessage());
                    }
                }
                return solutionVersionArn;
            }
        } catch(PersonalizeException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return "";
    }


```

SDK for JavaScript v3

```
// Get service clients module and commands using ES6 syntax.
import { CreateSolutionVersionCommand } from "@aws-sdk/client-personalize";
import { personalizeClient } from "./libs/personalizeClients.js";
// Or, create the client here.
// const personalizeClient = new PersonalizeClient({ region: "REGION"});

// Set the solution version parameters.
export const solutionVersionParam = {
  solutionArn: "SOLUTION_ARN" /* required */,
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new CreateSolutionVersionCommand(solutionVersionParam),
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```

To check the current solution version status, call the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md") operation
and pass the ARN of the solution version returned from the `CreateSolutionVersion`
operation. Training is complete when the `status` is `ACTIVE` and you can evaluate it using metrics supplied by Amazon Personalize.
For more information, see [Evaluating an Amazon Personalize solution version with metrics](working-with-training-metrics.md "working-with-training-metrics.md"). If training does not complete because of an error, you are not charged for the training.

If your solution version has a status of CREATE_PENDING or CREATE_IN_PROGRESS, you can use the
[StopSolutionVersionCreation](API_StopSolutionVersionCreation.md "API_StopSolutionVersionCreation.md") operation to stop the solution version creation process.
See [Stopping the creation of a solution version](stop-solution-version.md "stop-solution-version.md").

When the solution version is ACTIVE, you are ready to use it to get recommendations. How you use an active solution version depends on how you get recommendations:

- For real-time recommendations, you deploy an ACTIVE solution version with an Amazon Personalize campaign. You use the campaign to get recommendations for your users.
  See [Deploying an Amazon Personalize solution version with a campaign](campaigns.md "campaigns.md").
- For batch recommendations, you specify an ACTIVE solution version when you create a batch inference job or batch
  segment job. See [Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md") or [Getting batch user segments](getting-user-segments.md "getting-user-segments.md").
