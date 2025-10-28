This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Installation

1. Install [kubectl](https://kubernetes.io/docs/tasks/tools/ "https://kubernetes.io/docs/tasks/tools/") and [kots CLI](https://docs.replicated.com/reference/kots-cli-getting-started "https://docs.replicated.com/reference/kots-cli-getting-started").
2. Connect to the Kubernetes cluster.
3. Obtain Wickr Enterprise license file from Wickr Support.
4. Install Wickr Enterprise using the following command.

```
kubectl kots install wickr-enterprise-ha \
   --license-file ./license.yaml \
   --namespace wickr
```

###### Note

license.yaml represents your provided license file.
After initial installation the KOTS Admin Console will provide cluster level management and
configuration options.

## KOTS Admin Console

This interface is used for managing the deployed version of Wickr Enterprise. You can see
the status of the installation, modify configurations, or perform upgrades of Wickr
Enterprise. The KOTS Admin Console is accessible only through a Kubernetes port forward, which
can be opened using the following command:

```
kubectl kots admin-console -n wickr
```
