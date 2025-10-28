# Set RTO and RPO

You can define a new resiliency policy with your own RTO/RPO targets, or you can choose an
existing resiliency policy with predefined RTO/RPO targets. If you want to use one of the
existing resiliency policies, select **Choose an existing policy** option and
select an existing target application from the **Option item** drop-down
list.

###### To define your own RTO/RPO targets

1. Select **Create a new resiliency policy** option.
2. Enter a name for the resiliency policy in the **Enter policy name** box
   (under **Name**).

We have pre-populated this field with an auto-generated name. You can choose to use the
same, or provide a different name. 3. (Optional) Enter a description for the resiliency policy in the
**Description** box. 4. Define your RTO/RPO in the **RTO/RPO targets** section.

###### Note

    * We have pre-populated a default RTO and RPO for your application. You can change the
     RTO and RPO now, or after you assess the application.
    * AWS Resilience Hub allows you to enter a value zero in the **RTO** and
     **RPO** fields of your resiliency policy. But, while assessing your
     application, the lowest possible assessment result is near zero. Hence, if you enter a value
     zero in the **RTO** and **RPO** fields, the estimated
     workload RTO and estimated workload RPO results will be near zero and the
     **Compliance status** for your application will be set to **Policy
     breached**.

5. To define RTO/RPO for your infrastructure and AZ, choose the right arrow to expand the
   **Infrastructure RTO and RPO** section.
6. In **RTO/RPO targets**, enter a numeric value in the box and then choose
   the unit of time that the value represents for both **RTO** and
   **RPO**.

Repeat these entries for **Infrastructure** and **Availability
Zone** in **Infrastructure RTO and RPO** section. 7. (Optional) If you have a multi-Region application and if you want to define a Region RTO
and RPO, turn on **Region - Optional**.

In **RTO** and **RPO**, enter a numeric value in the box
and then choose the unit of time that the value represents for both **RTO**
and **RPO**.

## Next

[Setup scheduled assessments and drift
notification](scheduled-assessment.md "scheduled-assessment.md")
