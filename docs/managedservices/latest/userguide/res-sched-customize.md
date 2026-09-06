

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Customizing AMS Resource Scheduler
<a name="res-sched-customize"></a>

We recommend you customize the following properties of AMS Resource Scheduler using the update AMS Resource Scheduler change types, see [AMS Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/ctref/management-ams-resource-scheduler-section.html).
+ **Tag name**: The name of the tag that Resource Scheduler will use to associate instance schedules with resources. The default value is Schedule.
+ **Scheduled Services**: A comma-separated list of services that Resource Scheduler can manage. The default value is "ec2,rds,autoscaling". Valid values are "ec2", "rds" and "autoscaling"
+ **Default timezone**: Specify the default time zone for the Resource Scheduler to use. The default value is UTC.
+ **Use CMK**: A comma-separated list of Amazon KMS Customer Managed Key (CMK) ARNs that Resource Scheduler can be granted permissions to.
+ **Use LicenseManager**: A comma-separated list of AWS Licence Manager ARNs to that Resource Scheduler can be granted permissions to.

**Note**  
AMS may, time to time, release features and fixes to keep AMS Resource Scheduler up to date in your account. When this happens, any customization that you make to the AMS Resource Scheduler are preserved.