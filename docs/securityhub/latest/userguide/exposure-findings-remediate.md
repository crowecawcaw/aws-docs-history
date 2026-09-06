

# Remediating exposure findings
<a name="exposure-findings-remediate"></a>

 The topics in this section describe remediation steps for exposure findings across different AWS services. 

 The `Remediation` field of the [OCSF format](https://docs.aws.amazon.com/securityhub/latest/userguide/security-hub-v2-ocsf-findings.html) contains two fields: `remediation` and `references`. 

```
"Remediation": {
    "Recommendation": {
        "remediation":{"desc":"String", 
        "references":["string array"]}
    }
},
```

**Note**  
The remediation guidance provided in the following sections might require additional consultation in other AWS resources. 