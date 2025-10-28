# Updating a solution to change its automatic training configuration

After you create a solution, you can change its automatic training configuration and its events configuration:

- You can turn automatic training on or off, and you can change the training frequency.
  - If you turn on automatic training, the first automatic training starts within one hour after
    the solution update completes. If you manually create a solution version within the hour, the
    solution skips the first automatic training.
  - If you modify the solution’s training frequency, the training schedule resets and a new
    solution version starts training within the hour. Solution version creation continues at the new
    frequency, where day 1 is the day you update the solution.

- You can update the solutions events configuration. If the solution already has an events configuration specified, the new events config will replace the original one.
  For information about optimizing a solution for an event configuration, see [Optimizing a solution with events configuration](optimizing-solution-events-config.md "optimizing-solution-events-config.md").
  You can update a solution with the Amazon Personalize console, AWS Command Line Interface, or AWS SDKs. Solution updates can take a few minutes.
  While the update is in progress, you can create solution versions for the solution but you can't delete the solution. Until the update completes, the solution uses the previous configuration.
  For more information about automatic training, see [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md").

###### Topics

- [Updating a solution (console)](#update-solution-console "#update-solution-console")
- [Updating a solution (AWS CLI)](#update-solution-cli "#update-solution-cli")
- [Updating a solution (AWS SDKs)](#update-solution-sdk "#update-solution-sdk")

## Updating a solution (console)

To update a solution in the console, navigate to the solution, choose update, and specify the new configuration to use.

###### To configure a solution

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home"), and sign in to your account.
2. On the **Dataset groups** page, choose your dataset group.
3. In the navigation pane, choose **Custom resources** and choose **Solutions and recipes**.
4. Choose your solution and choose **Update** in the top right.
5. In **Automatic training**, modify whether the solution uses automatic training. If automatic training is on,
   you can change the `Automatic training frequency`. The default training frequency is
   every 7 days.
6. Choose **Update solution**. You can find the status of the solution update on
   the details page of your solution.

## Updating a solution (AWS CLI)

To update a solution with the AWS Command Line Interface, use the `update-solution` command. This command uses the [UpdateSolution](API_UpdateSolution.md "API_UpdateSolution.md")
API operation. The following code shows you how to update a solution to use automatic training with a training frequency of
5 days. To turn off auto training, specify `--no-perform-auto-training` and omit the `solution-update-config`.

The default training frequency is
every 7 days. The expression must be in `rate(*value*
*unit*)` format. For the value, specify a number between 1 and 30. For the unit, specify
`day` or `days`.

```
aws personalize update-solution \
--solution-arn `solution ARN` \
--perform-auto-training \
--solution-update-config "{\"autoTrainingConfig\": {\"schedulingExpression\": \"rate(5 days)\"}}"
```

To get the status of the update, use the `describe-solution` command (which uses the
[DescribeSolution](API_DescribeSolution.md "API_DescribeSolution.md") API operation) and find the update status in the
`latestSolutionUpdate`.

## Updating a solution (AWS SDKs)

To update a solution with the AWS SDKs, use the [UpdateSolution](API_UpdateSolution.md "API_UpdateSolution.md") API operation. The following code shows you how to use the SDK for Python (Boto3) to update a solution to use automatic training with
a training frequency of 5 days. The code gets the status of the update with the
[DescribeSolution](API_DescribeSolution.md "API_DescribeSolution.md") API operation.

The default training frequency is
every 7 days. The expression must be in `rate(*value*
*unit*)` format. For the value, specify a number between 1 and 30. For the unit, specify
`day` or `days`.

```
import boto3

personalize = boto3.client('personalize')

update_solution_response = personalize.update_solution(
    solutionArn='`SOLUTION ARN`',
    performAutoTraining=True,
    solutionUpdateConfig={
        "autoTrainingConfig": {
            "schedulingExpression": "rate(5 days)"
        }
    }
)
describe_solution_response = personalize.describe_solution(
    solutionArn='`SOLUTION ARN`'
)
update_status = describe_solution_response["solution"]["latestSolutionUpdate"]["status"]
print(f"Update status: {update_status}")
```
