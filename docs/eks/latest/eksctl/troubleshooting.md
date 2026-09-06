

# Troubleshooting
<a name="troubleshooting"></a>

This topic includes instructions on how to resolve common errors with Eksctl.

## Failed stack creation
<a name="_failed_stack_creation"></a>

You can use the `--cfn-disable-rollback` flag to stop Cloudformation from rolling back failed stacks to make debugging easier.

## subnet ID "subnet-11111111" is not the same as "subnet-22222222"
<a name="_subnet_id_subnet_11111111_is_not_the_same_as_subnet_22222222"></a>

Given a config file specifying subnets for a VPC like the following:

```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: test
  region: us-east-1

vpc:
  subnets:
    public:
      us-east-1a: {id: subnet-11111111}
      us-east-1b: {id: subnet-22222222}
    private:
      us-east-1a: {id: subnet-33333333}
      us-east-1b: {id: subnet-44444444}

nodeGroups: []
```

An error `subnet ID "subnet-11111111" is not the same as "subnet-22222222"` means that the subnets specified are not placed in the right Availability zone. Check in the AWS console which is the right subnet ID for each Availability Zone.

In this example, the correct configuration for the VPC would be:

```
vpc:
  subnets:
    public:
      us-east-1a: {id: subnet-22222222}
      us-east-1b: {id: subnet-11111111}
    private:
      us-east-1a: {id: subnet-33333333}
      us-east-1b: {id: subnet-44444444}
```

## Deletion issues
<a name="_deletion_issues"></a>

If your delete does not work, or you forget to add `--wait` on the delete, you may need to go to use amazon’s other tools to delete the cloudformation stacks. This can be accomplished via the gui or with the aws cli.

## kubectl logs and kubectl run fails with Authorization Error
<a name="_kubectl_logs_and_kubectl_run_fails_with_authorization_error"></a>

If your nodes are deployed in a private subnet and `kubectl logs` or `kubectl run` fail with an error such as the following:

```
Error attaching, falling back to logs: unable to upgrade connection: Authorization error (user=kube-apiserver-kubelet-client, verb=create, resource=nodes, subresource=proxy)
```

```
Error from server (InternalError): Internal error occurred: Authorization error (user=kube-apiserver-kubelet-client, verb=get, resource=nodes, subresource=proxy)
```

Then you might need to set [enableDnsHostnames](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support). More details can be found in [this issue](https://github.com/eksctl-io/eksctl/issues/4645).