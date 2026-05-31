# Resource integrations

## CloudFormation

Connect Customer is integrated with [CloudFormation](../../../AWSCloudFormation/latest/UserGuide/AWS_Connect.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Connect.md"), a service that allows you to treat infrastructure as code. Use CloudFormation to model, provision, and manage AWS and third-party
resources.

The following Connect Customer resource APIs support CloudFormation
templates:

- [AWS::Connect::ApprovedOrigin](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-approvedorigin.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-approvedorigin.md")
- [AWS::Connect::ContactFlow](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.md")
- [AWS::Connect::ContactFlowModule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.md")
- [AWS::Connect::EvaluationForm](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.md")
- [AWS::Connect::HoursOfOperation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.md")
- [AWS::Connect::Instance](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.md")
- [AWS::Connect::InstanceStorageConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.md")
- [AWS::Connect::IntegrationAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.md")
- [AWS::Connect::PhoneNumber](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.md")
- [AWS::Connect::Prompt](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.md")
- [AWS::Connect::Queue](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.md")
- [AWS::Connect::QuickConnect](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.md")
- [AWS::Connect::RoutingProfile](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.md")
- [AWS::Connect::Rule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.md")
- [AWS::Connect::SecurityKey](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.md")
- [AWS::Connect::TaskTemplate](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.md")
- [AWS::Connect::TrafficDistributionGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.md")
- [AWS::Connect::User](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.md")
- [AWS::Connect::UserHierarchyGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.md")
- [AWS::Connect::View](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.md")
- [AWS::Connect::ViewVersion](../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.md")

## CloudTrail

Connect Customer is integrated with AWS CloudTrail, a service that provides a
record of the Connect Customer API calls that a user, role, or AWS
service makes. CloudTrail captures Connect Customer API calls as events. All
public Connect Customer APIs support CloudTrail.

For more information, see [Logging Connect Customer API calls with AWS CloudTrail.](../adminguide/logging-using-cloudtrail.md "../adminguide/logging-using-cloudtrail.md")

## EventBridge

Connect Customer is integrated with Amazon EventBridge, a service that provides a
record of the Connect Customer API calls that a user, role, or AWS
service makes. All public Connect Customer APIs support EventBridge, with events
published to CloudTrail consumable in EventBridge.

Some Connect Customer resources are integrated directly into EventBridge. For
more information, see [EventBridge
events emitted by Connect Customer.](../adminguide/connect-eventbridge-events.md "../adminguide/connect-eventbridge-events.md")
