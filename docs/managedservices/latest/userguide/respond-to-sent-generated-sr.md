

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Responding to an AMS-generated service requests
<a name="respond-to-sent-generated-sr"></a>

AMS patch management sends service requests (aka service notification) to you prior to the time of your set maintenance window; for more information, see [AMS maintenance window](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-sd.html#maintenance-win). AMS also sends service notifications to you when there is a chance that your infrastructure will be impacted by an AWS service or when an EC2 instance in your account may need to be rebooted; for more information, see [Service notifications](https://docs.aws.amazon.com/managedservices/latest/userguide/service-notices.html).

**Note**  
AMS sends communications to the primary email address on your AWS account that you have given; we recommend adding an alternate Operations contact email alias to facilitate the service request or service notification management process. Adding these emails is covered during the AMS onboarding process and related onboarding documentation.