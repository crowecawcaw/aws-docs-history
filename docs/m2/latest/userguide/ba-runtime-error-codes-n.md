After careful consideration, we have made the decision to close new customer access to **AWS Mainframe Modernization self-managed experience**,
effective June 30, 2026. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for
AWS Mainframe Modernization self-managed experience, but we do not plan to introduce new features. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Transform for mainframe Runtime Error Codes related to ADABAS

ADABAS-specific error codes, prefixed with `BA-N`.

## ADASTRIP Utility Error Codes

| Key        | Severity | Text                                                                               | Additional details                                          |
| ---------- | -------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `BA-N1000` | Fatal    | Invalid `ADASTRIP` Field entry: expected type `'FieldFormat'` but received `'%s'`. | Field series are not supported by `ADASTRIP` (Ex: 'AA-AD'). |
