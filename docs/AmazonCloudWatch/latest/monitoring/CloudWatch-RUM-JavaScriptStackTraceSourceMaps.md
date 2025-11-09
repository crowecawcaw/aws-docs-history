# Enabling unminification of JavaScript error stack traces

When your web application JavaScript source code is minified, error stack traces can be difficult to read. You can enable unminification to the stack traces by uploading your source maps to Amazon S3. CloudWatch RUM will retrieve the source maps to map the line and
column numbers in the minified source code back to the original unminified source code. This will improve readability of your error stack traces and help identify the location of the error in the original source code.

## Requirements and syntax

Source maps are crucial for debugging and tracking issues in your web application across different releases. Make sure that each web application release has a unique source map. Each release should have its own unique releaseId. A releaseId must be a string between 1 and 200 characters long and can only contain letters, numbers, underscores, hyphens, colons, forward slashes, and periods.
To add the `releaseId` as metadata to RUM events, configure the CloudWatch RUM web client.

Source maps are expected to be plain JSON files following the structure defined by the [Source Map V3 specification](https://sourcemaps.info/spec.html "https://sourcemaps.info/spec.html"). The required fields are: `version`, `file`, `sources`, `names`,
and `mappings`.

Make sure the size of each source map does not exceed the limit of 50 MB. In addition, RUM service will only retrieve up to 50 MB of source maps per stack trace.
If needed, split the source code into multiple smaller chunks. For more information, see [Code Splitting with WebpackJS](https://webpack.js.org/guides/code-splitting/ "https://webpack.js.org/guides/code-splitting/").

###### Topics

- [Configure your Amazon S3 bucket resource policy to allow RUM service access](#CloudWatch-RUM-ConfigureS3 "#CloudWatch-RUM-ConfigureS3")
- [Upload source maps](#CloudWatch-RUM-UploadSourceMaps "#CloudWatch-RUM-UploadSourceMaps")
- [Configure releaseId in your CloudWatch RUM web client](#CloudWatch-RUM-ConfigureRumID "#CloudWatch-RUM-ConfigureRumID")
- [Enabling CloudWatch RUM app monitor to unminify JavaScript stack traces](#CloudWatch-RUM-unminifyjavascript "#CloudWatch-RUM-unminifyjavascript")
- [Viewing unminified stack traces in the RUM console](#CloudWatch-RUM-viewunminifiedstacktraces "#CloudWatch-RUM-viewunminifiedstacktraces")
- [Viewing unminified stack traces in CloudWatch Logs](#CloudWatch-RUM-viewunminifiedstacktracesCWL "#CloudWatch-RUM-viewunminifiedstacktracesCWL")
- [Troubleshooting source maps](#CloudWatch-RUM-troubleshootsourcemaps "#CloudWatch-RUM-troubleshootsourcemaps")

## Configure your Amazon S3 bucket resource policy to allow RUM service access

Make sure your Amazon S3 bucket is in the same region as your RUM appMonitor. Configure your Amazon S3 bucket to allow RUM service access for retrieving source map files. Include the `aws:SourceArn` and `aws:SourceAccount` global condition context keys to
limit the service’s permissions to the resource. This is the most effective way to protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

The following example shows how you can use the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in Amazon S3 to prevent the confused deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RUM Service S3 Read Permissions",
 "Effect": "Allow",
 "Principal": {
 "Service": "rum.amazonaws.com"
 },
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`BUCKET_NAME`",
 "arn:aws:s3:::`BUCKET_NAME`/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`ACCOUNT_ID`",
 "aws:SourceArn": "arn:aws:rum:`REGION`:`ACCOUNT_ID`:appmonitor/`APP_MONITOR_NAME`"
 }
 }
 }
 ]
}`

```

If you are using AWS KMS keys to encrypt the data, make sure the key’s resource policy is configured similarly to include the `aws:SourceArn` and `aws:SourceAccount` global condition context keys to give RUM service access to use the keys to retrieve the source map files.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RUM Service KMS Read Permissions",
 "Effect": "Allow",
 "Principal": {
 "Service": "rum.amazonaws.com"
 },
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/`KEY_ID`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`",
 "aws:SourceArn": "arn:aws:rum:`us-east-1`:`123456789012`/`APP_MONITOR_NAME`"
 }
 }
 }
 ]
}`

```

## Upload source maps

Configure your JavaScript bundle to generate source maps during minification. When you build your application, the bundle will create a directory (for example, dist) containing the minified JavaScript files and their corresponding source maps. See below for an example.

```
./dist
    |-index.d5a07c87.js
    |-index.d5a07c87.js.map
```

Upload the source map files to your Amazon S3 bucket. The files should be located in a folder with the `releaseId` as the name. For example, if my bucket name is `my-application-source-maps` and the `releaseId` is 2.0.0, then the source map file is located at the following
location:

```
my-application-source-maps
    |-2.0.0
        |-index.d5a07c87.js.map
```

To automate uploading your source maps, you can create the following bash script and execute it as part of your build process.

```
#!/bin/bash
# Ensure the script is called with required arguments
if [ "$#" -ne 2 ]; then
 echo "Usage: $0 `S3_BUCKET_NAME` `RELEASE_ID`"
 exit 1
fi

# Read arguments
S3_BUCKET="$1"
RELEASE_ID="$2"

# Set the path to your build directory
BUILD_DIR="./dist"


# Upload all .map files recursively
 if aws s3 cp "$BUILD_DIR" "s3://$S3_BUCKET/$RELEASE_ID/" --recursive --exclude "*" --include "*.map"; then
    echo "Successfully uploaded all source map files"
else
    echo "Failed to upload source map files"
fi
```

## Configure releaseId in your CloudWatch RUM web client

CloudWatch RUM uses the configured `releaseId` to determine the folder to retrieve the source map files. Name the `releaseId` the same as your source map files folder.
If you used the provided bash script above or a similar one, the `releaseId` configured in the script should be the same as the one configured in your CloudWatch RUM web client. You must use version 1.21.0 or later of the CloudWatch RUM web client.

```
import { AwsRum, AwsRumConfig } from "`aws-rum-web`";

try {
    const config: AwsRumConfig = {
        sessionSampleRate: 1,
        endpoint: "https://dataplane.rum.us-west-2.amazonaws.com",
        telemetries: ["performance", "errors", "http"],
        allowCookies: true,
        releaseId: "`RELEASE_ID`", //Add this
    };

    const APPLICATION_ID: string = "`APP_MONITOR_ID`";
    const APPLICATION_VERSION: string = "1.0.0";
    const APPLICATION_REGION: string = "us-west-2";

    new AwsRum(APPLICATION_ID, APPLICATION_VERSION, APPLICATION_REGION, config);
} catch (error: any) {
    // Ignore errors thrown during CloudWatch RUM web client initialization
}
```

## Enabling CloudWatch RUM app monitor to unminify JavaScript stack traces

To unminify JavaScript stack traces, set the app monitor's SourceMap status to `ENABLED`. Provide the Amazon S3 URI to the bucket or folder containing all source maps for your app monitor.

When storing source maps directly in the main bucket (not in a subfolder), then the Amazon S3 URI should be formatted as `Amazon S3://`BUCKET_NAME``. In this case, source map files should be located at the following location.

```
`BUCKET_NAME`
    |- `RELEASE_ID`
        |-index.d5a07c87.js.map
```

When a child directory is the root, then the Amazon S3 URI should be formatted as `Amazon S3://`BUCKET_NAME`/`DIRECTORY``. In this case, source map files should be located at the following location.

```
`BUCKET_NAME`
    |- `DIRECTORY`
        |-`RELEASE_ID`
            |-index.d5a07c87.js.map
```

## Viewing unminified stack traces in the RUM console

After uploading your source maps to Amazon S3, enabling source maps on your RUM app monitor, and deploying your web application with the `releaseId` configured in the CloudWatch RUM web client, select **Events** in the RUM console. This tab displays the raw RUM event data.
Filter by the JS error event type and view the latest JS error event. You will see the unminified stack trace in the new `event_details.unminifiedStack` field for events ingested after the feature was enabled.

## Viewing unminified stack traces in CloudWatch Logs

Enable RUM event storage in CloudWatch Logs by turning on **Data storage**. Once enabled, you can search the new **event_details.unminifiedStack** field. This allows you to analyze trends and relate issues across multiple sessions using CloudWatch Logs queries.

## Troubleshooting source maps

CloudWatch RUM provides out of the box metrics to troubleshoot your source map setup. These metrics are published in the metric namespace named `AWS/RUM`. The following metrics are published with an application_name dimension.
The value of this dimension is the name of the app monitor. The metrics are also published with an `aws:releaseId` dimension. The value of this dimension is the `releaseId` associated with the JavaScript error event.

| MetricName                | Unit  | Description                                                                                                                                                                                                            |
| ------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UnminifyLineFailureCount  | Count | The count of stack trace lines in the JS error event that failed to be unminified. Additional details regarding the failure will be added to the specific line that failed in the event_details.unminifiedStack field. |
| UnminifyLineSuccessCount  | Count | The count of stack trace lines in the JS error event that were successfully unminified.                                                                                                                                |
| UnminifyEventFailureCount | Count | The count of JS error events that failed to have any lines unminified. Additional details regarding the failure will be added in the event_details.unminifiedStack field.                                              |
| UnminifyEventSuccessCount | Count | The count of JS error events that succeeded to have at least one stack trace line unminified.                                                                                                                          |

CloudWatch RUM may fail to unminify a line in the stack trace for various reasons, including but not limited to:

- Failure to retrieve corresponding source map file due to permission issues. Make sure the bucket resource policy is configured correctly.
- Corresponding source map file does not exist. Make sure the source map files have been uploaded to the correct bucket or folder that has the same name as the releaseId configured in your CloudWatch RUM web client.
- Corresponding source map file is too big. Split your source code into smaller chunks.
- 50 MB worth of source map files already retrieved for the stack trace. Reduce the stack trace length as 50 MB is service side limitation.
- Source map is invalid and could not be indexed. Make sure the source map is a plain JSON following the structure defined by the Source Map V3 specification and includes the following fields: version, file, sources, names, mappings.
- Source map could not map the minified source code back to the unminified stack trace. Make sure the source map is the correct source map for the given releaseId.
