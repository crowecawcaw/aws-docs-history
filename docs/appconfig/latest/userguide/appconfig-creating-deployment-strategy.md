

# Working with deployment strategies
<a name="appconfig-creating-deployment-strategy"></a>

A deployment strategy enables you to slowly release changes to all targets or specific segments over minutes or hours—either session based or along your own target dimension by leveraging entity-based deployments.

**Note**  
AWS AppConfig Agent (version 2.0.136060 or later) supports deploying feature flag or free-form configuration data to specific segments or individual users during a gradual rollout. Entity-based gradual deployments ensure that once a user or segment receives a configuration version, they continue to receive that same version throughout the deployment period, regardless of which compute resource serves their requests. For more information, see [Using AWS AppConfig Agent for user- or entity-based gradual deployments](appconfig-agent-how-to-use.md#appconfig-entity-based-gradual-deployments).

An AWS AppConfig deployment strategy defines the following important aspects of a configuration deployment.



<table>
<thead>
  <tr><th>Setting</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Deployment type</td><td>Deployment type defines how the configuration deploys or <i>rolls out</i>. AWS AppConfig supports <b>Linear</b> and <b>Exponential</b> deployment types.<ul><li> <b>Linear</b>: For this type, AWS AppConfig processes the deployment by increments of the growth factor evenly distributed over the deployment. Here's an example timeline for a 10 hour deployment that uses 20% linear growth: <p><b></b></p>
<table>
<thead>
  <tr><th>Elapsed time</th><th>Deployment progress</th></tr>
</thead>
<tbody>
  <tr><td>0 hour</td><td>0%</td></tr>
  <tr><td>2 hour</td><td>20%</td></tr>
  <tr><td>4 hour</td><td>40%</td></tr>
  <tr><td>6 hour</td><td>60%</td></tr>
  <tr><td>8 hour</td><td>80%</td></tr>
  <tr><td>10 hour</td><td>100%</td></tr>
</tbody>
</table>
 </li><li> <b>Exponential</b>: For this type, AWS AppConfig processes the deployment exponentially using the following formula: <code>G*(2^N)</code>. In this formula, <code>G</code> is the step percentage specified by the user and <code>N</code> is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows: <pre>2*(2^0)<br />2*(2^1)<br />2*(2^2)</pre> <br />Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets. </li></ul></td></tr>
  <tr><td>Step percentage (growth factor)</td><td>This setting specifies the percentage of callers to target during each step of the deployment. In the SDK and the <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateDeploymentStrategy.html">AWS AppConfig API Reference</a>, <code>step percentage</code> is called <code>growth factor</code>. </td></tr>
  <tr><td>Deployment time</td><td>This setting specifies an amount of time during which AWS AppConfig deploys to hosts. This is not a timeout value. It is a window of time during which the deployment is processed in intervals.</td></tr>
  <tr><td>Bake time</td><td>This setting specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see <a href="setting-up-appconfig.md#getting-started-with-appconfig-cloudwatch-alarms-permissions">Configure permissions for automatic rollback</a>.</td></tr>
</tbody>
</table>


You can choose a predefined strategy included with AWS AppConfig or create your own. 

**Note**  
AWS AppConfig Agent (version 2.0.136060 or later) supports deploying feature flag or free-form configuration data to specific segments or individual users during a gradual rollout. Entity-based gradual deployments ensure that once a user or segment receives a configuration version, they continue to receive that same version throughout the deployment period, regardless of which compute resource serves their requests. For more information, see [Using AWS AppConfig Agent for user- or entity-based gradual deployments](appconfig-agent-how-to-use.md#appconfig-entity-based-gradual-deployments).

**Topics**
+ [Using predefined deployment strategies](appconfig-creating-deployment-strategy-predefined.md)
+ [Create a deployment strategy](appconfig-creating-deployment-strategy-create.md)