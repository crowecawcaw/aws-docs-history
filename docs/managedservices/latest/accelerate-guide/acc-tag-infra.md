

# Accelerate-managed tags
<a name="acc-tag-infra"></a>

During onboarding to AMS Accelerate, several AWS resources are deployed to your account. So you can identify them, these resources are tagged with the following:


<table>
<thead>
  <tr><th>Key</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td>ams:resourceOwner</td><td>AMS</td></tr>
  <tr><td>ams:resourceOwnerService</td><td>A description of which AMS Accelerate service offering this resource comes from, for instance, AMS Deployment, Backup, Controls, Monitoring, Patch, and so forth.</td></tr>
  <tr><td>AppId</td><td rowspan="3">AMSInfrastructure</td></tr>
  <tr><td>AppName</td></tr>
  <tr><td>Environment</td></tr>
</tbody>
</table>


**Note**  
These tags are applied using CloudFormation stack-level tags, and rely on CloudFormation propagating the tags to created resources. For more information, see [ Resource tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).