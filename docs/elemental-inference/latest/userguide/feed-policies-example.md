

# Example policy for MediaTailor access
<a name="feed-policies-example"></a>

The following example policy grants AWS Elemental MediaTailor permission to call `GetMetadata` on the specified feed. The policy uses two conditions to prevent the *confused deputy* problem:
+ `aws:SourceAccount` – Ensures only MediaTailor operating on behalf of your account can access the feed.
+ `aws:SourceArn` – Further restricts access to specific playback configurations. Replace the wildcard (`*`) with a specific playback configuration name for tighter scoping.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowMediaTailorGetMetadata",
            "Effect": "Allow",
            "Principal": {
                "Service": "mediatailor.amazonaws.com"
            },
            "Action": "elemental-inference:GetMetadata",
            "Resource": "arn:aws:elemental-inference:{{region}}:{{account-id}}:feed/{{feed-id}}",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{account-id}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:mediatailor:{{region}}:{{account-id}}:playbackConfiguration/*"
                }
            }
        }
    ]
}
```

Replace the following placeholder values:
+ `{{region}}` – The AWS Region where the feed and playback configuration exist (for example, `us-west-2`).
+ `{{account-id}}` – Your AWS account ID (the account that owns both the feed and the MediaTailor playback configuration).
+ `{{feed-id}}` – The ID of the Elemental Inference feed.

**Note**  
For opt-in AWS Regions, use the regionalized service principal `mediatailor.{{region}}.amazonaws.com` instead of `mediatailor.amazonaws.com`.