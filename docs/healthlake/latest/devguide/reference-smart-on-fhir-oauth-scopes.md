

# SMART on FHIR OAuth 2.0 scopes supported by HealthLake
<a name="reference-smart-on-fhir-oauth-scopes"></a>

HealthLake uses OAuth 2.0 as an authorization protocol. Using this protocol on your authorization server allows you to define HealthLake data store permissions (create, read, update, delete, and search) for FHIR resources that a client application has access to.

The SMART on FHIR framework defines a set of scopes that can be requested from the authorization server. For example, a client application that is only designed to allow patients to view their lab results or view their contact details should only be *authorized* to request `read` scopes.

**Note**  
HealthLake provides support for both SMART on FHIR V1 and V2 as described below. The SMART on FHIR [`AuthorizationStrategy`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html#HealthLake-Type-IdentityProviderConfiguration-AuthorizationStrategy) is set to one of the following three values when your data store is created:  
`SMART_ON_FHIR_V1` – Support for only SMART on FHIR V1, which includes `read` (read/search) and `write` (create/update/delete) permissions.
`SMART_ON_FHIR` – Support for both SMART on FHIR V1 and V2, which includes `create`, `read`, `update`, `delete`, and `search` permissions.
`AWS_AUTH` – The default AWS HealthLake authorization strategy; not affiliated with SMART on FHIR.

## Standalone launch scope
<a name="smart-on-fhir-scopes-launch"></a>

HealthLake supports the standalone launch mode scope `launch/patient`.

In standalone launch mode a client application requests access to patient's clinical data because the user and patient are not known to the client application. Thus, the client application's authorization request explicitly requests the patient scope be returned. After successful authentication, the authorization server issues a access token containing the requested launch patient scope. The needed patient context is provided alongside the access token in the authorization server's response.


**Supported launch mode scopes**  

| Scope | Description | 
| --- | --- | 
| `launch/patient` | A parameter in a OAuth 2.0 authorization request requesting that patient data be returned in the authorization response. | 

## SMART on FHIR resource scopes for HealthLake
<a name="smart-on-fhir-scopes-rest"></a>

HealthLake defines three levels of SMART on FHIR resource scopes.
+ `patient` scopes grant access to specific data about a single Patient.
+ `user` scopes grant access to specific data that a user can access.
+ `system` scopes grant access to all FHIR resources found in the HealthLake data store.

The following sections list the syntax for constructing FHIR resource scopes using either SMART on FHIR V1 or SMART on FHIR V2.

**Note**  
The SMART on FHIR authorization strategy is set when your data store is created. For more information, see [`AuthorizationStrategy`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html#HealthLake-Type-IdentityProviderConfiguration-AuthorizationStrategy) in the *AWS HealthLake API Reference*.

### SMART on FHIR V1 scopes supported by HealthLake
<a name="reference-smart-on-fhir-v1"></a>

When using SMART on FHIR V1, the general syntax for constructing FHIR resource scopes for HealthLake follows. To view the entire URL path in the following example, scroll over the **Copy** button.

```
('patient' | 'user' | 'system') '/' (fhir-resource | '*') '.' ('read' | 'write' | '*')
```


**SMART on FHIR v1 supported authorization scopes**  

| Scope syntax | Example scope | Result | 
| --- | --- | --- | 
| `patient/(fhir-resource \| '*').('read' \| 'write' \| '*')` | patient/AllergyIntolerance.\* | The patient client application has instance-level read/write access to all recorded allergies. | 
| `user/(fhir-resource \| '*').('read' \| 'write' \| '*')` | user/Observation.read | The user client application has instance-level read/write access to all recorded observations.  | 
| system/('read' \| 'write' \| \*) | system/\*.\* | The system client application has read/write access to all FHIR resource data. | 

### SMART on FHIR V2 scopes supported by HealthLake
<a name="reference-smart-on-fhir-v2"></a>

When using SMART on FHIR V2, the general syntax for constructing FHIR resource scopes for HealthLake follows. To view the entire URL path in the following example, scroll over the **Copy** button.

```
('patient' | 'user' | 'system') '/' (fhir-resource | '*') '.' ('c' | 'r' | 'u' | 'd' | 's')
```

**Note**  
To use SMART on FHIR V2, you must pass in the value [`permission-v2`](https://hl7.org/fhir/smart-app-launch/STU2/conformance.html#permissions) into the metadata `capabilities` string, which is a member of the [`IdentityProviderConfiguration`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html) data type.  
HealthLake supports granular scopes. For more information, see [supported granular scopes](https://hl7.org/fhir/us/core/scopes.html#the-following-granular-scopes-shall-be-supported) in the *FHIR US Core Implementation Guide*.


**SMART on FHIR V2 supported authorization scopes**  

| Scope syntax | Example V1 scope | Result | 
| --- | --- | --- | 
| `patient/Observation.rs` | user/Observation.read | Permission to read and search Observation resource for the current patient. | 
| `system/*.cruds` | system/\*.\* | The system client application has full create/read/update/delete/search access to all FHIR resource data.  | 

### SMART on FHIR V2.2 scopes supported by HealthLake
<a name="reference-smart-on-fhir-v2-2"></a>

V2.2 extends V2 scopes with search-parameter–based filtering. Authorization servers can now issue scopes that restrict access by specific data characteristics and not just by resource type and CRUDS operation.

Everything from V2 remains unchanged. V2.2 is purely additive:
+ Existing V2 scopes (without filters) continue to work as before.
+ The V2 grammar is extended with an optional `?param=value` query string.
+ No changes to scope levels (`patient`/`user`/`system`), resource types, or CRUDS letters.

#### Prerequisites
<a name="smart-on-fhir-v2-2-prerequisites"></a>

Before enabling SMART on FHIR V2.2, ensure the following:
+ Your data store was created with `AuthorizationStrategy` set to `SMART_ON_FHIR` (supports both V1 and V2). Data stores using `SMART_ON_FHIR_V1` or `AWS_AUTH` are not eligible.
+ Your data store already includes `permission-v2` in the `capabilities` array. V2.2 is additive as it extends V2 and cannot be used standalone.
+ Your IDP Lambda is configured to validate and pass through the V2.2 scope format (scopes containing `?` query syntax).

#### Enabling V2.2
<a name="smart-on-fhir-v2-2-enabling"></a>

The enablement path depends on whether you are creating a new data store or updating an existing one.

##### New data stores
<a name="smart-on-fhir-v2-2-new-data-stores"></a>

When creating a new data store, add `permission-v2.2` to the `capabilities` array in the `Metadata` field of your [`IdentityProviderConfiguration`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html):

```
"capabilities": [
  "launch-ehr",
  "sso-openid-connect",
  "client-public",
  "permission-v2",
  "permission-v2.2"
]
```

##### Existing data stores
<a name="smart-on-fhir-v2-2-existing-data-stores"></a>

To enable SMART on FHIR V2.2 on an existing data store, add `permission-v2.2` to the `capabilities` array in the `Metadata` field of your [`IdentityProviderConfiguration`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html) and submit the change with `UpdateFHIRDatastore`. For more information, see [Updating a HealthLake data store](managing-data-stores-update.md).

Requirements:
+ `permission-v2` must remain in the array. V2.2 extends V2 and can't be used on its own.
+ `AuthorizationStrategy` must be `SMART_ON_FHIR` (not `SMART_ON_FHIR_V1` or `AWS_AUTH`).
+ Updating the identity provider configuration replaces it in full, so include all existing fields and capabilities along with `permission-v2.2`.

The change takes effect immediately, with no downtime. To verify, fetch the [Discovery Document](reference-smart-on-fhir-discovery-document.md) (requires SigV4):

```
GET {healthlake-endpoint}/r4/.well-known/smart-configuration
```

If the `capabilities` array in the response includes `permission-v2.2`, SMART on FHIR V2.2 is active.

#### Extended scope syntax
<a name="smart-on-fhir-v2-2-extended-scope-syntax"></a>

The V2 grammar is extended with an optional query string:

```
V2:   (patient|user|system) / resource . cruds
V2.2: (patient|user|system) / resource . cruds [? param=value [& param=value ...]]
```


**V2.2 scope query string components**  

| Component | Description | 
| --- | --- | 
| `?param=value` | Search-parameter filter. Only resources matching this criterion are accessible. | 
| `&param=value` | Additional filter. Multiple filters are ANDed – all must match. | 

Rules:
+ Filters only apply to the resource type specified in the scope. Wildcard (`*`) with filters is not supported.
+ Parameters must be valid for the resource type per your data store's search configuration (check via `GET /r4/metadata`).
+ The full scope string (for example, `patient/Observation.rs?category=laboratory`) is the literal value that appears in the OAuth 2.0 scope parameter and access token `scp` claim.
+ URL-encode special characters per [RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749) in authorization requests (for example, `|` → `%7C`).
+ For date, number, and quantity parameters, V2.2 supports prefix [comparators](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-search-parameters.html#search-comparators) (for example, `?date=eq2023-01-01`). V2.2 also supports [search parameter modifiers](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-search-parameters.html#search-parameter-modifiers).

#### Scope examples
<a name="smart-on-fhir-v2-2-scope-examples"></a>


**V2.2 scope examples**  

| Scope | Access granted | 
| --- | --- | 
| `patient/DiagnosticReport.rs?category=LAB` | Only `DiagnosticReport` resources where `category` is `LAB`. | 
| `patient/Observation.rs?_security=http://terminology.hl7.org/CodeSystem/v3-Confidentiality\|R` | Only `Observation` resources with security label `Restricted`. | 
| `patient/Observation.rs?date=ge2023-01-01` | Only `Observation` resources dated on or after January 1, 2023. | 
| `patient/Observation.rs?category=laboratory&status=final` | Only `Observation` resources that are lab AND final. | 
| `user/Condition.rs?clinical-status=active` | Only active `Condition` resources. | 

#### Enforcement behavior
<a name="smart-on-fhir-v2-2-enforcement"></a>

When a token includes V2.2 scopes, HealthLake applies filters per operation:


**V2.2 enforcement per operation**  

| Operation | Behavior | 
| --- | --- | 
| Read (`r`) | Succeeds only if the resource matches all scope filters. Otherwise returns 403. | 
| Search (`s`) | Scope filters are intersected with the query. Only matching resources are returned. | 
| Create/Update (`c`/`u`) | Resource must satisfy scope filters to be written. Otherwise returns 403. | 
| Delete (`d`) | Target resource must match scope filters. Otherwise returns 403. | 

##### Scope precedence
<a name="smart-on-fhir-v2-2-scope-precedence"></a>
+ Multiple V2.2 scopes for the same resource type are unioned (OR across scopes).
+ A broader V2 scope without filters (for example, `patient/Observation.rs`) grants full access regardless of any narrower V2.2 scopes in the same token.
+ V2.2 scopes on a data store without `permission-v2.2` enabled are silently ignored.

#### Limitations
<a name="smart-on-fhir-v2-2-limitations"></a>

The following are not supported in V2.2 scope filters:
+ Composite search parameters (for example, `code-value-quantity`).
+ Chained search parameters (for example, `subject:Patient.name=Smith`).
+ `_include` / `_revinclude` search parameters.
+ `$export` / `$davinci-data-export` (Bulk Data) – V2.2 filters do not apply; bulk export uses V2 scopes.
+ Wildcard resource type combined with filters (for example, `patient/*.rs?category=LAB` is invalid). You must specify an explicit resource type when using search-parameter filters (for example, `patient/Observation.rs?category=LAB`).


**Troubleshooting**  

| Symptom | Cause | Fix | 
| --- | --- | --- | 
| Token scope not recognized | V2.2 not enabled on data store | Check `/.well-known/smart-configuration` and request enablement via a support ticket. | 
| 403 on a resource that exists | Resource does not match scope filter | Verify resource values against scope parameters. | 
| Empty search results | Scope filter narrower than query | Results are the intersection of query and scope filters. | 
| `InvalidScope` error | Invalid search parameter in scope | Confirm parameter via `/metadata` CapabilityStatement. | 

#### End-to-end example
<a name="smart-on-fhir-v2-2-end-to-end-example"></a>

Scenario: A patient app should only show finalized lab results from 2023 onward.

1. Authorization server issues token with scope:

   ```
   patient/Observation.rs?category=laboratory&status=final&date=ge2023-01-01
   ```

1. Client calls HealthLake:

   ```
   GET {endpoint}/r4/Observation?patient=Patient/123
   ```

1. HealthLake enforces scope filters. The response contains only `Observation` resources where `category=laboratory` AND `status=final` AND `date ≥ 2023-01-01` – even though the client requested all Observations.