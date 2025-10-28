# Creating a custom widget for a CloudWatch dashboard

To create a custom widget, you can use one of the samples provided by AWS, or you can
create your own. The AWS samples include samples
in both JavaScript and Python, and are created by a AWS CloudFormation stack. For a list of samples, see [Sample custom widgets for a CloudWatch dashboard](add_custom_widget_samples.md "add_custom_widget_samples.md").

###### To create a custom widget in a CloudWatch dashboard

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**,
   and then
   choose
   a dashboard.
3. Choose the **+** symbol.
4. Choose **Custom widget**.
5. Use one of the following methods:
   - To use a sample custom widget provided by AWS, do the following:
     1. Select the sample in the dropdown box.

     The AWS CloudFormation console launches in a new browser. In the AWS CloudFormation console, do the following: 2. (Optional) Customize the AWS CloudFormation stack name. 3. Make selections for any parameters used by the sample. 4. Select **I acknowledge that AWS CloudFormation might create IAM resources**, and choose **Create stack**.

   - To create your own custom widget provided by AWS, do the following:
     1. Choose **Next**.
     2. Choose to either select your Lambda function from a list, or enter
        its Amazon Resource Name
        (ARN). If you select it from a list, also specify the
        Region where the function is and the version to
        use.
     3. For **Parameters**, make selections for any parameters used by the function.
     4. Enter a title for the widget.
     5. For **Update on**, configure when the widget should be updated (when the
        Lambda function should be called again). This can be one
        or more of the following: **Refresh**
        to update it when the dashboard auto-refreshes,
        **Resize** to update it whenever
        the widget is resized, or **Time
        Range** to update it whenever the
        dashboard's time range is adjusted, including when
        graphs are zoomed into.
     6. If you are satisfied with the preview, choose **Create widget**.
