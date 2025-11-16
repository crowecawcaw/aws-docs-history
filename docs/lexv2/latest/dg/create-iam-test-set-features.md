# Create an IAM role for the Test

Workbench - Advanced Features

###### Permission setup for Test workbench IAM role

This section shows several example AWS Identity and Access Management (IAM)
identity-based policies to implement least-privilege access controls for Test
Workbench permissions.

1. **Policy for Test Workbench to read audio files in
   S3** – This policy enables Test Workbench to read audio
   files being used in the test sets. The below policy should be accordingly
   modified to update `S3BucketName` and
   `S3Path` to point them to an Amazon S3 location of
   the audio files in a test set.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TestWorkbenchS3AudioFilesReadOnly",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::`S3BucketName`/`S3Path`/*"
 ]
 }
 ]
}`

```

2. **Policy for Test Workbench to read and write test
   sets and results into an Amazon S3 bucket** – This policy
   enables Test Workbench to store the test set inputs and results. The below
   policy should be modified to update `S3BucketName`
   to the Amazon S3 Bucket where test-set data will be stored. Test Workbench stores
   these data exclusively in your Amazon S3 bucket and not in the Lex Service
   infrastructure. Therefore For this reason, Test Workbench requires access to
   your Amazon S3 bucket to function properly.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TestSetDataUploadWithEncryptionOnly",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`S3BucketName`/*/lex_testworkbench/test_set/*",
 "arn:aws:s3:::`S3BucketName`/*/lex_testworkbench/test_execution/*",
 "arn:aws:s3:::`S3BucketName`/*/lex_testworkbench/test_set_discrepancy_report/*"
 ],
 "Condition": {
 "StringEquals": {
 "s3:x-amz-server-side-encryption": "aws:kms"
 }
 }
 },
 {
 "Sid": "TestSetDataGetObject",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::`S3BucketName`/*/lex_testworkbench/test_set/*",
 "arn:aws:s3:::`S3BucketName`/*/lex_testworkbench/test_execution/*",
 "arn:aws:s3:::`S3BucketName`/*/lex_testworkbench/test_set_discrepancy_report/*"
 ]
 },
 {
 "Sid": "TestSetListS3Objects",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`S3BucketName`"
 ]
 }
 ]
}`

```

3. **Policy for Test Workbench to read CloudWatch
   Logs** – This policy enables Test Workbench to generate
   test-sets from Lex Conversation Text Logs stored in Amazon CloudWatch Logs.
   The below policy should be modified to update
   `Region`,
   `AwsAccountId`,
   `LogGroupName`.
4. **Policy for Test Workbench to call Lex
   Runtime** – This policy enables Test Workbench to execute
   a test set against Lex bots. The below policy should be modified to update
   `Region`,
   `AwsAccountId`,
   `BotId`. Since Test Workbench can test any bot
   in your Lex environment, you can replace the resource with
   "arn:aws:lex:`Region`:`AwsAccountId`:bot-alias/\*"
   to allow Test Workbench access to all Amazon Lex V2 bots in an account.
5. **(Optional) Policy for Test Workbench to encrypt and
   decrypt test set data** – If Test Workbench is configured
   to store test-set inputs and results in Amazon S3 buckets using a customer
   managed KMS key, Test Workbench will need both encryption and decryption
   permission to the KMS key. The below policy should be modified to update
   `Region`,
   `AwsAccountId`, and
   `KmsKeyId` where
   `KmsKeyId` is the ID of the customer managed
   KMS key.
6. **(Optional) Policy for Test Workbench to decrypt
   audio files** – If Audio files are stored in the S3
   bucket using customer managed KMS key, Test Workbench will need decryption
   permission to the KMS keys. The below policy should be modified to update
   `Region`,
   `AwsAccountId`, and
   `KmsKeyId` where
   `KmsKeyId` is the ID of the customer managed
   KMS key used to encrypt the audio files.
