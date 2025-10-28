# Constructing an ARN for Neptune

You can construct an ARN for an Amazon Neptune resource using the following syntax.
Note that Neptune shares the format of Amazon RDS ARNs.

`arn:aws:rds:`<region>`:`<account number>`:`<resourcetype>`:`<name>``

The following table shows the format that you should use when constructing an ARN for a
particular Neptune administrative resource type.

| Resource Type              | ARN Format                                                                                                                                                     |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DB instance                | arn:aws:rds:`<region>`:`<account>``:db:``<name>` For example: `` arn:aws:rds:`us-east-2`:`123456789012`:db:`my-instance-1` ``                                  |
| DB cluster                 | arn:aws:rds:`<region>`:`<account>``:cluster:``<name>` For example: `` arn:aws:rds:`us-east-2`:`123456789012`:cluster:`my-cluster-1` ``                         |
| Event subscription         | arn:aws:rds:`<region>`:`<account>``:es:``<name>` For example: `` arn:aws:rds:`us-east-2`:`123456789012`:es:`my-subscription` ``                                |
| DB parameter group         | arn:aws:rds:`<region>`:`<account>``:pg:``<name>` For example: `` arn:aws:rds:`us-east-2`:`123456789012`:pg:`my-param-enable-logs` ``                           |
| DB cluster parameter group | arn:aws:rds:`<region>`:`<account>``:cluster-pg:``<name>` For example: `` arn:aws:rds:`us-east-2`:`123456789012`:cluster-pg:`my-cluster-param-timezone` ``      |
| DB cluster snapshot        | arn:aws:`rds:``<region>`:`<account>``:cluster-snapshot:``<name>` For example: `` arn:aws:rds:`us-east-2`:`123456789012`:cluster-snapshot:`my-snap-20160809` `` |
| DB subnet group            | arn:aws:`rds:``<region>`:`<account>``:subgrp:``<name>` For example: `` arn:aws:rds:`us-east-2`:`123456789012`:subgrp:`my-subnet-10` ``                         |
