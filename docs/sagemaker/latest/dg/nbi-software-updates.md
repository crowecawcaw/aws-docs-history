# Notebook Instance Software Updates

Amazon SageMaker AI periodically tests and releases software that is installed on notebook
instances. This includes:

- Kernel updates
- Security patches
- AWS SDK updates
- [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable") updates
- Open source software updates
  To ensure that you have the most recent software updates, stop and restart your
  notebook instance, either in the SageMaker AI console or by calling [`StopNotebookInstance`](../APIReference/API_StopNotebookInstance.md "../APIReference/API_StopNotebookInstance.md").

You can also manually update software installed on your notebook instance while it
is running by using update commands in a terminal or in a notebook.

###### Note

Updating kernels and some packages might depend on whether root access is
enabled for the notebook instance. For more information, see [Control root access to a SageMaker notebook instance](nbi-root-access.md "nbi-root-access.md").

You can check the [Personal Health Dashboard](https://aws.amazon.com/premiumsupport/technology/personal-health-dashboard/ "https://aws.amazon.com/premiumsupport/technology/personal-health-dashboard/") or the security bulletin at [Security Bulletins](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/")
for updates.
