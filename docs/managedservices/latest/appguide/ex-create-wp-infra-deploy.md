# Create the Infrastructure

The following procedures describe creating an RDS database, a load balancer, and an Auto Scaling group in such a manner that you use the resource IDs to build the
infrastructure.

## Create an ELB Stack

Launch a public load balancer (ELB). See
[Load Balancer (ELB) Stack | Create](../ctref/deployment-advanced-load-balancer-elb-stack-create.md "../ctref/deployment-advanced-load-balancer-elb-stack-create.md").

## Create an Auto Scaling Group Stack

Launch an Auto scaling group.

See
[Auto Scaling Group | Create](../ctref/deployment-advanced-auto-scaling-group-create.md "../ctref/deployment-advanced-auto-scaling-group-create.md").

## Create an S3 Store

Launch an S3 bucket. The S3 bucket is where you upload the application bundle you created. See
[S3 Storage | Create](../ctref/deployment-advanced-s3-storage-create.md "../ctref/deployment-advanced-s3-storage-create.md").
