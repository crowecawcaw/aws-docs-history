AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime Error Codes related to ADABAS

ADABAS-specific error codes, prefixed with `BA-N`.

## ADASTRIP Utility Error Codes

| Key        | Severity | Text                                                                               | Additional details                                          |
| ---------- | -------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `BA-N1000` | Fatal    | Invalid `ADASTRIP` Field entry: expected type `'FieldFormat'` but received `'%s'`. | Field series are not supported by `ADASTRIP` (Ex: 'AA-AD'). |
