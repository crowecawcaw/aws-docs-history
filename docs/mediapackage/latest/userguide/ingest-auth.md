# Ingest authorization

MediaPackage ingest requests usually originate from a video encoder.

###### Topics

- [AWS Elemental MediaLive](#ingest-medialive "#ingest-medialive")
- [AWS Elemental Live](#ingest-elemental-live "#ingest-elemental-live")
- [Third-party encoders](#ingest-third-party "#ingest-third-party")

## AWS Elemental MediaLive

This example illustrates a channel policy that permits MediaLive to ingest MediaPackage.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "AllowMediaLiveChannelToIngestToEmpChannel",
 "Statement": [
 {
 "Sid": "AllowMediaLiveRoleToAccessEmpChannel",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/MediaLiveAccessRole"
 },
 "Action": "mediapackagev2:PutObject",
 "Resource": "arn:aws:mediapackagev2:`us-east-1`:`111122223333`:channelGroup/`ChannelGroupName`/channel/`ChannelName`"
 }
 ]
}`

```

## AWS Elemental Live

If you provide Elemental Live with an access key ID and secret access key, it can request access as an IAM identity.
To grant your Elemental Live encoder access to your MediaPackage channel, you can apply the following `Allow` policy.

1. In IAM, create an IAM user such as `ElementalLiveMediaPackageUser` with **Programmatic access**.
2. In MediaPackage, create or edit a channel to include the following channel policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "AllowIamUser",
 "Statement": [
 {
 "Sid": "AllowIamUserToEmpChannel",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/ElementalLiveMediaPackageUser"
 },
 "Action": "mediapackagev2:PutObject",
 "Resource": "arn:aws:mediapackagev2:`us-east-1`:`111122223333`:channelGroup/`ChannelGroupName`/channel/`ChannelName`"
 }
 ]
}`

```

3. In IAM, create an access key for `ElementalLiveMediaPackageAccessUser`. Save the access key .csv file
   in a secure location to retain a permanent record of the access key ID and secret access key.

The access key ID looks like this: AKIAIOSFODNN7EXAMPLE

The secret access key looks like this: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

For more information, see [Programmatic access](../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys "../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys") in
the _AWS General Reference_. 4. Share the access key ID and the secret access key with the Elemental Live operator. Do _not_ give the
username and password to the operator.

By following these steps, you'll create an AWS user with the necessary permissions required to allow Elemental Live to make
requests to MediaPackage. When the operator sets up the output with MediaPackage as the destination, they will enter
the access key ID and secret access key. During the Elemental Live event, Elemental Live sends these two IDs to the AWS service instead of the
username and password, providing authorization to AWS for the Elemental Live node to make requests to MediaPackage.

## Third-party encoders

Third-party encoders that support AWS authorization operate similarly to Elemental Live, as described earlier.
To grant access, create an IAM user and a MediaPackage channel resource policy that permits the user to call `PutObject`.
On the encoder's side, use the IAM user access key ID and secret access key to sign the requests.
