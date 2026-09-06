

# Amazon SQS access control architecture
<a name="sqs-creating-custom-policies-architecture"></a>

The following diagram describes the access control for your Amazon SQS resources.

![Describes access control for your Amazon SQS resources.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/AccessPolicyLanguage_Arch_Overview.png)


![In the previous diagram, section number one.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/number-1-red.png) You, the resource owner.

![In the previous diagram, section number two.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/number-2-red.png) Your resources contained within the AWS service (for example, Amazon SQS queues).

![In the previous diagram, section number three.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/number-3-red.png) Your policies. It is a good practice to have one policy per resource. The AWS service provides an API you use to upload and manage your policies.

![In the previous diagram, section number four.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/number-4-red.png) Requesters and their incoming requests to the AWS service.

![In the previous diagram, section number five.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/number-5-red.png) The access policy language evaluation code. This is the set of code within the AWS service that evaluates incoming requests against the applicable policies and determines whether the requester is allowed access to the resource.