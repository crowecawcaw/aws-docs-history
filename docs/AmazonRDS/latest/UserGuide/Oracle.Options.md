# Oracle UTL_MAIL

Amazon RDS supports Oracle UTL_MAIL
through the use of the UTL_MAIL option and SMTP servers.
You can send email directly from your database by using the UTL_MAIL package.
Amazon RDS supports UTL_MAIL for the following versions of Oracle:

- Oracle Database 21c (21.0.0.0), all versions
- Oracle Database 19c (19.0.0.0), all versions
  The following are some limitations to using UTL_MAIL:

- UTL_MAIL does not support Transport Layer Security (TLS)
  and therefore emails are not encrypted.

To connect securely to remote SSL/TLS resources by creating and uploading custom Oracle wallets, follow the instructions in
[Configuring UTL_HTTP access using certificates and an Oracle wallet](Oracle.Concepts.md "Oracle.Concepts.md").

The specific certificates that are required for your wallet vary by service. For AWS services, these can typically be found
in the [Amazon trust services repository](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/").

- UTL_MAIL does not support authentication with SMTP servers.
- You can only send a single attachment in an email.
- You can't send attachments larger than 32 K.
- You can only use ASCII and
  Extended Binary Coded Decimal Interchange Code (EBCDIC) character encodings.
- SMTP port (25) is throttled based on the elastic network interface owner's policies.
  When you enable UTL_MAIL,
  only the master user for your DB instance is granted the execute privilege.
  If necessary, the master user can grant the execute privilege to other users
  so that they can use UTL_MAIL.

###### Important

We recommend that you enable Oracle's built-in auditing feature
to track the use of UTL_MAIL procedures.

## Prerequisites for Oracle UTL_MAIL

The following are prerequisites for using Oracle UTL_MAIL:

- One or more SMTP servers,
  and the corresponding IP addresses
  or public or private Domain Name Server (DNS) names.
  For more information about
  private DNS names resolved through a custom DNS server, see
  [Setting up a custom DNS
  server](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.CustomDNS "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.CustomDNS").

## Adding the Oracle UTL_MAIL option

The general process for adding the Oracle UTL_MAIL option to a DB instance is the following:

1. Create a new option group, or copy or modify an existing option group.
2. Add the option to the option group.
3. Associate the option group with the DB instance.

After you add the UTL_MAIL option,
as soon as the option group is active, UTL_MAIL is active.

###### To add the UTL_MAIL option to a DB instance

1. Determine the option group you want to use.
   You can create a new option group or use an existing option group.
   If you want to use an existing option group, skip to the next step.
   Otherwise, create a custom DB option group with the following settings:
   1. For **Engine**,
      choose the edition of Oracle you want to use.
   2. For **Major engine version**,
      choose the version of your DB instance.For more information,
      see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create").

2. Add the **UTL_MAIL** option to the option group.
   For more information about adding options,
   see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption").
3. Apply the option group to a new or existing DB instance:
   - For a new DB instance, you apply the option group when you launch the instance.
     For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
   - For an existing DB instance, you apply the option group by modifying the instance and attaching the new option group.
     For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Using Oracle UTL_MAIL

After you enable the UTL_MAIL option,
you must configure the SMTP server
before you can begin using it.

You configure the SMTP server
by setting the SMTP_OUT_SERVER parameter
to a valid IP address or public DNS name.
For the SMTP_OUT_SERVER parameter,
you can specify a comma-separated list of the addresses of multiple servers.
If the first server is unavailable,
UTL_MAIL tries the next server, and so on.

You can set the default SMTP_OUT_SERVER for a DB instance
by using a [DB parameter group](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
You can set the SMTP_OUT_SERVER parameter for a session
by running the following code on your database on your DB instance.

```

ALTER SESSION SET smtp_out_server = `mailserver.domain.com:25`;

```

After the UTL_MAIL option is enabled,
and your SMTP_OUT_SERVER is configured,
you can send mail by using the `SEND` procedure.
For more information, see
[UTL_MAIL](http://docs.oracle.com/cd/B19306_01/appdev.102/b14258/u_mail.htm#BABFJJBD "http://docs.oracle.com/cd/B19306_01/appdev.102/b14258/u_mail.htm#BABFJJBD")
in the Oracle documentation.

## Removing the Oracle UTL_MAIL option

You can remove Oracle UTL_MAIL from a DB instance.

To remove UTL_MAIL from a DB instance, do one of the following:

- To remove UTL_MAIL from multiple DB instances,
  remove the UTL_MAIL option from the option group they belong to.
  This change affects all DB instances that use the option group.
  For more information, see [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption").
- To remove UTL_MAIL from a single DB instance,
  modify the DB instance
  and specify a different option group
  that doesn't include the UTL_MAIL option.
  You can specify the default (empty) option group, or a
  different custom option group.
  For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Troubleshooting

The following are issues you might encounter when you use UTL_MAIL with Amazon RDS.

- Throttling.
  SMTP port (25) is throttled based on the elastic network interface owner's policies.
  If you can successfully send email by using UTL_MAIL,
  and you see the error `ORA-29278: SMTP transient error: 421 Service not available`,
  you are possibly being throttled.
  If you experience throttling with email delivery,
  we recommend that you implement a backoff algorithm.
  For more information about backoff algorithms, see
  [Error retries and exponential backoff in AWS](../../../general/latest/gr/api-retries.md "../../../general/latest/gr/api-retries.md")
  and
  [How to handle a "throttling – Maximum sending rate exceeded" error](https://aws.amazon.com/blogs/ses/how-to-handle-a-throttling-maximum-sending-rate-exceeded-error/ "https://aws.amazon.com/blogs/ses/how-to-handle-a-throttling-maximum-sending-rate-exceeded-error/").

You can request that this throttle be removed. For more information, see
[How do I remove the throttle on port 25 from my EC2 instance?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-port-25-throttle/ "https://aws.amazon.com/premiumsupport/knowledge-center/ec2-port-25-throttle/").
