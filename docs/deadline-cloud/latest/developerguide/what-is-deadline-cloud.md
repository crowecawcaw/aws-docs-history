# What is AWS Deadline Cloud?

AWS Deadline Cloud is a fully-managed AWS service that enables you to have a scalable processing
farm up and running in minutes. It provides an administration console for managing users, farms,
queues for scheduling jobs, and fleets of workers that do the processing.

This developer guide is for pipeline, tools, and applications developers with
use cases including the following:

- Pipeline developers and technical directors can integrate Deadline Cloud APIs and features into
  their custom production pipelines.
- Independent software vendors can integrate Deadline Cloud into their applications, enabling users
  to submit Deadline Cloud jobs from their workstations or web interfaces.
- Data scientists and engineers can distribute compute-intensive workloads such as scientific
  simulations, financial modeling, machine learning training, and data processing across scalable
  fleets of workers.
- Web and cloud-based service developers can integrate Deadline Cloud processing into their
  platforms, enabling customers to submit and track jobs on demand.
  This developer guide covers job bundles, submitters, customer-managed fleets, and
  integrations with the Deadline Cloud API, AWS Command Line Interface (AWS CLI), and SDKs. If you submit and monitor jobs from
  a digital content creation (DCC) application, see the [AWS Deadline Cloud User Guide](../userguide/what-is-deadline-cloud.md "../userguide/what-is-deadline-cloud.md").
  The User Guide also covers setting up farms, queues, users, and budgets in the console. Each
  topic is documented once, in the guide for its audience. The other guide links to it.

We provide tools that enable you to work directly with any step of your pipeline:

- A command-line interface that you can use directly or from scripts.
- The AWS SDK for 11 popular programming languages.
- A REST-based web interface that you can call from your applications.
  You can also use other AWS services in your custom applications. For example, you can
  use:

- **AWS CloudFormation** to automate creating and removing farms, queues,
  and fleets.
- **Amazon CloudWatch** to gather metrics for jobs.
- **Amazon Simple Storage Service** to store and manage digital assets and job
  output.
- **AWS IAM Identity Center** to manage users and groups for your
  farms.

## Open Job Description

Deadline Cloud uses the Open Job Description (OpenJD) specification to specify the details of a job.
OpenJD was developed to define jobs that are portable between solutions. You use it to define a
job that is a set of commands that run on worker hosts. For more information, see the [OpenJD specification](https://github.com/OpenJobDescription/openjd-specifications "https://github.com/OpenJobDescription/openjd-specifications")
on the GitHub website.

You can create an OpenJD job template using a submitter that Deadline Cloud provides, or you can use
any tool that you want to create the template. After creating the template, you send it to Deadline Cloud.
If you use a submitter, it takes care of sending the template. If you created the template
another way, you call a Deadline Cloud command-line action, or you can use one of the AWS SDKs to send
the job. Either way, Deadline Cloud adds the job to the specified queue and schedules the work.
