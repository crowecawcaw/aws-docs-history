**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Validate container image signatures during deployment

If you use [AWS Signer](../../../signer/latest/developerguide/Welcome.md "../../../signer/latest/developerguide/Welcome.md") and want to verify signed container images at the time of deployment, you can use one of the following solutions:

- [Gatekeeper and Ratify](https://ratify.dev/docs/1.0/quickstarts/ratify-on-aws "https://ratify.dev/docs/1.0/quickstarts/ratify-on-aws") – Use Gatekeeper as the admission controller and Ratify configured with an AWS Signer plugin as a web hook for validating signatures.
- [Kyverno](https://github.com/nirmata/kyverno-notation-aws "https://github.com/nirmata/kyverno-notation-aws") – A Kubernetes policy engine configured with an AWS Signer plugin for validating signatures.

###### Note

Before verifying container image signatures, configure the [Notation](https://github.com/notaryproject/notation#readme "https://github.com/notaryproject/notation#readme") trust store and trust policy, as required by your selected admission controller.
