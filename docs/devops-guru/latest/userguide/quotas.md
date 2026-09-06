

# Quotas and limits for Amazon DevOps Guru
<a name="quotas"></a>

The following table lists the current quota in Amazon DevOps Guru. This quota is for each supported AWS Region for each AWS account. 

## Notifications
<a name="notifications-quota"></a>



|  |  | 
| --- |--- |
| Maximum number of Amazon Simple Notification Service topics you can specify at once | 2 | 

## CloudFormation stacks
<a name="cnf-stack-quota"></a>



|  |  | 
| --- |--- |
| Maximum number of AWS CloudFormation stacks you can specify | 1000 | 

## DevOps Guru resource monitoring limits
<a name="resource-monitoring-limits"></a>



| Resource description | Limit | Can be increased | 
| --- | --- | --- | 
| Default limit for monitoring Amazon Simple Queue Service (Amazon SQS) queues | 100\* | Yes\*\* | 

\*For new DevOps Guru accounts created on or after June 29, 2023, and for existing accounts that were active as of the same date and have less than 100 Amazon SQS queues.

\*\*To request a change in this limit, contact Support at [https://aws.amazon.com/contact-us](https://aws.amazon.com/contact-us). You can request an Amazon SQS queue monitoring limit of 100, 500, 1,000, 5,000, or 10,000.

## DevOps Guru quotas for creating, deploying, and managing an API
<a name="devops-guru-control-service-limits-table"></a>

The following fixed quotas apply to creating, deploying, and managing an API in DevOps Guru, using the AWS CLI, the API Gateway console, or the API Gateway REST API and its SDKs.

 For a list of all DevOps Guru APIs, see [ Amazon DevOps Guru Actions](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_Operations.html).


| Default quota | Can be increased | 
| --- | --- | 
| 20 requests every 1 second per account | Yes | 