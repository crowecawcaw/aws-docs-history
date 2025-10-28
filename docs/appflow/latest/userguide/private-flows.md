# Private Amazon AppFlow flows

With Amazon AppFlow, you can create private flows between AWS services and supported software
as a service (SaaS) applications. Private flows use AWS PrivateLink to route data over AWS
infrastructure without exposing it to the public internet.

The following SaaS applications are integrated with AWS PrivateLink:

- Salesforce
- Singular
- Snowflake
- Trend Micro

###### Note

Your SaaS account must be enabled for AWS PrivateLink access. Please check with the
administrator for the SaaS application.

When you create a connection using AWS PrivateLink, Amazon AppFlow creates the VPC endpoint
service configuration for you. When you no longer need the endpoint service configuration,
Amazon AppFlow deletes it.

###### Note

Amazon AppFlow makes metadata API calls to populate a list of objects and fields in the console

over the public endpoints. However, the actual data transfer during the flow run happens over
Amazon VPC endpoints powered by AWS PrivateLink.

The following diagram illustrates the components of a private flow.

![A private flow using AWS PrivateLink](images/PrivateLink%20for%20AppFlow.png)
