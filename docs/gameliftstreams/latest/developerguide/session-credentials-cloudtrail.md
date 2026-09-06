

# Auditing with CloudTrail
<a name="session-credentials-cloudtrail"></a>

When Amazon GameLift Streams assumes your role, the `RoleSessionName` in CloudTrail is set to:

```
streamsession_sg-{{{streamGroupId}}}_{{{sessionId}}}_a-{{{applicationId}}}
```

With this format, you can trace any AWS API calls made by your application back to the specific stream session, stream group, and application. You can use CloudTrail to:
+ Monitor which AWS APIs your streamed applications are calling.
+ Detect unexpected API calls from specific sessions.
+ Correlate application behavior with specific stream sessions for debugging.

You can also use the `sts:RoleSessionName` condition key in your role's trust policy to restrict which sessions can use the role. For example:

```
"Condition": {
  "StringLike": {
    "sts:RoleSessionName": "streamsession_*"
  }
}
```