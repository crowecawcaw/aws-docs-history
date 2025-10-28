# Creating resiliency policies

In AWS Resilience Hub, you can create a resiliency policy. A resiliency policy contains
information and objectives that you use to assess whether your application can recover
from a disruption type, such as software, hardware, Availability Zone, or AWS Region.
These policies do not change or affect an actual application. Multiple applications can
have the same resiliency policy.

When you create a resiliency policy, you define the recovery time objective (RTO) and
recovery point objective (RPO) targets. When you run an assessment, AWS Resilience Hub determines
whether the application is estimated to meet the objectives that are defined in the
resiliency policy.

The assessment evaluates your application configuration against the attached
resiliency policy. At the end of the process, AWS Resilience Hub provides an assessment of how
your application measures against the objectives in your resiliency policy.

###### Note

AWS Resilience Hub allows you to enter a value zero in the **RTO** and
**RPO** fields of your resiliency policy. But, while assessing
your application, the lowest possible assessment result is near zero. Hence, if you
enter a value zero in the **RTO** and **RPO**
fields, the estimated workload RTO and estimated workload RPO result will be near
zero and the **Compliance status** for your application will be set
to **Policy breached**.

You can create resiliency policies in Applications, and also in Resiliency policies.
You can access relevant details about your policies, and also modify and delete
them.

###### To create resiliency policies in Applications

1. In the left navigation menu, choose **Applications**.
2. Complete the procedures from [Get started by adding an application](describe-app-intro.md "describe-app-intro.md") through
   [Add tags](add-tags.md "add-tags.md") .
3. In **Resiliency policies** section, choose **Create
   resiliency policy**.

The **Create resiliency policy** page displays. 4. In the **Choose a creation method** section, select
**Create a policy**. 5. Enter a name for the policy. 6. (Optional) Enter a description for the policy. 7. Choose one of the following from **Tier** dropdown
list:

    * **Foundational IT core services**
    * **Mission critical**
    * **Critical**
    * **Important**
    * **Non critical**

8. For both **RTO** and **RPO** targets, under
   **Customer Application RTO and RPO**, enter a numeric value
   in the box, and then choose the unit of time that the value represents.

Repeat these entries under **Infrastructure RTO and RPO** for
**Infrastructure** and **Availability
Zone**. 9. (Optional) If you have a multi-Region application, you may want to define a
Region's RTO and RPO targets.

Turn-on **Region**. For both Region **RTO**
and **RPO** targets, under **Customer Application RTO
and RPO**, enter a numeric value in the box, and then choose the
unit of time that the value represents. 10. (Optional) If you want to add tags, you can do that later as you continue
creating your policy. For more information about tags, see [Tagging
resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General
Reference_. 11. To create the policy, choose **Create**.

###### To create resiliency policies in Resiliency policies

1. In the left navigation menu, choose **Policies**.
2. In **Resiliency policies** section, choose
   **Create resiliency policy**.

The **Create resiliency policy** page displays. 3. Enter a name for the policy. 4. (Optional) Enter a description for the policy. 5. Choose one of the following from **Tier**:

    * **Foundational IT core services**
    * **Mission critical**
    * **Critical**
    * **Important**
    * **Non critical**

6. For both **RTO** and **RPO** targets, under
   **Customer Application RTO and RPO**, enter a numeric value
   in the box and then choose the unit of time that the value represents.

Repeat these entries under **Infrastructure RTO and RPO** for
**Infrastructure** and **Availability
Zone**. 7. (Optional) If you have a multi-Region application, you may want to define a
Region's RTO and RPO targets.

Turn-on **Region**. For both **RTO** and
**RPO** targets, under **Customer Application RTO
and RPO**, enter a numeric value in the box and then choose the
unit of time that the value represents. 8. (Optional) If you want to add tags, you can do that later as you continue
creating your policy. For more information about tags, see [Tagging
resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General
Reference_. 9. To create the policy, choose **Create**.

###### To create resiliency policies based on a suggested policy

1. In the left navigation menu, choose **Policies**.
2. In the **Choose a creation method** section, select
   **Select a policy based on a suggested policy**.
3. In **Resiliency policies** section, choose
   **Create resiliency policy**.

The **Create resiliency policy** page displays. 4. Enter a name for the resiliency policy. 5. (Optional) Enter a description for the policy. 6. Under **Suggested resiliency policies** section, view and
choose one of the following predetermined resiliency policy tiers:

    * **Non-critical application**
    * **Important Application**
    * **Critical Application**
    * **Global Critical Application**
    * **Mission Critical Application**
    * **Global Mission Critical
     Application**
    * **Foundational Core Service**

7. To create the resiliency policy, choose **Create
   policy**.
