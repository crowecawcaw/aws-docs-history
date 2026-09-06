

# Restrict worker access to tasks to allowable IP addresses
<a name="sms-workforce-management-private-api-cidr"></a>

By default, a workforce isn't restricted to specific IP addresses. You can use the [`UpdateWorkforce`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateWorkforce.html) operation to require that workers use a specific range of IP addresses ([CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)) to access tasks. If you specify one or more CIDRs, workers who attempt to access tasks using any IP address outside the specified ranges are denied and will get a HTTP 204 No Content error message on the worker portal. You can specify up to 10 CIDR values using `UpdateWorkforce`. 

After you have restricted your workforce to one or more CIDRs, the output of `UpdateWorkforce` lists all allowable CIDRs. You can also use the [`DescribeWorkforce`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeWorkforce.html) operation to view all allowable CIDRs for a workforce. 