# Acquiring and payment facilitators

Acquirers, PSPs and Payment Facilators typically have a different set of cryptographic requirements than issuers. Common use cases include:

**Data Decryption**

Data (especially pan data) may be encrypted by a payment terminal and need to be decrypted by the backend. [Decrypt Data](../DataAPIReference/API_DecryptData.md "../DataAPIReference/API_DecryptData.md")
and Encrypt Data support a variety of methods including TDES, AES and DUKPT derivation techniques. The AWS Payment Cryptography service itself is also PCI P2PE compliant and is registered as a PCI P2PE decryption component.

**TranslatePin**

To maintain PCI PIN compliance, acquiring systems shall not have cardholder pins in the clear after they have been entered on a secure device. Therefore, to pass the pin
onward from terminal to a downstream system (such as a payment network or issuer), there is a need to re-encrypt it using a different key than the one that the payment terminal used.
[Translate Pin](../DataAPIReference/API_TranslatePinData.md "../DataAPIReference/API_TranslatePinData.md") accomplishes that by converting an encrypted pin from one key to another securely with the servicebbb. Using this command, pins can be converted between various schemes such as TDES, AES
and DUKPT derivation and pin block formats such as ISO-0, ISO-3 and ISO-4.

**VerifyMac**

Data from a payment terminal may be MAC'd to ensure that the data hasn't been modified in transit. [Verify Mac](../DataAPIReference/API_VerifyMac.md "../DataAPIReference/API_VerifyMac.md")
and GenerateMac supports a variety of techniques using symmetric keys
including TDES, AES and DUKPT derivation techniques for use with ISO-9797-1 algorithm 1, ISO-9797-1 algorithm 3 (Retail MAC) and CMAC techniques.

###### Additional Topics

- [Using Dynamic Keys](use-cases-acquirers-dynamickeys.md "use-cases-acquirers-dynamickeys.md")
