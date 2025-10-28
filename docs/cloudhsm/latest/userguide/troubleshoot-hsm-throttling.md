# HSM throttling

When your workload exceeds your AWS CloudHSM cluster’s hardware security module (HSM) capacity, you will receive error messages stating HSMs are busy or throttled.
When this happens, you may see reduced throughput or an increased rate of rejection requests from HSMs.
Additionally, HSMs may send the following busy errors.

- In PKCS11, busy errors map to `CKR_FUNCTION_FAILED`. This error can happen for multiple reasons, but if HSM throttling causes this error the following log lines will appear in your log:
  - `[cloudhsm_provider::hsm1::hsm_connection::e2e_encryption::error] Failed to prepare E2E response. Error: Received error response code from Server. Response Code: 187`
  - `[cloudhsm_pkcs11::decryption::aes_gcm] Received error from the server. Error: This operation is already in progress. Internal error code: 0x000000BB`

- In JCE, busy errors map to `com.amazonaws.cloudhsm.jce.jni.exception.InternalException: Unexpected error with the Provider: The HSM could not queue the request for processing.`
- Other SDKs' busy errors print out the following message:
  `Received error response code from Server. Response Code: 187`.

- In PKCS11, busy errors map to `CKR_OPERATION_ACTIVE` errors.
- In JCE, busy errors map to `CFM2Exception` with status of `0xBB (187)`.
  Applications can use `getStatus()` function on `CFM2Exception` to check what status is returned by the HSM.
- Other SDKs busy errors will print out the following message:
  `HSM Error: HSM is already busy generating the keys(or random bytes) for another request.`

## Resolution

You can resolve these issues by completing one or more of the following actions:

- Add retry commands for rejected HSM operations in your application layer.
  Before enabling retry commands, ensure your cluster is adequately sized to meet peak loads.

###### Note

For Client SDK 5.8.0 and above, retry commands are turned on by default. For details on each SDK’s retry command configuration,
refer to [Advanced configurations for the Client SDK 5 configure tool](configure-sdk5-advanced-configs.md "configure-sdk5-advanced-configs.md").

- Add more HSMs to your cluster by following the instructions in [Scaling HSMs in an AWS CloudHSM cluster](add-remove-hsm.md "add-remove-hsm.md").

###### Important

We recommend load testing your cluster to determine the peak load you should anticipate, and then add one more HSM to it to ensure high availability.
