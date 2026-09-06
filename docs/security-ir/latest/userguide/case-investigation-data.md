

# Case investigation data
<a name="case-investigation-data"></a>

 When you open a security incident case, Security Incident Response collects logs and metadata from your AWS environment to support the investigation. This case-specific data includes API logs, VPC Flow Logs, Amazon Route 53 DNS queries, Amazon S3 access events, resource metadata (names, tags, and configuration details), and case information such as comments and investigation notes. 

**Important**  
 Security Incident Response collects information about your environment's activity patterns and resource configurations. It does not collect the actual contents of your Amazon S3 buckets, database records, or application data. Security Incident Response collects the "who did what and when" rather than the underlying data itself. 

 This case investigation data is collected on-demand for specific incidents and remains associated with your case. Security Incident Response retains this data for 90 days by default to allow you to review investigation history, support ongoing or follow-up investigations, and meet audit and compliance documentation requirements. If you require data deletion before the 90-day period expires, contact AWS Support to request early deletion. 