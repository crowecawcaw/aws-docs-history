

# Security and data protection for inference routers

Security for inference routers follows the AWS shared responsibility model described in [Configure security in Amazon SageMaker AI](security.md). This topic covers what is specific to inference routers.

## IAM resources and condition keys
<a name="inference-router-security-iam"></a>

An inference router has the following ARN format:

```
arn:{{partition}}:sagemaker:{{region}}:{{account-id}}:inference-router/{{inference-router-name}}
```

You can use `aws:ResourceTag/${TagKey}` to control access to `InvokeInferenceRouter`, `InvokeInferenceRouterAsync`, `DescribeInferenceRouter`, `UpdateInferenceRouter`, and `DeleteInferenceRouter`, and `aws:RequestTag/${TagKey}` and `aws:TagKeys` to control `CreateInferenceRouter`. The `sagemaker:SourceInferenceRouterArn` condition key (ARN type) applies to `sagemaker:InvokeEndpoint` and `sagemaker:InvokeEndpointAsync`. It contains the ARN of the router that sent the request, and is absent on direct calls. For the actions, resources, and condition keys for inference routers, see [Actions, resources, and condition keys for Amazon SageMaker AI](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemaker.html) in the *Service Authorization Reference*.

## How the router authorizes requests to destinations
<a name="inference-router-security-confused-deputy"></a>

The router calls each destination with your caller's own credentials, so your callers can reach only the destinations that they're allowed to invoke. The router doesn't assume a role or share credentials between accounts. SageMaker AI sets `sagemaker:SourceInferenceRouterArn` only on requests that an inference router sends; a caller can't set it. To limit which routers can use your endpoint, add this condition to your IAM policies or endpoint policy with the router's full ARN. Endpoint policies require it on statements that grant another account invoke access. For more information, see [Route requests to endpoints in other AWS accounts](inference-router-cross-account.md).

## Data protection
<a name="inference-router-security-data"></a>

A request is processed in the router's AWS Region and in the Region of the destination that serves it. To keep requests within allowed Regions, see [Keep requests within allowed Regions](#inference-router-security-data-residency). For general guidance, see [Data Protection in Amazon SageMaker AI](data-protection.md).

The router stores the following data:
+ Your router configuration (name, routing targets, destination ARNs, and asynchronous output settings) and your endpoint policies, until you delete them.
+ For each asynchronous request, a record of the request settings: the Amazon S3 input, output, and failure locations, the AWS KMS key ID, content type, `Accept`, inference ID, custom attributes, timeouts, and the destinations tried. Credentials stored for an asynchronous request are encrypted and deleted when the request ends. The router deletes the record 7 days after it accepts the request.

The router doesn't store request or response payloads. For asynchronous requests, inputs and outputs stay in the Amazon S3 locations that you specify.

### Keep requests within allowed Regions
<a name="inference-router-security-data-residency"></a>

A routing target can send any request to any of its destinations. To keep requests within a set of allowed Regions, such as the EU Regions:

1. Create one router for each set of allowed Regions, in one of those Regions. Add only destinations in those Regions.

1. Allow each caller to invoke only the routers for its Regions. In the caller's IAM policy, list the router ARNs in the `Resource` element of `sagemaker:InvokeInferenceRouter` and `sagemaker:InvokeInferenceRouterAsync`.

1. As a guardrail, use a service control policy (SCP) that denies `sagemaker:InvokeEndpoint` and `sagemaker:InvokeEndpointAsync` outside the allowed Regions. The router calls each destination with your caller's credentials, so the SCP applies to requests that the router sends. A deny on `sagemaker:InvokeInferenceRouter` doesn't do this, because `aws:RequestedRegion` for that action is the router's Region. The following SCP also denies direct calls to endpoints outside the allowed Regions.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Deny",
         "Action": ["sagemaker:InvokeEndpoint", "sagemaker:InvokeEndpointAsync"],
         "Resource": "*",
         "Condition": { "StringNotEquals": { "aws:RequestedRegion": ["{{eu-west-1}}", "{{eu-central-1}}"] } }
       }
     ]
   }
   ```

1. To limit which routers can send requests to an endpoint, add the `sagemaker:SourceInferenceRouterArn` condition to the endpoint's policies. For more information, see [How the router authorizes requests to destinations](#inference-router-security-confused-deputy).

For asynchronous requests, the input and output buckets are in the router's Region, so choose a router Region within the allowed set.

When a destination in your own account denies a real-time request, the router retries it once on another destination. If that destination also denies it, you get an `AccessDeniedException`. When a destination in another account denies a request, the caller gets `ServiceUnavailableException` (503) instead of `AccessDeniedException`, so that the caller can't tell whether the endpoint exists. This applies to both real-time and asynchronous requests.

When a destination denies an asynchronous request, the router tries the other destinations. You get an `AccessDeniedException` (same account) or `ServiceUnavailableException` (other account) only if every destination denies the request.

### Encryption at rest
<a name="inference-router-security-encryption-at-rest"></a>

SageMaker AI encrypts the router configuration, endpoint policies, and asynchronous request records at rest with keys that AWS owns and manages. You can't use a customer managed key for this data.

For asynchronous routing targets, if you set `KmsKeyId` in `OutputConfig`, output and failure objects are encrypted with your customer managed key. Otherwise, output uses the default encryption of the output bucket, and failure objects use SSE-KMS with the AWS managed key for Amazon S3 (`aws/s3`). For more information, see [Protect Data at Rest Using Encryption](encryption-at-rest.md).

### Encryption in transit
<a name="inference-router-security-encryption-in-transit"></a>

Calls to an inference router use HTTPS with TLS 1.2 or later. For the hop from the router to a destination in another Region, see [Cross-Region requests](#inference-router-security-cross-region). For more information, see [Protecting Data in Transit with Encryption](encryption-in-transit.md).

### Cross-Region requests
<a name="inference-router-security-cross-region"></a>

When an inference router sends a request to a destination in another Region, it forwards the request over TLS 1.2 or later to the SageMaker AI runtime endpoint in that Region, signed with your credentials. The request is authorized in the destination Region against your IAM policies, the endpoint's resource-based policy, and your service control policies. Traffic between Regions stays on the AWS network. If you call the router through an interface VPC endpoint (AWS PrivateLink), the router reaches every destination, including one in its own Region, through the public SageMaker AI runtime endpoint of the destination's Region, not through PrivateLink.

## Invoke inference routers through an interface VPC endpoint
<a name="inference-router-privatelink"></a>

You can call `InvokeInferenceRouter` and `InvokeInferenceRouterAsync` from your Amazon VPC through an interface VPC endpoint (AWS PrivateLink), which keeps traffic between your Amazon VPC and the router off the public internet. Create the endpoint in the router's AWS Region with the following service name:

```
com.amazonaws.{{region}}.sagemaker.inferencerouter-runtime
```

For steps, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.
+ If you turn on private DNS, the router's default hostname, `inferencerouter-runtime.sagemaker.{{region}}.amazonaws.com`, resolves to your interface VPC endpoint, and you don't have to change your application.
+ The endpoint supports IPv4 only.
+ You can attach a VPC endpoint policy to control which principals can invoke which routers through the endpoint. The following VPC endpoint policy allows one router to be invoked through the endpoint.

  ```json
  {
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": "*",
        "Action": [
          "sagemaker:InvokeInferenceRouter",
          "sagemaker:InvokeInferenceRouterAsync"
        ],
        "Resource": "arn:aws:sagemaker:us-west-2:{{111122223333}}:inference-router/{{my-router}}"
      }
    ]
  }
  ```
+ The interface VPC endpoint covers the call to the router only. The router reaches each destination, in any Region, through the public SageMaker AI runtime endpoint of that Region, not through an interface VPC endpoint. For more information, see [Cross-Region requests](#inference-router-security-cross-region).