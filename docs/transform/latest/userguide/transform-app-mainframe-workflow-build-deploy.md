# Build and deploy your modernized application post-refactoring

After you complete the refactoring process with AWS Transform, you can build and deploy your modernized Java application.
This guide walks you through retrieving your modernized code, configuring your environment, and deploying and testing your application.

###### Note

In addition to the guidance provided here, the AWS Transform generated code package will
include an _Set up the AWS Automated Refactor Development
Environment_ document which provides instructions to set up a IDE
(Integrated Development Environment) with [Developer Runtime](../../../m2/latest/userguide/ba-runtime-options.md#ba-runtime-options-developer "../../../m2/latest/userguide/ba-runtime-options.md#ba-runtime-options-developer").

###### Topics

- [Prerequisites](#transform-app-mainframe-workflow-build-deploy-prerequisites "#transform-app-mainframe-workflow-build-deploy-prerequisites")
- [Step 1: Retrieve the modernized code](#transform-app-mainframe-workflow-build-deploy-retrieve "#transform-app-mainframe-workflow-build-deploy-retrieve")
- [Step 2:
  Build the modernized application](#transform-app-mainframe-workflow-build-deploy-build "#transform-app-mainframe-workflow-build-deploy-build")
- [Step 3: Configure the test environment](#transform-app-mainframe-workflow-build-deploy-configure "#transform-app-mainframe-workflow-build-deploy-configure")
- [Step 4: Deploy the modernized application](#transform-app-mainframe-workflow-build-deploy-deployment "#transform-app-mainframe-workflow-build-deploy-deployment")
- [Step 5: Test the modernized
  application](#transform-app-mainframe-workflow-build-deploy-test "#transform-app-mainframe-workflow-build-deploy-test")
- [Additional
  example](#transform-app-mainframe-workflow-build-deploy-examples "#transform-app-mainframe-workflow-build-deploy-examples")

## Prerequisites

Before you begin, make sure you have:

- Successfully completed a refactoring job with AWS Transform.
- Access to the Amazon S3 bucket containing your modernized code. You can
  find this path on the console under **Refactor code →
  View results** or see [Step 1: Retrieve the modernized code](#transform-app-mainframe-workflow-build-deploy-retrieve "#transform-app-mainframe-workflow-build-deploy-retrieve").
- Installed and configured build software tool stack on your development
  machine, such as [Apache
  Maven](https://maven.apache.org/index.html "https://maven.apache.org/index.html") or [Apache
  Tomcat](https://tomcat.apache.org/ "https://tomcat.apache.org/"). For more information on Runtime versioning, see [AWS Blu Age release notes](../../../m2/latest/userguide/ba-release-notes.md "../../../m2/latest/userguide/ba-release-notes.md").
- Installed and configured Amazon Corretto or a version of Java runtime. For more
  information on installing Amazon Corretto, see [Amazon Corretto 24](../../../corretto/latest/corretto-24-ug/what-is-corretto-24.md "../../../corretto/latest/corretto-24-ug/what-is-corretto-24.md").
- Access to create and configure Amazon Aurora PostgreSQL databases for Runtime
  components, if necessary. For more information on Creating the Aurora PostgreSQL
  database, see [Working with Amazon Aurora PostgreSQL](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md").
- Administrative access to deploy applications to your runtime
  environment.
- Reviewed the [AWS Blu Age Runtime
  concepts](../../../m2/latest/userguide/ba-shared-concept.md "../../../m2/latest/userguide/ba-shared-concept.md") for fundamental concepts on applications modernized
  with AWS automated refactoring solution.

## Step 1: Retrieve the modernized code

To retrieve the modernized code

1. Navigate to your **Refactor code → View
   results** page on the console and locate the S3 path containing
   your generated code.
2. Download and extract the generated code package.
3. Open `codebase/app-pom/pom.xml` and note the required
   runtime engine version. For example
   `<gapwalk.version>4.6.0</gapwalk.version>`.
4. Locate the _Set up the AWS Automated Refactor
   Development Environment_ document from the downloaded code
   package for reference.

## Step 2:

Build the modernized application

To build your modernized application

1. Access the runtime version from a dedicated Amazon S3 bucket on the
   AWS account used with AWS Transform:
2. Download and install the appropriate runtime version (identified in [Step 1: Retrieve the modernized code](#transform-app-mainframe-workflow-build-deploy-retrieve "#transform-app-mainframe-workflow-build-deploy-retrieve")) on
   your local development machine.

###### Note

Additional information for installing the runtime dependencies on your
local machine is available in section 3.1 of the _Set up the AWS Automated Refactor Development
Environment_ document. 3. Open the command prompt and navigate to your application's root
directory. 4. To build deployable packages for the modernized application run the Maven
build command:

```
mvn package
```

Refer to the [Application Organization](../../../m2/latest/userguide/ba-shared-structure.md#ba-shared-structure-org "../../../m2/latest/userguide/ba-shared-structure.md#ba-shared-structure-org") page for details on the basic
organization of the modernized code. For instance, for modernized
application containing a front-end web application, you may expect at-least
the following deployable `.war` aggregates in addition to the
runtime components:

    * **Service project**: Contains
     legacy business logic modernization elements



    ```
    <business-app>-**service.\*.**war
    ```
    * **Web project**: Contains the
     modernization of user interface-related elements



    ```
    <business-app>-**web.\*.**war
    ```

## Step 3: Configure the test environment

To configure your test environment

1. Configure your modernized application runtime. For more information, see the
   [Set up configuration
   for Runtime](../../../m2/latest/userguide/ba-runtime-config.md "../../../m2/latest/userguide/ba-runtime-config.md") section in the _AWS Mainframe Modernization user
   guide_.

###### Note

Refer section 5 of the _Set up the AWS
Automated Refactor Development Environment_ guide for
runtime component specific configuration examples. 2. Prepare input and output (I/O) data sets for modernized applications.
Modernized applications may process sequential I/O data sets, VSAM data
sets, or others.

###### Note

Refer section 6 of the _Set up the AWS
Automated Refactor Development Environment_ for
examples. 3. A runtime environment - You can use your existing runtime environment or
create a new runtime environment.

    * To configure a non-managed runtime environment, see [Set up a non-managed application](../../../m2/latest/userguide/ba-runtime-setup.md "../../../m2/latest/userguide/ba-runtime-setup.md").
    * To configure a managed runtime environment, see [Set up a managed application](../../../m2/latest/userguide/ba-app-config.md "../../../m2/latest/userguide/ba-app-config.md").

After configuring the test environment, you move to the next step of deploying
the modernized application.

## Step 4: Deploy the modernized application

Deploy the application artifacts in the runtime you created and/or configured in
the [Step 2:
Build the modernized application](#transform-app-mainframe-workflow-build-deploy-build "#transform-app-mainframe-workflow-build-deploy-build") and [Step 3: Configure the test environment](#transform-app-mainframe-workflow-build-deploy-configure "#transform-app-mainframe-workflow-build-deploy-configure")
sections.

Additional guidance for deploying the modernized application can be found using
these links:

- [Deploy on Amazon EC2](../../../m2/latest/userguide/ba-deploy-ec2.md "../../../m2/latest/userguide/ba-deploy-ec2.md")
- [Deploy on containers on Amazon ECS and Amazon EKS](../../../m2/latest/userguide/ba-deploy-container.md "../../../m2/latest/userguide/ba-deploy-container.md")
- [Create an AWS Mainframe Modernization application](../../../m2/latest/userguide/applications-m2-create.md "../../../m2/latest/userguide/applications-m2-create.md")

## Step 5: Test the modernized

application

After deployment,

1. Review the available [Runtime APIs](../../../m2/latest/userguide/ba-runtime-endpoints.md "../../../m2/latest/userguide/ba-runtime-endpoints.md") for ways to interact with the modernized
   applications.
2. Test your application to align its functional equivalence with legacy
   application. For example, see [Test a sample
   application](../../../m2/latest/userguide/ba-runtime-test-planetsdemo.md "../../../m2/latest/userguide/ba-runtime-test-planetsdemo.md") in the _AWS Mainframe Modernization user
   guide_.

## Additional

example

For a specific example of modernizing mainframe application with AWS Transform, see [Modernize the CardDemo mainframe application](../../../prescriptive-guidance/latest/patterns/modernize-carddemo-mainframe-app-amazon-q-dev.md "../../../prescriptive-guidance/latest/patterns/modernize-carddemo-mainframe-app-amazon-q-dev.md").
