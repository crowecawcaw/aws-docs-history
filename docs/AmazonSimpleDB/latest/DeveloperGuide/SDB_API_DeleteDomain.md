

# DeleteDomain
<a name="SDB_API_DeleteDomain"></a>

## Description
<a name="SDB_API_DeleteDomain_Description"></a>

The `DeleteDomain` operation deletes a domain. Any items (and their attributes) in the domain are deleted as well. The `DeleteDomain` operation might take 10 or more seconds to complete. 

**Note**  
Running `DeleteDomain` on a domain that does not exist or running the function multiple times using the same domain name will *not* result in an error response.

**Important**  
Domain deletion is blocked while any export for that domain is in PENDING or IN\_PROGRESS status. Ensure all exports have completed (SUCCEEDED or FAILED status) before attempting to delete a domain. You can use the `ListExports` operation to check for active exports.

## Request Parameters
<a name="SDB_API_DeleteDomain_RequestParameters"></a>


|  Name  |  Description  |  Required | 
| --- | --- | --- | 
|  DomainName  |  The name of the domain to delete. <br /> Type: String  |  Yes  | 

## Response Elements
<a name="SDB_API_DeleteDomain_CommonResponseElements"></a>

See [Common Response Elements](SDB_API_CommonResponseElements.md).

## Special Errors
<a name="SDB_API_DeleteDomain_SpecialErrors"></a>


|  Error  |  Description  | 
| --- | --- | 
|  MissingParameter  |  The request must contain the parameter DomainName. | 

## Examples
<a name="SDB_API_DeleteDomain_Examples"></a>

### Sample Request
<a name="SDB_API_DeleteDomain_Examples_Request"></a>

```
https://sdb.amazonaws.com/
?Action=DeleteDomain
&AWSAccessKeyId=[valid access key id]
&DomainName=MyDomain
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A02%3A20-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

### Sample Response
<a name="SDB_API_DeleteDomain_Examples_Response"></a>

```
<DeleteDomainResponse>
  <ResponseMetadata>
    <RequestId>c522638b-31a2-4d69-b376-8c5428744704</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</DeleteDomainResponse>
```

## Related Actions
<a name="SDB_API_DeleteDomain_Related_Actions"></a>
+  [CreateDomain](SDB_API_CreateDomain.md) 
+  [ListDomains](SDB_API_ListDomains.md) 