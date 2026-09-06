

# Getting started with inbound external links with custom domains
<a name="get-started-custom-domain"></a>

This section walks you through configuring inbound external links with custom domains end-to-end. After completing these steps, traffic arriving at your existing public endpoint routes through RTB Fabric to the correct link.

**Note**  
Before you begin, confirm that you meet all prerequisites listed in [Prerequisites](custom-domain-prerequisites.md). You need an active RTB Fabric account and a registered domain. If you use HTTPS, you also need an ACM-managed TLS certificate.

**Topics**
+ [Step 1: Create an external responder gateway](#step-create-external-gateway)
+ [Step 2: Register your domain (HTTPS only)](#step-register-domain)
+ [Step 3: Associate your TLS certificate (HTTPS only)](#step-associate-certificate)
+ [Step 4: Create an external inbound link](#step-create-link)
+ [Step 5: Configure routing rules](#step-configure-routing)
+ [Step 6: Update DNS records](#step-update-dns)
+ [Step 7: Verify traffic routing](#step-verify-routing)

## Step 1: Create an external responder gateway
<a name="step-create-external-gateway"></a>

Create an external responder gateway in RTB Fabric if you do not already have one. Inbound external links with custom domains require an external gateway — a gateway type designed for receiving traffic from endpoints outside RTB Fabric. Standard (internal) responder gateways do not support inbound external links with custom domains features such as certificate association and routing rules.

### AWS CLI
<a name="create-external-gateway-cli"></a>

Use the following command to create an external responder gateway using the AWS Command Line Interface (AWS CLI).

**Create an external responder gateway with HTTP**

```
$ aws rtbfabric create-responder-gateway \
--description {{"External gateway for inbound external links with custom domains"}} \
--vpc-id {{vpc-0abc123def456}} \
--subnet-ids {{subnet-0abc123 subnet-0def456}} \
--security-group-ids {{sg-0abc123}} \
--port {{80}} \
--protocol {{HTTP}} \
--managed-endpoint-configuration {{'{"autoScalingGroups":{"autoScalingGroupNames":["my-asg-name"],"roleArn":"arn:aws:iam::123456789012:role/MyASGRole"}}'}} \
--gateway-type {{EXTERNAL}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Create an external responder gateway with HTTPS**

```
$ aws rtbfabric create-responder-gateway \
--description {{"External gateway for inbound external links with custom domains"}} \
--vpc-id {{vpc-0abc123def456}} \
--subnet-ids {{subnet-0abc123 subnet-0def456}} \
--security-group-ids {{sg-0abc123}} \
--port {{443}} \
--protocol {{HTTPS}} \
--managed-endpoint-configuration {{'{"autoScalingGroups":{"autoScalingGroupNames":["my-asg-name"],"roleArn":"arn:aws:iam::123456789012:role/MyASGRole"}}'}} \
--gateway-type {{EXTERNAL}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Create an external responder gateway with both HTTP and HTTPS (multi-protocol)**

```
$ aws rtbfabric create-responder-gateway \
--description {{"External gateway for custom domain inbound"}} \
--vpc-id {{vpc-0abc123def456}} \
--subnet-ids {{subnet-0abc123 subnet-0def456}} \
--security-group-ids {{sg-0abc123}} \
--port {{443}} \
--protocol {{HTTPS}} \
--listener-config {{'{"protocols":["HTTP","HTTPS"]}'}} \
--managed-endpoint-configuration {{'{"autoScalingGroups":{"autoScalingGroupNames":["my-asg-name"],"roleArn":"arn:aws:iam::123456789012:role/MyASGRole"}}'}} \
--gateway-type {{EXTERNAL}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Key parameters:**
+ `--gateway-type EXTERNAL` — Required. Creates an external gateway that supports inbound external links with custom domains, certificate association, and routing rules.
+ `--managed-endpoint-configuration` — Required for external gateways. Specifies the backend that receives traffic. Provide either an `autoScalingGroups` configuration (with ASG names and a role ARN) or an `eksEndpoints` configuration (with EKS cluster details).
+ `--protocol` — `HTTP` or `HTTPS`. Choose based on whether you want TLS termination at the gateway.
+ `--listener-config` — Optional. Specifies a listener configuration with one or more protocols. Use this parameter to enable multi-protocol support (both HTTP and HTTPS) on the same gateway. When provided, the gateway listens on all specified protocols. If omitted, the gateway uses the single protocol specified in `--protocol`. Example: `'{"protocols":["HTTP","HTTPS"]}'`.
+ `--port` — The port the gateway listens on (for example, `80` for HTTP or `443` for HTTPS).

For detailed instructions, see Responder gateways.

Record the gateway endpoint hostname (for example, `rtb-gw-abc123.123456789012.gateway.rtbfabric.us-east-1.amazonaws.com`). You need this value in [Step 6: Update DNS records](#step-update-dns).

## Step 2: Register your domain (HTTPS only)
<a name="step-register-domain"></a>

**Note**  
If you use HTTP only, skip this step and [Step 3: Associate your TLS certificate (HTTPS only)](#step-associate-certificate), and proceed directly to [Step 4: Create an external inbound link](#step-create-link).

Ensure that your ACM certificate's common name (CN) or subject alternative names (SANs) cover all hostnames that partners use to send bid requests to your custom domain. RTB Fabric extracts the CN and SANs from the ACM certificate and uses them for SNI-based certificate selection.

For example, if partners send requests to `bid.example.com`, `east-bid.example.com`, and `west-bid.example.com`, your ACM certificate must include all three hostnames as the CN or SANs. Alternatively, a wildcard certificate (for example, `*.example.com`) covers all single-level subdomains.

**Important**  
RTB Fabric matches the SNI hostname from the client's TLS ClientHello against the CN and SANs from your ACM certificate. If the client's SNI hostname does not match any CN or SAN, the certificate resolver falls back to a service certificate, and the client sees a certificate mismatch error.

## Step 3: Associate your TLS certificate (HTTPS only)
<a name="step-associate-certificate"></a>

**Note**  
If you use HTTP only, skip this step and proceed directly to [Step 4: Create an external inbound link](#step-create-link).

Associate your ACM certificate with the responder gateway using the AssociateCertificate API. This tells RTB Fabric to serve your certificate for SNI-matched requests on your custom domain.

### AWS CLI
<a name="associate-certificate-cli"></a>

Use the following command to associate a certificate with your gateway using the AWS Command Line Interface (AWS CLI).

**Associate an ACM certificate with the gateway**

```
$ aws rtbfabric associate-certificate \
--gateway-id {{rtb-gw-abc123def456}} \
--acm-certificate-arn {{arn:aws:acm:us-east-1:123456789012:certificate/abcd1234-5678-90ef-ghij-klmnopqrstuv}} \
--client-token {{"unique-idempotency-token"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Key fields:**
+ `gatewayId` — The responder gateway to associate the certificate with.
+ `acmCertificateArn` — The ARN of your ACM certificate. RTB Fabric extracts the CN, SANs, certificate chain, and encrypted private key from ACM. It registers the CN and SANs for SNI-based hostname matching.
+ `clientToken` — An idempotency token to prevent duplicate associations.

RTB Fabric handles the private key decryption, certificate chain loading, and SNI registration internally. See [Certificate permissions (HTTPS only)](custom-domain-prerequisites.md#prereq-certificate-permissions).

**Important**  
Certificates associated through the AssociateCertificate API are treated as customer certificates and are never used as a fallback for unrecognized hostnames. See Customer vs. service certificates for details on certificate isolation.

**Note**  
Certificate association and disassociation can each take up to 50 minutes to complete. Wait for the gateway to return to **Active** status before creating links or routing rules.

## Step 4: Create an external inbound link
<a name="step-create-link"></a>

Create an external inbound link on your responder gateway using the CreateInboundExternalLink API. This link represents the connection from your external partner to your gateway and is the target for routing rules.

### AWS CLI
<a name="create-inbound-external-link-cli"></a>

Use the following command to create an external inbound link using the AWS Command Line Interface (AWS CLI).

**Create an external inbound link with log settings**

```
$ aws rtbfabric create-inbound-external-link \
--gateway-id {{rtb-gw-abc123def456}} \
--log-settings {{'{"applicationLogs":{"sampling":{"errorLog":2.0,"filterLog":1.0}}}'}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

The response includes a system-generated `linkId` (pattern: `link-[a-z0-9-]+`) and a `status` field. Record the `linkId` — you need it in the next step to create routing rules.

**Note**  
If you already have a link from a previous configuration (either a standard link or an external inbound link), you can skip this step and use the existing `linkId`. For inbound external links with custom domains, external inbound links are the recommended link type because they represent traffic arriving from outside RTB Fabric.

## Step 5: Configure routing rules
<a name="step-configure-routing"></a>

Create routing rules on the link using the CreateLinkRoutingRule API. Routing rules tell RTB Fabric which incoming requests to forward to a specific link based on the request's hostname, path, or query string.

### AWS CLI
<a name="create-link-routing-rule-cli"></a>

Use the following command to create a routing rule using the AWS Command Line Interface (AWS CLI).

**Create a routing rule with host header condition**

```
$ aws rtbfabric create-link-routing-rule \
--gateway-id {{rtb-gw-abc123def456}} \
--link-id {{link-001}} \
--priority {{1}} \
--conditions {{'{"hostHeader":"bid.example.com"}'}} \
--client-token {{"unique-idempotency-token"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Create a routing rule with host header and path prefix conditions**

```
$ aws rtbfabric create-link-routing-rule \
--gateway-id {{rtb-gw-abc123def456}} \
--link-id {{link-001}} \
--priority {{1}} \
--conditions {{'{"hostHeader":"bid.example.com","pathPrefix":"/openrtb"}'}} \
--client-token {{"unique-idempotency-token"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

The API returns a system-generated `ruleId` and a status of `PENDING_CREATION`. The rule transitions to `ACTIVE` after provisioning completes.

**Key points:**
+ `gatewayId` and `linkId` identify the link that receives matched requests. Use the `linkId` from [Step 4: Create an external inbound link](#step-create-link).
+ `priority` (1-1000) — Lower values take precedence. See Rule evaluation order.
+ `conditions` — At least one condition is required. See [Configuring routing rules](configure-routing-rule.md) for supported match types and AND logic.
+ Configure flow modules separately using the UpdateLinkModuleFlow API. See Modules.

For the full reference on supported match types and evaluation semantics, see [Configuring routing rules](configure-routing-rule.md).

**Tip**  
After creating your routing rules, use the `/resolve-link` endpoint to verify that rules match the expected URLs before updating DNS.

## Step 6: Update DNS records
<a name="step-update-dns"></a>

Create a CNAME record that points your custom domain to the RTB Fabric gateway endpoint.

**To create a CNAME record for inbound external links with custom domains**

1. Open your DNS provider's management console.

1. Create a CNAME record:
   + **Name**: Your custom domain (for example, **bid.example.com**)
   + **Value**: Your gateway endpoint (for example, **rtb-gw-abc123.123456789012.gateway.rtbfabric.us-east-1.amazonaws.com**)
   + **TTL**: Set a low TTL during initial setup. A value of 60 seconds is recommended so that DNS changes propagate quickly and you can revert fast if needed.

1. Save the record and wait for DNS propagation.

**Note**  
If you operate multiple regional endpoints (for example, `east-bid.example.com` and `west-bid.example.com`), create a separate CNAME record for each hostname pointing to the appropriate regional gateway endpoint.

## Step 7: Verify traffic routing
<a name="step-verify-routing"></a>

After DNS propagation completes, verify that requests to your custom domain reach RTB Fabric and route to the correct link.

**To verify traffic routing**

1. Confirm DNS resolution with **dig**:

   ```
   dig bid.example.com CNAME +short
   ```

   The output should return your gateway endpoint:

   ```
   rtb-gw-abc123.123456789012.gateway.rtbfabric.us-east-1.amazonaws.com.
   ```

1. Send a test request with **curl**. Use `https://` if you configured TLS, or `http://` if you use HTTP:

   ```
   curl -v https://bid.example.com/openrtb/bid \
   -H "Content-Type: application/json" \
   -d '{"id":"test-request-1","imp":[{"id":"1"}]}'
   ```

1. In the verbose output, verify the following:
   + **(HTTPS only)** The TLS handshake completes successfully and presents your customer certificate.
   + The response includes the `x-amz-response-source` header (for example, `x-amz-response-source: Responder`), confirming the request was processed by RTB Fabric.
   + The response includes the `x-amz-rtb-link-id` header (for example, `x-amz-rtb-link-id: link-3w7gffr6tiv84his7vdo42bcu`), confirming the request routed to the expected link.

**Note**  
If the TLS handshake fails (HTTPS) or the request returns an unexpected response, see [Troubleshooting inbound external links with custom domains](troubleshooting-custom-domain-ingress.md) for common issues and resolution steps.