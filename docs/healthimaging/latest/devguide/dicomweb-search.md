# Searching DICOM data in HealthImaging

AWS HealthImaging offers representations of [DICOMweb QIDO-RS](https://www.dicomstandard.org/using/dicomweb/query-qido-rs "https://www.dicomstandard.org/using/dicomweb/query-qido-rs") APIs
to search for studies, series, and instances by Patient ID, and receive their unique identifiers
for further usage. HealthImaging's DICOMweb QIDO-RS APIs offer flexibility in how you search for data
stored in HealthImaging and provide interoperability with legacy applications.

###### Important

HealthImaging's DICOMweb APIs can be used to return image set information with QIDO-RS.
HealthImaging DICOMweb APIs reference only primary [image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") unless otherwise noted. Use HealthImaging
[cloud native actions,](../APIReference/API_Operations.md "../APIReference/API_Operations.md")
or the optional image set parameter of DICOMweb actions to retrieve non-primary image sets. HealthImaging's DICOMweb APIs can be used to
return image set information with DICOMweb-conformant responses.

The APIs listed in this section are built in conformance to the DICOMweb (QIDO-RS) standard
for web-based medical imaging. They are not offered through AWS CLI and AWS SDKs.

## DICOMweb search APIs for HealthImaging

The following table describes all HealthImaging representations of DICOMweb QIDO-RS APIs available
for searching data in HealthImaging.

HealthImaging representations of DICOMweb QIDO-RS APIs| Name | Description |
| --- | --- |
| `SearchDICOMStudies` | Search for DICOM studies in HealthImaging by specifying search query elements using a GET<br>request. Study search results are returned in JSON format, ordered by last update, date<br>descending (latest to oldest). See [Search for studies](dicomweb-search-studies.md "dicomweb-search-studies.md"). |
| `SearchDICOMSeries` | Search for DICOM series in HealthImaging by specifying search query elements using a GET<br>request. Series search results are returned in JSON format, ordered by `Series Number<br>(0020, 0011)` in ascending order (oldest to latest). See [Search for series](dicomweb-search-series.md "dicomweb-search-series.md"). |
| `SearchDICOMInstances` | Search for DICOM instances in HealthImaging by specifying search query elements using a GET<br>request. Instance search results are returned in JSON format, ordered by `Instance<br>Number (0020, 0013)` in ascending order (oldest to latest). See [Search for instances](dicomweb-search-instances.md "dicomweb-search-instances.md"). |
| `SearchDICOMStudyInstances` | Searches for all DICOM instances within a study in HealthImaging by specifying search query<br>elements using a GET request. The API returns instance search results in JSON format, ordered<br>by last update date, descending (latest to oldest). See [Search for a study's instances](dicomweb-search-study-instances.md "dicomweb-search-study-instances.md"). |
| `SearchDICOMAllSeries` | Searches for all DICOM series across a data store in HealthImaging by specifying search query<br>elements using a GET request. The API returns series search results in JSON format, ordered<br>by `Series Number (0020,0011)` in ascending order (oldest to latest). See<br>[Search for all series](dicomweb-search-all-series.md "dicomweb-search-all-series.md"). |
| `SearchDICOMAllInstances` | Searches for all DICOM instances across a data store in HealthImaging by specifying search<br>query elements using a GET request. The API returns instance search results in JSON format,<br>ordered by `Instance Number (0020,0013)` in ascending order (oldest to<br>latest). See [Search for all instances](dicomweb-search-all-instances.md "dicomweb-search-all-instances.md"). |

## Supported DICOMweb query types for HealthImaging

HealthImaging supports QIDO-RS hierarchical resource queries at the Study, Series, and SOP Instance
levels. When using QIDO-RS hierarchical search for HealthImaging:

- Searching for studies returns a list of Studies
- Searching for a Study’s Series requires a known `StudyInstanceUID` and returns
  a list of Series
- Searching a list of Instances requires a known `StudyInstanceUID` and
  `SeriesInstanceUID`

With HealthImaging, you can run QIDO-RS relational queries without specifying all parent UIDs in
the resource hierarchy:

- Searching for a study's instances does not require a
  `SeriesInstanceUID`.
- Searching for all series in a data store does not require a
  `StudyInstanceUID`.
- Searching for all instances in a data store does not require a
  `StudyInstanceUID` or `SeriesInstanceUID`.

The following table describes supported QIDO-RS query types for searching data in
HealthImaging.

HealthImaging supported QIDO-RS query types| Query type | Example |
| --- | --- |
| Attribute value queries | Search for all series in a Study where `modality=CT`.<br>`.../studies/1.3.6.1.4.1.14519.5.2.1.6279.6001.101370605276577556143013894866/series?00080060=CT`<br>Search all studies where patient ID and study date are these values,<br>respectively.<br>`…/studies?PatientID=11235813&StudyDate=20130509` |
| Keyword queries | Search all series using the `SeriesInstanceUID` keyword.<br>`.../studies/1.3.6.1.4.1.14519.5.2.1.6279.6001.101370605276577556143013894866/series?SeriesInstanceUID=1.3.6.1.4.1.14519.5.2.1.6279.6001.101370605276577556143013894868` |
| Tag queries | Search for tags using query parameters passed in group/element form.<br>{group}{element} like 0020000D |
| Range queries | `...?Modality=CT&StudyDate=AABBYYYY-BBCCYYYY` |
| Result paging with `limit` and `offset` | `.../studies?limit=1&offset=0&00080020=20000101`<br>You can use the limit and offset parameters to paginate search responses. The<br>default value of limit is 1000, and see [AWS HealthImaging endpoints and quotas](endpoints-quotas.md "endpoints-quotas.md") for the maximum value.<br>Max limit = 1000, Max offset = 1,000,000 |
| Wildcard queries | Wildcard queries provide more flexibility on search using "\*" and "?". "\*" matches any sequence of characters (including a zero length value) and "?" matches any single character.<br>Search for all studies in a datastore where StudyDescription contains "Nuclear":<br>`.../studies?StudyDescription=*Nuclear*`<br>Search for all studies where StudyDescription ends with "Nuclear":<br>`.../studies?StudyDescription=*Nuclear`<br>Search for all studies where StudyDescription starts with "Nuclear":<br>`.../studies?StudyDescription=Nuclear*`<br>Search for all studies where PatientID has exactly any 3 characters after 200965981:<br>`.../studies?PatientID=200965981???` |
| FuzzyMatching queries | Enable fuzzy matching on name DICOM attributes (PatientName (0010,0010), ReferringPhysicianName(0008,0090)) by adding the fuzzymatching optional query parameter:<br>`.../studies?fuzzymatching=true&PatientName="Thomas^Albert"`<br>This query performs case-insensitive prefix word matching on any part of the PatientName value. It returns results with PatientName values like "thomas", "Albert", "Thomas Albert", "Thomas^Albert", but not "hom" or "ber". |
| IncludeField queries | Use the `includefield` query parameter to request additional DICOM<br>attributes beyond the default response set.<br>Return specific attributes by tag:<br>`.../studies?PatientID=11235813&includefield=00101081&includefield=PatientWeight`<br>Return all available attributes:<br>`.../studies?PatientID=11235813&includefield=all`<br>Return sequence (SQ) sub-attributes using dotted notation:<br>`.../studies?PatientID=11235813&includefield=00080096.00080100`<br>Return private data elements:<br>`.../instances?includefield=00191001&00190010=Philips` |
| Relational queries | Search for all series across a data store where the modality is CT:<br>`.../series?Modality=CT`<br>Search for all instances in a study where the study date is a specific value:<br>`.../studies/`StudyInstanceUID`/instances?StudyDate=20240101` |

## Using IncludeField in QIDO-RS queries

The `includefield` query parameter lets you request additional DICOM attributes
beyond the default response set in HealthImaging QIDO-RS queries. You can use
`includefield` at the study, series, and instance levels.

### Syntax

Use the following GET request format to include additional fields in your QIDO-RS
queries:

```
GET .../studies?<query_params>&includefield=<tag_or_keyword>
GET .../studies/<StudyInstanceUID>/series?<query_params>&includefield=<tag_or_keyword>
GET .../studies/<StudyInstanceUID>/series/<SeriesInstanceUID>/instances?<query_params>&includefield=<tag_or_keyword>
```

You can specify multiple `includefield` parameters in a single request:

```
GET .../studies?PatientID=11235813&includefield=00101081&includefield=00101030&includefield=00101010
```

### Supported values for includefield

The following table describes the supported values for the `includefield`
parameter.

Supported includefield values| Value type | Description | Example |
| --- | --- | --- |
| DICOM tag (8 hex characters) | Request a specific DICOM attribute by its tag in GGGGEEEE format. | `includefield=00081030` |
| `all` | Request all available DICOM attributes for the resource level. | `includefield=all` |
| Dotted SQ path | Request a specific sub-attribute within a Sequence (SQ) attribute using dot<br>notation: <parent\_tag>.<child\_tag>. | `includefield=00080096.00080100` |
| Private data element tag | Request a private tag (odd-group element). Requires the<br>`privateCreatorElement` parameter. | `includefield=00191001` |
| Standard DICOM attributes including bulkdata | Request specific single or multiple attributes by tag or keyword. | `includefield=00102201` |

### Behavior and rules

The following rules apply to `includefield` queries:

- **Default response** – Without
  `includefield`, the QIDO-RS response returns only the standard set of
  attributes.
- **includefield=all** – Returns all available attributes
  at the requested level. When `all` is combined with other
  `includefield` values, `all` takes priority.
- **Maximum tags** – A request can include up to 50
  `includefield` parameters.
- **Duplicate tags** – Duplicate
  `includefield` values are deduplicated and treated as a single request.
- **Invalid or missing tags** – If a requested tag does
  not exist in the DICOM data or is invalid, it is silently omitted from the response. Other
  valid `includefield` attributes are still returned.

### Sequence (SQ) attributes

Use dot notation to request nested attributes within a Sequence (SQ) attribute:

```
includefield=<parent_SQ_tag>.<child_tag>
```

For example, to retrieve CodeValue (0008,0100) within
ReferringPhysicianIdentificationSequence (0008,0096):

```
GET .../studies?PatientID=11235813&includefield=00080096.00080100
```

Multi-level nesting is supported. For example:

```
includefield=00081115.00081199.00081150
```

### Private tags

Private DICOM data elements (odd-group tags) are supported at all resource levels. To
request private tags, include the `privateCreatorElement` query parameter.

Use the following syntax:

```
GET .../instances?includefield=<private_tag>&<creator_tag>=<creator_name>
```

For example:

```
GET .../instances?includefield=00191001&00190010=Philips
```

The following rules apply to private tags:

- The `privateCreatorElement` tag and creator name must be provided as a match
  parameter if the private tag is requested.
- If the specified `privateCreatorElement` is not found, the private tag is
  silently omitted.
- Requesting only a `privateCreatorElement` tag without a private data
  element returns the creator element name and value only. It does not return all tags
  belonging to that creator's block.

### Bulkdata tags

DICOM attributes with bulkdata VRs (OB, OD, OF, OL, UN, OW, OV) with binary value
greater than 1 MB requested as part of the `includefield` are returned as
`bulkdataURI` instead of the raw binary value. For more information about
retrieving bulkdata, see [Retrieving DICOM bulkdata
in HealthImaging](dicom-retrieve-bulkdata.md "dicom-retrieve-bulkdata.md").

### What does includefield=all return at each level?

When `includefield=all` is specified, the response includes all attributes
at the specific resource level.

#### Study level (includefield=all)

The following table lists all attributes returned at the study level when
`includefield=all` is specified.

Study level attributes for includefield=all| Tag | Name | VR |
| --- | --- | --- |
| 00080005 | SpecificCharacterSet | CS |
| 00080020 | StudyDate | DA |
| 00080030 | StudyTime | TM |
| 00080050 | AccessionNumber | SH |
| 00080051 | IssuerOfAccessionNumberSequence | SQ |
| 00080056 | InstanceAvailability | CS |
| 00080061 | ModalitiesInStudy | CS |
| 00080062 | SOPClassesInStudy | UI |
| 00080090 | ReferringPhysicianName | PN |
| 0008009C | ConsultingPhysicianName | PN |
| 00080201 | TimezoneOffsetFromUTC | SH |
| 00081030 | StudyDescription | LO |
| 00081048 | PhysiciansOfRecord | PN |
| 00081060 | NameOfPhysiciansReadingStudy | PN |
| 00081080 | AdmittingDiagnosesDescription | LO |
| 00081190 | RetrieveURL | UR |
| 00100010 | PatientName | PN |
| 00100020 | PatientID | LO |
| 00100021 | IssuerOfPatientID | LO |
| 00100022 | TypeOfPatientID | CS |
| 00100026 | SourcePatientGroupIdentificationSequence | SQ |
| 00100027 | GroupOfPatientsIdentificationSequence | SQ |
| 00100028 | SubjectRelativePositionInImage | US |
| 00100030 | PatientBirthDate | DA |
| 00100032 | PatientBirthTime | TM |
| 00100033 | PatientBirthDateInAlternativeCalendar | LO |
| 00100034 | PatientDeathDateInAlternativeCalendar | LO |
| 00100035 | PatientAlternativeCalendar | CS |
| 00100040 | PatientSex | CS |
| 00100050 | PatientInsurancePlanCodeSequence | SQ |
| 00100101 | PatientPrimaryLanguageCodeSequence | SQ |
| 00100102 | PatientPrimaryLanguageModifierCodeSequence | SQ |
| 00100200 | QualityControlSubject | CS |
| 00100201 | QualityControlSubjectTypeCodeSequence | SQ |
| 00100213 | StrainNomenclature | LO |
| 00100214 | StrainStockNumber | LO |
| 00100215 | StrainSourceRegistryCodeSequence | SQ |
| 00100217 | StrainSource | LO |
| 00100219 | StrainCodeSequence | SQ |
| 00100223 | GeneticModificationsNomenclature | LO |
| 00100229 | GeneticModificationsCodeSequence | SQ |
| 00101001 | OtherPatientNames | PN |
| 00101005 | PatientBirthName | PN |
| 00101010 | PatientAge | AS |
| 00101020 | PatientSize | DS |
| 00101021 | PatientSizeCodeSequence | SQ |
| 00101022 | PatientBodyMassIndex | DS |
| 00101023 | MeasuredAPDimension | DS |
| 00101024 | MeasuredLateralDimension | DS |
| 00101030 | PatientWeight | DS |
| 00101040 | PatientAddress | LO |
| 00101060 | PatientMotherBirthName | PN |
| 00101080 | MilitaryRank | LO |
| 00101081 | BranchOfService | LO |
| 00102000 | MedicalAlerts | LO |
| 00102110 | Allergies | LO |
| 00102150 | CountryOfResidence | LO |
| 00102152 | RegionOfResidence | LO |
| 00102154 | PatientTelephoneNumbers | SH |
| 00102160 | EthnicGroup | SH |
| 00102180 | Occupation | SH |
| 001021A0 | SmokingStatus | CS |
| 001021C0 | PregnancyStatus | US |
| 001021D0 | LastMenstrualDate | DA |
| 001021F0 | PatientReligiousPreference | LO |
| 00102201 | PatientSpeciesDescription | LO |
| 00102202 | PatientSpeciesCodeSequence | SQ |
| 00102203 | PatientSexNeutered | CS |
| 00102210 | AnatomicalOrientationType | CS |
| 00102292 | PatientBreedDescription | LO |
| 00102293 | PatientBreedCodeSequence | SQ |
| 00102295 | BreedRegistrationNumber | LO |
| 00102296 | BreedRegistryCodeSequence | SQ |
| 00102297 | ResponsiblePerson | PN |
| 00102298 | ResponsiblePersonRole | CS |
| 00102299 | ResponsibleOrganization | LO |
| 00109431 | ExaminedBodyThickness | FL |
| 0020000D | StudyInstanceUID | UI |
| 00200010 | StudyID | SH |
| 00201206 | NumberOfStudyRelatedSeries | IS |
| 00201208 | NumberOfStudyRelatedInstances | IS |
| 00321032 | RequestingPhysician | PN |
| 00321033 | RequestingService | LO |
| 00321060 | RequestedProcedureDescription | LO |
| 00321070 | RequestedContrastAgent | LO |
| 00380010 | AdmissionID | LO |
| 00380016 | RouteOfAdmissions | LO |
| 00380020 | AdmittingDate | DA |
| 00380021 | AdmittingTime | TM |
| 00380050 | SpecialNeeds | LO |
| 00380060 | ServiceEpisodeID | LO |
| 00380062 | ServiceEpisodeDescription | LO |
| 00380300 | CurrentPatientLocation | LO |
| 00380400 | PatientInstitutionResidence | LO |
| 00380500 | PatientState | LO |
| 00400244 | PerformedProcedureStepStartDate | DA |
| 00400245 | PerformedProcedureStepStartTime | TM |
| 00400250 | PerformedProcedureStepEndDate | DA |
| 00400251 | PerformedProcedureStepEndTime | TM |
| 00400253 | PerformedProcedureStepID | SH |
| 00081032 | ProcedureCodeSequence | SQ |
| 00100024 | IssuerOfPatientIDQualifiersSequence | SQ |
| 00321034 | RequestingServiceCodeSequence | SQ |
| 00321064 | RequestedProcedureCodeSequence | SQ |
| 00401012 | ReasonForPerformedProcedureCodeSequence | SQ |

#### Series level (includefield=all)

The following table lists the series-level attributes returned when
`includefield=all` is specified. The series level also returns all study-level
attributes listed in the preceding table.

Series level attributes for includefield=all| Tag | Name | VR |
| --- | --- | --- |
| 00080021 | SeriesDate | DA |
| 00080031 | SeriesTime | TM |
| 00080060 | Modality | CS |
| 00080064 | ConversionType | CS |
| 00080068 | PresentationIntentType | CS |
| 00080070 | Manufacturer | LO |
| 00080080 | InstitutionName | LO |
| 00080082 | InstitutionCodeSequence | SQ |
| 00081010 | StationName | SH |
| 0008103E | SeriesDescription | LO |
| 0008103F | SeriesDescriptionCodeSequence | SQ |
| 00081040 | InstitutionalDepartmentName | LO |
| 00081041 | InstitutionalDepartmentTypeCodeSequence | SQ |
| 00081050 | PerformingPhysicianName | PN |
| 00081070 | OperatorsName | PN |
| 00081090 | ManufacturerModelName | LO |
| 00180010 | ContrastBolusAgent | LO |
| 00180015 | BodyPartExamined | CS |
| 00180050 | SliceThickness | DS |
| 00180088 | SpacingBetweenSlices | DS |
| 00181000 | DeviceSerialNumber | LO |
| 00181016 | SecondaryCaptureDeviceManufacturer | LO |
| 00181018 | SecondaryCaptureDeviceManufacturerModelName | LO |
| 00181019 | SecondaryCaptureDeviceSoftwareVersions | LO |
| 00181020 | SoftwareVersions | LO |
| 00181030 | ProtocolName | LO |
| 00181050 | SpatialResolution | DS |
| 00181200 | DateOfLastCalibration | DA |
| 00181201 | TimeOfLastCalibration | TM |
| 00185100 | PatientPosition | CS |
| 0020000D | StudyInstanceUID | UI |
| 0020000E | SeriesInstanceUID | UI |
| 00200011 | SeriesNumber | IS |
| 00200052 | FrameOfReferenceUID | UI |
| 00200060 | Laterality | CS |
| 00201209 | NumberOfSeriesRelatedInstances | IS |
| 00540081 | NumberOfSlices | US |
| 00540101 | NumberOfTimeSlices | US |
| 00541000 | SeriesType | CS |

#### Instance level (includefield=all)

At the instance level, `includefield=all` returns the full instance-level
DICOM metadata. This includes all attributes stored in the instance metadata in HealthImaging
storage. Every DICOM tag present in the original DICOM file for that instance is returned,
except the pixel data attribute.

###### Topics

- [Searching for DICOM studies in HealthImaging](dicomweb-search-studies.md "dicomweb-search-studies.md")
- [Searching for DICOM series in HealthImaging](dicomweb-search-series.md "dicomweb-search-series.md")
- [Searching for DICOM instances in HealthImaging](dicomweb-search-instances.md "dicomweb-search-instances.md")
- [Searching for a study's DICOM instances in HealthImaging](dicomweb-search-study-instances.md "dicomweb-search-study-instances.md")
- [Searching for all DICOM series in HealthImaging](dicomweb-search-all-series.md "dicomweb-search-all-series.md")
- [Searching for all DICOM instances in HealthImaging](dicomweb-search-all-instances.md "dicomweb-search-all-instances.md")
