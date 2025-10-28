# Announcing the End of Support

of the Original Version of SageMaker AI
Operators for Kubernetes

This page announces the end of support for the original version of [SageMaker AI Operators for
Kubernetes](https://github.com/aws/amazon-sagemaker-operator-for-k8s "https://github.com/aws/amazon-sagemaker-operator-for-k8s") and provides answers to frequently asked questions as well as migration
information about the [ACK service controller for Amazon SageMaker AI](https://github.com/aws-controllers-k8s/sagemaker-controller "https://github.com/aws-controllers-k8s/sagemaker-controller"), a new generation of fully supported SageMaker AI
Operators for Kubernetes. For general information about the new SageMaker AI Operators for Kubernetes,
see [Latest SageMaker AI Operators for Kubernetes](kubernetes-sagemaker-operators-ack.md "kubernetes-sagemaker-operators-ack.md").

## End of Support Frequently Asked

Questions

###### Contents

- [Why are we ending
  support for the original version of SageMaker AI Operators for Kubernetes?](#kubernetes-sagemaker-operators-eos-faq-why "#kubernetes-sagemaker-operators-eos-faq-why")
- [Where can I find more
  information about the new SageMaker AI Operators for Kubernetes and ACK?](#kubernetes-sagemaker-operators-eos-faq-more "#kubernetes-sagemaker-operators-eos-faq-more")
- [What does end of support
  (EOS) mean?](#kubernetes-sagemaker-operators-eos-faq-definition "#kubernetes-sagemaker-operators-eos-faq-definition")
- [How can I migrate my workload
  to the new SageMaker AI Operators for Kubernetes for training and inference?](#kubernetes-sagemaker-operators-eos-faq-how "#kubernetes-sagemaker-operators-eos-faq-how")
- [Which version of ACK should
  I migrate to?](#kubernetes-sagemaker-operators-eos-faq-version "#kubernetes-sagemaker-operators-eos-faq-version")
- [Are the initial SageMaker AI
  Operators for Kubernetes and the new Operators (ACK service controller for Amazon SageMaker AI)
  functionally equivalent?](#kubernetes-sagemaker-operators-eos-faq-parity "#kubernetes-sagemaker-operators-eos-faq-parity")

### Why are we ending

support for the original version of SageMaker AI Operators for Kubernetes?

Users can now take advantage of the [ACK service controller
for Amazon SageMaker AI](https://github.com/aws-controllers-k8s/sagemaker-controller "https://github.com/aws-controllers-k8s/sagemaker-controller"). The ACK service controller is a new generation of SageMaker AI Operators for
Kubernetes based on [AWS
Controllers for Kubernetes](https://aws-controllers-k8s.github.io/community/ "https://aws-controllers-k8s.github.io/community/") (ACK), a community-driven project optimized for
production, standardizing the way to expose AWS services via a Kubernetes operator. We are
therefore announcing the end of support (EOS) for the original version (not ACK-based) of
[SageMaker AI Operators for
Kubernetes](https://github.com/aws/amazon-sagemaker-operator-for-k8s "https://github.com/aws/amazon-sagemaker-operator-for-k8s"). The support ends on **Feb 15, 2023**
along with [Amazon Elastic Kubernetes Service
Kubernetes 1.21](../../../eks/latest/userguide/kubernetes-versions.md#kubernetes-release-calendar "../../../eks/latest/userguide/kubernetes-versions.md#kubernetes-release-calendar").

For more information on ACK, see [ACK
history and tenets](https://aws-controllers-k8s.github.io/community/docs/community/background/ "https://aws-controllers-k8s.github.io/community/docs/community/background/").

### Where can I find more

information about the new SageMaker AI Operators for Kubernetes and ACK?

- For more information about the new SageMaker AI Operators for Kubernetes, see the [ACK service
  controller for Amazon SageMaker AI](https://github.com/aws-controllers-k8s/sagemaker-controller "https://github.com/aws-controllers-k8s/sagemaker-controller") GitHub repository or read [AWS
  Controllers for Kubernetes Documentation](https://aws-controllers-k8s.github.io/community/docs/community/overview/ "https://aws-controllers-k8s.github.io/community/docs/community/overview/").
- For a tutorial on how to train a machine learning model with the ACK service
  controller for Amazon SageMaker AI using Amazon EKS, see this [SageMaker AI example](https://aws-controllers-k8s.github.io/community/docs/tutorials/sagemaker-example/ "https://aws-controllers-k8s.github.io/community/docs/tutorials/sagemaker-example/").

For an autoscaling example, see [Scale SageMaker AI Workloads with Application Auto Scaling](https://aws-controllers-k8s.github.io/community/docs/tutorials/autoscaling-example/ "https://aws-controllers-k8s.github.io/community/docs/tutorials/autoscaling-example/").

- For information on AWS Controller for Kubernetes (ACK), see the [AWS Controllers for
  Kubernetes](https://aws-controllers-k8s.github.io/community/ "https://aws-controllers-k8s.github.io/community/") (ACK) documentation.
- For a list of supported SageMaker AI resources, see [ACK API
  Reference](https://aws-controllers-k8s.github.io/community/reference/ "https://aws-controllers-k8s.github.io/community/reference/").

### What does end of support

(EOS) mean?

While users can continue to use their current operators, we are no longer developing new
features for the operators, nor will we release any patches or security updates for any
issues found. `v1.2.2` is the last release of [SageMaker AI Operators
for Kubernetes](https://github.com/aws/amazon-sagemaker-operator-for-k8s/tree/master "https://github.com/aws/amazon-sagemaker-operator-for-k8s/tree/master"). Users should migrate their workloads to use the [ACK service controller
for Amazon SageMaker AI](https://github.com/aws-controllers-k8s/sagemaker-controller "https://github.com/aws-controllers-k8s/sagemaker-controller").

### How can I migrate my workload

to the new SageMaker AI Operators for Kubernetes for training and inference?

For information about migrating resources from the old to the new SageMaker AI Operators for
Kubernetes, follow [Migrate resources to the latest
Operators](kubernetes-sagemaker-operators-migrate.md "kubernetes-sagemaker-operators-migrate.md").

### Which version of ACK should

I migrate to?

Users should migrate to the most recent
released version of the [ACK service controller for Amazon SageMaker AI](https://github.com/aws-controllers-k8s/sagemaker-controller/tags "https://github.com/aws-controllers-k8s/sagemaker-controller/tags").

### Are the initial SageMaker AI

Operators for Kubernetes and the new Operators (ACK service controller for Amazon SageMaker AI)
functionally equivalent?

Yes, they are at feature parity.

A few highlights of the main notable differences between the two versions
include:

- The Custom Resources Definitions (CRD) used by the ACK-based SageMaker AI Operators for
  Kubernetes follow the AWS API definition making it incompatible with the custom
  resources specifications from the SageMaker AI Operators for Kubernetes in its original version.
  Refer to the [CRDs](https://github.com/aws-controllers-k8s/sagemaker-controller/tree/main/helm/crds "https://github.com/aws-controllers-k8s/sagemaker-controller/tree/main/helm/crds") in the new controller or use the migration guide to adopt the resources
  and use the new controller.
- The `Hosting Autoscaling` policy is no longer part of the new SageMaker AI
  Operators for Kubernetes and has been migrated to the [Application autoscaling](https://github.com/aws-controllers-k8s/applicationautoscaling-controller "https://github.com/aws-controllers-k8s/applicationautoscaling-controller") ACK controller. To learn how to use the application
  autoscaling controller to configure autoscaling on SageMaker AI Endpoints, follow this [autoscaling example](https://aws-controllers-k8s.github.io/community/docs/tutorials/autoscaling-example/ "https://aws-controllers-k8s.github.io/community/docs/tutorials/autoscaling-example/").
- The `HostingDeployment` resource was used to create Models, Endpoint
  Configurations, and Endpoints in one CRD. The new SageMaker AI Operators for Kubernetes has a
  separate CRD for each of these resources.
