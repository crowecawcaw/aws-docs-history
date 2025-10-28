# Securing AWS Elemental MediaTailor origin interactions with SigV4

Signature Version 4 (SigV4) is a signing protocol used to authenticate MediaTailor requests to
supported origins over HTTPS. MediaTailor only supports HTTPS communication and does not allow HTTP
connections. With SigV4 signing, MediaTailor includes a signed authorization header in the HTTPS
origin request to MediaTailor Channel Assembly, Amazon S3 and AWS Elemental MediaPackage version 2.

You can use SigV4 at your origin to ensure that manifest requests are only fulfilled if
they’re from MediaTailor and contain a signed authorization header. This way, unauthorized MediaTailor
playback configurations are blocked from accessing your origin content. If the signed
authorization header is valid, your origin fulfills the request. If it isn't valid, the
request fails.

The following sections describe requirements for using MediaTailor SigV4 signing to supported
origins.

## MediaTailor Channel Assembly requirements

If you use SigV4 to protect your MediaTailor Channel Assembly origin, the following
requirements must be met for MediaTailor to access the manifest:

- The origin base URL in your MediaTailor configuration must be a Channel Assembly channel
  in the following format:
  `channel-assembly.mediatailor.`region`.amazonaws.com`
- Your origin must be configured to use HTTPS. MediaTailor only supports HTTPS communication
  and does not allow HTTP connections. If HTTPS is not enabled at the origin, MediaTailor will
  not sign the request.
- Your channel must have an origin access policy that includes the following:

      + Principal access for MediaTailor to access your channel. Grant access to
       **mediatailor.amazonaws.com**.
      + IAM permissions **mediatailor:GetManifest** to read all
       multivariant playlists referenced by the MediaTailor configuration.

  For information about setting a policy on the channel, see [Create a channel using the MediaTailor console](channel-assembly-creating-channels.md "channel-assembly-creating-channels.md").

###### Example origin access policy for Channel Assembly, scoped to the MediaTailor configuration

account

```
{
    "Effect": "Allow",
    "Principal": {"Service": "mediatailor.amazonaws.com"},
    "Action": "mediatailor:GetManifest",
    "Resource": "arn:aws:mediatailor:us-west-2:777788889999:channel/ca-origin-channel",
    "Condition": {
        "StringEquals": {"AWS:SourceAccount": "777788889999"}
    }
}
```

###### Example origin access policy for Channel Assembly, scoped to the MediaTailor playback

configuration

```
{
    "Effect": "Allow",
    "Principal": {"Service": "mediatailor.amazonaws.com"},
    "Action": "mediatailor:GetManifest",
    "Resource": "arn:aws:mediatailor:us-west-2:777788889999:channel/ca-origin-channel",
    "Condition": {
        "StringEquals": {"AWS:SourceArn": "arn:aws:mediatailor:us-west-2:777788889999:playbackConfiguration/test"}
    }
}
```

## Amazon S3 requirements

If you use SigV4 to protect your Amazon S3 origin, the following requirements must be met for
MediaTailor to access the manifest:

- The origin base URL in your MediaTailor configuration must be an S3 bucket in the
  following format: `s3.`region`.amazonaws.com`
- Your origin must be configured to use HTTPS. MediaTailor only supports HTTPS communication
  and does not allow HTTP connections. If HTTPS is not enabled at the origin, MediaTailor will
  not sign the request.
- Your channel must have an origin access policy that includes the following:
  - Principal access for MediaTailor to access your bucket. Grant access to
    **mediatailor.amazonaws.com.**

  For information about configuring access in IAM, see [Access management](../../../index.md "../../../index.md") in the _AWS
  Identity and Access Management User Guide_.
  - IAM permissions **s3:GetObject** to read all top-level
    manifests referenced by the MediaTailor configuration.

For general information about SigV4 for Amazon S3, see the [Authenticating Requests (AWS
Signature Version 4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md") topic in the _Amazon S3 API
reference_.

###### Example origin access policy for Amazon S3, scoped to the MediaTailor account

```
{
    "Effect": "Allow",
    "Principal": {"Service": "mediatailor.amazonaws.com"},
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::mybucket/*",
    "Condition": {
        "StringEquals": {"AWS:SourceAccount": "111122223333"}
    }
}
```

###### Example origin access policy for Amazon S3, scoped to the MediaTailor playback configuration

```
{
    "Effect": "Allow",
    "Principal": {"Service": "mediatailor.amazonaws.com"},
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::mybucket/*",
    "Condition": {
        "StringEquals": {"AWS:SourceArn": "arn:aws:mediatailor:us-west-2:111122223333:playbackConfiguration/test”}
    }
}
```

## MediaPackage requirements

If you use SigV4 to protect your MediaPackage v2 origin, the following requirements must be met
for MediaTailor to access the manifest:

- The origin base URL in your MediaTailor configuration must be a MediaPackage v2 endpoint in the
  following format:
  `mediapackagev2.`region`.amazonaws.com`
- Your origin must be configured to use HTTPS. MediaTailor only supports HTTPS communication
  and does not allow HTTP connections. If HTTPS is not enabled at the origin, MediaTailor will
  not sign the request.
- Your channel must have an origin access policy that includes the following:
  - Principal access for MediaTailor to access your endpoint. Grant access to
    **mediatailor.amazonaws.com.**
  - IAM permissions **mediapackagev2:GetObject** to read all
    multivariant playlists referenced by the MediaTailor configuration.

For general information about SigV4 for MediaPackage v2, see the [Authenticating Requests (AWS
Signature Version 4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md") topic in the _MediaPackage v2 API
reference_.

###### Example origin access policy for MediaPackage v2, scoped to the MediaTailor account

```
{
    "Effect": "Allow",
    "Principal": {"Service": "mediatailor.amazonaws.com"},
    "Action": "mediapackagev2:GetObject",
    "Resource": "arn:aws:mediapackagev2:us-west-2:444455556666:channelGroup/emp-origin-channel-group/channel/emp-origin-channel/originEndpoint/emp-origin-endpoint",
    "Condition": {
        "StringEquals": {"AWS:SourceAccount": "444455556666"}
    }
}
```

###### Example origin access policy for MediaPackage v2, scoped to the MediaTailor playback configuration

```
{
    "Effect": "Allow",
    "Principal": {"Service": "mediatailor.amazonaws.com"},
    "Action": "mediapackagev2:GetObject",
    "Resource": "arn:aws:mediapackagev2:us-west-2:444455556666:channelGroup/emp-origin-channel-group/channel/emp-origin-channel/originEndpoint/emp-origin-endpoint",
    "Condition": {
        "StringEquals": {"AWS:SourceArn": "arn:aws:mediatailor:us-west-2:444455556666:playbackConfiguration/test”"}
    }
}
```
