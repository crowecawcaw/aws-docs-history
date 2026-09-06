

# Valid configuration parameters for each provider type
<a name="structure-configuration-examples"></a>

This section lists valid `configuration` parameters for each action provider.

Every action must have a valid action configuration, which depends on the provider type for that action. The following table lists the required action configuration elements for each valid provider type:


**Action configuration properties for provider types**  

<table>
<thead>
  <tr><th>Name of provider</th><th>Provider name in action type</th><th>Configuration properties</th><th>Required/Optional</th></tr>
</thead>
<tbody>
  <tr><td>Amazon S3 (Deploy action provider)</td><td colspan="3">For more information, including examples related to Amazon S3 Deploy action parameters, see <a href="action-reference-S3Deploy.md">Amazon S3 deploy action reference</a>.</td></tr>
  <tr><td>Amazon S3 (Source action provider)</td><td colspan="3">For more information, including examples related to Amazon S3 source action parameters, see <a href="action-reference-S3.md">Amazon S3 source action reference</a>.</td></tr>
  <tr><td>Amazon ECR</td><td colspan="3">For more information, including examples related to Amazon ECR parameters, see <a href="action-reference-ECR.md">Amazon ECR source action reference</a>.</td></tr>
  <tr><td>CodeCommit</td><td colspan="3">For more information, including examples related to CodeCommit parameters, see <a href="action-reference-CodeCommit.md">CodeCommit source action reference</a>.</td></tr>
  <tr><td>CodeStarSourceConnection action for Bitbucket, GitHub (via GitHub app), GHES, and GitLab</td><td colspan="3">For more information, including examples of the action configuration, see <a href="action-reference-CodestarConnectionSource.md#action-reference-CodestarConnectionSource-config">Configuration parameters</a>.</td></tr>
  <tr><td>GitHub (via OAuth app)</td><td colspan="3">For more information, including examples related to GitHub parameters, see <a href="appendix-github-oauth.md#action-reference-GitHub">GitHub (via OAuth app) source action reference</a>. This is the Version 1 GitHub action.</td></tr>
  <tr><td>AWS CloudFormation</td><td colspan="3">For more information, including examples related to AWS CloudFormation parameters, see <a href="action-reference-CloudFormation.md">CloudFormation deploy action reference</a>.</td></tr>
  <tr><td>CodeBuild</td><td colspan="3">For more description and examples related to CodeBuild parameters, see <a href="action-reference-CodeBuild.md">AWS CodeBuild build and test action reference</a>.</td></tr>
  <tr><td>CodeDeploy</td><td colspan="3">For more description and examples related to CodeDeploy parameters, see <a href="action-reference-CodeDeploy.md">AWS CodeDeploy deploy action reference</a>.</td></tr>
  <tr><td>AWS Device Farm</td><td colspan="3">For more description and examples related to AWS Device Farm parameters, see <a href="action-reference-DeviceFarm.md">AWS Device Farm test action reference</a>.</td></tr>
  <tr><td rowspan="2">AWS Elastic Beanstalk</td><td rowspan="2"><code>ElasticBeanstalk</code></td><td><code>ApplicationName</code> </td><td>Required</td></tr>
  <tr><td><code>EnvironmentName</code></td><td>Required</td></tr>
  <tr><td>AWS Lambda</td><td colspan="3">For more information, including examples related to AWS Lambda parameters, see <a href="action-reference-Lambda.md">AWS Lambda invoke action reference</a>.</td></tr>
  <tr><td rowspan="3">AWS OpsWorks Stacks</td><td rowspan="3"><code>OpsWorks</code></td><td><code>Stack</code> </td><td>Required</td></tr>
  <tr><td><code>Layer</code></td><td>Optional</td></tr>
  <tr><td><code>App</code></td><td>Required</td></tr>
  <tr><td>Amazon ECS</td><td colspan="3">For more description and examples related to Amazon ECS parameters, see <a href="action-reference-ECS.md">Amazon Elastic Container Service deploy action reference</a>.</td></tr>
  <tr><td>Amazon ECS and CodeDeploy(Blue/Green)</td><td colspan="3">For more description and examples related to Amazon ECS and CodeDeploy blue/green parameters, see <a href="action-reference-ECSbluegreen.md">Amazon Elastic Container Service and CodeDeploy blue-green deploy action reference</a>.</td></tr>
  <tr><td rowspan="5">Service Catalog</td><td rowspan="5"><code>ServiceCatalog</code></td><td><code>TemplateFilePath</code></td><td>Required</td></tr>
  <tr><td><code>ProductVersionName</code></td><td>Required</td></tr>
  <tr><td><code>ProductType</code></td><td>Required</td></tr>
  <tr><td><code>ProductVersionDescription</code></td><td>Optional</td></tr>
  <tr><td><code>ProductId</code></td><td>Required</td></tr>
  <tr><td rowspan="4">Alexa Skills Kit</td><td rowspan="4"><code>AlexaSkillsKit</code></td><td><code>ClientId</code></td><td>Required</td></tr>
  <tr><td><code>ClientSecret</code></td><td>Required</td></tr>
  <tr><td><code>RefreshToken</code></td><td>Required</td></tr>
  <tr><td><code>SkillId</code></td><td>Required</td></tr>
  <tr><td>Jenkins</td><td>The name of the action you provided in the CodePipeline Plugin for Jenkins (for example, {{MyJenkinsProviderName}})</td><td><code>ProjectName</code></td><td>Required</td></tr>
  <tr><td rowspan="3">Manual Approval</td><td rowspan="3"><code>Manual</code></td><td><code>CustomData</code></td><td>Optional</td></tr>
  <tr><td><code>ExternalEntityLink</code></td><td>Optional</td></tr>
  <tr><td><code>NotificationArn</code></td><td>Optional</td></tr>
</tbody>
</table>


The following example shows a valid configuration for a deploy action that uses Alexa Skills Kit:

```
"configuration": {
  "ClientId": "amzn1.application-oa2-client.aadEXAMPLE",
  "ClientSecret": "****",
  "RefreshToken": "****",
  "SkillId": "amzn1.ask.skill.22649d8f-0451-4b4b-9ed9-bfb6cEXAMPLE"
}
```

The following example shows a valid configuration for a manual approval:

```
"configuration": {
  "CustomData": "Comments on the manual approval",
  "ExternalEntityLink": "http://my-url.com",
  "NotificationArn": "arn:aws:sns:us-west-2:12345EXAMPLE:Notification"
}
```