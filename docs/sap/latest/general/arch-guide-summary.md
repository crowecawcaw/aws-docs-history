# Summary

The table below summarizes the patterns and their key characteristics.

| #   | Single Region | Multi Region | Single AZ Primary | Multi AZ<br>Primary | Single AZ Second Region | Multi AZ Second Region | Prod Capacity in 2nd AZ | Use of non-prod capacity | Cross-Region data replication |
| --- | ------------- | ------------ | ----------------- | ------------------- | ----------------------- | ---------------------- | ----------------------- | ------------------------ | ----------------------------- |
| 1   | Yes           | No           | No                | Yes                 | No                      | No                     | Yes                     | No                       | No                            |
| 2   | Yes           | No           | No                | Yes                 | No                      | No                     | Yes                     | Yes                      | No                            |
| 3   | Yes           | No           | Yes               | No                  | No                      | No                     | No                      | Yes                      | No                            |
| 4   | Yes           | No           | Yes               | No                  | No                      | No                     | No                      | No                       | No                            |
| 5   | No            | Yes          | No                | Yes                 | Yes                     | No                     | Yes                     | No                       | Yes                           |
| 6   | No            | Yes          | No                | Yes                 | Yes                     | No                     | Yes                     | No                       | Yes                           |
| 7   | No            | Yes          | No                | Yes                 | No                      | Yes                    | Yes                     | No                       | Yes                           |
| 8   | No            | Yes          | Yes               | No                  | Yes                     | No                     | No                      | No                       | Yes                           |

**Table 1: Summary of patterns**

With the flexibility and agility of the AWS Cloud, you have the ability to select any of the patterns described in this guide. You can select the pattern that best meets the business requirements for your SAP systems. It saves you from the trouble of selecting the highest requirement and applying it to all production systems.

For example, if you require highly-available compute capacity in another Availability Zone for the production SAP database and central services tiers of your core ERP system and for your BW system, you can accept the variable time duration required to re-create the AWS resources in a different Availability Zone and restore the persistent data. In this case, you would select Pattern 3 for ERP and Pattern 1 for BW to reduce the overall TCO.

If your requirements change over time, it is possible to move to a different pattern without significant re-design. For example, during the earlier phases of an implementation project, you may not require highly-available compute capacity in another Availability Zone but you can deploy the capacity into a second Availability Zone a few weeks before go-live.

You should consider the following when selecting an architecture pattern to run your SAP system in AWS:

- The geographical residency of the data
- The impact of your production SAP systems' downtime on your organization
- The recovery time objective
- The recovery point objective
- The cost profile
