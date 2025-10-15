# How Git sync works with CloudFormation

This topic describes how Git sync works and introduces the key concepts required to work
 with it.

###### Topics

* [How Git sync works](#git-sync-concepts-terms-how "#git-sync-concepts-terms-how")
* [Comments on pull requests](#git-sync-comments-on-pull-requests "#git-sync-comments-on-pull-requests")
* [Stack deployment file](#git-sync-concepts-terms-depoyment-file "#git-sync-concepts-terms-depoyment-file")
* [CloudFormation template file](#git-sync-concepts-terms-template-file "#git-sync-concepts-terms-template-file")
* [Template definition
 repository](#git-sync-concepts-terms-template-definition-repository "#git-sync-concepts-terms-template-definition-repository")

## How Git sync works


To use Git sync, you first must connect a Git provider to CloudFormation using the [CodeConnections](https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html "https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html")
 service. In the procedures in this guide, the connection is created through the CodeConnections console.
 Alternatively, you can create the connection with the AWS CLI. You can use any of the following
 Git providers:



* [GitHub](https://github.com/ "https://github.com/")
* [GitHub Enterprise](https://github.com/enterprise/ "https://github.com/enterprise/")
* [GitLab](https://about.gitlab.com/ "https://about.gitlab.com/")
* [Bitbucket](https://bitbucket.org "https://bitbucket.org")
* [GitLab
 self-managed](https://docs.gitlab.com/subscriptions/self_managed/ "https://docs.gitlab.com/subscriptions/self_managed/")

Next, you create a CloudFormation template that defines your stack and add it to your
 repository. This template file is monitored. CloudFormation updates the stack automatically when
 changes are committed to it.


In the CloudFormation console, you create a new stack and choose **Sync from
 Git** to tell CloudFormation to use Git sync. You'll specify the repository and branch
 you want CloudFormation to monitor, and specify the CloudFormation template in your repository that
 defines the stack.


During configuration, you can either provide your own stack deployment file from your
 repository, or have Git sync generate one for you. The stack deployment file contains
 parameters and values that configure the resources in your stack. This stack deployment file
 is monitored. CloudFormation updates the stack automatically when changes are committed to
 it.


Git sync creates a pull request in your repository to sync your stack with the CloudFormation
 template file and stack deployment file. If Git sync generates the stack deployment file for
 you, it's submitted to your repository by Git sync.


You then merge the pull request to your repository so that CloudFormation provisions the
 stack, configures it with your deployment parameters, and begins monitoring your repository
 for changes.


From then on, whenever you make changes to your template file or stack deployment file and
 commit them to your repository, CloudFormation will automatically detect the changes. If your team
 uses pull requests, your team members can then review and approve the changes before they're
 deployed. Once the pull request is accepted, CloudFormation deploys your changes.


You can monitor the status of your Git sync configuration for the stack and see a history
 of commits applied to the stack in the CloudFormation console. The console also provides tools for
 reconfiguring Git sync and troubleshooting issues. 


## Comments on pull requests


You can choose to have CloudFormation create a summary of the code changes in pull requests
 through the CodeConnections service by turning on the **Enable comment on pull
 request** option in the console. Providing a summary of the changes in pull
 requests means that team members can easily review and understand the impact of the proposed
 modifications before merging the pull request. For more information, see [Enable CloudFormation to post a
 summary of stack changes in pull requests](gitsync-enable-comments-on-pull-requests.md "gitsync-enable-comments-on-pull-requests.md").


## Stack deployment file


A stack deployment file is a JavaScript Object Notation (JSON) or YAML standard formatted
 file that contains parameters and values that manage your CloudFormation stack. It is monitored
 for changes. When changes to the file are committed to the repository, the associated stack is
 automatically updated.


The stack deployment file contains a key-value pair and two dictionaries:



* `template-file-path`


This is the full repository path for the CloudFormation template file. The template file
 declares the resources for the CloudFormation stack associated with this deployment
 file.
* `parameters`


The parameters dictionary contains key-value pairs that configure the resources in the
 stack. A stack deployment file can have up to 50 parameters.
* `tags`


The tags dictionary contains optional key-value pairs that you can use to identify and
 categorize resources in the stack. A stack deployment file can have up to 50 tags.

You can provide your own stack deployment file, or have Git sync create one for you and
 automatically submit a pull request to your repository. You can manage the parameters and tags
 by editing the stack deployment file and committing changes to the repository.


The following is an example of a Git sync stack deployment file:



```
template-file-path: fargate-srvc/my-stack-template.yaml

parameters: 
    image: public.ecr.aws/lts/nginx:latest
    task_size: x-small
    max_capacity: 5
    port: 8080
    env: production
tags:
    cost-center: '123456'
    org: 'AWS'
```

## CloudFormation template file


A template file contains a declaration of the AWS resources that make up a CloudFormation
 stack. With Git sync, the template file is stored in your Git repository and referenced by
 the stack deployment file. You can manage the stack by editing the template file and
 committing changes to the repository.


For more information, see [Working with CloudFormation templates](template-guide.md "template-guide.md").


## Template definition
 repository


The template definition repository is the Git repository that is linked to CloudFormation
 through Git sync. The repository is monitored for changes to the CloudFormation template and
 stack deployment file. When you commit changes to the file, the associated stack is updated
 automatically.


###### Important

When you configure the template definition repository in the Git sync console, select
 the correct *repository* and *branch* from the Git
 connection. Git sync only monitors the configured repository and branch for changes to the
 CloudFormation template and the stack deployment file.
