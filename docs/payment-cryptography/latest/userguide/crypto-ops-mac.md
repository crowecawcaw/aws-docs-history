

# Generate and verify MAC
<a name="crypto-ops-mac"></a>

Message Authentication Codes (MAC) are typically used to authenticate the integrity of a message (whether it's been modified). Cryptographic hashes such as HMAC (Hash-Based Message Authentication Code), CBC-MAC and CMAC (Cipher-based Message Authentication Code) provide additional assurance of the sender of the MAC by utilizing cryptography. HMAC is based on hash functions while CMAC is based on block ciphers. The service also supports ISO9797 Algorithms 1 and 3 which are types of CBC-MACs. 

All MAC algorithms of this service combine a cryptographic hash function and a shared secret key. They take a message and a secret key, such as the key material in a key, and return a unique tag or mac. If even one character of the message changes, or if the secret key changes, the resulting tag is entirely different. By requiring a secret key, cryptographic MACs also provides authenticity; it is impossible to generate an identical mac without the secret key. Cryptographic MACs are sometimes called symmetric signatures, because they work like digital signatures, but use a single key for both signing and verification. 

AWS Payment Cryptography supports several types of MACs:

**ISO9797 ALGORITHM 1**  
Denoted by `KeyUsage` of ISO9797\_ALGORITHM1. If the field isn't a multiple of block size (8 bytes/16 hex characters for TDES, 16 bytes/32 characters for AES, AWS Payment Cryptography automatically applies ISO9797 Padding Method 1. If other padding methods are needed, you can apply them prior to calling the service.

**ISO9797 ALGORITHM 3 (Retail MAC)**  
Denoted by `KeyUsage` of ISO9797\_ALGORITHM3. The same padding rules apply as Algorithm 1

**ISO9797 ALGORITHM 5 (CMAC)**  
Denoted by `KeyUsage` of TR31\_M6\_ISO\_9797\_5\_CMAC\_KEY

**HMAC**  
Denoted by `KeyUsage` of TR31\_M7\_HMAC\_KEY including HMAC\_SHA224, HMAC\_SHA256, HMAC\_SHA384 and HMAC\_SHA512

**AS2805.4.1 MAC**  
Denoted by `KeyUsage` of TR31\_M0\_ISO\_16609\_MAC\_KEY. For more details on AS2805, see [AS2805](advanced.regional.as2805.md)

**DUKPT MAC**  
DUKPT MAC is typically used to confirm the source and payload of messages to/from payment terminals. It derives a key using DUKPT derivation techniques and then performs the MAC. Keys used with this option are denoted by a `KeyUsage` of TR31\_B0\_BASE\_DERIVATION\_KEY. 

**EMV MAC**  
EMV MAC is typically referred to as an integrity key in EMV documentation. It derives a key using EMV derivation techniques and then utilizes ISO9797\_ALGORITHM3 internally. It is typically used to send issuer scripts to a chip card for reprogramming. Keys used with this option are denoted by a `KeyUsage` of TR31\_E2\_EMV\_MKEY\_INTEGRITY. If you are both sending a script and update an offline pin, see [GenerateMacEmvPinChange](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateMacEmvPinChange) that performs both of these operations. 

**Topics**
+ [Generate MAC](generate-mac.md)
+ [Verify MAC](verify-mac.md)