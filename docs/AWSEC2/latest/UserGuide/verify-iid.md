

# Verify the instance identity document for an Amazon EC2 instance
<a name="verify-iid"></a>

If you intend to use the contents of the instance identity document for an important purpose, you should verify its contents and authenticity before using it.

The plaintext instance identity document is accompanied by three hashed and encrypted signatures. You can use these signatures to verify the origin and authenticity of the instance identity document and the information that it includes. The following signatures are provided:
+ Base64-encoded signature—This is a base64-encoded SHA256 hash of the instance identity document that is encrypted using an RSA key pair.
+ PKCS7 signature—This is a SHA1 hash of the instance identity document that is encrypted using a DSA key pair.
+ RSA-2048 signature—This is a SHA256 hash of the instance identity document that is encrypted using an RSA-2048 key pair.

Each signature is available at a different endpoint in the instance metadata. You can use any one of these signatures depending on your hashing and encryption requirements. To verify the signatures, you must use the corresponding AWS public certificate.

**Contents**
+ [Option 1: Verify instance identity document using the PKCS7 signature](#verify-pkcs7)
+ [Option 2: Verify instance identity document using the base64-encoded signature](#verify-signature)
+ [Option 3: Verify instance identity document using the RSA-2048 signature](#verify-rsa2048)

## Option 1: Verify instance identity document using the PKCS7 signature
<a name="verify-pkcs7"></a>

This topic explains how to verify the instance identity document using the PKCS7 signature and the AWS DSA public certificate.

### Linux instances
<a name="verify-pkcs7-linux"></a>

**To verify the instance identity document using the PKCS7 signature and the AWS DSA public certificate**

1. Connect to the instance.

1. Retrieve the PKCS7 signature from the instance metadata and add it to a new file named `pkcs7` along with the required header and footer. Use one of the following commands depending on the IMDS version used by the instance.

------
#### [ IMDSv2 ]

   ```
   $ echo "-----BEGIN PKCS7-----" >> {{pkcs7}} \
   	&& TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
   	&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/instance-identity/pkcs7 >> {{pkcs7}} \
   	&& echo "" >> {{pkcs7}} \
   	&& echo "-----END PKCS7-----" >> {{pkcs7}}
   ```

------
#### [ IMDSv1 ]

   ```
   $ echo "-----BEGIN PKCS7-----" >> {{pkcs7}} \
   	&& curl -s http://169.254.169.254/latest/dynamic/instance-identity/pkcs7 >> {{pkcs7}} \
   	&& echo "" >> {{pkcs7}} \
   	&& echo "-----END PKCS7-----" >> {{pkcs7}}
   ```

------

1. Find the **DSA** public certificate for your Region in [AWS public certificates for instance identity document signatures](regions-certs.md) and add the contents to a new file named `certificate`.

1. Use the **OpenSSL smime** command to verify the signature. Include the `-verify` option to indicate that the signature needs to be verified, and the `-noverify` option to indicate that the certificate does not need to be verified.

   ```
   $ openssl smime -verify -in {{pkcs7}} -inform PEM -certfile {{certificate}} -noverify | tee document
   ```

   If the signature is valid, the `Verification successful` message appears.

   The command also writes the contents of the instance identity document to a new file named `document`. You can compare the contents of the of the instance identity document from the instance metadata with the contents of this file using the following commands.

   ```
   $ openssl dgst -sha256 < {{document}}
   ```

   ```
   $ curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/instance-identity/document | openssl dgst -sha256
   ```

    If the signature cannot be verified, contact Support.

### Windows instances
<a name="verify-pkcs7-windows"></a>

**Prerequisites**  
This procedure requires the `System.Security` Microsoft .NET Core class. To add the class to your PowerShell session, run the following command.

```
PS C:\> Add-Type -AssemblyName System.Security
```

**Note**  
The command adds the class to the current PowerShell session only. If you start a new session, you must run the command again.

**To verify the instance identity document using the PKCS7 signature and the AWS DSA public certificate**

1. Connect to the instance.

1. Retrieve the PKCS7 signature from the instance metadata, convert it to a byte array, and add it to a variable named `$Signature`. Use one of the following commands depending on the IMDS version used by the instance.

------
#### [ IMDSv2 ]

   ```
   PS C:\> [string]$token = (Invoke-WebRequest -Method Put -Headers @{'X-aws-ec2-metadata-token-ttl-seconds' = '21600'} -Uri http://169.254.169.254/latest/api/token).Content
   ```

   ```
   PS C:\> {{$Signature}} = [Convert]::FromBase64String((Invoke-WebRequest -Headers @{'X-aws-ec2-metadata-token' = $Token} -Uri http://169.254.169.254/latest/dynamic/instance-identity/pkcs7).Content)
   ```

------
#### [ IMDSv1 ]

   ```
   PS C:\> {{$Signature}} = [Convert]::FromBase64String((Invoke-WebRequest -Uri http://169.254.169.254/latest/dynamic/instance-identity/pkcs7).Content)
   ```

------

1. Retrieve the plaintext instance identity document from the instance metadata, convert it to a byte array, and add it to a variable named `$Document`. Use one of the following commands depending on the IMDS version used by the instance.

------
#### [ IMDSv2 ]

   ```
   PS C:\> {{$Document }}= [Text.Encoding]::UTF8.GetBytes((Invoke-WebRequest -Headers @{'X-aws-ec2-metadata-token' = $Token} -Uri http://169.254.169.254/latest/dynamic/instance-identity/document).Content)
   ```

------
#### [ IMDSv1 ]

   ```
   PS C:\> {{$Document}} =  [Text.Encoding]::UTF8.GetBytes((Invoke-WebRequest http://169.254.169.254/latest/dynamic/instance-identity/document).Content)
   ```

------

1. Find the **DSA** public certificate for your Region in [AWS public certificates for instance identity document signatures](regions-certs.md) and add the contents to a new file named `certificate.pem`.

1. Extract the certificate from the certificate file and store it in a variable named `$Store`.

   ```
   PS C:\> {{$Store}} = [Security.Cryptography.X509Certificates.X509Certificate2Collection]::new([Security.Cryptography.X509Certificates.X509Certificate2]::new((Resolve-Path {{certificate.pem}})))
   ```

1. Verify the signature.

   ```
   PS C:\> {{$SignatureDocument}} = [Security.Cryptography.Pkcs.SignedCms]::new()
   ```

   ```
   PS C:\> {{$SignatureDocument}}.Decode({{$Signature}})
   ```

   ```
   PS C:\> {{$SignatureDocument}}.CheckSignature({{$Store}}, $true)
   ```

   If the signature is valid, the command returns no output. If the signature cannot be verified, the command returns `Exception calling "CheckSignature" with "2" argument(s): "Cannot find the original signer`. If your signature cannot be verified, contact AWS Support.

1. Validate the content of the instance identity document.

   ```
   PS C:\> [Linq.Enumerable]::SequenceEqual(${{SignatureDocument}}.ContentInfo.Content, {{$Document}})
   ```

   If the content of the instance identity document is valid, the command returns `True`. If instance identity document can't be validated, contact AWS Support.

## Option 2: Verify instance identity document using the base64-encoded signature
<a name="verify-signature"></a>

This topic explains how to verify the instance identity document using the base64-encoded signature and the AWS RSA public certificate.

### Linux instances
<a name="verify-signature-linux"></a>

**To validate the instance identity document using the base64-encoded signature and the AWS RSA public certificate**

1. Connect to the instance.

1. Retrieve the base64-encoded signature from the instance metadata, convert it to binary, and add it to a file named `signature`. Use one of the following commands depending on the IMDS version used by the instance.

------
#### [ IMDSv2 ]

   ```
   $ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
   	&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/instance-identity/signature | base64 -d >> {{signature}}
   ```

------
#### [ IMDSv1 ]

   ```
   $ curl -s http://169.254.169.254/latest/dynamic/instance-identity/signature | base64 -d >> {{signature}}
   ```

------

1. Retrieve the plaintext instance identity document from the instance metadata and add it to a file named `document`. Use one of the following commands depending on the IMDS version used by the instance.

------
#### [ IMDSv2 ]

   ```
   $ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
   	&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/instance-identity/document >> {{document}}
   ```

------
#### [ IMDSv1 ]

   ```
   $ curl -s http://169.254.169.254/latest/dynamic/instance-identity/document >> {{document}}
   ```

------

1. Find the **RSA** public certificate for your Region in [AWS public certificates for instance identity document signatures](regions-certs.md) and add the contents to a new file named `certificate`.

1. Extract the public key from the AWS RSA public certificate and save it to a file named `key`.

   ```
   $ openssl x509 -pubkey -noout -in {{certificate}} >> {{key}}
   ```

1. Use **OpenSSL dgst** command to verify the instance identity document.

   ```
   $ openssl dgst -sha256 -verify {{key}} -signature {{signature}} {{document}}
   ```

   If the signature is valid, the `Verification successful` message appears.

   The command also writes the contents of the instance identity document to a new file named `document`. You can compare the contents of the of the instance identity document from the instance metadata with the contents of this file using the following commands.

   ```
   $ openssl dgst -sha256 < {{document}}
   ```

   ```
   $ curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/instance-identity/document | openssl dgst -sha256
   ```

    If the signature cannot be verified, contact Support.

### Windows instances
<a name="verify-signature-windows"></a>

**To validate the instance identity document using the base64-encoded signature and the AWS RSA public certificate**

1. Connect to the instance.

1. Retrieve the base64-encoded signature from the instance metadata, convert it to a byte array, and add it to variable named `$Signature`. Use one of the following commands depending on the IMDS version used by the instance.

------
#### [ IMDSv2 ]

   ```
   PS C:\> [string]$token = (Invoke-WebRequest -Method Put -Headers @{'X-aws-ec2-metadata-token-ttl-seconds' = '21600'} http://169.254.169.254/latest/api/token).Content
   ```

   ```
   PS C:\> {{$Signature}} = [Convert]::FromBase64String((Invoke-WebRequest -Headers @{'X-aws-ec2-metadata-token' = $Token} http://169.254.169.254/latest/dynamic/instance-identity/signature).Content)
   ```

------
#### [ IMDSv1 ]

   ```
   PS C:\> {{$Signature}} = [Convert]::FromBase64String((Invoke-WebRequest http://169.254.169.254/latest/dynamic/instance-identity/signature).Content)
   ```

------

1. Retrieve the plaintext instance identity document from the instance metadata, convert it to a byte array, and add it to a variable named `$Document`. Use one of the following commands depending on the IMDS version used by the instance.

------
#### [ IMDSv2 ]

   ```
   PS C:\> {{$Document }}= [Text.Encoding]::UTF8.GetBytes((Invoke-WebRequest -Headers @{'X-aws-ec2-metadata-token' = $Token} http://169.254.169.254/latest/dynamic/instance-identity/document).Content)
   ```

------
#### [ IMDSv1 ]

   ```
   PS C:\> {{$Document}} =  [Text.Encoding]::UTF8.GetBytes((Invoke-WebRequest http://169.254.169.254/latest/dynamic/instance-identity/document).Content)
   ```

------

1. Find the **RSA** public certificate for your Region in [AWS public certificates for instance identity document signatures](regions-certs.md) and add the contents to a new file named `certificate.pem`.

1. Verify the instance identity document.

   ```
   PS C:\> [Security.Cryptography.X509Certificates.X509Certificate2]::new((Resolve-Path {{certificate.pem}})).PublicKey.Key.VerifyData({{$Document}}, 'SHA256', {{$Signature}})
   ```

   If the signature is valid, the command returns `True`. If the signature cannot be verified, contact Support.

## Option 3: Verify instance identity document using the RSA-2048 signature
<a name="verify-rsa2048"></a>

This topic explains how to verify the instance identity document using the RSA-2048 signature and the AWS RSA-2048 public certificate.

### Linux instances
<a name="verify-rsa2048-linux"></a>

**To verify the instance identity document using the RSA-2048 signature and the AWS RSA-2048 public certificate**

1. Connect to the instance.

1. Retrieve the RSA-2048 signature from the instance metadata and add it to a file named `rsa2048` along the required header and footer. Use one of the following commands depending on the IMDS version used by the instance.

------
#### [ IMDSv2 ]

   ```
   $ echo "-----BEGIN PKCS7-----" >> {{rsa2048}} \
   	&& TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
   	&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/instance-identity/rsa2048 >> {{rsa2048}} \
   	&& echo "" >> {{rsa2048}} \
   	&& echo "-----END PKCS7-----" >> {{rsa2048}}
   ```

------
#### [ IMDSv1 ]

   ```
   $ echo "-----BEGIN PKCS7-----" >> {{rsa2048}} \
   	&& curl -s http://169.254.169.254/latest/dynamic/instance-identity/rsa2048 >> {{rsa2048}} \
   	&& echo "" >> {{rsa2048}} \
   	&& echo "-----END PKCS7-----" >> {{rsa2048}}
   ```

------

1. Find the **RSA-2048** public certificate for your Region in [AWS public certificates for instance identity document signatures](regions-certs.md) and add the contents to a new file named `certificate`.

1. Use the **OpenSSL smime** command to verify the signature. Include the `-verify` option to indicate that the signature needs to be verified, and the `-noverify` option to indicate that the certificate does not need to be verified.

   ```
   $ openssl smime -verify -in {{rsa2048}} -inform PEM -certfile {{certificate}} -noverify | tee document
   ```

   If the signature is valid, the `Verification successful` message appears. If the signature cannot be verified, contact Support.

### Windows instances
<a name="verify-rsa2048-windows"></a>

**Prerequisites**  
This procedure requires the `System.Security` Microsoft .NET Core class. To add the class to your PowerShell session, run the following command.

```
PS C:\> Add-Type -AssemblyName System.Security
```

**Note**  
The command adds the class to the current PowerShell session only. If you start a new session, you must run the command again.

**To verify the instance identity document using the RSA-2048 signature and the AWS RSA-2048 public certificate**

1. Connect to the instance.

1. Retrieve the RSA-2048 signature from the instance metadata, convert it to a byte array, and add it to a variable named `$Signature`. Use one of the following commands depending on the IMDS version used by the instance.

------
#### [ IMDSv2 ]

   ```
   PS C:\> [string]$token = (Invoke-WebRequest -Method Put -Headers @{'X-aws-ec2-metadata-token-ttl-seconds' = '21600'} http://169.254.169.254/latest/api/token).Content
   ```

   ```
   PS C:\> {{$Signature}} = [Convert]::FromBase64String((Invoke-WebRequest -Headers @{'X-aws-ec2-metadata-token' = $Token} http://169.254.169.254/latest/dynamic/instance-identity/rsa2048).Content)
   ```

------
#### [ IMDSv1 ]

   ```
   PS C:\> {{$Signature}} = [Convert]::FromBase64String((Invoke-WebRequest http://169.254.169.254/latest/dynamic/instance-identity/rsa2048).Content)
   ```

------

1. Retrieve the plaintext instance identity document from the instance metadata, convert it to a byte array, and add it to a variable named `$Document`. Use one of the following commands depending on the IMDS version used by the instance.

------
#### [ IMDSv2 ]

   ```
   PS C:\> {{$Document }}= [Text.Encoding]::UTF8.GetBytes((Invoke-WebRequest -Headers @{'X-aws-ec2-metadata-token' = $Token} http://169.254.169.254/latest/dynamic/instance-identity/document).Content)
   ```

------
#### [ IMDSv1 ]

   ```
   PS C:\> {{$Document}} =  [Text.Encoding]::UTF8.GetBytes((Invoke-WebRequest http://169.254.169.254/latest/dynamic/instance-identity/document).Content)
   ```

------

1. Find the **RSA-2048** public certificate for your Region in [AWS public certificates for instance identity document signatures](regions-certs.md) and add the contents to a new file named `certificate.pem`.

1. Extract the certificate from the certificate file and store it in a variable named `$Store`.

   ```
   PS C:\> {{$Store}} = [Security.Cryptography.X509Certificates.X509Certificate2Collection]::new([Security.Cryptography.X509Certificates.X509Certificate2]::new((Resolve-Path {{certificate.pem}})))
   ```

1. Verify the signature.

   ```
   PS C:\> {{$SignatureDocument}} = [Security.Cryptography.Pkcs.SignedCms]::new()
   ```

   ```
   PS C:\> {{$SignatureDocument}}.Decode({{$Signature}})
   ```

   ```
   PS C:\> {{$SignatureDocument}}.CheckSignature({{$Store}}, $true)
   ```

   If the signature is valid, the command returns no output. If the signature cannot be verified, the command returns `Exception calling "CheckSignature" with "2" argument(s): "Cannot find the original signer`. If your signature cannot be verified, contact AWS Support.

1. Validate the content of the instance identity document.

   ```
   PS C:\> [Linq.Enumerable]::SequenceEqual(${{SignatureDocument}}.ContentInfo.Content, {{$Document}})
   ```

   If the content of the instance identity document is valid, the command returns `True`. If instance identity document can't be validated, contact AWS Support.