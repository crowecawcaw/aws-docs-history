For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Creating a VPC endpoint policy for

Timestream for LiveAnalytics

You can attach an endpoint policy to your VPC endpoint that controls access to
Timestream for LiveAnalytics. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.
  For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for Timestream for LiveAnalytics actions

The following is an example of an endpoint policy for Timestream for LiveAnalytics. When attached
to an endpoint, this policy grants access to the listed Timestream for LiveAnalytics actions (in this case,
[`ListDatabases`](API_ListDatabases.md "API_ListDatabases.md")) for
all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "timestream:ListDatabases"
         ],
         "Resource":"*"
      }
   ]
}
```
