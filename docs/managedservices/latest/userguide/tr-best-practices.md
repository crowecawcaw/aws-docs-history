

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Best practices in Trusted Remediator
<a name="tr-best-practices"></a>

The following are best practices to help you use Trusted Remediator:
+ If you're unsure about the remedation results, start with manual execution mode. Sometimes, applying automated execution for remediations from the start might cause unexpected results.
+ Conduct a weekly review of the remediations and OpsItems to gain insights in the Trusted Remediator results.
+ Member accounts inherit the configurations from the delegated administrator account. So, it’s important to structure the accounts in a way that helps you manage multiple accounts with the same configurations. You can exempt resources from the default configuration using tags.