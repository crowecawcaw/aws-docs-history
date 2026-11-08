

# Managing data source associations and Virtual Private Cloud access permissions
<a name="application-data-sources-and-vpc"></a>

Use the procedures in this section to manage data source associations and to configure any needed access permissions for a virtual private cloud (VPC).

**Topics**
+ [Associating a data source with an OpenSearch UI application](#application-data-source-association)
+ [Managing access to domains in a VPC](#application-manage-vpc-access)
+ [Verifying VPC endpoint access and security groups](#application-manage-vpc-access-verify)
+ [Configuring access to OpenSearch Serverless collections in a VPC](#application-configure-vpc-access-serverless-connections)

## Associating a data source with an OpenSearch UI application
<a name="application-data-source-association"></a>

After creating an OpenSearch UI application, you can use the console or AWS CLI to associate it with one or more data sources. After this, end-users can retrieve data from these data sources for searching, working with dashboards, and so on. 

### Associate a data source with an OpenSearch UI application (console)
<a name="application-data-source-association-console"></a>

**To associate a data source with an OpenSearch UI application using the console**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. Choose **OpenSearch UI (Dashboards)**, and then choose the name of an OpenSearch UI application.

1. In the **Associated data sources** area, choose **Manage data sources**.

1. Choose from the OpenSearch domains and collections that you want to associate with the application. 
**Tip**  
If you are not finding the data sources you are looking for, contact your administrators to grant you the necessary permission. For more information, see [Permissions to create an application that uses IAM Identity Center authentication (optional)](application-getting-started.md#prerequisite-permissions-idc). 

1. Choose **Next**, and then choose **Save**. 

After you have associated a data source with the application, the **Launch Application** button is enabled on the application detail page. You can choose **Launch Application** to open the **Welcome to OpenSearch** page, where you can create and manage workspaces.

For information about working with workspaces, see [Using Amazon OpenSearch Service workspaces](application-workspaces.md).

### Associating a data source with the AWS CLI
<a name="application-data-source-association-cli"></a>

Use the `update-application` command to associate one or more data sources. Replace the {{placeholder values}} with your own information.

```
aws opensearch update-application \
    --id {{application-id}} \
    --region {{region}} \
    --data-sources '[
      {
        "dataSourceArn": "arn:aws:es:{{region}}:{{account-id}}:domain/{{domain-name}}",
        "dataSourceDescription": "Production logs domain"
      },
      {
        "dataSourceArn": "arn:aws:aoss:{{region}}:{{account-id}}:collection/{{collection-id}}",
        "dataSourceDescription": "Search collection"
      }
    ]'
```

To confirm the association, run `aws opensearch get-application --id {{application-id}}`. The response includes a `dataSources` array that lists the currently associated sources.

**Important**  
The `--data-sources` parameter replaces the entire list rather than adding to it. To remove one data source, run the command again with every data source that you want to keep. Passing an empty array removes all data sources from the application.

### Supported data source types
<a name="application-data-source-types"></a>


**Data source types and how they are associated**  

| Data source type | ARN format | How it is associated | 
| --- | --- | --- | 
| OpenSearch managed domain | arn:aws:es:{{region}}:{{account-id}}:domain/{{domain-name}} | Console or AWS CLI | 
| OpenSearch Serverless collection | arn:aws:aoss:{{region}}:{{account-id}}:collection/{{collection-id}} | Console or AWS CLI | 
| Amazon S3 through direct query | Configured through an AWS Glue connection | Within OpenSearch UI | 
| Amazon CloudWatch Logs | Configured as a direct query source | Within OpenSearch UI | 
| Amazon Security Lake | Configured as a direct query source | Within OpenSearch UI | 

You associate domains and collections at the application level, with the console or the AWS CLI. You configure direct query sources from within OpenSearch UI after the application is running, not through the `update-application` command.

### Configuring a direct query data source
<a name="application-data-source-direct-query"></a>

With a direct query source, you can query data in place, without ingesting it into OpenSearch. Before you begin, confirm the following prerequisites:
+ For Amazon S3 sources, an AWS Glue database and table that catalog the data.
+ An IAM role that grants OpenSearch permission to read from the source.
+ A domain associated with the application that runs OpenSearch version 2.13 or later.

**To configure a direct query data source**

1. Launch your OpenSearch UI application.

1. In the left navigation pane, choose **Data sources**.

1. Choose **Create data source connection**.

1. Choose the source type: Amazon S3, Amazon CloudWatch Logs, or Amazon Security Lake.

1. Provide the connection details, such as the AWS Glue database and the IAM role.

1. Test the connection, and then save it.

For more information about direct queries, see [Working with Amazon OpenSearch Service direct queries](direct-query.md).

## Managing access to domains in a VPC
<a name="application-manage-vpc-access"></a>

If an OpenSearch domain in a VPC was associated with the application, a VPC administrator must authorize access between OpenSearch UI and VPC using the console or AWS CLI. 

### Managing access to domains in a VPC (console)
<a name="application-manage-vpc-access-console"></a>

**To configure the access to a VPC domain using the AWS Management Console:**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the left navigation pane, choose **Domains**, and the choose the name of the VPC domain.

   -or-

   Choose **Create domain**, and then configure the details for the domain.

1. Choose the **VPC endpoints** tab, and then choose **Authorize principal**. 

1. In the **Authorize principals** dialog box, select **Authorize Principals from other AWS Services**, and then choose **OpenSearch applications (Dashboard)** from the list.

1. Choose **Authorize**.

### Managing access to domains in a VPC (AWS CLI)
<a name="application-manage-vpc-access-cli"></a>

**To authorize a VPC domain using the AWS CLI**  
To authorize VPC domain using the AWS CLI, run the following command. Replace the {{placeholder values}} with your own information.

```
aws opensearch authorize-vpc-endpoint-access \
 --domain-name {{domain-name}} \
 --service application.opensearchservice.amazonaws.com \
 --region {{region-id}}
```

**Important**  
Revoking the authorization disconnects OpenSearch UI from the domain. Any workspace that uses the domain as a data source loses connectivity. Revoke it only when you intend to disconnect the domain.

**To revoke a VPC domain association using the console**

When an association is no longer needed, the VPC domain owner can revoke access using the following procedure.

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the left navigation pane, choose **Domains**, and the choose the name of the VPC domain.

1. Choose the **VPC endpoints** tab, and then select the button for the **OpenSearch applications (Dashboard)** row. 

1. Choose **Revoke access**. 

**To revoke a VPC domain association using the AWS CLI**  
To revoke a VPC domain association with the OpenSearch UI application, run the following command. Replace the {{placeholder values}} with your own information.

```
aws opensearch revoke-vpc-endpoint-access \
    --domain-name {{domain-name}} \
    --service application.opensearchservice.amazonaws.com \
    --region {{region-id}}
```

## Verifying VPC endpoint access and security groups
<a name="application-manage-vpc-access-verify"></a>

To confirm that the authorization is in place, run the following command. The response includes `application.opensearchservice.amazonaws.com` in the list of authorized services.

```
aws opensearch list-vpc-endpoint-access \
    --domain-name {{domain-name}} \
    --region {{region}}
```

The security group attached to a VPC domain must also allow the traffic. OpenSearch UI communicates over HTTPS on port 443, so you do not need to open port 9200 or any other port.


**Security group rules for a VPC domain**  

| Direction | Port | Source or destination | Purpose | 
| --- | --- | --- | --- | 
| Inbound | TCP 443 | The VPC CIDR block | HTTPS from the VPC endpoint | 
| Inbound | TCP 443 | The security group itself | Communication between the endpoint and the domain | 
| Outbound | All | As required by your configuration | Allows responses | 

**Note**  
This configuration affects only the connection between OpenSearch UI and your data sources. The OpenSearch UI application URL itself is reachable without being inside the VPC, and is protected by the authentication method that you configured. To restrict which networks can reach the application, see [Network access to OpenSearch UI](application-networking.md).

## Configuring access to OpenSearch Serverless collections in a VPC
<a name="application-configure-vpc-access-serverless-connections"></a>

If an Amazon OpenSearch Serverless collection in a VPC was associated with the application, a VPC administrator can authorize access by creating a new network policy and attaching it to the collection. 

### Configuring access to OpenSearch Serverless collections in a VPC (console)
<a name="application-configure-vpc-access-serverless-connections-console"></a>

**To configure access to OpenSearch Serverless collections in a VPC using the console**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the left navigation, choose **Network policies**, choose the name of the network policy, and then choose **Edit**.

   -or-

   Choose **Create network policy**, and then configure the details for the policy.

1. In the **Access type** area, choose **Private (recommended)**, and then select **AWS service private access**. 

1. In the search field, choose **Service**, and then choose `application.opensearchservice.amazonaws.com`. 

1. In the **Resource type** area, select the **Enable access to OpenSearch endpoint** box. 

1. For **Search collection(s), or input specific prefix term(s)**, in the search field, select **Collection Name**, and then enter or select the name of the collections to associate with the network policy. 

1. Choose **Create** for a new network policy or **Update** for an existing network policy. 

### Configuring access to OpenSearch Serverless collections in a VPC (AWS CLI)
<a name="application-configure-vpc-access-serverless-connections-cli"></a>

**To configure access to OpenSearch Serverless collections in a VPC using the AWS CLI**

1. Create a .json file similar to the following. Replace the {{placeholder values}} with your own information.

   ```
   {
       "Description" : "{{policy-description}}",
       "Rules": [{
          "ResourceType" : "collection",
           "Resource" : ["collection/{{collection_name}}"]
        }],
       "SourceServices" : [
             "application.opensearchservice.amazonaws.com"
         ],
         "AllowFromPublic" : false
   }
   ```

1. Create or update a network policy for a collection in a VPC to work with OpenSearch UI applications.

------
#### [ Create a network policy ]

   Run the following command. Replace the {{placeholder values}} with your own information.

   ```
   aws opensearchserverless create-security-policy \
       --type network  \
       --region {{region}} \
       --endpoint-url {{endpoint-url}} \
       --name {{network-policy-name}} \
       --policy file:/{{path_to_network_policy_json_file}}
   ```

   The command returns information similar to the following: 

   ```
   {
       "securityPolicyDetail": {
           "createdDate": ******,
           "lastModifiedDate": ******,
           "name": "{{network-policy-name}}",
           "policy": [
               {
                   "SourceVPCEs": [],
                   "AllowFromPublic": false,
                   "Description": "",
                   "Rules": [
                       {
                           "Resource": [
                               "collection/{{network-policy-name}}"
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

------
#### [ Update a network policy ]

   Run the following command. Replace the {{placeholder values}} with your own information.

   ```
   aws opensearchserverless update-security-policy \
       --type network  \
       --region {{region}} \
       --endpoint-url {{endpoint-url}} \
       --name {{network-policy-name}} \
       --policy-version "{{policy_version_from_output_of_network_policy_creation}}" \
       --policy file:/{{path_to_network_policy_json_file}}
   ```

   The command returns information similar to the following: 

   ```
   {
       "securityPolicyDetail": {
           "createdDate": ******,
           "lastModifiedDate": ******,
           "name": "{{network-policy-name}}",
           "policy": [
               {
                   "SourceVPCEs": [],
                   "AllowFromPublic": false,
                   "Description": "",
                   "Rules": [
                       {
                           "Resource": [
                               "collection/{{network-policy-name}}"
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

------