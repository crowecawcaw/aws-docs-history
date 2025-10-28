# When the service fails to create

If your attempt to create an App Runner service fails, the service enters a `CREATE_FAILED` status. This status appears as **Create
failed** on the console. A service might fail to create because of issues that are related to one or more of the following:

- Your application code
- The build process
- Configuration
- Resource quotas
- Temporary issues with the underlying AWS services that your service uses
  To troubleshoot a service failing to create, we recommend that you do the following.

1. Read the service events and logs to find out what caused the service to fail to create.
2. Make any necessary changes to your code or configuration.
3. If you reached your service quota, delete one or more services.
4. If you reached another resource quota, you might be able to increase it if it's adjustable.
5. Try rebuilding the service again after completing all of the above steps. For information on how to rebuild your service, see [Rebuilding a failed App Runner service](manage-rebuild.md "manage-rebuild.md").

###### Note

One of the adjustable resource quotas that might be causing an issue is the _Fargate On-Demand_ vCPU resource.

The vCPU resource count determines the number of instances that App Runner can provide to your service. This is an adjustable quota value for the
_Fargate On-Demand_ vCPU resource count that resides in the AWS Fargate service. To view the vCPU quota settings for your account or
to request a quota increase, use the Service Quotas console in the AWS Management Console. For more information, see [AWS Fargate service quotas](../../../AmazonECS/latest/developerguide/service-quotas.md#service-quotas-fargate "../../../AmazonECS/latest/developerguide/service-quotas.md#service-quotas-fargate") in the
_Amazon Elastic Container Service Developer Guide_.

###### Important

You don't incur any additional charges beyond the initial creation attempt for a failed service. Even though the failed service isn't usable, it
still counts towards your service quota. App Runner doesn't automatically delete the failed service, so make sure that you delete it when you're done
analyzing the failure.
