

# Working with Macie sample findings
<a name="findings-samples"></a>

To explore and learn about the different [types of findings](findings-types.md) that Amazon Macie can generate, you can create sample findings. Sample findings use example data and placeholder values to demonstrate the kinds of information that each type of finding might contain.

For example, the **Policy:IAMUser/S3BucketPublic** sample finding contains details about a fictitious Amazon Simple Storage Service (Amazon S3) bucket. The finding's details include example data about an actor and action that changed the access control list (ACL) for the bucket and made the bucket publicly accessible. Similarly, the **SensitiveData:S3Object/Multiple** sample finding contains details about a fictitious Microsoft Excel workbook. The finding's details include example data about the types and location of sensitive data in the workbook.

In addition to familiarizing yourself with the information that different types of findings might contain, you can use sample findings to test integration with other applications, services, and systems. Depending on the [suppression rules](findings-suppression.md) for your account, Macie can publish sample findings to Amazon EventBridge as events. The example data in these events can help you develop and test automated solutions for monitoring and processing findings with EventBridge. Depending on the [publication settings](findings-publish-frequency.md) for your account, Macie can also publish sample findings to AWS Security Hub CSPM. This means that you can also use sample findings to develop and test solutions for evaluating Macie findings with Security Hub CSPM. For information about publishing findings to these services, see [Monitoring and processing findings](findings-monitor.md).

**Topics**
+ [Creating sample findings](#findings-samples-create)
+ [Reviewing sample findings](#findings-samples-review)
+ [Suppressing sample findings](#findings-samples-suppress)

## Creating sample findings
<a name="findings-samples-create"></a>

You can create sample findings by using the Amazon Macie console or the Amazon Macie API. If you use the console, Macie automatically generates one sample finding for each type of finding that Macie supports. If you use the API, you can create a sample for each type, or only certain types that you specify.

------
#### [ Console ]

Follow these steps to create sample findings by using the Amazon Macie console.

**To create sample findings**

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/).

1. In the navigation pane, choose **Settings**.

1. Under **Sample findings**, choose **Generate sample findings**.

------
#### [ API ]

To create sample findings programmatically, use the [CreateSampleFindings](https://docs.aws.amazon.com/macie/latest/APIReference/findings-sample.html) operation of the Amazon Macie API. When you submit your request, optionally use the `findingTypes` parameter to specify only certain types of sample findings to create. To automatically create samples of all types, don't include this parameter in your request. 

To create sample findings by using the AWS Command Line Interface (AWS CLI), run the [create-sample-findings](https://docs.aws.amazon.com/cli/latest/reference/macie2/create-sample-findings.html) command. To automatically create samples of all types of findings, don't include the `finding-types` parameter. To create samples of only certain types of findings, include this parameter and specify the types of sample findings to create. For example:

```
C:\> aws macie2 create-sample-findings --finding-types "{{SensitiveData:S3Object/Multiple}}" "{{Policy:IAMUser/S3BucketPublic}}"
```

Where {{SensitiveData:S3Object/Multiple}} is a type of sensitive data finding to create and {{Policy:IAMUser/S3BucketPublic}} is a type of policy finding to create.

If the command runs successfully, Macie returns an empty response.

------

If you create sample findings again within 90 days, Macie generates a new finding for each type of sensitive data finding that you create. For policy findings, Macie updates each existing sample finding by incrementing the count of occurrences and updating details about when the subsequent occurrence occurred.

## Reviewing sample findings
<a name="findings-samples-review"></a>

To help you identify sample findings, Amazon Macie sets the value for the **Sample** field of each sample finding to *True*. In addition, the name of the affected S3 bucket is the same for all sample findings: *macie-sample-finding-bucket*. If you review sample findings by using **Findings** pages on the Amazon Macie console, Macie also displays the **[SAMPLE]** prefix in the **Finding type** field for each sample finding.

------
#### [ Console ]

Follow these steps to review sample findings by using the Amazon Macie console.

**To review sample findings**

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/).

1. In the navigation pane, choose **Findings**.

1. On the **Findings** page, do any of the following:
   + In the **Finding type** column, locate findings whose type begins with **[SAMPLE]**, as shown in the following image.  
![The Finding type column on the Findings page. It lists findings that have the [SAMPLE] prefix.](http://docs.aws.amazon.com/macie/latest/user/images/scrn-findings-samples-all.png)
   + By using the **Filter criteria** box above the table, filter the table to display only sample findings. To do this, place your cursor in the box. In the list of fields that appears, choose **Sample**. Then choose **True**, and then choose **Apply**.

1. To review the details of a specific sample finding, choose the finding. The details panel displays information for the finding.

You can also download and save the details of one or more sample findings as a JSON file. To do this, select the checkbox for each sample finding that you want to download and save. Then choose **Export (JSON)** on the **Actions** menu at the top of the **Findings** page. In the window that appears, choose **Download**. For detailed descriptions of the JSON fields that a finding can include, see [Findings](https://docs.aws.amazon.com/macie/latest/APIReference/findings-describe.html) in the *Amazon Macie API Reference*.

------
#### [ API ]

To review sample findings programmatically, first use the [ListFindings](https://docs.aws.amazon.com/macie/latest/APIReference/findings.html) operation of the Amazon Macie API to retrieve the unique identifier (`findingId`) for each sample finding that you created. Then use the [GetFindings](https://docs.aws.amazon.com/macie/latest/APIReference/findings-describe.html) operation to retrieve the details of those findings.

When you submit the **ListFindings** request, you can specify filter criteria to include only sample findings in the results. To do this, add a filter condition where the value for the `sample` field is `true`. If you're using the AWS CLI, run the [list-findings](https://docs.aws.amazon.com/cli/latest/reference/macie2/list-findings.html) command and use the `finding-criteria` parameter to specify the filter condition. For example:

```
C:\> aws macie2 list-findings --finding-criteria={\"criterion\":{\"sample\":{\"eq\":[\"true\"]}}}
```

If your request succeeds, Macie returns a `findingIds` array. The array lists the unique identifier for each sample finding for your account in the current AWS Region.

To then retrieve the details of the sample findings, specify these unique identifiers in a **GetFindings** request or, for the AWS CLI, when you run the [get-findings](https://docs.aws.amazon.com/cli/latest/reference/macie2/get-findings.html) command.

------

## Suppressing sample findings
<a name="findings-samples-suppress"></a>

Like other findings, Amazon Macie stores sample findings for 90 days. After you finish reviewing and experimenting with the samples, you can optionally archive them by [creating a suppression rule](findings-suppression-rule-create.md). If you do this, the sample findings stop appearing by default on the console and their status changes to *archived*.

To archive sample findings by using the Amazon Macie console, configure the rule to archive findings where the value for the **Sample** field is **True**. To archive sample findings by using the Amazon Macie API, configure the rule to archive findings where the value for the `sample` field is `true`.