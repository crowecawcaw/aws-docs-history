# Constructing an ARN for Neptune

You can construct an ARN for an Amazon Neptune resource using the following syntax.
Note that Neptune shares the format of Amazon RDS ARNs.

`arn:aws:rds:`<region>`:`<account number>`:`<resourcetype>`:`<name>``

The following table shows the format that you should use when constructing an ARN for a
particular Neptune administrative resource type.

| Resource Type              | ARN Format                                                                                                                                                                 |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DB instance                | arn:aws:rds:`<region>`:`<account>``:db:``<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:db:`my-instance-1`<br>``                                  |
| DB cluster                 | arn:aws:rds:`<region>`:`<account>``:cluster:``<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:cluster:`my-cluster-1`<br>``                         |
| Event subscription         | arn:aws:rds:`<region>`:`<account>``:es:``<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:es:`my-subscription`<br>``                                |
| DB parameter group         | arn:aws:rds:`<region>`:`<account>``:pg:``<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:pg:`my-param-enable-logs`<br>``                           |
| DB cluster parameter group | arn:aws:rds:`<region>`:`<account>``:cluster-pg:``<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:cluster-pg:`my-cluster-param-timezone`<br>``      |
| DB cluster snapshot        | arn:aws:`rds:``<region>`:`<account>``:cluster-snapshot:``<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:cluster-snapshot:`my-snap-20160809`<br>`` |
| DB subnet group            | arn:aws:`rds:``<region>`:`<account>``:subgrp:``<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:subgrp:`my-subnet-10`<br>``                         |
