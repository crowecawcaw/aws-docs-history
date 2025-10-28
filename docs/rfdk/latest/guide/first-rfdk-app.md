# Your first RFDK app

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

Now that you have installed the [Prerequisites](getting-started.md#prerequisites "getting-started.md#prerequisites") and have completed [Onboarding to CDK](getting-started.md#onboarding-to-cdk "getting-started.md#onboarding-to-cdk"), let’s get started on your first RFDK app — a simple render farm using
[AWS Thinkbox Deadline](https://www.awsthinkbox.com/deadline "https://www.awsthinkbox.com/deadline"). In this tutorial, you will learn how to:

1. Initialize an RFDK app.
2. Stage the Docker recipes used for various Deadline components.
3. Add code that defines a simple Deadline render farm.
4. Build and deploy your RFDK render farm to your AWS account.
   Your RFDK render farm will be deployed as a single CloudFormation stack that will contain:

- A VPC
- The back-end of the farm
  - Database and file system — Deadline Repository
  - Central service — Deadline Render Queue

- The render nodes — Deadline Worker Fleet

**Estimated time: 75-90 minutes** Approximately 60 minutes of this will be waiting for AWS CloudFormation to deploy and destroy your resources.

###### Important

This guide is written assuming you are working on an EC2 instance running on Linux, but you can also use your local machine if desired.
It also assumes that you have installed the [Prerequisites](getting-started.md#prerequisites "getting-started.md#prerequisites") and have completed [Onboarding to CDK](getting-started.md#onboarding-to-cdk "getting-started.md#onboarding-to-cdk") on this instance.

## Initialize the RFDK app

You can create your RFDK app anywhere on your machine, but each RFDK app should be in its own directory.
Create a new directory for your app and enter it:

```
mkdir hello-rfdk
cd hello-rfdk
```

First, you must determine the latest version of RFDK available.
The following command uses `npm` (bundled with Node.js) to look-up the latest version of the `aws-rfdk` package, store it in the `RFDK_VERSION` shell variable, and output a message indicating the version:

```
RFDK_VERSION=$(npm view aws-rfdk version)
echo "Using RFDK version ${RFDK_VERSION}"
```

Next, find the version of the AWS CDK that is compatible with this version of RFDK:

```
CDK_VERSION=$(npm view aws-rfdk 'dependencies.aws-cdk-lib')
echo "Using CDK version ${CDK_VERSION}"
```

###### Note

It is important that the version of the `aws-cdk` packages installed in your project match the version of `aws-cdk` packages required by the RFDK version used in your app.

Now, initialize the app using the CDK toolkit’s `cdk init` command:

Python

```
npx cdk@${CDK_VERSION} init app --language python
```

TypeScript

```
npx cdk@${CDK_VERSION} init app --language typescript
```

With the CDK project initialized, install the `aws-rfdk` package:

Python
Modify `setup.py` in the root of the app directory to add an entry for `aws-rfdk` to the `install_requires` list. Replace `RFDK_VERSION` with the version output in the previous step:

```
setup(
    # ...
    install_requires=[
        # ...
        "aws-rfdk==`RFDK_VERSION`",
        # ...
    ],
    # ...
)
```

Now activate the app's Python virtual environment and install its dependencies:

```
source .venv/bin/activate
python -m pip install -r requirements.txt
```

TypeScript

```
npm install --save aws-rfdk@${RFDK_VERSION}
```

To install all of the peer dependencies required by RFDK, use the following command (requires `jq`):

```
npm view --json aws-rfdk@${RFDK_VERSION} peerDependencies | jq '. | to_entries[] | .key + "@" + .value' | xargs npm i --save
```

## Setup the environment

Each application needs to be associated with an [AWS environment](../../../cdk/latest/guide/environments.md "../../../cdk/latest/guide/environments.md"): the target Account and Region into which the
stack is intended to be deployed. You can specify the exact values for Account and Region or use the environment variables as in the example below:

Python
In `app.py`:

```
# ...
import os

env = {
    'account': os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
    'region': os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"])
}

app = cdk.App()
HelloRfdkStack(app, "hello-rfdk", env=env)
```

TypeScript
In `bin/hello-rfdk.ts`:

```
new HelloRfdkStack(app, 'hello-rfdk', {
  env: {
    account: process.env.CDK_DEPLOY_ACCOUNT ?? process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEPLOY_REGION ?? process.env.CDK_DEFAULT_REGION,
}});
```

## Define a Deadline render farm

Now you are ready to start building your render farm. The first thing you will need is a [`Vpc`](../../../cdk/api/latest/docs/@aws-cdk_aws-ec2.md "../../../cdk/api/latest/docs/@aws-cdk_aws-ec2.md") construct instance for your render farm. The `Vpc` provides the foundational
networking that will be used by all other components in the farm.

Python
In `hello_rfdk/hello_rfdk_stack.py`:

```
import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
from constructs import Construct

class HelloRfdkStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "Vpc")
```

TypeScript
In `lib/hello-rfdk-stack.ts`:

```
import * as cdk from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import { Construct } from 'constructs';

export class HelloRfdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, 'Vpc');
  }
}
```

The next thing you will need to do is select a version of AWS Thinkbox Deadline to use for your Render Farm.
For more details, see the full documentation about [Using AWS Thinkbox ECR Repositories](work-with-rfdk.md#using-aws-thinkbox-ecr-repositories "work-with-rfdk.md#using-aws-thinkbox-ecr-repositories").
Once you have selected a Deadline version (`DEADLINE_VERSION`), create a
[`VersionQuery`](../../api/latest/docs/aws-rfdk.deadline.md "../../api/latest/docs/aws-rfdk.deadline.md") construct in your
CDK app.

Python
In `hello_rfdk/hello_rfdk_stack.py`:

```
# ...
import aws_rfdk.deadline as rfdk_deadline

class HelloRfdkStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        # ...

        # Pin to the 10.2.0.x Deadline release. Release patches are applied with each CDK deployment
        version = rfdk_deadline.VersionQuery(self, "Version",
            version=`"10.2.0"`,
        )
```

TypeScript
In `lib/hello-rfdk-stack.ts`:

```
// ...
import * as deadline from 'aws-rfdk/deadline';

export class HelloRfdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // ...

    // Pin to the 10.2.0.x Deadline release. Release patches are applied with each CDK deployment
    const version = new deadline.VersionQuery(this, 'Version', {
      version: `'10.2.0'`,
    });
  }
}
```

Next, let’s add in a [`Repository`](../../api/latest/docs/aws-rfdk.deadline.md "../../api/latest/docs/aws-rfdk.deadline.md").
This construct creates the database and file system that make up the back-end storage of your render farm.
Then, it configures them with the [Deadline Repository](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/overview.html#components "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/overview.html#components") installer.
By default, an [Amazon DocumentDB](https://aws.amazon.com/documentdb/ "https://aws.amazon.com/documentdb/") and [Amazon Elastic File System (EFS)](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/") are created.

###### Tip

In the Deadline documentation, the Database and Repository are two separate concepts. The RFDK combines the two concepts and calls it the Repository.

Python
In `hello_rfdk/hello_rfdk_stack.py`:

```
# ...
class HelloRfdkStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        # ...

        repository = rfdk_deadline.Repository(self, 'Repository',
            vpc=vpc,
            version=version,
        )
```

TypeScript
In `lib/hello-rfdk-stack.ts`:

```
// ...

export class HelloRfdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // ...

    const repository = new deadline.Repository(this, 'Repository', {
      vpc,
      version,
    });
  }
}
```

AWS Thinkbox publishes Deadline container images into a publicly-available **Elastic Container Registry (ECR)** Repository.
RFDK provides the [`ThinkboxDockerImages`](../../api/latest/docs/aws-rfdk.deadline.md "../../api/latest/docs/aws-rfdk.deadline.md") construct that can be used to deploy these container images using **AWS Elastic Container Service (ECS)**.

To use these images, add a `ThinkboxDockerImages` instance to your CDK app. For this, you will need to read and accept
the terms of the [AWS Customer Agreement](https://aws.amazon.com/agreement/ "https://aws.amazon.com/agreement/") and [AWS Intellectual Property License](https://aws.amazon.com/legal/aws-ip-license-terms/ "https://aws.amazon.com/legal/aws-ip-license-terms/").

Python
In `hello_rfdk/hello_rfdk_stack.py`:

```
# ...
class HelloRfdkStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        # ...

        images = rfdk_deadline.ThinkboxDockerImages(self, 'Images',
            version=version,
            # The ThinkboxDockerImages will install Deadline onto one or more EC2 instances.
            # By downloading or using the Deadline software, you agree to the AWS Customer Agreement (https://aws.amazon.com/agreement/)
            # and AWS Intellectual Property License (https://aws.amazon.com/legal/aws-ip-license-terms/). You acknowledge that Deadline
            # is AWS Content as defined in those Agreements.
            # Please set the user_aws_customer_agreement_and_ip_license_acceptance property to
            # USER_ACCEPTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE to signify your acceptance of these terms.
            user_aws_customer_agreement_and_ip_license_acceptance=rfdk_deadline.AwsCustomerAgreementAndIpLicenseAcceptance.`USER_REJECTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE`
        )
```

TypeScript
In `lib/hello-rfdk-stack.ts`:

```
// ...

export class HelloRfdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // ...

    const images = new deadline.ThinkboxDockerImages(this, 'Images', {
      version,
      /**
       * The ThinkboxDockerImages will install Deadline onto one or more EC2 instances.
       * By downloading or using the Deadline software, you agree to the AWS Customer Agreement (https://aws.amazon.com/agreement/)
       * and AWS Intellectual Property License (https://aws.amazon.com/legal/aws-ip-license-terms/). You acknowledge that Deadline
       * is AWS Content as defined in those Agreements.
       * Please set the userAwsCustomerAgreementAndIpLicenseAcceptance property to
       * USER_ACCEPTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE to signify your acceptance of these terms.
       */
      userAwsCustomerAgreementAndIpLicenseAcceptance: deadline.AwsCustomerAgreementAndIpLicenseAcceptance.`USER_REJECTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE`,
    });
  }
}
```

Now that you have Deadline container images and a Deadline Repository, you will need to add a [`RenderQueue`](../../api/latest/docs/aws-rfdk.deadline.md "../../api/latest/docs/aws-rfdk.deadline.md").
The `RenderQueue` acts as the central service of your render farm that clients and render nodes can connect to.
This construct creates a fleet of [Deadline Remote Connection Servers](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/remote-connection-server.html "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/remote-connection-server.html") running in [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/").

###### Tip

This example explicitly turns [deletion protection](../../../elasticloadbalancing/latest/application/application-load-balancers.md#deletion-protection "../../../elasticloadbalancing/latest/application/application-load-balancers.md#deletion-protection")
off so this stack can be easily cleaned up. By default, it is turned on to prevent accidental deletion of your `RenderQueue`.

Python
In `hello_rfdk/hello_rfdk_stack.py`:

```
# ...
class HelloRfdkStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        # ...

        render_queue = rfdk_deadline.RenderQueue(self, 'RenderQueue',
            vpc=vpc,
            repository=repository,
            version=version,
            images=images.for_render_queue(),
            deletion_protection=False,
        )
```

TypeScript
In `lib/hello-rfdk-stack.ts`:

```
// ...

export class HelloRfdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // ...

    const renderQueue = new deadline.RenderQueue(this, 'RenderQueue', {
      vpc,
      repository,
      version,
      images: images.forRenderQueue(),
      deletionProtection: false,
    });
  }
}
```

The last thing you need to add is a fleet of render nodes with the [`WorkerInstanceFleet`](../../api/latest/docs/aws-rfdk.deadline.md "../../api/latest/docs/aws-rfdk.deadline.md") construct, which creates a fleet of instances running
[Deadline Worker](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/worker.html "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/worker.html") in an
[Amazon EC2 Auto Scaling Group](../../../autoscaling/ec2/userguide/AutoScalingGroup.md "../../../autoscaling/ec2/userguide/AutoScalingGroup.md").

###### Important

The `WorkerInstanceFleet` construct requires an [Amazon Machine Image (AMI)](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") with
the Deadline Worker application installed. Substitute `your-ami-id` with your desired AMI ID in the code below. Conveniently,
AWS Thinkbox creates public AWS Portal AMIs you can use for this. Follow the steps in the Deadline guide for
[finding AWS Portal AMIs](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/aws-custom-ami.html#finding-which-ami-to-start-from "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/aws-custom-ami.html#finding-which-ami-to-start-from")
(these steps instruct you to specifically search for _“Deadline Worker Base”_ images, but you can use any Linux-based Deadline Worker image for this tutorial) and copy
over your desired AMI ID.

Python
In `hello_rfdk/hello_rfdk_stack.py`:

```
# ...
class HelloRfdkStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        # ...

        workers = rfdk_deadline.WorkerInstanceFleet(self, 'Workers',
            vpc=vpc,
            render_queue=render_queue,
            worker_machine_image=ec2.MachineImage.generic_linux({
                # TODO: Replace your-ami-id with your chosen AMI ID
                cdk.Stack.of(self).region: `"your-ami-id"`
            })
        )
```

TypeScript
In `lib/hello-rfdk-stack.ts`:

```
// ...

export class HelloRfdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // ...

    new deadline.WorkerInstanceFleet(this, 'WorkerFleet', {
      vpc,
      renderQueue,
      workerMachineImage: ec2.MachineImage.genericLinux({
        // TODO: Replace your-ami-id with your chosen AMI ID
        [this.region]: `'your-ami-id'`,
      }),
    });
  }
}
```

## Deploy the render farm

With the render farm fully defined in code, you can now build and deploy it. First, build the app with:

Python
No build step is necessary.

TypeScript

```
npm run build
```

You can optionally synthesize the CloudFormation template for your app if you are curious to see it (the generated CloudFormation template is
around _3300_ lines long):

```
npx cdk@${CDK_VERSION} synth
```

Now, deploy the render farm with:

```
npx cdk@${CDK_VERSION} deploy
```

This deployment will take approximately 30 minutes since the render farm contains many resources.

## Update the render farm

You can update properties of the deployed render farm by making changes to your app and deploying again.

By default, the RFDK will setup resources such that you cannot accidentally destroy important components by tearing down your CloudFormation stack. For instance, the
**Repository** contains information about your render farm and any work done with it, which is data that can be useful to keep (e.g. to start up your render farm again
in the same state it was in previously). For more details, see [Managing resources](best-practices.md#managing-resources "best-practices.md#managing-resources").

We don’t need to retain any render farm information for this tutorial, so let’s update the
[removal policies](../../../cdk/api/latest/docs/@aws-cdk_core.md "../../../cdk/api/latest/docs/@aws-cdk_core.md") to set the
[Deletion Policy](../../../AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.md") in the CloudFormation template of the
database and file system of your **Repository** so they are destroyed:

Python
In `hello_rfdk/hello_rfdk_stack.py`:

```
# ...
class HelloRfdkStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        # ...

        repository = rfdk_deadline.Repository(self, 'Repository',
            vpc=vpc,
            version=version,
            # Specify the removal policies
            removal_policy=rfdk_deadline.RepositoryRemovalPolicies(
                database=cdk.RemovalPolicy.DESTROY,
                filesystem=cdk.RemovalPolicy.DESTROY
            )
        )
```

TypeScript
In `lib/hello-rfdk-stack.ts`:

```
// ...

export class HelloRfdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // ...

    const repository = new deadline.Repository(this, 'Repository', {
      vpc,
      version,
      // Specify the removal policies
      removalPolicy: {
        database: cdk.RemovalPolicy.DESTROY,
        filesystem: cdk.RemovalPolicy.DESTROY,
      },
    });

    // ...
  }
}
```

Let’s also scale down your `WorkerInstanceFleet` to 0 so that all workers are terminated to save on costs:

Python
In `hello_rfdk/hello_rfdk_stack.py`:

```
# ...
class HelloRfdkStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        # ...

        workers = rfdk_deadline.WorkerInstanceFleet(self, 'Workers',
            vpc=vpc,
            render_queue=render_queue,
            worker_machine_image=ec2.MachineImage.generic_linux({
                # TODO: Replace your-ami-id with your chosen AMI ID
                cdk.Stack.of(self).region: `"your-ami-id"`
            }),
            # Scale capacity down to 0
            desired_capacity=0,
            min_capacity=0,
            max_capacity=0,
        )
```

TypeScript
In `lib/hello-rfdk-stack.ts`:

```
// ...

export class HelloRfdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // ...

    new deadline.WorkerInstanceFleet(this, 'WorkerFleet', {
      vpc,
      renderQueue,
      workerMachineImage: ec2.MachineImage.genericLinux({
        // TODO: Replace your-ami-id with your chosen AMI ID
        [this.region]: `'your-ami-id'`,
      }),
      // Scale capacity down to 0
      desiredCapacity: 0,
      minCapacity: 0,
      maxCapacity: 0,
    });
  }
}
```

Build your app again to incorporate your changes:

Python
No build step is necessary.

TypeScript

```
npm run build
```

You can optionally run `cdk diff` to see the changes in the CloudFormation template that will be applied:

```
npx cdk@${CDK_VERSION} diff
```

Now let’s deploy these changes:

```
npx cdk@${CDK_VERSION} deploy
```

You can verify these changes were applied by navigating to your `HelloRfdkStack` in the CloudFormation web console and viewing the updated resources.
They should have the **Status** field set to `UPDATE_COMPLETE`.

## (Optional) Submit a job to the render farm

###### Note

This is an optional step that shows you how to use your render farm but does not cover any new concepts in RFDK.
Feel free to skip this step and proceed with [tearing down your render farm](#tear-down-the-render-farm "#tear-down-the-render-farm").

### Setting up the connection

###### Important

In order to submit a job, you will need to [create a secure connection to your render](connecting-to-render-farm.md "connecting-to-render-farm.md").
The rest of this chapter will not work if you don’t set up this connection.

Once you set up the connection to the render farm and [allow the connection to the render queue](connecting-to-render-farm.md#allowing-connection-to-the-render-queue "connecting-to-render-farm.md#allowing-connection-to-the-render-queue"), you can build and deploy your changes.

```
npm run build
npx cdk@${CDK_VERSION} deploy
```

When the changes are deployed, [get remote connection server address](connecting-to-render-farm.md#getting-remote-connection-server-address "connecting-to-render-farm.md#getting-remote-connection-server-address") and save it for later.

```
RQ_DNS_NAME=`load-balancer-dns-name`

```

### Connecting Deadline Client to your render farm

You need to install [Deadline](https://www.awsthinkbox.com/deadline "https://www.awsthinkbox.com/deadline") Client on the machine you are submitting the job from.
You can download Deadline installers from the [AWS Thinkbox downloads page](https://downloads.thinkboxsoftware.com/ "https://downloads.thinkboxsoftware.com/").

Once you have downloaded an archive, extract the files and install Deadline Client.
For more information, please visit [Deadline Client Installation (Quick)](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/quick-install-client.html "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/quick-install-client.html") page.
Here is how you can install Deadline client in a silent mode on Amazon Linux 2 (AL2):

```
yum install lsb

DEADLINE_VERSION=`deadline-version`
tar -xvf Deadline-$DEADLINE_VERSION-linux-installers.tar
./DeadlineClient-$DEADLINE_VERSION-linux-x64-installer.run --mode text
```

You can now connect Deadline Client to your render farm.

New Deadline Client Installation

1. When prompted for the Repository Connection Type, select `Remote Connection Server`.
2. When prompted for the Remote Connection Server address, enter `$RQ_DNS_NAME:8080`.

Existing Deadline Client (Command Line)

1. Navigate to `bin` folder in your Deadline Client installation directory. For example:

```
cd /opt/Thinkbox/Deadline10/bin
```

2. Change the repository you are connected to with Deadline Command:

```
./deadlinecommand ChangeRepository Remote $RQ_DNS_NAME:8080
```

### Submitting a job to your render farm

Let’s submit a simple command line job that calls `ping` command.

Navigate to `bin` folder in your Deadline Client installation directory and submit the job with `deadlinecommand`:

```
cd /opt/Thinkbox/Deadline10/bin
./deadlinecommand SubmitCommandLineJob -frames 1 -executable "ping" -arguments "-c 3 localhost"
```

### Viewing Render Farm Statistics

The easiest way to check the result of the submitted job is to use another deadline command:

```
cd /opt/Thinkbox/Deadline10/bin
./deadlinecommand GetFarmStatistics
```

You should now have `Completed Jobs= 1` in the output.
Optionally, you can get the job id with `GetJobIds` and then use that id with `GetJob` command to view all the job details.
Find more [Deadline commands here](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/command.html "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/command.html").

### Viewing job output in CloudWatch

You can also view the output of the job you submitted in the Deadline Worker logs that can be found in CloudWatch.

1. Open the [AWS Web Console](https://console.aws.amazon.com/console/home "https://console.aws.amazon.com/console/home").
2. Navigate to `Services` > `CloudWatch` > `Log groups`.
3. Open the log group for your Deadline Worker fleet. By default, this will be of the form `/renderfarm/WorkerFleet`.
4. Open the logs for your Worker instance. This will be of the form WorkerLogs-`ec2-instance-id`.
   The `ec2-instance-id` is the ID of the `hello-rfdk/WorkerFleet/Default` instance.
   You can find this ID in the AWS Web Console for EC2 Service.
5. You should be able to find a line in the logs that contains `localhost ping`.
   You can use `Filter events` input field to easily find it.
   This is the output of Deadline Worker completing the job you submitted.

## Tear down the render farm

When you’re done with your render farm, you can destroy it:

```
npx cdk@${CDK_VERSION} destroy
```

If you have issues destroying your farm, ensure you have completed the [Update the render farm](#update-the-render-farm "#update-the-render-farm") section where we update properties that would
prevent some resources from being destroyed. Otherwise, refer to your `HelloRfdkStack` in the
[CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-using-console.md "../../../AWSCloudFormation/latest/UserGuide/cfn-using-console.md") to resolve any issues.

## Next steps

Now that you have seen RFDK in action, you can:

- Learn about [Working with the RFDK](work-with-rfdk.md "work-with-rfdk.md") in more depth
- Explore the [API reference](../../api/latest.md "../../api/latest.md") to discover all of the constructs and classes that RFDK offers
- Learn about [Best practices while using the RFDK](best-practices.md "best-practices.md") and [Security in the RFDK](security-considerations.md "security-considerations.md") to help make your render farm ready for production

The RFDK is an open-source project. We would be happy to have you [contribute](https://github.com/aws/aws-rfdk/blob/mainline/CONTRIBUTING.md "https://github.com/aws/aws-rfdk/blob/mainline/CONTRIBUTING.md")!
