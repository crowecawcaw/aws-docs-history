

# Resource integrations
<a name="resource-integrations"></a>

## CloudFormation
<a name="cloudformation-integration"></a>

Connect Customer is integrated with [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Connect.html), a service that allows you to treat infrastructure as code. Use CloudFormation to model, provision, and manage AWS and third-party resources. 

The following Connect Customer resource APIs support CloudFormation templates:
+ [AWS::Connect::ApprovedOrigin](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-approvedorigin.html)
+ [AWS::Connect::ContactFlow](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html)
+ [AWS::Connect::ContactFlowModule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html)
+ [AWS::Connect::EvaluationForm](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html)
+ [AWS::Connect::HoursOfOperation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html)
+ [AWS::Connect::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html)
+ [AWS::Connect::InstanceStorageConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html)
+ [AWS::Connect::IntegrationAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.html)
+ [AWS::Connect::PhoneNumber](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html)
+ [AWS::Connect::Prompt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html)
+ [AWS::Connect::Queue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html)
+ [AWS::Connect::QuickConnect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html)
+ [AWS::Connect::RoutingProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html)
+ [AWS::Connect::Rule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html)
+ [AWS::Connect::SecurityKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.html)
+ [AWS::Connect::TaskTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html)
+ [AWS::Connect::TrafficDistributionGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html)
+ [AWS::Connect::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html)
+ [AWS::Connect::UserHierarchyGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html)
+ [AWS::Connect::View](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html)
+ [AWS::Connect::ViewVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html)

## CloudTrail
<a name="cloudtrail-integration"></a>

Connect Customer is integrated with AWS CloudTrail, a service that provides a record of the Connect Customer API calls that a user, role, or AWS service makes. CloudTrail captures Connect Customer API calls as events. All public Connect Customer APIs support CloudTrail. 

For more information, see [Logging Connect Customer API calls with AWS CloudTrail.](https://docs.aws.amazon.com/connect/latest/adminguide/logging-using-cloudtrail.html) 

## EventBridge
<a name="eventbridge-integration"></a>

Connect Customer is integrated with Amazon EventBridge, a service that provides a record of the Connect Customer API calls that a user, role, or AWS service makes. All public Connect Customer APIs support EventBridge, with events published to CloudTrail consumable in EventBridge. 

Some Connect Customer resources are integrated directly into EventBridge. For more information, see [EventBridge events emitted by Connect Customer.](https://docs.aws.amazon.com/connect/latest/adminguide/connect-eventbridge-events.html) 