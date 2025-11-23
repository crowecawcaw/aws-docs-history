# Clone an Elastic Beanstalk environment

You can use an existing Elastic Beanstalk environment as the basis for a new environment by cloning the
existing environment. For example, you might want to create a clone so that you can use a newer
version of the platform branch used by the original environment's platform. Elastic Beanstalk configures the
clone with the environment settings used by the original environment. By cloning an existing
environment instead of creating a new environment, you don't have to manually configure option
settings, environment variables, and other settings that you made with the Elastic Beanstalk service. Elastic Beanstalk
also creates a copy of any AWS resource associated with the original environment.

It's important to be aware of the following situations:

- During the cloning process, Elastic Beanstalk doesn't copy data from Amazon RDS to the clone.
- Elastic Beanstalk doesn't include any unmanaged changes to resources in the clone. Changes to AWS
  resources that you make using tools other than the Elastic Beanstalk console, command-line tools, or API
  are considered unmanaged changes.
- The security groups for ingress are considered unmanaged changes. Cloned Elastic Beanstalk
  environments do not carry over the security groups for ingress, leaving the environment open
  to all internet traffic. You’ll need to reestablish ingress security groups for the cloned
  environment.
  You can only clone an environment to a different platform version of the same platform
  branch. A different platform branch isn't guaranteed to be compatible. To use a different
  platform branch, you have to manually create a new environment, deploy your application code,
  and make any necessary changes in code and options to ensure your application works correctly on
  the new platform branch.

## AWS management console

###### Important

Cloned Elastic Beanstalk environments do not carry over the security groups for ingress, leaving the
environment open to all internet traffic. You’ll need to reestablish ingress security groups for
the cloned environment.

You can see resources that may not be cloned by checking the drift status of your
environment configuration. For more information, see [Detect drift on an entire
CloudFormation stack](../../../AWSCloudFormation/latest/UserGuide/detect-drift-stack.md "../../../AWSCloudFormation/latest/UserGuide/detect-drift-stack.md") in the _AWS CloudFormation User Guide_.

###### To clone an environment

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. On the environment overview page, choose **Actions**.
4. Choose **Clone environment**.
5. On the **Clone environment** page, review the information in the
   **Original Environment** section to verify that you chose the
   environment from which you want to create a clone.
6. In the **New Environment** section, you can optionally change the
   **Environment name**, **Environment URL**,
   **Description**, **Platform version**, and
   **Service role** values that Elastic Beanstalk automatically set based on the
   original environment.

###### Note

If the platform version used in the original environment isn't the one recommended
for use in the platform branch, you are warned that a different platform version is
recommended. Choose **Platform version**, and you can see the
recommended platform version on the list—for example, **3.3.2
(Recommended)**. 7. When you are ready, choose **Clone**.

## Elastic Beanstalk command line interface (EB

CLI)

###### Important

Cloned Elastic Beanstalk environments do not carry over the security groups for ingress, leaving the
environment open to all internet traffic. You’ll need to reestablish ingress security groups for
the cloned environment.

You can see resources that may not be cloned by checking the drift status of your
environment configuration. For more information, see [Detect drift on an entire
CloudFormation stack](../../../AWSCloudFormation/latest/UserGuide/detect-drift-stack.md "../../../AWSCloudFormation/latest/UserGuide/detect-drift-stack.md") in the _AWS CloudFormation User Guide_.

Use the **eb clone** command to clone a running environment, as
follows.

```
~/workspace/my-app$ `eb clone `my-env1``
Enter name for Environment Clone
(default is my-env1-clone): ``my-env2``
Enter DNS CNAME prefix
(default is my-env1-clone): ``my-env2``

```

You can specify the name of the source environment in the clone command, or leave it out
to clone the default environment for the current project folder. The EB CLI prompts you to
enter a name and DNS prefix for the new environment.

By default, **eb clone** creates the new environment with the latest
available version of the source environment's platform. To force the EB CLI to use the same
version, even if there is a newer version available, use the `--exact`
option.

```
~/workspace/my-app$ `eb clone --exact`
```

For more information about this command, see [eb
clone](eb3-clone.md "eb3-clone.md").
