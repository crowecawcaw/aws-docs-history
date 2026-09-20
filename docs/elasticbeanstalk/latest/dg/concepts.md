

# Understanding concepts in Elastic Beanstalk
<a name="concepts"></a>

Becoming familiar with the concepts and terms will help you gain an understanding needed for deploying your applications with Elastic Beanstalk.

Elastic Beanstalk offers two modes: Standard and Cluster. Beanstalk Standard runs applications directly on Amazon EC2. Beanstalk Cluster runs applications as containers on Amazon EKS. For a side-by-side comparison of the two modes, see [Differences from Beanstalk Standard](beanstalk-cluster-concepts.md#beanstalk-cluster-differences).

The following diagram depicts two Beanstalk Standard environments: one web server environment and one worker environment.

![Illustrative diagram showing the relationship between an Elastic Beanstalk application and web/worker environments.](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/aeb-overview.png)


The following diagram depicts two Beanstalk Cluster environments sharing an EKS cluster.

![Two Beanstalk Cluster environments for one Elastic Beanstalk application share a service-operated Amazon EKS cluster because they are in the same AWS account and use the same VPC subnet set. Each environment has an optional Application Load Balancer and isolated application replicas. Amazon EKS Auto Mode supplies shared node capacity.](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/aeb-overview-cluster.png)


## Application
<a name="concepts-application"></a>

An Elastic Beanstalk *application* is a logical grouping of Elastic Beanstalk components, including *environments*, *versions*, and *environment configurations*. Within an Elastic Beanstalk application, you manage all the resources relevant to running your code.

## Application version
<a name="concepts-version"></a>

In Elastic Beanstalk, an *application version* refers to a specific, labeled iteration of deployable code for a web application. An application version points to an Amazon Simple Storage Service (Amazon S3) object that contains the deployable code, such as a Java WAR file. 

An application version is part of an application. Applications can have many versions and each application version is unique. In a running environment, you can deploy any application version you already uploaded to the application, or you can upload and immediately deploy a new application version. For example, you could upload multiple application versions to test differences between them.

## Environment
<a name="concepts-environment"></a>

An *environment* is a collection of AWS resources running an application version. Each environment runs only one application version at a time, however, you can run the same application version or different application versions in many environments simultaneously. When you create an environment, Elastic Beanstalk provisions the resources needed in your AWS account to run the application version you specified.

## Environment tier
<a name="concepts-tier"></a>

When you launch an Elastic Beanstalk environment, you first choose an environment tier. The environment tier determines what resources Elastic Beanstalk provisions to support it. An application that runs directly on Amazon EC2 and serves HTTP requests runs in a [web server environment tier](concepts-webserver.md). A backend environment that runs directly on Amazon EC2 and pulls tasks from an Amazon Simple Queue Service (Amazon SQS) queue runs in a [worker environment tier](concepts-worker.md). An application that runs as containers on Amazon Elastic Kubernetes Service (Amazon EKS) runs in a cluster environment tier.

## Environment configuration
<a name="concepts-environmentconfig"></a>

 An *environment configuration* identifies a collection of parameters and settings that define how an environment and its associated resources behave. When you update an environment’s configuration settings, Elastic Beanstalk automatically applies the changes to existing resources or deletes and deploys new resources (depending on the type of change).

## Saved configuration
<a name="concepts-configuration"></a>

A *saved configuration* is a template that you can use as a starting point for creating unique environment configurations. You can create and modify saved configurations, and apply them to environments, using the Elastic Beanstalk console, EB CLI, AWS CLI, or API. The API and the AWS CLI refer to saved configurations as *configuration templates*.

## Platform
<a name="concepts-platform"></a>

A *platform* is a combination of an operating system, programming language runtime, web server, application server, and Elastic Beanstalk components. With Beanstalk Standard, you design and target your web application to a platform. Elastic Beanstalk provides a variety of platforms on which you can build your applications.

For details, see [Elastic Beanstalk platforms](concepts-all-platforms.md).