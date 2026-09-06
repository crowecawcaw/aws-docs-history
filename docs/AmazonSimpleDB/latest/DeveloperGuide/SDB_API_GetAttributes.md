

# GetAttributes
<a name="SDB_API_GetAttributes"></a>

## Description
<a name="SDB_API_GetAttributes_Description"></a>

Returns all of the attributes associated with the item. Optionally, the attributes returned can be limited to one or more specified attribute name parameters.

Amazon SimpleDB keeps multiple copies of each domain. When data is written or updated, all copies of the data are updated. However, it takes time for the update to propagate to all storage locations. The data will eventually be consistent, but an immediate read might not show the change. If eventually consistent reads are not acceptable for your application, use `ConsistentRead`. Although this operation might take longer than a standard read, it always returns the last updated value. 

**Note**  
If the item does not exist on the replica that was accessed for this operation, an empty set is returned.   
If you specify `GetAttributes` without any attribute names, all the attributes for the item are returned. 

## Request Parameters
<a name="SDB_API_GetAttributes_RequestParameters"></a>


|  Name  |  Description  |  Required | 
| --- | --- | --- | 
|  ItemName  |  The name of the item.  |  Yes  | 
|  AttributeName  |  The name of the attribute.  |  No  | 
|  DomainName  |  The name of the domain in which to perform the operation. <br /> Type: String  |  Yes  | 
|  ConsistentRead  |  When set to `true`, ensures that the most recent data is returned. For more information, see [Consistency](ConsistencySummary.md)<br /> Type: Boolean <br /> Default: `false`  |  No | 

## Response Elements
<a name="SDB_API_GetAttributes_ResponseElements"></a>


|  Name  |  Description  | 
| --- | --- | 
|  <Attribute><Name>... </Name><Value>... </Value></Attribute>  |  The name of the attribute and value.  | 

## Special Errors
<a name="SDB_API_GetAttributes_SpecialErrors"></a>


|  Error  |  Description  | 
| --- | --- | 
|  InvalidParameterValue  |  Value (" \+ value \+ ") for parameter Name is invalid. Value exceeds maximum length of 1024. | 
|  InvalidParameterValue  |  Value (" \+ value \+ ") for parameter Item is invalid. Value exceeds max length of 1024. | 
|  InvalidParameterValue  |  Value (" \+ value \+ ") for parameter ConsistentRead is invalid. The ConsistentRead flag should be either true or false. | 
|  MissingParameter  |  The request must contain the parameter DomainName. | 
|  MissingParameter  |  The request must contain the parameter ItemName. | 
|  NoSuchDomain  |  The specified domain does not exist. | 

## Examples
<a name="SDB_API_GetAttributes_Examples"></a>

### Sample Request
<a name="SDB_API_GetAttributes_Examples_Request"></a>

```
https://sdb.amazonaws.com/
?Action=GetAttributes
&AWSAccessKeyId=[valid access key id]
&DomainName=MyDomain
&ItemName=Item123
&ConsistentRead=true
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A07-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

### Sample Response
<a name="SDB_API_GetAttributes_Examples_Response"></a>

```
<GetAttributesResponse>
  <GetAttributesResult>
    <Attribute><Name>Color</Name><Value>Blue</Value></Attribute>
    <Attribute><Name>Size</Name><Value>Med</Value></Attribute>
    <Attribute><Name>Price</Name><Value>14</Value></Attribute>
  </GetAttributesResult>
  <ResponseMetadata>
    <RequestId>b1e8f1f7-42e9-494c-ad09-2674e557526d</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</GetAttributesResponse>
```

### Sample Request
<a name="SDB_API_GetAttributes_Examples_Request2"></a>

```
https://sdb.amazonaws.com/
?Action=GetAttributes
&AWSAccessKeyId=[valid access key id]
&DomainName=MyDomain
&ItemName=Item123
&AttributeName.0=Color
&AttributeName.1=Size
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A07-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

### Sample Response
<a name="SDB_API_GetAttributes_Examples_Response2"></a>

```
<GetAttributesResponse>
  <GetAttributesResult>
    <Attribute><Name>Color</Name><Value>Blue</Value></Attribute>
    <Attribute><Name>Size</Name><Value>Med</Value></Attribute>
  </GetAttributesResult>
  <ResponseMetadata>
    <RequestId>b1e8f1f7-42e9-494c-ad09-2674e557526d</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</GetAttributesResponse>
```

## Related Actions
<a name="SDB_API_GetAttributes_Related_Actions"></a>
+  [DeleteAttributes](SDB_API_DeleteAttributes.md) 
+  [PutAttributes](SDB_API_PutAttributes.md) 