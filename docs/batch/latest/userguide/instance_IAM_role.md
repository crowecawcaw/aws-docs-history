# Amazon ECS instance role

AWS Batch compute environments are populated with Amazon ECS container instances. They run the
Amazon ECS container agent locally. The Amazon ECS container agent makes calls to various AWS API
operations on your behalf. Therefore, container instances that run the agent require an IAM
policy and role for these services to recognize that the agent belongs to you. You must create an
IAM role and an instance profile for the container instances to use when they're launched.
Otherwise, you can't create a compute environment and launch container instances into it. This
requirement applies to container instances launched with or without the Amazon ECS optimized AMI
provided by Amazon. For more information, see Amazon ECS instance role in the _Amazon Elastic Container Service Developer Guide_.

###### Topics

- [Check your account's Amazon ECS instance role](batch-check-ecsinstancerole.md "batch-check-ecsinstancerole.md")
