# Data protection in AWS Supply Chain

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Supply Chain. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
You are also responsible for the security configuration and management tasks for the AWS services
that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through
  a command line interface or an API, use a FIPS endpoint. For more information about the
  available FIPS endpoints, see [Federal
  Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS Supply Chain or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data handled by

AWS Supply Chain

To limit the data that can be accessed by authorized users of a specific AWS Supply
Chain instance, data held within AWS Supply Chain is segregated by your AWS account ID and
your AWS Supply Chain instance ID.

AWS Supply Chain handles a variety of supply chain data such as, user information, information extracted from the data connector, and inventory details.

## Opt-out preference

We may use and store Your Content that is processed by AWS Supply Chain, as noted in the [AWS Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/"). If you want to opt-out from AWS Supply Chain to use or
store your content, you can create an opt-out policy in AWS Organizations. For more information on creating an opt-out policy, see [AI services opt-out policy syntax and examples](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out_syntax.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out_syntax.md") .

## Encryption at rest

Contact data classified as PII, or data that represents customer content including content used in Amazon Q in AWS Supply Chain being stored by
AWS Supply Chain, is encrypted at rest (that is, before it is put, stored, or saved to a disk) with a
key that is time-limited and specific to the AWS Supply Chain instance.

Amazon S3 server-side encryption is used to encrypt all console and web application data with a
AWS Key Management Service data key that is unique to each customer account. For information about
AWS KMS keys, see [What is
AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the AWS Key Management Service Developer Guide.

###### Note

AWS Supply Chain features Supply Planning and N-Tier Visibility does not support encrypting data-at-rest with the provided KMS-CMK.

## Encryption in transit

Data including content used in Amazon Q in AWS Supply Chain exchanged with AWS Supply Chain is protected in transit between the user’s web browser and AWS Supply Chain using industry-standard TLS encryption.

## Key management

AWS Supply Chain partially supports KMS-CMK.

For information on updating the AWS KMS key in AWS Supply Chain, see [Step 2: Create an instance](creating-instance.md "creating-instance.md").

## Inter-network traffic privacy

###### Note

AWS Supply Chain does not support PrivateLink.

A virtual private cloud (VPC) endpoint for AWS Supply Chain is a logical entity within a VPC that allows connectivity only to AWS Supply Chain. The VPC routes requests to AWS Supply Chain and routes responses back to the VPC. For more information, see [VPC Endpoints](../../../vpc/latest/privatelink/concepts.md "../../../vpc/latest/privatelink/concepts.md") in the VPC User Guide.

## How AWS Supply Chain uses grants in AWS KMS

AWS Supply Chain requires a [grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") to use your customer managed key.

AWS Supply Chain creates several grants using the AWS KMS key that is passed during the **CreateInstance** operation. AWS Supply Chain creates a grant on your behalf by
sending [**CreateGrant**](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") requests to AWS KMS. Grants in AWS KMS are used to give AWS Supply Chain access to the AWS KMS key in a customer account.

###### Note

AWS Supply Chain uses it's own authorization mechanism. Once an user is added to AWS Supply Chain, you cannot deny list the same user using the AWS KMS policy.

AWS Supply Chain uses the grant for the following:

- To send **GenerateDataKey** requests to AWS KMS to [**encrypt**](../../../forecast/latest/dg/data-protection.md#kms-grants "../../../forecast/latest/dg/data-protection.md#kms-grants") the data stored in your instance.
- To send **Decrypt** requests to AWS KMS in order to read your encrypted data associated with the instance.
- To add _DescribeKey_, _CreateGrant_, and _RetireGrant_ permissions in order to keep your data secured when sending it to other AWS services like Amazon Forecast.

You can revoke access to the grant, or remove the service's access to the customer managed key at any time. If you do, AWS Supply Chain won't be able to access any of the data encrypted by the customer
managed key, which affects operations that are dependent on that data.

### Monitoring your encryption for AWS Supply Chain

The following examples are AWS CloudTrail events for `Encrypt`, `GenerateDataKey`, and `Decrypt` to monitor KMS operations called by AWS Supply Chain to access data encrypted by your customer managed key:

Encrypt

```

              {
    "eventVersion": "`1.08`",
    "userIdentity": {
        "type": "`AWSService`",
        "invokedBy": "`scn.amazonaws.com`"
    },
    "eventTime": "`2024-03-06T22:39:32Z`",
    "eventSource": "`kms.amazonaws.com`",
    "eventName": "`Encrypt`",
    "awsRegion": "`us-east-1`",
    "sourceIPAddress": "`172.12.34.56`"
    "userAgent": "`Example/Desktop/1.0 (V1; OS)`",
    "requestParameters": {
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "keyId": "`arn:aws:kms:us-east-1:123456789:key/1234abcd-11ab-22bc-33ef-123456sample`"
    },
    "responseElements": null,
    "requestID": "`12a345n4-78a4-8888-0000-a000-6q000yy666rr`",
    "eventID": "`12a345n4-78a4-8888-0000-a000-6q000yy666rr`",
    "readOnly": true,
    "resources": [
        {
            "accountId": `account ID`,
            "type": "`AWS::KMS::Key`",
            "ARN": "`arn:aws:kms:us-east-1:123456789:key/1234abcd-11ab-22bc-33ef-123456sample`"
        }
    ],
    "eventType": "`AwsApiCall`",
    "managementEvent": true,
    "recipientAccountId": "`112233445566`",
    "sharedEventID": "`fdf9ee0f-e43f-4e43-beac-df69067edb8b`",
    "eventCategory": "Management"
}

```

GenerateDataKey

```

            {
    "eventVersion": "`1.08`",
    "userIdentity": {
        "type": "`AWSService`",
        "invokedBy": "`scn.amazonaws.com`"
    },
     "eventTime": "`2024-03-06T22:39:32Z`",
    "eventSource": "`kms.amazonaws.com`",
    "eventName": "`GenerateDataKey`",
    "awsRegion": "`us-east-1`",
    "sourceIPAddress": "`172.12.34.56`"
    "userAgent": "`Example/Desktop/1.0 (V1; OS)`",
    "requestParameters": {
        "encryptionContext": {
            "aws:s3:arn": "`arn:aws:s3:::test/rawEvent/bf6666c1-111-48aaca-b6b0-dsadsadsa3432423/noFlowName/scn.data.inboundorder/20240306_223934_536"`
        },
        "keyId": "`arn:aws:kms:us-east-1:123456789:key/1234abcd-11ab-22bc-33ef-123456sample`",
        "keySpec": "`AES_222`"
    },
    "responseElements": null,
    "requestID": "`12a345n4-78a4-8888-0000-a000-6q000yy666rr`",
    "eventID": "`12a345n4-78a4-8888-0000-a000-6q000yy666rr`",
    "readOnly": true,
    "resources": [
        {
            "accountId": `account ID`,
            "type": "`AWS::KMS::Key`",
            "ARN": "`arn:aws:kms:us-east-1:123456789:key/1234abcd-11ab-22bc-33ef-123456sample`"
        }
    ],
    "eventType": "`AwsApiCall`",
    "managementEvent": true,
    "recipientAccountId": "`112233445566`",
    "sharedEventID": "`fdf9ee0f-e43f-4e43-beac-df69067edb8b`",
    "eventCategory": "Management"
}

```

Decrypt

```

            {
    "eventVersion": "`1.08`",
    "userIdentity": {
        "type": "`AWSService`",
        "invokedBy": "`scn.amazonaws.com`"
    },
     "eventTime": "`2024-03-06T22:39:32Z`",
    "eventSource": "`kms.amazonaws.com`",
    "eventName": "`Decrypt`",
    "awsRegion": "`us-east-1`",
    "sourceIPAddress": "`172.12.34.56`"
    "userAgent": "`Example/Desktop/1.0 (V1; OS)`",
    "requestParameters": {
        "keyId": "`arn:aws:kms:us-east-1:123456789:key/1234abcd-11ab-22bc-33ef-123456sample`",
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": "`12a345n4-78a4-8888-0000-a000-6q000yy666rr`",
    "eventID": "`12a345n4-78a4-8888-0000-a000-6q000yy666rr`",
    "readOnly": true,
    "resources": [
        {
            "accountId": `account ID`,
            "type": "`AWS::KMS::Key`",
            "ARN": "`arn:aws:kms:us-east-1:123456789:key/1234abcd-11ab-22bc-33ef-123456sample`"
        }
    ],
    "eventType": "`AwsApiCall`",
    "managementEvent": true,
    "recipientAccountId": "`112233445566`",
    "sharedEventID": "`fdf9ee0f-e43f-4e43-beac-df69067edb8b`",
    "eventCategory": "Management"
}

```
