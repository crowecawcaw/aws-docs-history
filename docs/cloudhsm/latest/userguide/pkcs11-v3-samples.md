# Code samples for the PKCS #11 library for AWS CloudHSM
 Client SDK 3

The code samples on GitHub show you how to accomplish basic tasks using the PKCS #11 library for
 AWS CloudHSM. 


## Sample code prerequisites


Before running the samples, perform the following steps to set up your
 environment:



* Install and configure the [PKCS #11 library](install-pkcs11-v3.md "install-pkcs11-v3.md") for Client SDK 3.
* Set up a [cryptographic user (CU)](manage-hsm-users.md "manage-hsm-users.md"). Your 
 application uses this HSM account to run the code samples on the HSM.

## Code samples


Code Samples for the AWS CloudHSM Software Library for PKCS#11 are available on [GitHub](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples"). This
 repository includes examples on how to do common operations using PKCS#11 including
 encryption, decryption, signing and verifying.



* [Generate keys (AES, RSA, EC)](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/generate "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/generate")
* [List key attributes](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/attributes/ "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/attributes/")
* [Encrypt and decrypt data with AES GCM](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/encrypt/aes_gcm.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/encrypt/aes_gcm.c")
* [Encrypt and decrypt data with AES\_CTR](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/encrypt/aes_ctr.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/encrypt/aes_ctr.c")
* [Encrypt and decrypt data with 3DES](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/encrypt/des_ecb.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/encrypt/des_ecb.c")
* [Sign and verify data with RSA](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/sign/rsa_sign.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/sign/rsa_sign.c")
* [Derive keys using HMAC KDF](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/derivation/hmac_kdf.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/derivation/hmac_kdf.c")
* [Wrap and unwrap keys with AES using PKCS #5 padding](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/wrapping/aes_wrapping.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/wrapping/aes_wrapping.c")
* [Wrap and unwrap keys with AES using no padding](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/wrapping/aes_no_padding_wrapping.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/wrapping/aes_no_padding_wrapping.c")
* [Wrap and unwrap keys with AES using zero padding](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/wrapping/aes_zero_padding_wrapping.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/wrapping/aes_zero_padding_wrapping.c")
* [Wrap and unwrap keys with AES-GCM](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/wrapping/aes_gcm_wrapping.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/wrapping/aes_gcm_wrapping.c")
* [Wrap and unwrap keys with RSA](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/wrapping/rsa_wrapping.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/wrapping/rsa_wrapping.c")
