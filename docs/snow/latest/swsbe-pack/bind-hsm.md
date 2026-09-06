

# Bind the hardware security module to the Snow device
<a name="bind-hsm"></a>

Each Snow device can be bound to one hardware security module (HSM) to secure and encrypt the data on the Snow device.

To complete this procedure, you will need:
+ A Snowball Edge client
+ The IP address to assign to the HSM.
+ The path to, and file name of the certificate file on the HSM.
+ The path to, and file name of the private key file on the HSM.

**Topics**
+ [Enable certificate‐based login](#enable-cert-login)
+ [Generate a certificate and private key](#gen-cert-key)
+ [Bind a Snow device to the hardware security module](#bind-sw-device)

## Enable certificate‐based login
<a name="enable-cert-login"></a>

1. Using a Web browser, connect to the device and log in.

1. Choose **Access Management**, then choose **Users.**

1. For the user account **admin**, choose its action button then choose **Manage**.

1. Choose **CONFIGURE CERTIFICATE LOGIN**. Choose **Allow user to login using certificate**.

1. <a name="common-name"></a>In the **Certificate Subject Distinguished Name** field, enter a common name. For example, **CN={{myCNName}}**.
**Note**  
The common name used here will be used when generating certificate. Remember the common name.

1. Choose **Update Certificate Login**.

## Generate a certificate and private key
<a name="gen-cert-key"></a>

1. Using a Web browser, connect to the device and log in.

1. Choose **CA** then **Local**.

1. Choose **Go to existing local CA**.

1. Choose **Issue Certificate**

   1. Enter the common name for this certificate. Ensure that the common name is the same as used when you [created the common name](#common-name).

   1. Choose **RSA** as the algorithm and **4096** as the size.

   1. In the **Name** field, make the same entry as for the **Certificate Subject Distinguished Name**.

   1. Choose **Issue Certificate**.

   1. Choose **Save private key** to download the **key.pem** file.

   1. Choose **Issue Certificate**. The newly‐created certificate appears in the certificates list.

## Bind a Snow device to the hardware security module
<a name="bind-sw-device"></a>

Run the `snowballEdge bind-device` command.

```
    snowballEdge bind-device 

        --device-id:{{unique_id_of_key_management_device}} /
        --certificate file://{{certificate.pem}} /
        --private-key file://{{key.pem}} /
        --ip-address "{{IP address of key management device}}"
```

When the command is successful, it produces the following output:

```
    bind-device with <BindDeviceOutput.DeviceId> successful.
```

**Example of snowballEdge bind-device Command**  

```
    snowballEdge bind-device 
        
        --device-id:k570
        --certificate file://path/to/certificate.pem
        --private-key file://path/to/key.pem
        --ip-address "192.158.1.38"
```

**Next:** [Unlocking the device](unlockdevice.md) 