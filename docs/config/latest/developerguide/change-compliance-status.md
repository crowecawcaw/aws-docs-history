# Change Compliance Status of a Process

Check

You can change the compliance status of a process check using the AWS Config console, the AWS CLI, and APIs.

Change Compliance Status for Process Checks (Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Navigate to the AWS Config Rules page.
3. Choose the name of the process check that you specified in the template
   along with the identifier in the conformance pack.

###### Note

All the process checks from the same conformance pack have the same
suffix. 4. On the Rule details page, you cannot edit the rule but you can edit the
compliance of the rule. In the Manual compliance section, choose
**Edit compliance**. 5. Choose the appropriate compliance from the dropdown list. 6. (Optional) Enter a description for the compliance status. 7. Choose **Save**.

Change the Compliance Status for Process
Checks (AWS CLI)
You can update the compliance of process checks within a conformance pack using
the AWS Command Line Interface (AWS CLI).

To install the AWS CLI on your local machine, see [Installing the
AWS CLI](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md") in the _AWS CLI User Guide_.

If necessary, type `AWS Configure` to configure the AWS CLI to use an AWS
Region where AWS Config conformance packs are available.

1. Open a command prompt or a terminal window.
2. Enter the following command to update the compliance of a process check
   where `ComplianceResourceId` is your `Account ID`, and
   include the name of your rule.

```
aws configservice put-external-evaluation --config-rule-name process-check-rule-name  --external-evaluation ComplianceResourceType=AWS::::Account,ComplianceResourceId=`Account ID`,ComplianceType=NON_COMPLIANT,OrderingTimestamp=2020-12-17T00:10:00.000Z
```

3. Press Enter to run the command.

Change the Compliance Status for Process
Checks (API)
After the deployment is complete, to update the evaluations and compliance of the
process checks, use the `PutExternalEvaluation` API. For more
information, see [PutExternalEvaluation](../APIReference/API_PutExternalEvaluation.md "../APIReference/API_PutExternalEvaluation.md").
