# HSM user permissions table for
 CloudHSM CLI

The following table lists hardware security module (HSM) operations sorted by the type of
 HSM user or session that can perform the operation in AWS CloudHSM.



|  | Admin | Crypto User (CU) | Appliance User (AU) | Unauthenticated Session |
| --- | --- | --- | --- | --- |
| Get basic cluster info¹ |  Yes |  Yes |  Yes |  Yes |
| Change own password |  Yes |  Yes |  Yes | Not applicable |
| Change any user's password |  Yes |  No |  No |  No |
| Add, remove users |  Yes |  No |  No |  No |
| Get sync status² |  Yes |  Yes |  Yes |  No |
| Extract, insert masked objects³ |  Yes |  Yes |  Yes |  No |
| Key management functions⁴ |  No |  Yes |  No |  No |
| Encrypt, decrypt |  No |  Yes |  No |  No |
| Sign, verify |  No |  Yes |  No |  No |
| Generate digests and HMACs |  No |  Yes |  No |  No | <br>• [1] Basic cluster information includes the number of HSMs in the cluster and each HSM's IP address, model, serial number, device ID, firmware ID, etc. <br>• [2] The user can get a set of digests (hashes) that correspond to the keys on the HSM. An application can compare these sets of digests to understand the synchronization status of HSMs in a cluster. <br>• [3] Masked objects are keys that are encrypted before they leave the HSM. They cannot be decrypted outside of the HSM. They are only decrypted after they are inserted into an HSM that is in the same cluster as the HSM from which they were extracted. An application can extract and insert masked objects to synchronize the HSMs in a cluster. <br>• [4] Key management functions include creating, deleting, wrapping, unwrapping, and modifying the attributes of keys.
