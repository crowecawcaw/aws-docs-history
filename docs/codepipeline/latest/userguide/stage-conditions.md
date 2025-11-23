# Configure conditions for a stage

You can specify a condition for a stage, such as checking for a specific variable in the
pipeline run, and then engage a result for the condition, such as skipping the stage or
failing the stage. A pipeline can be set up to check for stage conditions during the run,
where you specify checks for a stage and then specify how the stage should continue when
certain conditions are met. Conditions contain one or more rules that are available in a
list of rules in CodePipeline. If all rules in a condition succeed, then the condition is
met. You can configure conditions so that when the criteria are not met, the specified
result engages.

Each condition has a rule set which is an ordered set of rules that are evaluated
together. Therefore, if one rule fails in the condition, then the condition fails. You can
override rule conditions at pipeline runtime.

Conditions are used for specific types of expressions and each has specific options for
results available as follows:

- **Entry** - The conditions for making checks that, if
  met, allow entry to a stage. Rules are engaged with the following result options:
  **Fail** or **Skip**
- **On Failure** - The conditions for making checks for
  the stage when it fails. Rules are engaged with the following result option:
  **Rollback**
- **On Success** - The conditions for making checks for
  the stage when it succeeds. Rules are engaged with the following result options:
  **Rollback** or **Fail**
  Conditions are supported by a set of _rules_ for each
  type of condition.

For each type of condition, there are specific actions that are set up by the condition.
The action is the result of the succeeded or failed condition check. For example, the
condition for entry (entry condition) encounters an alarm (rule), then the check is
successful and the result (action) is that the stage entry is blocked.

You can also use the AWS CodePipeline console or the AWS CLI to manually roll back or retry a stage
or actions in a stage. See Configure conditions for a stage.

###### Topics

- [Use cases for stage conditions](#stage-conditions-cases "#stage-conditions-cases")
- [Considerations for results configured
  for stage conditions](#stage-conditions-considerations "#stage-conditions-considerations")
- [Considerations for rules
  configured for stage conditions](#stage-conditions-considerations-rules "#stage-conditions-considerations-rules")
- [Creating Entry conditions](#stage-conditions-entry "#stage-conditions-entry")
- [Creating On Failure conditions](#stage-conditions-onfailure "#stage-conditions-onfailure")
- [Creating On Success conditions](#stage-conditions-onsuccess "#stage-conditions-onsuccess")
- [Deleting stage conditions](#stage-conditions-delete "#stage-conditions-delete")
- [Overriding stage conditions](#stage-conditions-override "#stage-conditions-override")

## Use cases for stage conditions

Stage conditions have multiple use cases for setting up release and change safety in
pipelines. The following are sample use cases for stage conditions.

- Use an Entry condition to define a condition that will check the CloudWatch
  alarm state, which will then block a change if the production environment is not
  in a healthy state.
- Use an Entry condition with a wait time of 60 to define a condition to be
  evaluated when all the actions in a stage have successfully completed, and then
  roll back the changes if a CloudWatch alarm goes into ALARM state within 60
  minutes.
- Use an On Success condition to define a condition so that when the stage
  completes successfully, the rule will check whether the current time is in the
  deployment window and then deploy if the rule succeeds.

## Considerations for results configured

for stage conditions

Considerations for stage conditions are as follows:

- You cannot use automatic stage retry with onFailure conditions.
- When configuring a condition with a **Rollback** result, the
  stage can only roll back to a previous execution if available in the current
  pipeline structure version.
- When configuring a condition with a **Rollback** result, you
  cannot roll back to a target execution ID that is a rollback execution
  type.
- For Entry conditions that use the **Skip** result to skip the
  stage if the condition fails, only the `LambdaInvoke` and
  `VariableCheck` rules are supported.
- You cannot perform a manual stage retry on a stage in
  **Skipped** status.
- You cannot perform a manual rollback to a stage in
  **Skipped** status.
- You cannot override a condition if the condition is configured with a
  **Skip** result.
- With the exception of **Skip** results, you can override a
  stage condition when starting a pipeline execution. For a stage condition where
  an override is engaged, the execution will perform as detailed in the following
  table.
- | Type      | Configured result on condition failure | Stage status | Override behavior    |
  | --------- | -------------------------------------- | ------------ | -------------------- |
  | Entry     | Fail                                   | In-progress  | The stage proceeds.  |
  | Entry     | Skip                                   | Skipped      | Not applicable.      |
  | OnFailure | Rollback                               | Failed       | The stage is failed. |
  | OnSuccess | Rollback                               | Succeeded    | The stage proceeds.  |
  | OnSuccess | Fail                                   | Failed       | The stage proceeds.  |

## Considerations for rules

configured for stage conditions

Considerations for the available rules for stage conditions are as follows:

- For the `LambdaInvoke` rule, you must first configure the Lambda
  function to be used in the rule. Have the Lambda function ARN ready to provide
  when you configure the rule.
- For the `CloudWatchAlarm` rule, you must first configure the CloudWatch Events
  event to be used in the rule. Have the event ARN ready to provide when you
  configure the rule.

## Creating Entry conditions

You can configure Entry conditions for a stage using the console or CLI. You will
configure the corresponding rules and results for each condition. For a rollback result,
the pipeline can only roll back to a previous execution if the previous execution was
started in the current pipeline structure version.

The steps provide an example Entry condition that uses a monitor rule.

For more information, see [Condition](../APIReference/API_Condition.md "../APIReference/API_Condition.md"), [RuleTypeId](../APIReference/API_RuleTypeId.md "../APIReference/API_RuleTypeId.md"), and [RuleExecution](../APIReference/API_RuleExecution.md "../APIReference/API_RuleExecution.md") in the _CodePipeline API
Guide_.

### Creating Entry conditions -

CloudWatchAlarm rule example (Console)

You can configure Entry conditions for a stage, along with the rules and results
you want the stage to perform when the conditions are met.

###### Configure an Entry condition (console)

1. Complete any prerequisites, such as creating the resource and ARN for a
   rule where a resource is provided, such as the **AWS
   CloudWatchAlarm**.
2. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home "http://console.aws.amazon.com/codesuite/codepipeline/home").

The names and status of all pipelines associated with your AWS account
are displayed. 3. In **Name**, choose the name of the pipeline you want to
edit. 4. On the pipeline details page, choose **Edit**. 5. On the **Edit** page, for the action you want to edit,
choose **Edit stage**. 6. Choose **Add entry condition**. The **Before
stage entry condition** card displays with the
**Fail** option available for this condition. 7. Choose **Add rule**, and then complete the
following.

    1. In **Rule name**, enter a name for your rule. For
     this example, enter `MyAlarmRule`.
    2. In **Rule provider**, choose the preconfigured
     rule provider to add to your condition. For this example, choose
     **AWS CloudWatchAlarm**, and then complete
     the following steps.
    3. In **Region**, choose the Region for your
     condition or leave the default.
    4. In **Alarm name**, choose the CloudWatch resource
     to use for the rule. You must have already created the resource in
     your account.
    5. (Optional) In **Wait time**, enter the amount of
     time CodePipeline will wait if the alarm is in ALARM state when it
     is first evaluated. If the alarm is OK state when the rule is first
     checked, the rule will immediately succeed.
    6. (Optional) Enter any specific alarm states to monitor, and enter
     the role ARN if appropriate.
    7. When you are done editing the stage, choose
     **Done**. On the pipeline edit page, choose
     **Save**.

8. After the run, view the result.

### Creating Entry conditions with Skip

result and `VariableCheck` rule (console)

You can configure Entry conditions for a stage so that if the entry condition is
not met, the stage is skipped If the condition fails, then the result engages and
the stage is skipped. When a stage is skipped, the stage status is
**Skipped**, and the action status is **Didn't
Run**. For considerations for stage conditions with Skip results, see
[Considerations for results configured
for stage conditions](#stage-conditions-considerations "#stage-conditions-considerations").

In the following example, the variable check rule finds that the value is not a
match, and the build stage is skipped.

###### Configure an Entry condition with a **Skip** result

(console)

1. Complete any prerequisites, such as creating the resource and ARN for a
   rule where a resource is provided, such as the **AWS
   CloudWatchAlarm**.
2. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home "http://console.aws.amazon.com/codesuite/codepipeline/home").

The names and status of all pipelines associated with your AWS account
are displayed. 3. In **Name**, choose the name of the pipeline you want to
edit. 4. On the pipeline details page, choose **Edit**. 5. On the **Edit** page, for the action you want to edit,
choose **Edit stage**. 6. Choose **Add entry condition**, and then choose
**Skip** as the result. 7. Choose **Add rule**, and then complete the
following.

    1. In **Rule name**, enter a name for your rule. For
     this example, enter `MyAlarmRule`.
    2. In **Rule provider**, choose the preconfigured
     rule provider to add to your condition. For this example, choose
     **VariableCheck**, and then
     complete the following steps.



    ![An example release process using CodePipeline.](images/stage-cond-fail-skip.png)
    3. In **Region**, choose the Region for your
     condition or leave the default.
    4. In **Variable**, choose the variable to compare
     with, such as `#{SourceVariables.FullRepositoryName}` for
     a pipeline that has a GitHub (via GitHub App) source action. Enter the
     repository name and choose the operator, such as **Equals**.
    5. When you are done editing the stage, choose
     **Done**. On the pipeline edit page, choose
     **Save**.

8. After the run, view the result.

![An example release process using CodePipeline.](images/stage-skipped.png) 9. To review details, choose **Review**. The detail in the
following example shows that the configured result for the condition is
**Skip**, which cannot be overridden. The
rule status is **Failed** due to the condition
not being met.

![An example condition details page showing the Skip result condition in CodePipeline.](images/condition-exec-details.png)

### Creating Entry conditions (CLI)

To use the AWS CLI to configure an Entry condition, use the commands to create or
update a pipeline as detailed in [Create a pipeline, stages, and actions](pipelines-create.md "pipelines-create.md") and [Edit a pipeline in CodePipeline](pipelines-edit.md "pipelines-edit.md").

###### Configure the condition and rule or rules (CLI)

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI
  to run the `update-pipeline` command, specifying the failure
  condition in the pipeline structure. The following example configures an
  Entry condition for a staged named `Deploy`:

```
{
    "name": "Deploy",
    "actions": [
        {
            "name": "Deploy",
            "actionTypeId": {
                "category": "Deploy",
                "owner": "AWS",
                "provider": "S3",
                "version": "1"
            },
            "runOrder": 1,
            "configuration": {
                "BucketName": "MyBucket",
                "Extract": "false",
                "ObjectKey": "object.xml"
            },
            "outputArtifacts": [],
            "inputArtifacts": [
                {
                    "name": "SourceArtifact"
                }
            ],
            "region": "us-east-1",
            "namespace": "DeployVariables"
        }
    ],
    `"beforeEntry": {
 "conditions": [
 {
 "result": "FAIL",
 "rules": [
 {
 "name": "MyAlarmRule",
 "ruleTypeId": {
 "category": "Rule",
 "owner": "AWS",
 "provider": "CloudWatchAlarm",
 "version": "1"
 },
 "configuration": {
 "AlarmName": "CWAlarm",
 "WaitTime": "1"
 },
 "inputArtifacts": [],
 "region": "us-east-1"
 }
 ]
 }
 ]
 }`
}
```

For more information about configuring success conditions for stage
rollback, see [SuccessConditions](../APIReference/API_SuccessConditions.md "../APIReference/API_SuccessConditions.md") in the _CodePipeline API
Reference_.

### Creating Entry conditions (CFN)

To use CloudFormation to configure an Entry condition, use the `beforeEntry`
parameter. On entry, the stage will run the rule and perform the result.

```
beforeEntry:
     Result: FAIL
```

- Update the template as shown in the following snippet. The following
  example configures an Entry condition with a rule named
  `MyMonitorRule`:

```
Name: Deploy
Actions:
- Name: Deploy
  ActionTypeId:
    Category: Deploy
    Owner: AWS
    Provider: S3
    Version: '1'
  RunOrder: 1
  Configuration:
    BucketName: MyBucket
    Extract: 'false'
    ObjectKey: object.xml
  OutputArtifacts: []
  InputArtifacts:
  - Name: SourceArtifact
  Region: us-east-1
  Namespace: DeployVariables
BeforeEntry:
  Conditions:
  - Result: FAIL
    Rules:
    - Name: MyMonitorRule
      RuleTypeId:
        Category: Rule
        Owner: AWS
        Provider: CloudWatchAlarm
        Version: '1'
      Configuration:
        AlarmName: CWAlarm
        WaitTime: '1'
      InputArtifacts: []
      Region: us-east-1
```

For more information about configuring beforeEntry conditions, see [AWS::CodePipeline::Pipeline BeforeEntryConditions](../../../AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-beforeentryconditions.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-beforeentryconditions.md") under
`StageDeclaration` in the _CloudFormation User
Guide_.

## Creating On Failure conditions

You can configure On Failure conditions for a stage using the console or CLI. You will
configure the corresponding rules and results for each condition. For a rollback result,
the pipeline can only roll back to a previous execution if the previous execution was
started in the current pipeline structure version.

### Creating On Failure conditions

(Console)

You can configure On Failure conditions for a stage, along with the rules and
results you want the stage to perform when the conditions are met.

###### Configure an On Failure condition (console)

1. Complete any prerequisites, such as creating the resource and ARN for a
   rule where a resource is provided, such as the
   **LambdaInvoke** rule.
2. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home "http://console.aws.amazon.com/codesuite/codepipeline/home").

The names and status of all pipelines associated with your AWS account
are displayed. 3. In **Name**, choose the name of the pipeline you want to
edit. 4. On the pipeline details page, choose **Edit**. 5. On the **Edit** page, for the action you want to edit,
choose **Edit stage**. 6. Choose **Add failure condition**. The **Failure
condition** card displays with the
**Rollback** option available for this
condition. 7. Choose **Add rule**, and then complete the
following.

    1. In **Rule name**, enter a name for your rule. For
     this example, enter `MyLambdaRule`.
    2. In **Rule provider**, choose the preconfigured
     rule provider to add to your condition. For this example, choose
     **AWS LambdaInvoke**, and then complete the
     following steps.
    3. In **Region**, choose the Region for your
     condition or leave the default.
    4. In **Input artifacts**, choose the source
     artifact.
    5. In **Function name**, choose the Lambda resource
     to use for the rule. You must have already created the resource in
     your account.
    6. (Optional) In **User parameters**, enter any
     pairs that represent parameters for additional configuration.
    7. (Optional) In **Role Arn**, enter the role ARN if
     configured.
    8. (Optional) In **Timeout in Minutes**, enter the
     time in minutes that the rule should wait before timeout.
    9. When you are done editing the stage, choose
     **Done**. On the pipeline edit page, choose
     **Save**.

### Creating onFailure conditions with a Retry result example (Console)

You can configure onFailure conditions for a stage so that if the entry condition
is not met, the stage is retried. As part of this result, you configure the retry
mode, specifying whether to retry the failed actions or to retry the failed
stage.

###### Configure an onFailure condition with a Retry result (console)

1. Complete any prerequisites, such as creating the resource and ARN for a
   rule where a resource is provided, such as the **AWS
   CloudWatchAlarm**.
2. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home "http://console.aws.amazon.com/codesuite/codepipeline/home").

The names and status of all pipelines associated with your AWS account
are displayed. 3. In **Name**, choose the name of the pipeline you want to
edit. 4. On the pipeline details page, choose **Edit**. 5. On the **Edit** page, for the action you want to edit,
choose **Edit stage**. 6. At the bottom of the stage, under **Automated stage
configuration:**, choose **Enable automatic retry on
stage failure**. In **Retry mode**, choose
either **Retry failed stage** or **Retry failed
actions**.

![Configuring retry mode for a stage in CodePipeline.](images/stage-retry-mode.png) 7. Choose to add an onFailure condition and then choose **Add
rule** and enter a rule for the condition.

    1. In **Rule name**, enter a name for your rule. For
     this example, enter `MyAlarmRule`.
    2. In **Rule provider**, choose the preconfigured
     rule provider to add to your condition. For this example, choose
     **CloudWatchAlarm**, and then
     complete the following steps.
    3. In **Region**, choose the Region for your
     condition or leave the default.
    4. In **Alarm Name**, choose the configured resource
     for the alert.
    5. When you are done editing the stage, choose
     **Done**. On the pipeline edit page, choose
     **Save**.

8. After the run, view the result.

### Creating On Failure conditions

(CLI)

To use the AWS CLI to configure an On Failure condition, use the commands to create
or update a pipeline as detailed in [Create a pipeline, stages, and actions](pipelines-create.md "pipelines-create.md") and [Edit a pipeline in CodePipeline](pipelines-edit.md "pipelines-edit.md").

###### Configure the condition and rule or rules (CLI)

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI
  to run the `update-pipeline` command, specifying the failure
  condition in the pipeline structure. The following example configures an On
  Failure condition for a staged named `Deploy`:

```
{
    "name": "Deploy",
    "actions": [
        {
            "name": "Deploy",
            "actionTypeId": {
                "category": "Deploy",
                "owner": "AWS",
                "provider": "S3",
                "version": "1"
            },
            "runOrder": 1,
            "configuration": {
                "BucketName": "MyBucket",
                "Extract": "false",
                "ObjectKey": "object.xml"
            },
            "outputArtifacts": [],
            "inputArtifacts": [
                {
                    "name": "SourceArtifact"
                }
            ],
            "region": "us-east-1",
            "namespace": "DeployVariables"
        }
    ],
    `"onFailure": {
 "conditions": [
 {
 "result": "ROLLBACK",
 "rules": [
 {
 "name": "MyLambdaRule",
 "ruleTypeId": {
 "category": "Rule",
 "owner": "AWS",
 "provider": "LambdaInvoke",
 "version": "1"
 },
 "configuration": {
 "FunctionName": "my-function"
 },
 "inputArtifacts": [
 {
 "name": "SourceArtifact"
 }
 ],
 "region": "us-east-1"
 }
 ]
 }
 ]
 }`
}
```

For more information about configuring failure conditions, see [FailureConditions](../APIReference/API_FailureConditions.md "../APIReference/API_FailureConditions.md") in the _CodePipeline API
Reference_.

### Creating On Failure conditions

(CFN)

To use CloudFormation to configure an On Failure condition, use the `OnFailure`
parameter. On success, the stage will run the rule and perform the result.

```
OnFailure:
     Result: ROLLBACK
```

- Update the template as shown in the following snippet. The following
  example configures an OnFailure condition with a rule named
  `MyMonitorRule`:

```
name: Deploy
actions:
- name: Deploy
  actionTypeId:
    category: Deploy
    owner: AWS
    provider: S3
    version: '1'
  runOrder: 1
  configuration:
    BucketName: MyBucket
    Extract: 'false'
    ObjectKey: object.xml
  outputArtifacts: []
  inputArtifacts:
  - name: SourceArtifact
  region: us-east-1
  namespace: DeployVariables
OnFailure:
  conditions:
  - result: ROLLBACK
    rules:
    - name: MyMonitorRule
      ruleTypeId:
        category: Rule
        owner: AWS
        provider: CloudWatchAlarm
        version: '1'
      configuration:
        AlarmName: AlarmOnHelloWorldInvocation
        AlarmStates: ALARM
        WaitTime: '1'
      inputArtifacts: []
      region: us-east-1

```

For more information about configuring failure conditions, see [OnFailure](../../../AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stagedeclaration.md#cfn-codepipeline-pipeline-stagedeclaration-onfailure "../../../AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stagedeclaration.md#cfn-codepipeline-pipeline-stagedeclaration-onfailure") under `StageDeclaration` in the _CloudFormation User Guide_.

## Creating On Success conditions

You can configure On Success conditions for a stage using the console or CLI. You will
configure the corresponding rules and results for each condition. For a rollback result,
the pipeline can only roll back to a previous execution if the previous execution was
started in the current pipeline structure version.

The steps provide an example On Success condition that uses a deployment window
rule.

For more information, see [Condition](../APIReference/API_Condition.md "../APIReference/API_Condition.md"), [RuleTypeId](../APIReference/API_RuleTypeId.md "../APIReference/API_RuleTypeId.md"), and [RuleExecution](../APIReference/API_RuleExecution.md "../APIReference/API_RuleExecution.md") in the _CodePipeline API
Guide_.

### Creating On Success conditions

(Console)

You can configure On Success conditions for a stage, along with the rules and
results you want the stage to perform when the conditions are met.

###### Configure an On Success condition (console)

1. Complete any prerequisites, such as creating the resource and ARN for a
   rule where a resource is provided, such as the AWS LambdaRule.
2. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home "http://console.aws.amazon.com/codesuite/codepipeline/home").

The names and status of all pipelines associated with your AWS account
are displayed. 3. In **Name**, choose the name of the pipeline you want to
edit. 4. On the pipeline details page, choose **Edit**. 5. On the **Edit** page, for the action you want to edit,
choose **Edit stage**. 6. Choose **Add success condition**. The **On stage
success condition** card displays. Choose the
**Rollback** or **Fail** option shown
as the available results for this condition type. 7. Choose **Add rule**, and then complete the
following.

    1. In **Rule name**, enter a name for your
     condition. For this example, enter
     `MyDeploymentRule`.
    2. In **Rule provider**, choose the preconfigured
     rule to add to your condition. For this example, choose
     **AWS DeploymentWindow**, and then complete
     the following steps.
    3. In **Region**, choose the Region for your
     condition or leave the default.
    4. In **Cron**, enter the cron expression for the
     deployment window. The cron expression defines the days and times
     when the deployment should be allowed. For reference information
     about cron expressions, see [Using cron and rate expressions to schedule
     rules](../../../eventbridge/latest/userguide/eb-scheduled-rule-pattern.md#eb-cron-expressions "../../../eventbridge/latest/userguide/eb-scheduled-rule-pattern.md#eb-cron-expressions").
    5. (Optional) In **TimeZone**, enter the time zone
     for the deployment window.

8. After the run, view the result.

![An example condition in CodePipeline.](images/stage-condition-onsuccess-deplwin-example-message.png)

### Creating On Success conditions

(CLI)

To use the AWS CLI to configure an On Success condition, use the commands to create
or update a pipeline as detailed in [Create a pipeline, stages, and actions](pipelines-create.md "pipelines-create.md") and [Edit a pipeline in CodePipeline](pipelines-edit.md "pipelines-edit.md").

###### Configure the condition and rule or rules (CLI)

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI
  to run the `update-pipeline` command, specifying the failure
  condition in the pipeline structure. The following example configures an On
  Success condition for a staged named `Deploy`, where the rule is
  named `MyDeploymentRule`:

```
{
    "name": "Deploy",
    "actions": [
        {
            "name": "Deploy",
            "actionTypeId": {
                "category": "Deploy",
                "owner": "AWS",
                "provider": "S3",
                "version": "1"
            },
            "runOrder": 1,
            "configuration": {
                "BucketName": "MyBucket",
                "Extract": "false",
                "ObjectKey": "object.xml"
            },
            "outputArtifacts": [],
            "inputArtifacts": [
                {
                    "name": "SourceArtifact"
                }
            ],
            "region": "us-east-1",
            "namespace": "DeployVariables"
        }
    ],
    `"onSuccess": {
 "conditions": [
 {
 "result": "FAIL",
 "rules": [
 {
 "name": "MyAlarmRule",
 "ruleTypeId": {
 "category": "Rule",
 "owner": "AWS",
 "provider": "CloudWatchAlarm",
 "version": "1"
 },
 "configuration": {
 "AlarmName": "CWAlarm",
 "WaitTime": "1"
 },
 "inputArtifacts": [],
 "region": "us-east-1"
 }
 ]
 }
 ]
 }
}`
```

For more information about configuring success conditions, see [SuccessConditions](../APIReference/API_SuccessConditions.md "../APIReference/API_SuccessConditions.md") in the _CodePipeline API
Reference_.

### Create an On Success condition

(CFN)

To use CloudFormation to configure an On Success condition, use the `OnSuccess`
parameter. On success, the stage will run the rule and perform the result.

```
OnSuccess:
     Result: ROLLBACK
```

- Update the template as shown in the following snippet. The following
  example configures an OnSuccess condition with a rule named
  `MyDeploymentWindowRule`:

```
name: Deploy
actions:
- name: Deploy
  actionTypeId:
    category: Deploy
    owner: AWS
    provider: S3
    version: '1'
  runOrder: 1
  configuration:
    BucketName: MyBucket
    Extract: 'false'
    ObjectKey: object.xml
  outputArtifacts: []
  inputArtifacts:
  - name: SourceArtifact
  region: us-east-1
  namespace: DeployVariables`onSuccess:
 conditions:
 - result: FAIL
 rules:
 - name: MyMonitorRule
 ruleTypeId:
 category: Rule
 owner: AWS
 provider: CloudWatchAlarm
 version: '1'
 configuration:
 AlarmName: CWAlarm
 WaitTime: '1'
 inputArtifacts: []
 region: us-east-1`
```

For more information about configuring failure conditions for stage
rollback, see [OnFailure](../../../AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stagedeclaration.md#cfn-codepipeline-pipeline-stagedeclaration-onfailure "../../../AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stagedeclaration.md#cfn-codepipeline-pipeline-stagedeclaration-onfailure") under `StageDeclaration` in the _CloudFormation User Guide_.

## Deleting stage conditions

You can delete stage conditions that have been configured for your pipeline.

###### To delete a stage condition

1. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home "http://console.aws.amazon.com/codesuite/codepipeline/home").

The names and status of all pipelines associated with your AWS account are
displayed. 2. In **Name**, choose the name of the pipeline you want to
edit. 3. On the pipeline details page, choose **Edit**. 4. On the **Edit** page, for the condition you want to edit,
choose **Edit stage**. 5. Next to the condition that you want to delete, choose **Delete
condition**.

## Overriding stage conditions

You can override stage conditions that have been configured for your pipeline. In the
console, when the stage and rule are running, you can choose to override the stage
condition. This results in the stage running

###### To override a stage condition

1. In this example, the pipeline stage is running with a condition. The
   **Override** button is enabled.

![An example condition in CodePipeline.](images/stage-condition-override-depl.png) 2. Next to the condition that you want to override, choose
**Override**.

![An example condition in CodePipeline.](images/stage-condition-override-depl-overridden.png) 3. To review details, choose **Review**. The detail in the
following example shows that the configured result for the condition is Fail,
which has been overridden. The rule status is Abandoned due to the
override.

![An example condition details page showing the overriden condition in CodePipeline.](images/stage-condition-onsuccess-deplwin-example-message-review.png)
