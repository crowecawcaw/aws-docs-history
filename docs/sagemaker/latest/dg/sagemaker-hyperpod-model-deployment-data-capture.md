

# Data capture for inference on HyperPod
<a name="sagemaker-hyperpod-model-deployment-data-capture"></a>

Amazon SageMaker HyperPod inference data capture enables you to record inference request and response data for model monitoring, debugging, and model improvement. Inference requests flow from the SageMaker AI endpoint to the Application Load Balancer and then to the model pod. You can enable capture independently at each level, from the outermost layer (Tier 1, SageMaker AI endpoint) to the deepest layer (Tier 3, model pod):


**Data capture tiers**  

| Tier | Capture point | What is captured | Amazon S3 path | 
| --- | --- | --- | --- | 
| Tier 1 | SageMaker AI endpoint | Input and output payloads, sampling, AWS KMS encryption | {s3Uri}/{hash}/sme/ | 
| Tier 2 | Application Load Balancer | Access logs (request paths, client IPs, latencies) | {s3Uri}/{hash}/alb/ | 
| Tier 3 | Model pod | Inference input and output payloads with configurable sampling, buffering, and payload size limits. Supports AWS KMS encryption when you provide a key. Captures data closest to the model for the deepest visibility. | {s3Uri}/{hash}/pod/ | 

Tier 1 captures full payloads at the SageMaker AI Runtime API boundary and requires endpoint registration. Use Tier 1 when you need compatibility with SageMaker AI Model Monitor. Tier 3 captures full payloads at the inference container with configurable buffering, sampling, and payload limits, and works without SageMaker AI endpoint registration. Use Tier 3 when you need the deepest visibility closest to the model. Enable any combination — each tier captures at a different point in the request flow.

All tiers write to your Amazon S3 bucket. If you don't specify an `s3Uri`, data is stored in the TLS certificate bucket under a `/data-capture/` prefix by default. Within the bucket, each deployment gets a unique path based on a hash derived from the cluster ARN, namespace, CRD type, and deployment name. The same deployment always generates the same prefix, so data capture artifacts from multiple CRD submissions targeting the same deployment flow to the same Amazon S3 subfolder.

To disable data capture for a tier, set its `enabled` field to `false` or remove the tier section from your CRD. To disable all data capture, remove the `dataCapture` section entirely.

## Configuring data capture
<a name="sagemaker-hyperpod-model-deployment-data-capture-config"></a>

Enable data capture by adding a `dataCapture` section to your `InferenceEndpointConfig` or `JumpStartModel` CRD. The `dataCapture` block contains a single `s3Uri` (optional) and one or more tier configurations. The following example shows the overall structure with all three tiers enabled:

```
  dataCapture:
    s3Uri: s3://my-capture-bucket/captures/   # Optional. Defaults to TLS bucket.
    sagemakerEndpoint:
      enabled: true
      # Tier 1 fields...
    loadBalancer:
      enabled: true
    modelPod:
      enabled: true
      # Tier 3 fields...
```

`dataCapture.s3Uri` (Optional, String)  
The Amazon S3 URI where captured data is stored. If not specified, the TLS certificate bucket is used with a `/data-capture/` prefix. Maximum length: 512 characters. The bucket must be in the same account as the cluster.

### Tier 1: SageMaker AI endpoint capture
<a name="sagemaker-hyperpod-model-deployment-data-capture-tier1"></a>

Tier 1 uses SageMaker AI's native `DataCaptureConfig` to capture inference input and output payloads at the endpoint level. This is the outermost capture point and is compatible with SageMaker AI Model Monitor for automated data quality monitoring. For more information about SageMaker AI data capture, see [Capture data from real-time endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html).

```
    sagemakerEndpoint:
      enabled: true
      initialSamplingPercentage: 100
      kmsKeyId: arn:aws:kms:us-east-2:123456789012:key/my-key-id
      captureOptions:
        - captureMode: Input
        - captureMode: Output
      captureContentTypeHeader:
        jsonContentTypes:
          - application/json
```

`sagemakerEndpoint.enabled` (Required, Boolean)  
Set to `true` to enable Tier 1 capture.

`sagemakerEndpoint.initialSamplingPercentage` (Optional, Integer, 0–100)  
Percentage of inference requests to capture. Default: `100` (all requests are captured).

`sagemakerEndpoint.captureOptions` (Optional, List)  
Specifies whether to capture the inference request payload (`Input`), the inference response payload (`Output`), or both. Each item has a `captureMode` field set to `Input` or `Output`. Default: `[Input, Output]` (both request and response are captured). Maximum: 32 items.

`sagemakerEndpoint.kmsKeyId` (Optional, String)  
ARN, key ID, alias name, or alias ARN of a AWS KMS key for encrypting captured data at rest. When specified, captured data is encrypted with this key. When omitted, data is encrypted with the default Amazon S3 bucket encryption settings. Maximum length: 2048 characters.

`sagemakerEndpoint.captureContentTypeHeader` (Optional)  
Specifies how to interpret the content type of captured payloads. Supports `jsonContentTypes` and `csvContentTypes` arrays. Maximum: 10 items each.

### Tier 2: Load balancer capture
<a name="sagemaker-hyperpod-model-deployment-data-capture-tier2"></a>

Tier 2 enables ALB access logs, capturing request metadata such as client IPs, request paths, and latencies.

```
    loadBalancer:
      enabled: true
```

`loadBalancer.enabled` (Required, Boolean)  
Set to `true` to enable Tier 2 capture.

**Note**  
ALB access logs capture request metadata including URLs and query parameters. Use POST request bodies rather than query parameters for sensitive inputs. ALB logs do not support AWS KMS encryption and use Amazon S3 default encryption only.

### Tier 3: Model pod capture
<a name="sagemaker-hyperpod-model-deployment-data-capture-tier3"></a>

Tier 3 captures inference input and output payloads at the model pod level, providing the deepest visibility into inference traffic. Use this tier when you need fine-grained control over buffering, payload size limits, and capture closest to the model.

```
    modelPod:
      enabled: true
      initialSamplingPercentage: 100
      kmsKeyId: arn:aws:kms:us-east-2:123456789012:key/my-key-id
      captureOptions:
        - captureMode: Input
        - captureMode: Output
      bufferConfig:
        batchSize: 100
        flushIntervalSeconds: 60
      payloadConfig:
        maxPayloadSizeKB: 1024
```

`modelPod.enabled` (Required, Boolean)  
Set to `true` to enable Tier 3 capture.

`modelPod.initialSamplingPercentage` (Optional, Integer, 0–100)  
Percentage of inference requests to capture. Default: `100` (all requests are captured).

`modelPod.captureOptions` (Optional, List)  
Specifies whether to capture the inference request payload (`Input`), the inference response payload (`Output`), or both. Each item has a `captureMode` field set to `Input` or `Output`. Default: `[Input, Output]` (both request and response are captured). Maximum: 32 items.

`modelPod.kmsKeyId` (Optional, String)  
ARN, key ID, alias name, or alias ARN of a AWS KMS key for encrypting captured data at rest. When specified, captured data is encrypted with this key. When omitted, data is encrypted with the default Amazon S3 bucket encryption settings. Maximum length: 2048 characters.

`modelPod.bufferConfig.batchSize` (Optional, Integer, 1–1000)  
Number of inference requests to batch before flushing. Default: `10`.

`modelPod.bufferConfig.flushIntervalSeconds` (Optional, Integer, 10–300)  
Maximum time in seconds that a batch is held before being flushed, regardless of whether the batch size has been reached. Default: `60`.

`modelPod.payloadConfig.maxPayloadSizeKB` (Optional, Integer)  
Maximum payload size in KB per request. Payloads exceeding this limit are truncated. If not set, the entire payload is captured.

## Update Addon
<a name="sagemaker-hyperpod-model-deployment-update-addon"></a>

**Prerequisites: Authenticate and connect to your EKS cluster**

Authenticate to your AWS account. Before connecting, collect EKS cluster name, region, and HyperPod cluster ARN:

```
CLUSTER={{EKS_CLUSTER_NAME}}
REGION={{REGION}}
HP_ARN={{HYPERPOD_CLUSTER_ARN}}
```

Connect to your EKS cluster:

```
aws eks update-kubeconfig --region {{REGION}} --name {{EKS_CLUSTER_NAME}}
```

Update the addon configuration:

```
VERSION=$(aws eks describe-addon --cluster-name $CLUSTER --addon-name amazon-sagemaker-hyperpod-inference --region $REGION --query 'addon.addonVersion' --output text)
CURRENT_CONFIG=$(aws eks describe-addon --cluster-name $CLUSTER --addon-name amazon-sagemaker-hyperpod-inference --region $REGION --query 'addon.configurationValues' --output text)
NEW_CONFIG=$(echo "$CURRENT_CONFIG" | jq --arg arn "$HP_ARN" '. + {hyperpodClusterArn: $arn}')

aws eks update-addon \
--cluster-name $CLUSTER \
--addon-name amazon-sagemaker-hyperpod-inference \
--addon-version "$VERSION" \
--configuration-values "$NEW_CONFIG" \
--resolve-conflicts OVERWRITE \
--region $REGION
```

**Wait for the Addon to be active and then deploy the models**

## Updating permissions for existing clusters
<a name="sagemaker-hyperpod-model-deployment-data-capture-iam"></a>

To enable data capture on your HyperPod Inference deployments, configure the following IAM permissions.

1. **Inference Operator Execution Role**

   Add the following S3 permission:

   ```
   {
       "Sid": "DataCaptureS3Access",
       "Effect": "Allow",
       "Action": "s3:PutObject",
       "Resource": "arn:aws:s3:::hyperpod-tls*/data-capture/*",
       "Condition": {
           "StringEquals": {
               "aws:ResourceAccount": "${aws:PrincipalAccount}"
           }
       }
   }
   ```

   Add your bucket name if you want to use a custom S3 bucket.

   If you use a customer-managed KMS key, also add:

   ```
   {
       "Sid": "DataCaptureKmsAccess",
       "Effect": "Allow",
       "Action": [
           "kms:Decrypt",
           "kms:GenerateDataKey"
       ],
       "Resource": "arn:aws:kms:*:*:key/*",
       "Condition": {
           "StringLike": {
               "kms:ViaService": "s3.*.amazonaws.com",
               "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::hyperpod-tls*"
           },
           "StringEquals": {
               "aws:ResourceAccount": "${aws:PrincipalAccount}"
           }
       }
   }
   ```

1. **S3 CSI Driver Role**

   Add the following S3 permission:

   ```
   {
       "Sid": "DataCaptureWriteAccess",
       "Effect": "Allow",
       "Action": [
           "s3:PutObject",
           "s3:AbortMultipartUpload"
       ],
       "Resource": "arn:aws:s3:::hyperpod-tls*/data-capture/*",
       "Condition": {
           "StringEquals": {
               "aws:ResourceAccount": "${aws:PrincipalAccount}"
           }
       }
   }
   ```

   If you use a customer-managed KMS key, also add:

   ```
   {
       "Sid": "DataCaptureKmsAccess",
       "Effect": "Allow",
       "Action": [
           "kms:Decrypt",
           "kms:GenerateDataKey",
           "kms:DescribeKey"
       ],
       "Resource": "arn:aws:kms:*:*:key/*",
       "Condition": {
           "StringLike": {
               "kms:ViaService": "s3.*.amazonaws.com"
           },
           "StringEquals": {
               "aws:ResourceAccount": "${aws:PrincipalAccount}"
           }
       }
   }
   ```

1. **S3 Bucket Policy**

   Add this bucket policy only if you enable load balancer data capture (Tier 2) to allow ALB to write access logs. Replace `$ACCOUNT_ID` with your AWS account ID.

   ```
   {
       "Sid": "AllowALBAccessLogDelivery",
       "Effect": "Allow",
       "Principal": {
           "Service": "logdelivery.elasticloadbalancing.amazonaws.com"
       },
       "Action": "s3:PutObject",
       "Resource": "arn:aws:s3:::hyperpod-tls*/data-capture/*",
       "Condition": {
           "StringEquals": {
               "aws:SourceAccount": "$ACCOUNT_ID"
           }
       }
   }
   ```

## Best practices
<a name="sagemaker-hyperpod-model-deployment-data-capture-perf"></a>
+ Use `initialSamplingPercentage` to control the volume of captured data. Start with a lower percentage in production and increase as needed.
+ Use `payloadConfig.maxPayloadSizeKB` (Tier 3) to cap the size of captured payloads and control storage costs.
+ Specify a `kmsKeyId` for Tier 1 and Tier 3 if your workload requires encryption at rest with your own AWS KMS key.