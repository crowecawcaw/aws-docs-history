# RStudio on Amazon SageMaker AI user guide

With RStudio support in Amazon SageMaker AI, you can put your production workflows in place and take
advantage of SageMaker AI features. The following topics show how to launch an RStudio session and
complete key workflows. For information about managing RStudio on SageMaker AI, see [RStudio on Amazon SageMaker AI management](rstudio-manage.md "rstudio-manage.md").

For information about the onboarding steps to create an Amazon SageMaker AI domain with RStudio enabled, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md"). 

For information about the AWS Regions that RStudio on SageMaker AI is supported in, see [Supported Regions and Quotas](regions-quotas.md "regions-quotas.md"). 

###### Topics

- [Collaborate in RStudio](#rstudio-collaborate "#rstudio-collaborate")
- [Base R image](#rstudio-base-image "#rstudio-base-image")
- [RSession application colocation](#rstudio-colocation "#rstudio-colocation")
- [Launch RSessions from the RStudio Launcher](rstudio-launcher.md "rstudio-launcher.md")
- [Suspend your RSessions](rstudio-launcher-suspend.md "rstudio-launcher-suspend.md")
- [Delete your RSessions](rstudio-launcher-delete.md "rstudio-launcher-delete.md")
- [RStudio Connect](rstudio-connect.md "rstudio-connect.md")
- [Amazon SageMaker AI feature integration with RStudio on Amazon SageMaker AI](rstudio-sm-features.md "rstudio-sm-features.md")

## Collaborate in RStudio

To share your RStudio project, you can connect RStudio to your Git repo. For information
on setting this up, see  [Version Control with Git and SVN](https://support.rstudio.com/hc/en-us/articles/200532077-Version-Control-with-Git-and-SVN "https://support.rstudio.com/hc/en-us/articles/200532077-Version-Control-with-Git-and-SVN").

Note: Project sharing and realtime collaboration are not currently supported when using
RStudio on Amazon SageMaker AI. 

## Base R image

When launching your RStudio instance, the Base R image serves as the
basis of your instance. This image extends
the [r-session-complete](https://hub.docker.com/r/rstudio/r-session-complete "https://hub.docker.com/r/rstudio/r-session-complete")
Docker image. 

This Base R image includes the following:

- R v4.0 or higher
- `awscli`, `sagemaker`, and `boto3` Python packages
- [Reticulate](https://rstudio.github.io/reticulate/ "https://rstudio.github.io/reticulate/") package for R SDK
  integration

## RSession application colocation

Users can create multiple RSession applications on the same instance. Each instance type
supports up to four colocated RSession applications. This applies to each user independently.
For example, if two users create applications, then SageMaker AI allocates different underlying
instances to each user. Each of these instances would support 4 RSession applications.

Customers only pay for the instance type used regardless of how many Rsession applications
are running on the instance. If a user creates an RSession with a different associated
instance type, then a new underlying instance is created.
