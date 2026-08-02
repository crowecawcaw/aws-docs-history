# Configuration

## Amazon S3 source bucket policy

Your source Amazon S3 bucket must grant Connect Customer permission to read recordings from
it.

Add the following policy to your source bucket, replacing the placeholder
values:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "Service": "connect.amazonaws.com" },
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::`SOURCE_BUCKET_NAME`/*",
    "Condition": {
      "StringEquals": { "aws:SourceAccount": "`YOUR_AWS_ACCOUNT_ID`" },
      "ArnEquals": { "aws:SourceArn": "`YOUR_CONNECT_INSTANCE_ARN`" }
    }
  }]
}
```

## Amazon S3 destination bucket policy

The destination bucket is the Amazon S3 bucket configured in the **Call
Recording** section under the **Data Storage** tab of
your Connect Customer console. Connect Customer needs permission to write recordings into this
bucket.

Add the following policy to your destination bucket, replacing the placeholder
values:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "Service": "connect.amazonaws.com" },
    "Action": ["s3:PutObject", "s3:ListBucket"],
    "Resource": [
      "arn:aws:s3:::`DESTINATION_BUCKET_NAME`",
      "arn:aws:s3:::`DESTINATION_BUCKET_NAME`/*"
    ],
    "Condition": {
      "StringEquals": { "aws:SourceAccount": "`YOUR_AWS_ACCOUNT_ID`" },
      "ArnEquals": { "aws:SourceArn": "`YOUR_CONNECT_INSTANCE_ARN`" }
    }
  }]
}
```

## AWS KMS key policy (if encryption enabled)

If your Connect Customer instance has call recording encryption enabled, you must use a
customer-managed AWS KMS key (service-managed keys are not supported). The key policy
must grant the `connect.amazonaws.com` service principal the
`kms:Decrypt`, `kms:Encrypt`,
`kms:GenerateDataKey`, and `kms:DescribeKey` actions,
scoped to your AWS account via the `aws:SourceAccount`
condition.

Example key policy statement:

```
{
  "Sid": "AllowConnectServiceKMSAccess",
  "Effect": "Allow",
  "Principal": { "Service": "connect.amazonaws.com" },
  "Action": ["kms:Decrypt", "kms:Encrypt", "kms:GenerateDataKey", "kms:DescribeKey"],
  "Resource": "*",
  "Condition": {
    "StringEquals": { "aws:SourceAccount": "`YOUR_AWS_ACCOUNT_ID`" }
  }
}
```

## IAM permissions to call APIs

The IAM principal making these API calls must have the following
permissions:

- `connect:CreateContact`
- `connect:CreateAttachedFile`
- `connect:StartContactConversationalAnalyticsJob`

## Transcoding (if required)

Connect Customer does not transcode recordings. Recordings that do not match the required
format (Linear16 PCM WAV, 8 kHz, stereo, 16-bit) will be rejected.

If your source recordings are in a different format, you can use tools such as
FFmpeg to transcode them before ingestion.

Example: Convert an MP3 to the required WAV format:

```
ffmpeg -i input.mp3 -acodec pcm_s16le -ar 8000 -ac 2 output.wav
```

Breakdown:

- `-acodec pcm_s16le` – Linear PCM, 16-bit, little-endian
  (Linear16)
- `-ar 8000` – 8 kHz sample rate
- `-ac 2` – stereo (2 channels)

This produces a WAV file matching the Connect Customer recording format. The channel mapping
(left = customer, right = agent) depends on how your source MP3 is already laid
out.

If you need to swap channels, add:

```
ffmpeg -i input.mp3 -af "pan=stereo|c0=c1|c1=c0" -acodec pcm_s16le -ar 8000 output.wav
```

This swaps left and right so you can get customer on the left and agent on the
right.
