

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# Installation
<a name="installation"></a>

1. Install [kubectl](https://kubernetes.io/docs/tasks/tools/) and [kots CLI](https://docs.replicated.com/reference/kots-cli-getting-started).

1. Connect to the Kubernetes cluster.

1. Obtain Wickr Enterprise license file from Wickr Support.

1. Install Wickr Enterprise using the following command.

   ```
   kubectl kots install wickr-enterprise-ha \ 
      --license-file ./license.yaml \
      --namespace wickr
   ```
**Note**  
license.yaml represents your provided license file.

After initial installation the KOTS Admin Console will provide cluster level management and configuration options.

## KOTS Admin Console
<a name="kots-admin-console"></a>

This interface is used for managing the deployed version of Wickr Enterprise. You can see the status of the installation, modify configurations, or perform upgrades of Wickr Enterprise. The KOTS Admin Console is accessible only through a Kubernetes port forward, which can be opened using the following command: 

```
kubectl kots admin-console -n wickr
```