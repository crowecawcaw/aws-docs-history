

# Prepare input data
<a name="preparing-input-data"></a>

Format your input data as [Apache Parquet](https://parquet.apache.org/docs/overview/) files following the required schema for the job action type you want to perform. Each action type has its own schema requirements that define the fields your input data must include.

## Input schema overview
<a name="input-schema-overview"></a>

Your input data must conform to the schema for the specific job action type you want to run. Each action type defines its own set of required and optional fields.

All input schemas support an optional `Id` field. Use this field to assign an identifier to each input record. If you provide an `Id` value, it appears as `Input_Id` in the output, allowing you to correlate output records with their corresponding inputs.

For address validation input schema details, see [Address validation input schema](address-validation-concepts.md#address-validation-input-schema).

## File size limits
<a name="input-file-limits"></a>

Input files have the following limitations:
+ Maximum file size: 10 GB per file
+ Maximum Parquet row-group size: 1 GB
+ Maximum files per input prefix: 1000