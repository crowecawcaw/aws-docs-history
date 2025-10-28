# Create a log-group-level

transformer by copying an existing one

You can use the console to copy the JSON configuration of an existing transformer.
You can then use that code to create an identical transformer by using the AWS CLI, or
you can modify the configuration first.

###### To create a log transformer by copying an existing one

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, **Log
   groups**.
3. Choose the log group that has the transformer that you want to
   copy.
4. Choose the **Transformations** tab. You might have to
   scroll the tab list to the right to see it.
5. Choose **Manage transformer**.
6. Choose **Copy transformer**. This copies the transformer
   JSON to your clipboard.
7. Create a file and paste in the transformer configuration. In this example
   we'll call the file `CopiedTransformer.json`
8. Use the AWS CLI to create a new transformer with that configuration.

```
aws logs put-transformer --log-group-identifier `my-log-group-name` \
--transformer-config file://CopiedTransformer.json
```
