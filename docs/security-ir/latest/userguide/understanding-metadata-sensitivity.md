

# Understanding metadata sensitivity
<a name="understanding-metadata-sensitivity"></a>

 While Security Incident Response doesn't collect your application data, the metadata it collects across all three categories can reveal sensitive information about your environment and potentially your users. Consider the following examples: 
+  Resource names such as `patient-database-prod` or `financial-records-2026` indicate the purpose and sensitivity of resources. 
+  DNS queries like `user12345.internal.app.com` may contain user identifiers or internal system information. 
+  API call patterns can reveal business processes and operational workflows. 

 Organizations in regulated industries should evaluate whether this metadata falls under their compliance requirements, even though it isn't the regulated data itself. 