AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime Error Codes related to Utility Programs

Utility pgm error codes, prefixed with `BA-U`.

| Key        | Severity | Text                                                                                                                                                              | Additional details |
| ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-U1001` | Warn     | Input lilian seconds scale exceeds maximum scale. Maximum scale will be used instead.                                                                             |                    |
| `BA-U2001` | Error    | Failed to process TrailerItem subclass encountered. Ensure the trailer item is supported.                                                                         |                    |
| `BA-U2002` | Error    | Failed to parse TrailerItem argument. Ensure the trailer item arguments is supported.                                                                             |                    |
| `BA-U2003` | Error    | Failed to process the DFSORT date format argument. Ensure the date format argument is supported.                                                                  |                    |
| `BA-U2004` | Error    | Invalid input while extracting the Header1 from SortGrammar. Ensure Header1 string is well-formed and follows the expected structure.                             |                    |
| `BA-U2005` | Error    | Unexpected error while processing SortGrammar. Review exception details and verify input integrity and grammar parsing logic.                                     |                    |
| `BA-U2006` | Error    | Feedback code CEE2F3: Failed to retrieve current system date and time. Check system clock configuration and timezone settings.                                    |                    |
| `BA-U2007` | Error    | Feedback code CEE2EC: Failed to parse the date value passed to CEEDAYS or CEESECS. Ensure the date format is supported.                                           |                    |
| `BA-U2008` | Error    | Feedback code CEE2EH: Input date/time in a CEEISEC, CEEDAYS, or CEESECS call was not within the valid range. Ensure the input date is within the supported range. |                    |
| `BA-U2009` | Error    | Feedback code CEE2EM: Failed to parse an input picture string in a call to a date/time service. Ensure the picture format is supported.                           |                    |
| `BA-U2010` | Error    | Feedback code CEE2EG: Input lilian date value was not within the valid range. Ensure the input lilian date is within the supported range.                         |                    |
| `BA-U2011` | Fatal    | Number of arguments received does not match expected number of arguments. Ensure the correct number of arguments is passed to the called program.                 |                    |
