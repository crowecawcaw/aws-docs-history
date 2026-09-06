

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Tear Down the High Availability Deployment
<a name="gui-ex-delete-ha-deploy"></a>

To tear down the deployment, you submit the Delete Stack CT against the HA Two-Tier stack, and the S3 bucket, and you can request that RDS snapshots be deleted (they are deleted automatically after ten days, but they do cost a small amount while there). Gather the stack IDs for the HA stack and the S3 bucket and then follow these steps. See [Stack \| Delete](https://docs.aws.amazon.com/managedservices/latest/ctref/management-standard-stack-delete.html).