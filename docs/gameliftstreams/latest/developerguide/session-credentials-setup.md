

# Setting up session credentials
<a name="session-credentials-setup"></a>

## Step 1: Create an IAM role
<a name="session-credentials-step1"></a>

Create an IAM role in your account with a name starting with `GameLiftStreams-` and a trust policy that allows the `gameliftstreams.amazonaws.com` service principal to assume it.

**Important**  
The role name must start with `GameLiftStreams-`. You cannot rename a role after creation. If you use a role without this prefix, `StartStreamSession` returns an error. For more information, see [Troubleshooting session credentials](session-credentials-troubleshooting.md).

We recommend adding `aws:SourceAccount` and `aws:SourceArn` conditions to your trust policy. These conditions use your AWS account ID and restrict which sessions can assume the role. For more information about protecting against cross-service impersonation, see [Cross-service confused deputy prevention](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*.

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "Service": "gameliftstreams.amazonaws.com" },
    "Action": "sts:AssumeRole",
    "Condition": {
      "StringEquals": {
        "aws:SourceAccount": "{{123456789012}}"
      },
      "ArnLike": {
        "aws:SourceArn": "arn:aws:gameliftstreams:*:{{123456789012}}:streamsession/*"
      }
    }
  }]
}
```

Replace both occurrences of {{123456789012}} with your AWS account ID.

**Note**  
[Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) (identified by ARNs containing `/aws-service-role/`) cannot be used with this feature. Create an IAM role instead.

## Step 2: Attach permissions to the role
<a name="session-credentials-step2"></a>

Attach IAM policies to the role that grant only the permissions your application needs. For guidance on scoping permissions, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the *IAM User Guide*.

For example, if your application needs to read from an Amazon S3 bucket:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "s3:GetObject",
      "s3:ListBucket"
    ],
    "Resource": [
      "arn:aws:s3:::{{my-game-assets-bucket}}",
      "arn:aws:s3:::{{my-game-assets-bucket}}/*"
    ]
  }]
}
```

## Step 3: Grant iam:PassRole permission
<a name="session-credentials-step3"></a>

The IAM principal that calls `StartStreamSession` must have permission to pass the role to Amazon GameLift Streams. Add the following statement to the principal's IAM policy. For more information, see [Granting a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) in the *IAM User Guide*.

```
{
  "Effect": "Allow",
  "Action": "iam:PassRole",
  "Resource": "arn:aws:iam::{{123456789012}}:role/GameLiftStreams-{{MyAppRole}}",
  "Condition": {
    "StringEquals": {
      "iam:PassedToService": "gameliftstreams.amazonaws.com"
    }
  }
}
```

## Step 4: Start a stream session with the role
<a name="session-credentials-step4"></a>

Pass the role ARN when calling [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html):

```
aws gameliftstreams start-stream-session \
    --stream-group-identifier {{sg-1AB2C3De4}} \
    --application-identifier {{a-9ZY8X7Wv6}} \
    --protocol WebRTC \
    --signal-request "{{[webrtc-ice-offer json string]}}" \
    --user-id {{myUserId}} \
    --role-arn arn:aws:iam::{{123456789012}}:role/GameLiftStreams-{{MyAppRole}}
```

If the role cannot be assumed (for example, because the trust policy is misconfigured), `StartStreamSession` returns a `ValidationException`. The session does not start. For more information, see [Troubleshooting session credentials](session-credentials-troubleshooting.md).