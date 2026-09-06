

# DomainMetadata
<a name="SDB_API_DomainMetadata"></a>

## Description
<a name="SDB_API_DomainMetadata_Description"></a>

Returns information about the domain, including when the domain was created, the number of items and attributes, and the size of attribute names and values.

## Request Parameters
<a name="SDB_API_DomainMetadata_RequestParameters"></a>


|  Name  |  Description  |  Required | 
| --- | --- | --- | 
|  DomainName  |  The name of the domain for which to display metadata. <br /> Type: String  |  Yes  | 

## Response Elements
<a name="SDB_API_DomainMetadata_ResponseElements"></a>


|  Name  |  Description  | 
| --- | --- | 
|  Timestamp  |  The data and time when metadata was calculated in Epoch (UNIX) time. | 
|  ItemCount  |  The number of all items in the domain.  | 
|  AttributeValueCount  |  The number of all attribute name/value pairs in the domain.  | 
|  AttributeNameCount  |  The number of unique attribute names in the domain.  | 
|  ItemNamesSizeBytes  |  The total size of all item names in the domain, in bytes.  | 
|  AttributeValuesSizeBytes  |  The total size of all attribute values, in bytes.  | 
|  AttributeNamesSizeBytes  |  The total size of all unique attribute names, in bytes.  | 

## Special Errors
<a name="SDB_API_DomainMetadata_SpecialErrors"></a>


|  Error  |  Description  | 
| --- | --- | 
|  MissingParameter  |  The request must contain the parameter DomainName. | 
|  NoSuchDomain  |  The specified domain does not exist. | 

## Examples
<a name="SDB_API_DomainMetadata_Examples"></a>

### Sample Request
<a name="SDB_API_DomainMetadata_Examples_Request"></a>

```
https://sdb.amazonaws.com/
?Action=DomainMetadata
&AWSAccessKeyId=[valid access key id]
&DomainName=MyDomain
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A07-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

### Sample Response
<a name="SDB_API_DomainMetadata_Examples_Response"></a>

```
<DomainMetadataResponse>
  <DomainMetadataResult>
    <ItemCount>195078</ItemCount>
    <ItemNamesSizeBytes>2586634</ItemNamesSizeBytes>
    <AttributeNameCount >12</AttributeNameCount >
    <AttributeNamesSizeBytes>120</AttributeNamesSizeBytes>
    <AttributeValueCount>3690416</AttributeValueCount>
    <AttributeValuesSizeBytes>50149756</AttributeValuesSizeBytes>
    <Timestamp>1225486466</Timestamp>
  </DomainMetadataResult>
  <ResponseMetadata>
    	<RequestId>b1e8f1f7-42e9-494c-ad09-2674e557526d</RequestId>
    	<BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</DomainMetadataResponse>
```

## Related Actions
<a name="SDB_API_DomainMetadata_Related_Actions"></a>
+  [CreateDomain](SDB_API_CreateDomain.md) 
+  [ListDomains](SDB_API_ListDomains.md) 