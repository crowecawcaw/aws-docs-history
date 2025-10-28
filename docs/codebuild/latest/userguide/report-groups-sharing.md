# Share report groups

Report group sharing allows multiple AWS accounts or users to view a report group, its
unexpired reports, and the test results of its reports. In this model, the account that owns
the report group (owner) shares a report group with other accounts (consumers). A consumer
cannot edit a report group. A report expires 30 days after it is created.

###### Topics

- [Share a report group](#report-groups-sharing-share "#report-groups-sharing-share")
- [Related services](#report-groups-sharing-related "#report-groups-sharing-related")
- [Access
  report groups shared with you](report-groups-sharing-access-prereqs.md "report-groups-sharing-access-prereqs.md")
- [Unshare a shared report group](report-groups-sharing-unshare.md "report-groups-sharing-unshare.md")
- [Identify a shared report group](report-groups-sharing-identify.md "report-groups-sharing-identify.md")
- [Shared report group permissions](report-groups-sharing-perms.md "report-groups-sharing-perms.md")

## Share a report group

When you share a report group, the consumer is granted read-only access to the report
group and its reports. The consumer can use the AWS CLI to view the report group, its
reports, and the test case results for each report. The consumer cannot:

- View a shared report group or its reports in the CodeBuild console.
- Edit a shared report group.
- Use the ARN of the shared report group in a project to run a report. A
  project build that specifies a shared report group fails.

You can use the CodeBuild console to add a report group to an existing resource share. If
you want to add the report group to a new resource share, you must first create it in
the [AWS RAM console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram").

To share a report group with organizational units or an entire organization, you must
enable sharing with AWS Organizations. For more information, see [Enable sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md") in the _AWS RAM User Guide_.

You can use the CodeBuild console, AWS RAM console, or AWS CLI to share report groups that you
own.

###### Prerequisite

To share a report group, your AWS account must own it. You cannot share a report
group that has been shared with you.

###### To share a report group that you own (CodeBuild console)

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. In the navigation pane, choose **Report groups**.
3. Choose the project you want to share, and then choose
   **Share**. For more information, see [Create a resource share](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create") in the _AWS RAM User
   Guide_.

###### To share report groups that you own (AWS RAM console)

See [Creating a resource share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create") in the _AWS RAM User Guide_.

###### To share report groups that you own (AWS RAM command)

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md")
command.

**To share a report group that you own (CodeBuild command)**

Use the [put-resource-policy](../../../cli/latest/reference/codebuild/put-resource-policy.md "../../../cli/latest/reference/codebuild/put-resource-policy.md")
command:

1. Create a file named `policy.json` and copy the following
   into it.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[{
 "Effect":"Allow",
 "Principal":{
 "AWS":"`111122223333`"
 },
 "Action":[
 "codebuild:BatchGetReportGroups",
 "codebuild:BatchGetReports",
 "codebuild:ListReportsForReportGroup",
 "codebuild:DescribeTestCases"],
 "Resource":"`arn:aws:iam::*:role/Service*`"
 }]
 }`

```

2. Update `policy.json` with the report group ARN and
   identifiers to share it with. The following example grants read-only access to
   the report group with the ARN
   `arn:aws:codebuild:us-west-2:123456789012:report-group/my-report-group`
   to Alice and the root user for the AWS account identified by
3.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[{
 "Effect":"Allow",
 "Principal":{
 "AWS": [
 "arn:aws:iam::123456789012:user/Alice",
 "123456789012"
 ]
 },
 "Action":[
 "codebuild:BatchGetReportGroups",
 "codebuild:BatchGetReports",
 "codebuild:ListReportsForReportGroup",
 "codebuild:DescribeTestCases"],
 "Resource":"arn:aws:codebuild:us-west-2:123456789012:report-group/my-report-group"
 }]
 }`

```

3. Run the following command.

```
aws codebuild put-resource-policy --resource-arn `report-group-arn` --policy file://policy.json
```

## Related services

Report group sharing integrates with AWS Resource Access Manager (AWS RAM), a service that makes it
possible for you to share your AWS resources with any AWS account or through
AWS Organizations. With AWS RAM, you share resources that you own by creating a _resource
share_ that specifies the resources and the consumers to share them with.
Consumers can be individual AWS accounts, organizational units in AWS Organizations, or an
entire organization in AWS Organizations.

For more information, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.
