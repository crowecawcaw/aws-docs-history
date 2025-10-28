# Release: AWS Elastic Beanstalk console support for Network Load Balancer on October 10, 2018

Elastic Beanstalk added support for configuring a Network Load Balancer and made
Application Load Balancer the default Elastic Load Balancing load balancer type when you enable load balancing with the Elastic Beanstalk console.

**Release date:** October 10, 2018

## Changes

Starting with today's release, when you use the AWS Elastic Beanstalk console to add a load balancer to your environment, you can choose an additional
load balancer type—Network Load Balancer. Previously, the console supported only Classic Load Balancer and Application Load Balancer, and you could
choose and configure a Network Load Balancer only by using configuration options through .ebextensions configuration files or the Elastic Beanstalk
API.

As a result, you can now use the console to choose and configure all three types of load balancer, with the same functionality that is available
through configuration options.

In addition, when you previously used the AWS Elastic Beanstalk console to enable load balancing for an environment, the default option was a Classic Load Balancer,
the previous-generation Elastic Load Balancing load balancer. Starting with today's release, Application Load Balancer is the default option.

For more information about load balancing in Elastic Beanstalk, see [Load Balancer for Your AWS Elastic Beanstalk
Environment](../dg/using-features.managing.md "../dg/using-features.managing.md") in the _AWS Elastic Beanstalk Developer Guide_.
