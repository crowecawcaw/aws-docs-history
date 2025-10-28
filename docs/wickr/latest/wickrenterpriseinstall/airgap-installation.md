This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Airgap installation

Wickr Enterprise and KOTS both support deployment into a fully airgapped Kubernetes
cluster. You must provide access to a Private Docker Image Registry that is reachable from the
airgapped Kubernetes cluster. The Private Docker Image Registry supplied to KOTS must be secured
with username/password authentication to function correctly for this purpose. KOTS will utilize
the Private Docker Image Registry to host all of the Wickr Enterprise images.

- Wickr Enterprise license.yaml with airgap enabled (Contact Wickr Sales or Customer
  Support Team)
- Wickr Enterprise wickr.airgap archive bundle (Contact Wickr Sales or Customer
  Support Team)
- Access to a [Private Docker Image Registry](https://docs.replicated.com/enterprise/image-registry-settings "https://docs.replicated.com/enterprise/image-registry-settings") .
- Access to a [Kubernetes cluster](https://docs.replicated.com/enterprise/installing-general-requirements#minimum-system-requirements "https://docs.replicated.com/enterprise/installing-general-requirements#minimum-system-requirements") deployed in the airgap environment.
- [Kubectl](https://kubernetes.io/docs/tasks/tools/ "https://kubernetes.io/docs/tasks/tools/") installed.
- [KOTS
  CLI](https://docs.replicated.com/reference/kots-cli-getting-started "https://docs.replicated.com/reference/kots-cli-getting-started") installed.
- [kotsadm.tar.gz](https://github.com/replicatedhq/kots/releases "https://github.com/replicatedhq/kots/releases")
  downloaded.
  Run the following commands to deploy KOTS and Wickr Enterprise on your airgapped
  kubernetes cluster. These commands upload the KOTS admin images and the the Wickr Enterprise
  images to the Private Docker Image Registry. After the commands finish you will be prompted to
  access the KOTS Admin Console to complete the Wickr Enterprise installation as above.

```
kubectl kots admin-console push-images \
  ~/kotsadm.tar.gz $PRIVATE_REGISTRY_HOST \
  --registry-username $PRIVATE_REGISTRY_USER \
  --registry-password $PRIVATE_REGISTRY_PASSWORD

kubectl kots install wickr \
  --license-file ~/YOUR_LICENSE.yaml \
  --airgap-bundle ~/wickr.airgap \
  --kotsadm-registry $PRIVATE_REGISTRY_HOST \
  --registry-username $PRIVATE_REGISTRY_USER \
  --registry-password $PRIVATE_REGISTRY_PASSWORD
```

## Mobile notification for airgap installs

Additional networking allow lists are necessary for push notifications from server backend
to mobile clients. This requirement is due to how Apple iOS and Google Android implement this
feature for offline and background devices. Refer to the documentation for these services and
allow list the specified IP addresses and ports.

- [iOS](https://support.apple.com/en-us/102266 "https://support.apple.com/en-us/102266")
- [Android](https://firebase.google.com/docs/cloud-messaging/network-configuration "https://firebase.google.com/docs/cloud-messaging/network-configuration")
