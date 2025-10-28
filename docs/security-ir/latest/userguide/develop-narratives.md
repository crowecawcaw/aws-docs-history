# Develop narratives

During analysis and investigation, document the actions taken, analysis performed, and information
identified, to be used by the subsequent phases and ultimately a final report. These narratives should
be succinct and precise, confirming that relevant information is included to verify effective understanding
of the incident and to maintain an accurate timeline. They are also helpful when you engage people outside
of the core incident response team. Here is an example:

######

*The marketing and sales department received a ransom note on March 15th, 2022
demanding payment in cryptocurrency to avoid public posting of possible sensitive data.
The SOC determined that the Amazon RDS database belonging to marketing and sales was
publicly accessible on February 20th, 2022. The SOC queried RDS access logs and
determined that IP address 198.51.100.23 was used on February 20th, 2022 with the
credentials `mm03434` belonging to *Major Mary*, one of
the web developers. The SOC queried VPC Flow Logs and determined that approximately
256MB of data egressed to the same IP address at the same date (time stamp
2022-02-20T15:50+00Z). The SOC determined through open-source threat intelligence that
the credentials are currently available in plain text in the public repository
`https[:]//example[.]com/majormary/rds-utils`.*
