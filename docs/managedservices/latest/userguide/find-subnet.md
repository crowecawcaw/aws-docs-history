# Finding subnet IDs in AMS

Several resources require that you specify a subnet, or list of subnets, at configuration time. To find subnets, you can use either the
AMS console or AMS SKMS API/CLI. Note that the AMS SKMS API/CLI is private and must be installed before you can use it.

AMS Console:

1. In the navigation pane, select **VPCs** and the relevant VPC. The VPC details page for the selected VPC opens with a table
   of subnets, click a subnet ID to open the details page and find the ID.
   AMS SKMS API ListSubnetSummaries or CLI:

###### Note

The AMS CLI must be installed for these commands to work. To install the AMS API or CLI, go to the AMS console **Developers Resources**
page. For reference material on the AMS CM API or AMS SKMS API, see the AMS Information Resources section in the User Guide. You may need to add a `--profile` option for
authentication; for example, `aws amsskms `ams-cli-command` --profile SAML`. You may also need to add the `--region` option as all AMS
commands run out of us-east-1; for example `aws amscm `ams-cli-command` --region=us-east-1`.

###### Note

The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your
authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1`
when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.

To find the subnets for your VPC, you can search with the `list-subnet-summaries` command as shown.

###### Note

If you're looking for subnets that are not in an AMS account, you can try `aws ec2 describe-subnets --region us-west-2`.

1. The SKMS API/CLI ListSubnetSummaries operation:

A simple list:

```
aws amsskms list-subnet-summaries
```

Output to a table:

```
aws amsskms list-subnet-summaries --output table
```

2. The SKMS API ListSubnetSummaries operation has parameters to narrow the results based on visibility. In addition, you can [Filter](../ApiReference-cm/API_Filter.md "../ApiReference-cm/API_Filter.md") results based on name.
   If you're using the CLI, you can also use the `--query` option to narrow the output or search on a portion of a value. For example, to find all of
   the subnets for a particular VPC, you can use this command:

```
aws amsskms list-subnet-summaries --query "SubnetSummaries.sort_by(@,&Visibility.Name)[].[Visibility.Name,SubnetId,Name]" --output table
```

Which returns something like this:

```
--------------------------------------------------------------------
|                   ListSubnetSummaries                            |
+---------+------------         -------+---------------------------+
|  Private|  subnet-01234567890abcdef  |  Demo Deployment Zone #1  |
|  Private|  subnet-01234567890abcdef  |  Demo Deployment Zone #1  |
|  Public |  subnet-01234567890abcdef  |  Demo DMZ #1              |
|  Public |  subnet-01234567890abcdef  |  Demo DMZ #1              |
+---------+----------         ---------+---------------------------+
```

For information about using CLI queries, see [How to Filter the Output with the --query Option](../../../cli/latest/userguide/controlling-output.md#controlling-output-filter "../../../cli/latest/userguide/controlling-output.md#controlling-output-filter") and the query language reference, [JMESPath Specification](http://jmespath.org/specification.html "http://jmespath.org/specification.html"). 3. If you have multiple VPCs, include a VPC filter in the command, and then run the command for each VPC. For example:

```
list-subnet-summaries --filter Attribute=VpcId,Value=vpc-xxxxxxxx --query "SubnetSummaries.sort_by(@,&Visibility.Name)[].[Visibility.Name,SubnetId,Name]" --output table
```

4. In AWS, use [describe-subnets](../../../cli/latest/reference/ec2/describe-subnets.md "../../../cli/latest/reference/ec2/describe-subnets.md").
   For information about using CLI queries, see [How to Filter the Output with the --query Option](../../../cli/latest/userguide/controlling-output.md#controlling-output-filter "../../../cli/latest/userguide/controlling-output.md#controlling-output-filter") and the query language reference, [JMESPath Specification](http://jmespath.org/specification.html "http://jmespath.org/specification.html")..

**Subnet names**

Your AMS subnets are created automatically after input is gathered from you and added to the system. AMS uses a formula to create your subnet names:
A`ACCOUNT_ID`-`SUBNET-TYPE`-`AZ-IDENTIFIER`.
The subnet type would be either `dmz`, `shared-services`, or `customer-application`.
Should you have more than one customer-application subnet, an optional identifier may be added to the subnet name,
after the account ID, to indicated that the subnet is an "additional" or "reserved" subnet.
