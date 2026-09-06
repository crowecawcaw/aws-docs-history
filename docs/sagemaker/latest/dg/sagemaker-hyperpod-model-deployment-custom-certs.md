

# Custom certificates and Route 53 DNS management for HyperPod Inference
<a name="sagemaker-hyperpod-model-deployment-custom-certs"></a>

The following steps show you how to use your own ACM certificates for HyperPod inference endpoints and optionally configure the operator to manage Route 53 DNS records for your custom domain.

With custom certificates, you provide an ACM certificate ARN and the operator attaches it to the Application Load Balancer (ALB), monitors its health, and supports automatic renewal detection. The operator supports publicly trusted ACM certificates, AWS Private CA certificates, and certificates imported from external CAs.

Custom certificates can be used on their own or combined with Route 53 DNS management. Route 53 DNS management requires a custom certificate and uses the domain name from your certificate configuration to create and manage DNS records.

## Prerequisites
<a name="sagemaker-hyperpod-model-deployment-custom-certs-prereqs"></a>

Before you begin, verify that you've:
+ Set up inference capabilities on your Amazon SageMaker HyperPod clusters. For more information, see [Setting up your HyperPod clusters for model deployment](sagemaker-hyperpod-model-deployment-setup.md).
+ Installed [kubectl](https://kubernetes.io/docs/reference/kubectl/) in your terminal.
+ Provisioned or imported a TLS certificate in ACM in the same AWS Region as your HyperPod cluster. The certificate must be in the **Issued** state and must include a certificate chain (intermediate and root CA). Self-signed certificates imported to ACM are not supported as custom certificates because they lack a certificate chain.
+ (For Route 53 DNS management) Created a Route 53 hosted zone for your domain. Public hosted zones are recommended. Private hosted zones work for record creation, but the operator verifies DNS resolution using the pod's DNS resolver, which relies on the VPC DNS resolver. For private hosted zones, the VPC must have DNS resolution and DNS hostnames enabled, and the private hosted zone must be associated with the cluster's VPC.

## Configure IAM permissions
<a name="sagemaker-hyperpod-model-deployment-custom-certs-iam"></a>

The inference operator's execution role requires additional permissions for custom certificates and Route 53 DNS management. Add the following policies to your HyperPod Inference execution role.

### ACM and Amazon S3 permissions for custom certificates
<a name="sagemaker-hyperpod-model-deployment-custom-certs-iam-acm"></a>

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ACMCustomCertificateAccess",
            "Effect": "Allow",
            "Action": [
                "acm:DescribeCertificate",
                "acm:GetCertificate"
            ],
            "Resource": "arn:aws:acm:<region>:<account-id>:certificate/*"
        },
        {
            "Sid": "S3CertificateUpload",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectTagging"
            ],
            "Resource": "arn:aws:s3:::<tls-certificate-bucket>/*",
            "Condition": {
                "StringEquals": {
                    "s3:RequestObjectTag/CreatedBy": "HyperPodInference"
                }
            }
        }
    ]
}
```

**Note**  
If your Amazon S3 bucket name starts with `hyperpod-tls`, the Amazon S3 permissions are already included in the `AmazonSageMakerHyperPodInferenceAccess` managed policy and you only need to add the ACM statement.

### Route 53 permissions for DNS management
<a name="sagemaker-hyperpod-model-deployment-custom-certs-iam-r53"></a>

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Route53DNSManagement",
            "Effect": "Allow",
            "Action": [
                "route53:GetHostedZone",
                "route53:ListResourceRecordSets",
                "route53:ChangeResourceRecordSets"
            ],
            "Resource": "arn:aws:route53:::hostedzone/<hosted-zone-id>"
        }
    ]
}
```

Replace `<region>`, `<account-id>`, `<tls-certificate-bucket>`, and `<hosted-zone-id>` with your actual values. You can scope the ACM resource ARN to specific certificates for tighter security.

## Configure a custom certificate
<a name="sagemaker-hyperpod-model-deployment-custom-certs-configure"></a>

To use a custom certificate, add the `customCertificateConfig` section to your `tlsConfig` in the `InferenceEndpointConfig` or `JumpStartModel` spec. The `tlsConfig` and `dnsConfig` fields are identical in both CRDs.

The following fields are available in `customCertificateConfig` and `tlsConfig`:

`tlsConfig.customCertificateConfig.acmArn` (Required, String)  
The ARN of your ACM certificate. Must be in the **Issued** state.

`tlsConfig.customCertificateConfig.domainName` (Required, String)  
The domain name to use from the certificate.  
+ Must be a specific domain, not a wildcard. For wildcard certificates (for example, `*.example.com`), specify the specific subdomain (for example, `api.example.com`).
+ Must be lowercase.
+ Must match one of the domain names listed in the certificate.

`tlsConfig.tlsCertificateOutputS3Uri` (Conditional, String)  
Amazon S3 URI where the operator uploads the public certificate. Required unless the operator was installed with the `TLS_CERTIFICATE_OUTPUT_S3URI` environment variable configured. If you're unsure whether this was set, specify it explicitly.

The following is an example YAML file for creating an endpoint with a custom certificate.

```
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: InferenceEndpointConfig
metadata:
  name: my-model
  namespace: my-namespace
spec:
  modelName: my-llm
  instanceType: ml.g5.24xlarge
  invocationEndpoint: v1/chat/completions
  replicas: 2
  modelSourceConfig:
    modelSourceType: s3
    s3Storage:
      bucketName: my-model-bucket
      region: us-west-2
    modelLocation: models/my-llm
  tlsConfig:
    customCertificateConfig:
      acmArn: arn:aws:acm:us-west-2:123456789012:certificate/abc12345-1234-1234-1234-abc123456789
      domainName: api.example.com
    tlsCertificateOutputS3Uri: s3://my-tls-bucket
  worker:
    image: my-inference-image:latest
    modelInvocationPort:
      containerPort: 8000
      name: http
    modelVolumeMount:
      name: model-weights
      mountPath: /opt/ml/model
    resources:
      limits:
        nvidia.com/gpu: "4"
      requests:
        cpu: "6"
        memory: 30Gi
        nvidia.com/gpu: "4"
```

You can add `customCertificateConfig` to a deployment that is already running. The operator detects the change on the next reconciliation, validates the certificate, attaches it to the ALB, and uploads the public certificate to Amazon S3. No downtime or redeployment is required.

**Important**  
If you remove the `customCertificateConfig` section from a running deployment, the operator falls back to generating a new self-signed certificate. This replaces your CA-signed certificate on the ALB.

## Configure Route 53 DNS management
<a name="sagemaker-hyperpod-model-deployment-custom-certs-dns"></a>

Route 53 DNS management requires a custom certificate to be configured and uses the domain name from `tlsConfig.customCertificateConfig.domainName`. If you have not configured a custom certificate, see [Configure a custom certificate](#sagemaker-hyperpod-model-deployment-custom-certs-configure) first.

To enable Route 53 DNS management, add the `dnsConfig` section to your spec:

```
spec:
  tlsConfig:
    customCertificateConfig:
      acmArn: arn:aws:acm:us-west-2:123456789012:certificate/abc12345-1234-1234-1234-abc123456789
      domainName: api.example.com
    tlsCertificateOutputS3Uri: s3://my-tls-bucket
  dnsConfig:
    hostedZoneId: Z1234567890ABC
```

The `dnsConfig` section can be added at the same time as `customCertificateConfig`, or added later to an existing deployment. The operator creates the DNS records on the next reconciliation without restarting your pods.

When you deploy with `dnsConfig`, the operator:

1. Validates the hosted zone exists and that your domain belongs to the hosted zone (for example, `api.example.com` requires a hosted zone for `example.com`).

1. Checks for existing A records at the target domain to prevent accidental overwrites.

1. Creates an **A record** (alias) pointing your domain to the ALB, and a **TXT record** with an ownership marker (`hyperpod-inference/owner=<namespace>/<name>`) to prevent conflicts between endpoints. Do not modify or delete the TXT record manually.

1. Polls DNS resolution every 30 seconds until the domain resolves, then marks the status as `Active`. If the record doesn't resolve within 10 minutes, the status transitions to `Error`.

**Note**  
Route 53 DNS management is non-blocking. Errors in DNS record creation or propagation do not prevent your inference endpoint from reaching the `Ready` state. The endpoint remains accessible through the ALB's default hostname. Check the `dnsStatus` section in the resource status for DNS-specific errors.

## Use a custom certificate without Route 53 DNS management
<a name="sagemaker-hyperpod-model-deployment-custom-certs-no-dns"></a>

Route 53 DNS management is optional. If you want to manage your own DNS records, omit the `dnsConfig` section and configure your domain manually.

To find the ALB hostname for your deployment, the ingress name depends on whether intelligent routing is enabled.

**Without intelligent routing:** The ingress is named `alb-<deployment-name>` in your namespace.

```
kubectl get ingress alb-<deployment-name> -n <namespace> \
  -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
```

**With intelligent routing:** The ingress is named `alb-<deployment-name>-<namespace>` in the `hyperpod-inference-system` namespace.

```
kubectl get ingress alb-<deployment-name>-<namespace> -n hyperpod-inference-system \
  -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
```

Create a DNS record in your DNS provider pointing your domain to this ALB hostname:
+ **Route 53** — Create an **A record** with **Alias** enabled, pointing to the ALB.
+ **Other DNS providers** — Create a **CNAME record** pointing your domain to the ALB DNS name. CNAME records cannot be used at the root domain (for example, `example.com`); use a subdomain like `api.example.com`.

**Note**  
If the ALB is recreated (for example, after deleting and redeploying the endpoint), the ALB hostname changes. You must update your DNS record manually. Route 53 DNS management handles this automatically.

## Verify the status of your deployment
<a name="sagemaker-hyperpod-model-deployment-custom-certs-verify"></a>

### Check the custom certificate status
<a name="sagemaker-hyperpod-model-deployment-custom-certs-verify-cert"></a>

```
kubectl describe InferenceEndpointConfig my-model -n my-namespace
```

Look for the `tlsCertificate` section in the status:

```
Status:
  Tls Certificate:
    Certificate ARN:    arn:aws:acm:us-west-2:123456789012:certificate/abc12345-...
    Certificate Health: Valid
    Certificate Domain Names:
      api.example.com
    Last Cert Expiry Time: 2027-04-23T00:00:00Z
```

Certificate health values:
+ **Valid** — Certificate is more than 60 days from expiration.
+ **Expiring** — Certificate expires within 60 days. A Kubernetes warning event (`CertificateExpiring`) is emitted.
+ **Expired** — Certificate has expired. A Kubernetes warning event (`CertificateExpired`) is emitted.

The operator checks certificate expiration every 24 hours. When it detects that a certificate has been renewed in ACM (the `NotAfter` date changes), it automatically re-uploads the public certificate to Amazon S3 and emits a `CertificateRenewed` event.

### Check the DNS status
<a name="sagemaker-hyperpod-model-deployment-custom-certs-verify-dns"></a>

Look for the `dnsStatus` section:

```
Status:
  Dns Status:
    Managed By Operator: true
    Record Name:         api.example.com
    Hosted Zone Id:      Z1234567890ABC
    Dns Health:          Active
    Message:             DNS record resolves successfully
```

DNS health values:
+ **Active** — DNS record resolves successfully. Your custom domain is ready to use.
+ **Pending** — DNS records have been created in Route 53 but haven't propagated yet. The operator rechecks every 30 seconds.
+ **Error** — DNS record creation or propagation failed. Check the `Message` field for details.

### Test the deployed endpoint
<a name="sagemaker-hyperpod-model-deployment-custom-certs-verify-test"></a>

If you configured Route 53 DNS management, invoke your endpoint using your custom domain after the DNS status shows `Active`. If you configured only a custom certificate without DNS management, use the ALB hostname from the ingress (see [Use a custom certificate without Route 53 DNS management](#sagemaker-hyperpod-model-deployment-custom-certs-no-dns)).

```
curl -X POST https://api.example.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "my-llm", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Note**  
To invoke through the SageMaker AI endpoint, set `endpointName` in your `InferenceEndpointConfig` or `sageMakerEndpoint.name` in your `JumpStartModel` spec. If `endpointName` is not set, no SageMaker AI endpoint is created and only direct ALB invocation is available.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name my-model \
  --content-type "application/json" \
  --body '{"model": "my-llm", "messages": [{"role": "user", "content": "Hello"}]}' \
  --region us-west-2 \
  --cli-binary-format raw-in-base64-out \
  /dev/stdout
```

## Manage your custom certificates and DNS records
<a name="sagemaker-hyperpod-model-deployment-custom-certs-manage"></a>

**Changing the domain or hosted zone**

You can update the `domainName` (in `customCertificateConfig`) or `hostedZoneId` (in `dnsConfig`) on a running deployment. Changing the domain name triggers both certificate re-validation and DNS cutover — the new domain must be valid in your ACM certificate (as a SAN or wildcard match).

The operator performs a safe cutover:

1. Creates new DNS records in the new zone or for the new domain.

1. Verifies the new records resolve.

1. Deletes the old DNS records only after the new records are confirmed active.

During the transition, both old and new domains resolve to the ALB. The TXT ownership record has a TTL of 300 seconds (5 minutes), so DNS clients may cache the old record for up to 5 minutes after cleanup.

**Cleanup**

When you delete the `InferenceEndpointConfig` or remove the `dnsConfig` section, the operator automatically deletes the Route 53 A and TXT records it created. The operator only deletes records that it owns (verified by the ownership TXT record).

## Troubleshooting
<a name="sagemaker-hyperpod-model-deployment-custom-certs-troubleshooting"></a>

Use these debugging steps if your custom certificate or DNS configuration isn't working as expected.
+ **Deployment fails with Amazon S3 access error.** Verify the Amazon S3 bucket specified in `tlsCertificateOutputS3Uri` exists and is in the same Region. Verify the operator's execution role has `s3:PutObject` and `s3:PutObjectTagging` permissions on the bucket. The operator validates Amazon S3 write access by uploading a zero-byte test object during initial deployment.
+ **Certificate validation fails.** Verify the ACM certificate is in the `ISSUED` state: `aws acm describe-certificate --certificate-arn <arn> --region <region>`. Verify the `domainName` matches a domain or SAN in the certificate. For wildcard certificates (`*.example.com`), use a specific subdomain like `api.example.com`.
+ **DNS record creation fails.** Verify the hosted zone ID is correct and the operator's execution role has Route 53 permissions. Verify the domain belongs to the hosted zone (for example, `api.example.com` requires a hosted zone for `example.com`). If you see an NS delegation conflict, use the hosted zone ID of the delegated zone instead. If you see a record conflict, another endpoint or external process owns the A record at that domain.
+ **DNS record shows Pending for extended time.** Verify the hosted zone's NS records are properly delegated from the parent domain registrar. The operator uses the pod's DNS resolver (typically CoreDNS), which may cache results. After 10 minutes without resolution, the status transitions to `Error`.
+ **Certificate expiration warnings.** Renew or replace the certificate in ACM. For ACM-issued certificates, ACM handles renewal automatically. For imported certificates, import a new certificate. The operator detects renewal automatically and re-uploads the public certificate to Amazon S3.