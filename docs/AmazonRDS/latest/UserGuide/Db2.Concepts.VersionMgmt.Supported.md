

# Upgrade management for Amazon RDS Db2 instances
<a name="Db2.Concepts.VersionMgmt.Supported"></a>

To see the current list of supported Db2 minor versions on RDS, use one of the following commands:

```
aws rds describe-db-engine-versions --engine {{db2-ae}}
aws rds describe-db-engine-versions --engine {{db2-ce}}
aws rds describe-db-engine-versions --engine {{db2-se}}
```

Amazon RDS also supports upgrade rollout policy to manage automatic minor version upgrades across multiple database resources and AWS accounts. For more information, see [Using AWS Organizations upgrade rollout policy for automatic minor version upgrades](RDS.Maintenance.AMVU.UpgradeRollout.md).

You can specify any currently supported Db2 version when creating a new DB instance. You can specify the major version (such as Db2 11.5) and any supported minor version for the specified major version. If no version is specified, Amazon RDS defaults to a supported version, typically the most recent version. If a major version is specified but a minor version is not, Amazon RDS defaults to a recent release of the major version that you have specified. To see a list of supported versions, as well as defaults for newly created DB instances, use the [ describe-db-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html) AWS Command Line Interface (AWS CLI) command. 

For example, to list the supported engine versions for Amazon RDS for Db2, run the following AWS CLI command. Replace {{region}} with your AWS Region.

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
    --filters Name=engine,Values=db2-ae,db2-ce,db2-se \
    --query "DBEngineVersions[].{Engine:Engine, EngineVersion:EngineVersion, DBParameterGroupFamily:DBParameterGroupFamily}" \
    --region {{region}}
```

For Windows:

```
aws rds describe-db-engine-versions ^
    --filters Name=engine,Values=db2-ae,db2-ce,db2-se ^
    --query "DBEngineVersions[].{Engine:Engine, EngineVersion:EngineVersion, DBParameterGroupFamily:DBParameterGroupFamily}" ^
    --region {{region}}
```

This command produces output similar to the following example:

```
[
    {
    "Engine": "db2-ae",
    "EngineVersion": "11.5.9.0.sb00000000.r1",
    "DBParameterGroupFamily": "db2-ae-11.5"
    },
    {
    "Engine": "db2-ce",
    "EngineVersion": "12.1.4.0.sb00080714.r1",
    "DBParameterGroupFamily": "db2-ce-12.1"
    },
    {
    "Engine": "db2-se",
    "EngineVersion": "11.5.9.0.sb00000000.r1",
    "DBParameterGroupFamily": "db2-se-11.5"
    }

]
```

The default Db2 version might vary by AWS Region. To create a DB instance with a specific minor version, specify the minor version during DB instance creation. You can determine the default version for an AWS Region for `db2-ae`, `db2-ce` and `db2-se` database engines by running the` describe-db-engine-versions` command. The following example returns the default version for `db2-ae` in US East (N. Virginia).

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
    --default-only --engine {{db2-ae}} \
    --query "DBEngineVersions[].{Engine:Engine, EngineVersion:EngineVersion, DBParameterGroupFamily:DBParameterGroupFamily}" \
    --region {{us-east-1}}
```

For Windows:

```
aws rds describe-db-engine-versions ^
    --default-only --engine {{db2-ae}} ^
    --query "DBEngineVersions[].{Engine:Engine, EngineVersion:EngineVersion, DBParameterGroupFamily:DBParameterGroupFamily}" ^
    --region {{us-east-1}}
```

This command produces output similar to the following example:

```
[
    {
    "Engine": "db2-ae",
    "EngineVersion": "12.1.4.0.sb00080714.r1",
    "DBParameterGroupFamily": "db2-ae-12.1"
    }
]
```

When automatic minor version upgrade is enabled, Amazon RDS automatically upgrades your DB instances to new Db2 minor versions as they are supported by Amazon RDS. This patching occurs during your scheduled maintenance window. You can modify a DB instance to enable or disable automatic minor version upgrades. 

If you opt out of automatically scheduled upgrades, you can manually upgrade to a supported minor version release by following the same procedure as you would for a major version update. For information, see [Upgrading a DB instance engine version](USER_UpgradeDBInstance.Upgrading.md). 