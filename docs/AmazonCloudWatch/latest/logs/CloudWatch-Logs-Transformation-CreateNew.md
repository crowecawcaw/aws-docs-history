# Create a log-group-level log transformer from scratch

Use these steps to create a log-group-level transformer from scratch.

###### To use the console to create a log transformer for a log group

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, **Log
   groups**.
3. Choose the log group that you want to create the transformer for.
4. Choose the **Transformer** tab. You might have to scroll
   the tab list to the right to see it.
5. Choose **Create transformer**.
6. In the **Choose a parser** box, select a parser to
   include in your transformer.

If it is a pre-configured parser for a type of AWS vended log, you don't
have to specify any configuration for it.

If it is a different parser, you need to specify its configuration. For
more information, see the information for that processor in [Configurable parser-type processors](CloudWatch-Logs-Transformation-Configurable.md "CloudWatch-Logs-Transformation-Configurable.md"). 7. To add another processor, choose **+ Add processor**.
Then select the processor that you want in the **Choose
processors** box, and fill in the configuration parameters.

Remember that processors operate on the log events in the order that you
add them to the transformer. 8. (Optional) At any time, you can test the transformer that you have built
so far on a sample log event. To do so, do the following:

    1. In the **Transformation preview** section, either
     choose **Load sample log** to load a sample log
     event from the log group that this transformer is for, or paste a
     log event into the text box.


    Choose **Test transformer**. The transformed
     version of the log appears

9. When you are finished adding processors and satisfied with the tests on
   sample logs, choose **Save**.

###### To use the AWS CLI to create a log transformer from scratch

- Use the `aws logs put-transformer` command. When using
  `parseJSON` as the first processor, you must parse the entire
  log event using `@message` as the source field. After the initial
  JSON parsing, you can then manipulate specific fields in subsequent
  processors. The following is an example that creates a transformer that
  includes the `parseJSON` and `addKeys`
  processors:

```
 aws logs put-transformer \
  --transformer-config '[{"parseJSON":{"source":"@message"}},{"addKeys":{"entries":[{"key":"metadata.transformed_in","value":"CloudWatchLogs"},{"key":"feature","value":"Transformation"}]}},{"trimString":{"withKeys":["status"]}}]' \
  --log-group-identifier my-log-group-name
```
