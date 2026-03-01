# Private certificate renewal in AWS Certificate Manager

ACM certificates that were signed by a private CA from AWS Private CA are eligible for
managed renewal. Unlike publicly trusted ACM certificates, a certificate for a private
PKI requires no validation. Trust is established when an administrator installs the
appropriate root CA certificate in client trust stores.

###### Note

Only certificates obtained using the ACM console or the [RequestCertificate](../APIReference/API-RequestCertificate.md "../APIReference/API-RequestCertificate.md") action
of the ACM API are eligible for managed renewal. Certificates issued directly from
AWS Private CA using the [IssueCertificate](../APIReference/API_IssueCertificate.md "../APIReference/API_IssueCertificate.md") action of the AWS Private CA API are not managed by ACM.

When a managed certificate is 60 days away from expiration, ACM automatically
attempts to renew it. This includes certificates that were exported and installed
manually (for example, in an on-premises data center). Customers can also force renewal
at any time using the [RenewCertificate](../APIReference/API_RenewCertificate.md "../APIReference/API_RenewCertificate.md") action of the ACM API. For a sample Java implementation
of forced renewal, see [Renewing a certificate](sdk-renew.md "sdk-renew.md").

After renewal, a certificate's deployment into service occurs in one of the following
ways:

- If the certificate **is** associated with an
  ACM [integrated service](acm-services.md "acm-services.md"), the
  new certificate replaces the old one without additional customer action.
- If the certificate **is not** associated with an
  ACM [integrated service](acm-services.md "acm-services.md"),
  customer action is required to export and install the renewed certificate. You
  can perform these actions manually, or with assistance from [AWS Health](../../../health/latest/ug.md "../../../health/latest/ug.md"), [Amazon EventBridge](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md"), and [AWS Lambda](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md") as follows.
  For more information, see [Automate export of renewed certificates](#automating-export "#automating-export")

## Automate export of renewed certificates

The following procedure provides an example solution for automating export of your
private PKI certificates when ACM renews them. This example only exports a
certificate and its private key out of ACM; after export, the certificate must
still be installed on its target device.

###### To automate certificate export using the console

1. Following procedures in the AWS Lambda Developer Guide, create and
   configure a Lambda function that calls ACM export API.
   1. [Create a Lambda function](../../../lambda/latest/dg/getting-started-create-function.md "../../../lambda/latest/dg/getting-started-create-function.md").
   2. [Create
      a Lambda execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") for your function and add the
      following trust policy to it. The policy grants permission to the
      code in your function to retrieve the renewed certificate and
      private key by calling the [ExportCertificate](../APIReference/API_ExportCertificate.md "../APIReference/API_ExportCertificate.md") action of the ACM API.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement":[
    {
    "Effect":"Allow",
    "Action":"acm:ExportCertificate",
    "Resource":"*"
    }
    ]
   }`

   ```

2. [Create a rule in
   Amazon EventBridge](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") to listen for ACM health events and call your Lambda
   function when it detects one. ACM writes to an AWS Health event each time
   it attempts to renew a certificate. For more information about these
   notices, see [Check the status using Personal Health Dashboard (PHD)](check-certificate-renewal-status.md#check-renewal-status-phd "check-certificate-renewal-status.md#check-renewal-status-phd").

Configure the rule by adding the following event pattern.

```
{
   "source":[
      "aws.health"
   ],
   "detail-type":[
      "AWS Health Event"
   ],
   "detail":{
      "service":[
         "ACM"
      ],
      "eventTypeCategory":[
         "scheduledChange"
      ],
      "eventTypeCode":[
         "AWS_ACM_RENEWAL_STATE_CHANGE"
      ]
   },
   "resources":[
      "arn:aws:acm:region:account:certificate/certificate_ID"
   ]
}
```

3. Complete the renewal process by manually installing the certificate on the
   target system.

## Test managed renewal of private PKI certificates

You can use the ACM API or AWS CLI to manually test the configuration of your
ACM managed renewal workflow. By doing so, you can confirm that your certificates
will be renewed automatically by ACM prior to expiration.

###### Note

You can only test the renewal of certificates issued and exported by
AWS Private CA.

When you use API actions or CLI commands described below, ACM attempts to renew
the certificate. If the renewal succeeds, ACM updates the certificate metadata
displayed in the management console or in API output. If the certificate is
associated with an ACM [integrated
services](acm-services.md "acm-services.md"), the new certificate is deployed and a renewal event is
generated in Amazon CloudWatch Events. If the renewal fails, ACM returns a error and suggests
remedial action. (You can view this information using the [describe-certificate](../../../cli/latest/reference/acm/describe-certificate.md "../../../cli/latest/reference/acm/describe-certificate.md") command.) If the certificate is not deployed
through an integrated service, you still need to export it and manually install it
on your resource.

###### Important

In order to renew your AWS Private CA certificates with ACM, you must first
grant the ACM service principal permissions to do so. For more information,
see [Assigning
Certificate Renewal Permissions to ACM](../../../privateca/latest/userguide/assign-permissions.md#PcaPermissions "../../../privateca/latest/userguide/assign-permissions.md#PcaPermissions").

###### To manually test certificate renewal (AWS CLI)

1. Use the [renew-certificate](../../../cli/latest/reference/acm/renew-certificate.md "../../../cli/latest/reference/acm/renew-certificate.md") command to renew a private exported
   certificate.

```
aws acm renew-certificate \
	--certificate-arn arn:aws:acm:`region`:`account`:certificate/`certificate_ID`
```

2. Then use the [describe-certificate](../../../cli/latest/reference/acm/describe-certificate.md "../../../cli/latest/reference/acm/describe-certificate.md") command to confirm that the certificate's
   renewal details have been updated.

```
aws acm describe-certificate \
	--certificate-arn arn:aws:acm:`region`:`account`:certificate/`certificate_ID`
```

###### To manually test certificate renewal (ACM API)

- Send a [RenewCertificate](../APIReference/API_RenewCertificate.md "../APIReference/API_RenewCertificate.md") request, specifying the ARN of the private
  certificate to renew. Then use the [DescribeCertificate](../APIReference/API_DescribeCertificate.md "../APIReference/API_DescribeCertificate.md") operation to confirm that the certificate's
  renewal details have been updated.
