# Prerequisites

Before you begin, set up the following items:

- An AWS account – If you don't have one yet, start with [Setting up a new AWS account](setting-up-aws.md "setting-up-aws.md").
- An AWS Identity and Access Management (IAM) user with access to the permissions needed for DataBrew – For more
  information, see [Adding users or groups with
  DataBrew permissions](setting-up-iam-users-and-groups-for-databrew.md "setting-up-iam-users-and-groups-for-databrew.md").
- An IAM role to use in DataBrew operations – You can use the default, if
  `AwsGlueDataBrewDataAccessRole` is configured. To set up
  additional IAM roles, see [Adding an IAM role with data resource
  permissions](setting-up-iam-role-to-use-in-databrew.md "setting-up-iam-role-to-use-in-databrew.md").
- A JupyterLab installation (version 2.2.6 or greater) – For more
  information, see the following topics in the [JupyterLab
  documentation](https://JupyterLab.readthedocs.io/en/stable/index.html "https://JupyterLab.readthedocs.io/en/stable/index.html"):
  - [JupyterLab prerequisites](https://JupyterLab.readthedocs.io/en/stable/getting_started/installation.html#prerequisites "https://JupyterLab.readthedocs.io/en/stable/getting_started/installation.html#prerequisites")
  - [JupyterLab installation](https://JupyterLab.readthedocs.io/en/stable/getting_started/installation.html "https://JupyterLab.readthedocs.io/en/stable/getting_started/installation.html") – We recommend using `pip install
jupyterlab`.

- A Node.js installation (version 12.0 or greater).
- An AWS Command Line Interface (AWS CLI) installation – For more information, see [Setting up the AWS CLI](setting-up-the-aws-cli.md "setting-up-the-aws-cli.md").
- An AWS Jupyter proxy installation (`pip install aws-jupyter-proxy`)–
  This extension is used with an AWS service endpoint to securely pass your AWS
  credentials. For more information, see [aws-jupyter-proxy](https://github.com/aws/aws-jupyter-proxy "https://github.com/aws/aws-jupyter-proxy") on GitHub.
  To verify that you have the prerequisites installed, you can run a test that's similar
  to the following at the command line, as shown in the following example.

```
echo "
AWS CLI:"
which aws
aws --version
aws configure list
aws sts get-caller-identity

echo "
Python (current environment):"
which python
python --version

echo "
Node.JS:"
which node
node --version

echo "
Jupyter:"
where jupyter
jupyter --version
jupyter serverextension list
pip3 freeze | grep jupyter
```

The output should look something like the following. The directories vary by operating system
and configuration.

```
AWS CLI:
/usr/local/bin/aws
aws-cli/2.1.2 Python/3.7.4 Darwin/19.6.0 exe/x86_64
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key     ****************VXW4 shared-credentials-file
secret_key     ****************MRJN shared-credentials-file
    region                us-east-1      config-file    ~/.aws/config
{
    "UserId": "",
    "Account": "111122223333",
    "Arn": "arn:aws:iam::111122223333:user/user2"
}

Python (current environment):
/usr/local/opt/python /libexec/bin/python
Python 3.8.5

Node.JS:
/usr/local/bin/node
v15.0.1

Jupyter:
/usr/local/bin/jupyter
jupyter core     : 4.6.3
jupyter-notebook : 6.0.3
qtconsole        : 4.7.5
ipython          : 7.16.1
ipykernel        : 5.3.2
jupyter client   : 6.1.6
jupyter lab      : 2.2.9
nbconvert        : 5.6.1
ipywidgets       : 7.5.1
nbformat         : 5.0.7
traitlets        : 4.3.3

config dir: /usr/local/etc/jupyter
    **aws\_jupyter\_proxy**  enabled
    - Validating...
      aws_jupyter_proxy  OK
    jupyterlab  enabled
    - Validating...
      jupyterlab 2.2.9 OK

**aws-jupyter-proxy**==0.1.0
jupyter-client==6.1.7
jupyter-core==4.7.0
jupyterlab==2.2.9
jupyterlab-pygments==0.1.2
jupyterlab-server==1.2.0

```
