

# Supported resource types and identifiers
<a name="resource-matching-supported-types"></a>

Resource matching supports seven FHIR R4 resource types. For each type, it matches on the following identifiers. Identifiers not listed here are not used for matching.

## Patient and RelatedPerson
<a name="resource-matching-supported-types-patient"></a>


**Patient and RelatedPerson identifiers**  

| Identifier | Scope | 
| --- | --- | 
| Social Security Number (SSN) | Globally unique | 
| Medicare HIC | Globally unique | 
| Medicare MBI | Globally unique | 
| Driver's license | Scoped to the issuing state | 
| Medical record number (MRN) | Scoped to the issuing system | 
| Passport number | Scoped to the issuing country | 

## Practitioner and PractitionerRole
<a name="resource-matching-supported-types-practitioner"></a>


**Practitioner and PractitionerRole identifiers**  

| Identifier | Scope | 
| --- | --- | 
| National Provider Identifier (NPI) | Globally unique | 
| Tax ID (EIN) | Globally unique | 
| DEA number | Globally unique | 
| NCSBN ID | Globally unique | 
| Medical license number | Scoped to the issuing state | 

## Organization
<a name="resource-matching-supported-types-organization"></a>


**Organization identifiers**  

| Identifier | Scope | 
| --- | --- | 
| National Provider Identifier (NPI) | Globally unique | 
| Tax ID (EIN) | Globally unique | 
| CLIA number | Globally unique | 
| CMS Certification Number (CCN) | Globally unique | 
| Global Location Number (GLN) | Globally unique | 

## Location
<a name="resource-matching-supported-types-location"></a>


**Location identifiers**  

| Identifier | Scope | 
| --- | --- | 
| National Provider Identifier (NPI) | Globally unique | 
| Global Location Number (GLN) | Globally unique | 
| CMS Certification Number (CCN) | Globally unique | 

## Device
<a name="resource-matching-supported-types-device"></a>


**Device identifiers**  

| Identifier | Scope | 
| --- | --- | 
| Unique Device Identifier (UDI) | Globally unique | 
| Serial number | Scoped to the manufacturer | 