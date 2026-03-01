# Prerequisites for a Multi-AZ deployment in RDS Custom for Oracle

A Multi-AZ deployment for RDS Custom for Oracle is different from Multi-AZ for RDS for Oracle. Unlike Multi-AZ for
RDS for Oracle, you must meet the prerequisites for RDS Custom for Oracle before you create your Multi-AZ
DB instance. This is because RDS Custom runs inside your own account, which requires permissions.
Also, you need to create the Multi-AZ instance on the CEV with the latest
service-provided AMI, which supports the Multi-AZ deployments.

If you don't complete the prerequisites, your Multi-AZ DB instance might fail to run, or
automatically revert to a Single-AZ DB instance. For more information about prerequisites, see
Prerequisites for a Multi-AZ deployment in RDS Custom for Oracle.

RDS Custom for Oracle requires specific prerequisites when converting from Single-AZ to Multi-AZ
deployment. Incomplete prerequisites cause Multi-AZ setup to fail. Use either manual
setup or the latest CloudFormation template file provided in the network setup instructions. For
more information, see [Step 3: Extract the CloudFormation templates for RDS Custom for Oracle](custom-setup-orcl.md#custom-setup-orcl.cf.downloading "custom-setup-orcl.md#custom-setup-orcl.cf.downloading").

To complete the prerequisites manually, follow the steps in [Converting a Single-AZ deployment to a Multi-AZ deployment in RDS Custom for Oracle](custom-oracle-multiaz-modify-single-to-multi.md "custom-oracle-multiaz-modify-single-to-multi.md") and note the
following:

- Make sure your RDS Custom for Oracle DB instance uses a CEV created after June 30, 2025 with the
  latest service-provided AMI.
- Update the Amazon RDS security group inbound and outbound rules to allow port 1120.
- Create new Amazon SQS VPC endpoints that allow the Amazon RDS RDS Custom for Oracle DB
  instance to communicate with Amazon SQS.
- Update the Amazon SQS permissions in the instance profile role.

###### Important

Don't reboot your Multi-AZ primary DB instance manually by logging into the instance
without pausing RDS Custom for Oracle automation.

## Migration steps for DB instances using CEVs created before June 30, 2025

If you created your RDS Custom for Oracle DB instance before June 30, 2025, you can't directly modify it
to Multi-AZ deployment because the underlying CEV was built with an older service-provided AMI
that lacks Multi-AZ support. You must migrate your database to a new instance using a
CEV you create after June 30, 2025. Do the following for the migration.

1. **Create CEV from source** with the latest
   service-provided AMI (after June 30, 2025).
2. **Launch a new DB instance** with the new CEV.
3. **Migrate your database** from the existing DB
   instance that doesn’t support Multi-AZ deployment to the newly created instance using one
   of following methods:
   - [Physical migration of Oracle databases to Amazon RDS Custom using
     Data Guard](https://aws.amazon.com/blogs//database/physical-migration-of-oracle-databases-to-amazon-rds-custom-using-data-guard/ "https://aws.amazon.com/blogs//database/physical-migration-of-oracle-databases-to-amazon-rds-custom-using-data-guard/")
   - [Physical migration of Oracle databases to Amazon RDS Custom using
     RMAN duplication](https://aws.amazon.com/blogs//database/physical-migration-of-oracle-databases-to-amazon-rds-custom-using-rman-duplication/ "https://aws.amazon.com/blogs//database/physical-migration-of-oracle-databases-to-amazon-rds-custom-using-rman-duplication/")
