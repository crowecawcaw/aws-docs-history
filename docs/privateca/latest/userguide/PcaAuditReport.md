# Use audit reports with your private CA

You can create an audit report to list all of the certificates
that your private CA has issued or revoked. The report is saved in a new or existing
S3 bucket that you specify on input.

For information about adding encryption protection to your audit reports, see
[Encrypting your audit reports](#audit-report-encryption "#audit-report-encryption") .

The audit report file has the following path and file name. The ARN for an Amazon S3
bucket is the value for `amzn-s3-demo-bucket`. `CA_ID` is the
unique identifier of an issuing CA. `UUID` is the unique identifier of an
audit report.

```
`amzn-s3-demo-bucket`/audit-report/`CA_ID`/`UUID`.[json|csv]
```

You can generate a new report every 30 minutes and download it from your bucket.
The following example shows a CSV-separated report.

```
awsAccountId,requestedByServicePrincipal,certificateArn,serial,subject,notBefore,notAfter,issuedAt,revokedAt,revocationReason,templateArn
123456789012,,arn:aws:acm-pca:`region`:`account`:certificate-authority/`CA_ID`/certificate/`certificate_ID`,00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff,"2.5.4.5=#012345678901,2.5.4.44=#0a1b3c4d,2.5.4.65=#0a1b3c4e5f6a,2.5.4.43=#0a1b3c4d5e,2.5.4.42=#0123456789abcdef0123456789abcdef0123,2.5.4.4=#0123456789abcdef01234567,2.5.4.12=#0a1b3c4d5e,2.5.4.46=#0123456789ab,CN=www.example1.com,OU=Sales,O=Example Company,L=Seattle,ST=Washington,C=US",2020-03-02T21:43:57+0000,2020-04-07T22:43:57+0000,2020-03-02T22:43:58+0000,,UNSPECIFIED,arn:aws:acm-pca:::template/EndEntityCertificate/V1
123456789012,acm.amazonaws.com,arn:aws:acm-pca:`region`:`account`:certificate-authority/`CA_ID`/certificate/`certificate_ID`,ff:ee:dd:cc:bb:aa:99:88:77:66:55:44:33:22:11:00,"2.5.4.5=#012345678901,2.5.4.44=#0a1b3c4d,2.5.4.65=#0a1b3c4d5e6f,2.5.4.43=#0a1b3c4d5e,2.5.4.42=#0123456789abcdef0123456789abcdef0123,2.5.4.4=#0123456789abcdef01234567,2.5.4.12=#0a1b3c4d5e,2.5.4.46=#0123456789ab,CN=www.example1.com,OU=Sales,O=Example Company,L=Seattle,ST=Washington,C=US",2020-03-02T20:53:39+0000,2020-04-07T21:53:39+0000,2020-03-02T21:53:40+0000,,,arn:aws:acm-pca:::template/EndEntityCertificate/V1
```

The following example shows a JSON-formatted report.

```
[
   {
      "awsAccountId":"123456789012",
      "certificateArn":"arn:aws:acm-pca:`region`:`account`:certificate-authority/`CA_ID`/certificate/`certificate_ID`",
      "serial":"00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff",
      "subject":"2.5.4.5=#012345678901,2.5.4.44=#0a1b3c4d,2.5.4.65=#0a1b3c4d5e6f,2.5.4.43=#0a1b3c4d5e,2.5.4.42=#0123456789abcdef0123456789abcdef0123,2.5.4.4=#0123456789abcdef01234567,2.5.4.12=#0a1b3c4d5e,2.5.4.46=#0123456789ab,CN=www.example1.com,OU=Sales,O=Example Company,L=Seattle,ST=Washington,C=US",
      "notBefore":"2020-02-26T18:39:57+0000",
      "notAfter":"2021-02-26T19:39:57+0000",
      "issuedAt":"2020-02-26T19:39:58+0000",
      "revokedAt":"2020-02-26T20:00:36+0000",
      "revocationReason":"UNSPECIFIED",
      "templateArn":"arn:aws:acm-pca:::template/EndEntityCertificate/V1"
   },
   {
      "awsAccountId":"123456789012",
      "requestedByServicePrincipal":"acm.amazonaws.com",
      "certificateArn":"arn:aws:acm-pca:`region`:`account`:certificate-authority/`CA_ID`/certificate/`certificate_ID`",
      "serial":"ff:ee:dd:cc:bb:aa:99:88:77:66:55:44:33:22:11:00",
      "subject":"2.5.4.5=#012345678901,2.5.4.44=#0a1b3c4d,2.5.4.65=#0a1b3c4d5e6f,2.5.4.43=#0a1b3c4d5e,2.5.4.42=#0123456789abcdef0123456789abcdef0123,2.5.4.4=#0123456789abcdef01234567,2.5.4.12=#0a1b3c4d5e,2.5.4.46=#0123456789ab,CN=www.example1.com,OU=Sales,O=Example Company,L=Seattle,ST=Washington,C=US",
      "notBefore":"2020-01-22T20:10:49+0000",
      "notAfter":"2021-01-17T21:10:49+0000",
      "issuedAt":"2020-01-22T21:10:49+0000",
      "templateArn":"arn:aws:acm-pca:::template/EndEntityCertificate/V1"
   }
]
```

###### Note

When AWS Certificate Manager renews a certificate, the private CA audit report populates the
`requestedByServicePrincipal` field with
`acm.amazonaws.com`. This indicates that the AWS Certificate Manager service
called the `IssueCertificate` action of the AWS Private CA API on behalf
of a customer to renew the certificate.

## Prepare an Amazon S3 bucket for audit reports

###### Important

AWS Private CA doesn't support the use of [Amazon S3 Object
Lock](../../../AmazonS3/latest/userguide/object-lock.md "../../../AmazonS3/latest/userguide/object-lock.md"). If you enable Object Lock on your bucket, AWS Private CA isn't able
to write audit reports to the bucket.

To store your audit reports, you need to prepare an Amazon S3 bucket. For more
information, see [How Do I Create an
S3 bucket?](../../../AmazonS3/latest/userguide/create-bucket.md "../../../AmazonS3/latest/userguide/create-bucket.md")

Your S3 bucket must be secured by a permissions policy that allows AWS Private CA to
access and write to the S3 bucket that you specify. Authorized users and service
principals require `Put` permission to allow AWS Private CA to place
objects in the bucket, and `Get` permission to retrieve them. We
recommend that you apply the policy shown below, which restricts access to both
an AWS account and the ARN of a private CA. Alternatively, you can use the
[aws:SourceOrgID](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgid") condition key to constrain access to a specific
organization in AWS Organizations. For more information about bucket policies, see [Bucket policies for
Amazon Simple Storage Service](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md").

## Create an audit report

You can create an audit report from either the console or the AWS CLI.

###### To create an audit report (console)

1. Sign in to your AWS account and open the AWS Private CA console at [https://console.aws.amazon.com/acm-pca/home](https://console.aws.amazon.com/acm-pca/home "https://console.aws.amazon.com/acm-pca/home").
2. On the **Private certificate authories** page, choose
   your private CA from the list.
3. From the **Actions** menu, choose **Generate
   audit report**.
4. Under **Audit report destination**, for **Create
   a new S3 bucket?**, choose **Yes** and type a
   unique bucket name, or choose **No** and choose an existing
   bucket from the list.

If you choose **Yes**, AWS Private CA creates and attaches
the default policy to your bucket. The default policy includes an
`aws:SourceAccount` condition key, which limits access to a
specific AWS account. If you wish to further constrain access, you can add
other condition keys to the policy such as in the [preceding example](#s3-access "#s3-access").

If you choose **No**, you must attach a policy to your
bucket before you can generate an audit report. Use the policy pattern
described in [Prepare an Amazon S3 bucket for audit reports](#s3-access "#s3-access"). For
information about attaching a policy, see [Adding a bucket policy using
the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md"). 5. Under **Output format**, choose **JSON**
for JavaScript Object Notation or **CSV** for
comma-separated values. 6. Choose **Generate audit report**.

###### To create an audit report (AWS CLI)

1. If you do not already have an S3 bucket to use, [create one](../../../AmazonS3/latest/userguide/create-bucket.md "../../../AmazonS3/latest/userguide/create-bucket.md").
2. Attach a policy to your bucket. Use the policy pattern described in [Prepare an Amazon S3 bucket for audit reports](#s3-access "#s3-access"). For information about
   attaching a policy, see [Adding a bucket policy using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md")
3. Use the [create-certificate-authority-audit-report](../../../cli/latest/reference/acm-pca/create-certificate-authority-audit-report.md "../../../cli/latest/reference/acm-pca/create-certificate-authority-audit-report.md") command to create the
   audit report and to place it in the prepared S3 bucket.

```
`$` `aws acm-pca create-certificate-authority-audit-report \
--certificate-authority-arn arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566` \
--s3-bucket-name `amzn-s3-demo-bucket` \
--audit-report-response-format JSON`
```

## Retrieve an audit report

To retrieve an audit report for inspection, use the Amazon S3 console, API, CLI, or
SDK. For more information, see [Downloading an object](../../../AmazonS3/latest/userguide/download-objects.md "../../../AmazonS3/latest/userguide/download-objects.md") in the _Amazon Simple
Storage Service User Guide_.

## Encrypting your audit reports

You can optionally configure encryption on the Amazon S3 bucket containing your
audit reports. AWS Private CA supports two encryption modes for assets in S3:

- Automatic server-side encryption with Amazon S3-managed AES-256
  keys.
- Customer managed encryption using AWS Key Management Service and an AWS KMS key configured to your specifications.

###### Note

AWS Private CA does not support using default KMS keys generated
automatically by S3.

The following procedures describe how to set up each of the
encryption options.

###### To configure automatic encryption

Complete the following steps to enable S3 server-side
encryption.

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Buckets** table, choose the
   bucket that will hold your AWS Private CA assets.
3. On the page for your bucket, choose the
   **Properties** tab.
4. Choose the **Default encryption**
   card.
5. Choose **Enable**.
6. Choose **Amazon S3 key (SSE-S3)**.
7. Choose **Save Changes**.

###### To configure custom encryption

Complete the following steps to enable encryption using a custom key.

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Buckets** table, choose the
   bucket that will hold your AWS Private CA assets.
3. On the page for your bucket, choose the
   **Properties** tab.
4. Choose the **Default encryption**
   card.
5. Choose **Enable**.
6. Choose **AWS Key Management Service key (SSE-KMS)**.
7. Choose either **Choose from your AWS KMS keys** or
   **Enter AWS KMS key ARN**.
8. Choose **Save Changes**.
9. (Optional) If you do not have an KMS key already, create one using the following AWS CLI
   [create-key](../../../cli/latest/reference/kms/create-key.md "../../../cli/latest/reference/kms/create-key.md") command:

```
`$` `aws kms create-key`
```

The output contains the key ID and Amazon Resource Name (ARN) of the KMS key.
The following is an example output:

```
{
    "KeyMetadata": {
        "KeyId": "01234567-89ab-cdef-0123-456789abcdef",
        "Description": "",
        "Enabled": true,
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "CreationDate": 1478910250.94,
        "Arn": "arn:aws:kms:us-west-2:123456789012:key/01234567-89ab-cdef-0123-456789abcdef",
        "AWSAccountId": "123456789012"
    }
}
```

10. Using the following steps, you give the AWS Private CA service principal
    permission to use the KMS key. By default, all KMS keys are private; only the resource owner can
    use a KMS key to encrypt and decrypt data. However, the resource owner can
    grant permissions to access the KMS key to other users and resources. The service
    principal must be in the same Region as where the KMS key is stored.
    1.  First, save the default policy for your KMS key as `policy.json` using the
        following [get-key-policy](../../../cli/latest/reference/kms/get-key-policy.md "../../../cli/latest/reference/kms/get-key-policy.md") command:

    ```
    `$` `aws kms get-key-policy --key-id `key-id` --policy-name default --output text > ./policy.json`
    ```

    2.  Open the `policy.json` file in a text editor. Select one of the following policy statements and add it to the existing policy.

    If your Amazon S3 bucket key is _enabled_, use the following statement:

    ```
    {
       "Sid":"Allow ACM-PCA use of the key",
       "Effect":"Allow",
       "Principal":{
          "Service":"acm-pca.amazonaws.com"
       },
       "Action":[
          "kms:GenerateDataKey",
          "kms:Decrypt"
       ],
       "Resource":"*",
       "Condition":{
          "StringLike":{
             "kms:EncryptionContext:aws:s3:arn":"arn:aws:s3:::`bucket-name`"
          }
       }
    }
    ```

    If your Amazon S3 bucket key is _disabled_, use the following statement:

    ```
    {
       "Sid":"Allow ACM-PCA use of the key",
       "Effect":"Allow",
       "Principal":{
          "Service":"acm-pca.amazonaws.com"
       },
       "Action":[
          "kms:GenerateDataKey",
          "kms:Decrypt"
       ],
       "Resource":"*",
       "Condition":{
          "StringLike":{
             "kms:EncryptionContext:aws:s3:arn":[
                "arn:aws:s3:::`bucket-name`/acm-pca-permission-test-key",
                "arn:aws:s3:::`bucket-name`/acm-pca-permission-test-key-private",
                "arn:aws:s3:::`bucket-name`/audit-report/*",
                "arn:aws:s3:::`bucket-name`/crl/*"
             ]
          }
       }
    }
    ```

    3.  Finally, apply the updated policy using the following [put-key-policy](../../../cli/latest/reference/kms/put-key-policy.md "../../../cli/latest/reference/kms/put-key-policy.md") command:

    ```
    `$` `aws kms put-key-policy --key-id `key_id` --policy-name default --policy file://policy.json`
    ```
