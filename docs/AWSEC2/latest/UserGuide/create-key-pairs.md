# Create a key pair for your Amazon EC2 instance

You can use Amazon EC2 to create your key pairs, or you can use a third-party tool to create
your key pairs, and then import them to Amazon EC2.

Amazon EC2 supports 2048-bit SSH-2 RSA keys for Linux and Windows instances. Amazon EC2 also
supports ED25519 keys for Linux instances.

For instructions on how to connect to your instance after you have created a key pair, see
[Connect to your Linux instance using SSH](connect-to-linux-instance.md "connect-to-linux-instance.md") and [Connect to your Windows instance using RDP](connecting_to_windows_instance.md "connecting_to_windows_instance.md").

###### Contents

- [Create a key pair using Amazon EC2](#having-ec2-create-your-key-pair "#having-ec2-create-your-key-pair")
- [Create a key pair using AWS CloudFormation](#create-key-pair-cloudformation "#create-key-pair-cloudformation")
- [Create a key pair using
  a third-party tool and import the public key to Amazon EC2](#how-to-generate-your-own-key-and-import-it-to-aws "#how-to-generate-your-own-key-and-import-it-to-aws")

## Create a key pair using Amazon EC2

When you create a key pair using Amazon EC2, the public key is stored in Amazon EC2, and you store
the private key.

You can create up to 5,000 key pairs per Region. To request an increase, create a
support case. For more information, see [Creating a
support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case") in the _Support User Guide_.

Console

###### To create a key pair using Amazon EC2

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Network & Security**,
   choose **Key Pairs**.
3. Choose **Create key pair**.
4. For **Name**, enter a descriptive name for the key pair.
   Amazon EC2 associates the public key with the name that you specify as the key name. A
   key name can include up to 255 ASCII characters. It can’t include leading or
   trailing spaces.
5. Select a key pair type appropriate for your operating system:

(Linux instances) For **Key pair type**, choose either
**RSA** or **ED25519**.

(Windows instances) For **Key pair type**, choose
**RSA**. **ED25519** keys are not supported
for Windows instances. 6. For **Private key file format**, choose the format in which
to save the private key. To save the private key in a format that can be used with
OpenSSH, choose **pem**. To save the private key in a format that
can be used with PuTTY, choose **ppk**. 7. To add a tag to the public key, choose **Add
tag**, and enter the key and value for the tag. Repeat for each tag. 8. Choose **Create key pair**. 9. The private key file is automatically downloaded by your browser. The base
file name is the name that you specified as the name of your key pair, and the
file name extension is determined by the file format that you chose. Save the
private key file in a safe place.

###### Important

This is the only chance for you to save the private key file. 10. If you plan to use an SSH client on a macOS or Linux computer to connect to your Linux
instance, use the following command to set the permissions of your private key file so that
only you can read it.

```
`chmod 400 `key-pair-name`.pem`
```

If you do not set these permissions, then you cannot connect to your instance using this
key pair. For more information, see [Error: Unprotected private key file](TroubleshootingInstancesConnecting.md#troubleshoot-unprotected-key "TroubleshootingInstancesConnecting.md#troubleshoot-unprotected-key").

AWS CLI

###### To create a key pair using Amazon EC2

1. Use the [create-key-pair](../../../cli/latest/reference/ec2/create-key-pair.md "../../../cli/latest/reference/ec2/create-key-pair.md") command as follows to generate the key
   pair and to save the private key to a `.pem` file.
   The `--query` option prints the private key material to the
   output. The `--output` option saves the private key material
   in the specified file. The extension should be either `.pem`
   or `.ppk`, depending on the key format. The private key name
   can be different from the public key name, but for ease of use, use the same
   name.

```
aws ec2 create-key-pair \
    --key-name `my-key-pair` \
    --key-type `rsa` \
    --key-format `pem` \
    --query "KeyMaterial" \
    --output text > `my-key-pair.pem`
```

2. If you plan to use an SSH client on a macOS or Linux computer to connect to your Linux
   instance, use the following command to set the permissions of your private key file so that
   only you can read it.

```
`chmod 400 `key-pair-name`.pem`
```

If you do not set these permissions, then you cannot connect to your instance using this
key pair. For more information, see [Error: Unprotected private key file](TroubleshootingInstancesConnecting.md#troubleshoot-unprotected-key "TroubleshootingInstancesConnecting.md#troubleshoot-unprotected-key").

PowerShell

###### To create a key pair using Amazon EC2

Use the [New-EC2KeyPair](../../../powershell/latest/reference/items/New-EC2KeyPair.md "../../../powershell/latest/reference/items/New-EC2KeyPair.md") cmdlet as follows to generate
the key and save it to a `.pem` or `.ppk`
file. The **Out-File** cmdlet saves the private key
material in a file with the specified extension. The extension should be
either `.pem` or `.ppk`, depending on the key format.
The private key name can be different from the public key name,
but for ease of use, use the same name.

```
(New-EC2KeyPair `
    -KeyName "`my-key-pair`" `
    -KeyType "`rsa`" `
    -KeyFormat "`pem`").KeyMaterial | Out-File -Encoding ascii -FilePath `C:\path\my-key-pair`.pem
```

## Create a key pair using AWS CloudFormation

When you create a new key pair using AWS CloudFormation, the private key is saved to AWS Systems Manager
Parameter Store. The parameter name has the following format:

```
/ec2/keypair/`key_pair_id`
```

For more information, see [AWS Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md")
in the _AWS Systems Manager User Guide_.

###### To create a key pair using AWS CloudFormation

1. Specify the [AWS::EC2::KeyPair](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-keypair.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-keypair.md") resource in your template.

```
Resources:
  NewKeyPair:
    Type: 'AWS::EC2::KeyPair'
    Properties:
      KeyName: new-key-pair
```

2. Use the [describe-key-pairs](../../../cli/latest/reference/ec2/describe-key-pairs.md "../../../cli/latest/reference/ec2/describe-key-pairs.md") command as follows to get the ID of the
   key pair.

```
aws ec2 describe-key-pairs --filters Name=key-name,Values=`new-key-pair` --query KeyPairs[*].KeyPairId --output text
```

The following is example output.

```
key-05abb699beEXAMPLE
```

3. Use the [get-parameter](../../../cli/latest/reference/ssm/get-parameter.md "../../../cli/latest/reference/ssm/get-parameter.md") command as follows to get the parameter for
   your key and save the key material in a `.pem` file.

```
aws ssm get-parameter --name /ec2/keypair/`key-05abb699beEXAMPLE` --with-decryption --query Parameter.Value --output text > `new-key-pair.pem`
```

###### Required IAM permissions

To enable AWS CloudFormation to manage Parameter Store parameters on your behalf, the IAM role
assumed by AWS CloudFormation or your user must have the following permissions:

- `ssm:PutParameter` – Grants permission to create a parameter for
  the private key material.
- `ssm:DeleteParameter` – Grants permission to delete the parameter
  that stored the private key material. This permission is required whether the key pair
  was imported or created by AWS CloudFormation.

When AWS CloudFormation deletes a key pair that was created or imported by a stack, it performs a
permissions check to determine whether you have permission to delete parameters, even though
AWS CloudFormation creates a parameter only when it creates a key pair, not when it imports a key pair.
AWS CloudFormation tests for the required permission using a fabricated parameter name that does not
match any parameter in your account. Therefore, you might see a fabricated parameter name in
the `AccessDeniedException` error message.

## Create a key pair using

a third-party tool and import the public key to Amazon EC2

Instead of using Amazon EC2 to create a key pair, you can create an RSA or ED25519 key pair
by using a third-party tool and then import the public key to Amazon EC2.

###### Requirements for key pairs

- Supported types:
  - (Linux and Windows) RSA
  - (Linux only) ED25519

  ###### Note

  ED25519 keys are not supported for Windows instances.
  - Amazon EC2 does not accept DSA keys.

- Supported formats:
  - OpenSSH public key format (for Linux, the format in
    `~/.ssh/authorized_keys`)
  - (Linux only) If you connect using SSH while using the EC2 Instance Connect API, the
    SSH2 format is also supported.
  - SSH private key file format must be PEM or PPK
  - (RSA only) Base64 encoded DER format
  - (RSA only) SSH public key file format as specified in [RFC 4716](https://www.ietf.org/rfc/rfc4716.txt "https://www.ietf.org/rfc/rfc4716.txt")

- Supported lengths:
  - 1024, 2048, and 4096.
  - (Linux only) If you connect using SSH while using the EC2 Instance Connect API, the
    supported lengths are 2048 and 4096.

###### To create a key pair using a third-party tool

1. Generate a key pair with a third-party tool of your choice. For example, you can use
   **ssh-keygen** (a tool provided with the standard OpenSSH
   installation). Alternatively, Java, Ruby, Python, and many other programming languages
   provide standard libraries that you can use to create a key pair.

###### Important

The private key must be in the PEM or PPK format. For example, use
`ssh-keygen -m PEM` to generate the OpenSSH key in the PEM format. 2. Save the public key to a local file. For example,
`~/.ssh/my-key-pair.pub` (Linux, macOS) or
`C:\keys\my-key-pair.pub` (Windows). The file name extension for
this file is not important. 3. Save the private key to a local file that has the `.pem` or
`.ppk` extension. For example, `~/.ssh/my-key-pair.pem`
or `~/.ssh/my-key-pair.ppk` (Linux, macOS) or
`C:\keys\my-key-pair.pem` or
`C:\keys\my-key-pair.ppk` (Windows). The file extension is
important because, depending on the tool you use to connect to your instance, you'll
need a specific file format. OpenSSH requires a `.pem` file, while
PuTTY requires a `.ppk` file.

###### Important

Save the private key file in a safe place. You'll need to provide the name of your
public key when you launch an instance, and the corresponding private key each time
you connect to the instance.

After you have created the key pair, use one of the following methods to import your
public key to Amazon EC2.

Console

###### To import the public key to Amazon EC2

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Key Pairs**.
3. Choose **Import key pair**.
4. For **Name**, enter a descriptive name for the public key.
   The name can include up to 255 ASCII characters. It can’t include leading or
   trailing spaces.

###### Note

When you connect to your instance from the EC2 console, the console suggests
this name for the name of your private key file. 5. Either choose **Browse** to navigate to and select your
public key, or paste the contents of your public key into the **Public key
contents** field. 6. Choose **Import key pair**. 7. Verify that the public key that you imported appears in the list of key
pairs.

AWS CLI

###### To import the public key to Amazon EC2

Use the [import-key-pair](../../../cli/latest/reference/ec2/import-key-pair.md "../../../cli/latest/reference/ec2/import-key-pair.md") command.

```
aws ec2 import-key-pair \
    --key-name `my-key-pair` \
    --public-key-material fileb://`path`/`my-key-pair.pub`
```

###### To verify that the key pair was imported successfully

Use the [describe-key-pairs](../../../cli/latest/reference/ec2/describe-key-pairs.md "../../../cli/latest/reference/ec2/describe-key-pairs.md") command.

```
aws ec2 describe-key-pairs --key-names `my-key-pair`
```

PowerShell

###### To import the public key to Amazon EC2

Use the [Import-EC2KeyPair](../../../powershell/latest/reference/items/Import-EC2KeyPair.md "../../../powershell/latest/reference/items/Import-EC2KeyPair.md") cmdlet.

```
$publickey=[Io.File]::ReadAllText("C:\Users\TestUser\.ssh\id_rsa.pub")
Import-EC2KeyPair `
    -KeyName `my-key-pair` `
    -PublicKey $publickey
```

###### To verify that the key pair was imported successfully

Use the [Get-EC2KeyPair](../../../powershell/latest/reference/items/Get-EC2KeyPair.md "../../../powershell/latest/reference/items/Get-EC2KeyPair.md") cmdlet.

```
Get-EC2KeyPair -KeyName `my-key-pair`
```
