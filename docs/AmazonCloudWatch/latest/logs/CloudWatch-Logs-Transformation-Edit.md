# Edit a log-group-level

transformer

Use these steps to edit an existing log transformer.

###### To edit a log transformer

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, **Log
   groups**.
3. Choose the log group that has the transformer that you want to
   edit.
4. Choose the **Transformations** tab. You might have to
   scroll the tab list to the right to see it.
5. Choose **Manage transformer**.
6. In the **Parsers** and **Processors**
   sections, make your changes.
7. To add another processor, choose **+ Add Processor**.
   Then select the processor that you want in the
   **Processor** box, and fill in the configuration
   parameters. For information about the configuration parameters, see the
   section for that processor in [Processors that you can
   use](CloudWatch-Logs-Transformation-Processors.md "CloudWatch-Logs-Transformation-Processors.md").

Remember that processors operate on the log events in the order that you
add them to the transformer. 8. (Optional) At any time, you can test the transformer that you have built
so far on a sample log event. To do so, do the following:

    1. In the **Transformation Preview** section, either
     choose **Load Sample Log** to load a sample log
     event from the log group that this transformer is for, or paste a
     log event into the text box.


    Choose **Test Transformation**. The transformed
     version of the log appears

9. When you are finished adding processors and satisfied with the tests on
   sample logs, choose **Save**.
