# Creating a BYOM DB instance for RDS for SQL Server

You can create BYOM instances through the Amazon RDS console or the AWS CLI.

**Console:** From the Create database page, you can create a BYOM instance the same way you would create a License Included (LI) instance. The console creates the BYOM engine version behind the scenes on your behalf. Note that building the engine version from your provided installation media adds approximately 20 minutes to the overall instance creation time.

To avoid this additional wait, you can pre-create the BYOM engine version from the Custom engine versions page. After the engine version is created, launching instances against it follows the same timeline as LI instances.

**CLI:** Through the AWS CLI, you first call `create-custom-db-engine-version` to create the BYOM engine version, then call `create-db-instance` to launch your database. This two-step process also applies when you modify existing BYOM instances to a new minor version: create the target BYOM engine version first, wait for it to reach `Available` status, and then call `modify-db-instance` to upgrade.

## Prerequisites

Before you create a BYOM DB instance, verify the following:

- You have completed the steps in [Creating and managing BYOM engine versions for RDS for SQL Server](sqlserver-byom-creating-cev.md "sqlserver-byom-creating-cev.md").

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") and open the Amazon RDS console.
2. In the navigation pane, choose **Databases**, then choose **Create database**.
3. For **Choose a database creation method**, choose **Full configuration**.
4. For **Engine options**, choose **Microsoft SQL Server**.
5. For **Templates**, choose **Production** or **Dev/Test** based on your use case.
6. For **Database management type**, choose **Amazon RDS**.
7. For **Edition**, choose **SQL Server Standard Edition** or **SQL Server Enterprise Edition**.
8. For **License model**, choose **BYOM (Bring Your Own Media)**.
9. For **Major engine version**, choose the SQL Server version that matches your installation media (for example, 2022 or 2025).
10. For **Minor engine version**, choose the target minor version (for example, `16.00.4175.1.v1` for SQL Server 2022, or `17.00.4045.5.v1` for SQL Server 2025).
11. For **DB instance identifier**, enter a unique name for your DB instance.
12. Configure the remaining settings (DB instance class, storage, connectivity, authentication, backups, and maintenance) as you would for a License Included instance.
13. Choose **Create database**.
    Amazon RDS creates the BYOM engine version automatically and launches your instance.

Use the `create-db-instance` command with `--license-model bring-your-own-media`:

```
aws rds create-db-instance \
    --engine sqlserver-ee \
    --engine-version 17.00.4045.5.v1 \
    --license-model bring-your-own-media \
    --db-instance-identifier my-byom-instance \
    --db-instance-class db.m7i.xlarge \
    --master-username admin \
    --master-user-password <password> \
    --allocated-storage 200 \
    --db-subnet-group-name my-subnet-group \
    --vpc-security-group-ids sg-0123456789abcdef0
```

## Verifying your BYOM DB instance

After you create the instance, verify that it uses the BYOM license model:

```
aws rds describe-db-instances \
    --db-instance-identifier my-byom-instance
```

In the response, confirm the following values:

- `"LicenseModel": "bring-your-own-media"` — The instance uses your own SQL Server license.
- `"Engine": "sqlserver-ee"` — The correct engine edition.
- `"EngineVersion": "17.00.4045.5.v1"` — The target engine version.

## Considerations

- If you have existing automation that creates DB instances without specifying `--license-model`, those workflows fail after you create a BYOM engine version for that engine version. Update your automation to include the `--license-model` parameter before you activate a BYOM engine version.
