

# AS2805
<a name="advanced.regional.as2805"></a>

Australia Standard 2805 (AS2805) is a standard for electronic funds transfers used primarily for card-based payment transactions. It is maintained by [Standards Australia](https://www.standards.org.au/). The standard consists of 6 books that covers numerous topics from message format to encryption standards.

Part 6 provides guidance on key management including host-to-host (node-to-node) communication and relevant cryptographic requirements while other aspects are covered in other parts. All cryptography in this standard is currently based on TDES. 

AS2805 has a number of differences compared to other implementations, which are summarized below.

*Key Protection*  
Relies on key variants instead of keyblocks such as in TR-31/X9.143. AWS Payment Cryptography stores all keys as key blocks internally but permits import, export and calculation using AS2805 defined variants. 

*Unidirectional Keys*  
AS2805 mandates the use of unidirectional keys. If both nodes need to generate message authentication codes (MAC), they use two keys. 

*Pin Blocks*  
AS2805 defines a key derivation technique for unique pin encryption keys per transaction. This can be used in lieu of DUKPT. The AS2805 scheme relies on transaction data (trace number and transaction amount) as compared to DUKPT's use of transaction counter. 

*Key Exchange Validation*  
Defines a process to validate KEK before beginning to exchange working keys such as pin keys. In other schemes, KEK are exchanged infrequently and are validated using KCV. 

AS2805 uses the concept of key variants rather than key blocks to ensure keys are only used for the intended (and sole) purpose. The following is how AWS Payment Cryptography maps between variants and keyblocks when importing, exporting or performing other cryptographic functions with keys.


| AS2805 Key Type | AWS Payment Cryptography Key Type | 
| --- | --- | 
| TERMINAL\_MAJOR\_KEY\_VARIANT\_00 | TR31\_K0\_KEY\_ENCRYPTION\_KEY | 
| PIN\_ENCRYPTION\_KEY\_VARIANT\_28 | TR31\_P0\_PIN\_ENCRYPTION\_KEY | 
| MESSAGE\_AUTHENTICATION\_KEY\_VARIANT\_24 | TR31\_M0\_ISO\_16609\_MAC\_KEY | 
| DATA\_ENCRYPTION\_KEY\_VARIANT\_22 | TR31\_D0\_SYMMETRIC\_DATA\_ENCRYPTION\_KEY | 
| VARIANT\_MASK\_82,VARIANT\_MASK\_82C0 | Options available as part of KEK validation process. These key types are ephemeral and are not stored by the service. | 

Given two nodes, node1 and node2, the following examples are from the perspective of node1. AWS Payment Cryptography supports APIs from both sides of the process.

**Topics**
+ [Initial Key(KEK) exchange](as2805.kekexchange.md)
+ [Validation of KEK](as2805.kekvalidation.md)
+ [Creation and transmission of working keys](as2805.workingkeys.create.md)
+ [Exporting working keys](as2805.workingkeys.export.md)
+ [Pin Translation](as2805.pintranslation.md)
+ [Mac Generation and Validation](as2805.mac.md)