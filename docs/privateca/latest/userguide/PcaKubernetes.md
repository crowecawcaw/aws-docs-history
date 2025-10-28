# Secure Kubernetes with AWS Private Certificate Authority

You can use AWS Private Certificate Authority to provide certificates for secure authentication and encryption
over TLS and mTLS. AWS Private CA provides an open source plugin, [AWS Private CA Connector for Kubernetes](https://github.com/cert-manager/aws-privateca-issuer "https://github.com/cert-manager/aws-privateca-issuer"),
(`aws-privateca-issuer`) for the widely adopted [cert-manager](https://cert-manager.io/docs/ "https://cert-manager.io/docs/") add-on to Kubernetes that
requests certificates, distributes them to Kubernetes secrets, and automates certificate
renewal.

The `aws-privateca-issuer` plugin allows you to issue AWS Private CA certificates
through `cert-manager`. You can use the plugin with Amazon Elastic Kubernetes Service (Amazon EKS), a
self-managed Kubernetes cluster on AWS, or in an on-premise Kubernetes cluster. The plugin
works on both x86 and ARM architectures.

AWS Private CA has HSM backed keys that can't be exported. If you have regulatory requirements for
controlling access and auditing your CA operations, you can use AWS Private CA to improve
auditability and to support compliance.

###### Note

If you are running on Amazon EKS, we recommend that you use the `cert-manager`
and `aws-privateca-connector-for-kubernetes` add-ons for a managed
installation experience. For more information, refer to [AWS add-ons](../../../eks/latest/userguide/workloads-add-ons-available-eks.md#add-ons-aws-privateca-connector "../../../eks/latest/userguide/workloads-add-ons-available-eks.md#add-ons-aws-privateca-connector").
