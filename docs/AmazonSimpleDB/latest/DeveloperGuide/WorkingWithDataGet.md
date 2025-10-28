# Getting Data from a Domain

The following is an example of getting data from an item using REST.

```

https://sdb.amazonaws.com/
?Action=GetAttributes
&AWSAccessKeyId=[valid access key id]
&DomainName=MyDomain
&ItemName=JumboFez
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A07-07%3A00
&Version=2009-04-15
&Signature=[valid signature]

```

Amazon SimpleDB returns output similar to the following.

```

<GetAttributesResponse>
  <GetAttributesResult>
    <Attribute><Name>Color</Name><Value>Blue</Value></Attribute>
    <Attribute><Name>Size</Name><Value>Med</Value></Attribute>
    <Attribute><Name>Price</Name><Value>0014.99</Value></Attribute>
  </GetAttributesResult>
  <ResponseMetadata>
    <RequestId>b1e8f1f7-42e9-494c-ad09-2674e557526d</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</GetAttributesResponse>

```
