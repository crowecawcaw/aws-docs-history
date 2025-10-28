# DRHCREL03-BP01 Use AWS Outposts or Local Zones for scenarios where data must reside within a country or jurisdiction without a local AWS Region

To meet data residency requirements in Regions without local AWS
infrastructure, leverage AWS Outposts across multiple locations or
AWS Local Zones with redundancy, while utilizing services like
Amazon S3 on Outposts for resilient local data management.

**Desired outcome:** Achieve
seamless integration of AWS Cloud capabilities into local
operations while maintaining strict adherence to data residency
requirements even in countries with no AWS Regions.

**Benefits of establishing this best
practice:** AWS Outposts and Local Zones enable
organizations to use AWS services while keeping data within
specific geographical boundaries, facilitating compliance with
local data sovereignty laws and regulations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

When data must remain within the country and a local AWS Region
isn't available, deploy on Outposts in different physical
locations with redundant power and network sources or AWS Local
Zones. Use services like Amazon S3 on Outposts for backup and
recovery to achieve high availability while adhering to data
residency regulations.
