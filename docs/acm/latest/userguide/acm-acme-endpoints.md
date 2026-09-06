

# ACME endpoints
<a name="acm-acme-endpoints"></a>

An ACME endpoint is a customer-specific, managed ACME server with a unique URL. Each endpoint is configured to issue certificates from a specific Certificate Authority. When you create an endpoint, ACM provisions an RFC 8555-compliant ACME server that your ACME clients can connect to.

## Endpoint directory URL
<a name="acm-acme-endpoint-url"></a>

When you create an ACME endpoint, ACM assigns it a unique ACME directory URL. You provide this URL to your ACME clients so they can connect to the endpoint. Retrieve the directory URL from the endpoint details in the console, or from the `EndpointUrl` field returned by `DescribeAcmeEndpoint`. The directory URL has the following form:

```
https://acm-acme-enroll.{{region}}.api.aws/{{00000000-0000-0000-0000-000000000000}}/directory
```

## Endpoint configuration
<a name="acm-acme-endpoint-configuration"></a>

When you create an ACME endpoint, you configure the following settings. For ACME quotas, see [Quotas](acm-limits.md).

`AuthorizationBehavior`  
`PRE_APPROVED`: Domain validation is handled by pre-configured domain validation resources rather than live ACME challenges.

`Contact`  
`REQUIRED` or `NOT_REQUIRED`: Specifies whether ACME clients must provide contact information when they register an account with the endpoint. In the console, this setting is **Account email registration**.  
By default, an ACME account contains no identifying information. The contact field is an email address that a client can supply during account registration to associate the account with an identity. Setting `Contact` to `REQUIRED` lets a PKI administrator enforce that the endpoint only accepts account registrations that include contact information, and rejects registrations that omit it. Registered contact information is purely informational and is used by the PKI administrator to manage ACME accounts.

`CertificateAuthority`  
`PublicCertificateAuthority`: Opts the endpoint in to issuing publicly trusted (web PKI) certificates from Amazon Trust Services. You do not specify a particular CA; this field declares that the endpoint is associated with public certificate issuance.

`AllowedKeyAlgorithms`  
`RSA_2048`, `EC_prime256v1`, `EC_secp384r1`: Adds an enforcement layer to the endpoint. If a certificate request contains an embedded public key whose algorithm does not match one of the allowed algorithms, the endpoint rejects the request. When you don't set `AllowedKeyAlgorithms`, the endpoint applies no key algorithm enforcement.  
In the console, these algorithms appear as **Certificate key types**: `EC_prime256v1` is **ECDSA P-256**, `RSA_2048` is **RSA 2048**, and `EC_secp384r1` is **ECDSA P-384**.

`CertificateTags`  
Tags that ACM automatically attaches to every certificate issued through this endpoint. Use certificate tags to organize certificates, track costs, or control access to certificates issued through ACME. In the console, these appear as **Certificate tags**, separate from the **Tags** applied to the endpoint resource itself.

## Endpoint status lifecycle
<a name="acm-acme-endpoint-status"></a>

An ACME endpoint transitions through the following statuses:

`ACTIVE`  
The endpoint is operational and can accept ACME requests.

`DELETING`  
The endpoint is being deleted.

`FAILED`  
Endpoint creation failed. Check the `FailureReason` field for details.

## Creating an ACME endpoint
<a name="acm-acme-endpoint-create"></a>

You can create an ACME endpoint by using the ACM console or the AWS CLI.

### To create an endpoint (console)
<a name="acm-acme-endpoint-create-console"></a>

1. Sign in to the AWS Management Console and open the ACM console.

1. In the left navigation pane, under **ACME**, choose **Endpoints**.

1. Choose **Create ACME endpoint**.

1. For **Endpoint name**, enter a name for the endpoint. The name is stored as a tag on the endpoint, and you can change it later.

1. Note that **Endpoint type** is **Public**. ACME clients connect to the endpoint over the internet by using HTTPS.

1. (Optional) Under **Account email registration**, select **Enable contact information during ACME account registration** to require ACME clients to provide a contact email address when they register an account.

1. Note that **Certificate type** is **Public**. The endpoint issues publicly trusted certificates from Amazon Trust Services.

1. For **Certificate key types**, select at least one key algorithm: **ECDSA P-256** (default), **RSA 2048**, or **ECDSA P-384**.

1. (Optional) Under **Domains**, add one or more domains to validate for this endpoint. You can also add domains later from the endpoint details page. For more information, see [ACME domain validation](acm-acme-domain-validation.md).

1. (Optional) Under **Tags**, add tags to the endpoint.

1. (Optional) Under **Certificate tags**, add tags that ACM automatically attaches to every certificate issued through this endpoint.

1. Choose **Create ACME endpoint**.

After the endpoint status changes to `ACTIVE`, retrieve the endpoint's directory URL and provide it to your ACME clients.

### To create an endpoint (AWS CLI)
<a name="acm-acme-endpoint-create-cli"></a>

Run the following command to create an ACME endpoint:

```
aws acm create-acme-endpoint \
    --authorization-behavior PRE_APPROVED \
    --contact REQUIRED \
    --certificate-authority '{
        "PublicCertificateAuthority": {
            "AllowedKeyAlgorithms": ["RSA_2048", "EC_prime256v1", "EC_secp384r1"]
        }
    }'
```

The response includes the `AcmeEndpointArn`:

```
{
    "AcmeEndpointArn": "arn:aws:acm:{{region}}:{{111122223333}}:acme-endpoint/{{00000000-0000-0000-0000-000000000000}}"
}
```

To retrieve the endpoint URL and configuration, run the following command:

```
aws acm describe-acme-endpoint \
    --acme-endpoint-arn arn:aws:acm:{{region}}:{{111122223333}}:acme-endpoint/{{00000000-0000-0000-0000-000000000000}}
```

The following shows an example response. The `EndpointUrl` is the ACME directory URL that you provide to your ACME clients.

```
{
    "AcmeEndpoint": {
        "AcmeEndpointArn": "arn:aws:acm:{{region}}:{{111122223333}}:acme-endpoint/{{00000000-0000-0000-0000-000000000000}}",
        "EndpointUrl": "https://acm-acme-enroll.{{region}}.api.aws/{{00000000-0000-0000-0000-000000000000}}/directory",
        "Status": "ACTIVE",
        "AuthorizationBehavior": "PRE_APPROVED",
        "Contact": "REQUIRED",
        "CertificateAuthority": {
            "PublicCertificateAuthority": {
                "AllowedKeyAlgorithms": [
                    "RSA_2048",
                    "EC_prime256v1",
                    "EC_secp384r1"
                ]
            }
        },
        "CreatedAt": "2026-06-18T20:35:06.331000-04:00",
        "UpdatedAt": "2026-06-18T20:35:06.331000-04:00"
    }
}
```

## Managing ACME endpoints
<a name="acm-acme-endpoint-manage"></a>

You can perform the following management operations on ACME endpoints:

Describe  
View endpoint details including status and configuration.

List  
View all ACME endpoints in your account.

Update  
Modify authorization behavior, contact requirements, or certificate authority settings.

Delete  
Remove an endpoint. Deleting an endpoint also deletes its external account binding and domain validation resources, along with any ACME accounts registered with the endpoint.

## Monitoring ACME endpoints
<a name="acm-acme-endpoint-monitoring"></a>

You can monitor ACME endpoint activity and certificate issuance through the ACM console and Amazon CloudWatch.

**Console monitoring tab**

In the ACM console, select an ACME endpoint and choose the **Monitoring** tab to view issuance metrics for that endpoint. The monitoring tab displays graphs for `CertificateIssuanceSuccess` and `CertificateIssuanceFailed` metrics over time.

**Certificates dashboard**

The ACM console **Certificates dashboard** provides an overview of all certificates in your account, including ACME-issued certificates. Use the dashboard to track certificate counts, expiration timelines, and renewal status across your inventory.

**CloudWatch metrics**

ACM publishes the following metrics to the `AWS/CertificateManager` namespace for each ACME endpoint:
+ `CertificateIssuanceSuccess` – Count of certificates successfully issued through the endpoint.
+ `CertificateIssuanceFailed` – Count of failed issuance attempts for the endpoint.

Both metrics use the `AcmeEndpointArn` dimension. You can create CloudWatch alarms on these metrics to be notified of issuance failures. For more information, see [Supported CloudWatch metrics](cloudwatch-metrics.md).