# Validate key file using AWS CloudHSM

KMU

Use the **IsValidKeyHandlefile** command in the AWS CloudHSM key_mgmt_util to find out
whether a key file contains a real private key or a fake RSA PEM key. A fake PEM file does
not contain the actual private key material but instead references the private key in the
HSM. Such a file can be used to establish SSL/TLS offloading from your web server to AWS CloudHSM.
For more information, see [SSL/TLS Offload
on Linux using Tomcat](third-offload-linux-jsse.md "third-offload-linux-jsse.md") or [SSL/TLS Offload
on Linux using NGINX or Apache](third-offload-linux-openssl.md "third-offload-linux-openssl.md").

###### Note

**IsValidKeyHandlefile** only works for RSA keys.

Before you run any key_mgmt_util command, you must [start
key_mgmt_util](key_mgmt_util-setup.md#key_mgmt_util-start "key_mgmt_util-setup.md#key_mgmt_util-start") and [log in](key_mgmt_util-log-in.md "key_mgmt_util-log-in.md") to the HSM
as a crypto user (CU).

## Syntax

```
IsValidKeyHandlefile -h

IsValidKeyHandlefile -f `<rsa-private-key-file>`

```

## Examples

These examples show how to use **IsValidKeyHandlefile** to determine
whether a given key file contains the real key material or fake PEM key material.

###### Example : Validate a real private key

This command confirms that the file called `privateKey.pem` contains
real key material.

```
`Command:` `IsValidKeyHandlefile -f privateKey.pem`

`Input key file has real private key`
```

###### Example : Invalidate a fake PEM key

This command confirms that the file called `caviumKey.pem` contains
fake PEM key material made from key handle `15`.

```
`Command:` `IsValidKeyHandlefile -f caviumKey.pem`

`Input file has invalid key handle: 15`
```

## Parameters

This command takes the following parameters.

**`-h`**

Displays command line help for the command.

Required: Yes

**`-f`**

Specifies the RSA private key file to be checked for valid key
material.

Required: Yes

## Related topics

- [getCaviumPrivKey](key_mgmt_util-getCaviumPrivKey.md "key_mgmt_util-getCaviumPrivKey.md")
- [SSL/TLS Offload
  on Linux using Tomcat](third-offload-linux-jsse.md "third-offload-linux-jsse.md")
- [SSL/TLS Offload
  on Linux using NGINX or Apache](third-offload-linux-openssl.md "third-offload-linux-openssl.md")
