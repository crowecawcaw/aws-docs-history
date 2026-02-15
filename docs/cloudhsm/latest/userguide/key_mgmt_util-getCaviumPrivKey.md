# Export an AWS CloudHSM key to fake PEM format

using KMU

Use the **getCaviumPrivKey** command in the AWS CloudHSM key_mgmt_util to
export a private key from a hardware security module (HSM) in fake PEM format. The fake PEM
file, which does not contain the actual private key material but instead references the
private key in the HSM, can then be used to establish SSL/TLS offloading from your web
server to AWS CloudHSM. For more information, see [SSL/TLS Offload
on Linux using Tomcat](third-offload-linux-jsse.md "third-offload-linux-jsse.md") or [SSL/TLS Offload
on Linux using NGINX or Apache](third-offload-linux-openssl.md "third-offload-linux-openssl.md").

Before you run any key_mgmt_util command, you must [start
key_mgmt_util](key_mgmt_util-setup.md#key_mgmt_util-start "key_mgmt_util-setup.md#key_mgmt_util-start") and [login](key_mgmt_util-log-in.md "key_mgmt_util-log-in.md") to the HSM as
a crypto user (CU).

## Syntax

```
getCaviumPrivKey -h

getCaviumPrivKey -k `<private-key-handle>`
                 -out `<fake-PEM-file>`

```

## Examples

This example shows how to use **getCaviumPrivKey** to export a private
key in fake PEM format.

###### Example: Export a fake PEM file

This command creates and exports a fake PEM version of a private key with handle
`15` and saves it to a file called `cavKey.pem`. When the
command succeeds, **exportPrivateKey** returns a success
message.

```
`Command:` `getCaviumPrivKey -k 15 -out cavKey.pem`

`Private Key Handle is written to cavKey.pem in fake PEM format

 getCaviumPrivKey returned: 0x00 : HSM Return: SUCCESS`
```

## Parameters

This command takes the following parameters.

**`-h`**

Displays command line help for the command.

Required: Yes

**`-k`**

Specifies the key handle of the private key to be exported in fake PEM
format.

Required: Yes

**`-out`**

Specifies the name of the file to which the fake PEM key will be
written.

Required: Yes

## Related topics

- [importPrivateKey](key_mgmt_util-importPrivateKey.md "key_mgmt_util-importPrivateKey.md")
- [SSL/TLS Offload
  on Linux using Tomcat](third-offload-linux-jsse.md "third-offload-linux-jsse.md")
- [SSL/TLS Offload
  on Linux using NGINX or Apache](third-offload-linux-openssl.md "third-offload-linux-openssl.md")
