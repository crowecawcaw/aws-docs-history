

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: Direct container launch from Amazon ECR Public Gallery on September 29, 2021
<a name="release-2021-09-29-gallery"></a>

Amazon ECR Public added the ability to launch containers directly to AWS App Runner.

**Release date:** September 29, 2021

## Changes
<a name="release-2021-09-29-gallery.changes"></a>

You can now test popular web frameworks and applications hosted on the [Amazon ECR Public Gallery](https://gallery.ecr.aws). When browsing the gallery, look for **Launch with App Runner** on the gallery page for an image. Choose it to open the App Runner console with most details pre-filled. Add the port number for the application and launch a new service.

![Amazon ECR Public Gallery showing a container image page with a Launch with App Runner button](http://docs.aws.amazon.com/apprunner/latest/relnotes/images/ecr-gallery-image-launch.png)


For more information, see [Launch a service directly from Amazon ECR Public](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-image.html#service-source-image.providers.ecrpublic.direct) in the *AWS App Runner Developer Guide*.

If you want to try out this feature, we recommend using one of the following container images.


|  **Image**  |  **Port**  | 
| --- | --- | 
| [hello-app-runner](https://gallery.ecr.aws/aws-containers/hello-app-runner) | 8000 | 
| [nginx](https://gallery.ecr.aws/nginx/nginx) | 80 | 
| [tomcat](https://gallery.ecr.aws/bitnami/tomcat) | *See gallery page for description.* | 