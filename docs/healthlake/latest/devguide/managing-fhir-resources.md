

# Managing FHIR resources in AWS HealthLake
<a name="managing-fhir-resources"></a>

Use FHIR R4 RESTful API interactions to manage FHIR resources in a HealthLake data store. The following sections describe all HealthLake-supported FHIR R4 RESTful API interactions available for FHIR resource management. For information about HealthLake data store capabilities and which portions of the FHIR specification it supports, see [FHIR R4 Capability Statement for AWS HealthLake](reference-fhir-capability-statement.md).

**Note**  
The FHIR interactions listed in this chapter are built in conformance to the HL7 FHIR R4 standard for health care data exchange. Because they are representations of HL7 FHIR services, they are not offered through AWS CLI and AWS SDKs. For more information, see [RESTful API](https://hl7.org/fhir/R4/http.html) in the **FHIR R4 RESTful API documentation**.

The following table lists FHIR R4 interactions supported by AWS HealthLake. For information about FHIR *resource types* supported by HealthLake, see [Resource types](reference-fhir-resource-types.md).




**FHIR R4 interactions supported by AWS HealthLake**  
<a name="supported-fhir-interactions"></a>
<table>
<thead>
  <tr><th>Interaction</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="2">Whole system interactions</td></tr>
  <tr><td>    <a href="https://hl7.org/fhir/R4/http.html#capabilities">https://hl7.org/fhir/R4/http.html#capabilities</a></td><td>Get a capability statement for the system. See <a href="reference-fhir-capability-statement.md">FHIR R4 Capability Statement for AWS HealthLake</a>.</td></tr>
  <tr><td>    <a href="https://hl7.org/fhir/R4/http.html#transaction">https://hl7.org/fhir/R4/http.html#transaction</a></td><td>Update, create, or delete a set of resources in a single interaction. See <a href="managing-fhir-resources-bundle.md">Bundling FHIR resources</a>.</td></tr>
  <tr><td colspan="2">Type level interactions</td></tr>
  <tr><td>    <a href="https://hl7.org/fhir/R4/http.html#create">https://hl7.org/fhir/R4/http.html#create</a></td><td>Create a new resource with a server-assigned ID. See <a href="managing-fhir-resources-create.md">Creating a FHIR resource</a>.</td></tr>
  <tr><td>    <a href="https://hl7.org/fhir/R4/http.html#search">https://hl7.org/fhir/R4/http.html#search</a></td><td>Search a resource type based on some filter criteria. See <a href="searching-fhir-resources.md">Searching FHIR resources</a>.</td></tr>
  <tr><td>    <a href="https://hl7.org/fhir/R4/http.html#history">https://hl7.org/fhir/R4/http.html#history</a></td><td>Retrieve the change history for a particular resource type. See <a href="managing-fhir-resources-read-history.md">Reading FHIR resource history</a>.</td></tr>
  <tr><td colspan="2">Instance level interactions</td></tr>
  <tr><td>    <a href="https://hl7.org/fhir/R4/http.html#read">https://hl7.org/fhir/R4/http.html#read</a></td><td>Read the current state of a resource. See <a href="managing-fhir-resources-read.md">Reading a FHIR resource</a>.</td></tr>
  <tr><td>    <a href="https://hl7.org/fhir/R4/http.html#history">https://hl7.org/fhir/R4/http.html#history</a></td><td>Read the change history for a particular resource. See <a href="managing-fhir-resources-read-history.md">Reading FHIR resource history</a>.</td></tr>
  <tr><td>    <a href="https://hl7.org/fhir/R4/http.html#vread">https://hl7.org/fhir/R4/http.html#vread</a></td><td>Read the state of a specific version of the resource. See <a href="managing-fhir-resources-read-history.md#managing-fhir-data-get-version-specific-resource">Reading version-specific FHIR resource history</a>.</td></tr>
  <tr><td>    <a href="https://hl7.org/fhir/R4/http.html#update">https://hl7.org/fhir/R4/http.html#update</a></td><td>Update a resource by its ID (or create it if it's new). See <a href="managing-fhir-resources-update.md">Updating a FHIR resource</a>.</td></tr>
  <tr><td>    <a href="https://hl7.org/fhir/R4/http.html#delete">https://hl7.org/fhir/R4/http.html#delete</a></td><td>Delete a resource. See <a href="managing-fhir-resources-delete.md">Deleting a FHIR resource</a>.</td></tr>
</tbody>
</table>


**Topics**
+ [Creating a FHIR resource](managing-fhir-resources-create.md)
+ [Reading a FHIR resource](managing-fhir-resources-read.md)
+ [Reading FHIR resource history](managing-fhir-resources-read-history.md)
+ [Updating a FHIR resource](managing-fhir-resources-update.md)
+ [Modifying Resources with PATCH Operation](managing-fhir-resources-patch.md)
+ [Bundling FHIR resources](managing-fhir-resources-bundle.md)
+ [Deleting a FHIR resource](managing-fhir-resources-delete.md)
+ [Idempotency and Concurrency](managing-fhir-resources-idempotency.md)