# Remediating exposure findings

The topics in this section describe remediation steps for exposure findings across different AWS services.

The `Remediation` field of the [OCSF
format](security-hub-v2-ocsf-findings.md "security-hub-v2-ocsf-findings.md") contains two fields: `remediation` and
`references`.

```
"Remediation": {
    "Recommendation": {
        "remediation":{"desc":"String",
        "references":["string array"]}
    }
},
```

###### Note

The remediation guidance provided in the following sections might require
additional consultation in other AWS resources.
