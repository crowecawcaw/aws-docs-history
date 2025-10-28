# Bind the

hardware security module
to the Snow
device

Each Snow device can be bound to one
hardware security module (HSM) to secure and encrypt the data on the Snow device.

To complete this procedure, you will need:

- A
  Snowball Edge client
- The IP address to assign to
  the
  HSM.
- The
  path
  to, and file name of the certificate file on the HSM.
- The
  path
  to, and file name of the private key file on the HSM.

###### Topics

- [Enable certificate‐based login](#enable-cert-login "#enable-cert-login")
- [Generate a certificate and private key](#gen-cert-key "#gen-cert-key")
- [Bind a Snow device to the hardware security module](#bind-sw-device "#bind-sw-device")

## Enable certificate‐based login

1. Using a Web browser, connect to the device and log in.
2. Choose **Access Management**, then choose **Users.**
3. For the user account **admin**, choose its action button then choose **Manage**.
4. Choose **CONFIGURE CERTIFICATE LOGIN**. Choose **Allow user to login using certificate**.
5. In the **Certificate Subject Distinguished Name** field, enter a common name. For example, `CN=`myCNName``.

###### Note

The common name used here will be used when generating certificate. Remember the common name. 6. Choose `Update Certificate Login`.

## Generate a certificate and private key

1. Using a Web browser, connect to the device and log in.
2. Choose **CA** then **Local**.
3. Choose **Go to existing local CA**.
4. Choose **Issue Certificate**
   1. Enter the common name for this certificate. Ensure that the common name is the same as used when you [created the common name](#common-name "#common-name").
   2. Choose **RSA** as the algorithm and **4096** as the size.
   3. In the **Name** field, make the same entry as for the **Certificate Subject Distinguished Name**.
   4. Choose **Issue Certificate**.
   5. Choose **Save private key** to download the **key.pem** file.
   6. Choose **Issue Certificate**. The newly‐created certificate appears in the certificates list.

## Bind a Snow device to the hardware security module

Run the `snowballEdge bind-device` command.

```

    snowballEdge bind-device

        --device-id:`unique_id_of_key_management_device` /
        --certificate file://`certificate.pem` /
        --private-key file://`key.pem` /
        --ip-address "`IP address of key management device`"
```

When the command is
successful, it produces the following output:

```

    bind-device with <BindDeviceOutput.DeviceId> successful.

```

###### Example of snowballEdge bind-device Command

```

    snowballEdge bind-device

        --device-id:k570
        --certificate file://path/to/certificate.pem
        --private-key file://path/to/key.pem
        --ip-address "192.158.1.38"

```

**Next:**
[Unlocking the device](unlockdevice.md "unlockdevice.md")
