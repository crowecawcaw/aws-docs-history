# Sample rules

Following, you can find some example configurations of inbound and outbound rules for
Amazon RDS and Amazon Redshift.

## VPC connection rules: Amazon Quick Sight: Amazon RDS

for MySQL

The following tables show rule settings for connecting Amazon Quick Sight to Amazon RDS for MySQL.

Amazon Quick Sight Network interface security group: inbound rule| Type | All TCP |
| Protocol | TCP |
| Port Range | 0 - 65535 |
| Source | `sg-RDS11111111` |
| Description | Amazon Quick Sight - RDS MySQL | Amazon Quick Sight Network interface security group: outbound rule| Type | MYSQL/Aurora |
| Protocol | TCP |
| Port Range | 3306 |
| Source | sg-RDS11111111 |
| Description | Amazon Quick Sight to RDS MySQL | RDS MySQL: inbound rule| Type | MYSQL/Aurora |
| Protocol | TCP |
| Port Range | 3306 |
| Source | sg-ENI3333333 |
| Description | Amazon Quick Sight to RDS MySQL | ## VPC connection rules: Amazon Redshift in Amazon Quick Sight The following tables show rule settings for connecting Amazon Quick Sight to Amazon Redshift. Amazon Quick Sight network interface security group: inbound rule| Type | All TCP |
| Protocol | TCP |
| Port Range | 0 - 65535 |
| Source | sg-RedSh222222 |
| Description | Amazon Quick Sight–Amazon Redshift | Amazon Quick Sight network interface security group: outbound rule| Type | Amazon Redshift |
| Protocol | TCP |
| Port Range | 5439 |
| Source | sg-RedSh222222 |
| Description | Amazon Quick Sight–Amazon Redshift | Amazon Redshift: inbound rule| Type | Amazon Redshift |
| Protocol | TCP |
| Port Range | 5439 |
| Source | sg-ENI3333333 |
| Description | Amazon Quick Sight–Amazon Redshift |
