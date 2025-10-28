# Convert CSE-KMS table data to SSE-KMS

If your workflows currently use CSE-KMS for table data encryption, transition
to SSE-KMS with the following steps.

## Prerequisite

If you still write data using a CSE-KMS workgroup or client-side settings,
follow the steps in [Migrate from CSE-KMS to SSE-KMS](migrating-csekms-ssekms.md "migrating-csekms-ssekms.md") to update it
to SSE-KMS. This prevents new CSE-KMS encrypted data from being added during
the migration process from any other workflows that might write to the
tables.

## Data migration

1. Check if the table has the `has_encrypted_data` property set to `true`.
   This property specifies that the table might contain CSE-KMS
   encrypted data. However, it's important to note that this property
   could be present even on tables without any actual CSE-KMS encrypted
   data.

Console

    1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/ "https://console.aws.amazon.com/athena/").
    2. Choose **Launch query
     editor**.
    3. On the left side of the editor, under
     **Database**, choose the database
     that you want to query.
    4. In the Query editor, run the following query
     to see the value set to the
     `has_encrypted_data table`
     property.



    ```
    SHOW TBLPROPERTIES `<table_name>`('has_encrypted_data');
    ```

CLI
Start Athena query that shows the value of the
`has_encrypted_data` property on the table as
shown in the following example.

```
aws athena start-query-execution \
    --query-string "SHOW TBLPROPERTIES `<table-name>`('has_encrypted_data');" \
    --work-group "`<my-workgroup>`"
```

Fetch query results to check the value of
`has_encrypted_data` table property for the table
as shown in the following example.

```
aws athena get-query-results --query-execution-id `<query-execution-id-from-previous-step>`
```

2. For each CSE-KMS encrypted object in the table.
   1. Download the object from S3 using the S3 encryption client
      and decrypt it. Here is an example with AWS Java SDK
      V2.

   **Imports**

   ```
   import software.amazon.awssdk.core.ResponseInputStream;
   import software.amazon.awssdk.services.s3.model.GetObjectRequest;
   import software.amazon.awssdk.services.s3.model.GetObjectResponse;
   import software.amazon.encryption.s3.S3EncryptionClient;
   import software.amazon.encryption.s3.materials.Keyring;
   import software.amazon.encryption.s3.materials.KmsDiscoveryKeyring;
   ```

   Code

   ```
   final Keyring kmsDiscoveryKeyRing = KmsDiscoveryKeyring.builder()
           .enableLegacyWrappingAlgorithms(true)
           .build();
   final S3EncryptionClient s3EncryptionClient = S3EncryptionClient.builder()
           .enableLegacyUnauthenticatedModes(true)
           .keyring(kmsDiscoveryKeyRing)
           .build();

   GetObjectRequest getObjectRequest = GetObjectRequest.builder()
           .bucket("`amzn-s3-demo-bucket`")
           .key("`<my-key>`")
           .build();

   ResponseInputStream<GetObjectResponse> s3Object = s3EncryptionClient.getObject(getObjectRequest);

   ```

   2. Upload the object to S3 with the same name and SSE-KMS
      encryption. Here is an example with AWS Java SDK
      V2.

   **Imports**

   ```
   import software.amazon.awssdk.core.ResponseInputStream;
   import software.amazon.awssdk.core.sync.RequestBody;
   import software.amazon.awssdk.services.s3.S3Client;
   import software.amazon.awssdk.services.s3.model.PutObjectRequest;
   import software.amazon.awssdk.services.s3.model.ServerSideEncryption;
   ```

   **Code**

   ```
   final S3Client s3Client = S3Client.builder()
           .build();

   PutObjectRequest putObjectRequest = PutObjectRequest.builder()
           .bucket("`amzn-s3-demo-bucket`")
           .key("`<my-key>`")
           .serverSideEncryption(ServerSideEncryption.AWS_KMS)
           .ssekmsKeyId("`<my-kms-key>`")
           .build();

   s3Client.putObject(putObjectRequest, RequestBody.fromBytes(s3Object.readAllBytes()));

   ```

## Post migration

After successfully re-encrypting all CSE-KMS files in the table,
perform the following steps.

1. Remove the `has_encrypted_data` property from the
   table.

Console

    1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/ "https://console.aws.amazon.com/athena/").
    2. Choose **Launch query
     editor**.
    3. On the left side of the editor, under
     **Database**, choose the database
     that you want to query.
    4. In the Query editor, run the following query
     for your table.



    ```
    ALTER TABLE `<database-name>`.`<table-name>` UNSET TBLPROPERTIES ('has_encrypted_data')
    ```

CLI
Run the following command to remove the
`has_encrypted_data` property from your
table.

```
aws athena start-query-execution \
    --query-string "ALTER TABLE `<database-name>`.`<table-name>` UNSET TBLPROPERTIES ('has_encrypted_data');" \
    --work-group "`<my-workgroup>`"
```

2. Update your workflows to use a basic S3 client instead of a S3
   encryption client and then specify SSE-KMS encryption for data
   writes.
