

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Transform for mainframe Runtime Error codes related to Datasimplifier
<a name="ba-runtime-error-codes-d"></a>

Datasimplifier error codes, prefixed with `BA-D`


| Key | Severity | Text | Additional details | 
| --- | --- | --- | --- | 
| BA-D0001 | Fatal | Invalid parameterized GDG generation reference. Use signed integer format (-nnn to \+nnn) or 0. |  | 
| BA-D0002 | Warn | PROGRAM COLLATING SEQUENCE encoding %s differs from default COBOL encoding %s. String comparisons requiring specific collating sequence are not fully implemented. Review string comparisons that depend on a specific collating sequence; results may differ from the mainframe. |  | 
| BA-D1001 | Fatal | Invalid empty union: Union must contain at least one child field. Ensure Union field is well-formed and follows the expected structure. |  | 
| BA-D2001 | Fatal | Data size mismatch: Cannot copy size-prefixed data to target structure. The source contains %d bytes (including %d-byte prefix) but the target structure can only hold %d bytes. 1. Increase the size of the target structure fields to accommodate the data. 2. Verify the source data length is within expected bounds. 3. Check if the PL/I VARCHAR declaration matches the target structure size. |  | 
| BA-D2002 | Fatal | The utility method recordCount, corresponding to the EasyTrieve built-in RECORD-COUNT, is not implemented in the current version of the AWS Transform for mainframe Runtime. Avoid relying on RECORD-COUNT, or implement an equivalent count in application logic. |  | 
| BA-D2003 | Warn | The utility method readXmlFromFile, corresponding to the PL/I built-in PLISAXB, is currently partially implemented. Validate PLISAXB-based XML parsing results; unsupported cases may not behave as on the mainframe. |  | 
| BA-D2004 | Error | PLISAXB: Unexpected error: %s. Review the input parameters passed to the function. |  | 
| BA-D3001 | Fatal | Unexpected value for GS21 print mode function: %s. Verify the GS21 print-mode function value is one the runtime supports. |  | 
| BA-D3002 | Fatal | Unexpected value for GS21 print mode: %s. Verify the GS21 print-mode value is one the runtime supports. |  | 