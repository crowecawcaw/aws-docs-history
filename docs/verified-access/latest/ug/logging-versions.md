# Verified Access logging versions

By default, the Verified Access logging system uses Open Cybersecurity Schema Framework (OCSF)
version 0.1. For sample logs that use version 0.1 see [OCSF version 0.1 log examples for Verified Access](ocsfv01-examples.md "ocsfv01-examples.md").

The latest logging version is compatible with OCSF version 1.0.0-rc.2. For more
information about the schema, see [OCSF Schema](https://schema.ocsf.io/1.0.0-rc.2/classes/access_activity "https://schema.ocsf.io/1.0.0-rc.2/classes/access_activity"). For sample logs that use version 1.0.0-rc.2, see
[OCSF version 1.0.0-rc.2 log examples for
Verified Access](ocsfv1-examples.md "ocsfv1-examples.md").

Note that you can't use OCSF version 0.1 if the Verified Access endpoint uses the
TCP protocol.

###### To upgrade the logging version using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access
   instances**.
3. Select the appropriate Verified Access instance.
4. On the **Verified Access instance logging configuration** tab,
   choose **Modify Verified Access instance logging
   configuration**.
5. Select **ocsf-1.0.0-rc.2** from the **Update log
   version** drop-down list.
6. Choose **Modify Verified Access instance logging
   configuration**.

###### To upgrade the logging version using the AWS CLI

Use the [modify-verified-access-instance-logging-configuration](../../../cli/latest/reference/ec2/modify-verified-access-instance-logging-configuration.md "../../../cli/latest/reference/ec2/modify-verified-access-instance-logging-configuration.md")
command.
