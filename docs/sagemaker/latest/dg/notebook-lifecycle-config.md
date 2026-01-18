# Customization of a SageMaker notebook instance

using an LCC script

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

A _lifecycle configuration_ (LCC) provides shell
scripts that run only when you create the notebook instance or whenever you start one.
When you create a notebook instance, you can create a new LCC or attach an LCC that you
already have. Lifecycle configuration scripts are useful for the following use
cases:

- Installing packages or sample notebooks on a notebook instance
- Configuring networking and security for a notebook instance
- Using a shell script to customize a notebook instance
  You can also use a lifecycle configuration script to access AWS services from your
  notebook. For example, you can create a script that lets you use your notebook to
  control other AWS resources, such as an Amazon EMR instance.

We maintain a public repository of notebook lifecycle configuration scripts that
address common use cases for customizing notebook instances at [https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples "https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples").

###### Note

Each script has a limit of 16384 characters.

The value of the `$PATH` environment variable that is available to both
scripts is
`/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin`. The
working directory, which is the value of the `$PWD` environment variable,
is `/`.

View CloudWatch Logs for notebook instance lifecycle configurations in log group
`/aws/sagemaker/NotebookInstances` in log stream
`[notebook-instance-name]/[LifecycleConfigHook]`.

Scripts cannot run for longer than 5 minutes. If a script runs for longer than 5
minutes, it fails and the notebook instance is not created or started. To help
decrease the run time of scripts, try the following:

- Cut down on necessary steps. For example, limit which conda environments
  in which to install large packages.
- Run tasks in parallel processes.
- Use the `nohup` command in your script.
  You can see a list of notebook instance lifecycle configurations you previously
  created by choosing **Lifecycle configuration** in the SageMaker AI console.
  You can attach a notebook instance LCC when you create a new notebook instance. For more
  information about creating a notebook instance, see [Create an Amazon SageMaker notebook instance](howitworks-create-ws.md "howitworks-create-ws.md").

## Lifecycle Configuration Best

Practices

The following are best practices for using lifecycle configurations:

###### Important

We do not recommend storing sensitive information in your lifecycle
configuration script.

###### Important

Lifecycle configuration scripts run with root access and the notebook
instance's IAM execution role privileges, regardless of the root access setting
for notebook users. Principals with permissions to create or modify lifecycle
configurations and update notebook instances can execute code with the
execution role's credentials. See [Control root access to a SageMaker notebook instance](nbi-root-access.md "nbi-root-access.md") for more information.

- Lifecycle configurations run as the `root` user. If your script
  makes any changes within the `/home/ec2-user/SageMaker`
  directory, (for example, installing a package with `pip`), use
  the command `sudo -u ec2-user` to run as the
  `ec2-user` user. This is the same user that Amazon SageMaker AI runs
  as.
- SageMaker AI notebook instances use `conda` environments to implement
  different kernels for Jupyter notebooks. If you want to install packages
  that are available to one or more notebook kernels, enclose the commands to
  install the packages with `conda` environment commands that
  activate the conda environment that contains the kernel where you want to
  install the packages.

For example, if you want to install a package only for the
`python3` environment, use the following code:

```
#!/bin/bash
sudo -u ec2-user -i <<EOF

# This will affect only the Jupyter kernel called "conda_python3".
source activate python3

# Replace `myPackage` with the name of the package you want to install.
pip install `myPackage`
# You can also perform "conda install" here as well.

source deactivate

EOF
```

If you want to install a package in all conda environments in the notebook
instance, use the following code:

```
#!/bin/bash
sudo -u ec2-user -i <<EOF

# Note that "base" is special environment name, include it there as well.
for env in base /home/ec2-user/anaconda3/envs/*; do
    source /home/ec2-user/anaconda3/bin/activate $(basename "$env")

    # Installing packages in the Jupyter system environment can affect stability of your SageMaker
    # Notebook Instance.  You can remove this check if you'd like to install Jupyter extensions, etc.
    if [ $env = 'JupyterSystemEnv' ]; then
      continue
    fi

    # Replace `myPackage` with the name of the package you want to install.
    pip install --upgrade --quiet `myPackage`
    # You can also perform "conda install" here as well.

    source /home/ec2-user/anaconda3/bin/deactivate
done

EOF
```

- You must store all conda environments in the default environments folder
  (/home/user/anaconda3/envs).

###### Important

When you create or change a script, we recommend that you use a text editor
that provides Unix-style line breaks, such as the text editor available in the
console when you create a notebook. Copying text from a non-Linux operating
system might introduce incompatible line breaks and result in an unexpected
error.
