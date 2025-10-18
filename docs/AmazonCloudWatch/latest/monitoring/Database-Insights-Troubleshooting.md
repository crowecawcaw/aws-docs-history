# Troubleshooting for CloudWatch Database Insights

Use the following information to troubleshoot issues for CloudWatch Database Insights.


## Applying tags to Amazon RDS resources


To apply tags to your databases, use the Amazon RDS API, AWS CLI, or Amazon RDS console. For more information, see the following topics.



* [AddTagsToResource](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddTagsToResource.html "https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddTagsToResource.html") in the *Amazon RDS API Reference*
* [add-tags-to-resource](https://docs.aws.amazon.com/cli/latest/reference/rds/add-tags-to-resource.html "https://docs.aws.amazon.com/cli/latest/reference/rds/add-tags-to-resource.html") in the *Amazon RDS Command Line Reference*
* [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html") in the *Amazon Aurora User Guide*

## Maximum DB instances for fleets


You can't monitor more than 500 DB instances in a database fleet. You can use filters to create a fleet health view with less than 500 DB instances.
