

# FHIR R4 `$davinci-data-export` operation for HealthLake
<a name="reference-fhir-operations-davinci-data-export"></a>

The `$davinci-data-export` operation is an asynchronous FHIR operation that you can use to export healthcare data from AWS HealthLake. This operation supports multiple export types, including Member Attribution (ATR), PDex Provider Access, Payer-to-Payer, and Member Access APIs. It is a specialized version of the standard FHIR `$export` operation, designed to meet the requirements of the DaVinci implementation guides.

## Key Features
<a name="davinci-data-export-features"></a>
+ *Asynchronous Processing*: Follows the standard FHIR asynchronous request pattern
+ *Group-Level Export*: Exports data for members within a specific Group resource
+ *Multiple Export Types*: Supports ATR (Member Attribution), PDex Provider Access, Payer-to-Payer, and Member Access APIs
+ *Comprehensive Profile Support*: Includes US Core, CARIN Blue Button, and PDex profiles
+ *Flexible Filtering*: Supports filtering by patients, resource types, and time ranges
+ *NDJSON Output*: Provides data in newline-delimited JSON format

## Operation Endpoint
<a name="davinci-data-export-endpoint"></a>

```
GET [base]/Group/[id]/$davinci-data-export
POST [base]/Group/[id]/$davinci-data-export
```

## Request Parameters
<a name="davinci-data-export-parameters"></a>


| Parameter | Cardinality | Description | 
| --- | --- | --- | 
| patient | 0..\* | Specific members whose data to export. When omitted, all members in the Group are exported. | 
| \_type | 0..1 | Comma-delimited list of FHIR resource types to export. When omitted, all supported resource types for the specified export type are included. For ATR exports, this defaults to the 8 attribution resource types. For PDex exports, this includes all attribution resource types plus clinical and claims resource types from the US Core, CARIN Blue Button, and PDex profiles. | 
| \_since | 0..1 | Only include resources updated after this date and time. | 
| \_until | 0..1 | Only include resources updated before this date and time. | 
| exportType | 0..1 | The type of export to perform. Valid values: hl7.fhir.us.davinci-atr (ATR), hl7.fhir.us.davinci-pdex (Provider Access), hl7.fhir.us.davinci-pdex\#provider-snapshot (Provider Access snapshot), hl7.fhir.us.davinci-pdex.p2p (Payer-to-Payer), hl7.fhir.us.davinci-pdex.member (Member Access). Default: hl7.fhir.us.davinci-atr. | 
| \_includeEOB2xWoFinancial | 0..1 | When set to true, includes ExplanationOfBenefit resources that declare a CARIN BB 2.x Financial (non-Basis) profile in the export with financial data stripped. The exported resource conforms to the corresponding Basis profile, but the original resource in the data store is not modified. This parameter has no effect on resources that already declare a Basis profile, as those are always included and have residual financial data removed automatically. Default: false. | 
| \_security | 0..\* | Filter exported resources by meta.security Coding values. Use the system\|code format (pipe character must be URL-encoded as %7C). When multiple values are provided, resources must match all of them (AND semantics). Use system\| (trailing pipe, no code) to match any code from a given system. | 
| \_tag | 0..\* | Filter exported resources by meta.tag Coding values. Uses the same system\|code format and AND semantics as \_security. When both \_security and \_tag are specified, resources must match both filters. | 

**Filter behavior for \_security and \_tag**  
The `_security` and `_tag` filters apply to all export types, including `hl7.fhir.us.davinci-atr`. These filters also support the following FHIR search modifiers: `:not`, `:missing`, `:text`, `:above`, and `:below`. For example, you can use `_tag:not=archived` or `_security:missing=true`. The operation excludes from the export any resources that do not match the supplied filters.

**ExplanationOfBenefit financial data**  
The following financial data fields are removed from all exported CARIN BB 2.x `ExplanationOfBenefit` resources, regardless of whether the resource declares a Basis or a Financial profile: adjudication amounts, `payment`, `total`, `benefitPeriod`, `benefitBalance`, and item `net` and `unitPrice`. This ensures that financial data is not exported on Da Vinci Provider Access and Payer-to-Payer paths. `ExplanationOfBenefit` resources that declare only a PDex Prior Authorization profile (without a CARIN BB 2.x profile) are exported unchanged and no financial data is removed. If a resource declares both profiles, financial data is stripped.

### Supported Resource Types
<a name="davinci-data-export-supported-resources"></a>

The supported resource types depend on the export type you specify. For ATR exports, the following resource types are supported:
+ `Group`
+ `Patient`
+ `Coverage`
+ `RelatedPerson`
+ `Practitioner`
+ `PractitionerRole`
+ `Organization`
+ `Location`

For PDex exports (Provider Access, Payer-to-Payer, and Member Access), all clinical and claims resource types are supported in addition to the preceding types. For a complete list of supported resource types, see the [US Core Implementation Guide (STU 6.1)](https://hl7.org/fhir/us/core/STU6.1/), the [CARIN Blue Button Implementation Guide](https://hl7.org/fhir/us/carin-bb/), and the [Da Vinci Prior Authorization Support Implementation Guide](https://hl7.org/fhir/us/davinci-pas/).

## Export Types
<a name="davinci-data-export-types"></a>

The `$davinci-data-export` operation supports the following export types. You specify the export type by using the `exportType` parameter.


| Export Type | Purpose | Data Scope | Temporal Limit | 
| --- | --- | --- | --- | 
| hl7.fhir.us.davinci-atr | Member Attribution List | Attribution-related resources | None | 
| hl7.fhir.us.davinci-pdex | Provider Access API | Clinical and claims data for attributed patients | None | 
| hl7.fhir.us.davinci-pdex\#provider-snapshot | Provider Access API (snapshot) | All clinical, prior authorization, and non-financial claims and encounter data for attributed patients | None | 
| hl7.fhir.us.davinci-pdex.p2p | Payer-to-Payer Exchange | Historical member data for insurance transitions | 5 years | 
| hl7.fhir.us.davinci-pdex.member | Member Access API | Member's own health data | 5 years | 

**Temporal limits by export type**  
The 5-year temporal limit applies only to the Payer-to-Payer (`hl7.fhir.us.davinci-pdex.p2p`) and Member Access (`hl7.fhir.us.davinci-pdex.member`) export types. The Provider Access export types (`hl7.fhir.us.davinci-pdex` and `hl7.fhir.us.davinci-pdex#provider-snapshot`) have no temporal restriction. For the export types that are temporally limited, the 5-year limit does not apply to ATR resource types (`Group`, `Patient`, `Coverage`, `RelatedPerson`, `Practitioner`, `PractitionerRole`, `Organization`, `Location`). These resources are always included regardless of age.

**Temporal filtering basis**  
Temporal limits and the `_since` and `_until` parameters are evaluated against each resource's `meta.lastUpdated` timestamp rather than clinical or service dates. This provides consistent temporal filtering across all resource types.

### ATR (hl7.fhir.us.davinci-atr)
<a name="davinci-data-export-type-atr"></a>

With the ATR export type, you can export Member Attribution List data. Use this export type to retrieve attribution-related resources for members within a Group. For more information, see the [Da Vinci ATR Export Operation](https://build.fhir.org/ig/HL7/davinci-atr/OperationDefinition-davinci-data-export.html).

Supported Resource Types  
`Group`, `Patient`, `Coverage`, `RelatedPerson`, `Practitioner`, `PractitionerRole`, `Organization`, `Location`

Temporal Filtering  
No temporal filtering is applied. All matching resources are exported regardless of date.

### PDex Export Types
<a name="davinci-data-export-type-pdex"></a>

All PDex export types share the same supported profiles and filtering logic. For more information, see the [Da Vinci PDex Provider Access API](https://build.fhir.org/ig/HL7/davinci-epdx/provider-access-api.html). The following profiles are supported:
+ US Core 3.1.1, 6.1.0, and 7.0.0
+ PDex Prior Authorization (not supported for Member Access)
+ CARIN BB 2.x Basis profiles: Inpatient Institutional, Outpatient Institutional, Professional NonClinician, Oral, Pharmacy

For PDex exports, clinical and claims resources are automatically discovered for each patient in the Group. You do not need to explicitly reference these resources in the Group resource. The operation searches for all patient-compartment resources (such as `Observation`, `Condition`, `Coverage`, `RelatedPerson`, `MedicationRequest`, and `ExplanationOfBenefit`) that belong to the attributed patients. Only `Patient`, `Group`, and non-patient-compartment ATR types (`Practitioner`, `PractitionerRole`, `Organization`, `Location`) require explicit references in the Group.

Provider Access (`hl7.fhir.us.davinci-pdex`)  
Enables in-network providers to retrieve patient data for attributed patients.

Provider Access — snapshot (`hl7.fhir.us.davinci-pdex#provider-snapshot`)  
Returns a full snapshot of all clinical, prior authorization, and non-financial claims and encounter data for attributed patients. This export type behaves the same as `hl7.fhir.us.davinci-pdex` and is not subject to a temporal limit.

Payer-to-Payer (`hl7.fhir.us.davinci-pdex.p2p`)  
Enables data exchange between payers when a patient changes insurance.

Member Access (`hl7.fhir.us.davinci-pdex.member`)  
Enables members to access their own health data.

## Profile Support and Inclusion Logic
<a name="davinci-data-export-profile-support"></a>

For PDex exports, the `$davinci-data-export` operation uses profile declarations in the `meta.profile` element to determine which resources to include in the export.

### ExplanationOfBenefit Resource Handling
<a name="davinci-data-export-carin-handling"></a>

`ExplanationOfBenefit` (EOB) resources are included or excluded from PDex exports based on their `meta.profile` declarations:
+ ExplanationOfBenefit resources with a CARIN BB 1.x profile are excluded from the export.
+ ExplanationOfBenefit resources with no `meta.profile` set are excluded from the export.
+ ExplanationOfBenefit resources with a CARIN BB 2.x Basis profile are always included, with any residual financial data removed so that the resource conforms to the CARIN BB 2.x Non-Financial Basis profile.
+ ExplanationOfBenefit resources with a CARIN BB 2.x profile that contains financial data are excluded by default. When `_includeEOB2xWoFinancial=true` is set, they are included with financial data stripped and the resource is transformed to the corresponding Basis profile.
+ ExplanationOfBenefit resources with a PDex Prior Authorization profile are always included.

**Profile precedence for financial-data stripping**  
When an ExplanationOfBenefit resource declares multiple profiles, financial-data stripping takes precedence over pass-through. For a resource that declares both a Basis (or Financial) profile and a PDex Prior Authorization profile, the operation removes financial data before exporting the resource.

### Financial Data Transformation
<a name="davinci-data-export-financial-transformation"></a>

When you set `_includeEOB2xWoFinancial=true`, the operation transforms [CARIN BB 2.x](https://hl7.org/fhir/us/carin-bb/) ExplanationOfBenefit resources to their corresponding Basis profiles by removing financial data. For example, a `C4BB ExplanationOfBenefit Oral` resource is transformed to `C4BB ExplanationOfBenefit Oral Basis`, which strips financial data from the record per the FHIR specification.

The operation removes the following financial data elements in two scenarios: when it transforms a CARIN BB 2.x Financial resource to its Basis profile (using `_includeEOB2xWoFinancial=true`), and when it removes residual financial data from a CARIN BB 2.x Basis resource:
+ The `total` element
+ The `payment` element
+ The `benefitPeriod` element
+ The `benefitBalance` element
+ The `adjudication` amount entries (the `amount` slice; non-financial entries such as `benefitpaymentstatus` and `billingnetworkstatus` are preserved)
+ The `item.net` element
+ The `item.unitPrice` element
+ The `item.adjudication` amount entries

The operation also updates profile metadata during transformation:
+ `meta.profile` is updated to the Basis profile canonical URL
+ Version is updated to the CARIN BB 2.x Basis version
+ Existing resources in the data store are not modified
+ Exported resources are not persisted back to the data store

### Profile Detection Rules
<a name="davinci-data-export-profile-detection"></a>

The operation uses the following rules to detect and validate profiles:
+ Version detection is based on the `meta.profile` canonical URLs
+ A resource is included if ANY of its declared profiles match the export criteria
+ Profile validation occurs during export processing

## Temporal filtering for PDex exports
<a name="davinci-data-export-temporal-filtering"></a>

HealthLake applies a 5-year temporal filter for the Payer-to-Payer (`hl7.fhir.us.davinci-pdex.p2p`) and Member Access (`hl7.fhir.us.davinci-pdex.member`) export types. The filter is based on when the resource was last updated. The Provider Access export types (`hl7.fhir.us.davinci-pdex` and `hl7.fhir.us.davinci-pdex#provider-snapshot`) are not subject to any temporal limit. For the temporally limited export types, the filter applies to all resources except the following core attribution resource types, which are always exported regardless of age:
+ `Patient`
+ `Coverage`
+ `Organization`
+ `Practitioner`
+ `PractitionerRole`
+ `RelatedPerson`
+ `Location`
+ `Group`

These administrative and demographic resources are exempt because they provide essential context for the exported data. ATR exports are not subject to any temporal filtering.

## Sample Requests
<a name="davinci-data-export-examples"></a>

The following examples show how to start export jobs for different export types.

*ATR export*

```
GET https://healthlake.{region}.amazonaws.com/datastore/{datastoreId}/r4/Group/example-group/$davinci-data-export?_type=Group,Patient,Coverage,Practitioner,Organization&exportType=hl7.fhir.us.davinci-atr

POST https://healthlake.{region}.amazonaws.com/datastore/{datastoreId}/r4/Group/example-group/$davinci-data-export?_type=Group,Patient,Coverage,Practitioner,Organization&exportType=hl7.fhir.us.davinci-atr
Content-Type: application/json

{
  "DataAccessRoleArn": "arn:aws:iam::444455556666:role/your-healthlake-service-role",
  "JobName": "attribution-export-job",
  "OutputDataConfig": {
    "S3Configuration": {
      "S3Uri": "s3://your-export-bucket/EXPORT-JOB",
      "KmsKeyId": "arn:aws:kms:region:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    }
  }
}
```

*Provider Access export with ExplanationOfBenefit financial data removal*

```
GET https://healthlake.{region}.amazonaws.com/datastore/{datastoreId}/r4/Group/example-group/$davinci-data-export?_type=Patient,Observation,Condition,MedicationRequest,ExplanationOfBenefit&exportType=hl7.fhir.us.davinci-pdex&_includeEOB2xWoFinancial=true
```

*Provider Access snapshot export*

```
GET https://healthlake.{region}.amazonaws.com/datastore/{datastoreId}/r4/Group/example-group/$davinci-data-export?exportType=hl7.fhir.us.davinci-pdex%23provider-snapshot
```

*Payer-to-Payer export*

```
GET https://healthlake.{region}.amazonaws.com/datastore/{datastoreId}/r4/Group/example-group/$davinci-data-export?_type=Patient,Coverage,ExplanationOfBenefit,Condition,Procedure&exportType=hl7.fhir.us.davinci-pdex.p2p&_includeEOB2xWoFinancial=true
```

*Member Access export for a specific patient*

```
GET https://healthlake.{region}.amazonaws.com/datastore/{datastoreId}/r4/Group/example-group/$davinci-data-export?_type=Patient,Observation,Condition,ExplanationOfBenefit,MedicationRequest&exportType=hl7.fhir.us.davinci-pdex.member&patient=Patient/example-patient-id
```

## Sample Response
<a name="davinci-data-export-sample-response"></a>

```
{
  "datastoreId": "eaee622d8406b41eb86c0f4741201ff9",
  "jobStatus": "SUBMITTED",
  "jobId": "48d7b91dae4a64d00d54b70862f33f61"
}
```

## Resource Relationships
<a name="davinci-data-export-resource-relationships"></a>

The operation exports resources based on their relationships within the Member Attribution List:

```
Group (Attribution List)
├── Patient (Members)
├── Coverage → RelatedPerson (Subscribers)
├── Practitioner (Attributed Providers)
├── PractitionerRole → Location
└── Organization (Attributed Providers)
```

**Note**  
The preceding resource relationship diagram applies to ATR exports. For PDex exports, clinical and claims resources are automatically discovered through patient search and do not require explicit references in the Group resource.

### Resource Sources
<a name="davinci-data-export-resource-sources"></a>


| Resource | Source Location | Description | 
| --- | --- | --- | 
| Patient | Group.member.entity | The patients who are members of the attribution list | 
| Coverage | Group.member.extension:coverageReference | Coverage that resulted in patient membership | 
| Organization | Group.member.extension:attributedProvider | Organizations that patients are attributed to | 
| Practitioner | Group.member.extension:attributedProvider | Individual practitioners that patients are attributed to | 
| PractitionerRole | Group.member.extension:attributedProvider | Practitioner roles that patients are attributed to | 
| RelatedPerson | Coverage.subscriber | Subscribers of the coverage | 
| Location | PractitionerRole.location | Locations associated with practitioner roles | 
| Group | Input endpoint | The attribution list itself | 

## Job Management
<a name="davinci-data-export-job-management"></a>

Check Job Status  
`GET [base]/export/[job-id]`

Cancel Job  
`DELETE [base]/export/[job-id]`

### Job Lifecycle
<a name="davinci-data-export-job-lifecycle"></a>
+ `SUBMITTED` - Job has been received and queued
+ `IN_PROGRESS` - Job is actively processing
+ `COMPLETED` - Job finished successfully, files available for download
+ `FAILED` - Job encountered an error

## Output Format
<a name="davinci-data-export-output-format"></a>
+ *File Format*: NDJSON (Newline Delimited JSON)
+ *File Organization*: Separate files for each resource type
+ *File Extension*: .ndjson
+ *Location*: Specified S3 bucket and path

## Error Handling
<a name="davinci-data-export-error-handling"></a>

The operation returns HTTP 400 Bad Request with an OperationOutcome for the following conditions:

Authorization Errors  
The IAM role specified in `DataAccessRoleArn` does not have sufficient permissions to perform the export operation. For the complete list of required S3 and KMS permissions, see [Setting up permissions for export jobs](getting-started-setting-up.md#setting-up-export-permissions).

Parameter Validation Errors  
+ The `patient` parameter is not formatted as `Patient/id,Patient/id,...`
+ One or more patient references are invalid or do not belong to the specified Group
+ The `exportType` parameter value is not a supported export type
+ The `_type` parameter contains resource types that are not supported for the specified export type
+ The `_type` parameter is missing required resource types (`Group`, `Patient`, `Coverage`) for the `hl7.fhir.us.davinci-atr` export type
+ The `_includeEOB2xWoFinancial` parameter value is not a valid boolean

Resource Validation Errors  
+ The specified Group resource does not exist in the data store
+ The specified Group resource has no members
+ One or more Group members reference Patient resources that do not exist in the data store

## Security and Authorization
<a name="davinci-data-export-security"></a>

`$davinci-data-export` is a backend bulk operation authorized through IAM permissions or system-level SMART on FHIR (OAuth 2.0) scopes; requests presenting patient- or user-level scopes are rejected. The operation does not evaluate FHIR Consent resources to filter or restrict the exported data.
+ Standard FHIR authorization mechanisms apply
+ The data access role must have the required IAM permissions for S3 and KMS operations. For the complete list of required permissions, see [Setting up permissions for export jobs](getting-started-setting-up.md#setting-up-export-permissions).

## Best Practices
<a name="davinci-data-export-best-practices"></a>
+ *Resource Type Selection*: Only request the resource types you need to minimize export size and processing time
+ *Time-Based Filtering*: Use the `_since` parameter for incremental exports
+ *Patient Filtering*: Use the `patient` parameter when you only need data for specific members
+ *Job Monitoring*: Regularly check job status for large exports
+ *Error Handling*: Implement proper retry logic for failed jobs
+ *Temporal Filter Awareness*: For Payer-to-Payer and Member Access exports, consider the 5-year temporal filter when you select resource types
+ *Financial Data Removal*: Use `_includeEOB2xWoFinancial=true` when you need claims data without financial information
+ *Profile Management*: Ensure resources have appropriate profile declarations, validate against target profiles before ingestion, and use profile versioning to control export behavior

## Limitations
<a name="davinci-data-export-limitations"></a>
+ Maximum of 500 patients can be specified in the `patient` parameter
+ Export is limited to Group-level operations only
+ Only supports the predefined set of resource types for each export type
+ Output is always in NDJSON format
+ Payer-to-Payer and Member Access exports are limited to 5 years of clinical and claims data
+ Financial data transformation only applies to CARIN BB 2.x ExplanationOfBenefit profiles

## Additional Resources
<a name="davinci-data-export-additional-resources"></a>
+ [Da Vinci Member Attribution List IG](https://build.fhir.org/ig/HL7/davinci-atr/)
+ [Da Vinci Payer Data Exchange IG](https://hl7.org/fhir/us/davinci-pdex/)
+ [CARIN Consumer Directed Payer Data Exchange IG](https://build.fhir.org/ig/HL7/carin-bb/)
+ [US Core Implementation Guide](https://www.hl7.org/fhir/us/core/)
+ [FHIR Bulk Data Access Specification](https://hl7.org/fhir/uv/bulkdata/)