# Prerequisites for exporting an instance from Amazon EC2

To export a VM from Amazon EC2, first meet the following prerequisites:

- Create an Amazon S3 bucket for storing the exported instances or choose an existing
  bucket. The bucket must be in the Region where you want export your VMs.
  Additionally, the bucket must belong to the AWS account where you are
  performing the export operation. For more information, see the
  [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").
- You can't export a VM to an S3 bucket that uses the bucket owner enforced
  setting for S3 Object Ownership because ACLs are disabled. For more
  information, see [Configuring
  ACLs](../../../AmazonS3/latest/userguide/managing-acls.md "../../../AmazonS3/latest/userguide/managing-acls.md") in the _Amazon Simple Storage Service User Guide_.
- Prepare your S3 bucket by attaching an access control list (ACL) containing
  the following grants. For more information, see [Managing access with ACLs](../../../AmazonS3/latest/userguide/acls.md "../../../AmazonS3/latest/userguide/acls.md")
  in the _Amazon Simple Storage Service User Guide_.
  - For each `Grantee`, provide the following permissions:
    - `READ_ACP` (In the Amazon S3 console, **Bucket
      ACL** should have the **Read**
      permission)
    - `WRITE` (In the Amazon S3 console,
      **Objects** should have the
      **Write** permission)

  - For `Grantee`, provide the appropriate Region-specific
    canonical account ID:
    - Africa (Cape Town) – 3f7744aeebaf91dd60ab135eb1cf908700c8d2bc9133e61261e6c582be6e33ee
    - Asia Pacific (Hong Kong) – 97ee7ab57cc9b5034f31e107741a968e595c0d7a19ec23330eae8d045a46edfb
    - Asia Pacific (Hyderabad) – 77ab5ec9eac9ade710b7defed37fe0640f93c5eb76ea65a64da49930965f18ca
    - Asia Pacific (Jakarta) – de34aaa6b2875fa3d5086459cb4e03147cf1a9f7d03d82f02bedb991ff3d1df5
    - Asia Pacific (Malaysia) – ed006f67543afcfe0779e356e52d5ed53fa45f95bcd7d277147dfc027aaca0e7
    - Asia Pacific (Melbourne) – 8b8ea36ab97c280aa8558c57a380353ac7712f01f82c21598afbb17e188b9ad5
    - Asia Pacific (New Zealand) – 2dc8fa4ca1c59da5c6a4c5b0e397eea130ec62e49f18cff179034665fd20e8a2
    - Asia Pacific (Osaka) – 40f22ffd22d6db3b71544ed6cd00c8952d8b0a63a87d58d5b074ec60397db8c9
    - Asia Pacific (Taipei) – a9fa0eb7c8483f9558cd14b24d16e9c4d1555261a320b586a3a06908ff0047ce
    - Asia Pacific (Thailand) – d011fe83abcc227a7ac0f914ce411d3630c4ef735e92e88ce0aa796dcfecfbdd
    - Canada West (Calgary) – 78e12f8d798f89502177975c4ccdac686c583765cea2bf06e9b34224e2953c83
    - Europe (Milan) – 04636d9a349e458b0c1cbf1421858b9788b4ec28b066148d4907bb15c52b5b9c
    - Europe (Spain) – 6e81c4c52a37a7f59e103625162ed97bcd0e646593adb107d21310d093151518
    - Europe (Zurich) – 5d9fcea77b2fb3df05fc15c893f212ae1d02adb4b24c13e18586db728a48da67
    - Israel (Tel Aviv) – 328a78de7561501444823ebeb59152eca7cb58fee2fe2e4223c2cdd9f93ae931
    - Mexico (Central) – edaff67fe25d544b855bd0ba9a74a99a2584ab89ceda0a9661bdbeca530d0fca
    - Middle East (Bahrain) – aa763f2cf70006650562c62a09433f04353db3cba6ba6aeb3550fdc8065d3d9f
    - Middle East (UAE) – 7d3018832562b7b6c126f5832211fae90bd3eee3ed3afde192d990690267e475
    - AWS GovCloud (US) – af913ca13efe7a94b88392711f6cfc8aa07c9d1454d4f190a624b126733a5602
    - All other Regions – c4d8eabf8db69dbe46bfe0e517100c554f01200b104d59cd408e777ba442a322

## Configure your S3 bucket

Console

###### To configure the S3 bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Select the bucket in which to store the exported instances.
3. On the **Permissions** tab, change the object ownership
   to **Bucket owner preferred**.
4. Attach the following bucket policy. For `CanonicalUser`, enter
   the canonical account ID for the bucket Region. For `Resource`,
   enter the name of your bucket in the bucket ARNs.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GrantReadAclAndWrite",
 "Effect": "Allow",
 "Principal": {
 "CanonicalUser": "`c4d8eabf8db69dbe46bfe0e517100c554f01200b104d59cd408e777ba442a322`"
 },
 "Action": [
 "s3:GetBucketAcl",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-export-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-export-bucket`/*"
 ]
 }
 ]
}`

```

AWS CLI

###### To configure the S3 bucket

Use the [put-bucket-ownership-controls](../../../cli/latest/reference/s3api/put-bucket-ownership-controls.md "../../../cli/latest/reference/s3api/put-bucket-ownership-controls.md") command to change the object
ownership.

```
aws s3api put-bucket-ownership-controls \
    --bucket amzn-s3-demo-export-bucket \
    --ownership-controls='{"Rules":[{"ObjectOwnership":"BucketOwnerPreferred"}]}'
```

Use the [put-bucket-policy](../../../cli/latest/reference/s3api/put-bucket-policy.md "../../../cli/latest/reference/s3api/put-bucket-policy.md") command to attach the bucket policy. For
`CanonicalUser`, enter the canonical account ID for the bucket
Region. For `Resource`, enter the name of your bucket in the
bucket ARNs.

```
aws s3api put-bucket-policy \
    --bucket `amzn-s3-demo-export-bucket` \
    --policy \
'{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GrantReadAcpAndWrite",
            "Effect": "Allow",
            "Principal": {
                "CanonicalUser": "`c4d8eabf8db69dbe46bfe0e517100c554f01200b104d59cd408e777ba442a322`"
            },
            "Action": [
                "s3:GetBucketAcl",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-export-bucket`",
                "arn:aws:s3:::`amzn-s3-demo-export-bucket`/*"
            ]
        }
    ]
}'
```

PowerShell

###### To configure the S3 bucket

Use the [Write-S3BucketOwnershipControl](../../../powershell/latest/reference/items/Write-S3BucketOwnershipControl.md "../../../powershell/latest/reference/items/Write-S3BucketOwnershipControl.md") cmdlet to change the object
ownership.

```
Write-S3BucketOwnershipControl `
    -BucketName "amzn-s3-demo-export-bucket" `
    -OwnershipControls_Rule @{ObjectOwnership="BucketOwnerPreferred"}
```

Use the [Write-S3BucketPolicy](../../../powershell/latest/reference/items/Write-S3BucketPolicy.md "../../../powershell/latest/reference/items/Write-S3BucketPolicy.md") cmdlet to attach the bucket policy. For
`CanonicalUser`, enter the canonical account ID for the bucket
Region. For `Resource`, enter the name of your bucket in the
bucket ARNs.

```
Write-S3BucketPolicy `
    -BucketName "`amzn-s3-demo-export-bucket`" `
    -Policy `
'{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GrantReadAcpAndWrite",
            "Effect": "Allow",
            "Principal": {
                "CanonicalUser": "`c4d8eabf8db69dbe46bfe0e517100c554f01200b104d59cd408e777ba442a322`"
            },
            "Action": [
                "s3:GetBucketAcl",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-export-bucket`",
                "arn:aws:s3:::`amzn-s3-demo-export-bucket`/*"
            ]
        }
    ]
}'
```
