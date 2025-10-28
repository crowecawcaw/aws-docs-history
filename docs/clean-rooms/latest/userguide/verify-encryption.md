# Step 8: Verify data encryption

###### To verify that the data was encrypted

1.  View the encrypted data file (for example, `sales-output.csv`).
2.  Verify the following columns:

        1. Column **1** – Encrypted (for example,
         `username_fingerprint`).


        For the fingerprint columns (HMAC), after the version and type
         prefix (for example, `01:hmac:`), there are 44 characters of base64-encoded
         data.
        2. Column **2** – Not encrypted (for example,
         `purchased`).
        3. Column **3** – Encrypted (for example,
         `product_sealed`).


        For encrypted (SELECT) columns, the length of the
         cleartext plus any padding after the version and type prefix (for
         example, `01:enc:`) is directly proportional to the length of the
         cleartext that was encrypted. That is, the length is the size of the
         input plus approximately 33 percent overhead because of the encoding.

    You are now ready to:

3.  [Upload the encrypted data to S3](prepare-data-S3.md#upload-to-s3 "prepare-data-S3.md#upload-to-s3").
4.  [Create an AWS Glue table](prepare-data-S3.md#create-glue-crawler "prepare-data-S3.md#create-glue-crawler").
5.  [Create a configured table in
    AWS Clean Rooms](create-configured-table.md "create-configured-table.md").
    The C3R encryption client will create temporary files that don't contain unencrypted data (unless
    that data would also be unencrypted in the final output). However, some encrypted values might
    not be padded properly. Fingerprint columns might contain duplicate values, even if the
    collaboration setting `allowRepeatedFingerprintValue` is `false`. This
    issues occurs because the temporary file is written before proper padding lengths and
    duplicate-removal properties are checked.

If the C3R encryption client fails or is interrupted during encryption, it might stop after
writing the temporary file but before checking these properties and deleting the temporary
files. Therefore, these temporary files might still be on disk. If this is the case, the
contents in these files doesn't protect the plaintext data to the same levels that the output
does. In particular, these temporary files might reveal plaintext data to statistical analyses
that would not work against the final output. The user should delete these files (particularly
a SQLite database) to prevent these files from falling into unauthorized
hands.
