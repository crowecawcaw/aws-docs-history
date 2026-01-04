# Instance deployment workflow

###### Note

The information in this section doesn't apply to the _ECS running on Amazon Linux 2 and Amazon Linux 2023_ platform branches. For more
information, see the next section [Instance deployment workflow for ECS running on Amazon Linux 2 and later](platforms-linux-extend.workflow.md "platforms-linux-extend.workflow.md").

With many ways to extend your environment's platform, it's useful to know what happens whenever Elastic Beanstalk provisions an instance or runs a deployment to
an instance. The following diagram shows this entire deployment workflow. It depicts the different phases in a deployment and the steps that Elastic Beanstalk takes
in each phase.

###### Notes

- The diagram doesn't represent the complete set of steps that Elastic Beanstalk takes on environment instances during deployment. We provide this diagram for
  illustration, to provide you with the order and context for the execution of your customizations.
- For simplicity, the diagram mentions only the `.platform/hooks/*` hook subdirectories (for application deployments), and not
  the `.platform/confighooks/*` hook subdirectories (for configuration deployments). Hooks in the latter subdirectories run during
  exactly the same steps as hooks in corresponding subdirectories shown in the diagram.

![Workflow for extensions execution order on an environment instance running on a Amazon Linux-based platform.](images/platforms-linux-extend-order.png)
The following list details the deployment phases and steps.

1. **Initial steps**

Elastic Beanstalk downloads and extracts your application. After each one of these steps, Elastic Beanstalk runs one of the extensibility steps.

    1. Runs commands found in the [commands:](customize-containers-ec2.md#linux-commands "customize-containers-ec2.md#linux-commands") section of any configuration file.
    2. Runs any executable files found in the `.platform/hooks/prebuild` directory of your source bundle
     (`.platform/confighooks/prebuild` for a configuration deployment).

2. **Configure**

Elastic Beanstalk configures your application and the proxy server.

    1. Runs the commands found in the `Buildfile` in your source bundle.
    2. Copies your custom proxy configuration files, if you have any in the `.platform/nginx` directory of your source bundle, to
     their runtime location.
    3. Runs commands found in the [container\_commands:](customize-containers-ec2.md#linux-container-commands "customize-containers-ec2.md#linux-container-commands") section of any configuration file.
    4. Runs any executable files found in the `.platform/hooks/predeploy` directory of your source bundle
     (`.platform/confighooks/predeploy` for a configuration deployment).

3. **Deploy**

Elastic Beanstalk deploys and runs your application and the proxy server.

    1. Runs the command found in the `Procfile` file in your source bundle.
    2. Runs or reruns the proxy server with your custom proxy configuration files, if you have any.
    3. Runs any executable files found in the `.platform/hooks/postdeploy` directory of your source bundle
     (`.platform/confighooks/postdeploy` for a configuration deployment).
