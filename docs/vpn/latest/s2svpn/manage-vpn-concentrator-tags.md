# Manage AWS Site-to-Site VPN Concentrator tags

Tags are key-value pairs that help you organize and manage your Site-to-Site VPN
Concentrators. You can use tags to categorize Site-to-Site VPN Concentrators by purpose, environment,
cost center, or any other criteria that makes sense for your organization.

## Manage tags using the console

You can add or delete tags for a Site-to-Site VPN Concentrator using the AWS Management Console.

###### To add tags to a Site-to-Site VPN Concentrator

1. Open the Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN
   Concentrators**.
3. Select the Site-to-Site VPN Concentrator that you want to tag.
4. Choose the **Tags** tab.
5. Choose **Manage tags**.
6. Choose **Add new tag**.
7. For **Key**, enter a tag key (for example, `Environment`).
8. For **Value**, enter a tag value (for example, `Production`).
9. Choose **Save changes**.

###### To delete tags from a Site-to-Site VPN Concentrator

1. Open the Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN
   Concentrators.**
3. Select the Site-to-Site VPN Concentrator from which you want to remove tags.
4. Choose the **Tags** tab.
5. Choose **Manage tags**.
6. For each tag you want to remove, choose **Remove**.
7. Choose **Save changes**.

## Manage tags using the CLI

You can add, modify, or remove tags using the AWS CLI.

###### Add tags

The following example adds tags to a Site-to-Site VPN Concentrator:

```
aws ec2 create-tags --resources vcn-0123456789abcdef0 --tags Key=Environment,Value=Production Key=Team,Value=NetworkOps
```

This command returns no output on success.

###### View tags

The following example describes the tags for a Site-to-Site VPN Concentrator:

```
aws ec2 describe-tags --filters "Name=resource-id,Values=vcn-0123456789abcdef0"
```

The following response is returned:

```
{
    "Tags": [
        {
            "Key": "Environment",
            "ResourceId": "vcn-0123456789abcdef0",
            "ResourceType": "vpn-concentrator",
            "Value": "Production"
        },
        {
            "Key": "Team",
            "ResourceId": "vcn-0123456789abcdef0",
            "ResourceType": "vpn-concentrator",
            "Value": "NetworkOps"
        }
    ]
}
```

###### Remove tags

The following example removes tags from a Site-to-Site VPN Concentrator:

```
aws ec2 delete-tags --resources vcn-0123456789abcdef0 --tags Key=Environment Key=Team
```

This command returns no output on success.

## Manage tags using the API

You can programmatically manage Site-to-Site VPN Concentrator tags using the Amazon EC2 API operations.

###### CreateTags

Use the `CreateTags` operation to add or update tags:

```
POST / HTTP/1.1
Host: ec2.region.amazonaws.com
Content-Type: application/x-www-form-urlencoded

Action=CreateTags
&ResourceId.1=vcn-0123456789abcdef0
&Tag.1.Key=Environment
&Tag.1.Value=Production
&Tag.2.Key=Team
&Tag.2.Value=NetworkOps
&Version=2016-11-15
```

The following response is returned:

```
<?xml version="1.0" encoding="UTF-8"?>
<CreateTagsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
    <return>true</return>
</CreateTagsResponse>
```

###### DescribeTags

Use the `DescribeTags` operation to retrieve tags:

```
POST / HTTP/1.1
Host: ec2.region.amazonaws.com
Content-Type: application/x-www-form-urlencoded

Action=DescribeTags
&Filter.1.Name=resource-id
&Filter.1.Value.1=vcn-0123456789abcdef0
&Version=2016-11-15
```

The following response is returned:

```
<?xml version="1.0" encoding="UTF-8"?>
<DescribeTagsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
    <tagSet>
        <item>
            <resourceId>vcn-0123456789abcdef0</resourceId>
            <resourceType>vpn-concentrator</resourceType>
            <key>Environment</key>
            <value>Production</value>
        </item>
        <item>
            <resourceId>vcn-0123456789abcdef0</resourceId>
            <resourceType>vpn-concentrator</resourceType>
            <key>Team</key>
            <value>NetworkOps</value>
        </item>
    </tagSet>
</DescribeTagsResponse>
```

###### DeleteTags

Use the `DeleteTags` operation to remove tags:

```
POST / HTTP/1.1
Host: ec2.region.amazonaws.com
Content-Type: application/x-www-form-urlencoded

Action=DeleteTags
&ResourceId.1=vcn-0123456789abcdef0
&Tag.1.Key=Environment
&Tag.2.Key=Team
&Version=2016-11-15
```

The following response is returned:

```
<?xml version="1.0" encoding="UTF-8"?>
<DeleteTagsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
    <return>true</return>
</DeleteTagsResponse>
```
