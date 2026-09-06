

# Updating the source of a MediaConnect flow
<a name="source-update"></a>

Updating the source of a flow allows you to modify where your content comes from without having to create a new flow. For most flows, you can make these updates even while the flow is running. 

## Prerequisites
<a name="source-update-prerequisites"></a>

Depending on the type of update you want to make, there are some steps to complete before you get started.

**If you're updating a flow with an entitled source**  
You can't update an entitled flow while it's active. Before you update the flow source, you must [stop the flow first](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-stop.html). After you make your updates, you can then restart the flow.

**If you're switching between an NDI® source and a transport stream source**  
You can update the flow source while it's either active or on standby.
+ **When changing to an NDI source** 

  Before you update the flow source, you must edit the flow first and change the flow size from medium to large.
+ **When changing to a transport stream source**

  Your flow size will remain as large after you update the source type. If you want to downgrade the flow size, you'll need to edit the flow afterwards as a separate step.

## Procedure
<a name="source-update-procedure"></a>

The following procedure guides you through the process of updating a flow source. 

**To update the source of an existing flow (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. On the **Flows** page, choose the name of the flow that you want to update.

1. Choose the **Source** tab.

1. Choose the source that you want to update.

1. Choose **Update**.

1. Make the appropriate changes, and then choose **Update source**.

**To update the source of an existing flow (AWS CLI)**
+ In the AWS CLI, use the **update-flow-source** command:

  ```
  aws mediaconnect update-flow-source --flow-arn {{arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow}} --source-arn {{arn:aws:mediaconnect:us-east-1:111122223333:source:2-3aBC45dEF67hiJ89-c34de5fG678h:AwardsShowSource}} --allowlist-cidr {{10.24.34.0/24}} --profile {{PMprofile}}
  ```