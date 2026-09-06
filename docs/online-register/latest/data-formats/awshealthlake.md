

# Data retrieval APIs for AWS HealthLake
<a name="awshealthlake"></a>

AWS HealthLake provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="healthlake-DescribeDataTransformationJob"></a>[DescribeDataTransformationJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeDataTransformationJob.html) | Describe a data transformation job | Read | 
| <a name="healthlake-DescribeFHIRBulkDeleteJob"></a>[DescribeFHIRBulkDeleteJob](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-bulk-delete.html) | Describe a FHIR Bulk Delete Job | Read | 
| <a name="healthlake-DescribeFHIRBulkMemberMatchJob"></a>[DescribeFHIRBulkMemberMatchJob](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-bulk-member-match.html) | Describe a FHIR Bulk Member Match Job | Read | 
| <a name="healthlake-DescribeFHIRDatastore"></a>[DescribeFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeFHIRDatastore.html) | Get the properties associated with the FHIR datastore, including the datastore ID, datastore ARN, datastore name, datastore status, created at, datastore type version, and datastore endpoint | Read | 
| <a name="healthlake-DescribeFHIRExportJob"></a>[DescribeFHIRExportJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeFHIRExportJob.html) | Display the properties of a FHIR export job, including the ID, ARN, name, and the status of the datastore | Read | 
| <a name="healthlake-DescribeFHIRExportJobWithGet"></a>[DescribeFHIRExportJobWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/export-datastore-rest.html) | Display the properties of a FHIR export job, including the ID, ARN, name, and the status of the datastore with Get | Read | 
| <a name="healthlake-DescribeFHIRImportJob"></a>[DescribeFHIRImportJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeFHIRImportJob.html) | Display the properties of a FHIR import job, including the ID, ARN, name, and the status of the datastore | Read | 
| <a name="healthlake-ExpandValueSetWithGet"></a>[ExpandValueSetWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-expand.html) | Search and expand ValueSet resource | Read | 
| <a name="healthlake-ExpandValueSetWithPost"></a>[ExpandValueSetWithPost](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-expand.html) | Search and expand ValueSet resource | Read | 
| <a name="healthlake-GetCapabilities"></a>[GetCapabilities](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html) | Get the capabilities of a FHIR datastore | Read | 
| <a name="healthlake-GetDataTransformationProfile"></a>[GetDataTransformationProfile](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_GetDataTransformationProfile.html) | Retrieve a data transformation profile and its content | Read | 
| <a name="healthlake-GetExportedFile"></a>[GetExportedFile](https://docs.aws.amazon.com/healthlake/latest/devguide/export-datastore-rest.html) | Access exported files from a FHIR Export job initiated with Get | Read | 
| <a name="healthlake-GetHistoryByResourceId"></a>[GetHistoryByResourceId](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html) | Read resource history | Read | 
| <a name="healthlake-InquirePreAuthClaim"></a>[InquirePreAuthClaim](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-inquire.html) | Inquire about the status of a prior authorization Claim | Read | 
| <a name="healthlake-ListDataTransformationJobs"></a>[ListDataTransformationJobs](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListDataTransformationJobs.html) | List data transformation jobs in the account | List | 
| <a name="healthlake-ListDataTransformationProfileVersions"></a>[ListDataTransformationProfileVersions](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListDataTransformationProfileVersions.html) | List all versions of a data transformation profile | List | 
| <a name="healthlake-ListDataTransformationProfiles"></a>[ListDataTransformationProfiles](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListDataTransformationProfiles.html) | List data transformation profiles in the account | List | 
| <a name="healthlake-ListFHIRDatastores"></a>[ListFHIRDatastores](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListFHIRDatastores.html) | List all FHIR datastores that are in the user's account, regardless of datastore status | List | 
| <a name="healthlake-ListFHIRExportJobs"></a>[ListFHIRExportJobs](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListFHIRExportJobs.html) | Get a list of export jobs for the specified datastore | List | 
| <a name="healthlake-ListFHIRImportJobs"></a>[ListFHIRImportJobs](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListFHIRImportJobs.html) | Get a list of import jobs for the specified datastore | List | 
| <a name="healthlake-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListTagsForResource.html) | Get a list of tags for the specified datastore | List | 
| <a name="healthlake-LookupCodeSystemWithGet"></a>[LookupCodeSystemWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-lookup.html) | Retrieve Codes for a CodeSystem resource | Read | 
| <a name="healthlake-LookupCodeSystemWithPost"></a>[LookupCodeSystemWithPost](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-lookup.html) | Retrieve Codes for a CodeSystem resource | Read | 
| <a name="healthlake-QuestionnairePackage"></a>[QuestionnairePackage](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-questionnaire-package.html) | Retrieve Questionnaire packages with dependency Library and ValueSet resources | Read | 
| <a name="healthlake-ReadResource"></a>[ReadResource](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html) | Read resource | Read | 
| <a name="healthlake-SearchEverything"></a>[SearchEverything](https://docs.aws.amazon.com/healthlake/latest/devguide/search-healthlake.html) | Search all resources related to a patient | Read | 
| <a name="healthlake-SearchWithGet"></a>[SearchWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/search-healthlake.html) | Search resources with GET method | Read | 
| <a name="healthlake-SearchWithPost"></a>[SearchWithPost](https://docs.aws.amazon.com/healthlake/latest/devguide/search-healthlake.html) | Search resources with POST method | Read | 
| <a name="healthlake-TranslateConceptMapWithGet"></a>[TranslateConceptMapWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-translate.html) | Translate a code from one value set to another using a ConceptMap resource with GET method | Read | 
| <a name="healthlake-TranslateConceptMapWithPost"></a>[TranslateConceptMapWithPost](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-translate.html) | Translate a code from one value set to another using a ConceptMap resource with POST method | Read | 
| <a name="healthlake-ValidateResource"></a>[ValidateResource](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-validate.html) | Validate a resource | Read | 
| <a name="healthlake-ValidateSource"></a>[ValidateSource](https://docs.aws.amazon.com/healthlake/latest/devguide/data-transformation-features.html) | Validate source data against format specifications | Read | 
| <a name="healthlake-VersionReadResource"></a>[VersionReadResource](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html) | Read version of a resource | Read | 