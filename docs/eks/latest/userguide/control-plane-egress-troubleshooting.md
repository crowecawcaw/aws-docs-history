**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshooting control plane egress issues

When using the `CUSTOMER_ROUTED` control plane egress mode, you are responsible for network connectivity from the control plane ENIs. This page covers common issues and their solutions.

## Detect a failing webhook

When the control plane can’t reach a webhook server or OIDC provider, the symptom usually surfaces as a webhook timeout. To confirm, create or modify a resource that triggers the webhook and check the error:

```
kubectl apply -f my-resource.yaml
```

A connectivity or DNS failure typically returns an error similar to the following:

```
Error from server (InternalError): error when creating "my-resource.yaml": Internal error occurred:
failed calling webhook "my-webhook.example.com": failed to call webhook:
Post "https://my-webhook.example.com/validate?timeout=10s": context deadline exceeded
```

You can also check recent events for webhook errors across the cluster:

```
kubectl get events --all-namespaces --field-selector reason=FailedCreate
```

- If the error is a timeout (`context deadline exceeded`) or connection refused, the control plane can’t reach the webhook endpoint. See [No egress route to the required endpoints](#egress-troubleshoot-natgw "#egress-troubleshoot-natgw"), [NACLs blocking webhook or control plane traffic](#egress-troubleshoot-nacl "#egress-troubleshoot-nacl"), and [Security groups preventing access](#egress-troubleshoot-sg "#egress-troubleshoot-sg").
- If the error mentions a DNS or no such host failure, the control plane can’t resolve the endpoint. See [DHCP option set refresh failure](#egress-troubleshoot-dhcp "#egress-troubleshoot-dhcp").

## No egress route to the required endpoints

**Symptoms:**

- Admission webhooks time out.
- OIDC provider discovery fails.
- Cluster creation or update stalls.

**Cause:**

The control plane network interface subnets don’t have a working route to the endpoints the control plane needs to reach. Most commonly, the subnet route table is missing a default route to an egress device. Alternatively, that device is misconfigured. The egress device is usually a NAT gateway. However, it can be a NAT instance, a firewall or proxy appliance, or a transit gateway to a centralized egress VPC.

**Solution:**

1. Identify the subnets your cluster uses for control plane network interfaces:

```
aws eks describe-cluster --name my-cluster \
    --query "cluster.resourcesVpcConfig.subnetIds"
```

2. For each subnet, check the associated route table:

```
aws ec2 describe-route-tables \
    --filters "Name=association.subnet-id,Values=subnet-ExampleID1"
```

3. Verify a route exists for `0.0.0.0/0` (or a route that covers the endpoint) pointing at your egress device. If it is missing, add the route. The following example adds a NAT gateway route; substitute your own egress target (for example, a transit gateway or network interface):

```
aws ec2 create-route \
    --route-table-id rtb-ExampleID \
    --destination-cidr-block 0.0.0.0/0 \
    --nat-gateway-id nat-ExampleID
```

## NACLs blocking webhook or control plane traffic

**Symptoms:**

- Admission webhook calls time out (error: `failed calling webhook`).
- Intermittent failures when creating or modifying Kubernetes resources that use mutating or validating webhooks.

**Cause:**

Network ACLs on the control plane ENI subnets block outbound traffic to webhook endpoints or block the inbound ephemeral port return traffic.

**Solution:**

1. Identify the NACLs associated with your control plane subnets:

```
aws ec2 describe-network-acls \
    --filters "Name=association.subnet-id,Values=subnet-ExampleID1"
```

2. Ensure the following rules exist:

| Direction | Protocol | Port range | Destination/Source          | Action                           |
| --------- | -------- | ---------- | --------------------------- | -------------------------------- |
| Outbound  | TCP      | 443        | 0.0.0.0/0 (or webhook CIDR) | Allow                            |
| Outbound  | TCP      | 10250      | VPC CIDR                    | Allow                            |
| Inbound   | TCP      | 1024–65535 | 0.0.0.0/0                   | Allow (ephemeral return traffic) |

###### Note

NACLs are stateless. You must explicitly allow return traffic on ephemeral ports (1024–65535) in the inbound rules.

These rules cover two different paths. The port 443 rule is for outbound traffic to webhook and OIDC endpoints, which leaves the VPC through your egress device. The port 10250 rule is for the kubelet API, which stays within your VPC between the control plane and your nodes. A missing egress device does not affect port 10250, but a restrictive network ACL can block it.

## Security groups preventing access

**Symptoms:**

- Webhook calls fail.
- Control plane can’t reach the kubelet API on nodes (port 10250).
- `kubectl exec`, `kubectl logs`, or `kubectl port-forward` fail.

**Cause:**

The security group attached to the control plane ENIs (the _cluster security group_) doesn’t allow outbound traffic on required ports.

**Solution:**

1. Identify the cluster security group:

```
aws eks describe-cluster --name my-cluster \
    --query "cluster.resourcesVpcConfig.clusterSecurityGroupId"
```

2. Verify outbound rules allow:

| Protocol | Port  | Destination                                   |
| -------- | ----- | --------------------------------------------- |
| TCP      | 443   | 0.0.0.0/0 (webhook endpoints, OIDC providers) |
| TCP      | 10250 | Node security group or VPC CIDR (kubelet API) |

3. If outbound rules are restrictive, add rules for the required traffic:

```
aws ec2 authorize-security-group-egress \
    --group-id sg-ExampleClusterSG \
    --protocol tcp \
    --port 443 \
    --cidr 0.0.0.0/0
```

###### Note

If you have strict egress requirements and you know the IP ranges of your webhook and OIDC endpoints, you can scope the port 443 rule to those specific CIDRs instead of `0.0.0.0/0`. The port 10250 (kubelet API) rule is VPC-internal; scope it to your node security group or VPC CIDR rather than the internet.

## DHCP option set refresh failure

**Symptoms:**

- DNS resolution fails from the control plane.
- Cluster operations that require DNS lookups (OIDC discovery, webhook resolution) fail.
- Issue appears after VPC DHCP options are changed or after a control plane update.

**Cause:**

The VPC DHCP option set was changed. Alternatively, it doesn’t include `AmazonProvidedDNS` in its domain name servers. It might also lack another resolver that can resolve the names the control plane needs. The control plane automatically detects DHCP option set changes and applies the new DNS settings, usually within one hour. The control plane can do this only when the cluster IAM role grants the required Amazon EC2 read permissions.

**Solution:**

1. Verify the DHCP option set for your VPC:

```
aws ec2 describe-vpcs --vpc-ids vpc-ExampleID \
    --query "Vpcs[0].DhcpOptionsId" \
    --region region-code
```

```
aws ec2 describe-dhcp-options --dhcp-options-ids dopt-ExampleID --region region-code
```

2. Confirm that `domain-name-servers` includes `AmazonProvidedDNS` (the Amazon-provided DNS resolver, which is the base of your VPC IPv4 CIDR plus two), or another resolver that can resolve the names the control plane needs.
3. Confirm the cluster IAM role grants `ec2:DescribeVpcs` and `ec2:DescribeDhcpOptions`. Without these permissions, the control plane can’t read the updated DHCP options and can’t refresh its DNS settings. For more information, see [Amazon EKS cluster IAM role](cluster-iam-role.md "cluster-iam-role.md").
4. After a DHCP options change, allow up to one hour for the control plane to detect and apply the new settings automatically. No cluster update or instance replacement is required. If DNS resolution still fails after an hour and the permissions above are in place, contact AWS Support.

## IPv6 routing issues

**Symptoms:**

- IPv6 clusters can’t reach external OIDC or webhook endpoints.
- Node registration works over IPv4 but IPv6 services fail.

**Cause:**

The subnet route table is missing a `::/0` route to an egress-only internet gateway, or security groups/NACLs don’t allow IPv6 traffic.

**Solution:**

1. Verify an egress-only internet gateway exists and is attached to the VPC:

```
aws ec2 describe-egress-only-internet-gateways \
    --filters "Name=attachment.vpc-id,Values=vpc-ExampleID"
```

2. Check that the route table for the control plane subnets has a `::/0` route:

```
aws ec2 describe-route-tables \
    --filters "Name=association.subnet-id,Values=subnet-ExampleID1" \
    --query "RouteTables[0].Routes[?DestinationIpv6CidrBlock=='::/0']"
```

3. If missing, add the route:

```
aws ec2 create-route \
    --route-table-id rtb-ExampleID \
    --destination-ipv6-cidr-block ::/0 \
    --egress-only-internet-gateway-id eigw-ExampleID
```

4. Ensure NACLs and security groups allow IPv6 outbound on port 443 and inbound ephemeral ports.

## OIDC provider unreachable

**Symptoms:**

- `IAM roles for service accounts` (IRSA) fails — pods can’t assume roles.
- Cluster events show OIDC discovery errors.

**Cause:**

The control plane can’t reach the OIDC provider endpoint (for example, `oidc.eks.region-code.amazonaws.com`) because egress is blocked.

**Solution:**

1. Verify that the egress path and route table allow outbound HTTPS traffic. For troubleshooting steps when the egress route is missing or misconfigured, see [No egress route to the required endpoints](#egress-troubleshoot-natgw "#egress-troubleshoot-natgw").
2. Verify that the cluster security group allows outbound TCP 443 to `0.0.0.0/0` (see [Security groups preventing access](#egress-troubleshoot-sg "#egress-troubleshoot-sg")).

📝 [Edit this page on GitHub](https://github.com/search?q=repo%3Aawsdocs%2Famazon-eks-user-guide+%5B%23control-plane-egress-troubleshooting%5D&type=code "https://github.com/search?q=repo%3Aawsdocs%2Famazon-eks-user-guide+%5B%23control-plane-egress-troubleshooting%5D&type=code")
