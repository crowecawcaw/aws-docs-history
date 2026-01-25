**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure advanced security settings for nodes

This topic describes how to configure advanced security settings for Amazon EKS Auto Mode nodes using the `advancedSecurity` specification in your Node Class.

## Prerequisites

Before you begin, ensure you have:

- An Amazon EKS Auto Mode cluster. For more information, see [Create a cluster with Amazon EKS Auto Mode](create-auto.md "create-auto.md").
- `kubectl` installed and configured. For more information, see [Set up to use Amazon EKS](setting-up.md "setting-up.md").
- Understanding of Node Class configuration. For more information, see [Create a Node Class for Amazon EKS](create-node-class.md "create-node-class.md").

## Configure advanced security settings

To configure advanced security settings for your nodes, set the `advancedSecurity` fields in your Node Class specification:

```
apiVersion: eks.amazonaws.com/v1
kind: NodeClass
metadata:
  name: security-hardened
spec:
  role: MyNodeRole

  subnetSelectorTerms:
    - tags:
        Name: "private-subnet"

  securityGroupSelectorTerms:
    - tags:
        Name: "eks-cluster-sg"

  advancedSecurity:
    # Enable FIPS-compliant AMIs (US regions only)
    fips: true

    # Configure kernel lockdown mode
    kernelLockdown: "integrity"
```

Apply this configuration:

```
kubectl apply -f nodeclass.yaml
```

Reference this Node Class in your Node Pool configuration. For more information, see [Create a Node Pool for EKS Auto Mode](create-node-pool.md "create-node-pool.md").

## Field descriptions

- `fips` (boolean, optional): When set to `true`, provisions nodes using AMIs with FIPS 140-2 validated cryptographic modules. This setting selects FIPS-compliant AMIs; customers are responsible for managing their compliance requirements. For more information, see [AWS FIPS compliance](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/"). Default: `false`.
- `kernelLockdown` (string, optional): Controls the kernel lockdown security module mode. Accepted values:
  - `integrity`: Blocks methods for overwriting kernel memory or modifying kernel code. Prevents unsigned kernel modules from loading.
  - `none`: Disables kernel lockdown protection.

  For more information, see [Linux kernel lockdown documentation](https://man7.org/linux/man-pages/man7/kernel_lockdown.7.html "https://man7.org/linux/man-pages/man7/kernel_lockdown.7.html").

## Considerations

- FIPS-compliant AMIs are available in AWS US East/West, AWS GovCloud (US), and AWS Canada (Central/West) Regions. For more information, see [AWS FIPS compliance](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
- When using `kernelLockdown: "integrity"`, ensure your workloads don’t require loading unsigned kernel modules or modifying kernel memory.

## Related resources

- [Create a Node Class for Amazon EKS](create-node-class.md "create-node-class.md") - Complete Node Class configuration guide
- [Create a Node Pool for EKS Auto Mode](create-node-pool.md "create-node-pool.md") - Node Pool configuration
