# Retry commands for OpenSSL for AWS CloudHSM

AWS CloudHSM Client SDK 5.8.0 and later have a built-in automatic retry strategy which will retry HSM-throttled operations from the client side.
When an HSM throttles operations because it is too busy performing previous operations and cannot take more requests, client SDKs will attempt to retry throttled operations up to 3 times while exponentially backing off.
This automatic retry strategy can be set to one of two modes: **off** and **standard**.

- **off**: The Client SDK will not perform any retry strategy for any throttled operations by the HSM.
- **standard**: This is the default mode for Client SDK 5.8.0 and later. In this mode, client SDKs will automatically retry throttled operations by exponentially backing off.
  For more information, see [HSM throttling](troubleshoot-hsm-throttling.md "troubleshoot-hsm-throttling.md").

## Set retry commands to off mode

You can use the following command to set retry commands to **off** mode:

```
`$` `sudo /opt/cloudhsm/bin/configure-dyn --default-retry-mode off`
```
