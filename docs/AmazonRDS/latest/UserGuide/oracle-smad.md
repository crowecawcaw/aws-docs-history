

# Working with self-managed Active Directory with an Amazon RDS for Oracle DB instance
<a name="oracle-smad"></a>

Amazon RDS for Oracle integrates with your self-managed Microsoft Active Directory (AD) domain. Your AD can run in your data center, on Amazon Elastic Compute Cloud (EC2), or with another cloud provider. With this integration, users in your AD authenticate to your Amazon RDS for Oracle DB instance with the Kerberos protocol, eliminating the need for complex intermediary domains or forest trusts. When a user connects with a Kerberos ticket issued by your domain controllers, RDS for Oracle validates the ticket against a service key that Amazon RDS registers in your domain. You keep your existing identity management structure while you use the managed database capabilities of Amazon RDS.

Kerberos authentication is additive. Joining a DB instance to your domain doesn’t change how existing database users sign in. The master user and any user created with `IDENTIFIED BY` continue to authenticate with passwords. To allow an Active Directory user to connect, you create an externally identified Oracle user that maps to that user.

**Topics**
+ [Region and version availability](#oracle-smad.region-version)
+ [Limitations](#oracle-smad.limitations)
+ [Considerations](#oracle-smad.considerations)
+ [Viewing the status of domain membership](#oracle-smad.domain-status)
+ [Requirements for self-managed Active Directory](oracle-smad-requirements.md)
+ [Setting up self-managed Active Directory](oracle-smad-setting-up.md)
+ [Configuring a Kerberos client and connecting to your DB instance](oracle-smad-connecting.md)
+ [Managing a DB instance in a self-managed Active Directory domain](oracle-smad-managing.md)
+ [Troubleshooting self-managed Active Directory for Amazon RDS for Oracle](oracle-smad-troubleshooting.md)

## Region and version availability
<a name="oracle-smad.region-version"></a>

Amazon RDS for Oracle supports self-managed AD using Kerberos in all commercial AWS Regions.

## Limitations
<a name="oracle-smad.limitations"></a>

The following limitations apply to RDS for Oracle DB instances joined to a self-managed AD domain:
+ **Per-user authorization.** Each AD user who connects must have a matching Oracle user created with `IDENTIFIED EXTERNALLY`. Amazon RDS for Oracle doesn’t map AD groups to Oracle roles or schemas.
+ **Kerberos encryption types.** Amazon RDS registers its service account with the AES128-CTS-HMAC-SHA1-96 and AES256-CTS-HMAC-SHA1-96 encryption types and doesn’t support RC4 or DES, so your domain controllers must allow at least one of these AES types.

## Considerations
<a name="oracle-smad.considerations"></a>

Keep the following in mind when you use self-managed AD with your DB instance.
+ **Domain join isn’t inherited.** A DB instance created from a snapshot, restored to a point in time, or created as a read replica doesn’t inherit the domain membership of its source. To join the new DB instance, specify the domain parameters on the restore or replica command. For details, see [Step 1: Create or modify an Amazon RDS for Oracle DB instance](oracle-smad-connecting.md#oracle-smad.connecting.step1).
+ **Switchover between domains.** If a read replica is joined to a different domain than its primary DB instance, Kerberos authentication on the new primary is validated against the replica’s domain after you switch over. Amazon RDS for Oracle matches a Kerberos login to a database user by its full principal name, including the realm. Users and applications that connect with a principal from the original domain can’t authenticate after the switchover unless each affected user also exists in the replica’s domain and you create a matching database user on the primary DB instance, or you configure a trust relationship between the two domains. Users who authenticate with a password aren’t affected.
+ **Customer-managed network.** You are responsible for connectivity between your virtual private cloud (VPC) and your domain controllers. If the DB instance loses connectivity to your domain controllers, Kerberos authentication stops working until you restore connectivity.
+ **Best-effort join.** If Amazon RDS can’t join the DB instance to your domain, the DB instance remains available with password authentication, and Amazon RDS reports the failure in the domain membership status and in an RDS event. Follow the failure details in the RDS event to fix the configuration, then retry the join.

We recommend that you do the following:
+ Create a dedicated Organizational Unit (OU) and a dedicated domain service account for each AWS account that owns domain-joined RDS for Oracle DB instances. This follows the principle of least privilege and keeps permissions from overlapping.
+ Subscribe to RDS event notifications for your DB instances so that you learn about domain connectivity or credential problems when they occur. For more information, see [Working with Amazon RDS event notification](USER_Events.html).
+ The master user always uses password authentication, so you can still manage the DB instance if your domain is unreachable. If you grant administrative privileges to other users, keep at least one of them on password authentication as well.

## Viewing the status of domain membership
<a name="oracle-smad.domain-status"></a>

After you create, modify, or restore a DB instance with self-managed AD parameters, Amazon RDS joins the DB instance to your domain. The AWS Management Console shows the status of the domain membership on the **Connectivity & security** tab of the DB instance details page. You can also view the status in the `DomainMemberships` field of the [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) output. The status can be one of the following:
+ `kerberos-enabled` – The DB instance has Kerberos authentication enabled.
+ `enabling-kerberos` – AWS is in the process of enabling Kerberos authentication on this DB instance.
+ `pending-enable-kerberos` – Enabling Kerberos authentication is pending on this DB instance.
+ `pending-maintenance-enable-kerberos` – AWS will attempt to enable Kerberos authentication on the DB instance during the next scheduled maintenance window.
+ `pending-disable-kerberos` – Disabling Kerberos authentication is pending on this DB instance.
+ `pending-maintenance-disable-kerberos` – AWS will attempt to disable Kerberos authentication on the DB instance during the next scheduled maintenance window.
+ `enable-kerberos-failed` – A configuration problem has prevented AWS from enabling Kerberos authentication on the DB instance. Correct the configuration problem before reissuing the command to modify the DB instance.
+ `disabling-kerberos` – AWS is in the process of disabling Kerberos authentication on this DB instance.

When Amazon RDS finishes removing a DB instance from the domain, the `DomainMemberships` list is empty.

The following example shows the `DomainMemberships` output for a DB instance that joined a self-managed AD domain.

```
[
    {
        "Status": "kerberos-enabled",
        "FQDN": "corp.example.com",
        "OU": "OU=AWS-RDS-OU,DC=corp,DC=example,DC=com",
        "AuthSecretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-ad-secret-AbCdEf",
        "DnsIps": [
            "10.0.1.100",
            "10.0.1.101"
        ]
    }
]
```

**Note**  
The status describes the result of the last join or removal operation. It doesn’t reflect the current health of the connection to your domain. If a DB instance in the `kerberos-enabled` state later loses connectivity to your domain controllers, or if the service account credentials stop working, the status stays `kerberos-enabled` and Amazon RDS emits an RDS event that describes the problem. For details, see [Troubleshooting self-managed Active Directory for Amazon RDS for Oracle](oracle-smad-troubleshooting.md).