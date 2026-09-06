

# BatchDeleteAttributes
<a name="SDB_API_BatchDeleteAttributes"></a>

## Description
<a name="SDB_API_BatchDeleteAttributes_Description"></a>

Performs multiple `DeleteAttributes` operations in a single call, which reduces round trips and latencies. This enables Amazon SimpleDB to optimize requests, which generally yields better throughput. 

**Note**  
If you specify `BatchDeleteAttributes` without attributes or values, all the attributes for the item are deleted.   
`BatchDeleteAttributes` is an idempotent operation; running it multiple times on the same item or attribute *doesn't* result in an error.  
The `BatchDeleteAttributes` operation succeeds or fails in its entirety. There are no partial deletes.  
You can execute multiple `BatchDeleteAttributes` operations and other operations in parallel. However, large numbers of concurrent `BatchDeleteAttributes` calls can result in Service Unavailable (503) responses.   
This operation is vulnerable to exceeding the maximum URL size when making a REST request using the HTTP GET method.  
This operation does not support conditions using `Expected.Name`, `Expected.Value`, or `Expected.Exists`.

The following limitations are enforced for this operation:
+ 1 MB request size
+ 25 item limit per `BatchDeleteAttributes` operation

## Request Parameters
<a name="SDB_API_BatchDeleteAttributes_RequestParameters"></a>


|  Name  |  Description  |  Required | 
| --- | --- | --- | 
|  Item.Y.ItemName  |  The name of the item. <br /> Type: String. <br /> Default: None.  |  Yes  | 
| `Item.Y.Attribute.X.Name` |  The name of the attribute for the specified item. *Y* or *X* can be any positive integer or 0. If you specify `BatchDeleteAttributes` without attribute names or values, all the attributes for the item are deleted.<br /> Type: String. <br /> Default: None.  |  No  | 
| `Item.Y.Attribute.X.Value` |  The value of the attribute for the specified item. *Y* or *X* can be any positive integer or 0. If an attribute value is specified, then the corresponding attribute name is required.<br /> Type: String. <br /> Default: None.  |  Yes  | 
|  DomainName  |  The name of the domain in which to perform the operation. <br /> Type: String <br /> Default: None.  |  Yes  | 

## Response Elements
<a name="SDB_API_BatchDeleteAttributes_CommonResponseElements"></a>

See [Common Response Elements](SDB_API_CommonResponseElements.md).

## Special Errors
<a name="SDB_API_BatchDeleteAttributes_SpecialErrors"></a>


|  Error  |  Description  | 
| --- | --- | 
|  AttributeDoesNotExist  |  Attribute ("\+ name \+ ") does not exist. | 
|  DuplicateItemName  |  Item item\_name was specified more than once.  | 
|  InvalidParameterValue  |  Value (" \+ value \+ ") for parameter Name is invalid.The empty string is an illegal attribute name. | 
|  InvalidParameterValue  |  Value (" \+ value \+ ") for parameter Name is invalid. Value exceeds maximum length of 1024. | 
|  InvalidParameterValue  |  Value (" \+ value \+ ") for parameter Item is invalid. Value exceeds max length of 1024. | 
|  InvalidParameterValue  |  Value (" \+ value \+ ") for parameter Value is invalid. Value exceeds maximum length of 1024. | 
|  InvalidWSDLVersion  |  Parameter (" \+ parameterName \+") is only supported in WSDL version 2009-04-15 or beyond. Please upgrade to new version. | 
|  MissingParameter  |  The request must contain the parameter DomainName. | 
|  MissingParameter  |  The request must contain the parameter ItemName. | 
|  MissingParameter  |  The request must contain the attribute Name, if an attribute Value is specified.  | 
|  NoSuchDomain  |  The specified domain does not exist. | 
| `NumberSubmittedItemsExceeded` |  Too many items in a single call. Up to 25 items per call allowed. | 
| `NumberSubmittedAttributesExceeded` |  Too many attributes for item itemName in a single call. Up to 256 attributes per call allowed.  | 

## Examples
<a name="SDB_API_BatchDeleteAttributes_Examples"></a>

### Sample Request
<a name="SDB_API_BatchDeleteAttributes_Examples_Request"></a>

In this example, the Jumbo Fez and Petite Fez have sold out in several colors. The following sample deletes the `red`, `brick`, and `garnet` values from the `color` attribute of the `JumboFez` item, and the `pink` and `fuchsia` values from the `color` attribute of the `PetiteFez` item.

```
https://sdb.amazonaws.com/
?Action=BatchDeleteAttributes
&Item.1.ItemName=JumboFez
&Item.1.Attribute.1.name=color&
&Item.1.Attribute.1.value=red&
&Item.1.Attribute.2.name=color&
&Item.1.Attribute.2.value=brick&
&Item.1.Attribute.3.name=color&
&Item.1.Attribute.3.value=garnet&
&Item.2.ItemName=PetiteFez
&Item.2.Attribute.1.name=color&
&Item.2.Attribute.1.value=pink&
&Item.2.Attribute.2.name=color&
&Item.2.Attribute.2.value=fuchsia&
&AWSAccessKeyId=[valid access key id]
&DomainName=MyDomain
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A07-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

### Sample Response
<a name="SDB_API_BatchDeleteAttributes_Examples_Response"></a>

```
<BatchDeleteAttributesResponse">
  <ResponseMetadata>
    <RequestId>05ae667c-cfac-41a8-ab37-a9c897c4c3ca</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</BatchDeleteAttributesResponse>
```

## Related Actions
<a name="SDB_API_BatchDeleteAttributes_Related_Actions"></a>
+  [DeleteAttributes](SDB_API_DeleteAttributes.md) 
+  [GetAttributes](SDB_API_GetAttributes.md) 