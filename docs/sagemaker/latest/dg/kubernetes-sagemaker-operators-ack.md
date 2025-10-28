# Latest SageMaker AI Operators for Kubernetes

This section is based on the latest version of SageMaker AI Operators for Kubernetes using AWS
Controllers for Kubernetes (ACK).

###### Important

If you are currently using version `v1.2.2`
or below of [SageMaker Operators for Kubernetes](https://github.com/aws/amazon-sagemaker-operator-for-k8s/tree/master "https://github.com/aws/amazon-sagemaker-operator-for-k8s/tree/master"), we recommend migrating your resources to the
[ACK service controller for Amazon SageMaker](https://github.com/aws-controllers-k8s/sagemaker-controller "https://github.com/aws-controllers-k8s/sagemaker-controller").
The ACK service controller is a new generation of SageMaker Operators for Kubernetes based on
[AWS Controllers for Kubernetes (ACK)](https://aws-controllers-k8s.github.io/community/ "https://aws-controllers-k8s.github.io/community/").

For information on the migration steps, see [Migrate resources to the latest
Operators](kubernetes-sagemaker-operators-migrate.md "kubernetes-sagemaker-operators-migrate.md").

For answers to frequently asked
questions on the end of support of the original version of SageMaker Operators for
Kubernetes, see [Announcing the End of Support
of the Original Version of SageMaker AI
Operators for Kubernetes](kubernetes-sagemaker-operators-eos-announcement.md "kubernetes-sagemaker-operators-eos-announcement.md")

The latest version of [SageMaker AI Operators
for Kubernetes](https://github.com/aws-controllers-k8s/sagemaker-controller "https://github.com/aws-controllers-k8s/sagemaker-controller") is based on [AWS Controllers for Kubernetes
(ACK)](https://aws-controllers-k8s.github.io/community/ "https://aws-controllers-k8s.github.io/community/ "), a framework for building Kubernetes custom controllers where each controller
communicates with an AWS service API. These controllers allow Kubernetes users to provision
AWS resources like databases or message queues using the Kubernetes API.

Use the following steps to install and use ACK to train, tune, and deploy
machine learning models with Amazon SageMaker AI.

###### Contents

- [Install SageMaker AI Operators for
  Kubernetes](#kubernetes-sagemaker-operators-ack-install "#kubernetes-sagemaker-operators-ack-install")
- [Use SageMaker AI Operators for
  Kubernetes](#kubernetes-sagemaker-operators-ack-use "#kubernetes-sagemaker-operators-ack-use")
- [Reference](#kubernetes-sagemaker-operators-ack-reference "#kubernetes-sagemaker-operators-ack-reference")

## Install SageMaker AI Operators for

Kubernetes

To set up the latest available version of SageMaker AI Operators for Kubernetes, see the
_Setup_ section in [Machine Learning with the ACK SageMaker AI Controller](https://aws-controllers-k8s.github.io/community/docs/tutorials/sagemaker-example/#setup "https://aws-controllers-k8s.github.io/community/docs/tutorials/sagemaker-example/#setup").

## Use SageMaker AI Operators for

Kubernetes

For a tutorial on how to train a machine learning model with the ACK service controller
for Amazon SageMaker AI using Amazon EKS, see [Machine Learning with the ACK SageMaker AI Controller](https://aws-controllers-k8s.github.io/community/docs/tutorials/sagemaker-example/ "https://aws-controllers-k8s.github.io/community/docs/tutorials/sagemaker-example/").

For an autoscaling example, see [Scale SageMaker AI Workloads with Application Auto Scaling](https://aws-controllers-k8s.github.io/community/docs/tutorials/autoscaling-example/ "https://aws-controllers-k8s.github.io/community/docs/tutorials/autoscaling-example/")

## Reference

See also the [ACK service controller for Amazon SageMaker AI GitHub repository](https://github.com/aws-controllers-k8s/sagemaker-controller "https://github.com/aws-controllers-k8s/sagemaker-controller") or read [AWS
Controllers for Kubernetes Documentation](https://aws-controllers-k8s.github.io/community/docs/community/overview/ "https://aws-controllers-k8s.github.io/community/docs/community/overview/").
