

# FHIR R4 `$confirm-attribution-list` operation for HealthLake
<a name="reference-fhir-operations-confirm-attribution-list"></a>

Indicates to a Producer that the Consumer has no more changes to make to the Attribution List. This operation finalizes the attribution list by removing inactive members from the list, changing the status to "final", and acknowledging the operation. This operation is part of the [FHIR Member Attribution (ATR) List IG 2.1.0 implementation.](https://build.fhir.org/ig/HL7/davinci-atr/spec.html)

## Endpoint
<a name="confirm-attribution-list-endpoint"></a>

```
POST [base]/Group/[id]/$confirm-attribution-list
```

## Request
<a name="confirm-attribution-list-request"></a>

No parameters required.

```
POST [base]/Group/[id]/$confirm-attribution-list
```

## Response
<a name="confirm-attribution-list-response"></a>

Returns HTTP 201 with a confirmation message.

### Sample Response
<a name="confirm-attribution-list-response-example"></a>

```
HTTP Status Code: 201

{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "message",
      "valueString": "Accepted."
    }
  ]
}
```

## Group Status After Confirmation
<a name="confirm-attribution-list-group-status"></a>

After successful confirmation, the Group resource will have its attribution list status set to "final":

```
{
  "resourceType": "Group",
  "id": "fullexample",
  "extension": [
    {
      "url": "http://hl7.org/fhir/us/davinci-atr/StructureDefinition/ext-attributionListStatus",
      "valueCode": "final"
    }
  ]
  // ... other Group properties
}
```

## Error Handling
<a name="confirm-attribution-list-error-handling"></a>

The operation handles the following error conditions:


| Error | HTTP Status | Description | 
| --- | --- | --- | 
| Invalid operation request | 400 | Non-conformant request parameters or structure | 
| Group resource not found | 404 | The specified Group ID does not exist | 

## Authorization and Security
<a name="confirm-attribution-list-authorization"></a>

SMART Scope Requirements  
Clients must have appropriate privileges to read Group resources and related attribution resources  
For `$confirm-attribution-list`, clients must also have write privileges to modify Group resources  
Standard FHIR authorization mechanisms apply to all operations