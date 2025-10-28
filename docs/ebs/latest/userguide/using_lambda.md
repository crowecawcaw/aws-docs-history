# Using AWS Lambda to handle EventBridge events

You can use Amazon EBS and Amazon EventBridge to automate your data-backup workflow. This requires you
to create an IAM policy, a AWS Lambda function to handle the event, and an EventBridge
rule that matches incoming events and routes them to the Lambda function.

The following procedure uses the `createSnapshot` event to automatically
copy a completed snapshot to another Region for disaster recovery.

###### To copy a completed snapshot to another Region

1. Create an IAM policy, such as the one shown in the following example, to
   provide permissions to use the `CopySnapshot` action and write to
   the EventBridge log. Assign the policy to the user that will handle the EventBridge event.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CopySnapshot"
 ],
 "Resource": "*"
 }
 ]
}`

```

2. Define a function in Lambda that will be available from the EventBridge console.
   The sample Lambda function below, written in Node.js, is invoked by EventBridge when a
   matching `createSnapshot` event is emitted by Amazon EBS (signifying that
   a snapshot was completed). When invoked, the function copies the snapshot from
   `us-east-2` to `us-east-1`.

```
// Sample Lambda function to copy an EBS snapshot to a different Region

var AWS = require('aws-sdk');
var ec2 = new AWS.EC2();

// define variables
var destinationRegion = '`us-east-1`';
var sourceRegion = '`us-east-2`';
console.log ('Loading function');

//main function
exports.handler = (event, context, callback) => {

    // Get the EBS snapshot ID from the event details
    var snapshotArn = event.detail.snapshot_id.split('/');
    const snapshotId = snapshotArn[1];
    const description = `Snapshot copy from ${snapshotId} in ${sourceRegion}.`;
    console.log ("snapshotId:", snapshotId);

    // Load EC2 class and update the configuration to use destination Region to initiate the snapshot.
    AWS.config.update({region: destinationRegion});
    var ec2 = new AWS.EC2();

    // Prepare variables for ec2.modifySnapshotAttribute call
    const copySnapshotParams = {
        Description: description,
        DestinationRegion: destinationRegion,
        SourceRegion: sourceRegion,
        SourceSnapshotId: snapshotId
    };

    // Execute the copy snapshot and log any errors
    ec2.copySnapshot(copySnapshotParams, (err, data) => {
        if (err) {
            const errorMessage = `Error copying snapshot ${snapshotId} to Region ${destinationRegion}.`;
            console.log(errorMessage);
            console.log(err);
            callback(errorMessage);
        } else {
            const successMessage = `Successfully started copy of snapshot ${snapshotId} to Region ${destinationRegion}.`;
            console.log(successMessage);
            console.log(data);
            callback(null, successMessage);
        }
    });
};
```

To ensure that your Lambda function is available from the EventBridge console,
create it in the Region where the EventBridge event will occur. For more information,
see the [AWS Lambda Developer Guide](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md"). 3. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/"). 4. In the navigation pane, choose **Rules**, and then choose
**Create rule**. 5. For **Step 1: Define rule detail**, do the following:

    1. Enter values for **Name** and **Description**.
    2. For **Event bus**, keep **default**.
    3. Ensure that **Enable the rule on the selected event bus** is toggled on.
    4. For **Event type**, select **Rule with an event pattern**.
    5. Choose **Next**.

6. For **Step 2: Build event pattern**, do the following:
   1. For **Event source**, select **AWS events or EventBridge partner events**.
   2. In the **Event pattern** section, for **Event source**,
      ensure that **AWS service** is selected, and for **AWS service**,
      select **EC2**.
   3. For **Event type**, select **EBS Snapshot Notification**, select
      **Specific event(s)**, and then choose **createSnapshot**.
   4. Select **Specific result(s)** and then choose **succeeded**.
   5. Choose **Next**.

7. For **Step 3: Select targets**, do the following:
   1. For **Target types**, choose **AWS service**.
   2. For **Select target**, choose **Lambda function**, and for
      **Function** select the function that you created earlier.
   3. Choose **Next**

8. For **Step 4: Configure tags**, specify tags for the rule if needed, and then choose
   **Next**.
9. For **Step 5: Review and create**, review the rule and then choose **Create rule**.
   Your rule should now appear on the **Rules** tab. In the example
   shown, the event that you configured should be emitted by EBS the next time you copy a
   snapshot.
