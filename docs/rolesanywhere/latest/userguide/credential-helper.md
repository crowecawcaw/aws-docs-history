# Get temporary security credentials from IAM Roles Anywhere

To obtain temporary security credentials from AWS Identity and Access Management Roles Anywhere, use the
credential helper tool that IAM Roles Anywhere provides. This tool is compatible
with the `credential_process` feature available across
the language SDKs. When used with an AWS SDK, these credentials
automatically refresh before they expire, requiring no additional
implementation for credential renewal. The helper manages the process
of creating a signature with the certificate and calling the endpoint
to obtain session credentials; it returns the credentials to the calling
process in a standard JSON format.

See
[Temporary security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md")
for more information on session credentials.

To download the credential helper tool, use the following links. Releases for Darwin and Windows on or after version 1.1.1 are signed.

| Platform | Architecture | Download URL                                                                                                                                                                                                                                                                                                     | SHA256 checksum                                                  |
| -------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Linux    | x86-64       | [https://rolesanywhere.amazonaws.com/releases/1.7.2/X86_64/Linux/Amzn2023/aws_signing_helper](https://rolesanywhere.amazonaws.com/releases/1.7.2/X86_64/Linux/Amzn2023/aws_signing_helper "https://rolesanywhere.amazonaws.com/releases/1.7.2/X86_64/Linux/Amzn2023/aws_signing_helper")                         | 39d406c703e07a3943831a3164474770a15c40243d8ffed0a2fcdf8eccf84274 |
| Windows  | x86-64       | [https://rolesanywhere.amazonaws.com/releases/1.7.2/X86_64/Windows/Server2019/aws_signing_helper.exe](https://rolesanywhere.amazonaws.com/releases/1.7.2/X86_64/Windows/Server2019/aws_signing_helper.exe "https://rolesanywhere.amazonaws.com/releases/1.7.2/X86_64/Windows/Server2019/aws_signing_helper.exe") | 56d340cd58e7ce50e407838688e64f90533a9f42ae445d955252f2f28ff1e9a2 |
| Darwin   | x86-64       | [https://rolesanywhere.amazonaws.com/releases/1.7.2/X86_64/MacOS/Ventura/aws_signing_helper](https://rolesanywhere.amazonaws.com/releases/1.7.2/X86_64/MacOS/Ventura/aws_signing_helper "https://rolesanywhere.amazonaws.com/releases/1.7.2/X86_64/MacOS/Ventura/aws_signing_helper")                            | 106baf58e5eeb7c4d84b0472c2d3c0cd6dc89e47ebed467789d3297a1790a913 |
| Linux    | Aarch64      | [https://rolesanywhere.amazonaws.com/releases/1.7.2/Aarch64/Linux/Amzn2023/aws_signing_helper](https://rolesanywhere.amazonaws.com/releases/1.7.2/Aarch64/Linux/Amzn2023/aws_signing_helper "https://rolesanywhere.amazonaws.com/releases/1.7.2/Aarch64/Linux/Amzn2023/aws_signing_helper")                      | 75e998e9a6b63f579421c2f8dd6fb38a9d69c987a4399ab6ce1da60684f759ee |
| Darwin   | Aarch64      | [https://rolesanywhere.amazonaws.com/releases/1.7.2/Aarch64/MacOS/Sonoma/aws_signing_helper](https://rolesanywhere.amazonaws.com/releases/1.7.2/Aarch64/MacOS/Sonoma/aws_signing_helper "https://rolesanywhere.amazonaws.com/releases/1.7.2/Aarch64/MacOS/Sonoma/aws_signing_helper")                            | 3708c4ac1418c6485dee04ba718a0d5318c9e841fdb32005ae36dd1e01e483f0 |

###### Important

To get temporary credentials, you need all of the following:

- A Profile configured in AWS Identity and Access Management Roles Anywhere
- A Role ARN from IAM
- An end-entity certificate from your certificate authority
- The certificate associated private key is required in most cases, except when inferred. For example when using OS certificate stores.
- A trust anchor configured in IAM Roles Anywhere
  For more information, see [Getting started](getting-started.md "getting-started.md").

## Credential Helper on GitHub

The source code for the credential helper is available on [GitHub](https://github.com/aws/rolesanywhere-credential-helper "https://github.com/aws/rolesanywhere-credential-helper") so that you can adapt the helper to your needs.
We encourage you to submit pull requests for changes that you would like to have included. However, AWS doesn't provide support for running modified copies of this software.

###### Note

You can find more modes and options and for credential helper in the [README.md](https://github.com/aws/rolesanywhere-credential-helper/blob/main/README.md "https://github.com/aws/rolesanywhere-credential-helper/blob/main/README.md").

## Advanced Features

The credential helper supports several advanced features for working with different types of key storage and authentication mechanisms.

### OS Certificate Store Integration

On Windows and macOS, the credential helper can leverage private keys and certificates stored in OS-specific secure stores:

- **Windows:** Both CNG and Cryptography APIs are supported. By default, only the user's "MY" certificate store is searched, but you can specify a different store using the `--system-store-name` option.
- **macOS:** Keychain Access is supported. The credential helper searches Keychains on the search list.

To use certificates from these stores, use the `--cert-selector` option instead of providing certificate and private key files.

#### macOS Keychain Integration

For securing keys through macOS Keychain, consider creating a dedicated Keychain that only the credential helper can access:

1. Create a new Keychain:

```
security create-keychain -p ${CREDENTIAL_HELPER_KEYCHAIN_PASSWORD} credential-helper.keychain
```

2. Unlock the Keychain:

```
security unlock-keychain -p ${CREDENTIAL_HELPER_KEYCHAIN_PASSWORD} credential-helper.keychain
```

3. Add the Keychain to the search list:

```
EXISTING_KEYCHAINS=$(security list-keychains | cut -d '"' -f2) security list-keychains -s credential-helper.keychain $(echo ${EXISTING_KEYCHAINS} | awk -v ORS=" " '{print $1}')
```

4. Import your certificate and private key:

```
security import /path/to/identity.pfx -T /path/to/aws_signing_helper -P ${UNWRAPPING_PASSWORD} -k credential-helper.keychain
```

###### Note

Since the official credential helper binary is signed, but not notarized, so it isn't trusted by macOS by default. You may need to specify your Keychain password whenever the credential helper uses the private key, or choose to always allow the credential helper to use the Keychain item.

#### Windows CNG Integration

To use Windows CNG for key storage, import your certificate and private key into your user's "MY" certificate store:

```
certutil -user -p %UNWRAPPING_PASSWORD% -importPFX "MY" \path\to\identity.pfx
```

You can also use PowerShell cmdlets or Windows CNG/Cryptography APIs to import certificates.

### PKCS#11 Integration

The credential helper supports using certificates and keys from hardware or software PKCS#11 tokens and HSMs using PKCS#11 URIs:

- Use a certificate from a PKCS#11 token:

```
--certificate 'pkcs11:manufacturer=piv_II;id=%01'
```

- Use a certificate by object name:

```
--certificate 'pkcs11:object=My%20RA%20key'
```

- Use a certificate from a file but the key from a token:

```
--certificate client-cert.pem --private-key 'pkcs11:model=SoftHSM%20v2;object=My%20RA%20key'
```

Most Unix-based systems use [p11-kit](https://p11-glue.github.io/p11-glue/p11-kit/manual/config.html "https://p11-glue.github.io/p11-glue/p11-kit/manual/config.html") to provide consistent system-wide and per-user configuration of available PKCS#11 providers. For systems or containers that lack p11-kit, you can specify a specific PKCS#11 provider library using the `--pkcs11-lib` parameter.

If your private key object has the `CKA_ALWAYS_AUTHENTICATE` attribute set and the `CKU_CONTEXT_SPECIFIC` PIN matches the `CKU_USER` PIN, you can use the `--reuse-pin` parameter to avoid being prompted for the PIN multiple times.

###### Note

For YubiKey devices with PIV support, when a key pair and certificate exist in slots 9a or 9c, the YubiKey automatically generates an attestation certificate for the slot. To disambiguate between your certificate and the attestation certificate, use the `CKA_LABEL` (the `object` path attribute in a URI).

### TPM Integration

The credential helper supports TPM wrapped keys in the `-----BEGIN TSS2 PRIVATE KEY-----` format. You can use such a file as you would any plain key file. These files are supported by both TPMv2 OpenSSL engines/providers and GnuTLS.

###### Important

To use these commands below you must install the [tpm2-tools](https://github.com/tpm2-software/tpm2-tools "https://github.com/tpm2-software/tpm2-tools") software package. This package provides the necessary commands for working with TPM2 devices.

This package is available on many Linux distributions through standard package managers.

To create and use a TPM key with the credential helper:

1. Create a primary key in the TPM owner hierarchy:

```
tpm2_createprimary -G rsa -g sha256 -p ${TPM_PRIMARY_KEY_PASSWORD} -c parent.ctx -P ${OWNER_HIERARCHY_PASSWORD}
```

2. Create a child key with the primary key as its parent:

```
tpm2_create -C parent.ctx -u child.pub -r child.priv -P ${TPM_PRIMARY_KEY_PASSWORD} -p ${TPM_CHILD_KEY_PASSWORD}
```

3. Load the child key into the TPM and make it persistent:

```
tpm2_load -C parent.ctx -u child.pub -r child.priv -c child.ctx -P ${TPM_PRIMARY_KEY_PASSWORD}
CHILD_HANDLE=$(tpm2_evictcontrol -c child.ctx | cut -d ' ' -f 2 | head -n 1)
```

4. Create a CSR using the TPM key:

```
openssl req -provider tpm2 -provider default -propquery '?provider=tpm2' \
            -new -key handle:${CHILD_HANDLE} \
            -out client-csr.pem
```

5. After obtaining a certificate from your CA, use it with the credential helper:

```
./aws_signing_helper credential-process \
    --certificate /path/to/certificate/file \
    --private-key handle:${CHILD_HANDLE} \
    --role-arn ${ROLE_ARN} \
    --trust-anchor-arn ${TA_ARN} \
    --profile-arn ${PROFILE_ARN}
```

###### Important

When using TPM handles, it's your responsibility to clear out the persistent and temporary objects from the TPM after you no longer need them. If you load a key into the TPM that isn't password-protected, anyone with access to the machine can use that key.

Alternatively, you can use a TPM key file in the format described in the [TSS2 Private Key Format](https://www.hansenpartnership.com/draft-bottomley-tpm2-keys.html "https://www.hansenpartnership.com/draft-bottomley-tpm2-keys.html"). With this approach, the wrapped private key will be loaded into the TPM as a transient object and automatically flushed after use.

###### Note

For RSA keys used with the credential helper, ensure they have the sign attribute set. Some tools (like the IBM OpenSSL ENGINE) create RSA keys with the decrypt attribute but not the sign attribute by default. The credential helper delegates the signing operation to the TPM rather than implementing PKCS#1 v1.5 padding manually.

### Diagnostic Commands

The credential helper includes diagnostic commands that can help you troubleshoot issues:

#### read-certificate-data

Reads and displays information about a certificate. This is useful for verifying certificate details and finding the correct certificate when multiple certificates match a selector.

```
./aws_signing_helper read-certificate-data --certificate /path/to/certificate.pem
```

Or with a certificate selector:

```
./aws_signing_helper read-certificate-data --cert-selector Key=x509Subject,Value=CN=Subject
```

If multiple certificates match a selector, information about each of them is printed. For PKCS#11, URIs for each matched certificate are also printed to help uniquely identify certificates.

#### sign-string

Signs a fixed test string to validate your private key and digest configuration:

```
./aws_signing_helper sign-string --private-key /path/to/private-key.pem
```

Or with a certificate selector:

```
./aws_signing_helper sign-string --cert-selector Key=x509Subject,Value=CN=Subject
```

Optional parameters include:

- `--digest`: Must be one of SHA256 (default), SHA384, or SHA512
- `--format`: Must be one of text (default), json, or bin

## Available commands

The credential helper tool provides several commands to help you work with IAM Roles Anywhere. This section describes the available commands and their usage.

- [credential-process command](#credential-helper-credential-process "#credential-helper-credential-process") - Obtains temporary security credentials from IAM Roles Anywhere using your certificate and private key.
- [update command](#credential-helper-update "#credential-helper-update") - Obtains temporary security credentials from IAM Roles Anywhere and writes them directly to the AWS credentials file.
- [serve command](#credential-helper-serve "#credential-helper-serve") - Vends temporary security credentials from IAM Roles Anywhere through a local endpoint.

For additional commands and options, see the [credential helper README on GitHub](https://github.com/aws/rolesanywhere-credential-helper/blob/main/README.md "https://github.com/aws/rolesanywhere-credential-helper/blob/main/README.md").

### Comparison of credential-helper commands

| Feature                      | credential-process                  | update                      | serve                           |
| ---------------------------- | ----------------------------------- | --------------------------- | ------------------------------- |
| Automatic credential refresh | No (AWS CLI calls for each command) | Yes                         | Yes                             |
| SDK integration              | No (requires profile setup)         | No (requires profile setup) | Yes (with environment variable) |
| Credentials storage          | In memory                           | On disk                     | In memory                       |
| Best for                     | Single commands                     | AWS CLI usage               | SDK applications                |

## credential-process command

The credential-process command obtains temporary security credentials from IAM Roles Anywhere using your certificate and private key.

### Synopsis

```
./aws_signing_helper credential-process \
    --certificate
    [--cert-selector]
    [--endpoint]
    [--region]
    [--intermediates]
    --private-key
    [--tpm-key-password]
    [--pkcs11-lib]
    [--pkcs11-pin]
    [--reuse-pin]
    [--system-store-name]
    [--reuse-latest-expiring-certificate]
    --profile-arn
    --role-arn
    [--session-duration]
    --trust-anchor-arn
    [--with-proxy]
    [--no-verify-ssl]
    [--role-session-name]
```

### Options

`--certificate` (string)
Path to certificate file. Can also be a PKCS#11 URI (e.g., `pkcs11:manufacturer=piv_II;id=%01`) to use certificates from hardware or software PKCS#11 tokens/HSMs.

`--cert-selector` (string)

Specifies which certificate (and associated private key) to use from OS-specific secure stores. On Windows, this searches the user's "MY" certificate store (or another store specified with `--system-store-name`). On macOS, this searches Keychains on the search list.

The selector can be specified either through a JSON file or directly on the command line. It allows searching by certificate Subject, Issuer, and Serial Number using the keys `x509Subject`, `x509Issuer`, and `x509Serial`.

Example using a JSON file:

```
--cert-selector file://path/to/selector.json
```

Example using command line:

```
--cert-selector Key=x509Subject,Value=CN=Subject Key=x509Issuer,Value=CN=Issuer Key=x509Serial,Value=15D19632234BF759A32802C0DA88F9E8AFC8702D
```

`--endpoint` (string)

The IAM Roles Anywhere endpoint for the region. For a list of endpoints,
see [Service endpoints
and quotas](../../../general/latest/gr/rolesanywhere.md "../../../general/latest/gr/rolesanywhere.md").

`--region` (string)
Signing region.

`--intermediates` (string)
Path to intermediate certificate bundle.

`--private-key` (string)

Specifies the private key to use for signing. This can be:

- A Path to a plaintext private key file
- A PKCS#11 URI (e.g., `pkcs11:object=My%20RA%20key`)
- A TPM wrapped key file in the `-----BEGIN TSS2 PRIVATE KEY-----` format
- A TPM handle reference (e.g., `handle:0x81000001`)

Not required when using `--cert-selector` as the private key is inferred from the OS certificate store.

`--tpm-key-password` (string)
Password for TPM-protected private keys. Required when using password-protected TPM keys.

`--pkcs11-lib` (string)
Path to a specific PKCS#11 provider library. Only needed for systems or containers that lack p11-kit, otherwise the default p11-kit-proxy provider is used.

`--pkcs11-pin` (string)
PIN for PKCS#11 token authentication. Required when using PKCS#11 tokens that require authentication.

`--reuse-pin`
Boolean flag to reuse the PKCS#11 user PIN for object-specific authentication. Useful when the private key object has the `CKA_ALWAYS_AUTHENTICATE` attribute set and the `CKU_CONTEXT_SPECIFIC` PIN matches the `CKU_USER` PIN.

`--system-store-name` (string)
Windows only: Specifies a system certificate store other than "MY" (the default) in the `CERT_SYSTEM_STORE_CURRENT_USER` context. Only used with `--cert-selector`.

`--reuse-latest-expiring-certificate`
Boolean flag to use the latest expiring certificate when multiple certificates match a certificate selector. This can be useful when you have multiple valid certificates and want to use the one with the longest remaining validity period.

`--profile-arn` (string)
Profile to pull policies, attribute mappings and other data from.

`--role-arn` (string)
Target role to assume.

`--session-duration` (int)
Duration, in seconds, for the resulting session (corresponds to the `durationSeconds` parameter in the
`CreateSession` request). This is optional and can range from 900 seconds (15 minutes) up to 43200 seconds (12 hours).
Please see the `Expiration` subsection of the
[Credentials Object](authentication-create-session.md#credentials-object "authentication-create-session.md#credentials-object")
section for more details on how this value is used in determining the expiration of the vended session.

`--trust-anchor-arn` (string)
Trust anchor to use for authentication.

`--with-proxy`
To use the tool with a proxy. This is a boolean flag. Note that you will have to set the
`HTTPS_PROXY` environment variable with the address of the proxy server.

`--no-verify-ssl`

To disable SSL verification. This is a boolean flag.

###### Important

Note that this disables TLS host authentication, and can open the connection to man-in-the-middle attacks.
This option should only be used under specific, tightly controlled scenarios, such as debugging proxy connections.

`--role-session-name`

An identifier for the role session. Please see
[The relationship between CreateSession and AssumeRole](authentication-create-session.md#create-session-and-assume-role "authentication-create-session.md#create-session-and-assume-role")
section for more details on how this option will affect the `CreateSession` operation.

### Output

The credential helper tool will return a JSON containing the credentials.
This format allows the credentials to be consumed by the [external credential process](../../../sdkref/latest/guide/feature-process-credentials.md "../../../sdkref/latest/guide/feature-process-credentials.md") supported by the `credential_process`.

```

{
    "Version": 1,
    "AccessKeyId": `String`,
    "SecretAccessKey": `String`,
    "SessionToken": `String`,
    "Expiration": `Timestamp`
}

```

### Examples

###### Example Obtain temporary security credentials

Use the following command to get temporary security credentials. Specify the Region where you want to make the request.

###### Important

Before you run this command, make sure you have your certificate and private key. To get these credentials, follow the documentation from your certificate authority.

```
`$` `./aws_signing_helper credential-process \
 --certificate `/path/to/certificate` \
 --private-key `/path/to/private-key` \
 --trust-anchor-arn arn:aws:rolesanywhere:`region`:`account`:trust-anchor/`TA_ID` \
 --profile-arn arn:aws:rolesanywhere:`region`:`account`:profile/`PROFILE_ID` \
 --role-arn arn:aws:iam::`account`:role/`role-name-with-path``
```

###### Example Use temporary security credentials with AWS SDKs and the AWS CLI

To use temporary security credentials with AWS SDKs and the AWS CLI, you can
configure the credential helper tool as a credential process. For more information, see
[Sourcing credentials
with an external process](../../../cli/latest/userguide/cli-configure-sourcing-external.md "../../../cli/latest/userguide/cli-configure-sourcing-external.md").

The following example shows a the `config` file that sets the helper tool as
the credential process.

```
`[profile developer]
 credential_process = ./aws_signing_helper credential-process --certificate `/path/to/certificate` --private-key `/path/to/private-key` --trust-anchor-arn arn:aws:rolesanywhere:`region`:`account`:trust-anchor/`TA_ID` --profile-arn arn:aws:rolesanywhere:`region`:`account`:profile/`PROFILE_ID` --role-arn arn:aws:iam::`account`:role/`role-name-with-path`
 region = `region``
```

For using this profile with any AWS SDK not mentioned below, see 'Set a named profile' from
[Using shared config and credentials files to globally configure AWS SDKs and tools](../../../sdkref/latest/guide/file-format.md "../../../sdkref/latest/guide/file-format.md")

###### Example Python SDK

To specify your Roles Anywhere enabled profile for use with Python, see
[Boto3: Shared credentials file](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file").

###### Example Java SDK

To specify your Roles Anywhere enabled profile for use with Java, see
[Java 2.x: Use profiles](../../../sdk-for-java/latest/developer-guide/credentials-profiles.md "../../../sdk-for-java/latest/developer-guide/credentials-profiles.md")

###### Example C# SDK

To specify your Roles Anywhere enabled profile for use with C#, see
[Examples for classes SharedCredentialsFile and AWSCredentialsFactory](../../../sdk-for-net/v3/developer-guide/creds-locate.md#creds-locate-cred-shared-file "../../../sdk-for-net/v3/developer-guide/creds-locate.md#creds-locate-cred-shared-file")

###### Example Go SDK

To specify your IAM Roles Anywhere enabled profile for use with Go, see the Specifying Profiles section in
[Specifying Credentials](../../../sdk-for-go/v2/developer-guide/configure-gosdk.md#specifying-credentials "../../../sdk-for-go/v2/developer-guide/configure-gosdk.md#specifying-credentials")

## serve command

The serve command vends temporary security credentials from IAM Roles Anywhere through a local endpoint running on localhost. This endpoint is compatible with Instance Metadata Service (IMDSv2), allowing AWS SDKs to automatically discover and use the credentials without additional configuration.

### Synopsis

```
./aws_signing_helper serve \
        --certificate
        [--cert-selector]
        [--endpoint]
        [--region]
        [--intermediates]
        --private-key
        [--tpm-key-password]
        [--pkcs11-lib]
        [--pkcs11-pin]
        [--reuse-pin]
        [--system-store-name]
        [--reuse-latest-expiring-certificate]
        --profile-arn
        --role-arn
        [--session-duration]
        --trust-anchor-arn
        [--with-proxy]
        [--no-verify-ssl]
        [--role-session-name]
        [--port]
        [--hop-limit]
```

### Options

The serve command accepts all the options available to the [credential-process command](#credential-helper-credential-process-options "#credential-helper-credential-process-options"), plus the following additional options. For details on common options like `--cert-selector`, `--tpm-key-password`, `--pkcs11-lib`, and others, see the [Options section under credential-process](#credential-helper-credential-process-options "#credential-helper-credential-process-options").

`--port` (int)
The port on which the local endpoint will be exposed. Default is 9911.

`--hop-limit` (int)
The IP TTL (Time To Live) to set on response packets. Default is 64. Setting this to 1 maintains parity with EC2's IMDSv2 hop count behavior.

### Behavior

When you run the serve command, the credential helper starts a local server that:

- Listens on 127.0.0.1 at the specified port (default 9911)
- Implements the same URIs and request headers as IMDSv2
- Automatically refreshes credentials five minutes before the previous set expires
- Continues running until manually terminated

###### Important

When using the serve command, be aware that any process running on the system that can reach 127.0.0.1 will be able to retrieve AWS credentials from the credential helper.

### Examples

###### Example Start a credential server on the default port

```
`$` `./aws_signing_helper serve \
 --certificate `/path/to/certificate` \
 --private-key `/path/to/private-key` \
 --trust-anchor-arn arn:aws:rolesanywhere:`region`:`account`:trust-anchor/`TA_ID` \
 --profile-arn arn:aws:rolesanywhere:`region`:`account`:profile/`PROFILE_ID` \
 --role-arn arn:aws:iam::`account`:role/`role-name-with-path``
```

###### Example Start a credential server on a custom port with restricted hop limit

```
`$` `./aws_signing_helper serve \
 --certificate `/path/to/certificate` \
 --private-key `/path/to/private-key` \
 --trust-anchor-arn arn:aws:rolesanywhere:`region`:`account`:trust-anchor/`TA_ID` \
 --profile-arn arn:aws:rolesanywhere:`region`:`account`:profile/`PROFILE_ID` \
 --role-arn arn:aws:iam::`account`:role/`role-name-with-path` \
 --port 8000 \
 --hop-limit 1`
```

###### Example Use with AWS SDKs

To use the credentials served by the credential helper with AWS SDKs, set the `AWS_EC2_METADATA_SERVICE_ENDPOINT` environment variable to point to your local endpoint:

```
`$` `export AWS_EC2_METADATA_SERVICE_ENDPOINT=http://127.0.0.1:9911`
```

###### Important

Depending on which AWS SDK you are using, the above
environment variable must not end in a trailing '/' character.

AWS SDKs will use the environment variable and the credentials from this endpoint using their credential providers without any changes to application code. The SDKs will request new AWS credentials from the credential helper's server as needed.

## update command

The update command obtains temporary security credentials from IAM Roles Anywhere and writes them directly to the AWS credentials file. This allows the AWS CLI and SDKs to use the credentials without having to call the credential helper for each command.

### Synopsis

```
./aws_signing_helper update \
        --certificate
        [--cert-selector]
        [--endpoint]
        [--region]
        [--intermediates]
        --private-key
        [--tpm-key-password]
        [--pkcs11-lib]
        [--pkcs11-pin]
        [--reuse-pin]
        [--system-store-name]
        [--reuse-latest-expiring-certificate]
        --profile-arn
        --role-arn
        [--session-duration]
        --trust-anchor-arn
        [--with-proxy]
        [--no-verify-ssl]
        [--role-session-name]
        [--profile]
        [--once]
```

### Options

The update command accepts all the options available to the [credential-process command](#credential-helper-credential-process-options "#credential-helper-credential-process-options"), plus the following additional options. For details on common options like `--cert-selector`, `--tpm-key-password`, `--pkcs11-lib`, and others, see the [Options section under credential-process](#credential-helper-credential-process-options "#credential-helper-credential-process-options").

`--profile` (string)
The named profile in the AWS credentials file to update. If not specified, the default profile will be updated. If the profile doesn't exist, it will be created.

`--once`
Update the credentials only once and then exit. If not specified, the command will continuously update the credentials before they expire.

### Behavior

When you run the update command, the credential helper:

- Obtains temporary security credentials from IAM Roles Anywhere
- Writes the credentials directly to the AWS credentials file (~/.aws/credentials)
- Unless the `--once` flag is specified, automatically refreshes the credentials approximately five minutes before they expire
- Continues running until manually terminated (unless `--once` is specified)

###### Important

When using the update command, be aware that the credentials are written to a file on disk. Any user or process who can read the credentials file may be able to read and use those AWS credentials.

###### Note

Running the update command multiple times simultaneously, creating multiple processes, may not work as intended. There may be issues with concurrent writes to the credentials file.

### Examples

###### Example Update the default profile continuously

```
`$` `./aws_signing_helper update \
 --certificate `/path/to/certificate` \
 --private-key `/path/to/private-key` \
 --trust-anchor-arn arn:aws:rolesanywhere:`region`:`account`:trust-anchor/`TA_ID` \
 --profile-arn arn:aws:rolesanywhere:`region`:`account`:profile/`PROFILE_ID` \
 --role-arn arn:aws:iam::`account`:role/`role-name-with-path``
```

###### Example Update a named profile once

```
`$` `./aws_signing_helper update \
 --certificate `/path/to/certificate` \
 --private-key `/path/to/private-key` \
 --trust-anchor-arn arn:aws:rolesanywhere:`region`:`account`:trust-anchor/`TA_ID` \
 --profile-arn arn:aws:rolesanywhere:`region`:`account`:profile/`PROFILE_ID` \
 --role-arn arn:aws:iam::`account`:role/`role-name-with-path` \
 --profile developer \
 --once`
```

###### Example Use with AWS CLI

After running the update command, you can use the AWS CLI with the updated profile:

```
`$` `aws s3 ls --profile developer`
```

If you updated the default profile, you don't need to specify the profile:

```
`$` `aws s3 ls`
```

###### Example Use with JavaScript SDK

To specify your Roles Anywhere enabled profile for use with JavaScript, see
[Loading Credentials in Node.js from the Shared Credentials File](../../../sdk-for-javascript/v2/developer-guide/loading-node-credentials-shared.md "../../../sdk-for-javascript/v2/developer-guide/loading-node-credentials-shared.md")

## Credential Helper Changelog

### CredentialHelper version 1.7.2

On November 24, 2025, AWS IAM Roles Anywhere released Credential Helper version 1.7.2. As a part of this release, some security vulnerabilities were patched and some error messages were improved.

### CredentialHelper version 1.7.1

On August 12, 2025, AWS IAM Roles Anywhere released Credential Helper version 1.7.1. As part of this release, some security vulnerabilities were patched.

### CredentialHelper version 1.7.0

On Jun 2, 2025, AWS IAM Roles Anywhere released Credential Helper version 1.7.0. As part of this release, a bug was fixed that prevented adding custom roots for use in TLS, and an enhancement was introduced to make parsing logic more robust for cert selectors provided through the CLI. Dependency module versions were also upgraded to address any vulnerabilities picked up by scanners.

### CredentialHelper version 1.6.0

On May 6, 2025, AWS IAM Roles Anywhere released Credential Helper version 1.6.0. As part of this release, password-protected private keys in PKCS#8 format are now supported, and a fix was introduced for a bug where the credential helper opened terminal device files when the process didn't have a controlling terminal.

### CredentialHelper version 1.5.0

On April 3, 2025, AWS IAM Roles Anywhere released Credential Helper version 1.5.0. As a part of this release, an option was added to use the latest expiring certificate when multiple match a certificate selector, and some minor fixes were introduced related to PKCS#12 file support.

### CredentialHelper version 1.4.0

On December 13, 2024, AWS IAM Roles Anywhere released Credential Helper version 1.4.0. As a part of this release, TPM keys are now supported on Windows systems.

### CredentialHelper version 1.3.0

On November 13, 2024, AWS IAM Roles Anywhere released Credential Helper version 1.3.0. As a part of this release, TPM keys are supported for non-Windows systems, and a previously unhandled error when parsing certificate data from a file was fixed.

### CredentialHelper version 1.2.1

On October 22, 2024, AWS IAM Roles Anywhere released Credential Helper version 1.2.1. As a part of this release, some security vulnerabilities were patched.

### CredentialHelper version 1.2.0

On August 23, 2024, AWS IAM Roles Anywhere released Credential Helper version 1.2.0. As a part of this release, custom role session name is supported in the CreateSession request, a hop limit option is supported to limit the IP TTL on response packets for the serve command, and file updates for certificate and private key data are recognized by long-running commands and will be honored in subsequent credentialing requests.

### CredentialHelper version 1.1.1

On October 12, 2023, AWS IAM Roles Anywhere released Credential Helper version 1.1.1. As a part of this release, providers in Windows are attempted to be silenced when performing signing operations. Also, Windows user certificate store names can now be explicitly provided.

### CredentialHelper version 1.1.0

On September 20, 2023, AWS IAM Roles Anywhere released Credential Helper version 1.1.0. As a part of this release, PKCS#11 module integration is now supported. Also, any debug logs that previously went to stderr now go to stdout.

### CredentialHelper version 1.0.6

On August 16, 2023, AWS IAM Roles Anywhere released Credential Helper version 1.0.6. As a part of this release, certificates within OS secure stores that can't be parsed are now skipped. An issue relating to mismatched regions in the ARN inputs is also now fixed.

### CredentialHelper version 1.0.5

On July 25, 2023, AWS IAM Roles Anywhere released Credential Helper version 1.0.5. As a part of this release, some bugs relating to the update command were fixed. PKCS#12 containers that aren't password-protected are now supported. Lastly, MacOS Keychain Access and Windows CNG/CryptoAPI integrations are also now supported.

### CredentialHelper version 1.0.4

On January 17, 2023, AWS IAM Roles Anywhere released Credential Helper version 1.0.4. As a part of this release, some bugs specific to the serve command were fixed.

### CredentialHelper version 1.0.3

On December 5, 2022, AWS IAM Roles Anywhere released Credential Helper version 1.0.3. As a part of this release, the tool now supports the update and serve commands.

### CredentialHelper version 1.0.2

On September 8, 2022, AWS IAM Roles Anywhere released Credential Helper version 1.0.2. As a part of this release, the tool now sets the minimum TLS version to 1.2.

### CredentialHelper version 1.0.1

On July 14, 2022, AWS IAM Roles Anywhere released Credential Helper version 1.0.1. As a part of this release, the tool now has better error handling.
