

# Reading from Avalara entities

**Prerequisites**

An Avalara object you want to read from. See the supported entities table below for the available entities.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| companies | No | Yes | Yes | No | No | 
| accounts | No | Yes | Yes | No | No | 
| locations | No | Yes | Yes | No | No | 
| nexus | No | Yes | Yes | No | No | 
| users | No | Yes | Yes | No | No | 
| contacts | No | Yes | Yes | No | No | 
| transactions | Yes | Yes | Yes | No | No | 
| service-types | No | Yes | Yes | No | No | 
| definition-countries | No | Yes | Yes | No | No | 
| definition-currencies | No | Yes | Yes | No | No | 
| definition-entityusecodes | No | Yes | Yes | No | No | 
| definition-filingfrequencies | No | Yes | Yes | No | No | 
| definition-nexustaxtypegroups | No | Yes | Yes | No | No | 
| definition-preferredprograms | No | Yes | Yes | No | No | 
| definition-regions | No | Yes | Yes | No | No | 
| definition-taxauthorities | No | Yes | Yes | No | No | 
| definition-taxauthoritytypes | No | Yes | Yes | No | No | 
| definition-taxcodes | No | Yes | Yes | No | No | 
| definition-taxsubtypes | No | Yes | Yes | No | No | 
| definition-taxtypegroups | No | Yes | Yes | No | No | 
| definition-unitofbasis | No | Yes | Yes | No | No | 
| definition-unitofmeasurements | No | Yes | Yes | No | No | 
| items | No | Yes | Yes | No | No | 
| tax-codes | No | Yes | Yes | No | No | 
| tax-rules | No | Yes | Yes | No | No | 
| distance-thresholds | No | Yes | Yes | No | No | 
| companies-nexus-bytaxtypegroup | No | Yes | Yes | No | No | 
| definitions-countries-ratetypes | No | Yes | Yes | No | No | 
| definitions-countries-regions | No | Yes | Yes | No | No | 
| definition-taxauthorityforms | No | Yes | Yes | No | No | 
| definition-postalcodes | No | Yes | Yes | No | No | 
| definition-jurisdictions | No | Yes | Yes | No | No | 
| definition-jurisdictions-hierarchy | No | Yes | Yes | No | No | 
| definition-taxforms | No | Yes | Yes | No | No | 
| definition-nexus | No | Yes | Yes | No | No | 

**Example – Reading from an Avalara entity**  
The following example reads from the `companies` entity. Replace {{connectionName}} with the name of your Avalara connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="avalara",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "companies"
    }
)
```