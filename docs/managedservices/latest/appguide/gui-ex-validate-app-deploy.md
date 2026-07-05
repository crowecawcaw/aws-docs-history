End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# Validate the Application Deployment

Navigate to the endpoint (LoadBalancerCName) of the previously-created load balancer, with the WordPress deployed path: /WordPress. For example:

```
http://stack-`ID-FOR-ELB`.us-east-1.elb.amazonaws.com/WordPress
```

You should see a page like this:

![WordPress installation page with fields for site title, username, password, and email.](images/wpFirstPage.png)
