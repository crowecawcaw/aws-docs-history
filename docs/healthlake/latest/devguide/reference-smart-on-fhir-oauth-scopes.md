# SMART on FHIR OAuth 2.0 scopes

supported by HealthLake

HealthLake uses OAuth 2.0 as an authorization protocol. Using this protocol on your
authorization server allows you to define HealthLake data store permissions (create, read,
update, delete, and search) for FHIR resources that a client application has access
to.

The SMART on FHIR framework defines a set of scopes that can be requested from the
authorization server. For example, a client application that is only designed to allow
patients to view their lab results or view their contact details should only be
_authorized_ to request `read` scopes.

###### Note

HealthLake provides support for both SMART on FHIR V1 and V2 as described below. The
SMART on FHIR [`AuthorizationStrategy`](../APIReference/API_IdentityProviderConfiguration.md#HealthLake-Type-IdentityProviderConfiguration-AuthorizationStrategy "../APIReference/API_IdentityProviderConfiguration.md#HealthLake-Type-IdentityProviderConfiguration-AuthorizationStrategy") is set to one of the following three
values when your data store is created:

- `SMART_ON_FHIR_V1` – Support for only SMART on FHIR V1,
  which includes `read` (read/search) and `write`
  (create/update/delete) permissions.
- `SMART_ON_FHIR` – Support for both SMART on FHIR V1 and V2,
  which includes `create`, `read`, `update`,
  `delete`, and `search` permissions.
- `AWS_AUTH` – The default AWS HealthLake authorization strategy;
  not affiliated with SMART on FHIR.

## Standalone launch scope

HealthLake supports the standalone launch mode scope `launch/patient`.

In standalone launch mode a client application requests access to patient's clinical
data because the user and patient are not known to the client application. Thus, the
client application's authorization request explicitly requests the patient scope be
returned. After successful authentication, the authorization server issues a access
token containing the requested launch patient scope. The needed patient context is
provided alongside the access token in the authorization server's response.

| Supported launch mode scopes | Scope                                                                                                                          | Description |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `launch/patient`             | A parameter in a OAuth 2.0 authorization request requesting<br>that patient data be returned in the authorization<br>response. |

## SMART on FHIR resource scopes for

HealthLake

HealthLake defines three levels of SMART on FHIR resource scopes.

- `patient` scopes grant access to specific data about a single
  Patient.
- `user` scopes grant access to specific data that a user can
  access.
- `system` scopes grant access to all FHIR resources found in the
  HealthLake data store.

The following sections list the syntax for constructing FHIR resource scopes using
either SMART on FHIR V1 or SMART on FHIR V2.

###### Note

The SMART on FHIR authorization strategy is set when your data store is created.
For more information, see [`AuthorizationStrategy`](../APIReference/API_IdentityProviderConfiguration.md#HealthLake-Type-IdentityProviderConfiguration-AuthorizationStrategy "../APIReference/API_IdentityProviderConfiguration.md#HealthLake-Type-IdentityProviderConfiguration-AuthorizationStrategy") in the _AWS HealthLake API
Reference_.

### SMART on FHIR V1 scopes supported by

HealthLake

When using SMART on FHIR V1, the general syntax for constructing FHIR resource
scopes for HealthLake follows. To view the entire URL path in the following example,
scroll over the **Copy** button.

```
('patient' | 'user' | 'system') '/' (fhir-resource | '*') '.' ('read' | 'write' | '*')
```

| SMART on FHIR v1 supported authorization scopes | Scope syntax  | Example scope | Result       |
| ----------------------------------------------- | ------------- | ------------- | ------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `patient/(fhir-resource                         | '\*').('read' | 'write'       | <br>'\*')`   | `patient/AllergyIntolerance.*`                                                    | The patient client application has instance-level read/write<br>access to all recorded allergies. |
| `user/(fhir-resource                            | '\*').('read' | 'write'       | <br>'\*')`   | `user/Observation.read`                                                           | The user client application has instance-level read/write access<br>to all recorded observations. |
| `system/('read'                                 | 'write'       | \*)`          | `system/*.*` | The system client application has read/write access to all FHIR<br>resource data. |

### SMART on FHIR V2 scopes supported by

HealthLake

When using SMART on FHIR V2, the general syntax for constructing FHIR resource
scopes for HealthLake follows. To view the entire URL path in the following example,
scroll over the **Copy** button.

```
('patient' | 'user' | 'system') '/' (fhir-resource | '*') '.' ('c' | 'r' | 'u' | 'd' | 's')
```

###### Note

To use SMART on FHIR V2, you must pass in the value [`permission-v2`](https://hl7.org/fhir/smart-app-launch/STU2/conformance.html#permissions "https://hl7.org/fhir/smart-app-launch/STU2/conformance.html#permissions") into the metadata
`capabilities` string, which is a member of the [`IdentityProviderConfiguration`](../APIReference/API_IdentityProviderConfiguration.md "../APIReference/API_IdentityProviderConfiguration.md") data type.

HealthLake supports granular scopes. For more information, see [supported granular scopes](https://hl7.org/fhir/us/core/scopes.html#the-following-granular-scopes-shall-be-supported "https://hl7.org/fhir/us/core/scopes.html#the-following-granular-scopes-shall-be-supported") in the _FHIR US Core
Implementation Guide_.

| SMART on FHIR V2 supported authorization scopes | Scope syntax            | Example V1 scope                                                                                             | Result |
| ----------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| `patient/Observation.rs`                        | `user/Observation.read` | Permission to read and search `Observation` resource<br>for the current patient.                             |
| `system/*.cruds`                                | `system/*.*`            | The system client application has full<br>create/read/update/delete/search access to all FHIR resource data. |
