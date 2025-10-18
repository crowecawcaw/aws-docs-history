# AWS CloudHSM application integration best practices

Follow the best practices in this section to optimize how your application integrates with your AWS CloudHSM cluster.


## Bootstrap your Client SDK


Before your client SDK can connect to your cluster, it must be bootstrapped. When bootstrapping IP addresses to your cluster, we recommend using the `--cluster-id` parameter when possible. 
 This method populates your config with all HSM IP addresses in your cluster without needing to keep track of each individual address. 
 Doing this adds extra resilience to your application initialization in the event an HSM is undergoing maintenance or during an Availability Zone outage. For more details, see
 [Bootstrap the Client SDK](cluster-connect.md#connect-how-to "cluster-connect.md#connect-how-to").


## Authenticate to perform operations


In AWS CloudHSM, you must authenticate to your cluster before you are able to perform most operations such as cryptographic operations.


**Authenticate with CloudHSM CLI**: You can authenticate with CloudHSM CLI using either its 
 [single command mode](cloudhsm_cli-modes.md#cloudhsm_cli-mode-single-command "cloudhsm_cli-modes.md#cloudhsm_cli-mode-single-command") or [interactive mode](cloudhsm_cli-modes.md#cloudhsm_cli-mode-interactive "cloudhsm_cli-modes.md#cloudhsm_cli-mode-interactive").
 Use the [Log in to an HSM using CloudHSM CLI](cloudhsm_cli-login.md "cloudhsm_cli-login.md") command to authenticate in interactive mode. To authenticate in single command mode, you must set the environmental variables 
 `CLOUDHSM_ROLE` and `CLOUDHSM_PIN`. For details on doing this, refer to [Single Command mode](cloudhsm_cli-modes.md#cloudhsm_cli-mode-single-command "cloudhsm_cli-modes.md#cloudhsm_cli-mode-single-command"). 
 AWS CloudHSM recommends securely storing your HSM credentials when not being used by your application.


**Authenticate with PKCS #11**: In PKCS #11, you login using the C\_Login API after opening a session using C\_OpenSession. 
 You only need to perform one C\_Login per slot (cluster). After you have successfully logged in, you can open additional sessions using C\_OpenSession without the need to perform additional login operations.
 For examples on authenticating to PKCS #11, see [Code samples for the PKCS #11 library for AWS CloudHSM
 Client SDK 5](pkcs11-samples.md "pkcs11-samples.md").


**Authenticate with JCE**: The AWS CloudHSM JCE Provider supports both implicit and explicit login. 
 The method that works for you depends on your use case. When possible, we recommend using Implicit Login because the SDK will automatically handle authentication if 
 your application becomes disconnected from your cluster and needs to be re-authenticated. Using implicit login also allows you to provide credentials to your application 
 when using an integration that doesn’t allow you to have control over your application code. For more about login methods, see [Step 2: Provide credentials to the
 JCE provider](java-library-install_5.md#java-library-credentials_5 "java-library-install_5.md#java-library-credentials_5").


**Authenticate with OpenSSL**: With the OpenSSL Dynamic Engine, you provide credentials through environment variables. 
 AWS CloudHSM recommends securely storing your HSM credentials when not being used by your application. If possible, you should configure your environment 
 to systematically retrieve and set these environment variables without manual entry. For details on authenticating with OpenSSL, see [Install the OpenSSL Dynamic Engine for AWS CloudHSM
 Client SDK 5](openssl5-install.md "openssl5-install.md").


**Authenticate with KSP**: You can authenticate with Key Storage Provider (KSP) using either Windows credential manager or environment variables, see [Install the Key storage provider (KSP) for AWS CloudHSM Client SDK 5](ksp-library-install.md "ksp-library-install.md").


## Effectively manage keys in your application


**Use key attributes to control what keys can do**: When generating a key, use key attributes to define a set of permissions that will allow or deny specific types of 
 operations for that key. We recommend that keys be generated with the least amount of attributes needed to complete their task. For example, an AES key used for encryption should not also be allowed to wrap keys 
 out of the HSM. For more information, see our attributes pages for the following Client SDKs:



* [PKCS #11 key attributes](pkcs11-attributes.md "pkcs11-attributes.md")
* [JCE key attributes](java-lib-attributes_5.md "java-lib-attributes_5.md")

**When possible, cache key objects to minimize latency**: Key find operations will query every HSM in your cluster. This operation is expensive and does not scale with HSM count in your cluster.



* With PKCS #11, you find keys using the `C_FindObjects` API.
* With JCE, you find keys using the KeyStore.

For optimal performance, AWS recommends that you utilize key find commands (like [Search for AWS CloudHSM keys by attributes using
 KMU](key_mgmt_util-findKey.md "key_mgmt_util-findKey.md") and [List keys for a user with CloudHSM CLI](cloudhsm_cli-key-list.md "cloudhsm_cli-key-list.md")) only once during your application start-up and cache the key object returned in application memory. 
 If you require this key object later on, you should retrieve the object from your cache instead of querying for this object for each operation which will add significant performance overhead.


## Use multi-threading


AWS CloudHSM supports multi-threaded applications, but there are certain things to keep in mind with multi-threaded applications.


**With PKCS #11**, you should initialize the PKCS #11 library (calling `C_Initialize`) only once. 
 Each thread should be assigned its own session (`C_OpenSession`). Using the same session in multiple threads is not recommended.


**With JCE**, the AWS CloudHSM provider should be initialized only once. Do not share instances of SPI objects across threads. 
 For example, Cipher, Signature, Digest, Mac, KeyFactory or KeyGenerator objects should only be utilized in the context of their own thread.


## Handle throttling errors


You may experience HSM throttling errors under the following circumstances:



* Your cluster is not properly scaled to manage peak traffic.
* Your cluster is not sized with a +1 redundancy during maintenance events.
* Availability Zone outages result in a reduced number of available HSMs in your cluster.

See [HSM throttling](troubleshoot-hsm-throttling.md "troubleshoot-hsm-throttling.md") for information on how to best handle this scenario.


To ensure your cluster is adequately sized and will not be throttled, AWS recommends you load test in your environment with your expected peak traffic.


## Integrate retries on cluster operations


AWS may replace your HSM for operational or maintenance reasons. 
 In order to make your application resilient to such situations, AWS recommends that you implement client-side retry logic on all operations that are routed to your cluster. 
 Subsequent retries on failed operations due to replacements are expected to succeed.


## Implement disaster recovery strategies


In response to an event, it may be necessary to shift your traffic away from an entire cluster or region. The following sections describe multiple strategies for doing this.


**Use VPC peering to access your cluster from another account or region**: You can utilize VPC peering to access your AWS CloudHSM cluster from another account or region. 
 For information on how to set this up, see [What is VPC peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html "https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html") in the *VPC Peering Guide*.
 Once you have established your peering connections and configured your security groups appropriately, you can communicate with HSM IP addresses in the same way as you normally would.


**Connect to multiple clusters from the same application**: The JCE provider, PKCS #11 library, and CloudHSM CLI in Client SDK 5 support connecting to multiple clusters from the same application. 
 For example, you can have two active clusters, each in different regions, and your application can connect to both at once and load balance between the two as part of normal operations. 
 If your application is not using Client SDK 5 (the latest SDK), then you cannot connect to multiple clusters from the same application. Alternatively, you can keep another cluster up and running and, 
 in the event there is a regional outage, shift your traffic to the other cluster to minimize downtime. See the respective pages for details:



* [Multiple slot configuration with PKCS #11 library for
 AWS CloudHSM](pkcs11-library-configs-multi-slot.md "pkcs11-library-configs-multi-slot.md")
* [Connecting to multiple AWS CloudHSM clusters with the JCE
 provider](java-lib-configs-multi.md "java-lib-configs-multi.md")
* [Connecting to multiple clusters with CloudHSM CLI](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**Restore a cluster from a backup**: You can create a new Cluster from a backup of an existing Cluster. For more information, see [Cluster backups in AWS CloudHSM](manage-backups.md "manage-backups.md").
