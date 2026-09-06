

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Update Strategies
<a name="update-strategies"></a>

There are a few different strategies you can employ to update your applications or instances in your AMS-managed environment.
+ Scheduled Downtime: This simple strategy involves scheduling time for your application to be offline and manually updated. To do this, submit a Management \| Other \| Other \| Update CT (ct-0xdawir96cy7k) request to stop the required instances. Make the necessary updates, and then submit another Management \| Other \| Other \| Update CT (ct-0xdawir96cy7k) request to start the instances.

  
+ Blue/Green: This strategy requires that you have a redundant environment (two completely functional environments) and take one environment offline using domain name system (DNS) or web firewall (WAF) updates to redirect traffic. Update one environment and then redirect again to update the other environment.

  To learn more, see [ AWS CodeDeploy Introduces Blue/Green Deployments.](https://aws.amazon.com/about-aws/whats-new/2017/01/aws-codedeploy-introduces-blue-green-deployments/)
+ Rolling Update with new AMI: This is where you have a new AMI that you customize (see [Create AMI](https://docs.aws.amazon.com/managedservices/latest/ctref/ex-create-ami.html)) and then request that AMS deploy it to your Auto Scaling group. Use a Management \| Other \| Other \| Update CT (ct-0xdawir96cy7k) to do this.