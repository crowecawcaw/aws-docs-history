# CreateDomain

## Description

The `CreateDomain` operation creates a new domain. The domain name must be
unique among the domains associated with the Access Key ID provided in the request. The
`CreateDomain` operation might take 10 or more seconds to complete.

###### Note

`CreateDomain` is an idempotent operation; running it multiple times
using the same domain name will _not_ result in an error response.

You can create up to 250 domains per account.

If you require additional domains, go to [https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-simpledb-domains](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-simpledb-domains "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-simpledb-domains").

## Request Parameters

| Name         | Description                                                                                                                                                                          | Required |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `DomainName` | The name of the domain to create. The name can range between<br>3 and 255 characters and can contain the following characters: a-z, A-Z,<br>0-9, '\_', '-', and '.'.<br>Type: String | Yes      |

## Response Elements

See [Common Response Elements](SDB_API_CommonResponseElements.md "SDB_API_CommonResponseElements.md").

## Special Errors

| Error                   | Description                                                |
| ----------------------- | ---------------------------------------------------------- |
| `InvalidParameterValue` | Value (" + value + ") for parameter DomainName is invalid. |
| `MissingParameter`      | The request must contain the parameter<br>`DomainName`.    |
| `NumberDomainsExceeded` | Number of domains limit exceeded.                          |

## Examples

### Sample Request

```

https://sdb.amazonaws.com/
?Action=CreateDomain
&AWSAccessKeyId=[valid access key id]
&DomainName=MyDomain
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A01%3A28-07%3A00
&Version=2009-04-15
&Signature=[valid signature]

```

### Sample Response

```

**<CreateDomainResponse>**
  **<ResponseMetadata>**
    **<RequestId>**2a1305a2-ed1c-43fc-b7c4-e6966b5e2727**</RequestId>**
    **<BoxUsage>**0.0000219907**</BoxUsage>**
  **</ResponseMetadata>**
**</CreateDomainResponse>**

```

## Related Actions

- [DeleteDomain](SDB_API_DeleteDomain.md "SDB_API_DeleteDomain.md")
- [ListDomains](SDB_API_ListDomains.md "SDB_API_ListDomains.md")
