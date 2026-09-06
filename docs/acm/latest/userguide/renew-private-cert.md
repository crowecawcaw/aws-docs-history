

# Private certificate renewal in AWS Certificate Manager
<a name="renew-private-cert"></a>

ACM certificates that were signed by a private CA from AWS Private CA are eligible for managed renewal. Unlike publicly trusted ACM certificates, a certificate for a private PKI requires no validation. Trust is established when an administrator installs the appropriate root CA certificate in client trust stores.

**Note**  
Only certificates obtained using the ACM console or the [RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API-RequestCertificate.html) action of the ACM API are eligible for managed renewal. Certificates issued directly from AWS Private CA using the [IssueCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_IssueCertificate.html) action of the AWS Private CA API are not managed by ACM. 

When a managed certificate is 60 days away from expiration, ACM automatically attempts to renew it. This includes certificates that were exported and installed manually (for example, in an on-premises data center). Customers can also force renewal at any time using the [RenewCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RenewCertificate.html) action of the ACM API. For a sample Java implementation of forced renewal, see [Renewing a certificate](sdk-renew.md).

After renewal, a certificate's deployment into service occurs in one of the following ways:
+ If the certificate **is** associated with an ACM [integrated service](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html), the new certificate replaces the old one without additional customer action. 
+ If the certificate **is not** associated with an ACM [integrated service](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html), customer action is required to export and install the renewed certificate. You can perform these actions manually, or with assistance from [AWS Health](https://docs.aws.amazon.com/health/latest/ug/), [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) as follows. For more information, see [Automate export of renewed certificates](#automating-export)

## Automate export of renewed certificates
<a name="automating-export"></a>

The following procedure provides an example solution for automating export of your private PKI certificates when ACM renews them. This example only exports a certificate and its private key out of ACM; after export, the certificate must still be installed on its target device.

**To automate certificate export using the console**

1. Following procedures in the AWS Lambda Developer Guide, create and configure a Lambda function that calls ACM export API. 

   1. [Create a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html).

   1. [Create a Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) for your function and add the following trust policy to it. The policy grants permission to the code in your function to retrieve the renewed certificate and private key by calling the [ExportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ExportCertificate.html) action of the ACM API.

------
#### [ JSON ]

****  

      ```
      {
         "Version":"2012-10-17",		 	 	 
         "Statement":[
            {
               "Effect":"Allow",
               "Action":"acm:ExportCertificate",
               "Resource":"*"
            }
         ]
      }
      ```

------

1.  

   [Create a rule in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) to listen for ACM health events and call your Lambda function when it detects one. ACM writes to an AWS Health event each time it attempts to renew a certificate. For more information about these notices, see [Check the status using Personal Health Dashboard (PHD)](check-certificate-renewal-status.md#check-renewal-status-phd).

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

1. Complete the renewal process by manually installing the certificate on the target system.

## Test managed renewal of private PKI certificates
<a name="manual-renewal"></a>

You can use the ACM API or AWS CLI to manually test the configuration of your ACM managed renewal workflow. By doing so, you can confirm that your certificates will be renewed automatically by ACM prior to expiration.

**Note**  
You can only test the renewal of certificates issued and exported by AWS Private CA.

When you use API actions or CLI commands described below, ACM attempts to renew the certificate. If the renewal succeeds, ACM updates the certificate metadata displayed in the management console or in API output. If the certificate is associated with an ACM [integrated services](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html), the new certificate is deployed and a renewal event is generated in Amazon CloudWatch Events. If the renewal fails, ACM returns a error and suggests remedial action. (You can view this information using the [describe-certificate](https://docs.aws.amazon.com/cli/latest/reference/acm/describe-certificate.html) command.) If the certificate is not deployed through an integrated service, you still need to export it and manually install it on your resource. 

**Important**  
In order to renew your AWS Private CA certificates with ACM, you must first grant the ACM service principal permissions to do so. For more information, see [Assigning Certificate Renewal Permissions to ACM](https://docs.aws.amazon.com/privateca/latest/userguide/assign-permissions.html#PcaPermissions).

**To manually test certificate renewal (AWS CLI)**

1. Use the [renew-certificate](https://docs.aws.amazon.com/cli/latest/reference/acm/renew-certificate.html) command to renew a private exported certificate.

   ```
   aws acm renew-certificate \
   	--certificate-arn arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate_ID}}
   ```

1. Then use the [describe-certificate](https://docs.aws.amazon.com/cli/latest/reference/acm/describe-certificate.html) command to confirm that the certificate's renewal details have been updated.

   ```
   aws acm describe-certificate \
   	--certificate-arn arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate_ID}}
   ```

**To manually test certificate renewal (ACM API)**
+ Send a [RenewCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RenewCertificate.html) request, specifying the ARN of the private certificate to renew. Then use the [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html) operation to confirm that the certificate's renewal details have been updated.