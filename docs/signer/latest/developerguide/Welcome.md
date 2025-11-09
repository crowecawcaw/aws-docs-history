# What is AWS Signer?

AWS Signer is a fully managed code-signing service to ensure the trust and integrity of
your code. Organizations validate code against a digital signature to confirm that the code
is unaltered and from a trusted publisher. With AWS Signer, your security administrators
have a single place to define your signing environment, including what AWS Identity and Access Management (IAM)
role can sign code and in what Regions. AWS Signer manages the code-signing certificate's
public and private keys, and enables central management of the code-signing lifecycle.
Integration with [AWS CloudTrail](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md") helps you track who is
generating code signatures and to meet your compliance requirements.

For information about AWS services that Signer supports, see [Interoperation with other AWS services](#whatis-services "#whatis-services").

###### Topics

- [Interoperation with other AWS services](#whatis-services "#whatis-services")
- [Supported Regions](#whatis-regions "#whatis-regions")
- [Quotas for Signer](#whatis-limits "#whatis-limits")
- [Pricing for Signer](#whatis-pricing "#whatis-pricing")
  For information about the AWS Signer API, see the [AWS Signer API Reference](../api/Welcome.md "../api/Welcome.md").

## Interoperation with other AWS services

AWS Signer is integrated or used with the following AWS services.

**AWS Lambda**

With AWS Signer, you can digitally sign packages intended for Lambda
deployment in your organization, ensuring that only trusted code runs in
your Lambda functions. AWS Signer defines a trusted publisher in a signing
profile. Authorized developers use the profile to generate certified code
packages. AWS Lambda verifies signatures and package integrity when code is
deployed.

To sign your code packages before deploying them to [AWS Lambda](../../../lambda/latest/dg/configuration-codesigning.md "../../../lambda/latest/dg/configuration-codesigning.md"), you
can use the [AWS Signer
console](https://console.aws.amazon.com/signer/ "https://console.aws.amazon.com/signer/"), the [Signer
CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") the [AWS Serverless Application Model (AWS SAM)
CLI](../../../serverless-application-model/latest/developerguide.md "../../../serverless-application-model/latest/developerguide.md"), or one of the AWS SDKs.

**Amazon FreeRTOS** and **AWS IoT Device Management**

You can sign code that you create for IoT devices supported by [Amazon FreeRTOS](../../../freertos/latest/userguide.md "../../../freertos/latest/userguide.md") and [AWS IoT](../../../iot/latest/developerguide.md "../../../iot/latest/developerguide.md") device management. Code signing for AWS IoT is integrated
with AWS Certificate Manager (ACM). To sign code, you import a third-party code-signing
certificate into ACM that is used to sign updates in FreeRTOS and AWS IoT
Device Management.

Amazon FreeRTOS is a microcontroller operating system based on the FreeRTOS
kernel. It includes libraries for connectivity and security. You can build
and deploy your embedded applications on top of Amazon FreeRTOS. To ensure the
security of deployments to these microcontrollers, Amazon FreeRTOS uses
AWS Signer for the initial manufacture of these devices and subsequent
over-the-air updates. You can use AWS Signer through the Amazon FreeRTOS
console to sign your code images before you deploy them to a
microcontroller.

With AWS IoT Device Management, you can manage Internet-connected devices and establish
secure, bidirectional communication between them. To do so, AWS IoT Device Management uses
AWS Signer to authenticate each device in your IoT environment. You can
use AWS Signer through the AWS IoT Device Management console to sign your code images before
you deploy them to a microcontroller.

You can sign your firmware images before deploying them to a
microcontroller using the [FreeRTOS
console](https://console.aws.amazon.com/freertos/ "https://console.aws.amazon.com/freertos/"). To sign your code images before deploying them in an
over-the-air (OTA) update, you can use the [AWS IoT Device Management
console](https://console.aws.amazon.com/iotdm/ "https://console.aws.amazon.com/iotdm/"), the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), or one of the AWS SDKs.

**Amazon Elastic Container Registry (Amazon ECR)**

With AWS Signer and the Notation CLI from the
[Notary  Project](https://notaryproject.dev/ "https://notaryproject.dev/"), you can sign
container images stored in
a container registry such as Amazon Elastic Container Registry (Amazon ECR). The signatures are stored in
the registry alongside the images, where they are available for verifying
image authenticity and integrity.

For more information, see the [Amazon Elastic Container Registry User Guide](../../../AmazonECR/latest/userguide.md "../../../AmazonECR/latest/userguide.md").

**Amazon Elastic Kubernetes Service (Amazon EKS)**

Amazon EKS and self-managed Kubernetes customers on Amazon EC2 can verify the ownership and
integrity of signed images at the time of deployment. For more information,
see the [_Amazon EKS User Guide_](../../../eks/latest/userguide.md "../../../eks/latest/userguide.md").

**AWS Certificate Manager (ACM)**

ACM handles the complexity of creating and managing or importing SSL/TLS
certificates. You use ACM to create an ACM certificate or import a
third-party certificate that you use for signing. You must have a
certificate to sign code. For more information about certificates, see
[AWS Certificate Manager User Guide](../../../acm/latest/userguide.md "../../../acm/latest/userguide.md").

**CloudTrail**

You can use AWS CloudTrail to record API calls made to AWS Signer. CloudTrail is an
AWS service that simplifies governance, compliance, and risk auditing by
providing visibility into actions made in your AWS account. For more
information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Supported Regions

Visit [AWS Signer endpoints and quotas](../../../general/latest/gr/signer.md "../../../general/latest/gr/signer.md")
to see an up-to-date list of supported Regions.

## Quotas for Signer

AWS Signer sets per-second quotas on the allowed rate at which you can call API
actions. Each API's quota is specific to an AWS account and Region. If the number of
requests for an API exceeds its quota, AWS Signer rejects an otherwise valid request,
returning a [ThrottlingException](../api/CommonErrors.md "../api/CommonErrors.md")
error. AWS Signer does not offer a minimum request rate for APIs.

To view your quotas and see which ones can be adjusted, see the [AWS Signer quotas table](../../../general/latest/gr/signer.md#quotas_signer "../../../general/latest/gr/signer.md#quotas_signer") in
the _AWS General Reference Guide_.

You can also view and adjust quotas using the Service Quotas console.

###### To see an up-to-date list of your AWS Signer quotas

1. Log in to your AWS account.
2. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
3. In the \***\*AWS services\*\***
   list, enter **signer** into the search box, and
   choose **AWS Signer**. Each quota in the
   **Service quotas** list shows your currently applied quota
   value, the default quota value, and whether the quota is adjustable. Choose the
   name of a quota for more information about it.

###### To request a quota increase

1. In the **Service quotas** list, choose the radio button for
   an adjustable quota.
2. Choose the **Request quota increase** button.
3. Complete and submit the **Request quota increase**
   form.

## Pricing for Signer

There is no additional charge to use AWS Signer with AWS IoT Device Management, AWS Lambda, Amazon ECR, Amazon EKS, or
third-party container services. Refer to the pricing for the related services for other
charges that you may incur. For example, if you use Signer with Lambda, you pay for the
storage of signed and unsigned objects (such as your Lambda zip-file archives) in
Amazon S3.
