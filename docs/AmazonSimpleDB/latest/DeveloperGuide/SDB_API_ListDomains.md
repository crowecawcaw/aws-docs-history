# ListDomains

## Description

The `ListDomains` operation lists all domains associated with the Access Key
ID. It returns domain names up to the limit set by `MaxNumberOfDomains`. A
`NextToken` is returned if there are more than
`MaxNumberOfDomains` domains. Calling `ListDomains`
successive times with the `NextToken` returns up to
`MaxNumberOfDomains` more domain names each time.

## Request Parameters

| Name                 | Description                                                                                                                    | Required |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `MaxNumberOfDomains` | The maximum number of domain names you want returned.<br>Type: String<br>The range is 1 to 100.<br>The default setting is 100. | No       |
| `NextToken`          | String that tells Amazon SimpleDB where to start the next list of domain names.                                                | No       |

## Response Elements

| Name         | Description                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------- |
| `DomainName` | Domain names that match the expression.                                                              |
| `NextToken`  | An opaque token indicating that there are more than<br>`MaxNumberOfDomains` domains still available. |

## Special Errors

| Error                   | Description                                                                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `InvalidParameterValue` | Value (" + value + ") for parameter `MaxNumberOfDomains`<br>is invalid. `MaxNumberOfDomains` must be between 1 and<br>100. |
| `InvalidNextToken`      | The specified next token is not valid.                                                                                     |

## Examples

### Sample Request

```

https://sdb.amazonaws.com/
?Action=ListDomains
&AWSAccessKeyId=[valid access key id]
&MaxNumberOfDomains=2
&NextToken=[valid next token]
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A02%3A19-07%3A00
&Version=2009-04-15
&Signature=[valid signature]

```

### Sample Response

```

**<ListDomainsResponse>**
  **<ListDomainsResult>**
    **<DomainName>**Domain1-200706011651**</DomainName>**
    **<DomainName>**Domain2-200706011652**</DomainName>**
    **<NextToken>**TWV0ZXJpbmdUZXN0RG9tYWluMS0yMDA3MDYwMTE2NTY=**</NextToken>**
  **</ListDomainsResult>**
  **<ResponseMetadata>**
    **<RequestId>**eb13162f-1b95-4511-8b12-489b86acfd28**</RequestId>**
    **<BoxUsage>**0.0000219907**</BoxUsage>**
  **</ResponseMetadata>**
**</ListDomainsResponse>**

```

## Related Actions

- [CreateDomain](SDB_API_CreateDomain.md "SDB_API_CreateDomain.md")
- [DeleteDomain](SDB_API_DeleteDomain.md "SDB_API_DeleteDomain.md")
