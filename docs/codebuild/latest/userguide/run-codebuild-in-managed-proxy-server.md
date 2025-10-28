# Use AWS CodeBuild with a managed proxy server

To run AWS CodeBuild reserved capacity fleets in a managed proxy server, you must configure the proxy server to
allow or deny traffic to and from external sites using proxy rules. Note that running reserved capacity fleets
in a managed proxy server is not supported for VPC, Windows, or MacOS.

###### Important

There are additional costs based on the duration that a proxy configuration is present in the fleet.
For more information, see [https://aws.amazon.com/codebuild/pricing/](https://aws.amazon.com/codebuild/pricing/ "https://aws.amazon.com/codebuild/pricing/").

###### Topics

- [Configure a managed proxy
  configuration for reserved capacity fleets](#run-codebuild-in-managed-proxy-server-configure "#run-codebuild-in-managed-proxy-server-configure")
- [Run a CodeBuild
  reserved capacity fleet](#use-managed-server-run-acb-fleet "#use-managed-server-run-acb-fleet")

## Configure a managed proxy

configuration for reserved capacity fleets

To configure a managed proxy server for your reserved capacity fleet, you must
enable this feature when creating your fleet in your console or using the AWS CLI. There
are several properties which you need to define:

**Define proxy configurations - optional**

Proxy configurations that apply network access control to your reserved capacity instances.

**Default behavior**

Defines the behavior of outgoing traffic.

**Allow**

Allows outgoing traffic to all destinations by default.

**Deny**

Denies outgoing traffic to all destinations by default.

**Proxy rules**

Specifies destination domains to restrict network access control to.

To define proxy configurations in your console, see [Create a reserved capacity fleet](fleets.md#fleets.how-to "fleets.md#fleets.how-to") for instructions. To define proxy configurations
using the AWS CLI, you can do so by modifying the following JSON syntax and saving your results:

```
"proxyConfiguration": {
    "defaultBehavior": "ALLOW_ALL" | "DENY_ALL",
    "orderedProxyRules": [
        {
            "type": "DOMAIN" | "IP",
            "effect": "ALLOW" | "DENY",
            "entities": [
                "`destination`"
            ]
        }
    ]
}
```

Your JSON file may look similar to the following:

```
"proxyConfiguration": {
    "defaultBehavior": "DENY_ALL",
    "orderedProxyRules": [
        {
            "type": "DOMAIN",
            "effect": "ALLOW",
            "entities": [
                "github.com"
            ]
        }
    ]
}
```

## Run a CodeBuild

reserved capacity fleet

When running AWS CodeBuild reserved capacity fleets with your managed proxy
server, CodeBuild will automatically set its `HTTP_PROXY`
and `HTTPS_PROXY` environment variables with the managed proxy addresses. If
your dependency software has its own configuration and does not adhere to the environment variables,
you can refer to these values and update your software configuration in your build commands to properly route
your build traffic through the managed proxy.
For more information, see [Create a build project in AWS CodeBuild](create-project.md "create-project.md") and [Change build project settings in AWS CodeBuild](change-project.md "change-project.md").
