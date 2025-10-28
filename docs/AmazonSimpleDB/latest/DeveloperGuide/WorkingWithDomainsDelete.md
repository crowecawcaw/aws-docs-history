# Deleting a Domain

The following is an example of deleting a domain using REST.

```

https://sdb.amazonaws.com/
?Action=DeleteDomain
&AWSAccessKeyId=[valid access key id]
&DomainName=MyOtherDomain
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A02%3A20-07%3A00
&Version=2009-04-15
&Signature=[valid signature]

```

Amazon SimpleDB returns output similar to the following.

```

<DeleteDomainResponse>
  <ResponseMetadata>
    <RequestId>c522638b-31a2-4d69-b376-8c5428744704</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</DeleteDomainResponse>

```
