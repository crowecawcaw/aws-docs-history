# Tear Down the Application Deployment

To tear down the deployment, you submit the Delete Stack CT against the RDS database stack, the application load balancer, the Auto Scaling group, the S3 bucket, and
the Code Deploy application and group--six RFCs in all. Additionally, you can submit a service request for the RDS snapshots to be deleted
(they are deleted automatically after ten days, but they do cost a small amount while there). Gather the stack IDs for all and then follow these steps.
See [Stack | Delete](../ctref/management-standard-stack-delete.md "../ctref/management-standard-stack-delete.md").
