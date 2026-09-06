

# Build and deploy your modernized application post-refactoring
<a name="transform-app-mainframe-workflow-build-deploy"></a>

After you complete the refactoring process with AWS Transform, you can build and deploy your modernized Java application. This guide walks you through retrieving your modernized code, configuring your environment, and deploying and testing your application.

**Note**  
In addition to the guidance provided here, the AWS Transform generated code package will include an *Set up the AWS Automated Refactor Development Environment* document which provides instructions to set up a IDE (Integrated Development Environment) with [Developer Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-options.html#ba-runtime-options-developer).

**Topics**
+ [Prerequisites](#transform-app-mainframe-workflow-build-deploy-prerequisites)
+ [Step 1: Retrieve the modernized code](#transform-app-mainframe-workflow-build-deploy-retrieve)
+ [Step 2: Build the modernized application](#transform-app-mainframe-workflow-build-deploy-build)
+ [Step 3: Configure the test environment](#transform-app-mainframe-workflow-build-deploy-configure)
+ [Step 4: Deploy the modernized application](#transform-app-mainframe-workflow-build-deploy-deployment)
+ [Step 5: Test the modernized application](#transform-app-mainframe-workflow-build-deploy-test)
+ [Additional example](#transform-app-mainframe-workflow-build-deploy-examples)

## Prerequisites
<a name="transform-app-mainframe-workflow-build-deploy-prerequisites"></a>

Before you begin, make sure you have:
+ Successfully completed a refactoring job with AWS Transform.
+ Access to your modernized code.
+ Installed and configured build software tool stack on your development machine, such as [Apache Maven](https://maven.apache.org/index.html) or [Apache Tomcat](https://tomcat.apache.org/). For more information on Runtime versioning, see [AWS Transform for mainframe Runtime release notes](https://docs.aws.amazon.com/m2/latest/userguide/ba-release-notes.html).
+ Installed and configured Amazon Corretto or a version of Java runtime. For more information on installing Amazon Corretto, see [Amazon Corretto 24](https://docs.aws.amazon.com/corretto/latest/corretto-24-ug/what-is-corretto-24.html).
+ Access to create and configure Amazon Aurora PostgreSQL databases for Runtime components, if necessary. For more information on Creating the Aurora PostgreSQL database, see [Working with Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html).
+ Administrative access to deploy applications to your runtime environment.
+ Reviewed the [AWS Transform for mainframe Runtime concepts](https://docs.aws.amazon.com/m2/latest/userguide/ba-shared-concept.html) for fundamental concepts on applications modernized with AWS automated refactoring solution.

## Step 1: Retrieve the modernized code
<a name="transform-app-mainframe-workflow-build-deploy-retrieve"></a>

To retrieve the modernized code

1. Download and extract the generated code package.

1. Open `codebase/app-pom/pom.xml` and note the required runtime engine version. For example `<gapwalk.version>4.6.0</gapwalk.version>`.

1. Locate the *Set up the AWS Automated Refactor Development Environment* document from the downloaded code package for reference.

## Step 2: Build the modernized application
<a name="transform-app-mainframe-workflow-build-deploy-build"></a>

To build your modernized application

1. Access the Runtime from the AWS Transform for mainframe Toolbox.

1. Download and install the appropriate runtime version (identified in [Step 1: Retrieve the modernized code](#transform-app-mainframe-workflow-build-deploy-retrieve)) on your local development machine.
**Note**  
Additional information for installing the runtime dependencies on your local machine is available in section 3.1 of the *Set up the AWS Automated Refactor Development Environment* document.

1. Open the command prompt and navigate to your application's root directory.

1. To build deployable packages for the modernized application run the Maven build command:

   ```
   mvn package
   ```

   Refer to the [Application Organization ](https://docs.aws.amazon.com/m2/latest/userguide/ba-shared-structure.html#ba-shared-structure-org) page for details on the basic organization of the modernized code. For instance, for modernized application containing a front-end web application, you may expect at-least the following deployable `.war` aggregates in addition to the runtime components: 
   + **Service project**: Contains legacy business logic modernization elements

     ```
     <business-app>-service.*.war
     ```
   + **Web project**: Contains the modernization of user interface-related elements 

     ```
     <business-app>-web.*.war
     ```

## Step 3: Configure the test environment
<a name="transform-app-mainframe-workflow-build-deploy-configure"></a>

To configure your test environment

1. Configure your modernized application runtime. For more information, see the [Set up configuration for Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-config.html) section in the *AWS Mainframe Modernization user guide*.
**Note**  
Refer section 5 of the *Set up the AWS Automated Refactor Development Environment* guide for runtime component specific configuration examples.

1. Prepare input and output (I/O) data sets for modernized applications. Modernized applications may process sequential I/O data sets, VSAM data sets, or others. 
**Note**  
Refer section 6 of the *Set up the AWS Automated Refactor Development Environment* for examples.

1. A runtime environment - You can use your existing runtime environment or create a new runtime environment.
   + To configure a non-managed runtime environment, see [Set up a non-managed application](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-setup.html).
   + To configure a managed runtime environment, see [Set up a managed application](https://docs.aws.amazon.com/m2/latest/userguide/ba-app-config.html).

After configuring the test environment, you move to the next step of deploying the modernized application.

## Step 4: Deploy the modernized application
<a name="transform-app-mainframe-workflow-build-deploy-deployment"></a>

Deploy the application artifacts in the runtime you created and/or configured in the [Step 2: Build the modernized application](#transform-app-mainframe-workflow-build-deploy-build) and [Step 3: Configure the test environment](#transform-app-mainframe-workflow-build-deploy-configure) sections.

Additional guidance for deploying the modernized application can be found using these links:
+ [Deploy on Amazon EC2](https://docs.aws.amazon.com/m2/latest/userguide/ba-deploy-ec2.html)
+ [Deploy on containers on Amazon ECS and Amazon EKS](https://docs.aws.amazon.com/m2/latest/userguide/ba-deploy-container.html)
+ [Create an AWS Mainframe Modernization application](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-create.html)

## Step 5: Test the modernized application
<a name="transform-app-mainframe-workflow-build-deploy-test"></a>

After deployment,

1. Review the available [Runtime APIs](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-endpoints.html) for ways to interact with the modernized applications.

1. Test your application to align its functional equivalence with legacy application. For example, see [Test a sample application](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-test-planetsdemo.html) in the *AWS Mainframe Modernization user guide*.

## Additional example
<a name="transform-app-mainframe-workflow-build-deploy-examples"></a>

For a specific example of modernizing mainframe application with AWS Transform, see [Modernize the CardDemo mainframe application](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-carddemo-mainframe-app-amazon-q-dev.html).