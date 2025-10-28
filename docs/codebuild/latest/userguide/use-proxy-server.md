# Use AWS CodeBuild with a proxy server

You can use AWS CodeBuild with a proxy server to regulate HTTP and HTTPS traffic to and from
the internet. To run CodeBuild with a proxy server, you install a proxy server in a public
subnet and CodeBuild in a private subnet in a VPC.

There are two primary use cases for running CodeBuild in a proxy server:

- It eliminates the use of a NAT gateway or NAT instance in your VPC.
- It lets you specify the URLs that instances in the proxy server can access and
  the URLs to which the proxy server denies access.
  You can use CodeBuild with two types of proxy servers. For both, the proxy server runs in
  a public subnet and CodeBuild runs in a private subnet.

- **Explicit proxy**: If you use an explicit proxy
  server, you must configure `NO_PROXY`, `HTTP_PROXY`, and `HTTPS_PROXY`
  environment variables in CodeBuild at the project level. For more information, see [Change build project settings in AWS CodeBuild](change-project.md "change-project.md") and [Create a build project in AWS CodeBuild](create-project.md "create-project.md").
- **Transparent proxy**: If you use a transparent proxy
  server, no special configuration is required.

###### Topics

- [Set up components required to run
  CodeBuild in a proxy server](use-proxy-server-transparent-components.md "use-proxy-server-transparent-components.md")
- [Run CodeBuild in an explicit proxy
  server](run-codebuild-in-explicit-proxy-server.md "run-codebuild-in-explicit-proxy-server.md")
- [Run CodeBuild in a transparent
  proxy server](run-codebuild-in-transparent-proxy-server.md "run-codebuild-in-transparent-proxy-server.md")
- [Run a package manager and other tools in a
  proxy server](use-proxy-server-tools.md "use-proxy-server-tools.md")
