# Verify an image during in Amazon EKS or Kubernetes clusters

For AWS Signer customers wishing to verify signed container images at the time
of deployment, there are various open-source solutions such as the following.

- [Deis Labs Gatekeeper and
  Ratify](https://ratify.dev/docs/quickstarts/ratify-on-aws "https://ratify.dev/docs/quickstarts/ratify-on-aws") – Use Gatekeeper as the admission controller and
  Ratify configured with an AWS Signer plug-in as a web hook for validating
  signatures.
- [Kyverno](https://github.com/nirmata/kyverno-notation-aws "https://github.com/nirmata/kyverno-notation-aws") – A Kubernetes policy engine configured with a
  AWS Signer plugin for validating signatures.

###### Note

Before verifying container-image signatures, customers must configure the
Notation trust store and trust policy as required by their selected admission
controller.
