

# General information for Amazon AppFlow flows
<a name="general"></a>

The following general information applies to all Amazon AppFlow flows.

**Source and destination API limits**  
The API calls that Amazon AppFlow makes to data sources and destinations count against any API limits for that application. For example, if you set up an hourly flow that pulls 5 pages of data from Salesforce, Amazon AppFlow will make a total of 120 daily API calls (24x5=120). This will count against your 24-hour Salesforce API limit. Exact API limits can vary depending on your licensing with the SaaS application.

**IP address ranges**  
Amazon AppFlow operates from the [AWS IP address ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) shown in the *Amazon Web Services General Reference Guide*. Configuring a flow connection with an incorrect URL, URI, or IP address range can return a bad gateway error. If you encounter this error, we recommend deleting your connection and creating a new one with the correct URL, URI, or IP address range. For instructions on how to create a new connection for your SaaS application, see [Supported source and destination applications](app-specific.md).

**Note**  
You can't use IP allow listing in your S3 bucket policy to deny access to any other IP addresses besides Amazon AppFlow IP addresses. This is because Amazon AppFlow uses a VPC endpoint when placing data in your Amazon S3 buckets. For more information about Amazon AppFlow Regions and endpoints, see [Amazon AppFlow Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference*.

**Schema changes**  
Amazon AppFlow only supports the automatic import of newly created Salesforce fields into Amazon S3 without requiring the user to update their flow configurations. For other source applications, Amazon AppFlow does not currently support schema changes, but you can edit your flow to reload the fields and update your mapping. For more information on how to edit a flow, see [Managing Amazon AppFlow flows](flows-manage.md).

**Note**  
If the source or destination fields in a flow's configuration are deleted from the source or destination application (including Salesforce), then the flow run will fail. To prevent failed flows, we recommend that you edit your flows to remove deleted fields from the mapping.