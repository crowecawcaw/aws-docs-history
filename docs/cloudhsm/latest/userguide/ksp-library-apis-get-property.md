# NCryptGetProperty with Key storage provider (KSP)

The `NCryptGetProperty` function retrieves property values for a key
storage object.

## Parameters

`hObject` [in]

The handle of the object whose property you want to retrieve. You can
use:

- A provider handle (`NCRYPT_PROV_HANDLE`)
- A key handle (`NCRYPT_KEY_HANDLE`)

`pszProperty` [in]

A pointer to a null-terminated Unicode string containing the property name
to retrieve.

When using `NCRYPT_PROV_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the
following KSP identifiers:

| Identifier/Value                                                        | Description                                                                                     |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| NCRYPT\_IMPL\_TYPE\_PROPERTY<br>L"Impl Type"                            | A DWORD containing flags that define provider<br>implementation details                         |
| NCRYPT\_MAX\_NAME\_LENGTH\_PROPERTY<br>L"Max Name Length"               | A DWORD containing the maximum length (in characters)<br>for a persistent key name.             |
| NCRYPT\_NAME\_PROPERTY<br>L"Name"                                       | A pointer to a null-terminated Unicode string<br>containing the KSP name.                       |
| NCRYPT\_VERSION\_PROPERTY<br>L"Version"                                 | A DWORD containing the provider version (high word:<br>major version, low word: minor version). |
| NCRYPT\_USE\_CONTEXT\_PROPERTY<br>L"Use Context"                        | A pointer to a null-terminated Unicode string<br>describing the operation context.              |
| NCRYPT\_SECURITY\_DESCR\_SUPPORT\_PROPERTY<br>L"Security Descr Support" | Indicates if the provider supports security<br>descriptors for keys.                            |

When using `NCRYPT_KEY_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the
following KSP identifiers:

| Identifier/Value                                         | Description                                                                                 |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| NCRYPT\_ALGORITHM\_PROPERTY<br>L"Algorithm Name"         | A null-terminated Unicode string containing the key's<br>algorithm name.                    |
| NCRYPT\_BLOCK\_LENGTH\_PROPERTY<br>L"Block Length"       | A DWORD containing the encryption block length in<br>bytes.                                 |
| NCRYPT\_EXPORT\_POLICY\_PROPERTY<br>L"Export Policy"     | A DWORD containing flags that specify the persisted<br>key's export policy.                 |
| NCRYPT\_KEY\_USAGE\_PROPERTY<br>L"Key Usage"             | A DWORD containing flags that define key usage<br>details.                                  |
| NCRYPT\_KEY\_TYPE\_PROPERTY<br>L"Key Type"               | A DWORD containing flags that define the key<br>type.                                       |
| NCRYPT\_LENGTH\_PROPERTY<br>L"Length"                    | A DWORD containing the key length in bits.                                                  |
| NCRYPT\_LENGTHS\_PROPERTY<br>L"Lengths"                  | A pointer to an NCRYPT\_SUPPORTED\_LENGTHS structure<br>containing supported key sizes.     |
| NCRYPT\_NAME\_PROPERTY<br>L"Name"                        | A pointer to a null-terminated Unicode string<br>containing the key name.                   |
| NCRYPT\_SECURITY\_DESCR\_PROPERTY<br>L"Security Descr"   | A pointer to a SECURITY\_DESCRIPTOR structure<br>containing key access control information. |
| NCRYPT\_ALGORITHM\_GROUP\_PROPERTY<br>L"Algorithm Group" | A null-terminated Unicode string containing the<br>object's algorithm group name.           |
| NCRYPT\_UNIQUE\_NAME\_PROPERTY<br>L"Unique Name"         | A pointer to a null-terminated Unicode string<br>containing the key's unique name.          |

###### Note

Values are wide-character string literal, as indicated by L before the
literal.

`pbOutput` [out]

The address of a buffer to store the property value. Specify the buffer
size using `cbOutput`.

To determine the required buffer size, set this parameter to NULL. The
function stores the required size (in bytes) in the location pointed to by
`pcbResult`.

`cbOutput` [in]

The size of the `pbOutput` buffer in bytes.

`pcbResult` [out]

A pointer to a DWORD variable that stores the number of bytes copied to
the`pbOutput` buffer.

If the `pbOutput` is NULL, this stores the required
size (in bytes).

`dwFlags` [in]

Flags to modify the function's behavior. You can use zero or:

| Value                | Meaning                  |
| -------------------- | ------------------------ |
| NCRYPT\_SILENT\_FLAG | This flag has no effect. |

When pszProperty is `NCRYPT_SECURITY_DESCR_PROPERTY`, use one
or a combination of:

| Value                        | Meaning                  |
| ---------------------------- | ------------------------ |
| OWNER\_SECURITY\_INFORMATION | This flag has no effect. |
| GROUP\_SECURITY\_INFORMATION | This flag has no effect. |
| DACL\_SECURITY\_INFORMATION  | This flag has no effect. |
| LABEL\_SECURITY\_INFORMATION | This flag has no effect. |
| SACL\_SECURITY\_INFORMATION  | This flag has no effect. |

## Return Value

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code             | Description                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| ERROR\_SUCCESS          | The operation completed successfully.                               |
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid.                               |
| NTE\_FAIL               | The operation couldn't complete.                                    |
| NTE\_BAD\_FLAGS         | The `dwFlags` parameter contains an invalid<br>value.               |
| NTE\_NOT\_SUPPORTED     | The `pszAlgId` parameter contains a value that is not<br>supported. |
| NTE\_INVALID\_HANDLE    | The handle in `hObject` is not valid.                               |
| NTE\_BUFFER\_TOO\_SMALL | The `cbOutput` parameter is too small for return<br>values.         |
