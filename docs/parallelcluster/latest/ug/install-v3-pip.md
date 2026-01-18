# Installing AWS ParallelCluster in a non-virtual environment using pip

You can also install AWS ParallelCluster in a non-virtual environment using pip, a package
manager for Python packages.

###### Prerequisites

- AWS ParallelCluster requires Python 3.7 or later. If you don't already have it installed, [download a compatible version](https://www.python.org/downloads/ "https://www.python.org/downloads/") for your platform at [python.org](https://www.python.org/ "https://www.python.org/").

###### Install AWS ParallelCluster

1. Use `pip` to install AWS ParallelCluster.

```
`$` `python3 -m pip install "aws-parallelcluster" --upgrade --user`
```

When you use the `--user` switch, `pip` installs AWS ParallelCluster to `~/.local/bin`. 2. Install Node Version Manager and the latest Long-Term Support (LTS) Node.js version. AWS Cloud Development Kit (AWS CDK) requires Node.js for CloudFormation for template generation.

###### Note

If your Node.js installation isn't working on your platform, you can install an LTS version prior to the latest LTS version. For more information,
see the [Node.js release schedule](https://github.com/nodejs/release#release-schedule "https://github.com/nodejs/release#release-schedule") and the [AWS CDK](../../../cdk/v2/guide/work-with.md#work-with-prerequisites "../../../cdk/v2/guide/work-with.md#work-with-prerequisites") prerequisites.

```
`$`  `nvm install --lts=Hydrogen`
```

```
`$` `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash`
`$` `chmod ug+x ~/.nvm/nvm.sh`
`$` `source ~/.nvm/nvm.sh`
`$` `nvm install --lts`
`$` `node --version`
```

3. Verify that AWS ParallelCluster installed correctly.

```
`$` `pcluster version`
`{
 "version": "3.14.1"
}`
```

4. To upgrade to the latest version, run the installation command again.

```
`$` `python3 -m pip install "aws-parallelcluster" --upgrade --user`
```
