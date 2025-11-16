# Subnets and subnet groups

A _subnet group_ is a collection of subnets (typically private)
that you can designate for your clusters running in an Amazon Virtual Private Cloud (VPC) environment.

When you create a cluster in an Amazon VPC, you can specify a subnet group or use the default one provided.
MemoryDB uses that subnet group to choose a subnet and IP addresses within that
subnet to associate with your nodes.

This section covers how to create and leverage subnets and subnet groups
to manage access to your MemoryDB resources.

For more information about subnet group usage in an Amazon VPC environment,
see [Step 3: Authorize access to the cluster](getting-started.md#getting-started.authorizeaccess "getting-started.md#getting-started.authorizeaccess").

| Supported MemoryDB AZ IDs                           | Region Name/Region                                 | Supported AZ IDs |
| --------------------------------------------------- | -------------------------------------------------- | ---------------- |
| US East (Ohio) Region<br>`us-east-2`                | `use2-az1, use2-az2, use2-az3`                     |
| US East (N. Virginia) Region<br>`us-east-1`         | `use1-az1, use1-az2, use1-az4, use1-az5, use1-az6` |
| US West (N. California) Region<br>`us-west-1`       | `usw1-az1, usw1-az2, usw1-az3`                     |
| US West (Oregon) Region<br>`us-west-2`              | `usw2-az1, usw2-az2, usw2-az3, usw2-az4`           |
| Canada (Central) Region<br>`ca-central-1`           | `cac1-az1, cac1-az2, cac1-az4`                     |
| Asia Pacific (Hong Kong) Region<br>`ap-east-1`      | `ape1-az1, ape1-az2, ape1-az3`                     |
| Asia Pacific (Mumbai) Region<br>`ap-south-1`        | `aps1-az1, aps1-az2, aps1-az3`                     |
| Asia Pacific (Tokyo) Region<br>`ap-northeast-1`     | `apne1-az1, apne1-az2, apne1-az4`                  |
| Asia Pacific (Seoul) Region<br>`ap-northeast-2`     | `apne2-az1, apne2-az2, apne2-az3`                  |
| Asia Pacific (Singapore) Region<br>`ap-southeast-1` | `apse1-az1, apse1-az2, apse1-az3`                  |
| Asia Pacific (Sydney) Region<br>`ap-southeast-2`    | `apse2-az1, apse2-az2, apse2-az3`                  |
| Europe (Frankfurt) Region<br>`eu-central-1`         | `euc1-az1, euc1-az2, euc1-az3`                     |
| Europe (Ireland) Region<br>`eu-west-1`              | `euw1-az1, euw1-az2, euw1-az3`                     |
| Europe (London) Region<br>`eu-west-2`               | `euw2-az1, euw2-az2, euw2-az3`                     |
| EU (Paris) Region<br>`eu-west-3`                    | `euw3-az1, euw3-az2, euw3-az3`                     |
| Europe (Stockholm) Region<br>`eu-north-1`           | `eun1-az1, eun1-az2, eun1-az3`                     |
| Europe (Milan) Region<br>`eu-south-1`               | `eus1-az1, eus1-az2, eus1-az3`                     |
| South America (São Paulo) Region<br>`sa-east-1`     | `sae1-az1, sae1-az2, sae1-az3`                     |
| China (Beijing) Region<br>`cn-north-1`              | `cnn1-az1, cnn1-az2`                               |
| China (Ningxia) Region<br>`cn-northwest-1`          | `cnw1-az1, cnw1-az2, cnw1-az3`                     |
| `us-gov-east-1`                                     | `usge1-az1, usge1-az2, usge1-az3`                  |
| `us-gov-west-1`                                     | `usgw1-az1, usgw1-az2, usgw1-az3`                  |
| Europe (Spain) Region<br>`eu-south-2`               | `eus2-az1, eus2-az2, eus2-az3`                     |

###### Topics

- [MemoryDB and IPV6](subnetgroups.md "subnetgroups.md")
- [Creating a subnet group](subnetgroups.md "subnetgroups.md")
- [Updating a subnet group](subnetgroups.md "subnetgroups.md")
- [Viewing subnet group details](subnetgroups.md "subnetgroups.md")
- [Deleting a subnet group](subnetgroups.md "subnetgroups.md")
