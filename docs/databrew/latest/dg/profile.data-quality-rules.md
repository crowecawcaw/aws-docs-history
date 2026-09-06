

# Validating data quality in AWS Glue DataBrew
<a name="profile.data-quality-rules"></a>

To ensure the quality of your datasets, you can define a list of data quality rules in a ruleset. A *ruleset* is a set of rules that compare different data metrics against expected values. If any of a rule's criteria isn't met, the ruleset as a whole fails validation. You can then inspect individual results for each rule. For any rule that causes a validation failure, you can make the necessary corrections and revalidate.

Examples of rules include the following: 
+ Value in column `"APY"` is between 0 and 100
+ Number of missing values in column `group_name` doesn't exceed 5%

You can define each rule for an individual column or independently apply it to several selected columns, for example:
+ Max value doesn’t exceed 100 for columns `"rate"`, `"pay"`, `"increase"`.

A rule can consist of multiple simple checks. You can define whether all of them should be true or any, for example:
+ Value in column `"ProductId"` should start with `"asin-"` AND length of value in column `"ProductId"` is 32. 

You can verify rules against either aggregate values such as `max`, `min`, or `number of duplicate values` where there is only one value being compared, or nonaggregate values in each row of a column. In the latter case, you can also define a "passing" threshold such as `value in columnA > value in columnB for at least 95% of rows`.

 As with profile information, you can define column-level data quality rules only for columns of simple types, such as strings and numbers. You can't define data quality rules for columns of complex types, such as arrays or structures. For more details about working with profile information, see [Creating and working with AWS Glue DataBrew profile jobs](jobs.profile.md).

## Validating data quality rules
<a name="profile.data-quality-rules-validating"></a>

After a ruleset is defined, you can add it to a profile job for validation. You can define more than one ruleset for a dataset. 

For example, one ruleset might contain rules with minimally acceptable criteria. A validation failure for that ruleset might mean that the data isn't acceptable for further use. An example is missing values in key columns of a dataset used for machine learning training. You can use a second ruleset with stricter rules to verify whether the dataset has such good quality that no cleanup is required. 

You can apply one or more rulesets defined for a given dataset in a profile job configuration. When the profile job runs, it produces a validation report in addition to the data profile. The validation report is available at the same location as your profile data. As with profile information, you can explore the results in the DataBrew console. In the **Dataset details** view, choose the **Data Quality** tab to view the results. For more details about working with profile information, see [Creating and working with AWS Glue DataBrew profile jobs](jobs.profile.md). 

## Acting on validation results
<a name="profile.data-quality-rules-results-acting"></a>

When a DataBrew profile job completes, DataBrew sends an Amazon CloudWatch event with the details of that job run. If you also configured your job to validate data quality rules, DataBrew sends an event for each validated ruleset. The event contains its result (`SUCCEEDED`, `FAILED`, or `ERROR`) and a link to the detailed data quality validation report. You can then automate further action by invoking **next action** depending on the status of validation. For more information on connecting events to target actions, such as Amazon SNS notification, AWS Lambda function invocations and others, see [Getting started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-getting-set-up.html). 

 Following is an example of a DataBrew Validation Result event:

```
{
  "version": "0",
  "id": "fb27348b-112d-e7c2-560d-85e7c2c09964",
  "detail-type": "DataBrew Ruleset Validation Result",   
  "source": "aws.databrew",                     
  "account": "123456789012",          
  "time": "2021-11-18T13:15:46Z", 
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "datasetName": "MyDataset", 
    "jobName": "MyProfileJob",
    "jobRunId": "db_f07954d20d083de0c1fc1eee11498d8635ee5be4ca416af27d33933e91ff4e6e",
    "rulesetName": "MyRuleset",
    "validationState": "FAILED",
    "validationReportLocation": "s3://MyBucket/MyKey/MyDataset_f07954d20d083de0c1fc1eee11498d8635ee5be4ca416af27d33933e91ff4e6e_dq-validation-report.json"
  }
}
```

You can use attributes of events such as `detail-type`, `source` and nested properties of the `detail` attribute to [create event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in Amazon Eventbridge. For example an event pattern to match all failed validations from any DataBrew job would look like this:

```
{
  "source": ["aws.databrew"],
  "detail-type": ["DataBrew Ruleset Validation Result"],
  "detail": {
   "validationState": ["FAILED"]
  }
}
```

For an example of creating a ruleset and validating its rules, see [Creating a ruleset with data quality rules](profile.data-quality-rules-create.md). For more information about working with CloudWatch events in DataBrew, see [Automating DataBrew with CloudWatch Events](monitoring.cloudwatch-events.md) 

## Inspecting validation results for and updating data quality rules
<a name="profile.data-quality-ruleset-inspect-results"></a>

After your profile job completes, you can view the validation results for your data quality rules and as needed update your rules. 

**To view validation data for your data quality rules**

1. On the DataBrew console, choose **View data profile**. Doing this displays the **Data profile overview** tab for your dataset.

1. Choose the **Data quality rules** tab. On this tab, you can view the results for all of your data quality rules.

1. Select an individual rule for more details about that rule. 

For any rule that failed validation, you can make the necessary corrections.

**To update your data quality rules**

1. On the navigation pane, choose **DQ RULES**.

1. Under **Data quality ruleset name**, choose the dataset that contains the rules that you plan to edit.

1. Choose the rule that you want to change, and then choose **Edit**.

1. Make the necessary corrections, and then choose **Update ruleset**.

1. Rerun the job. Repeat this process until all validations pass.