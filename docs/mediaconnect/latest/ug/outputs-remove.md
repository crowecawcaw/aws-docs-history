# Disabling or removing outputs from a flow

You can disable or remove outputs that you added to the flow. If AWS Elemental MediaConnect
generated the output as the result of an entitlement, you must [revoke the entitlement](entitlements-revoke.md "entitlements-revoke.md").

Disabling an output stops the streaming of content to the output destination, but
remains attached to the flow. A disabled output does not incur data transfer
costs.

###### To disable an output (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose the name of the flow that is
   associated with the output that you want to disable.

The details page for that flow appears. 3. Choose the **Outputs** tab. 4. Choose the output, and then choose **Update**. 5. In the **Update output** window, use the **Output
status** toggle to disable or enable the selected output. 6. Choose **Save** to save your changes.

###### To disable an output (AWS CLI)

- In the AWS CLI, use the `update-flow-output` command with the
  `--output-status DISABLED` option to disable the output.
  Alternately, you can use `--output-status ENABLED` to enable a
  disabled output.

```
aws mediaconnect update-flow-output --flow-arn "`arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame`" --output-arn "`arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:Output1`" --output-status `DISABLED`

```

The following example shows the return value:

```
{
    "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame",
    "Output": {
        "Destination": "192.0.2.12",
        "Name": "NYCOutput",
        "OutputArn": "arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:NYCOutput",
        "OutputStatus": "DISABLED",
        "Port": 5020,
        "Transport": {
            "MinLatency": 1000,
            "Protocol": "rtp-fec"
        }
    }
}
```

###### To remove an output from a flow (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose the name of the flow that is
   associated with the output that you want to remove.

The details page for that flow appears. 3. Choose the **Outputs** tab. 4. Choose the output, and then choose **Remove**.

###### To remove an output from a flow (AWS CLI)

- In the AWS CLI, use the `remove-flow-output` command:

```
aws mediaconnect remove-flow-output --flow-arn "`arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame`" --output-arn "`arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:Output1`" --region `us-west-2`

```

The following example shows the return value:

```
{
    "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame",
    "OutputArn": "arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:Output1"
}
```
