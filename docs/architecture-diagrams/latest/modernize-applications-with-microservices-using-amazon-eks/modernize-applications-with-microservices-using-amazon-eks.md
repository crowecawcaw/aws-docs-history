# Modernize Applications with Microservices Using Amazon EKS

Publication date: **July 24, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture enables you to integrate Amazon Elastic Kubernetes Service (Amazon EKS) with VMware Cloud on AWS. Use AWS DevOps tools to accelerate
application modernization.

## Modernize Applications with Microservices Using Amazon EKS Diagram

![Reference architecture diagram showing how to integrate Amazon EKS with VMware Cloud on AWS.](images/modernize-applications-with-microservices-using-amazon-eks.png)

1. The Elastic Network Interface is automatically attached to the **Amazon Elastic Compute Cloud**
   (Amazon EC2) bare metal (ESXi) hosts in VMware Cloud on AWS during the software-defined data center (SDDC) provisioning.
2. Provision fully managed **Amazon Elastic Kubernetes Service** (Amazon EKS) clusters for different
   environments (dev/test/production).
3. Use tools such as **AWS App2Container** (App2Container) to accelerate
   refactoring/rearchitecting applications into containerized microservices. Use
   **Amazon EKS** to manage and automate the testing and deployment
   of container workloads.
4. Transform and containerize legacy systems to modern applications with minimal
   disruptions. The existing database tier can keep running on **VMware Cloud on AWS**
   to avoid the complexity and delay of database migrations.
5. **Network Load Balancer** integrates with the Kubernetes Ingress
   Controller, providing a secure and consistent approach for exposing applications.
6. **Amazon Route 53** resolves incoming requests to
   **Network Load Balancer** in the primary AWS Region.
7. The dev team commits code to an **AWS CodeCommit** repository, which
   initiates **AWS CodePipeline** to start processing the code changes through the pipeline.
8. **AWS CodeBuild** packages the code changes and dependencies and builds a Docker image.
9. The new Docker image is pushed to **Amazon Elastic Container Registry** (Amazon ECR).
10. **CodeBuild** uses a Kubectl command line tool to invoke
    Kubernetes API and update the image tag for the microservice deployment.
11. Kubernetes performs a rolling update of the pods in the application deployment
    according to the new docker image specified in **Amazon ECR**.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/modernize-applications-with-microservices-using-amazon-eks.md "samples/modernize-applications-with-microservices-using-amazon-eks.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Contributors

Contributors to this reference architecture diagram include:

- Sheng Chen, Senior Migration Solutions Architect, VMware Cloud on AWS
- Jyothi Goudar, Manager Partner Solutions Architect, Amazon Web Services

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date           |
| ------------------- | ----------------------------------------------- | -------------- |
| Diagram update      | Diagram reviewed and updated for freshness      | July 24, 2023  |
| Initial publication | Reference architecture diagram first published. | April 12, 2021 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
