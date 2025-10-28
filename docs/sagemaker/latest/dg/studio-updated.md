# Amazon SageMaker Studio

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio
experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

Amazon SageMaker Studio is the latest web-based experience for running ML workflows. Studio
offers a suite of integrated development environments (IDEs). These include Code Editor, based on Code-OSS, Visual Studio Code - Open Source, a new
JupyterLab application, RStudio, and Amazon SageMaker Studio Classic. For more information, see [Applications supported in Amazon SageMaker Studio](studio-updated-apps.md "studio-updated-apps.md").

The new web-based UI in Studio is faster and provides access to all SageMaker AI resources,
including jobs and endpoints, in one interface. ML practitioners can also choose their
preferred IDE to accelerate ML development. A data scientist can use JupyterLab to
explore data and tune models. In addition, a machine learning operations (MLOps) engineer
can use Code Editor with the pipelines tool in Studio to deploy and monitor models in
production.

The previous Studio experience is still being supported as Amazon SageMaker Studio Classic.
Studio Classic is the default experience for existing customers, and is available as an
application in Studio. For more information about Studio Classic, see [Amazon SageMaker Studio Classic](studio.md "studio.md"). For information about how to migrate from
Studio Classic to Studio, see [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md "studio-updated-migrate.md").

Studio offers the following benefits:

- A new JupyterLab application that has a faster start-up time and is more
  reliable than the existing Studio Classic application. For more information, see [SageMaker JupyterLab](studio-updated-jl.md "studio-updated-jl.md").
- A suite of IDEs that open in a separate tab, including the new Code Editor, based on Code-OSS, Visual Studio Code - Open Source
  application. Users can interact with supported IDEs in a full screen experience. For
  more information, see [Applications supported in Amazon SageMaker Studio](studio-updated-apps.md "studio-updated-apps.md").
- Access to all of your SageMaker AI resources in one place. Studio displays running
  instances across all of your applications.
- Access to all training jobs in a single view, regardless of whether they were
  scheduled from notebooks or initiated from Amazon SageMaker JumpStart.
- Simplified model deployment workflows and endpoint management and monitoring
  directly from Studio. You don't need to access the SageMaker AI console.
- Automatic creation of all configured applications when you onboard to a domain.
  For information about onboarding to a domain, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
- An improved JumpStart experience where you can discover, import, register,
  fine tune, and deploy a foundation model. For more information, see [SageMaker JumpStart pretrained models](studio-jumpstart.md "studio-jumpstart.md").

###### Topics

- [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md")
- [Amazon SageMaker Studio UI overview](studio-updated-ui.md "studio-updated-ui.md")
- [Amazon EFS auto-mounting in Studio](studio-updated-automount.md "studio-updated-automount.md")
- [Idle shutdown](studio-updated-idle-shutdown.md "studio-updated-idle-shutdown.md")
- [Applications supported in Amazon SageMaker Studio](studio-updated-apps.md "studio-updated-apps.md")
- [Connect your local Visual Studio Code to SageMaker spaces with remote
  access](remote-access.md "remote-access.md")
- [Bring your own image (BYOI)](studio-updated-byoi.md "studio-updated-byoi.md")
- [Lifecycle configurations within
  Amazon SageMaker Studio](studio-lifecycle-configurations.md "studio-lifecycle-configurations.md")
- [Amazon SageMaker Studio spaces](studio-updated-spaces.md "studio-updated-spaces.md")
- [Trusted identity propagation with
  Studio](trustedidentitypropagation.md "trustedidentitypropagation.md")
- [Perform common UI tasks](studio-updated-common.md "studio-updated-common.md")
- [NVMe stores with Amazon SageMaker Studio](studio-updated-nvme.md "studio-updated-nvme.md")
- [Local mode support in Amazon SageMaker Studio](studio-updated-local.md "studio-updated-local.md")
- [View your Studio running instances,
  applications, and spaces](studio-updated-running.md "studio-updated-running.md")
- [Stop and delete your Studio running
  applications and spaces](studio-updated-running-stop.md "studio-updated-running-stop.md")
- [SageMaker Studio image support policy](sagemaker-distribution.md "sagemaker-distribution.md")
- [Amazon SageMaker Studio pricing](studio-updated-cost.md "studio-updated-cost.md")
- [Troubleshooting](studio-updated-troubleshooting.md "studio-updated-troubleshooting.md")
- [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md "studio-updated-migrate.md")
- [Amazon SageMaker Studio Classic](studio.md "studio.md")
