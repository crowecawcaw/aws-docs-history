# Appendix A: Points of contact and critical information

Complete the following table and provide it to your AWS account team before deployment. This information enables Security Incident Response Engineering to reach the right people quickly during a security event.

| IR and SOC Personnel Contact Information | Entry                                         | IR      | SOC Personnel: Role, Name, Email | Primary, Secondary Escalation Contacts | Internal, Known CIDR Ranges | External, Known CIDR Ranges | Additional Cloud Service Providers | Working AWS Regions                   | DNS Server IPs (if other than Amazon Route 53 Resolver) | VPN        | Remote Access Solutions and IPs | Critical Application Names | Account Numbers | Uncommon Ports Commonly Used | EDR | AV  | Vulnerability Management Tools Used | IDP | Locations |
| ---------------------------------------- | --------------------------------------------- | ------- | -------------------------------- | -------------------------------------- | --------------------------- | --------------------------- | ---------------------------------- | ------------------------------------- | ------------------------------------------------------- | ---------- | ------------------------------- | -------------------------- | --------------- | ---------------------------- | --- | --- | ----------------------------------- | --- | --------- |
| 1                                        | SOC Commander, John Smith, jsmith@example.com | Primary | 10.0.0.0/16                      | 5.5.60.0/20 (Azure)                    | Azure                       | us-east-1, us-east-2        | N/A                                | Direct Connect, Public VIF 116.32.8.7 | Nginx Webserver (Example Critical)                      | 1234567890 | 8080                            | CrowdStrike Falcon         | Entra, Azure    |

###### To submit this inforamtion, complete the following steps:

1. Complete the preceding metadata table with your environment information.
2. Create an [AWS Support case](https://repost.aws/knowledge-center/get-aws-technical-support "https://repost.aws/knowledge-center/get-aws-technical-support") with the following details:

   - **Case type:** Technical
   - **Service:** Security Incident Response
   - **Category:** Other

3. Attach the completed metadata table to the case.
