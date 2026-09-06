

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Create the Infrastructure
<a name="ex-create-wp-infra-deploy"></a>

The following procedures describe creating an RDS database, a load balancer, and an Auto Scaling group in such a manner that you use the resource IDs to build the infrastructure.

## Create an ELB Stack
<a name="ex-WP-stack-elb-create"></a>

Launch a public load balancer (ELB). See [Load Balancer (ELB) Stack \| Create](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-load-balancer-elb-stack-create.html).

## Create an Auto Scaling Group Stack
<a name="ex-WP-stack-asg-create"></a>

Launch an Auto scaling group.

See [Auto Scaling Group \| Create](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-auto-scaling-group-create.html).

## Create an S3 Store
<a name="ex-WP-stack-s3-create"></a>

Launch an S3 bucket. The S3 bucket is where you upload the application bundle you created. See [S3 Storage \| Create](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-s3-storage-create.html).