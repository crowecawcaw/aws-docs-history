# FHIR profile validations for

HealthLake

AWS HealthLake supports the base [FHIR R4
specification](https://hl7.org/fhir/R4 "https://hl7.org/fhir/R4"). Included in the base FHIR R4 specification are FHIR Profiles.
Profiles are used on a FHIR resource type to define a more specific resource type definition
using constraints and/or extensions on the base resource type. For example, a FHIR Profile can
identify mandatory fields such as extensions and value sets. A resource can support multiple
profiles. All HealthLake data stores support using FHIR Profiles.

###### Note

Adding a FHIR profile is _not_ required when adding data to a HealthLake
data store. If a FHIR profile is not specified when a resource is added or updated, the
resource is validated against only the base FHIR R4 schema.

FHIR profiles, to which FHIR resources conform to, are included in resources before
they are imported into HealthLake. Therefore, FHIR profiles are validated by HealthLake during
import.

FHIR Profiles are specified in an implementation guide. A FHIR Implementation Guide (IG)
is a set of instructions that describe how to use the FHIR standard for a specific purpose.
HealthLake validates FHIR Profiles defined in the following implementation guides.

| FHIR profiles supported by AWS HealthLake                          | Name         | Version                                                                                                                                                                                                                                                                                                                                                                | Implementation guide | Capability | US East (Ohio) | US East (N. Virginia) | US West (Oregon) | Asia Pacific (Mumbai) | Asia Pacific (Sydney) | Canada (Central) | Europe (Ireland) | Europe (London) |
| ------------------------------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ---------- | -------------- | --------------------- | ---------------- | --------------------- | --------------------- | ---------------- | ---------------- | --------------- |
| US Core                                                            | 3.1.1        | [http://hl7.org/fhir/us/core/STU3.1.1/](http://hl7.org/fhir/us/core/STU3.1.1/ "http://hl7.org/fhir/us/core/STU3.1.1/")                                                                                                                                                                                                                                                 | Default              | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| US Core                                                            | 4.0.0        | [https://hl7.org/fhir/us/core/STU4/index.html](https://hl7.org/fhir/us/core/STU4/index.html "https://hl7.org/fhir/us/core/STU4/index.html")                                                                                                                                                                                                                            | Supported            | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| US Core                                                            | 5.0.1        | [https://hl7.org/fhir/us/core/STU5.0.1/index.html](https://hl7.org/fhir/us/core/STU5.0.1/index.html "https://hl7.org/fhir/us/core/STU5.0.1/index.html")                                                                                                                                                                                                                | Supported            | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| US Core                                                            | 6.1.0        | [https://hl7.org/fhir/us/core/STU6.1/index.html](https://hl7.org/fhir/us/core/STU6.1/index.html "https://hl7.org/fhir/us/core/STU6.1/index.html")                                                                                                                                                                                                                      | Supported            | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| US Core                                                            | 7.0.0        | [https://hl7.org/fhir/us/core/STU7/](https://hl7.org/fhir/us/core/STU7/ "https://hl7.org/fhir/us/core/STU7/")                                                                                                                                                                                                                                                          | Supported            | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| UK Core                                                            | 2.0.1        | [https://simplifier.net/guide/uk-core-implementation-guide-stu2/Home/ProfilesandExtensions/ProfilesIndex?version=2.0.1](https://simplifier.net/guide/uk-core-implementation-guide-stu2/Home/ProfilesandExtensions/ProfilesIndex?version=2.0.1 "https://simplifier.net/guide/uk-core-implementation-guide-stu2/Home/ProfilesandExtensions/ProfilesIndex?version=2.0.1") | Supported            | X          | X              | X                     | X                |                       |                       | X                | X                |
| CARIN Blue Button                                                  | 1.1.0        | [http://hl7.org/fhir/us/carin-bb/STU1.1/](http://hl7.org/fhir/us/carin-bb/STU1.1/ "http://hl7.org/fhir/us/carin-bb/STU1.1/")                                                                                                                                                                                                                                           | Default              | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| CARIN Blue Button                                                  | 1.0.0        | [https://hl7.org/fhir/us/carin-bb/STU1/](https://hl7.org/fhir/us/carin-bb/STU1/ "https://hl7.org/fhir/us/carin-bb/STU1/")                                                                                                                                                                                                                                              | Supported            | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| Da Vinci Payer Data Exchange                                       | 1.0.0        | [https://hl7.org/fhir/us/davinci-pdex/](https://hl7.org/fhir/us/davinci-pdex/ "https://hl7.org/fhir/us/davinci-pdex/")                                                                                                                                                                                                                                                 | Default              | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| Da Vinci Health Record Exchange (HRex)                             | 0.2.0        | [https://hl7.org/fhir/us/davinci-hrex/2020Sep/](https://hl7.org/fhir/us/davinci-hrex/2020Sep/ "https://hl7.org/fhir/us/davinci-hrex/2020Sep/")                                                                                                                                                                                                                         | Default              | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| DaVinci PDEX Plan Net                                              | 1.1.0        | [https://hl7.org/fhir/us/davinci-pdex-plan-net/STU1.1/](https://hl7.org/fhir/us/davinci-pdex-plan-net/STU1.1/ "https://hl7.org/fhir/us/davinci-pdex-plan-net/STU1.1/")                                                                                                                                                                                                 | Default              | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| DaVinci PDEX Plan Net                                              | 1.0.0        | [https://hl7.org/fhir/us/davinci-pdex-plan-net/STU1/](https://hl7.org/fhir/us/davinci-pdex-plan-net/STU1/ "https://hl7.org/fhir/us/davinci-pdex-plan-net/STU1/")                                                                                                                                                                                                       | Supported            | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| DaVinci Payer Data Exchange (PDex) US Drug Formulary               | 1.1.0        | [https://hl7.org/fhir/us/davinci-drug-formulary/STU1.1/](https://hl7.org/fhir/us/davinci-drug-formulary/STU1.1/ "https://hl7.org/fhir/us/davinci-drug-formulary/STU1.1/")                                                                                                                                                                                              | Default              | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| DaVinci Payer Data Exchange (PDex) US Drug Formulary               | 1.0.1        | [https://hl7.org/fhir/us/davinci-drug-formulary/STU1.0.1/](https://hl7.org/fhir/us/davinci-drug-formulary/STU1.0.1/ "https://hl7.org/fhir/us/davinci-drug-formulary/STU1.0.1/")                                                                                                                                                                                        | Supported            | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| NCQA HEDIS® Implementation Guide                                  | 0.3.1        | [https://www.ncqa.org/resources/hedis-ig-resource-page/](https://www.ncqa.org/resources/hedis-ig-resource-page/ "https://www.ncqa.org/resources/hedis-ig-resource-page/")                                                                                                                                                                                              | Default              | X          | X              | X                     | X                |                       |                       | X                | X                |
| International Patient Summary (IPS)                                | 2.0.0-ballot | [https://hl7.org/fhir/uv/ips/2024Sep/](https://hl7.org/fhir/uv/ips/2024Sep/ "https://hl7.org/fhir/uv/ips/2024Sep/")                                                                                                                                                                                                                                                    | Default              | X          | X              | X                     | X                | X                     | X                     | X                | X                |
| Quality Measure                                                    | 5.0.0        | [https://registry.fhir.org/package/hl7.fhir.us.cqfmeasures%7C5.0.0](https://registry.fhir.org/package/hl7.fhir.us.cqfmeasures%7C5.0.0 "https://registry.fhir.org/package/hl7.fhir.us.cqfmeasures%7C5.0.0")                                                                                                                                                             | Default              | X          | X              | X                     | X                |                       |                       | X                | X                |
| Genomics Reporting                                                 | 3.0.0        | [https://build.fhir.org/ig/HL7/genomics-reporting/index.html](https://build.fhir.org/ig/HL7/genomics-reporting/index.html "https://build.fhir.org/ig/HL7/genomics-reporting/index.html")                                                                                                                                                                               | Default              | X          | X              | X                     | X                |                       |                       | X                | X                |
| National Health Authority's Ayushman Bharat Digital Mission (ABDM) | 2.0          | [https://www.nrces.in/ndhm/fhir/r4/index.html](https://www.nrces.in/ndhm/fhir/r4/index.html "https://www.nrces.in/ndhm/fhir/r4/index.html")                                                                                                                                                                                                                            | Default              | X          | X              | X                     | X                |                       |                       | X                | X                |
| CA Core+                                                           | 1.1.0        | [https://simplifier.net/ca-core](https://simplifier.net/ca-core "https://simplifier.net/ca-core")                                                                                                                                                                                                                                                                      | Supported            |            |                |                       |                  |                       | X                     |                  |                  |
| CA:eReC Pan-Canadian eReferral-eConsult                            | 1.1.0        | [https://simplifier.net/CA-eReC/~introduction](https://simplifier.net/CA-eReC/~introduction "https://simplifier.net/CA-eReC/~introduction")                                                                                                                                                                                                                            | Supported            |            |                |                       |                  |                       | X                     |                  |                  |
| Patient Summary Canadian Edition<br>• (PS-CA)                      | 2.11         | [https://simplifier.net/PS-CA-R1/~introduction](https://simplifier.net/PS-CA-R1/~introduction "https://simplifier.net/PS-CA-R1/~introduction")                                                                                                                                                                                                                         | Supported            |            |                |                       |                  |                       | X                     |                  |                  |
| Ontario Digital Health Drug Repository                             | 4.0.3        | [https://simplifier.net/ca-on-dhdr-r4/~introduction](https://simplifier.net/ca-on-dhdr-r4/~introduction "https://simplifier.net/ca-on-dhdr-r4/~introduction")                                                                                                                                                                                                          | Supported            |            |                |                       |                  |                       | X                     |                  |                  |
| AU Core                                                            | 1.0.0        | [https://hl7.org.au/fhir/core/](https://hl7.org.au/fhir/core/ "https://hl7.org.au/fhir/core/")                                                                                                                                                                                                                                                                         | Supported            |            |                |                       |                  | X                     |                       |                  |                  |
| Magentus Practice Management                                       | 1.2.16       | [https://fhir-versions.dev.geniesolutions.io/1.2.16/downloads.html](https://fhir-versions.dev.geniesolutions.io/1.2.16/downloads.html "https://fhir-versions.dev.geniesolutions.io/1.2.16/downloads.html")                                                                                                                                                             | Supported            |            |                |                       |                  | X                     |                       |                  |                  |

## Validating FHIR profiles specified in a

resource

For a FHIR Profile to be validated add it to the `profile` element of
individual resources using the profile URL designated in the implementation guide.

FHIR Profiles are validated when you add a new resource to your data store. To add a new
resource, you can use the `StartFHIRImportJob` API operation, make a `POST` request
to add a new resource, or make `PUT` to update an existing resource.

###### Example – To see which FHIR profile is referenced in a resource

The profile URL is added to the `profile` element in the `"meta" :
 "profile"` key-value pair. This resource was truncated for clarity.

```
{
    "resourceType": "Patient",
    "id": "abcd1234efgh5678hijk9012",
    "meta": {
        "lastUpdated": "2023-05-30T00:48:07.8443764-07:00",
        "profile": [
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
        ]
    }
}

```

###### Example – How to reference a non-default supported FHIR profile

To validate against a supported non-default profile (e.g. CarinBB 1.0.0) - add the
profile URL with version (separated by '|') and the base profile URL in the
`meta.profile` element. This example resource was truncated for clarity.

```
{
    "resourceType": "ExplanationOfBenefit",
    "id": "sample-EOB",
    "meta": {
        "lastUpdated": "2024-02-02T05:56:09.4+00:00",
        "profile": [
            "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-ExplanationOfBenefit-Pharmacy|1.0.0",
      "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-ExplanationOfBenefit-Pharmacy“
        ]
    }
}

```
