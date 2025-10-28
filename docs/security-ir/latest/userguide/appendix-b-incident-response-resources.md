# Appendix B: AWS incident response resources

AWS publishes resources to assist customers with developing incident response capabilities. Most example code and procedures can be found at the AWS
external GitHub public repository. Following are some resources that provide examples of how to perform incident response.

## Playbook resources

- [Framework for Incident Response Playbooks](https://github.com/aws-samples/aws-customer-playbook-framework "https://github.com/aws-samples/aws-customer-playbook-framework") -
  An example framework for customers to create, develop, and integrate security playbooks in preparation for potential attack scenarios when using AWS services.
- [Incident Response Playbook Samples](https://github.com/aws-samples/aws-incident-response-playbooks "https://github.com/aws-samples/aws-incident-response-playbooks") -
  Playbooks covering common scenarios faced by AWS customers.
- [AWS
  CIRT announces the release of five publicly available workshops](https://aws.amazon.com/blogs/security/aws-cirt-announces-the-release-of-five-publicly-available-workshops/ "https://aws.amazon.com/blogs/security/aws-cirt-announces-the-release-of-five-publicly-available-workshops/").

## Forensic resources

- [Automated Incident Response and Forensics Framework](https://github.com/awslabs/aws-automated-incident-response-and-forensics "https://github.com/awslabs/aws-automated-incident-response-and-forensics") – This
  framework and solution provides a standard digital forensic process, consisting of the following phases: containment, acquisition, examination, and analysis.
  It leverages AWS Λ functions to trigger the incident response process in an automated repeatable way. It provides segregation of accounts to operate
  the automation steps, store artifacts and create forensic environments.
- [Automated Forensics Orchestrator for Amazon EC2](https://aws.amazon.com/solutions/implementations/automated-forensics-orchestrator-for-amazon-ec2/ "https://aws.amazon.com/solutions/implementations/automated-forensics-orchestrator-for-amazon-ec2/")
  – This implementation guide provides a self-service solution to capture and examine data from EC2 instances and attached volumes for forensic analysis in the event
  of a potential security issue being detected. There is an AWS CloudFormation template to deploy the solution.
- [How to automate forensic disk collection in AWS](https://aws.amazon.com/blogs/security/how-to-automate-forensic-disk-collection-in-aws/ "https://aws.amazon.com/blogs/security/how-to-automate-forensic-disk-collection-in-aws/")
  – This AWS blog details how to set up an automation workflow to capture the disk evidence for analysis in order to determine the scope and the impact of
  potential security incidents. There is also an AWS CloudFormation template included to deploy the solution.
