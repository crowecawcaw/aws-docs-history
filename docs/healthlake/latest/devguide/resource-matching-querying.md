

# Querying linked data
<a name="resource-matching-querying"></a>

A matched entity is stored as multiple resources connected by a `Linkage`. Use the standard FHIR R4 search interactions to retrieve linked data (see [Searching FHIR resources](searching-fhir-resources.md)).

Get all resources linked to a patient  
Use the `item` search parameter to find the patient's `Linkage`, and `_include=Linkage:item` to return the linked resources in the same bundle:  

```
GET /Linkage?item=Patient/patient-A&_include=Linkage:item
```

Get all linkages in the data store  
Return every `Linkage` along with its linked resources:  

```
GET /Linkage?_include=Linkage:item&_count=100
```

Count the linkages in the data store  

```
GET /Linkage?_summary=count
```

Get clinical data across a linked patient  
To retrieve another resource type (such as `Observation`) for a patient and everyone linked to them, first read the `Linkage` to get the linked patient IDs:  

```
GET /Linkage?item=Patient/patient-A&_include=Linkage:item
```
Then search the target resource type across those IDs:  

```
GET /Observation?patient=Patient/patient-A,Patient/patient-B,Patient/patient-C
```