

# Key management with the AWS CloudHSM KMU
<a name="manage-keys-kmu-cmu"></a>

If using the [latest SDK version series](use-hsm.md), use [CloudHSM CLI](cloudhsm_cli.md) to manage the keys in your AWS CloudHSM cluster.

If using the [previous SDK version series](choose-client-sdk.md), you can manage keys on the hardware security modules (HSM) in your AWS CloudHSM cluster using the key\_mgmt\_util (KMU) command line tool. Before you can manage keys, you must start the AWS CloudHSM client, start key\_mgmt\_util, and log in to the HSMs. For more information, see [Getting Started with key\_mgmt\_util](key_mgmt_util-getting-started.md).
+ [Using trusted keys](cloudhsm_using_trusted_keys_control_key_wrap.md) describes how to use PKCS \#11 library attributes and CMU to create trusted keys to secure data.
+ [Generating keys](generate-keys.md) has instructions on generating keys, including symmetric keys, RSA keys, and EC keys.
+ [Importing keys](import-keys.md) provides details on how key owners import keys.
+ [Exporting keys](export-keys.md) provides details on how key owners export keys.
+ [Deleting keys](delete-keys.md) provides details on how key owners delete keys.
+ [Sharing and unsharing keys](share-keys.md) details how key owners share and unshare keys.