# Retry commands for PKCS #11 library for AWS CloudHSM

AWS CloudHSM Client SDK 5.8.0 and later have a built-in automatic retry strategy which will retry HSM-throttled operations from the client side.
When an HSM throttles operations because it is too busy performing previous operations and cannot take more requests, client SDKs will attempt to retry throttled operations up to 3 times while exponentially backing off.
This automatic retry strategy can be set to one of two modes: **off** and **standard**.

- **off**: The Client SDK will not perform any retry strategy for any throttled operations by the HSM.
- **standard**: This is the default mode for Client SDK 5.8.0 and later. In this mode, client SDKs will automatically retry throttled operations by exponentially backing off.
  For more information, see [HSM throttling](troubleshoot-hsm-throttling.md "troubleshoot-hsm-throttling.md").

## Set retry commands to off mode

Linux

###### To set retry commands to **off** for Client SDK 5 on Linux

- You can use the following command to set retry configuration to **off** mode:

```
`$` `sudo /opt/cloudhsm/bin/configure-pkcs11 --default-retry-mode off`
```

Windows

###### To set retry commands to **off** for Client SDK 5 on Windows

- You can use the following command to set retry configuration to **off** mode:

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" --default-retry-mode off`
```
