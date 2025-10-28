# Encrypt

A basic function of AWS KMS is to encrypt an object under a KMS key. By design, AWS KMS
provides low latency cryptographic operations on HSMs. Thus there is a limit of 4 KB on the
amount of plaintext that can be encrypted in a direct call to the encrypt function. The
AWS Encryption SDK can be used to encrypt larger messages. AWS KMS, after authenticating the command,
acquires the current active EKT pertaining to the KMS key. It passes the EKT, along with the
plaintext and encryption context, to any available HSM in the Region. These are sent over an
authenticated session between the AWS KMS host and an HSM in the domain.

The HSM runs the following:

1. Decrypts the EKT to obtain the _HBK = Decrypt(DKi,
   EKT)_ .
2. Generates a random nonce _N_.
3. Derives a 256-bit AES-GCM derived encryption key _K_ from
   _HBK_ and _N_.
4. Encrypts the plaintext _ciphertext = Encrypt(K, context,
   plaintext)_.
   The ciphertext value is returned to you, and neither the plaintext data or ciphertext is
   retained anywhere in the AWS infrastructure. Without possession of the
   _ciphertext_ and the encryption context, and the authorization to use the
   KMS key, the underlying plaintext cannot be returned.
