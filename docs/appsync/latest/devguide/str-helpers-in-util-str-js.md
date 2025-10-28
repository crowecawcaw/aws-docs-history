# String helpers in util.str

`util.str` contains methods to help with common String operations.

## util.str utils list

**`util.str.normalize(String,
 String)`**

Normalizes a string using one of the four unicode normalization forms:
NFC, NFD, NFKC, or NFKD. The first argument is the string to normalize. The
second argument is either "nfc", "nfd", "nfkc", or "nfkd" specifying the
normalization type to use for the normalization process.
