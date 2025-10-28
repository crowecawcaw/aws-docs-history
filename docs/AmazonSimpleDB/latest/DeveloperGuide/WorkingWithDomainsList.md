# Verifying the Domain

The following is an example of listing domains using REST.

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

Amazon SimpleDB returns output similar to the following.

```

<ListDomainsResponse>
  <ListDomainsResult>
    <DomainName>MyDomain</DomainName>
    <DomainName>MyOtherDomain</DomainName>
  </ListDomainsResult>
  <ResponseMetadata>
    <RequestId>eb13162f-1b95-4511-8b12-489b86acfd28</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</ListDomainsResponse>

```
