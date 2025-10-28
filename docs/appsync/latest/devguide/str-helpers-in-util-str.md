# String helpers in $util.str

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please
consider using the APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

`$util.str` contains methods to help with common String operations.

## $util.str utils list

**`$util.str.toUpper(String) : String`**

Takes a string and converts it to be entirely uppercase.

**`$util.str.toLower(String) : String`**

Takes a string and converts it to be entirely lowercase.

**`$util.str.toReplace(String, String, String) : String`**

Replaces a substring within a string with another string. The first
argument specifies the string on which to perform the replacement operation.
The second argument specifies the substring to replace. The third argument
specifies the string to replace the second argument with. The following is
an example of this utility's usage:

```

 INPUT:      $util.str.toReplace("hello world", "hello", "mellow")
 OUTPUT:     "mellow world"
```

**`$util.str.normalize(String, String) : String`**

Normalizes a string using one of the four unicode normalization forms:
NFC, NFD, NFKC, or NFKD. The first argument is the string to normalize. The
second argument is either "nfc", "nfd", "nfkc", or "nfkd" specifying the
normalization type to use for the normalization process.
