# Advanced: Open source adapters

Framework authors can use the file system based deployment specification to develop open
source build adapters customized for their specific frameworks. These adapters will transform
an app's build output into a deployment bundle that conforms to Amplify Hosting’s expected
directory structure. This deployment bundle will include all the necessary files and assets to
host an app, including runtime configuration, such as routing rules.

If you aren't using a framework, you can develop your own solution to generate a build
output that Amplify expects.

###### Topics

- [Using the Amplify Hosting deployment specification to configure build output](ssr-deployment-specification.md "ssr-deployment-specification.md")
- [Deploying an Express server using the deployment manifest](deploy-express-server.md "deploy-express-server.md")
- [Image optimization integration for framework authors](integrate-image-optimization-framework.md "integrate-image-optimization-framework.md")
- [Using open source adapters for any SSR framework](using-framework-adapter.md "using-framework-adapter.md")
