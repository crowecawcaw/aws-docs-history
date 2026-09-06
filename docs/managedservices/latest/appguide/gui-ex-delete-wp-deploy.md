

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Tear Down the Application Deployment
<a name="gui-ex-delete-wp-deploy"></a>

To tear down the deployment, you submit the Delete Stack CT against the RDS database stack, the application load balancer, the Auto Scaling group, the S3 bucket, and the Code Deploy application and group--six RFCs in all. Additionally, you can submit a service request for the RDS snapshots to be deleted (they are deleted automatically after ten days, but they do cost a small amount while there). Gather the stack IDs for all and then follow these steps. See [Stack \| Delete](https://docs.aws.amazon.com/managedservices/latest/ctref/management-standard-stack-delete.html).