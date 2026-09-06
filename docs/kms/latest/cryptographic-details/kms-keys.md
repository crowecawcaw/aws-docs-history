

# Working with AWS KMS keys
<a name="kms-keys"></a>

An AWS KMS key refers to a logical key that might refer to one or more hardware security module (HSM) backing keys (HBKs). This topic explains how to create a KMS key, import key material, and how to enable, disable, rotate, and delete KMS keys.

**Note**  
AWS KMS is replacing the term *customer master key (CMK)* with *AWS KMS key* and *KMS key*. The concept has not changed. To prevent breaking changes, AWS KMS is keeping some variations of this term.

This chapter discusses the lifecycle of a KMS key from creation to deletion, as shown in the following image.

![KMS key lifecycle.](http://docs.aws.amazon.com/kms/latest/cryptographic-details/images/keystate.png)


**Topics**
+ [Calling CreateKey](create-key.md)
+ [Importing key material](importing-key-material.md)
+ [Enabling and disabling keys](enable-and-disable-key.md)
+ [Deleting keys](key-deletion.md)
+ [Rotating key material](rotate-customer-master-key.md)