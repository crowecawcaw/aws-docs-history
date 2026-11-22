

# Session evidence

*Session evidence* is the set of capabilities that you use to track what happened during an agent session. Session evidence gives you an audit-ready record of what the AI agent did, delivered to your own Amazon S3 bucket.

You can choose either of the following evidence options:
+ **Screenshots and CloudWatch logs**. Store the screenshots that the agent takes during a session in your Amazon S3 bucket, and review agent activity in CloudWatch. For more information, see [Screenshot storage](agent-access-mcp-session-behavior.md#agent-access-screenshots) and [Monitoring](agent-access-mcp-server-monitoring.md).
+ **[Public Preview] Replay Session**. Combine the screenshots taken before each agent action into a replayable session video, paired with an AI-generated transcript and an HTML report. The rest of this topic describes Replay Session. Replay Session is available on stacks and not on image builder.

## How Replay Session works
<a name="agent-access-replay-session-how-it-works"></a>

Replay Session is turned off by default. An administrator turns it on for each stack and names an Amazon S3 bucket to receive the recordings. When Replay Session is turned on, it works as follows:

1. During the session, just before the agent performs each action, Replay Session captures a frame of the whole screen and records metadata about the action, such as the tool that the agent called, its arguments, the tool response, and a timestamp.

1. Replay Session stores the frames and their metadata in storage that AWS owns, encrypted at rest. For more information, see [Encryption at rest for Replay Session](agent-access-replay-session-encryption.md).

1. After the session ends, Replay Session uses Amazon Bedrock to analyze the frames and metadata, and produces the following artifacts:
   + A session video built from the frames.
   + A transcript of the session.
   + An HTML report.

1. Replay Session delivers the artifacts to your Amazon S3 bucket. Processing and delivery continue for a few minutes after the session ends.

Frames, metadata, tool responses, and finished artifacts that are awaiting delivery remain in AWS-owned storage for up to 15 days, and then expire. This retention period applies only to the copy that Replay Session holds during processing. The artifacts in your bucket are retained according to the lifecycle configuration of your bucket, which you control.

## What Replay Session records and how it is processed
<a name="agent-access-replay-session-data"></a>

Before you turn on Replay Session, review what it records and how it processes that content. By turning on Replay Session, you accept the following:
+ **Whole-screen capture**. Each frame records the entire screen as it appears just before the agent acts. Anything visible on the screen at that moment is in the recording.
+ **Typed text**. Text that the agent types is saved in the `arguments` field of the per-action metadata, and can appear in the transcript.
+ **No redaction**. Replay Session doesn't redact sensitive data from frames, metadata, or artifacts.
+ **Processing by Amazon Bedrock**. Replay Session sends frames and metadata to Amazon Bedrock to produce the AI-generated transcript. This content is processed in AWS Regions other than the Region where the session runs. For details, see [Cross-Region inference for Replay Session](#agent-access-replay-session-cross-region).

## Cross-Region inference for Replay Session
<a name="agent-access-replay-session-cross-region"></a>

Review this section before you turn on Replay Session.

Replay Session uses Amazon Bedrock cross-Region inference to produce the AI-generated transcript. In-Region inference for the model that Replay Session uses isn't available in any of the AWS Regions that support Replay Session. As a result, inference requests, including the frames and metadata from your sessions, can be routed to and processed in AWS Regions other than the Region where your session runs:
+ **Geographic cross-Region inference**. Where Amazon Bedrock offers an inference profile for the geography of your Region, requests are routed only to Regions within that geography, such as North America, Europe, or Australia.
+ **Global cross-Region inference**. Where no inference profile exists for the geography of your Region, requests can be routed to commercial AWS Regions worldwide.

The following table shows how requests are routed for each Region where Replay Session is available.


**Cross-Region inference routing for Replay Session**  

| Session Region | Inference Regions | 
| --- | --- | 
| US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2)<br />Canada (Central) (ca-central-1) | US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2)<br />Canada (Central) (ca-central-1) | 
| Europe (Frankfurt) (eu-central-1)<br />Europe (Ireland) (eu-west-1)<br />Europe (London) (eu-west-2)<br />Europe (Milan) (eu-south-1)<br />Europe (Paris) (eu-west-3)<br />Europe (Spain) (eu-south-2) | Europe (Frankfurt) (eu-central-1)<br />Europe (Ireland) (eu-west-1)<br />Europe (London) (eu-west-2)<br />Europe (Milan) (eu-south-1)<br />Europe (Paris) (eu-west-3)<br />Europe (Spain) (eu-south-2)<br />Europe (Stockholm) (eu-north-1) | 
| Asia Pacific (Sydney) (ap-southeast-2) | Asia Pacific (Sydney) (ap-southeast-2)<br />Asia Pacific (Melbourne) (ap-southeast-4) | 
| Asia Pacific (Malaysia) (ap-southeast-5)<br />Asia Pacific (Mumbai) (ap-south-1)<br />Asia Pacific (Seoul) (ap-northeast-2)<br />Asia Pacific (Singapore) (ap-southeast-1)<br />Asia Pacific (Tokyo) (ap-northeast-1)<br />South America (São Paulo) (sa-east-1) | [Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 

For the current list of destination Regions in each geography, and for the Regions that a global inference profile can route to, see [Supported Regions and models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html) and [Increase throughput with cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) in the *Amazon Bedrock User Guide*.

Amazon Bedrock doesn't retain your content after it serves an inference request, and doesn't use your content to train models. For more information, see [Data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html) in the *Amazon Bedrock User Guide*.

**Important**  
You are responsible for determining whether cross-Region inference is consistent with your regulatory and data residency obligations. If you require that inference data remain within a specific Region or geography, don't turn on Replay Session in a Region that routes requests outside that Region or geography.

## Destination bucket requirements
<a name="agent-access-replay-session-bucket"></a>

The Amazon S3 bucket that receives Replay Session artifacts must meet the following requirements:
+ The bucket must be in the same AWS account as the principal that creates or updates the stack.
+ The IAM identity that your agent uses to connect to the Model Context Protocol (MCP) service must have the `s3:PutObject` permission on the bucket. Replay Session writes the artifacts as that identity.

The artifacts in your bucket are encrypted with the default encryption settings of the bucket. To use your own AWS KMS key for the artifacts in your bucket, see [Encrypting delivered artifacts in your bucket](agent-access-replay-session-encryption.md#agent-access-replay-session-encryption-delivered).

Replay Session doesn't add a signature or checksum to the artifacts that it delivers. To protect the artifacts from being changed or deleted, we recommend that you turn on versioning and Amazon S3 Object Lock for the bucket. For more information, see [Retaining multiple versions of objects with S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) and [Locking objects with Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) in the *Amazon S3 User Guide*.

## Turn on Replay Session
<a name="agent-access-replay-session-enable"></a>

To turn on Replay Session, set the following fields in the `AgentAccessConfig` when you call `CreateStack` or `UpdateStack`:
+ `ReplaySessionEnabled`. Set to `true` to record agent sessions on the stack.
+ `S3BucketArn`. The ARN of the Amazon S3 bucket that receives the artifacts.
+ `KmsKeyArn` (optional). The key ARN of a customer managed key that encrypts the recording while Replay Session processes it. For more information, see [Encryption at rest for Replay Session](agent-access-replay-session-encryption.md).

The following example creates a stack with Replay Session turned on:

```bash
aws appstream create-stack \
    --name {{your-stack-name}} \
    --agent-access-config '{
        "Settings": [
            {"AgentAction": "COMPUTER_VISION", "Permission": "ENABLED"},
            {"AgentAction": "COMPUTER_INPUT", "Permission": "ENABLED"}
        ],
        "ScreenResolution": "W_1280xH_720",
        "ScreenImageFormat": "PNG",
        "S3BucketArn": "{{arn:aws:s3:::amzn-s3-demo-bucket}}",
        "ReplaySessionEnabled": true,
        "KmsKeyArn": "{{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}"
    }'
```

The identity that your agent uses must keep its Amazon S3 permissions, and its AWS KMS permissions if you use a customer managed key, for the whole session and until processing finishes a few minutes after the session ends. If the identity loses these permissions before processing finishes, the recording can't be delivered.