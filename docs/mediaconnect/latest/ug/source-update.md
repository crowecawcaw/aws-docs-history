# Updating the source of a MediaConnect flow

Updating the source of a flow allows you to modify where your content comes from
without having to create a new flow. For most flows, you can make these updates even
while the flow is running.

###### Note

You can't update an entitled flow while it's active. Before you follow the steps
below to update an entitled flow, you must [stop the flow first](flows-stop.md "flows-stop.md"). After
you make your updates, you can then restart the flow.

The following procedure guides you through the process of updating a flow source.

###### To update the source of an existing flow (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose the name of the flow that you
   want to update.
3. Choose the **Source** tab.
4. Choose the source that you want to update.
5. Choose **Update**.
6. Make the appropriate changes, and then choose **Update
   source**.

###### To update the source of an existing flow (AWS CLI)

- In the AWS CLI, use the **update-flow-source** command:

```
aws mediaconnect update-flow-source --flow-arn `arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow` --source-arn `arn:aws:mediaconnect:us-east-1:111122223333:source:2-3aBC45dEF67hiJ89-c34de5fG678h:AwardsShowSource` --allowlist-cidr `10.24.34.0/24` --profile `PMprofile`
```
