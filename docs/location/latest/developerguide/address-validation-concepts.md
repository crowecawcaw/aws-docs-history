

# Address validation
<a name="address-validation-concepts"></a>

Address validation jobs process address data to verify and standardize addresses. The service supports both free-form address lines and structured address components, and can optionally enhance results with geographic coordinates and country-specific postal attributes.

Address validation supports addresses from the following countries: Australia, Canada, United Kingdom, and United States.

## Address validation features
<a name="address-validation-features"></a>

Address validation provides the following features for verifying and enhancing address data:

**Address standardization**  
Address validation verifies that an address exists and is deliverable by checking it against authoritative address datasets. Address standardization formats addresses according to official postal standards, such as consistent abbreviations, capitalization, and punctuation. It also corrects errors such as spelling mistakes and adds missing address components such as postal codes and street names.

**Enhanced validation**  
Address validation jobs support optional additional features that enhance validation results:  
+ **Position** — Returns geographic coordinates (longitude and latitude) for validated addresses, enabling you to map addresses or perform geographic analysis. This feature is only available in the United States, Canada, and Australia, and incurs additional costs.
+ **CountrySpecificAttributes** — Provides postal system information specific to each country. For example, US addresses receive USPS data such as delivery point codes and carrier route information, while Australian addresses receive Australia Post identifiers.
For more information about pricing, see [Jobs pricing](jobs-pricing.md).

## Address validation use cases
<a name="address-validation-use-cases"></a>

**Healthcare systems and insurers**  
Validate patient and provider addresses for claims processing, care coordination, and regulatory reporting requirements.

**Financial services and insurance carriers**  
Standardize customer addresses to support identity verification workflows, risk assessment, and fraud prevention.

**Retail and e-commerce operations**  
Clean customer databases to reduce shipping failures, improve delivery rates, and optimize fulfillment costs.

**Transportation and logistics providers**  
Validate delivery addresses for route optimization and reduce failed deliveries across last-mile operations.

**Data migration and database maintenance**  
Perform one-time database cleanup during system transitions and regularly validate address records to maintain data quality.

**Analytics, reporting, and entity resolution**  
Standardize addresses for location-based analytics, demographic analysis, and Customer Relationship Management (CRM) database cleanup through entity resolution workflows.

## Input schema
<a name="address-validation-input-schema"></a>

Address validation jobs require input data with a specific schema. The schema supports both free-form address lines and structured address components, allowing you to submit addresses in the format that best matches your data.

The input schema includes the following fields:

Id  
An optional identifier to give to this input record. If provided, it is mirrored in the output file as `Input_Id` to help you correlate output records with their corresponding inputs.

Address lines  
Use `AddressLines_1` through `AddressLines_5` for free-form addresses. Enter single-line inputs in `AddressLines_1`. Order multi-line inputs according to regional postal rules, as they would appear on mail.

AddressComponents\_Country  
The alpha-2, alpha-3 character code, or full name of the country where the address is located.

AddressComponents\_Region  
The region of the input address, such as state, province, or territory.

AddressComponents\_SubRegion  
The sub-region of the input address, such as county.

AddressComponents\_Locality  
The locality of the input address, such as city or town.

AddressComponents\_PostalCode  
The postal code of the input address.

AddressComponents\_Street  
The street name of the input address.

AddressComponents\_AddressNumber  
The address or house number of the input address.

AddressComponents\_Unit  
The unit of the input address.

AddressComponents\_UnitDesignator  
The unit designator or type of the input address, such as Apt, Suite, or \#.

**Note**  
When combining both AddressLines and AddressComponents in a request, enter first-line address components (AddressNumber, Street, Unit, and UnitDesignator) in AddressLines. Enter last-line components (Locality, Region, SubRegion, Country, and PostalCode) through AddressComponents.

### Sample Python script to create input data
<a name="address-validation-input-sample"></a>

The following Python script creates a sample Parquet file with address data:

```
import pyarrow as pa
import pyarrow.parquet as pq

data = [
    {
        "Id": "record-001",
        "AddressLines_1": "Pike Place",
        "AddressLines_2": "Apartment 4B",
        "AddressLines_3": None,
        "AddressLines_4": None,
        "AddressLines_5": None,
        "AddressComponents_Country": "USA",
        "AddressComponents_Region": None,
        "AddressComponents_SubRegion": None,
        "AddressComponents_Locality": None,
        "AddressComponents_PostalCode": "98101",
        "AddressComponents_Street": None,
        "AddressComponents_AddressNumber": None,
        "AddressComponents_Unit": None,
        "AddressComponents_UnitDesignator": None
    },
    {
        "Id": "record-002",
        "AddressLines_1": "2901 E Madison St",
        "AddressLines_2": None,
        "AddressLines_3": None,
        "AddressLines_4": None,
        "AddressLines_5": None,
        "AddressComponents_Country": "USA",
        "AddressComponents_Region": None,
        "AddressComponents_SubRegion": None,
        "AddressComponents_Locality": None,
        "AddressComponents_PostalCode": "98112",
        "AddressComponents_Street": None,
        "AddressComponents_AddressNumber": None,
        "AddressComponents_Unit": None,
        "AddressComponents_UnitDesignator": None
    }
]

schema = pa.schema([
    ("Id", pa.string()),
    ("AddressLines_1", pa.string()),
    ("AddressLines_2", pa.string()),
    ("AddressLines_3", pa.string()),
    ("AddressLines_4", pa.string()),
    ("AddressLines_5", pa.string()),
    ("AddressComponents_Country", pa.string()),
    ("AddressComponents_Region", pa.string()),
    ("AddressComponents_SubRegion", pa.string()),
    ("AddressComponents_Locality", pa.string()),
    ("AddressComponents_PostalCode", pa.string()),
    ("AddressComponents_Street", pa.string()),
    ("AddressComponents_AddressNumber", pa.string()),
    ("AddressComponents_Unit", pa.string()),
    ("AddressComponents_UnitDesignator", pa.string())
])

table = pa.Table.from_pylist(data, schema=schema)
pq.write_table(table, 'addresses.parquet')
```

For file size limits, see [Prepare input data](preparing-input-data.md).

## Output schema
<a name="address-validation-output-schema"></a>

Address validation jobs produce output that includes standardized address components, validation results, and optional additional feature data. The following sections describe the address validation-specific output fields.

For general output schema information and how to retrieve results, see [Retrieve job results](retrieving-results.md).

### Output address fields
<a name="output-address-fields"></a>

Standardized address components with an `Output_` prefix, formatted according to regional postal rules.

#### Complete list of output address fields
<a name="output-address-fields-list"></a>

Output\_AddressId  
A unique identifier for the returned address.

Output\_AddressLines\_1  
The first line of the complete returned address written on multiple lines, as it should appear on a piece of mail. It is formatted according to the regional postal rules.

Output\_AddressLines\_2  
The second line of the complete returned address written on multiple lines, as it should appear on a piece of mail. It is formatted according to the regional postal rules.

Output\_AddressLines\_3  
The third line of the complete returned address written on multiple lines, as it should appear on a piece of mail. It is formatted according to the regional postal rules.

Output\_AddressLines\_4  
The fourth line of the complete returned address written on multiple lines, as it should appear on a piece of mail. It is formatted according to the regional postal rules.

Output\_AddressLines\_5  
The fifth line of the complete returned address written on multiple lines, as it should appear on a piece of mail. It is formatted according to the regional postal rules.

Output\_Address\_Label  
The assembled address built out of the address components, according to the regional postal rules.

Output\_Address\_Country\_Code2  
Alpha-2 character code of the country.

Output\_Address\_Country\_Code3  
Alpha-3 character code of the country.

Output\_Address\_Country\_Name  
Full name of the country.

Output\_Address\_Region\_Code  
Abbreviated code for the region.

Output\_Address\_Region\_Name  
Full name for the region.

Output\_Address\_SubRegion\_Code  
Abbreviated code for the sub-region.

Output\_Address\_SubRegion\_Name  
Full name for the sub-region.

Output\_Address\_Locality  
The locality component of the address, such as city or town.

Output\_Address\_PostalCode  
The full postal code component of the address.

Output\_Address\_PostalCodeDetails\_Base  
The base segment of the postal code.

Output\_Address\_PostalCodeDetails\_Extension  
The extension or add-on segment of the postal code.

Output\_Address\_Street  
The full street component of the address.

Output\_Address\_StreetComponents\_BaseName  
Base name part of the street name.

Output\_Address\_StreetComponents\_Prefix  
Directional identifier that precedes, but is not included in, the base name of a road.

Output\_Address\_StreetComponents\_Suffix  
Directional identifier that follows, but is not included in, the base name of a road.

Output\_Address\_StreetComponents\_Type  
Street type part of the street name such as `ST`, `AVE`, `BLVD`.

Output\_Address\_StreetComponents\_TypePlacement  
Defines if the street type is before or after the base name. (`BeforeBaseName` or `AfterBaseName`)

Output\_Address\_AddressNumber  
The address or house number component of the address.

Output\_Address\_SecondaryAddressComponents\_Unit\_Number  
The alphanumeric identifier of the unit secondary address component.

Output\_Address\_SecondaryAddressComponents\_Unit\_Designator  
The designator of the unit secondary address component, as it appears in the address label.

Output\_Address\_SecondaryAddressComponents\_Floor\_Number  
The alphanumeric identifier of the floor secondary address component.

Output\_Address\_SecondaryAddressComponents\_Floor\_Designator  
The designator of the floor secondary address component, as it appears in the address label.

### Address metadata
<a name="address-metadata"></a>

Metadata about the address and delivery characteristics.

Output\_AddressMetadata\_DeliveryIndicators\_Mailable  
Indicates whether an address is mailable. Values: `true`/`false`

Output\_AddressMetadata\_DeliveryIndicators\_Locatable  
Indicates whether an address is locatable. Values: `true`/`false`

### Validation results
<a name="validation-results"></a>

Overall validation quality metrics for the address.

Output\_ValidationResults\_ValidationGranularity  
Indicates the overall level of granularity that the returned address was validated to. Values:  
+ `Premise` – All components to the address number level were validated
+ `Street` – All components to the street level were validated
+ `LocalityAndPostalCode` – Locality, PostalCode, and Country were validated
+ `Locality` – Locality and Country were validated

Output\_ValidationResults\_MatchConfidence  
Indicates the overall confidence level in the address match performed during the address validation process. Values: `High`, `MediumHigh`, `Medium`, `MediumLow`, `Low`

Output\_ValidationResults\_MatchConfidenceScore  
Provides a precise score for the match confidence. Ranges from 0 - 1.0, with 1.0 indicating a perfect match.

### Component validation status
<a name="component-validation-status"></a>

For each address component, two fields indicate validation results:
+ `Status` fields indicate the validation status: `Validated` or `Unconfirmed`
+ `StatusDetail` fields provide additional detail about the validation status:
  + `NotFound` – Component was not found or empty.
  + `StandardizedNoMatch` – Component was parsed and standardized, but not identified in reference data.
  + `OutOfRange` – Component was not identified, reference data suggests the component is out of range or unknown.
  + `Corrected` – Component was corrected using reference data.
  + `Exact` – Component was validated without changes.
  + `Alias` – Component was validated using reference data alias.
  + `Appended` – Component was appended using reference data.

#### Component validation field pairs
<a name="component-validation-fields-list"></a>

Output\_ValidationResults\_Components\_Address\_Country\_Status  
Validation status for the country component.

Output\_ValidationResults\_Components\_Address\_Country\_StatusDetail  
Detailed validation status for the country component.

Output\_ValidationResults\_Components\_Address\_Region\_Status  
Validation status for the region component.

Output\_ValidationResults\_Components\_Address\_Region\_StatusDetail  
Detailed validation status for the region component.

Output\_ValidationResults\_Components\_Address\_Locality\_Status  
Validation status for the locality component.

Output\_ValidationResults\_Components\_Address\_Locality\_StatusDetail  
Detailed validation status for the locality component.

Output\_ValidationResults\_Components\_Address\_Street\_Status  
Validation status for the street component.

Output\_ValidationResults\_Components\_Address\_Street\_StatusDetail  
Detailed validation status for the street component.

Output\_ValidationResults\_Components\_Address\_AddressNumber\_Status  
Validation status for the address number component.

Output\_ValidationResults\_Components\_Address\_AddressNumber\_StatusDetail  
Detailed validation status for the address number component.

Output\_ValidationResults\_Components\_Address\_PostalCodeDetails\_Base\_Status  
Validation status for the postal code base component.

Output\_ValidationResults\_Components\_Address\_PostalCodeDetails\_Base\_StatusDetail  
Detailed validation status for the postal code base component.

Output\_ValidationResults\_Components\_Address\_PostalCodeDetails\_Extension\_Status  
Validation status for the postal code extension component.

Output\_ValidationResults\_Components\_Address\_PostalCodeDetails\_Extension\_StatusDetail  
Detailed validation status for the postal code extension component.

Output\_ValidationResults\_Components\_Address\_SecondaryAddressComponents\_Unit\_Status  
Validation status for the unit component.

Output\_ValidationResults\_Components\_Address\_SecondaryAddressComponents\_Unit\_StatusDetail  
Detailed validation status for the unit component.

Output\_ValidationResults\_Components\_Address\_SecondaryAddressComponents\_Floor\_Status  
Validation status for the floor component.

Output\_ValidationResults\_Components\_Address\_SecondaryAddressComponents\_Floor\_StatusDetail  
Detailed validation status for the floor component.

### Additional feature output
<a name="additional-feature-output"></a>

If you requested additional features when starting the job, the output includes:

#### Position
<a name="position-output"></a>

Geographic coordinates in World Geodetic System (WGS 84) format.

Output\_Position\_Longitude  
The longitude coordinate in World Geodetic System (WGS 84) format.

Output\_Position\_Latitude  
The latitude coordinate in World Geodetic System (WGS 84) format.

#### Country-specific attributes
<a name="country-specific-attributes"></a>

Country-specific postal and census data. The available fields vary by country.

##### Australia
<a name="australia-attributes"></a>

##### AustraliaPost
<a name="australia-post"></a>

Output\_CountrySpecificAttributes\_AUS\_AustraliaPost\_DeliveryPointIdentifier  
An eight-digit code developed by Australia Post which enables each delivery point in Australia to be uniquely identified.

##### Census
<a name="australia-census"></a>

Output\_CountrySpecificAttributes\_AUS\_Census\_MeshBlockId  
Mesh Blocks are the smallest geographic areas defined by the ABS and form the building blocks for the larger regions of the Australian Statistical Geography Standard (ASGS). They broadly identify land use such as residential, commercial, primary production and parks.

##### Gnaf
<a name="australia-gnaf"></a>

Output\_CountrySpecificAttributes\_AUS\_Gnaf\_AddressClass  
The address class, which is constructed using a combination of address elements. Values include: `A` (Alias), `P` (Principal), `PP` (Principal Primary), `PS` (Principal Secondary), `AP` (Alias Primary), `AS` (Alias Secondary).

Output\_CountrySpecificAttributes\_AUS\_Gnaf\_GnafPid  
The Persistent Identifier is unique to the real world feature this record represents. The Persistent Identifier (PID) is a 14-character alphanumeric string uniquely identifying each G-NAF address.

Output\_CountrySpecificAttributes\_AUS\_Gnaf\_LegalParcelId  
This field within G-NAF is designed to hold a unique identifier for the land parcel associated with a specific address. Parcel ID, representing the Lot on Plan description. Used by government agencies. Format varies.

Output\_CountrySpecificAttributes\_AUS\_Gnaf\_StatisticalArea1  
Geographic areas built from whole Mesh Blocks. Whole SA1s aggregate to form Statistical Areas Level 2 (SA2s). Statistical Area Level 1 (SA1) field representing a geographic area used in the Census. Seven-digit unique code.

##### Canada
<a name="canada-attributes"></a>

##### CanadaPost
<a name="canada-post"></a>

Output\_CountrySpecificAttributes\_CAN\_CanadaPost\_BuildingType  
A code that denotes whether the building is a business building or an apartment building. Valid values are: `1` = Residential, `2` = Commercial.

Output\_CountrySpecificAttributes\_CAN\_CanadaPost\_RecordType  
Defines the type of record in the Address Lookup and the Text Lookup files. Values include: `A1` (High-rise building), `B1` (Large Volume Receiver), `C1` (Government Address), `D2` (LVR Served by Lock Box), `E2` (Government Served by Lock Box), `F2` (LVR Served by General Delivery), `11` (Street), `21` (Street served by route), `32` (PO Box).

##### Census
<a name="canada-census"></a>

Output\_CountrySpecificAttributes\_CAN\_Census\_DisseminationArea  
Uniquely identifies a dissemination area. It is composed of the two-digit province or territory code, the two-digit census division code and the four-digit dissemination area code.

Output\_CountrySpecificAttributes\_CAN\_Census\_Division  
Uniquely identifies a census division. The first two digits of the CDuid identify the province or territory (PR).

Output\_CountrySpecificAttributes\_CAN\_Census\_MetropolitanArea  
Formed by one or more adjacent municipalities centered on a population centre (known as the core).

Output\_CountrySpecificAttributes\_CAN\_Census\_Subdivision  
Uniquely identifies a census subdivision in the country. The province/territory, census division, and census subdivision (municipality) codes combine to represent the Standard Geographical Classification (SGC).

Output\_CountrySpecificAttributes\_CAN\_Census\_Tract  
Identifies a census tract within a CMA/CA. To uniquely identify each census tract in its corresponding census metropolitan area or tracted census agglomeration, the three-digit CMA/CA code must precede the census tract 'name.'

##### United States
<a name="usa-attributes"></a>

##### USPS
<a name="usa-usps"></a>

Output\_CountrySpecificAttributes\_USA\_Usps\_CarrierRoute  
A group of mailing addresses within a ZIP code that the USPS groups together to make the mail delivery process more efficient. In the same way that ZIP codes divide up the country into different areas carrier routes divide up those ZIP codes.

Output\_CountrySpecificAttributes\_USA\_Usps\_DefaultFlag  
Indicated the record processed obtained a match to a highrise, rural route or street default record in the ZIP \+ 4 product. `Y` - The default flag indicator is set, `N` or Blank - Acceptable.

Output\_CountrySpecificAttributes\_USA\_Usps\_DeliveryPoint\_Barcode  
2-digit delivery point of the house/box.

Output\_CountrySpecificAttributes\_USA\_Usps\_DeliveryPoint\_CheckDigit  
A number that is added to the sum of the other digits in the DPBC to yield a number that is a multiple of ten.

Output\_CountrySpecificAttributes\_USA\_Usps\_Elot\_AscendingDescendingFlag  
The ascending/descending code indicates the approximate delivery order within the sequence number.

Output\_CountrySpecificAttributes\_USA\_Usps\_Elot\_SequenceNumber  
Enhanced Line of Travel (eLOT) sequence number to help mailers sort mailings in a way that aligns with the carrier's delivery path. Indicates the first occurrence of delivery made to the add-on range within the carrier route.

Output\_CountrySpecificAttributes\_USA\_Usps\_NonDeliverableRecord  
Field on the Stage I file indicates the address test question is a valid match to a record on the ZIP \+ 4® Product. However, the match is made to a non-deliverable (ND) type record. `Y` - Record is an ND type, Blank - Record is not an ND type.

Output\_CountrySpecificAttributes\_USA\_Usps\_PoBoxOnlyFlag  
There is a portion of the City State product that contains PO Box Only Delivery Zones. The file layout utilizes `P` as the Copyright Detail Code which is different from the existing ZIP. Classification code `P` located in the thirteenth (13) position of the City State detail record that indicates there are PO Box and other types of deliveries to the community. These zones have no other form of postal delivery.

Output\_CountrySpecificAttributes\_USA\_Usps\_RecordType  
Type of the address record that matches the input address such as Firm (`F`) General Delivery (`G`) Highrise (`H`) P.O. Box (`P`) Rural Route (`R`) or Street Record (`S`).

Output\_CountrySpecificAttributes\_USA\_Usps\_RuralRouteDefault  
Indicates a rural route match. `Y` - the address matched to a rural route record. `N` or blank - the address did not match to a rural route record.

Output\_CountrySpecificAttributes\_USA\_Usps\_Urbanization  
Puerto Rican urbanization name.

Output\_CountrySpecificAttributes\_USA\_Usps\_ZipValid  
True/false flag that indicates a valid zip code. Indicates whether the address record can be added to Form 3553. Five-digit validation requires that the last line values of city state and ZIP Code correspond to each other.

Output\_CountrySpecificAttributes\_USA\_Usps\_Zip10  
10-digit ZIP Code (ZIP \+ 4) with dash separator.

Output\_CountrySpecificAttributes\_USA\_Usps\_Zip9  
9-digit ZIP Code (ZIP \+ 4).

##### Census
<a name="usa-census"></a>

Output\_CountrySpecificAttributes\_USA\_Census\_BlockId  
2020 Census Block ID.

Output\_CountrySpecificAttributes\_USA\_Census\_CombinedStatisticalArea\_Number  
Combined Statistical Area (CSA) number.

Output\_CountrySpecificAttributes\_USA\_Census\_CombinedStatisticalArea\_Name  
Combined Statistical Area (CSA) name.

Output\_CountrySpecificAttributes\_USA\_Census\_CoreBasedStatisticalArea\_Number  
Core Based Statistical Area (CBSA) number.

Output\_CountrySpecificAttributes\_USA\_Census\_CoreBasedStatisticalArea\_Name  
The name of the Core Based Statistical Area (CBSA) in which the address is located.

Output\_CountrySpecificAttributes\_USA\_Census\_CountyFipsCode  
The county FIPS code.

Output\_CountrySpecificAttributes\_USA\_Census\_MetropolitanAreaFlag  
Indicates whether the Core Based Statistical Area (CBSA) in which the address is located is a metropolitan area or a micropolitan area (`Y`/`N`).

##### United Kingdom
<a name="uk-attributes"></a>

##### RoyalMail
<a name="uk-royalmail"></a>

Output\_CountrySpecificAttributes\_GBR\_RoyalMail\_SubBuilding  
The sub-building name and/or identifier of the address.

Output\_CountrySpecificAttributes\_GBR\_RoyalMail\_ThoroughfareName  
The base name of the street or thoroughfare of the address.

Output\_CountrySpecificAttributes\_GBR\_RoyalMail\_DependentThoroughfareName  
The double dependent thoroughfare of the address. This is used when there are named thoroughfares within other named thoroughfares.

Output\_CountrySpecificAttributes\_GBR\_RoyalMail\_DependentLocality  
The dependent locality of the address. This is used when there are thoroughfares with the same or similar names within a locality.

Output\_CountrySpecificAttributes\_GBR\_RoyalMail\_DoubleDependentLocality  
The double dependent locality of the address. This is used when there are multiple thoroughfares with the same or similar names within a dependent locality.

Output\_CountrySpecificAttributes\_GBR\_RoyalMail\_OrganizationName  
The name of the organization registered at the address.

Output\_CountrySpecificAttributes\_GBR\_RoyalMail\_Udprn  
The Unique Delivery Point Reference Number (UDPRN) is a unique, 8-digit code assigned by Royal Mail to addresses within the UK.