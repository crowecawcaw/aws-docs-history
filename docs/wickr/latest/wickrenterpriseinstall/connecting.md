This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Connecting to the Kubernetes cluster

The Amazon EKS API is accessible only through a bastion host that is created as a part of the
deployment. As a result, all `kubectl` commands must either be run on the bastion
host itself or be proxied through the bastion host.

## Proxying

connections through the bastion

The first time you're connecting to the cluster, you must update your local kubeconfig
file using the `aws eks update-kubeconfig` command, and then set the
`proxy-url` in your configuration. Then, each time you want to connect to
the cluster, you start an SSM session with the bastion host to port forward to the proxy
for API access.

**One-time setup**

There is an output value on the `WickrEks` CloudFormation stack with a name
that begins with `WickrEnterpriseConfigCommand`. The value contains the full
command needed to generate the kubectl configuration for your cluster. This output can
be viewed with the following command:

```
aws cloudformation describe-stacks --stack-name WickrEks \
--query 'Stacks[0]`.Outputs`[?starts_with(OutputKey, `WickrEnterpriseConfigCommand`)]`.OutputValue`' \
--output text
```

This should output a command that begins with `aws eks update-kubeconfig`.
Run this command.

Next, the Kubernetes configuration must be modified to proxy requests through the
bastion host. This can be done using the following commands:

```
CLUSTER_ARN=$(aws cloudformation describe-stacks --stack-name WickrEks --query 'Stacks[0].Outputs[?OutputKey==`WickrEnterpriseEksClusterArn`].OutputValue' --output text)
kubectl config set `"clusters.${CLUSTER_ARN}.proxy-url"` http://localhost:8888
```

If it worked correctly, you will see output like `'Property
 "clusters.arn:aws:eks:us-west-2:012345678912:cluster/WickrEnterprise5B8BF472-1234a41c4ec48b7b615c6789d93dcce.proxy-url"
 set.'`

**Port forward to the bastion**

To connect to the Amazon EKS cluster, you must start an SSM session to port forward
requests to the proxy running on your bastion host. The command to do this is provided
as the output `BastionSSMProxyEKSCommand` on the `WickrEks` stack.
Run the following command to view the output value:

```
aws cloudformation describe-stacks --stack-name WickrEks \
--query 'Stacks[0]`.Outputs`[?OutputKey==`BastionSSMProxyEKSCommand`]`.OutputValue`' \
--output text
```

The command that it outputs will begin with `aws ssm start-session`. Run
this command to start a local proxy running on port 8888 through which you can connect
to the Amazon EKS cluster. If the port forward worked correctly, the output should say
'Waiting for connections...'. Keep this process running the entire time that you need to
access the Amazon EKS cluster.

If everything is set up correctly, you will be able to run `kubectl get nodes` in another terminal to list the worker nodes in the Amazon EKS cluster:

```
kubectl get nodes
   NAME                           STATUS   ROLES    AGE     VERSION
   ip-10-0-111-216.ec2.internal   Ready     none   3d      v1.26.4-eks-0a21954
   ip-10-0-180-1.ec2.internal     Ready     none   2d23h   v1.26.4-eks-0a21954
   ip-10-0-200-102.ec2.internal   Ready     none   3d      v1.26.4-eks-0a21954

```
