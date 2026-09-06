

# Change AWS CloudHSM client key durability settings
<a name="working-client-sync"></a>

Key synchronization is mostly an automatic process, but you can manage client-side key durability settings. Client-side key durability settings works differently in Client SDK 5 and Client SDK 3. 
+ In Client SDK 5, we introduce the concept of *key availability quorums* which requires you to run clusters with a minimum of two HSMs. You can use client-side key durability settings to opt out of the two HSM requirement. For more information about quorums, see [AWS CloudHSM key concepts](concepts-key-sync.md).
+ In Client SDK 3, you use client-side key durability settings to specify the number of HSMs on which key creation must succeed for the overall operation to be deemed a success. 

## Client SDK 5 client key durability settings
<a name="client-sync-sdk8"></a>

In Client SDK 5, key synchronization is a fully automatic process. With key availability quorum, newly created keys must exist on two HSMs in the cluster before your application can use the key. To use key availability quorum, your cluster must have a minimum of two HSMs.

If your cluster configuration doesn’t meet the key durability requirements, any attempt to create or use a token key will fail with the following error message in the logs:

```
Key {{<key handle>}} does not meet the availability requirements - The key must be available on at least 2 HSMs before being used.
```

You can use client configuration settings to opt out of key availability quorum. You might want to opt out to run a cluster with a single HSM, for example. 

### Client SDK 5 concepts
<a name="client-sync-8concept"></a>

**Key Availability Quorum**  
AWS CloudHSM specifies the number of HSMs in a cluster on which keys must exist before your application can use the key. Requires clusters with a minimum of two HSMs.

### Managing client key durability settings
<a name="setting-file-sdk8"></a>

To manage client key durability settings, you must use the configure tool for Client SDK 5. 

------
#### [ PKCS \#11 library ]

**To disable client key durability for Client SDK 5 on Linux**
+  Use the configure tool to disable client key durability settings. 

  ```
  $ sudo /opt/cloudhsm/bin/configure-pkcs11 --disable-key-availability-check
  ```

**To disable client key durability for Client SDK 5 on Windows**
+  Use the configure tool to disable client key durability settings. 

  ```
  PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" --disable-key-availability-check
  ```

------
#### [ OpenSSL Dynamic Engine ]

**To disable client key durability for Client SDK 5 on Linux**
+  Use the configure tool to disable client key durability settings. 

  ```
  $ sudo /opt/cloudhsm/bin/configure-dyn --disable-key-availability-check
  ```

------
#### [ OpenSSL Dynamic Engine Provider ]

**To disable client key durability for Client SDK 5 on Linux**
+  Use the configure tool to disable client key durability settings. 

  ```
  $ sudo /opt/cloudhsm/bin/configure-openssl-provider --disable-key-availability-check
  ```

------
#### [ Key Storage Provider (KSP) ]

**To disable client key durability for Client SDK 5 on Windows**
+  Use the configure tool to disable client key durability settings. 

  ```
  PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --disable-key-availability-check
  ```

------
#### [ JCE provider ]

**To disable client key durability for Client SDK 5 on Linux**
+  Use the configure tool to disable client key durability settings. 

  ```
  $ sudo /opt/cloudhsm/bin/configure-jce --disable-key-availability-check
  ```

**To disable client key durability for Client SDK 5 on Windows**
+  Use the configure tool to disable client key durability settings. 

  ```
  PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" --disable-key-availability-check
  ```

------
#### [ CloudHSM CLI ]

**To disable client key durability for Client SDK 5 on Linux**
+  Use the configure tool to disable client key durability settings. 

  ```
  $ sudo /opt/cloudhsm/bin/configure-cli --disable-key-availability-check
  ```

**To disable client key durability for Client SDK 5 on Windows**
+  Use the configure tool to disable client key durability settings. 

  ```
  PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-cli.exe" --disable-key-availability-check
  ```

------

## Client SDK 3 client key durability settings
<a name="client-sync-sdk3"></a>

In Client SDK 3, key synchronization is mostly an automatic process, but you can use the client key durability settings to make keys more durable. You specify the number of HSMs on which key creation must succeed for the overall operation to be deemed a success. Client-side synchronization always makes a best-effort attempt to clone keys to every HSM in the cluster no matter what setting you choose. Your setting enforces key creation on the number of HSMs you specify. If you specify a value and the system cannot replicate the key to that number of HSMs, then the system automatically cleans up any unwanted key material and you can try again.

**Important**  
If you don’t set client key durability settings (or if you use the default value of 1), your keys are vulnerable to loss. If your current HSM should fail before the server-side service has cloned that key to another HSM, you lose the key material. 

To maximize key durability, consider specifying at least two HSMs for client-side synchronization. Remember that no matter how many HSMs you specify, the workload on your cluster remains the same. Client-side synchronization always makes a best-effort attempt to clone keys to every HSM in the cluster. 

**Recommendations**
+ **Minimum**: Two HSMs per cluster
+ **Maximum**: One fewer than the total number of HSMs in your cluster

If client-side synchronization fails, the client service cleans up any unwanted keys that may have been created and are now unwanted. This clean up is a best-effort response that may not always work. If cleanup fails, you may have to delete unwanted key material. For more information, see [Key Synchronization Failures](ts-client-sync-fail.md).

### Setting up the configuration file for client key durability
<a name="setting-file"></a>

To specify client key durability settings, you must edit `cloudhsm_client.cfg`. 

**To edit the client configuration file**

1. Open `cloudhsm_client.cfg`.

   **Linux**:

   ```
   /opt/cloudhsm/etc/cloudhsm_client.cfg
   ```

   **Windows**:

   ```
   C:\ProgramData\Amazon\CloudHSM\data\cloudhsm_client.cfg
   ```

1. In the `client` node of the file, add `create_object_minimum_nodes` and specify a value for the minimum number of HSMs on which AWS CloudHSM must successfully create keys for key creation operations to succeed.

   ```
   "create_object_minimum_nodes" : 2
   ```
**Note**  
The key\_mgmt\_util (KMU) command-line tool has an additional setting for client key durability. For more information, see [KMU and client-side synchronization](#kmu-sync)

#### Configuration reference
<a name="client-side-ref"></a>

These are the client-side synchronization properties, shown in an excerpt of the `cloudhsm_client.cfg`:

```
{
    "client": {
        "create_object_minimum_nodes" : 2,
        ...
    },
    
    ...
}
```

**create\_object\_minimum\_nodes**  
Specifies the minimum number of HSMs required to deem key generation, key import, or key unwrap operations a success. If set, the default is 1. This means that for every key create operation, the client-side service attempts to create keys on every HSM in the cluster, but to return a success, only needs to create a *single key* on one HSM in the cluster. 

### KMU and client-side synchronization
<a name="kmu-sync"></a>

If you create keys with the key\_mgmt\_util (KMU) command-line tool, you use an optional command line parameter (`-min_srv`) to *limit* the number of HSMs on which to clone keys. If you specify the command-line parameter *and* a value in the configuration file, AWS CloudHSM honors the LARGER of the two values.

 For more information, see the following topics:
+ [genDSAKeyPair](key_mgmt_util-genDSAKeyPair.md)
+ [genECCKeyPair](key_mgmt_util-genECCKeyPair.md)
+ [genRSAKeyPair](key_mgmt_util-genRSAKeyPair.md)
+ [genSymKey](key_mgmt_util-genSymKey.md)
+ [importPrivateKey](key_mgmt_util-importPrivateKey.md)
+ [importPubKey](key_mgmt_util-importPubKey.md)
+ [imSymKey](key_mgmt_util-imSymKey.md)
+ [insertMaskedObject](key_mgmt_util-insertMaskedObject.md)
+ [unWrapKey](key_mgmt_util-unwrapKey.md)