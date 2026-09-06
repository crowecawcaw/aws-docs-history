

# FHIR R4 Capability Statement for AWS HealthLake
<a name="reference-fhir-capability-statement"></a>

To find the FHIR-related capabilities (behaviors) of an active HealthLake data store, you must retrieve its Capability Statement. The Capability Statement is used as a statement of actual server functionality or a statement of required or desired server implementation. The FHIR [`capabilities`](https://hl7.org/fhir/R4/http.html#capabilities) interaction retrieves information about HealthLake data store capabilities and which portions of the FHIR specification it supports. HealthLake validates FHIR resource types according to the FHIR R4 [`StructureDefinition`](https://hl7.org/fhir/R4/structuredefinition.html) resource.

**To get the Capability Statement for a HealthLake data store**  


1. Collect HealthLake `region` and `datastoreId` values. For more information, see [Getting data store properties](managing-data-stores-describe.md).

1. Construct a URL for the request using the collected values for HealthLake `region` and `datastoreId`. Also include the FHIR `metadata` element in the URL. To view the entire URL path in the following example, scroll over the **Copy** button.

   ```
   https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/metadata
   ```

1. Send the request. The FHIR `capabilities` interaction uses a `GET` request with [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) signing protocol. The following `curl` example gets the Capability Statement for the HealthLake data store specified by the `datastoreId`. To view the entire example, scroll over the **Copy** button.

------
#### [ curl ]

   ```
   curl --request GET \
     'https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/metadata \
     --aws-sigv4 'aws:amz:region:healthlake' \
     --user "{{$AWS_ACCESS_KEY_ID}}:{{$AWS_SECRET_ACCESS_KEY}}" \
     --header "x-amz-security-token:{{$AWS_SESSION_TOKEN}}" \
     --header 'Accept: application/json'
   ```

------

   You will receive a `200` HTTP response code and the Capability Statement for your HealthLake data store. For more information, see [`CapabilityStatement`](https://hl7.org/fhir/R4/capabilitystatement.html) in the **FHIR R4 documentation**.