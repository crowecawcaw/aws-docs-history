# Add tags to a report group

Adding tags to a report group can help you identify and organize your AWS resources
and manage access to them. First, you add one or more tags (key-value pairs) to a report
group. Keep in mind that there are limits on the number of tags you can have on a report
group. There are restrictions on the characters you can use in the key and value fields.
For more information, see [Tags](limits.md#tag-limits "limits.md#tag-limits"). After
you have tags, you can create IAM policies to manage access to the report group based
on these tags. You can use the CodeBuild console or the AWS CLI to add tags to a report group.

###### Important

Adding tags to a report group can impact access to that report group. Before you
add a tag to a report group, make sure to review any IAM policies that might use
tags to control access to resources such as report groups. For examples of tag-based
access policies, see [Using tags to control access to
AWS CodeBuild resources](auth-and-access-control-using-tags.md "auth-and-access-control-using-tags.md").

For more information about adding tags to a report group when you create it, see [Create a report group
(console)](report-group-create.md#test-report-group-create-console "report-group-create.md#test-report-group-create-console").

###### Topics

- [Add a tag to a report group
  (console)](#how-to-tag-report-group-add-console "#how-to-tag-report-group-add-console")
- [Add a tag to a report group
  (AWS CLI)](#how-to-tag-report-group-add-cli "#how-to-tag-report-group-add-cli")

## Add a tag to a report group

(console)

You can use the CodeBuild console to add one or more tags to a CodeBuild report group.

1. Open the CodeBuild console at
   [https://console.aws.amazon.com/codebuild/](https://console.aws.amazon.com/codebuild/ "https://console.aws.amazon.com/codebuild/").
2. In **Report groups**, choose the name of the report group
   where you want to add tags.
3. In the navigation pane, choose **Settings**.
4. If no tags have been added to the report group, choose **Add
   tag**. You can also choose **Edit**, and then
   choose **Add tag**.
5. In **Key**, enter a name for the tag. You can add an
   optional value for the tag in **Value**.
6. (Optional) To add another tag, choose **Add tag**
   again.
7. When you have finished adding tags, choose
   **Submit**.

## Add a tag to a report group

(AWS CLI)

To add a tag to a report group when you create it, see [Create a report group
(CLI)](report-group-create.md#test-report-group-create-cli "report-group-create.md#test-report-group-create-cli"). In
`CreateReportGroup.json`, add your tags.

To add tags to an existing report group, see [Update a report group (CLI)](report-group-export-settings.md#update-report-group-cli "report-group-export-settings.md#update-report-group-cli") and
add your tags in `UpdateReportGroupInput.json`.

In these steps, we assume that you have already installed a recent version of the
AWS CLI or updated to the current version. For more information, see [Installing the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md").
