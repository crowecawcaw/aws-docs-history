

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Validate the Application Deployment
<a name="gui-ex-validate-app-deploy"></a>

Navigate to the endpoint (LoadBalancerCName) of the previously-created load balancer, with the WordPress deployed path: /WordPress. For example:

```
http://stack-{{ID-FOR-ELB}}.us-east-1.elb.amazonaws.com/WordPress
```

You should see a page like this:

![WordPress installation page with fields for site title, username, password, and email.](http://docs.aws.amazon.com/managedservices/latest/appguide/images/wpFirstPage.png)
