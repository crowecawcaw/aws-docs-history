# Serving static files

To improve performance, you can configure the proxy server to serve static files (for
example, HTML or images) from a set of directories inside your web application. When the proxy
server receives a request for a file under the specified path, it serves the file directly
instead of routing the request to your application.

Elastic Beanstalk supports configuring the proxy to serve static files on most platform branches based
on Amazon Linux 2. The one exception is Docker.

###### Note

On the Python and Ruby platforms, Elastic Beanstalk configures some static file folders by default.
For details, see the static file configuration sections for [Python](create-deploy-python-container.md#python-platform-staticfiles "create-deploy-python-container.md#python-platform-staticfiles") and [Ruby](create_deploy_Ruby.md#create_deploy_Ruby.container.console.staticfiles "create_deploy_Ruby.md#create_deploy_Ruby.container.console.staticfiles"). You can configure
additional folders as explained on this page.

## Configure static files using the

console

###### To configure the proxy server to serve static files

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.
5. Scroll to the **Platform software** section and locate
   the **Static files** group.
   1. To add a static file mapping, select **Add static
      files**. In the extra row that appears you'll enter a _path_ for serving static files and the _directory_ that contains the static files to serve.
      - In the **Path** field, start the path name with a
        slash (`/`) (for example, "_/images_").
      - In the **Directory** field, specify a directory
        name located in the root of your application's source code. Don't start it with a
        slash (for example, "_static/image-files_").

   ###### Note

   If you aren't seeing the **Static files** section, you have to
   add at least one mapping by using a [configuration
   file](ebextensions.md "ebextensions.md"). For details, see [Configure static files using
   configuration options](#environment-cfg-staticfiles.namespace "#environment-cfg-staticfiles.namespace") on this page. 2. To remove a mapping, select **Remove**.

6. To save the changes choose **Apply** at the bottom of the page.

## Configure static files using

configuration options

You can use a [configuration file](ebextensions.md "ebextensions.md") to configure static
file paths and directory locations using configuration options. You can add a configuration
file to your application's source bundle and deploy it during environment creation or a later
deployment.

If your environment uses a platform branch based on Amazon Linux 2, use the `aws:elasticbeanstalk:environment:proxy:staticfiles` namespace.

The following example configuration file tells the proxy server to serve files in the
`statichtml` folder at the path `/html`, and files in the
`staticimages` folder at the path `/images`.

###### Example.ebextensions/static-files.config

```
option_settings:
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /html: statichtml
    /images: staticimages
```

If your Elastic Beanstalk environment uses an Amazon Linux AMI platform version (preceding Amazon Linux 2), read the
following additional information:

On Amazon Linux AMI platform branches, static file configuration namespaces vary by platform.
For details, see one of the following pages:

- [Go configuration namespace](go-environment.md#go-namespaces "go-environment.md#go-namespaces")
- [Java SE configuration namespace](java-se-platform.md#java-se-namespaces "java-se-platform.md#java-se-namespaces")
- [Tomcat configuration namespaces](java-tomcat-platform.md#java-tomcat-namespaces "java-tomcat-platform.md#java-tomcat-namespaces")
- [Node.js configuration namespace](create_deploy_nodejs.md#nodejs-namespaces "create_deploy_nodejs.md#nodejs-namespaces")
- [Python configuration namespaces](create-deploy-python-container.md#python-namespaces "create-deploy-python-container.md#python-namespaces")
