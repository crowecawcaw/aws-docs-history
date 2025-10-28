# Best practices

The following are a few best practices for integrating with Amazon Location Service.

## Resource management

To help effectively manage your location resources in Amazon Location Service, consider the following
best practices:

- Use regional endpoints that are central to your expected user base to improve
  their experience. For information about region endpoints, see [Amazon Location supported regions](location-regions.md "location-regions.md").
- For resources that use data providers, such as map resources and place index
  resources, make sure to follow the terms of use agreement of the specific data
  provider. For more information, see [Terms of use and data attribution](data-attribution.md "data-attribution.md").
- Minimize the creation of resources by having one resource for each
  configuration of map, place index, or routes. Within a region, you typically
  need only one resource per data provider or map style. Most applications use
  existing resources, and do not create resources at run time.
- When using different resources in a single application, such as a map resource
  and a route calculator, use the same data provider in each resource to ensure
  that the data matches. For example, that a route geometry you create with your
  route calculator aligns with the streets on the map drawn using the map
  resource.

## Billing and cost management

To help manage your costs and billing, consider the following best practice:

- Use monitoring tools, such as Amazon CloudWatch, to track your resource usage. You can set
  alerts that notify you when usage is about to exceed your specified limits. For more
  information, see [Creating a Billing Alarm to Monitor Your Estimated AWS Charges](../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md") in the _Amazon CloudWatch User Guide_.

## Quotas and usage

You AWS account includes quotas that set a default limit your usage amount. You
can set up alarms to alert you when your usage is getting close to your limit, and
you can request a raise to a quota, when you need it. For information about
how to work with quotas, see the following topics.

- [Manage quotas with Service Quotas](manage-quotas.md "manage-quotas.md")
- [Create CloudWatch alarms for Amazon Location Service metrics](cloudwatch.md#create-alarms "cloudwatch.md#create-alarms")
- [Visualizing your service quotas and setting alarms](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md") in the
  _Amazon CloudWatch User Guide_.

You can create alarms to give you advance warning when you are close to exceeding your
limits. We recommend setting alarms for each quota in each AWS Region where you use
Amazon Location. For example, you can monitor your use of the
`SearchPlaceIndexForText` operation, and create an alarm when you exceed
80 percent of your current quota.

When you get an alarm warning about your quota, you must decide what to do. You
might be using additional resources because your customer base has grown. In that case
you may want to request an increase to your quota, such as a 50 percent
increase in the quota for an API call in that Region. Or, maybe there's an error in
your service that causes you to make additional unnecessary calls to Amazon Location. In
that case you'd want to solve the problem in your service.
