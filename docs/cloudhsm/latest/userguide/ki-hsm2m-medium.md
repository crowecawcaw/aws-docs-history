# Known issues for AWS CloudHSM hsm2m.medium instances

The following issues impact all AWS CloudHSM hsm2m.medium instances. 

###### Topics

* [Issue: Increased login latency on hsm2m.medium](#ki-hsm2m-medium-1 "#ki-hsm2m-medium-1")
* [Issue: Increased find key latency on hsm2m.medium](#ki-hsm2m-medium-2 "#ki-hsm2m-medium-2")
* [Issue: A CO using trying to set the trusted attribute of a key will fail with Client SDK 5.12.0 and earlier](#ki-hsm2m-medium-3 "#ki-hsm2m-medium-3")
* [Issue: ECDSA verify will fail with Client SDK 5.12.0 and earlier for clusters in FIPS mode](#ki-hsm2m-medium-4 "#ki-hsm2m-medium-4")
* [Issue: Only the PEM-formatted certificates can be registered as mtls trust anchors with CloudHSM CLI](#ki-hsm2m-medium-5 "#ki-hsm2m-medium-5")
* [Issue: Customer applications will stop processing all requests when using mTLS with a passphrase protected client private key.](#ki-hsm2m-medium-6 "#ki-hsm2m-medium-6")
* [Issue: User replicate fails when using the CloudHSM CLI](#ki-hsm2m-medium-7 "#ki-hsm2m-medium-7")
* [Issue: Operations can fail during backup creation](#ki-hsm2m-medium-8 "#ki-hsm2m-medium-8")
* [Issue: Client SDK 5.8 and above do not perform automatic retries
 for HSM throttled operations in some scenarios on hsm2m.medium](#ki-hsm2m-medium-9 "#ki-hsm2m-medium-9")

## Issue: Increased login latency on hsm2m.medium



* **Impact:** The hsm2m.medium adheres to the latest FIPS 140-3 Level 3 requirements. Logging into hsm2m.medium follows enhanced security and compliance requirements, which results in increased latency.
* **Workaround:** If possible, serialize login requests in the same application to avoid extended latency during login. Multiple login requests in parallel will cause increased latency.

## Issue: Increased find key latency on hsm2m.medium



* **Impact:** The hsm2m.medium HSM instance has improved fair share architecture which results in more consistent predictable performance compared to hsm1.medium. With hsm1.medium, customers may observe higher find key performance due to irregular use of HSM resources. However, hsm1.medium find key performance will decrease when the HSM instance is patched or updated with new firmware. This issue affects operations such as `KeyStore.getKey()` in JCE.
* **Workaround:** We are working to improve our HSM firmware. As best practice, cache the results from find key operations. Caching will reduce the total number of find key operations as it is a resource intensive operation in HSM. In addition, implement client-side retries with exponential backoff and jitter to reduce HSM throttling failures.

## Issue: A CO using trying to set the trusted attribute of a key will fail with Client SDK 5.12.0 and earlier


 



* **Impact:** Any CO user attempting to set the trusted attribute of a key will receive an error indicating that `User type should be CO or CU`.
* **Resolution:** Future versions of the Client SDK will resolve this issue. Updates will be announced in our user guide's [Document history](document-history.md "document-history.md").

## Issue: ECDSA verify will fail with Client SDK 5.12.0 and earlier for clusters in FIPS mode


 



* **Impact:** ECDSA verify operation performed for HSMs in FIPS mode will fail.
* **Resolution status:** This issue has been resolved in the [client SDK 5.13.0 release](client-version-previous.md#client-version-5-13-0 "client-version-previous.md#client-version-5-13-0"). You must upgrade to this client version or later to benefit from the fix.

## Issue: Only the PEM-formatted certificates can be registered as mtls trust anchors with CloudHSM CLI


 



* **Impact:** Certificates in DER format cannot be registered as mTLS trust anchors with CloudHSM CLI.
* **Workaround:** You can convert a certificate in DER format to PEM format with openssl command: `openssl x509 -inform DER -outform PEM -in `certificate.der` -out `certificate.pem``

## Issue: Customer applications will stop processing all requests when using mTLS with a passphrase protected [client private key](getting-started-setup-mtls.md#getting-start-setup-mtl-sdk "getting-started-setup-mtls.md#getting-start-setup-mtl-sdk").


 



* **Impact:** All operations performed by the application will be halted and the user will be prompted for the passphrase on standard input multiple times throughout the lifetime of application. Operations will timeout and fail if passphrase is not provided before the operation's timeout duration.
* **Workaround:** Passphrase encrypted private keys are not supported for mTLS. Remove passphrase encryption from client private key

## Issue: User replicate fails when using the CloudHSM CLI


 



* **Impact:** User replication fails on hsm2m.medium instances when using the CloudHSM CLI.
 The `user replicate` command works as expected on hsm1.medium instances.
* **Resolution:**  We're working to resolve this issue.
 For updates, see the [Document history](document-history.md "document-history.md") in the user guide.

## Issue: Operations can fail during backup creation



* **Impact:** Operations like generating random numbers can fail
 on hsm2m.medium instances while AWS CloudHSM creates a backup.
* **Resolution:** To minimize service interruptions, implement these
 best practices:




	+ Create a multi-HSM cluster
	+ Configure your applications to retry cluster operations
For more information about best practices, see [Best practices for AWS CloudHSM](best-practices.md "best-practices.md").

## Issue: Client SDK 5.8 and above do not perform automatic retries
 for HSM throttled operations in some scenarios on hsm2m.medium



* **Impact:** Client SDK 5.8 and above will not retry some HSM
 throttled operations
* **Workaround:** Follow best practices to architect your cluster
 to handle load and implement application level retries. We are currently working on a fix.
 Updates will be announced in our user guide's [Document history](document-history.md "document-history.md").
* **Resolution status:** This issue has been resolved in the AWS CloudHSM Client SDK 5.16.2.
 You must upgrade to this client version or later to benefit from the fix.
