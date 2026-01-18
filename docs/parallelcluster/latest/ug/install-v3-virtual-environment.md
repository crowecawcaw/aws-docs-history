# Install AWS ParallelCluster in a virtual environment (recommended)

We recommend that you install AWS ParallelCluster in a virtual environment to avoid requirement version conflicts with other
`pip` packages.

###### Prerequisites

- AWS ParallelCluster requires Python 3.7 or later. If you don't already have it installed, [download a compatible version](https://www.python.org/downloads/ "https://www.python.org/downloads/") for your platform at [python.org](https://www.python.org/ "https://www.python.org/").

###### To install AWS ParallelCluster in a virtual environment

1. If `virtualenv` isn't installed, install `virtualenv` using `pip3`. If `python3 -m virtualenv
help` displays help information, go to step 2.

```
`$` `python3 -m pip install --upgrade pip`
`$` `python3 -m pip install --user --upgrade virtualenv`
```

Run `exit` to leave the current terminal window and open a new terminal window to pick up changes to the
environment. 2. Create a virtual environment and name it.

```
`$` `python3 -m virtualenv `~/apc-ve``
```

Alternatively, you can use the `-p` option to specify a specific version of Python.

```
`$` `python3 -m virtualenv -p $(which python3) `~/apc-ve``
```

3. Activate your new virtual environment.

```
`$` `source `~/apc-ve`/bin/activate`
```

4. Install AWS ParallelCluster into your virtual environment.

```
`(apc-ve)~$` `python3 -m pip install --upgrade "aws-parallelcluster"`
```

5. Install Node Version Manager and the latest Long-Term Support (LTS) Node.js version. AWS Cloud Development Kit (AWS CDK) requires Node.js for CloudFormation for template generation.

###### Note

If your Node.js installation isn't working on your platform, you can install an LTS version prior to the latest LTS version. For more information,
see the [Node.js release schedule](https://github.com/nodejs/release#release-schedule "https://github.com/nodejs/release#release-schedule") and the [AWS CDK](../../../cdk/v2/guide/work-with.md#work-with-prerequisites "../../../cdk/v2/guide/work-with.md#work-with-prerequisites") prerequisites.

Example Node.js installation command:

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

6. Verify that AWS ParallelCluster is installed correctly.

```
`$` `pcluster version`
`{
 "version": "3.14.1"
}`
```

You can use the `deactivate` command to exit the virtual environment. Each time you start a session, you must [reactivate the environment](#activate-virtual-environment-3 "#activate-virtual-environment-3").

To upgrade to the latest version of AWS ParallelCluster, run the installation command again.

```
`(apc-ve)~$` `python3 -m pip install --upgrade "aws-parallelcluster"`
```
