**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Remove Pod Identity associations from an Amazon EKS add-on

Remove the Pod Identity associations from an Amazon EKS add-on.

1. Determine:
   - `cluster-name` - The name of the EKS cluster to install the add-on onto.
   - `addon-name` - The name of the Amazon EKS add-on to install.

2. Update the addon to specify an empty array of pod identity associations.

```
aws eks update-addon --cluster-name <cluster-name> \
--addon-name <addon-name> \
--pod-identity-associations "[]"
```
