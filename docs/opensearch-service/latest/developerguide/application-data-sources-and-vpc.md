# Managing data source associations and

Virtual Private Cloud access permissions

Use the procedures in this section to manage data source associations and to configure
any needed access permissions for a virtual private cloud (VPC).

###### Topics

- [Associating a data source with
  an OpenSearch UI application](#application-data-source-association "#application-data-source-association")
- [Managing access to domains in a
  VPC](#application-manage-vpc-access "#application-manage-vpc-access")
- [Configuring access to OpenSearch Serverless collections in a VPC](#application-configure-vpc-access-serverless-connections "#application-configure-vpc-access-serverless-connections")

## Associating a data source with

an OpenSearch UI application

After creating an OpenSearch UI application, you can use the console or AWS CLI to
associate it with one or more data sources. After this, end-users can retrieve data
from these data sources for searching, working with dashboards, and so on.

### Associate a data source

with an OpenSearch UI application (console)

###### To associate a data source with an OpenSearch UI application using the

console

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
2. Choose **OpenSearch UI (Dashboards)**, and then
   choose the name of an OpenSearch UI application.
3. In the **Associated data sources** area, choose
   **Manage data sources**.
4. Choose from the OpenSearch domains and collections that you want to
   associate with the application.

###### Tip

If you are not finding the data sources you are looking for,
contact your administrators to grant you the necessary permission.
For more information, see [Permissions to create an
application that uses IAM Identity Center authentication (optional)](application-getting-started.md#prerequisite-permissions-idc "application-getting-started.md#prerequisite-permissions-idc"). 5. Choose **Next**, and then choose
**Save**.

After you have associated a data source with the application, the
**Launch Application** button is enabled on the application
detail page. You can choose **Launch Application** to open the
**Welcome to OpenSearch** page, where you can create and
manage workspaces.

For information about working with workspaces, see [Using Amazon OpenSearch Service workspaces](application-workspaces.md "application-workspaces.md").

## Managing access to domains in a

VPC

If an OpenSearch domain in a VPC was associated with the application, a VPC
administrator must authorize access between OpenSearch UI and VPC using the
console or AWS CLI.

### Managing access to

domains in a VPC (console)

###### To configure the access to a VPC domain using the AWS Management Console:

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
2. In the left navigation pane, choose **Domains**, and
   the choose the name of the VPC domain.

-or-

Choose **Create domain**, and then configure the
details for the domain. 3. Choose the **VPC endpoints** tab, and then choose
**Authorize principal**. 4. In the **Authorize principals** dialog box, select
**Authorize Principals from other AWS Services**,
and then choose **OpenSearch applications
(Dashboard)** from the list. 5. Choose **Authorize**.

### Managing access to domains

in a VPC (AWS CLI)

###### To authorize a VPC domain using the AWS CLI

To authorize VPC domain using the AWS CLI, run the following command.
Replace the `placeholder values` with your own
information.

```
aws opensearch authorize-vpc-endpoint-access \
 --domain-name `domain-name` \
 --service application.opensearchservice.amazonaws.com \
 --region `region-id`
```

###### To revoke a VPC domain association using the console

When an association is no longer needed, the VPC domain owner can revoke
access using the following procedure.

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
2. In the left navigation pane, choose **Domains**, and the
   choose the name of the VPC domain.
3. Choose the **VPC endpoints** tab, and then select the
   button for the **OpenSearch applications (Dashboard)**
   row.
4. Choose **Revoke access**.

###### To revoke a VPC domain association using the AWS CLI

To revoke a VPC domain association with the OpenSearch UI application, run
the following command. Replace the `placeholder values`
with your own information.

```
aws opensearch revoke-vpc-endpoint-access \
    --domain-name `domain-name` \
    --service application.opensearchservice.amazonaws.com \
    --region `region-id`
```

## Configuring access to OpenSearch Serverless collections in a VPC

If an Amazon OpenSearch Serverless collection in a VPC was associated with the application, a VPC
administrator can authorize access by creating a new network policy and attaching it
to the collection.

### Configuring access to OpenSearch Serverless collections in a VPC (console)

###### To configure access to OpenSearch Serverless collections in a VPC using the

console

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
2. In the left navigation, choose **Network policies**,
   choose the name of the network policy, and then choose
   **Edit**.

-or-

Choose **Create network policy**, and then configure
the details for the policy. 3. In the **Access type** area, choose **Private
(recommended)**, and then select **AWS service
private access**. 4. In the search field, choose **Service**, and then
choose `application.opensearchservice.amazonaws.com`. 5. In the **Resource type** area, select the
**Enable access to OpenSearch endpoint** box. 6. For **Search collection(s), or input specific prefix
term(s)**, in the search field, select **Collection
Name**, and then enter or select the name of the
collections to associate with the network policy. 7. Choose **Create** for a new network policy or
**Update** for an existing network policy.

### Configuring access to OpenSearch Serverless collections in a VPC (AWS CLI)

###### To configure access to OpenSearch Serverless collections in a VPC using the

AWS CLI

1. Create a .json file similar to the following. Replace the
   `placeholder values` with your own
   information.

```
{
    "Description" : "`policy-description`",
    "Rules": [{
       "ResourceType" : "collection",
        "Resource" : ["collection/`collection_name`"]
     }],
    "SourceServices" : [
          "application.opensearchservice.amazonaws.com"
      ],
      "AllowFromPublic" : false
}
```

2. Create or update a network policy for a collection in a VPC to work
   with OpenSearch UI applications.

Create a network policy
Run the following command. Replace the
`placeholder values` with your
own information.

```
aws opensearchserverless create-security-policy \
    --type network  \
    --region `region` \
    --endpoint-url `endpoint-url` \
    --name `network-policy-name` \
    --policy file:/`path_to_network_policy_json_file`
```

The command returns information similar to the following:

```
{
    "securityPolicyDetail": {
        "createdDate": ******,
        "lastModifiedDate": ******,
        "name": "`network-policy-name`",
        "policy": [
            {
                "SourceVPCEs": [],
                "AllowFromPublic": false,
                "Description": "",
                "Rules": [
                    {
                        "Resource": [
                            "collection/`network-policy-name`"
                        ],
                        "ResourceType": "collection"
                    }
                ],
                "SourceServices": [
                    "application.opensearchservice.amazonaws.com"
                ]
            }
        ],
        "policyVersion": "******",
        "type": "network"
    }
}
```

Update a network policy
Run the following command. Replace the
`placeholder values` with your
own information.

```
aws opensearchserverless update-security-policy \
    --type network  \
    --region `region` \
    --endpoint-url `endpoint-url` \
    --name `network-policy-name` \
    --policy-version "`policy_version_from_output_of_network_policy_creation`" \
    --policy file:/`path_to_network_policy_json_file`
```

The command returns information similar to the following:

```
{
    "securityPolicyDetail": {
        "createdDate": ******,
        "lastModifiedDate": ******,
        "name": "`network-policy-name`",
        "policy": [
            {
                "SourceVPCEs": [],
                "AllowFromPublic": false,
                "Description": "",
                "Rules": [
                    {
                        "Resource": [
                            "collection/`network-policy-name`"
                        ],
                        "ResourceType": "collection"
                    }
                ],
                "SourceServices": [
                    "application.opensearchservice.amazonaws.com"
                ]
            }
        ],
        "policyVersion": "******",
        "type": "network"
    }
}
```
