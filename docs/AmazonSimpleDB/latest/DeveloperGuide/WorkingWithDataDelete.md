# Deleting Data from a Domain

The following is an example of deleting data from an item using REST.

```

https://sdb.amazonaws.com/
?Action=DeleteAttributes
&DomainName=MyDomain
&ItemName=JumboFez
&Attribute.1.Name=color
&Attribute.1.Value=red
&Attribute.2.Name=color
&Attribute.2.Value=brick
&Attribute.3.Name=color
&Attribute.3.Value=garnet
&AWSAccessKeyId=[valid access key id]
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A07-07%3A00
&Version=2009-04-15
&Signature=[valid signature]

```

Amazon SimpleDB returns output similar to the following.

```

<DeleteAttributesResponse>
  <ResponseMetadata>
    <RequestId>05ae667c-cfac-41a8-ab37-a9c897c4c3ca</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</DeleteAttributesResponse>

```

###### Note

For information on performing multiple delete operations at once, see [BatchDeleteAttributes](SDB_API_BatchDeleteAttributes.md "SDB_API_BatchDeleteAttributes.md").
