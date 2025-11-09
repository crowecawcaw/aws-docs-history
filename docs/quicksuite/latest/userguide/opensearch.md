# Authorizing connections to Amazon OpenSearch Service

|                                            |
| ------------------------------------------ |
| \*_Applies<br>to:_<br>• Enterprise Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

Before you can use OpenSearch in a Amazon Quick Sight dataset, there are a few tasks for the
Quick Suite administrator to complete with the cooperation of a person who has
access to the OpenSearch console.

To get started, identify each OpenSearch domain that you want to connect to. Then
gather the following information for each domain:

- The name of the OpenSearch domain.
- The OpenSearch version used by this domain.
- The Amazon Resource Name (ARN) of the OpenSearch domain.
- The HTTPS endpoint.
- The OpenSearch Dashboards URL, if you use Dashboards. You can extrapolate the
  Dashboards URL by appending "`/dashboards/`" to an endpoint.
- If the domain has a VPC endpoint, gather all the related information on the
  VPC tab of the OpenSearch Service console:
  - The VPC ID
  - The VPC security groups
  - The associated IAM role or roles
  - The associated Availability Zones
  - The associated subnets

- If the domain has a regular endpoint (not a VPC endpoint), note that it uses
  the public network.
- The start hour for the daily automated snapshot (if your users want to
  know).
  Before you proceed, the Amazon Quick Suite administrator enables authorized connections from
  Amazon Quick Suite to OpenSearch Service. This process is required for every AWS service that you connect
  to from Amazon Quick Suite. You need to do this only once per AWS account for each AWS
  service that you use as a data source.

For OpenSearch Service, the authorization process adds the AWS managed policy
`AWSQuickSightOpenSearchPolicy` to your AWS account.

###### Important

Make sure that the IAM policy for your OpenSearch domain doesn't conflict with
the permissions in `AWSQuickSightOpenSearchPolicy`. You can find the
domain access policy in the OpenSearch Service console. For more information, see [Configuring access policies](../../../opensearch-service/latest/developerguide/ac.md#ac-creating "../../../opensearch-service/latest/developerguide/ac.md#ac-creating") in the
_Amazon OpenSearch Service Developer Guide_.

###### To turn on or turn off connections from Amazon Quick Suite to OpenSearch Service

1. Within Amazon Quick Suite, choose **Administrator** and
   **Manage Amazon Quick Suite**.
2. Choose **Security & permissions**, **Add or
   remove**.
3. To enable connections, select the **Amazon OpenSearch Service** check
   box.

To disable connections, clear the **Amazon OpenSearch Service** check
box. 4. Choose **Update** to confirm your choices.
If needed, use the topics below to configure a OpenSearch VPC connection and
permissions for Amazon Quick Suite to access OpenSearch.

###### Topics

- [Using a VPC connection](#opensearch-and-vpc-connection "#opensearch-and-vpc-connection")
- [Using OpenSearch permissions](#opensearch-permissions "#opensearch-permissions")

## Using a VPC connection

In some cases, your OpenSearch domain is in a virtual private cloud (VPC) based on
the Amazon VPC service. If so, make sure to determine if Amazon Quick Suite is already
connected to the VPC ID that the OpenSearch domain uses. You can reuse an existing
VPC connection. If you're not sure if it's working, you can test it. For more
information, see [Testing the connection to your Amazon VPC data
source](../../../quicksight/latest/user/vpc-creating-a-quicksight-data-source-profile.md "../../../quicksight/latest/user/vpc-creating-a-quicksight-data-source-profile.md").

If a connection isn't already defined in Amazon Quick Suite for the VPC that you want to
use, you can create one. This task is a multistep process that you need to complete
before you proceed. To learn how to add Amazon Quick Suite to a VPC and add a connection
from Amazon Quick Suite to the VPC, see [Connecting to a Amazon VPC with Amazon Quick Suite](../../../quicksight/latest/user/working-with-aws-vpc.md "../../../quicksight/latest/user/working-with-aws-vpc.md").

## Using OpenSearch permissions

After you configure Amazon Quick Suite to connect to OpenSearch Service, you might need to enable
permissions in OpenSearch. For this part of the setup process, you can use the
OpenSearch Dashboards link for each OpenSearch domain. Use the following list to help
determine what permissions you need:

1. For domains that use fine-grained access control, configure permissions in
   the form of a role. This process is similar to using scoped-down policies in
   Amazon Quick Suite.
2. For each domain that you create a role for, add a role mapping.

For more information, see following.

If your OpenSearch domain has [fine-grained
access control](../../../opensearch-service/latest/developerguide/fgac.md "../../../opensearch-service/latest/developerguide/fgac.md") enabled, there are some permissions to configure so the
domain is accessible from Amazon Quick Suite. Perform these steps for each domain that you
want to use.

The following procedure uses OpenSearch Dashboards, which is an open-source tool
that works with OpenSearch. You can find the link to Dashboards on the domain
dashboard on the OpenSearch Service console.

###### To add permissions to a domain to allow access from Amazon Quick Suite

1. Open OpenSearch Dashboards for the OpenSearch domain that you want to work
   with. The URL is
   ``opensearch-domain-endpoint`/dashboards/`.
2. Choose **Security** from the navigation pane.

If you don't see the navigation pane, open it by using the menu icon at
upper left. To keep the menu open, choose **Dock
navigation** at lower left. 3. Choose **Roles**, **Create
role**. 4. Name the role `quicksight_role`.

You can choose a different name, but we recommend this one because we use
it in our documentation and it's thus easier to support. 5. Under **Cluster permissions**, add the following
permissions:

    * `cluster:monitor/main`
    * `cluster:monitor/health`
    * `cluster:monitor/state`
    * `indices:data/read/scroll`
    * `indices:data/read/scroll/clear`,

6. Under **Index permissions** specify
   `*` as the index pattern.
7. For **Index permissions**, add the following
   permissions:
   - `indices:admin/get`
   - `indices:admin/mappings/get`
   - `indices:admin/mappings/fields/get*`
   - `indices:data/read/search*`
   - `indices:monitor/settings/get`

8. Choose **Create**.
9. Repeat this procedure for each OpenSearch domain that you're planning to
   use.

Use the following procedure to add a role mapping for the permissions that you
added in the previous procedure. You might find it more efficient to add the
permissions and the role mapping as part of a single process. These instructions are
separate for clarity.

###### To create a role mapping for the IAM role you added

1. Open OpenSearch Dashboards for the OpenSearch domain that you want to work
   with. The URL is
   ``opensearch-domain-endpoint`/dashboards/`.
2. Choose **Security** from the navigation pane.
3. Search for and open `quicksight_role` from the
   list.
4. On the **Mapped users** tab, choose **Manage
   mapping**.
5. In the **Backend roles** section, enter the ARN of the
   AWS-managed IAM role for Amazon Quick Suite. Following is an example.

```
arn:`aws`:iam::`AWS-ACCOUNT-ID`:role/service-role/`aws-quicksight-service-role-v0`
```

6. Choose **Map**.
7. Repeat this procedure for each OpenSearch domain that you want to
   use.
