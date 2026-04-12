AWS IoT FleetWise will no longer be open to new customers as of April 30, 2026. Existing
AWS IoT FleetWise customers can continue using the service. The
[Guidance
for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/ "https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/") provides guidance on how to develop and deploy modular
services for connected mobility solutions that can be used to achieve equivalent capabilities
as AWS IoT FleetWise.

# Get AWS IoT FleetWise campaign information

You can use the [GetCampaign](../APIReference/API_GetCampaign.md "../APIReference/API_GetCampaign.md") API
operation to retrieve vehicle information. The following example uses the AWS CLI.

To retrieve the metadata of a campaign, run the following command.

Replace `campaign-name` with the name of the campaign to you
want to retrieve.

```
aws iotfleetwise get-campaign --name `campaign-name`
```

###### Note

This operation is [eventually consistent](https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf "https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf"). In other words, changes to the campaign might
not be reflected immediately.

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `GetCampaign` API operation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`KMS_KEY_ID`"
 ]
 }
 ]
}`

```
