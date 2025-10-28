# Edit tags for a report group

You can change the value for a tag associated with a report group. You can also change
the name of the key, which is equivalent to removing the current tag and adding a
different one with the new name and the same value as the other key. Keep in mind that
there are restrictions on the characters you can use in the key and value fields. For
more information, see [Tags](limits.md#tag-limits "limits.md#tag-limits").

###### Important

Editing tags for a report group can impact access to that report group. Before you
edit the name (key) or value of a tag for a report group, make sure to review any
IAM policies that might use the key or value for a tag to control access to
resources such as report groups. For examples of tag-based access policies, see
[Deny or allow actions on report groups based on resource tags](auth-and-access-control-using-tags.md#report-group-tag-policy-example "auth-and-access-control-using-tags.md#report-group-tag-policy-example").

## Edit a tag for a report

group (console)

You can use the CodeBuild console to edit the tags associated with a CodeBuild report
group.

1. Open the CodeBuild console at
   [https://console.aws.amazon.com/codebuild/](https://console.aws.amazon.com/codebuild/ "https://console.aws.amazon.com/codebuild/").
2. In **Report groups**, choose the name of the report group
   where you want to edit tags.
3. In the navigation pane, choose **Settings**.
4. Choose **Edit**.
5. Do one of the following:
   - To change the tag, enter a new name in **Key**.
     Changing the name of the tag is the equivalent of removing a tag and
     adding a new tag with the new key name.
   - To change the value of a tag, enter a new value. If you want to
     change the value to nothing, delete the current value and leave the
     field blank.

6. When you have finished editing tags, choose
   **Submit**.

## Edit tags for a report group

(AWS CLI)

To add, change, or delete tags from a report group, see [Update a report group (CLI)](report-group-export-settings.md#update-report-group-cli "report-group-export-settings.md#update-report-group-cli"). Update the tags in
`UpdateReportGroupInput.json`.
