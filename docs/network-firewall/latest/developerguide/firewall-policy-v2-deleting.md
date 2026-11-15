

# Deleting a Next Generation policy in AWS Network Firewall
<a name="firewall-policy-v2-deleting"></a>

To delete a Next Generation policy, first remove it from any firewalls that use it, then delete it.

**To delete a Next Generation policy**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.

1. In the **Firewall policies** page, select the Next Generation policy that you want to delete.

1. Choose **Delete**, and confirm your request.

Your firewall policy is removed from the list in the **Firewall policies** page.

To delete the policy with the AWS CLI, use `delete-firewall-policy-v2`:

```
aws network-firewall delete-firewall-policy-v2 \
--firewall-policy-v2-name example-policy \
--region us-west-2
```

Deletion is asynchronous. The policy moves to the `DELETING` status and is removed shortly after. A policy that's attached to a firewall can't be deleted—associate the firewall with a different policy first.

**Deleting a rule group, TLS inspection configuration, or firewall policy**  
When you delete a rule group, TLS inspection configuration, or a firewall policy, AWS Network Firewall checks to see if it's currently being referenced. A rule group and TLS inspection configuration can be referenced by a firewall policy, and a firewall policy can be referenced by a firewall. If Network Firewall determines that the resource is being referenced, it warns you. Network Firewall is almost always able to determine whether a resource is being referenced. However, in rare cases, it might not be able to do so. If you need to be sure that the resource that you want to delete isn't in use, check all of your firewalls or firewall policies before deleting it. Note that policies that have associations can't be deleted.