

# Enable users to resume chat conversations across active Regions
<a name="resume-chat-across-regions"></a>

Customers often start a chat, then leave the conversation and return later to continue chatting. When you run Connect Customer Global Resiliency (ACGR) across your linked Regions with global routing, or in a business continuity setup, you can let users resume these conversations with the context, metadata, and transcripts carried forward across Regions. Users don't need to repeat themselves when they return to a chat, regardless of which active Region serves them.

For example, an end user can start a chat in US East (N. Virginia) and later come back to it in the linked US West (Oregon) Region, continuing the same conversation with an agent with full conversation history.

Connect Customer achieves persistent chat across Regions through a process called chat rehydration. Chat rehydration lets you retrieve chat transcripts and attachments from previous chat contacts and display them to customers and agents, so agents can continue offering a personalized experience regardless of their active Region.

**Important**  
You must adopt [Global routing](global-routing-across-acgr-regions.md) to take advantage of this feature.

Connect Customer supports two types of rehydration:
+ `ENTIRE_PAST_SESSION`: Starts a new chat session and rehydrates all chat segments from past chat sessions.
+ `FROM_SEGMENT`: Starts a new session and rehydrates from the specified past chat segment.

## How to enable persistent chat across Regions
<a name="resume-chat-enable"></a>

To enable persistent chat across Regions, you must pass the previous contact ID and use the **Create persistent contact association** block in your flows.

**Note**  
Although you can pass the previous contact ID in the [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) API, we recommend using the **Create persistent contact association** block for persistent chat across Regions. The block still creates the chat contact if the previous contact ID is not available.

Connect Customer does not populate the previous contact ID automatically. You must maintain an external data store that stores the previous contact ID for each customer, and design that data store to replicate entries across your ACGR linked Regions so the information is available in both Regions. For example, you can use DynamoDB global tables across your ACGR Regions to maintain the previous contact ID and replicate it across Regions.

There are two ways to create entries in the data store:
+ Use chat message streaming to create an entry when a chat has ended.
+ Inspect contact events and use an Lambda function to create entries in your data store.

After you set up the data store, retrieve the previous contact ID for the customer and provide it dynamically through contact attributes in the **Create persistent contact association** flow block.

In addition, grant the Amazon S3 and AWS KMS permissions described in the following sections for the bucket and key where the chat transcripts and attachments are stored. These permissions give the Connect Customer service-linked role access to your Amazon S3 bucket and AWS KMS key so it can decrypt and present the chat transcript.

## Resource policy: Amazon S3 bucket
<a name="resume-chat-s3-policy"></a>

Buckets in the source and replica Regions must carry the other Region's Connect Customer service-linked role. For example, the Amazon S3 bucket in US East (N. Virginia) must include the US West (Oregon) Connect Customer instance's service-linked role (SLR) ARN; similarly, the Amazon S3 bucket in US West (Oregon) Region must include the US East (N. Virginia) Connect Customer instance's service-linked role (SLR) ARN.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "OptionDCrossRegionReplicaSLRRead",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{123456789012}}:role/aws-service-role/connect.amazonaws.com/AWSServiceRoleForAmazonConnect_{{unique-suffix}}"
            },
            "Action": [
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::{{bucket-name}}",
                "arn:aws:s3:::{{bucket-name}}/*"
            ]
        }
    ]
}
```

Replace the following values:
+ The account ID and `AWSServiceRoleForAmazonConnect_` suffix with the alternate Region's Connect Customer SLR (from the **Account Overview** page in the console).
+ {{bucket-name}} with your Amazon S3 bucket.

To obtain the Connect Customer SLR information, navigate to the **Account Overview** section in the AWS Management Console.

![The Amazon Connect Account overview page with the service-linked role highlighted.](https://docs.aws.amazon.com/connect/latest/adminguide/images/chat-rehydration-account-overview-slr.png)


## Resource policy: AWS KMS
<a name="resume-chat-kms-policy"></a>

The AWS Key Management Service (AWS KMS) keys in the source and replica Regions must carry the other Region's Connect Customer service-linked role (SLR) ARN. For example, the AWS KMS key in US East (N. Virginia) must include the US West (Oregon) Connect Customer instance's service-linked role (SLR) ARN; similarly, the AWS KMS key in US West (Oregon) must include the US East (N. Virginia) Connect Customer instance's SLR ARN.

```
{
    "Sid": "OptionDCrossRegionReplicaSLRDecrypt",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::{{123456789012}}:role/aws-service-role/connect.amazonaws.com/AWSServiceRoleForAmazonConnect_{{unique-suffix}}"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:DescribeKey"
    ],
    "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{key-id}}"
}
```

Replace the following values:
+ The account ID and `AWSServiceRoleForAmazonConnect_` suffix with the alternate Region's Connect Customer SLR (from the **Account Overview** page in the console).
+ {{key-id}} with your AWS KMS key ID.

**Note**  
You can avoid using the unique suffix shown and instead use the SLR specific to your Connect Customer instance.

Use the following table to identify which permissions you need and when.


| **Scenario** | **Permission update** | 
| --- | --- | 
| You're using an AWS managed AWS KMS key and the Amazon S3 bucket created by your Connect Customer instance. | No permission updates are needed. The permissions are automatically replicated and cross-Region transcription and attachments work. | 
| You're using an AWS managed AWS KMS key and an Amazon S3 bucket created by you. | You must update the Amazon S3 bucket policy. Include the alternate Region Connect Customer SLR information. Perform this action across both Regions. | 
| You're using a customer managed AWS KMS key (CMK) and an Amazon S3 bucket created by you. | You must update the Amazon S3 bucket policy and the AWS KMS permissions. Include the alternate Region Connect Customer SLR information in the local Region Amazon S3 bucket and CMK. Perform this action across both Regions. | 
| You're using a customer managed AWS KMS key (CMK) and the Amazon S3 bucket created by your Connect Customer instance. | You must update the AWS KMS key permissions. Include the alternate Region Connect Customer SLR information in the local Region CMK permissions. Perform this action across both Regions. | 

**Important**  
Connect Customer Global Resiliency does not replicate your file attachment configuration — the allowed file types and the file size limit — across Regions. Configure attachment options in each Region. For more information, see [Step 3: Configure attachment file types and size limits](enable-attachments.md#step3-configure-attachment-options).

## Message streaming across Regions
<a name="resume-chat-message-streaming"></a>

With [Global routing](global-routing-across-acgr-regions.md), you can evenly distribute your agents and contacts across ACGR active Regions. If you have enabled **Enable message streaming** in the Connect Customer instance settings, chat message streaming is available in the Region the contact originated in. For example, if the chat contact originated in US East (N. Virginia) and was routed to an agent in US West (Oregon), chat message streaming is available in the US East (N. Virginia) Region.

## Example use case
<a name="resume-chat-example"></a>

For example, a customer starts a chat session:
+ Agent a1 accepts the chat in US East (N. Virginia), and the conversation starts between the customer and agent a1. The contact ID C1 for this contact might be `11111111-aaaa-bbbb-1111-111111111111`.
+ Agent a1 ends the chat.
+ Later, the customer returns and wants to resume their past chat session.
+ This new chat request is routed to the US West (Oregon) ACGR instance.
+ When the contact is routed to the flow, you have an Lambda function that invokes the data store to look for the previous contact ID for this customer. This contact ID (`11111111-aaaa-bbbb-1111-111111111111`) is passed as an attribute to the **Create persistent contact association** flow block. In the block you can choose the rehydration to start from a segment or the entire session.

**Expected behavior**: Depending on the rehydration type selected in the block, the chat transcript and attachments that are part of the session or segment are rehydrated and available for the customer and the agent.