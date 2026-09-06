

# CMS compliance features
<a name="reference-compliance-cms"></a>

AWS HealthLake provides features to help you meet CMS (Centers for Medicare & Medicaid Services) interoperability and compliance requirements. These features enable you to track API usage by CMS category and subsequently report usage metrics for compliance purposes.

**Topics**
+ [CMS interoperability endpoints](#cms-interoperability-endpoints)
+ [Enhanced CloudWatch metrics for CMS compliance](#cms-cloudwatch-metrics)

## CMS interoperability endpoints
<a name="cms-interoperability-endpoints"></a>

### Overview
<a name="cms-endpoints-overview"></a>

HealthLake provides four CMS interoperability endpoints that correspond to the CMS-mandated API categories. The underlying base URL of your HealthLake data store does not change. These endpoints simply provide a way to categorize and track your API calls for CMS reporting purposes.

### Purpose
<a name="cms-endpoints-purpose"></a>

The primary purpose of these interoperability endpoints is to enable customers to:
+ **Easily track** API transactions by CMS category
+ **Automatically report** usage metrics for CMS compliance
+ **Maintain** existing FHIR workflows with minimal changes

All API calls function identically whether you use the interoperability endpoint or the standard FHIR endpoint—the only difference is how the transactions are categorized in CloudWatch metrics.

### Supported CMS interoperability endpoints
<a name="cms-supported-endpoints"></a>


| CMS Category | Interoperability Endpoint | Example Usage | 
| --- | --- | --- | 
| Patient Access | /patientaccess/v2/r4 | baseURL/patientaccess/v2/r4/Patient/123 | 
| Provider Access | /​provideraccess/v2/r4 | baseURL/​provideraccess/v2/r4/Observation?patient=123 | 
| Payer to Payer | /payertopayerdx/v2/r4 | baseURL/payertopayerdx/v2/r4/Practitioner/456 | 
| Prior Auth Service | /priorauthservice/v2/r4 | baseURL/priorauthservice/v2/r4/ExplanationOfBenefit?patient=789 | 

### How interoperability endpoints work
<a name="cms-endpoints-how-it-works"></a>

**Standard HealthLake API Call:**

```
baseURL/resourceType/[id]
baseURL/resourceType?[parameters]
```

**With CMS Interoperability Endpoint:**

```
baseURL/interoperability-endpoint/resourceType/[id]
baseURL/interoperability-endpoint/resourceType?[parameters]
```

The interoperability endpoint path is simply inserted between your base URL and the resource type. Everything after the interoperability endpoint path remains exactly the same as your current API calls.

### Usage examples
<a name="cms-endpoints-examples"></a>

#### Example 1: Patient Access API
<a name="cms-example-patient-access"></a>

**Current API call (still works):**

```
curl -X GET \
  https://healthlake.us-east-1.amazonaws.com/datastore/abc123/r4/Patient/123 \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/fhir+json"
```

**With Patient Access interoperability endpoint (for CMS tracking):**

```
curl -X GET \
  https://healthlake.us-east-1.amazonaws.com/datastore/abc123/patientaccess/v2/r4/Patient/123 \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/fhir+json"
```

**Key Points:**
+ Base URL remains: `https://healthlake.us-east-1.amazonaws.com/datastore/abc123`
+ Interoperability endpoint inserted: `/patientaccess/v2/r4`
+ Resource path unchanged: `/Patient/123`
+ **Both calls return identical responses**
+ The interoperability endpoint call is automatically tracked under `URIType=patient-access` in CloudWatch
+ POST, PUT, PATCH, DELETE operations work identically.
+ Request body remains unchanged.

### Endpoint translation reference
<a name="cms-endpoint-translation"></a>


| Interoperability Endpoint | Translates To | CMS Category | 
| --- | --- | --- | 
| baseURL/patientaccess/v2/r4/Patient | baseURL/r4/Patient | Patient Access | 
| baseURL/​provideraccess/v2/r4/Observation | baseURL/r4/Observation | Provider Access | 
| baseURL/payertopayerdx/v2/r4/Practitioner/456 | baseURL/r4/Practitioner/456 | Payer to Payer Data Exchange | 
| baseURL/priorauthservice/v2/r4/ExplanationOfBenefit?patient=789 | baseURL/r4/ExplanationOfBenefit?patient=789 | Prior Authorization | 

### Important notes
<a name="cms-endpoints-important-notes"></a>
+ **No Functional Difference**: Interoperability endpoints and standard FHIR endpoints return identical responses and support identical operations
+ **Base URL Unchanged**: Your HealthLake data store endpoint remains the same
+ **Simple Integration**: Insert the interoperability endpoint path between your base URL and resource type
+ **Automatic Tracking**: CloudWatch metrics automatically categorize calls by interoperability endpoint used
+ **Backward Compatible**: Existing API calls without interoperability endpoints continue to work normally

## Enhanced CloudWatch metrics for CMS compliance
<a name="cms-cloudwatch-metrics"></a>

### Overview
<a name="cms-metrics-overview"></a>

When you use the CMS interoperability endpoints, HealthLake automatically emits enhanced CloudWatch metrics with additional dimensions to support CMS reporting requirements. These metrics track API usage by caller identity, application, and CMS-specific URI types **without any additional configuration required**.

### How it works
<a name="cms-metrics-how-it-works"></a>

When you make an API call using an interoperability endpoint:

```
# This call...
curl https://healthlake.us-east-1.amazonaws.com/datastore/abc123/patientaccess/v2/r4/Patient/123

# Automatically generates metrics with:
# - URIType: "patient-access"
# - Sub: extracted from your bearer token (SMART on FHIR datastores only)
# - ClientId: extracted from your bearer token (SMART on FHIR datastores only)
# - Plus all standard dimensions (DatastoreId, Operation, etc.)
```

**No additional code or configuration is needed.** Simply use the interoperability endpoints, and the enhanced metrics are automatically captured.

**Note**  
For non-SMART on FHIR data stores, the `URIType` dimension is still captured, allowing you to track API usage by CMS category. The `Sub` and `ClientId` dimensions are only available when using SMART on FHIR authentication with bearer tokens containing these claims.

### New metric dimensions
<a name="cms-metrics-dimensions"></a>

In addition to existing dimensions (`DatastoreId`, `DatastoreType`, `Operation`), the following dimensions are automatically added when using interoperability endpoints:


| Dimension | Description | Example Values | Source | 
| --- | --- | --- | --- | 
| URIType | CMS compliance category | patient-access, provider-access, payer-to-payer, prior-authorization | Automatically determined from interoperability endpoint path | 
| Sub | Caller identity | User/entity identifier | Extracted from bearer token sub claim | 
| ClientId | Application identifier | portal\_app, ehr\_system | Extracted from bearer token client\_id claim | 

### Available metrics
<a name="cms-available-metrics"></a>

All existing HealthLake metrics now include the additional dimensions when using interoperability endpoints:
+ **CallCount** - Total number of API calls
+ **Latency** - API response time in milliseconds
+ **UserErrors** - Count of 4xx client errors
+ **SystemErrors** - Count of 5xx server errors
+ **Throttles** - Count of throttled requests
+ **SuccessfulRequests** - Count of successful API calls

### Querying metrics in CloudWatch
<a name="cms-querying-metrics"></a>

#### CloudWatch Insights query example
<a name="cms-cloudwatch-insights-example"></a>

**Query all Patient Access API calls by application:**

```
SELECT SUM(CallCount)
FROM "AWS/HealthLake"
WHERE DatastoreId = '75c1cf9b0d71cd38fec8f7fb317c4c1a'
    AND URIType = 'patient-access'
GROUP BY ClientId
```