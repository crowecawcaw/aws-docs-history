# Finding VPC IDs in AMS

A virtual private cloud (VPC) has one or more subnets. In AMS your VPC is in an AWS Region and you have private and public subnets.

See also [Finding subnet IDs in AMS](find-subnet.md "find-subnet.md").

Some CTs require the VpcId. To find a VPC ID, you can use either the AMS console or API/CLI.

AMS Console:

In the navigation pane, select **VPCs** and the relevant VPC. The VPC details page for the selected VPC opens with information including the VPC ID.

AMS SKMS API ListVpcSummaries or CLI:

###### Note

The AMS CLI must be installed for these commands to work. To install the AMS API or CLI, go to the AMS console **Developers Resources**
page. For reference material on the AMS CM API or AMS SKMS API, see the AMS Information Resources section in the User Guide. You may need to add a `--profile` option for
authentication; for example, `aws amsskms `ams-cli-command` --profile SAML`. You may also need to add the `--region` option as all AMS
commands run out of us-east-1; for example `aws amscm `ams-cli-command` --region=us-east-1`.

###### Note

The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your
authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1`
when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.

1. In the following examples, the first command requests a list of summaries for all VPCs in the account. The second command requests the list of VPCs, with a
   query filter to list only those VPCs created in 2016, and output the CreatedTime, VpcId, and Name.

###### Note

You can obtain the AMS SKMS CLI through the **Developer's Resources** page in the AMS console.

```
aws amsskms list-vpc-summaries --output table
```

````
-----------------------------------------------------
|                 ListVPCSummaries                  | +---------------------------------------------------+
|                  VPCSummaries                     |
|+------------------+-------------------------------|
|   CreatedTime     |   2016-01-15T18:50:11Z        |
|   VpcId           |   vpc-01234567890abcdef       |
|   LastModifiedTime|   2016-01-15T18:50:11Z        |
|   Name            |   952444781316-initial-vpc    |
|+------------------+-------------------------------| |                   Visibility                      |
|+------------------+-------------------------------|
|   Id              |  PrivateAndPublic             |
|   Name            |  PrivateAndPublic             |
|+------------------+-------------------------------| ``` 2. This time with a query: ``` aws amsskms list-VPC-summaries --query "VPCSummaries[?starts_with(@.CreatedTime,to_string(`2016`))].[CreatedTime, VpcId, Name]" --output table ``` ``` ------------------------------------------------------------------------- |                               ListVPCSummaries                         | +---------------------+-----------------------+--------------------------+
|2016-01-15T18:50:11Z | vpc-01234567890abcdef | 952444781316-initial-VPC | +---------------------+-----------------------+--------------------------+ ```
````
