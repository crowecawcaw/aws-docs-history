# Use `GenerateDataKeyWithoutPlaintext` with an AWS SDK or CLI

The following code examples show how to use `GenerateDataKeyWithoutPlaintext`.

CLI

**AWS CLI**

**To generate a 256-bit symmetric data key without a plaintext key**

The following `generate-data-key-without-plaintext` example requests an encrypted copy of a 256-bit symmetric data key for use outside of AWS. You can call AWS KMS to decrypt the data key when you are ready to use it.

To request a 256-bit data key, use the `key-spec` parameter with a value of `AES_256`. To request a 128-bit data key, use the `key-spec` parameter with a value of `AES_128`. For all other data key lengths, use the `number-of-bytes` parameter.

The KMS key you specify must be a symmetric encryption KMS key, that is, a KMS key with a key spec value of SYMMETRIC_DEFAULT.

```
`aws kms generate-data-key-without-plaintext \
 --key-id `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"` \
 --key-spec `AES_256``

```

Output:

```
{
    "CiphertextBlob": "AQEDAHjRYf5WytIc0C857tFSnBaPn2F8DgfmThbJlGfR8P3WlwAAAH4wfAYJKoZIhvcNAQcGoG8wbQIBADBoBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDEFogL",
    "KeyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "KeyMaterialId": "0b7fd7ddbac6eef27907413567cad8c810e2883dc8a7534067a82ee1142fc1e6"
}
```

The `CiphertextBlob` (encrypted data key) is returned in base64-encoded format.

For more information, see [Data keys](concepts.md#data-keys "concepts.md#data-keys") in the _AWS Key Management Service Developer Guide_.

- For API details, see
  [GenerateDataKeyWithoutPlaintext](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/generate-data-key-without-plaintext.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/generate-data-key-without-plaintext.html")
  in _AWS CLI Command Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/kms#code-examples").

```
async fn make_key(client: &Client, key: &str) -> Result<(), Error> {
    let resp = client
        .generate_data_key_without_plaintext()
        .key_id(key)
        .key_spec(DataKeySpec::Aes256)
        .send()
        .await?;

    // Did we get an encrypted blob?
    let blob = resp.ciphertext_blob.expect("Could not get encrypted text");
    let bytes = blob.as_ref();

    let s = base64::encode(bytes);

    println!();
    println!("Data key:");
    println!("{}", s);

    Ok(())
}


```

- For API details, see
  [GenerateDataKeyWithoutPlaintext](https://docs.rs/aws-sdk-kms/latest/aws_sdk_kms/client/struct.Client.html#method.generate_data_key_without_plaintext "https://docs.rs/aws-sdk-kms/latest/aws_sdk_kms/client/struct.Client.html#method.generate_data_key_without_plaintext")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
