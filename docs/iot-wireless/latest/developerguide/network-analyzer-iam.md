# Add necessary IAM role for network

analyzer

When you use network analyzer, you must grant a user permission to use the API
operations [UpdateNetworkAnalyzerConfiguration](../../2020-11-22/apireference/API_UpdateNetworkAnalyzerConfiguration.md "../../2020-11-22/apireference/API_UpdateNetworkAnalyzerConfiguration.md") and [GetNetworkAnalyzerConfiguration](../../2020-11-22/apireference/API_GetNetworkAnalyzerConfiguration.md "../../2020-11-22/apireference/API_GetNetworkAnalyzerConfiguration.md") to access network analyzer resources. The
following shows the IAM policies that you use to grant permissions.

## IAM policies for network

analyzer

Use either of the following:

- ###### Full access wireless policy

Grant AWS IoT Core for LoRaWAN the full access policy by attaching the policy
**AWSIoTWirelessFullAccess** to your role. For more
information, see [`AWSIoTWirelessFullAccess` policy summary](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessFullAccess$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTWirelessFullAccess$serviceLevelSummary").

- ###### Scoped IAM policy for Get and Update API

Create the following IAM policy by going to the [Create policy](https://console.aws.amazon.com/iam/home#/policies$new?step=edit "https://console.aws.amazon.com/iam/home#/policies$new?step=edit") page of
the IAM console, and on the **Visual editor**
tab:

    1. Choose **IoTWireless** for
     **Service**.
    2. Under **Access level**, expand
     **Read** and choose
     **GetNetworkAnalyzerConfiguration**, and then
     expand **Write** and choose
     **UpdateNetworkAnalyzerConfiguration**.
    3. Choose **Next:Tags**, and enter a
     **Name** for the policy, such as
     **IoTWirelessNetworkAnalyzerPolicy**. Choose
     **Create policy**.

The following shows the policy
**IoTWirelessNetworkAnalyzerPolicy** that you created.
For more information about creating a policy, see [Create IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "iotwireless:GetNetworkAnalyzerConfiguration",
 "iotwireless:UpdateNetworkAnalyzerConfiguration"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Scoped policy to access specific resources

To configure more fine-grained access control, you must add the wireless
gateways and devices to the **Resource** field. The following
policy uses the wildcard ARN to grant access to all gateways and devices. You
can control access to specific gateways and devices by using the
`WirelessGatewayId` and `WirelessDeviceId`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "iotwireless:GetNetworkAnalyzerConfiguration",
 "iotwireless:UpdateNetworkAnalyzerConfiguration"
 ],
 "Resource": [
 "arn:aws:iotwireless:*:`111122223333`:WirelessDevice/*",
 "arn:aws:iotwireless:*:`111122223333`:WirelessGateway/*",
 "arn:aws:iotwireless:*:`111122223333`:NetworkAnalyzerConfiguration/*"
 ]
 }
 ]
}`

```

To grant a user permission to use network analyzer but not to use any wireless
gateways or devices, use the following policy. Unless specified, permissions to use
the resources are implicitly denied.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "iotwireless:GetNetworkAnalyzerConfiguration",
 "iotwireless:UpdateNetworkAnalyzerConfiguration"
 ],
 "Resource": [
 "arn:aws:iotwireless:*:`111122223333`:NetworkAnalyzerConfiguration/*"
 ]
 }
 ]
}`

```

## Next steps

Now that you've created the policy, you can add resources to your network analyzer
configuration and receive trace messaging information for those resources. For more
information, see [Create network analyzer
configuration and add resources](network-analyzer-create-resources.md "network-analyzer-create-resources.md").
