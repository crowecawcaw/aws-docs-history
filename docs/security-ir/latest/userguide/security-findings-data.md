

# Security findings data
<a name="security-findings-data"></a>

 Security Incident Response continuously ingests security findings metadata from Amazon GuardDuty and AWS Security Hub CSPM across all supported AWS Regions where you have enabled these services. This findings data includes resource identifiers, finding types, severity levels, affected resources, and detection timestamps. Unlike case investigation data, findings data is ingested automatically and continuously to enable Security Incident Response to correlate threats across your entire AWS environment. 

 The findings data does not include the detailed logs or raw data that generated the findings—only the metadata about what was detected, where it was detected, and the severity of the detection. This metadata enables Security Incident Response to identify patterns, correlate related security events across Regions, and provide comprehensive threat analysis. 