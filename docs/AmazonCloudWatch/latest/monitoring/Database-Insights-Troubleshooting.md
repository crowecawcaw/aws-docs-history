# Troubleshooting for CloudWatch Database Insights

Use the following information to troubleshoot issues for CloudWatch Database Insights.

## Applying tags to Amazon RDS resources

To apply tags to your databases, use the Amazon RDS API, AWS CLI, or Amazon RDS console. For more information, see the following topics.

- [AddTagsToResource](../../../AmazonRDS/latest/APIReference/API_AddTagsToResource.md "../../../AmazonRDS/latest/APIReference/API_AddTagsToResource.md") in the _Amazon RDS API Reference_
- [add-tags-to-resource](../../../cli/latest/reference/rds/add-tags-to-resource.md "../../../cli/latest/reference/rds/add-tags-to-resource.md") in the _Amazon RDS Command Line Reference_
- [Tagging Amazon Aurora and Amazon RDS resources](../../../AmazonRDS/latest/AuroraUserGuide/USER_Tagging.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_Tagging.md") in the _Amazon Aurora User Guide_

## Maximum DB instances for fleets

You can't monitor more than 500 DB instances in a database fleet. You can use filters to create a fleet health view with less than 500 DB instances.
