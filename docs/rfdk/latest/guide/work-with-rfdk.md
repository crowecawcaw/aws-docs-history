

# Working with the RFDK
<a name="work-with-rfdk"></a>

**Important**  
On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/) for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com) or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html).

The Render Farm Deployment Kit on AWS (RFDK) lets you define your AWS cloud infrastructure in a general-purpose programming language. Currently, the RFDK supports TypeScript and Python.

We develop the RFDK in TypeScript and use [JSII](https://github.com/aws/jsii) to provide an idiomatic experience in other supported languages. For example, we distribute RFDK modules using each language’s standard repository, and you install them using the language’s standard package manager. Methods and properties are even named using your language’s recommended naming patterns.

## RFDK prerequisites
<a name="work-with-prerequisites"></a>

To use the RFDK, you need an AWS account and a corresponding access key. If you don’t have an AWS account yet, see [Create and Activate an AWS Account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/). To find out how to obtain an access key ID and secret access key for your AWS account, see [Understanding and Getting Your Security Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html). To find out how to configure your workstation so the CDK uses your credentials, see [Setting Credentials in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-credentials-node.html).

**Tip**  
If you have the [AWS CLI](https://aws.amazon.com/cli/) installed, the simplest way to set up your workstation with your credentials is to open a command prompt and type:  

```
aws configure
```

All RFDK applications require Node.js, even when your app is written in Python. Please see [Prerequisites](getting-started.md#prerequisites) for determining the minimum supported Node.js version. You may download a compatible version for your platform at [nodejs.org](https://nodejs.org/). We recommend the [current LTS version](https://nodejs.org/en/about/releases/) (at this writing, the latest 12.x release).

**Topics**

## Creating a project
<a name="creating-a-project"></a>

This section documents how to create a new RFDK Python project.

### Creating an AWS CDK application
<a name="typescript-newproject-createapp"></a>

The first step to create a new RFDK project is to select a version of RFDK to use. It is highly recommended to use the latest version of RFDK available when starting a new project. The following command lists the latest published version of RFDK, stores the result in the `RFDK_VERSION` shell variable, and outputs a message with the version number.

```
RFDK_VERSION=$(npm view aws-rfdk version)
echo "RFDK Version: ${RFDK_VERSION}"
```

If you require a legacy version of RFDK, you can [list all available RFDK versions](#list-rfdk-versions) and set the variable to {{DESIRED\_RFDK\_VERSION}} manually.

```
RFDK_VERSION={{DESIRED_RFDK_VERSION}}
```

Once you have the desired version of RFDK stored in the `RFDK_VERSION` shell variable, you must determine the corresponding AWS CDK version. To determine the CDK version and store it in the `CDK_VERSION` shell variable, run the following command:

```
CDK_VERSION=$(npm view aws-rfdk@${RFDK_VERSION} 'dependencies.@aws-cdk/core')
```

Next, initialize the CDK app with:

------
#### [ Python ]

```
npx cdk@${CDK_VERSION} init app --language=python
```

------
#### [ TypeScript ]

```
npx cdk@${CDK_VERSION} init app --language=typescript
```

------

**Note**  
We also provide some sample applications in the [RFDK’s github](https://github.com/aws/aws-rfdk/tree/release/examples) that you may find useful as a starting point for your own render farm. Please be sure to use example code from only the `release` branch as examples in other branches may not be compatible with the officially released RFDK.

### Installing RFDK
<a name="python-newproject-installrfdk"></a>

------
#### [ Python ]

Given that you want to use {{RFDK\_VERSION}} (see previous section), you will need to add the RFDK to the list of dependencies required by your python package. This is done by modifying the `setup.py` file in the root of your CDK application to add an entry for `aws-rfdk` to the `install_requires` argument of the `setup` function:

```
setup(
    # ...
    install_requires=[
        "aws-cdk.core==1.57.0",
        "aws-rfdk=={{RFDK_VERSION}}"
    ],
    # ...
)
```

Once the dependency has been added to `setup.py`, install it into the virtual environment created by the CDK toolkit:

```
source .venv/bin/activate
pip install -r requirements.txt
```

------
#### [ TypeScript ]

Given that you have the version of RFDK in the `RFDK_VERSION` shell variable (see previous section), you will need to add the RFDK to the list of dependencies required by your npm package. This can be done with the following command:

```
npm install --save aws-rfdk@${RFDK_VERSION}
```

Next, you will need to [Install peer dependencies](work-with-rfdk-typescript.md#typescript-installpeerdeps).

------

## Deadline Container Images
<a name="deadline-container-images"></a>

RFDK deploys Deadline server components, such as:
+ The [`RenderQueue`](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.deadline.RenderQueue.html) construct, and
+ The [`UsageBasedLicensing`](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.deadline.UsageBasedLicensing.html) construct,

using **AWS Elastic Container Service (ECS)**. RFDK integrates with the Deadline container images and recipes published by [AWS Thinkbox](https://www.awsthinkbox.com/). These images and recipes can be extended to customize the images deployed to your RFDK render farm. The two supported workflows to deploy Deadline conatiner images are:

1.  [Using AWS Thinkbox ECR Repositories](#using-aws-thinkbox-ecr-repositories) 

   In most cases, RFDK apps can make use of the Deadline container images published by AWS Thinkbox. The images have been designed to integrate with the RFDK and are automatically updated with the latest system security patches. By using images published by AWS Thinkbox, you can eliminate the effort of building your own images, maintaining a container image repository, and keeping the images updated.

1.  [Staging Deadline Recipes](#staging-deadline) 

   For more control over the Deadline container images deployed, RFDK provides a staging workflow. AWS Thinkbox publishes recipes for building Deadline container images using Docker. These recipes can be used as-is, or they can be customized as desired. When deploying the `RenderQueue` or `UsageBasedLicensing` constructs to an isolated subnet without internet access, you will need to use the staging workflow. This is because the AWS Thinkbox published container images are hosted through ECR Public Repositories and VPC endpoints are currently unavailable for this service.

### Using AWS Thinkbox ECR Repositories
<a name="using-aws-thinkbox-ecr-repositories"></a>

RFDK provides a [`ThinkboxDockerImages`](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.deadline.ThinkboxDockerImages.html) construct that can be used to provide Deadline container images from AWS Thinkbox’s public ECR Repositories to other RFDK constructs in your CDK app.

It is recommended that you pin this version to the latest available version of Deadline when building your farm. Please consult Deadline’s [CHANGELOG](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/release-notes.html) for a list of available versions.

**Note**  
Please check with the [RFDK release notes](https://github.com/aws/aws-rfdk/releases) to determine the version compatibility with Deadline.

The following sample code demonstrates how to use `ThinkboxDockerImages`:

------
#### [ Python ]

Replace {{"10.2.0"}} with your desired minor version of Deadline:

```
import aws_cdk as cdk
import Vpc from aws_cdk.aws_ec2
import Construct from constructs
from aws_rfdk import deadline

class HelloRfdkStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        vpc = Vpc(stack, 'Vpc')

        # Specify Deadline Version (in this example we pin to the latest 10.2.0.x)
        version = deadline.VersionQuery(self, 'Version',
            version={{"10.2.0"}},
        )

        # Fetch the Deadline container images for the specified Deadline version
        images = deadline.ThinkboxDockerImages(self, 'Images',
            version=version,
            # The ThinkboxDockerImages will install Deadline onto one or more EC2 instances.
            # By downloading or using the Deadline software, you agree to the AWS Customer Agreement (https://aws.amazon.com/agreement/)
            # and AWS Intellectual Property License (https://aws.amazon.com/legal/aws-ip-license-terms/). You acknowledge that Deadline
            # is AWS Content as defined in those Agreements.
            # Please set the user_aws_customer_agreement_and_ip_license_acceptance property to
            # USER_ACCEPTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE to signify your acceptance of these terms.
            user_aws_customer_agreement_and_ip_license_acceptance=deadline.AwsCustomerAgreementAndIpLicenseAcceptance.{{USER_REJECTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE}}
        )

        repo = deadline.Repository(stack, 'Repo',
            vpc=vpc,
            version=version,
        )

        # Use the container images to create a RenderQueue
        render_queue = deadline.RenderQueue(stack, 'RenderQueue',
            vpc=vpc,
            repository=repo,
            version=version,
            images=images.for_render_queue(),
        )
```

------
#### [ TypeScript ]

Replace {{"10.2.0"}} with your desired minor version of Deadline:

```
import * as cdk from 'aws-cdk-lib';
import { Vpc } from 'aws-cdk-lib/aws-ec2';
import { Construct } from 'constructs';
import * as deadline from 'aws-rfdk/deadline';

export class HelloRfdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new Vpc(this, 'Vpc');

    // Specify Deadline Version (in this example we pin to the latest 10.2.0.x)
    const version = new deadline.VersionQuery(this, 'Version', {
      version: {{"10.2.0"}},
    });

    # Fetch the Deadline container images for the specified Deadline version
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
      userAwsCustomerAgreementAndIpLicenseAcceptance: deadline.AwsCustomerAgreementAndIpLicenseAcceptance.{{USER_REJECTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE}},
    });

    const repo = new deadline.Repository(stack, 'Repo', {
      vpc: vpc,
      version: version,
    });

    // Use the container images to create a RenderQueue
    const renderQueue = new deadline.RenderQueue(stack, 'RenderQueue', {
      vpc: vpc,
      repository: repo,
      version: version,
      images: images.forRenderQueue(),
    });
  }
}
```

------

### Staging Deadline Recipes
<a name="staging-deadline"></a>

RFDK builds upon the [Docker image assets](https://docs.aws.amazon.com/cdk/latest/guide/assets.html#assets_types_docker) feature of the AWS CDK to streamline the workflow of customizing Deadline container images. When you deploy a CDK application that uses Docker image assets, the CDK:

1. Uses Docker to build a container image from a specified directory

1. Pushes the container image layers to the CDK boostrap ECR Repository

1. Specifies CloudFormation parameters that refer to the name of the pushed ECR

 **Staging** Deadline describes the process of preparing a conventional directory structure that can be built into Deadline container images by the RFDK at deployment time.

RFDK provides a `stage-deadline` command that stages Deadline.

To stage the Docker recipes for the latest version of Deadline, run the following command:

------
#### [ Python ]

Assuming your CDK application uses {{RFDK\_VERSION}}:

```
npx -p aws-rfdk@{{RFDK_VERSION}} stage-deadline 
```

------
#### [ TypeScript ]

```
npx stage-deadline
```

------

To stage the Docker recipes for a specified Deadline version (<replaceable>DEADLINE\_VERSION</replaceable>), run the following command:

------
#### [ Python ]

Assuming your CDK application uses {{RFDK\_VERSION}}:

```
npx -p aws-rfdk@{{RFDK_VERSION}} stage-deadline {{DEADLINE_VERSION}}
```

------
#### [ TypeScript ]

```
npx stage-deadline {{DEADLINE_VERSION}}
```

------

If you have custom Deadline installers ({{DEADLINE\_INSTALLER\_S3\_URI}}) or Docker recipes ({{DOCKER\_RECIPES\_S3\_URI}}), they can be uploaded to S3 in the `tar.gz` format and used as well:

------
#### [ Python ]

Assuming your CDK application uses {{RFDK\_VERSION}}:

```
npx -p aws-rfdk@{{RFDK_VERSION}} stage-deadline {{DEADLINE_VERSION}}
```

------
#### [ TypeScript ]

```
npx stage-deadline {{DEADLINE_VERSION}}
```

------

**Note**  
Please check with the [RFDK release notes](https://github.com/aws/aws-rfdk/releases) to determine the version compatibility with Deadline.

The default behavior of `stage-deadline` is to create a `stage` subdirectory under the current working directory and stage the files into it. The choice of destination directory can be changed by specifying a `--output {{OUTPUT_DIR}} ` command-line argument.

RFDK provides a [`ThinkboxDockerRecipes`](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.deadline.ThinkboxDockerRecipes.html) construct that interacts with the Deadline Docker recipes within a staging directory.

The following sample code demonstrates how to use `ThinkboxDockerRecipes`:

------
#### [ Python ]

Replace {{STAGE\_DIR}} with the path to the stage directory:

```
import aws_cdk.core as cdk
import aws_rfdk.deadline as rfdk_deadline

class HelloRfdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        vpc = cdk.Vpc(stack, 'Vpc')

        # This directory is the one specified in the --output argument of the stage-deadline command
        stage = rfdk_deadline.Stage.from_directory({{STAGE_DIR}})

        # Create the ThinkboxDockerRecipes instance
        recipes = rfdk_deadline.ThinkboxDockerRecipes(self, 'ServerImages',
            stage=stage,
        )

        repo = rfdk_deadline.Repository(stack, 'Repo',
            vpc=vpc,
            version=recipes.version,
        )

        # Use the container images to create a RenderQueue
        render_queue = rfdk_deadline.RenderQueue(stack, 'RenderQueue',
            vpc=vpc,
            repository=repo,
            version=recipes.version,
            image=recipes.render_queue_images,
        )
```

------
#### [ TypeScript ]

Replace {{STAGE\_DIR}} with the path to the stage directory:

```
import * as cdk from '@aws-cdk/core';
import * as deadline from 'aws-rfdk/deadline';

export class HelloRfdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    vpc = new cdk.Vpc(this, 'Vpc');

    // Create the ThinkboxDockerRecipes instance
    recipes = new deadline.ThinkboxDockerRecipes(this, 'Recipes', {
      stage: deadline.Stage.fromDirectory({{STAGE_DIR}}),
    });

    repo = new deadline.Repository(stack, 'Repo', {
      vpc: vpc,
      version: recipes.version,
    });

    // Use the container images to create a RenderQueue
    render_queue = new deadline.RenderQueue(stack, 'RenderQueue', {
      vpc: vpc,
      repository: repo,
      version: recipes.version,
      image: recipes.renderQueueImages,
    });
  }
}
```

------

## Listing available RFDK versions
<a name="list-rfdk-versions"></a>

Use the following command to output a list of available versions of RFDK:

```
npm view aws-rfdk versions
```