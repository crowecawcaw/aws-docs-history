# Migrate your Key Storage Provider (KSP) from AWS CloudHSM Client SDK 3 to

Client SDK 5

This topic explains how to migrate your [Key Storage Provider (KSP)](ksp-library.md "ksp-library.md") from
AWS CloudHSM Client SDK 3 to Client SDK 5. The latest version of AWS CloudHSM Client SDK is 5.16. For information about migration benefits, see [Benefits of AWS CloudHSM Client SDK 5](client-sdk-5-benefits.md "client-sdk-5-benefits.md").

In AWS CloudHSM, you use the AWS CloudHSM Client Software Development Kit (SDK) to perform cryptographic
operations. Client SDK 5 is the primary SDK that receives new features and platform support
updates.

For migration instructions for all providers, see [Migrating from AWS CloudHSM Client SDK 3 to
Client SDK 5](client-sdk-migration.md "client-sdk-migration.md").

## Migrate to Client SDK 5

1. Stop the Client Daemon for Client SDK 3.

```
`PS C:\>` `Stop-Service "AWS CloudHSM Client"`
```

2. Install the Client SDK 5 Key Storage Provider (KSP) on your Windows Server instance. For instructions,
   see [Install the Key storage provider (KSP) for AWS CloudHSM Client SDK 5](ksp-library-install.md "ksp-library-install.md").
3. Configure your Client SDK 5 Key Storage Provider (KSP) using the new configuration file format and
   command-line bootstrapping tool. For instructions, see [Bootstrap the Client SDK](cluster-connect.md#connect-how-to "cluster-connect.md#connect-how-to").
4. Key Storage Provider (KSP) for AWS CloudHSM Client SDK 5 includes SDK3 compatibility mode to support key
   reference files generated in SDK3. For more information, see [SDK3 compatibility mode for Key Storage Provider (KSP)
   for AWS CloudHSM](ksp-library-configs-sdk3-compatibility-mode.md "ksp-library-configs-sdk3-compatibility-mode.md").

###### Note

You must enable SDK3 compatibility mode when using Client SDK 3 generated key
reference files with Client SDK 5.

## Migrate to new Windows Server

instances

1. Complete all steps in [Migrate to
   Client SDK 5](#ksp-migrate-steps "#ksp-migrate-steps") on your new Windows Server instances.
2. ###### Check for existing key reference files

On your original Windows Server instance, check for key reference files in
`C:\Users\Default\AppData\Roaming\Microsoft\Crypto\CaviumKSP\GlobalPartition`.

    * If key reference files exist, copy all contents under
     `C:\Users\Default\AppData\Roaming\Microsoft\Crypto\CaviumKSP`
     including `GlobalPartition` to the same directory path on
     your new Windows Server instance. Create the directory if it doesn't
     exist.
    * If key reference files don't exist, use `cloudhsm-cli key
     generate-file --encoding ksp-key-reference` on your new
     Windows Server instance to create them. For instructions, see [Generating KSP key references (Windows)](cloudhsm_cli-key-generate-file.md#key-generate-ksp-key-reference "cloudhsm_cli-key-generate-file.md#key-generate-ksp-key-reference").

3. ###### Verify root certificate

Check your root certificate in the trusted root certification
authorities:

```
`PS C:\Users\Administrator\Desktop> certutil -store Root

Root "Trusted Root Certification Authorities"
================ Certificate 0 ================
Serial Number: `certificate-serial-number`
Issuer: CN=MYRootCA
 NotBefore: 2/5/2020 1:38 PM
 NotAfter: 2/5/2021 1:48 PM
 Issuer: CN=MYRootCA
Signature matches Public Key
Root Certificate: Subject matches Issuer
Cert Hash(sha1): `cert-hash`
No key provider information
Cannot find the certificate and private key for decryption.
CertUtil: -store command completed successfully.`
```

###### Note

Note the certificate serial number for use in next step. 4. ###### Export root certificate

Export the root certificate to a file:

```
certutil -store Root `certificate-serial-number` `root-certificate-name`.cer
```

5. ###### Verify HSM-backend certificate

Check your HSM-backend certificate in the Personal certificate
store:

```
`PS C:\Users\Administrator\Desktop> certutil -store My

my "Personal"
================ Certificate 0 ================
Serial Number: `certificate-serial-number`
Issuer: CN=MYRootCA
 NotBefore: 2/5/2020 1:38 PM
 NotAfter: 2/5/2021 1:48 PM
Subject: CN=www.mydomain.com, OU=Certificate Management, O=Information Technology, L=Houston, S=Texas, C=US
Non-root Certificate
Cert Hash(sha1): `cert-hash`
 Key Container = `key-container-name`
 Provider = Cavium Key Storage Provider
Private key is NOT exportable
Encryption test passed
CertUtil: -store command completed successfully.`
```

###### Note

Note the certificate serial number for use in next step. 6. ###### Export HSM-backend certificate

Export the HSM-backend certificate to a file:

```
certutil -store My `certificate-serial-number` `signed-certificate-name`.cer
```

7. ###### Import root certificate

On your new Windows instance:

    1. Copy the root CA file to your new Windows instance
    2. Import the certificate:



    ```
    certutil -addstore Root `root-certificate-name`.cer
    ```

8. ###### Verify root certificate installation

Confirm the root certificate is properly installed:

```
`PS C:\Users\Administrator\Desktop> certutil -store Root

Root "Trusted Root Certification Authorities"
================ Certificate 0 ================
Serial Number: `certificate-serial-number`
Issuer: CN=MYRootCA
 NotBefore: 2/5/2020 1:38 PM
 NotAfter: 2/5/2021 1:48 PM
 Issuer: CN=MYRootCA
Signature matches Public Key
Root Certificate: Subject matches Issuer
Cert Hash(sha1): `cert-hash`
No key provider information
Cannot find the certificate and private key for decryption.
CertUtil: -store command completed successfully.`
```

9. ###### Import HSM-backend certificate

On your new Windows instance:

    1. Copy the HSM-backend certificate to your new Windows instance
    2. Import the certificate:



    ```
    certutil -addstore My `signed-certificate-name`.cer
    ```

10. ###### Verify HSM-backend certificate installation

Confirm the HSM-backend certificate is properly installed:

```
`PS C:\Users\Administrator\Desktop> certutil -store My

my "Personal"
================ Certificate 0 ================
Serial Number: `certificate-serial-number`
Issuer: CN=MYRootCA
 NotBefore: 2/5/2020 1:38 PM
 NotAfter: 2/5/2021 1:48 PM
Subject: CN=www.mydomain.com, OU=Certificate Management, O=Information Technology, L=Houston, S=Texas, C=US
Non-root Certificate
Cert Hash(sha1): `cert-hash`
No key provider information
Cannot find the certificate and private key for decryption.
CertUtil: -store command completed successfully.`
```

###### Note

Note the certificate serial number for use in subsequent steps. 11. ###### Create a key reference file (optional)

Complete this step only if you need to create new key reference file.
Otherwise, proceed to the next step.

###### Note

This feature is only in SDK version 5.16.0 and later.

    1. Install [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html "https://slproweb.com/products/Win32OpenSSL.html") and extract the modulus:



    ```
    openssl x509 -in `signed-certificate-name`.cer -modulus -noout
    ```

    ###### Note

    The OpenSSL command outputs the modulus in the format:
     `Modulus=`modulus-value``.
     Note the `modulus-value` for use in the
     next command.
    2. Create key reference file with CloudHSM CLI, see [Generating KSP key references (Windows)](cloudhsm_cli-key-generate-file.md#key-generate-ksp-key-reference "cloudhsm_cli-key-generate-file.md#key-generate-ksp-key-reference"):



    ```
    & "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" key generate-file --encoding ksp-key-reference --filter attr.class=private-key attr.modulus=0x`modulus-value`
    ```

    ###### Note

    The `modulus-value` in CloudHSM CLI command
     arguments must be prefixed with `0x` to indicate
     hexadecimal format.

    Key reference files are created in
     `C:\Users\Default\AppData\Roaming\Microsoft\Crypto\CaviumKSP\GlobalPartition`.

12. ###### Create repair configuration

Create a file named `repair.txt` with the following
content:

```
[Properties]
11 = "" ; Add friendly name property
2 = "{text}" ; Add Key Provider Information property
_continue_="Container=`key-container-name`&"
_continue_="Provider=Cavium Key Storage Provider&"
_continue_="Flags=0&"
_continue_="KeySpec=2"
```

###### Note

Replace `key-container-name` with the key
reference filename from
`C:\Users\Default\AppData\Roaming\Microsoft\Crypto\CaviumKSP\GlobalPartition`. 13. ###### Repair certificate store

Run the repair command:

```
certutil -repairstore My `certificate-serial-number` repair.txt
```

###### Note

The certificate serial number is obtained from the previous steps when
verifying HSM-backend certificate installation. 14. ###### Verify certificate association

Confirm the certificate is properly associated:

```
`PS C:\Users\Administrator\Desktop> certutil -store My

my "Personal"
================ Certificate 0 ================
Serial Number: `certificate-serial-number`
Issuer: CN=MYRootCA
 NotBefore: 2/5/2020 1:38 PM
 NotAfter: 2/5/2021 1:48 PM
Subject: CN=www.mydomain.com, OU=Certificate Management, O=Information Technology, L=Houston, S=Texas, C=US
Non-root Certificate
Cert Hash(sha1): `cert-hash`
 Key Container = `key-container-name`
 Provider = Cavium Key Storage Provider
Private key is NOT exportable
ERROR: Could not verify certificate public key against private key
CertUtil: -store command completed successfully.`
```

Verify the output shows:

    * The correct key container name
    * The Cavium Key Storage Provider
    * The `ERROR: Could not verify certificate public key against
     private key` is a known issue, see [Issue: Verification of a certificate store fails](ki-ksp-sdk.md#ki-ksp-1 "ki-ksp-sdk.md#ki-ksp-1")

15. ###### Test your application

Before completing the migration:

    1. Test your application in your development environment
    2. Update your code to resolve any breaking changes
    3. For application-specific guidance, see [Integrating third-party applications with
     AWS CloudHSM](third-party-applications.md "third-party-applications.md")

## Verify the migration

After completing the migration steps, verify that:

- Your certificates are properly installed in the correct certificate
  stores
- Key reference files are present in the correct location
- Your application can perform cryptographic operations using the migrated
  certificates

## Troubleshooting

If you encounter issues during migration, verify:

- All certificates are properly exported from the source system
- Certificate serial numbers match between systems
- Key container names in the repair.txt file match your key reference
  files
- SDK3 compatibility mode is enabled if using SDK3-generated key reference
  files

## Related topics

- [Best practices for AWS CloudHSM](best-practices.md "best-practices.md")
