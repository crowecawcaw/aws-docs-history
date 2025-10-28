# Origin endpoint authorization

MediaPackage egress requests usually originate from CDNs, but they may also come from
other sources such as customer-owned monitoring scripts or operators using web browsers like Safari or Chrome to
view the video stream and identify any issues.

###### Topics

- [MediaPackage L2V Harvester](#mediapackage-endpoint "#mediapackage-endpoint")
- [Third-party CDNs that support AWS authorization](#endpoint-third-party "#endpoint-third-party")
- [Clients that don't support AWS authorization](#endpoint-no-aws "#endpoint-no-aws")

## MediaPackage L2V Harvester

To allow MediaPackage harvest jobs to get content from your origin endpoint, create or edit an origin endpoint with the following endpoint policy. For more information about harvest jobs, see [Creating live-to-VOD assets with MediaPackage](live-to-vod.md "live-to-vod.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "MediaPackageHarvesterAccessPolicy",
 "Statement": [
 {
 "Sid": "AllowMediaPackageHarvestObjectAccess",
 "Effect": "Allow",
 "Principal": {
 "Service": "mediapackagev2.amazonaws.com"
 },
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "`111122223333`"
 }
 },
 "Action": [
 "mediapackagev2:HarvestObject",
 "mediapackagev2:GetObject"
 ],
 "Resource": "arn:aws:mediapackagev2:`us-east-1`:`111122223333`:channelGroup/`ChannelGroupName`/channel/`ChannelName`/originEndpoint/`OriginEndpointName`"
 }
 ]
}`

```

## Third-party CDNs that support AWS authorization

To authorize an external CDN that supports AWS authorization, you need to create a specific IAM user
for the CDN, allow access in their origin endpoint policy, and provide the CDN with the AWS access key ID
and secret access key for the IAM user. For example, if you want to give your CDN provider access to your
MediaPackage origin endpoint, you can follow the following procedure.

1. In IAM, create an IAM user such as `CDNProviderMediaPackageAccessUser` with
   **Programmatic access**.
2. In MediaPackage, create or edit an origin endpoint to include the following endpoint policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "PolicyForCDNProviderPrivateContent",
 "Statement": [
 {
 "Sid": "AllowCDNProviderUser",
 "Effect": "Allow",
 "Principal": { "AWS": "arn:aws:iam::`111122223333`:user/CDNProviderMediaPackageAccessUser" },
 "Action": "mediapackagev2:GetObject",
 "Resource": "arn:aws:mediapackagev2:`us-east-1`:`111122223333`:channelGroup/`ChannelGroupName`/channel/`ChannelName`/originEndpoint/`OriginEndpointName`"
 }
 ]
}`

```

3. In IAM, create an access key for `CDNProviderMediaPackageAccessUser`. Save the access key .csv
   file in a secure location to retain a permanent record of the access key ID and secret access key.

The access key ID looks like this: AKIAIOSFODNN7EXAMPLE

The secret access key looks like this: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

For more information, see [Programmatic access](../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys "../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys") in
the _AWS General Reference_. 4. Follow the instructions in your CDN provider's documentation for authenticating with AWS
access keys.

By following these steps, you'll create an AWS user with the necessary permissions required to allow the external CDN
make requests to MediaPackage. When the CDN provider sets up the output with MediaPackage as the destination, they will enter
the access key ID and secret access key. During the event, the provider sends these two IDs to the AWS service instead of the
username and password, providing authorization to make requests to MediaPackage.

## Clients that don't support AWS authorization

Clients without AWS authorization support can be granted access to origin endpoints either by enabling
anonymous access or by restricting access to specific IP ranges using the `aws:SourceIp` condition key.
This is useful for clients such as external CDNs that don't support AWS authorization,
as well as monitoring scripts and human operators who may use web browsers to visually inspect a video stream.
For information about condition keys, see [IAM
JSON Policy Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md").

### Anonymous access

Consider the following `Allow` policy. With this policy in effect, MediaPackage
allows anonymous access to the `mediapackagev2:GetObject` action on the channel resource in the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "AnonymousAccessPolicy",
 "Statement": [
 {
 "Sid": "AllowAnonymousAccess",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "mediapackagev2:GetObject",
 "Resource": "arn:aws:mediapackagev2:`us-east-1`:`111122223333`:channelGroup/`ChannelGroupName`/channel/`ChannelName`/originEndpoint/`OriginEndpointName`"
 }
 ]
}`

```

MediaPackage doesn't support anonymous access for `PutObject` API calls.

### Cross-account access

Consider the following `Allow` policy. With this policy in effect, MediaPackage
allows, across accounts (`accountID` and `differentAccountID`), the
`mediapackagev2:GetObject` action on the channel resource in the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCrossAccountAccess",
 "Effect": "Allow",
 "Principal": {"AWS": "arn:aws:iam::`444455556666`:root"},
 "Action": "mediapackagev2:GetObject",
 "Resource": "arn:aws:mediapackagev2:`us-east-1`:`111122223333`:channelGroup/`ChannelGroupName`/channel/`ChannelName`"
 }
 ]
}`

```

### Restrict access by IP range

Consider the following `Allow` policy. With this policy in effect, MediaPackage restricts access to IP addresses
in the range `203.0.113.0` to `203.0.113.255` using the `aws:SourceIp` condition key.
For information about condition keys, see [IAM
JSON Policy Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "IpRangePolicy",
 "Statement": [
 {
 "Sid": "RestrictByIpRange",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "mediapackagev2:GetObject",
 "Resource": "arn:aws:mediapackagev2:`us-east-1`:`111122223333`:channelGroup/`ChannelGroupName`/channel/`ChannelName`/originEndpoint/`OriginEndpointName`",
 "Condition": {
 "IpAddress": { "aws:SourceIp": "203.0.113.0/24" }
 }
 }
 ]
}`

```
