

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Expected costs
<a name="expected-costs"></a>

Review this section before you enable large-scale decryption to anticipate costs. You pay for the AWS resources that the template creates in your account, and for the AWS KMS requests made with your keys. The Wickr-managed processing components run in the service account and are not billed to your account. The figures in this section are estimates based on the behavior of the current template version. Actual costs depend on your message volume, attachment sizes, how often you decrypt, and your Region. For current prices, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/), [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/), [Step Functions pricing](https://aws.amazon.com/step-functions/pricing/), [Lambda pricing](https://aws.amazon.com/lambda/pricing/), and [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

## AWS KMS costs
<a name="costs-kms"></a>

AWS KMS costs have two parts: a monthly charge per customer managed key, and a per-request charge. For current prices in your Region, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/). The template creates up to two keys: the retention key and an optional password recovery key. You use the recovery key only for the migration from the Docker data retention bot. If you supply your own keys, the template creates no new keys.

**Retaining messages**. The service uses your key each time it processes a message. Plan for approximately *5 AWS KMS requests per retained message*: 2 `Decrypt` requests (the data retention bot's private key and account state) and 3 `GenerateDataKey` requests (the KMS-encrypted message and two replenished bot keys).

As retention consumes the bot's key pool, the service creates additional keys in batches. This adds a small number of requests. Messages with file attachments use additional requests. The retention bucket uses Amazon S3-managed encryption, so writes to Amazon S3 do not generate additional AWS KMS requests.

**Decrypting messages**. On-demand decryption makes approximately *1 AWS KMS `Decrypt` request per stored object* (one per message, and one each for the metadata and the content of a file). Decrypting the same messages again repeats the cost.


| Messages per month | AWS KMS requests to retain them (approx.) | AWS KMS requests to decrypt all of them once (approx.) | 
| --- | --- | --- | 
| 100,000 | 500,000 | 100,000 | 
| 1,000,000 | 5,000,000 | 1,000,000 | 
| 10,000,000 | 50,000,000 | 10,000,000 | 

To estimate your cost, multiply these request counts by the current AWS KMS per-request price for your Region, and add the monthly charge for each key. To measure your actual usage, use the **KMS Key Success** graph on the dashboard, or the AWS KMS `SuccessfulRequest` metric for your key.

## Decryption operation costs
<a name="costs-decryption"></a>

Decryption runs only when you start the decryption state machine, so it adds no cost while idle. Each execution can incur charges for the following:
+ **AWS KMS**: one `Decrypt` request per object, as described in the preceding section.
+ **Lambda**: The decryption function is configured with 10 GB of memory and a 15-minute timeout and processes messages in batches of 200. Cost is the duration multiplied by memory, so it scales with the number of messages and the size of attachments. Large attachments dominate the duration.
+ **Step Functions**: Executions use distributed map states with Express child workflows. Charges are based on the number of child workflow executions, which scales with the number of batches, and on the duration and memory of each child.
+ **Amazon S3**: `LIST` and `GET` requests against the retention bucket, `PUT` requests and storage for the decrypted output and temporary files, and manifests. The template deletes manifests after one day and removes temporary files when an execution completes. Decrypted output contains readable message content and remains in the decrypted bucket until you delete it. Delete it when you no longer need it, or add your own lifecycle rule.

To control cost, decrypt the narrowest date range and `vgroupId` that meets your need, and avoid repeating decryption of the same range. To estimate the cost of a large decryption, run it for a single day first and use the resulting Step Functions, Lambda, and AWS KMS usage to extrapolate.

## Other ongoing costs
<a name="costs-other"></a>
+ **Amazon S3 storage and requests**: Retained objects accumulate for as long as you keep them. Versioning is enabled on the retention bucket, so deleted or overwritten objects continue to incur storage cost until their versions expire. Use lifecycle rules to move older data to lower-cost storage classes.
+ **CloudWatch**: one dashboard, one alarm, and any alarms you add, plus Amazon S3 request metrics on the retention bucket.
+ **CloudWatch Logs**: Decryption executions log at the `ALL` level, retained for one year. Cost scales with how often you decrypt.
+ **CloudTrail**: Every AWS KMS request is a logged event. Costs apply if you have additional trails or data event logging enabled.