# SDK3 compatibility mode for Key Storage Provider (KSP)
 for AWS CloudHSM

Key Storage Provider (KSP) implements different approaches for HSM key interaction:


* Client SDK 5: Provides direct communication with keys stored in the HSM, eliminating the
 need for local reference files
* Client SDK 3: Maintains local files on the Windows server that act as references to keys
 stored in the HSM, using these files to facilitate key operations
For customers migrating from Client SDK 3 to Client SDK 5, enabling SDK3 compatibility mode option
 supports operations using existing key reference files while preserving the underlying HSM key
 storage architecture.


## Enable SDK3 compatibility mode



Windows
###### To enable SDK3 compatibility mode for Key Storage Provider (KSP) for Client SDK 5 in Windows

* You can use the following command to enable SDK3 compatibility mode:



```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --enable-sdk3-compatibility-mode`
```



## Disable SDK3 compatibility mode



Windows
###### To disable SDK3 compatibility mode for Key Storage Provider (KSP) for Client SDK 5 in Windows

* You can use the following command to disable SDK3 compatibility mode:



```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --disable-sdk3-compatibility-mode`
```
