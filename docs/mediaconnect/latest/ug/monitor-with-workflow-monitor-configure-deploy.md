# Deploying

templates to the signal map of your AWS media workflow

After you have attached the alarm and event templates to your signal map, you
must deploy the monitoring. Until the deployment is complete, the monitoring of
your signal map will not be active.

Workflow monitor will only deploy alarms that are relevant to the selected
signal map. For example, the attached alarm template group might contain
alarms for multiple services, such as MediaLive, MediaPackage, and MediaConnect. If the
selected signal map only contains MediaLive resources, no MediaPackage or MediaConnect alarms
will be deployed.

###### To deploy the monitoring templates

1. After attaching alarm and event template groups to your signal map
   and saving your changes, select **Deploy monitor**
   in the **Actions** dropdown menu.
2. You will be asked to confirm the deployment and presented with the
   number of CloudWatch and EventBridge resources that will be created. If you would
   like to proceed, select **Deploy**.

###### Note

There is no direct cost for using workflow monitor. However, there are costs associated with the resources created and used to monitor your workflow.

When monitoring is deployed, Amazon CloudWatch and Amazon EventBridge resources are created. When
using the AWS Management Console, prior to deploying monitoring to a signal map,
you will be notified of how many resources will be created. For more information
about pricing, see: [CloudWatch
pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") and [EventBridge pricing](https://aws.amazon.com/eventbridge/pricing/ "https://aws.amazon.com/eventbridge/pricing/").

Workflow monitor uses AWS CloudFormation templates to deploy the CloudWatch and EventBridge resources. These templates are stored in a
standard class Amazon Simple Storage Service bucket that is created on your behalf, by workflow monitor, during the deployment process and will incur object storage and recall charges.
For more information about pricing, see: [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"). 3. The status of the deployment is displayed next to the name of the
signal map. The deployment status is also visible in the
**Stacks** section of the CloudFormation console. After
a few moments of resource creation and deployment, your signal map
monitoring will begin.
