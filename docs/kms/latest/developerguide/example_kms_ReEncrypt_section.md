# Use `ReEncrypt` with an AWS SDK or CLI

The following code examples show how to use `ReEncrypt`.

CLI

**AWS CLI**

**Example 1: To re-encrypt an encrypted message under a different symmetric KMS key (Linux and macOS).**

The following `re-encrypt` command example demonstrates the recommended way to re-encrypt data with the AWS CLI.

Provide the ciphertext in a file.In the value of the `--ciphertext-blob` parameter, use the `fileb://` prefix, which tells the CLI to read the data from a binary file. If the file is not in the current directory, type the full path to file. For more information about reading AWS CLI parameter values from a file, see [Loading AWS CLI parameters from a file](../../../cli/latest/userguide/cli-usage-parameters-file.md "../../../cli/latest/userguide/cli-usage-parameters-file.md") in the _AWS Command Line Interface User Guide_ and [Best Practices for Local File Parameters](https://aws.amazon.com/blogs/developer/best-practices-for-local-file-parameters/ "https://aws.amazon.com/blogs/developer/best-practices-for-local-file-parameters/") in the _AWS Command Line Tool Blog_.Specify the source KMS key, which decrypts the ciphertext.The `--source-key-id` parameter is not required when decrypting with symmetric encryption KMS keys. AWS KMS can get the KMS key that was used to encrypt the data from the metadata in the ciphertext blob. But it's always a best practice to specify the KMS key you are using. This practice ensures that you use the KMS key that you intend, and prevents you from inadvertently decrypting a ciphertext using a KMS key you do not trust.Specify the destination KMS key, which re-encrypts the data.The `--destination-key-id` parameter is always required. This example uses a key ARN, but you can use any valid key identifier.Request the plaintext output as a text value.The `--query` parameter tells the CLI to get only the value of the `Plaintext` field from the output. The `--output` parameter returns the output as text.Base64-decode the plaintext and save it in a file.The following example pipes (|) the value of the `Plaintext` parameter to the Base64 utility, which decodes it. Then, it redirects (>) the decoded output to the `ExamplePlaintext` file.

Before running this command, replace the example key IDs with valid key identifiers from your AWS account.

```
`aws kms re-encrypt \
 --ciphertext-blob `fileb://ExampleEncryptedFile` \
 --source-key-id `1234abcd-12ab-34cd-56ef-1234567890ab` \
 --destination-key-id `0987dcba-09fe-87dc-65ba-ab0987654321` \
 --query `CiphertextBlob` \
 --output `text` `|` `base64` --decode `>` `ExampleReEncryptedFile``

```

This command produces no output. The output from the `re-encrypt` command is base64-decoded and saved in a file.

For more information, see [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md") in the _AWS Key Management Service API Reference_.

**Example 2: To re-encrypt an encrypted message under a different symmetric KMS key (Windows command prompt).**

The following `re-encrypt` command example is the same as the previous one except that it uses the `certutil` utility to Base64-decode the plaintext data. This procedure requires two commands, as shown in the following examples.

Before running this command, replace the example key ID with a valid key ID from your AWS account.

```
`aws kms re-encrypt `^`
 --ciphertext-blob `fileb://ExampleEncryptedFile` `^`
 --source-key-id `1234abcd-12ab-34cd-56ef-1234567890ab` `^`
 --destination-key-id `0987dcba-09fe-87dc-65ba-ab0987654321` `^`
 --query `CiphertextBlob` `^`
 --output `text` `>` `ExampleReEncryptedFile.base64``

```

Then use the `certutil` utility

```
certutil -decode ExamplePlaintextFile.base64 ExamplePlaintextFile
```

Output:

```
Input Length = 18
Output Length = 12
CertUtil: -decode command completed successfully.
```

For more information, see [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md") in the _AWS Key Management Service API Reference_.

- For API details, see
  [ReEncrypt](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/re-encrypt.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/re-encrypt.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kms#code-examples").

```
class KeyEncrypt:
    def __init__(self, kms_client):
        self.kms_client = kms_client

    @classmethod
    def from_client(cls) -> "KeyEncrypt":
        """
        Creates a KeyEncrypt instance with a default KMS client.

        :return: An instance of KeyEncrypt initialized with the default KMS client.
        """
        kms_client = boto3.client("kms")
        return cls(kms_client)


    def re_encrypt(self, source_key_id, cipher_text):
        """
        Takes ciphertext previously encrypted with one key and reencrypt it by using
        another key.

        :param source_key_id: The ARN or ID of the original key used to encrypt the
                              ciphertext.
        :param cipher_text: The encrypted ciphertext.
        :return: The ciphertext encrypted by the second key.
        """
        destination_key_id = input(
            f"Your ciphertext is currently encrypted with key {source_key_id}. "
            f"Enter another key ID or ARN to reencrypt it: "
        )
        if destination_key_id != "":
            try:
                cipher_text = self.kms_client.re_encrypt(
                    SourceKeyId=source_key_id,
                    DestinationKeyId=destination_key_id,
                    CiphertextBlob=cipher_text,
                )["CiphertextBlob"]
            except ClientError as err:
                logger.error(
                    "Couldn't reencrypt your ciphertext. Here's why: %s",
                    err.response["Error"]["Message"],
                )
            else:
                print(f"Reencrypted your ciphertext as: {cipher_text}")
                return cipher_text
        else:
            print("Skipping reencryption demo.")



```

- For API details, see
  [ReEncrypt](../../../goto/boto3/kms-2014-11-01/ReEncrypt.md "../../../goto/boto3/kms-2014-11-01/ReEncrypt.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/kms#code-examples").

```

require 'aws-sdk-kms' # v2: require 'aws-sdk'

# Human-readable version of the ciphertext of the data to reencrypt.

blob = '01020200785d68faeec386af1057904926253051eb2919d3c16078badf65b808b26dd057c101747cadf3593596e093d4ffbf22434a6d00000068306606092a864886f70d010706a0593057020100305206092a864886f70d010701301e060960864801650304012e3011040c9d629e573683972cdb7d94b30201108025b20b060591b02ca0deb0fbdfc2f86c8bfcb265947739851ad56f3adce91eba87c59691a9a1'
sourceCiphertextBlob = [blob].pack('H*')

# Replace the fictitious key ARN with a valid key ID

destinationKeyId = 'arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321'

client = Aws::KMS::Client.new(region: 'us-west-2')

resp = client.re_encrypt({
                           ciphertext_blob: sourceCiphertextBlob,
                           destination_key_id: destinationKeyId
                         })

# Display a readable version of the resulting re-encrypted blob.
puts 'Blob:'
puts resp.ciphertext_blob.unpack('H*')


```

- For API details, see
  [ReEncrypt](../../../goto/SdkForRubyV3/kms-2014-11-01/ReEncrypt.md "../../../goto/SdkForRubyV3/kms-2014-11-01/ReEncrypt.md")
  in _AWS SDK for Ruby API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/kms#code-examples").

```
async fn reencrypt_string(
    verbose: bool,
    client: &Client,
    input_file: &str,
    output_file: &str,
    first_key: &str,
    new_key: &str,
) -> Result<(), Error> {
    // Get blob from input file
    // Open input text file and get contents as a string
    // input is a base-64 encoded string, so decode it:
    let data = fs::read_to_string(input_file)
        .map(|input_file| base64::decode(input_file).expect("invalid base 64"))
        .map(Blob::new);

    let resp = client
        .re_encrypt()
        .ciphertext_blob(data.unwrap())
        .source_key_id(first_key)
        .destination_key_id(new_key)
        .send()
        .await?;

    // Did we get an encrypted blob?
    let blob = resp.ciphertext_blob.expect("Could not get encrypted text");
    let bytes = blob.as_ref();

    let s = base64::encode(bytes);
    let o = &output_file;

    let mut ofile = File::create(o).expect("unable to create file");
    ofile.write_all(s.as_bytes()).expect("unable to write");

    if verbose {
        println!("Wrote the following to {}:", output_file);
        println!("{}", s);
    } else {
        println!("Wrote base64-encoded output to {}", output_file);
    }

    Ok(())
}


```

- For API details, see
  [ReEncrypt](https://docs.rs/aws-sdk-kms/latest/aws_sdk_kms/client/struct.Client.html#method.re_encrypt "https://docs.rs/aws-sdk-kms/latest/aws_sdk_kms/client/struct.Client.html#method.re_encrypt")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
