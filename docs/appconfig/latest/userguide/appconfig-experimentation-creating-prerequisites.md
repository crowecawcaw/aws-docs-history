

# Step 1: Configuring prerequisites
<a name="appconfig-experimentation-creating-prerequisites"></a>

Before you begin, complete the following tasks:

1. **Deploy the feature flag you want to experiment on**: Before you can run an experiment on a feature flag, the flag must be deployed to the environment where you want to run the experiment.

1. **[Install and configure AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent.html)**: AWS AppConfig experimentation requires AWS AppConfig Agent to deliver treatments to users. Experimentation requires AWS AppConfig Agent Lambda extension version 2.0.20159 or later, or Amazon ECS/Amazon EC2 agent version 2.0.175233 or later. The following topics describe how to install and configure AWS AppConfig Agent for each supported compute environment:
   + [Using AWS AppConfig Agent with AWS Lambda](appconfig-integration-lambda-extensions.md)
   + [Using AWS AppConfig Agent with Amazon EC2 and on-premises machines](appconfig-integration-ec2.md)
   + [Using AWS AppConfig Agent with Amazon ECS and Amazon EKS](appconfig-integration-containers-agent.md)

   Note that each section includes information about configuring IAM permissions so the agent can retrieve feature flags and other configuration data.

1. [Configure experiment assignment logging](appconfig-experimentation-about-data-collection.md): To capture treatment assignment data during an experiment run, set the `EXPERIMENT_ASSIGNMENT_LOG_DESTINATION` agent option (Lambda: `AWS_APPCONFIG_EXTENSION_EXPERIMENT_ASSIGNMENT_LOG_DESTINATION`) to `stderr` or to a disk path such as `file:/var/log/appconfig/experiments/`.