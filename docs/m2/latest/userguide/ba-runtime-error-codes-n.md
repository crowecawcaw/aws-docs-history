

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Transform for mainframe Runtime Error Codes related to ADABAS
<a name="ba-runtime-error-codes-n"></a>

ADABAS-specific error codes, prefixed with `BA-N`.

## ADASTRIP Utility Error Codes
<a name="adastrip-utility-errors"></a>


| Key | Severity | Text | Additional details | 
| --- | --- | --- | --- | 
| BA-N0001 | Fatal | Invalid ADASTRIP Field entry: expected type 'FieldFormat' but received '%s'. | Field series are not supported by ADASTRIP (Ex: 'AA-AD'). | 
| BA-N0002 | Error | Unsupported field type '%s' in PE (Periodic Group) field processing. |  | 
| BA-N0003 | Fatal | Missing required MODE parameter in ADASTRIP. Add MODE parameter to your ADASTRIP card. Example syntax: 'MODE DUMP'. |  | 
| BA-N0004 | Fatal | Invalid MODE value '%s' in ADASTRIP card. Only 'DUMP' or 'ADASEL' are currently supported. Set 'MODE DUMP' to sort fields by FDT order (default behavior), or 'MODE ADASEL' to preserve field order as specified in STRIP card. |  | 
| BA-N0005 | Fatal | Invalid ADASTRIP INDEX limit. Field: '%s', Limit: '%s'. INDEX syntax requires numeric limits followed by field names. Example: 'INDEX 5 FIELD1 FIELD2 10 FIELD3'. |  | 
| BA-N0006 | Fatal | Missing required argument '%s' in ADABAS call. Verify the ADABAS call parameters. Ensure all required buffers and arguments are provided according to the ADABAS command syntax. |  | 
| BA-N0007 | Fatal | Cannot read past record buffer specified length. The field definition exceeds the record buffer size. Verify the record length matches the FDT definition. |  | 
| BA-N0008 | Fatal | Missing value for field type '%s'. |  | 
| BA-N0009 | Fatal | Invalid ADASTRIP TYPE override format '%s' for field '%s'. Only 'P' (Packed) or 'U' (Unpacked) are allowed. Use TYPE to override field formats. Example: 'TYPE P FIELD1 U FIELD2' to convert FIELD1 to Packed and FIELD2 to Unpacked decimal. |  | 
| BA-N0020 | Fatal | Unsupported field format '%s' in search buffer. This field format is not currently supported in ADABAS search operations. |  | 
| BA-N0021 | Fatal | Unhandled field type '%s' in search buffer. This field type is not currently supported in ADABAS search operations. |  | 
| BA-N0022 | Fatal | Field selection criteria are not supported in format buffer. Check for field selection criteria like 'AA(S)' or 'AB(D)' in the format buffer definition. |  | 
| BA-N0023 | Fatal | Literals in format buffer are not supported. Check for literal values in format buffer. Example: 'AA,"TEXT",AB' contains a literal "TEXT". |  | 
| BA-N0024 | Fatal | Unhandled record format type '%s' in format buffer. Verify the format buffer syntax and field definitions. |  | 
| BA-N0025 | Fatal | Unhandled indexed field type '%s'. Check for complex expressions with index notation. Example: field series like '(AA-AD)(1)' are not supported. |  | 
| BA-N0026 | Fatal | Unhandled field format '%s'. Check the FDT field definition for this format type. |  | 
| BA-N0027 | Fatal | Unhandled FieldOccurencesRange inner format type '%s'. Check the periodic group field definition in format buffer for complex occurrence ranges. |  | 
| BA-N0028 | Fatal | Unhandled unpacked decimal conversion for field '%s' from length %d to %d. Check the field length definitions in the FDT and format buffer. |  | 
| BA-N0029 | Fatal | Unhandled field type '%s' for update operation. Check the field definition in the format buffer. |  | 
| BA-N0030 | Fatal | Unhandled field format conversion for field '%s' from '%s' to '%s'. Check the field format in the FDT and the target format in the format buffer or TYPE override. |  | 
| BA-N0031 | Fatal | Failed to sync Oracle sequence after batch commit for fileNumber '%s'. Verify Oracle sequence exists and the user has ALTER SEQUENCE privileges. The transaction has been rolled back. |  | 
| BA-N0032 | Fatal | Unhandled SQL exception during batch commit: '%s'. Check the database logs for details. The batch operation has failed. |  | 
| BA-N0033 | Fatal | No active ISN counter for key '%s'. Ensure a batch insert (NP) has been initiated before attempting to retrieve the next ISN. |  | 
| BA-N0034 | Warn | Unique descriptor insert failed; value already exists in the table. An attempt was made to duplicate a descriptor value for a unique descriptor. |  | 
| BA-N0035 | Error | Failed during batch commit sync/commit: '%s'. Check the database logs and Oracle sequence privileges. The transaction has been rolled back. |  | 
| BA-N0036 | Warn | ISN counter already active for key '%s' with current value '%s'. A batch insert counter was re-initialized before the previous one was deactivated. The previous ISN range may not be synced to the Oracle sequence. |  | 
| BA-N0037 | Fatal | Required table ADABAS\_ET\_USER\_DATA not found in the database. Create the ADABAS\_ET\_USER\_DATA table before starting the application. ET/RE commands (job restartability) require this table. |  | 
| BA-N0038 | Fatal | Failed to store ET user data for user '%s': %s Check the database connection and verify the ADABAS\_ET\_USER\_DATA table exists and is accessible. |  | 