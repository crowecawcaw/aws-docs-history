

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS recommended tags
<a name="ams-tags"></a>

AMS recommends the following tags on supported resources. Starred (\*) tags are highly recommended.

**Note**  
You can use tags to schedule patching. For information, see [AMS Advanced Patch Orchestrator: a tag-based patching model](https://docs.aws.amazon.com/managedservices/latest/userguide/patch-orchestrator.html).


**AMS recommended tags**  

<table>
<thead>
  <tr><th>Tag key</th><th>Supported values</th><th>Notes</th></tr>
</thead>
<tbody>
  <tr><td><code>AppName</code>*</td><td rowspan="3">Unconstrained.</td><td rowspan="2">Identify the applications that will reside on, or require access to, the resource. This facilitates tracking and communications between AMS and you. </td></tr>
  <tr><td><code>AppId</code>*</td></tr>
  <tr><td><code>EnvironmentType</code>*</td><td>Distinguish between development, test, and production infrastructure as the environment for the resource.</td></tr>
  <tr><td><code>OwnerTeamEmail</code>*</td><td>Distribution list email address</td><td>Identify the distribution list email address for the team responsible for the resource. The email should not be a personal email; it must be an anonymous email like a distribution list. </td></tr>
  <tr><td colspan="3"></td></tr>
  <tr><td><code>ComplianceFramework</code></td><td rowspan="6">Unconstrained</td><td>Identify which controls and policies should be applied to the resource.</td></tr>
  <tr><td><code>CostCenter</code></td><td>Identify the cost center or business unit associated with a resource (typically for cost allocation and tracking).</td></tr>
  <tr><td><code>Customer</code></td><td>Used by AMS customers that have resources from multiple customers (AMS sub-customers). To group resources in the managed environment into the specific customer they are serving. Identify a specific client on a particular group of resources or services.</td></tr>
  <tr><td><code>DataClassification</code></td><td>Identify the specific data-confidentiality level a resource supports. Identify which controls and policies should be applied to the resource.</td></tr>
  <tr><td><code>HoursOfOperation</code></td><td>Identify the date or time a resource should be started, stopped, deleted, or rotated.</td></tr>
  <tr><td><code>OwnerTeam</code></td><td>Identify the team responsible for the resource. Facilitates communication with the team responsible for the resource.</td></tr>
  <tr><td><code>Patch Group</code></td><td>You have two options:<ul><li>You can submit a service request with the information outlined in <a href="https://docs.aws.amazon.com/managedservices/latest/userguide/patch-orchestrator.html">AMS Advanced Patch Orchestrator: a tag-based patching model</a>, and AMS creates on your specified resources, and using the information you provide, a <code>Patch Group</code> tag for you.</li><li>If you have already created a <code>Patch Group</code> tag on your resources, the supported values are unconstrained.</li></ul></td><td>What resources to include in an automated patching maintenance window.</td></tr>
  <tr><td><code>ProjectId</code></td><td>Unconstrained</td><td>Identify the projects the resource supports.</td></tr>
  <tr><td><code>SupportPriority</code></td><td>One of six possible acronyms for Confidentiality, Integrity, or Availability; the order of the acronym is the priority. For example, I.C.A. would mean the order is Integrity, Confidentiality, Availability. Other acceptable values are C.I.A., C.A.I., I.A.C., A.C.I., and A.I.C.</td><td>Identify which type of support should be priority: Confidentiality, Integrity, or Availability.</td></tr>
</tbody>
</table>
