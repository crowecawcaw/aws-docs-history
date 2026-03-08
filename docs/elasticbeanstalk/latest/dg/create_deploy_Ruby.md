# Deploying Ruby applications with Elastic Beanstalk

This chapter provides instructions for configuring and deploying your Ruby web application to AWS Elastic Beanstalk. Elastic Beanstalk makes it easy to deploy,
manage, and scale your Ruby web applications using Amazon Web Services.

You can deploy your application in just a few minutes using the Elastic Beanstalk Command Line Interface (EB CLI) or by using the Elastic Beanstalk console. After you deploy
your Elastic Beanstalk application, you can continue to use the EB CLI to manage your application and environment, or you can use the Elastic Beanstalk console, AWS CLI, or the
APIs.

This chapter also provides step-by-step instructions for deploying a sample application to Elastic Beanstalk using the EB CLI, and then updating the application to
use the [Rails](http://rubyonrails.org/ "http://rubyonrails.org/") and [Sinatra](http://www.sinatrarb.com/ "http://www.sinatrarb.com/") web application frameworks.

The topics in this chapter assume that you have some knowledge of Elastic Beanstalk environments. If you
haven't used Elastic Beanstalk before, try the [getting started
tutorial](GettingStarted.md "GettingStarted.md") to learn the basics.

###### Topics

- [Setting up your Ruby development environment for Elastic Beanstalk](ruby-development-environment.md "ruby-development-environment.md")
- [Using the Elastic Beanstalk Ruby platform](create_deploy_Ruby.md "create_deploy_Ruby.md")
- [Deploying a rails application to Elastic Beanstalk](ruby-rails-tutorial.md "ruby-rails-tutorial.md")
- [Deploying a sinatra application to Elastic Beanstalk](ruby-sinatra-tutorial.md "ruby-sinatra-tutorial.md")
- [Adding an Amazon RDS DB instance to your Ruby Elastic Beanstalk environment](create_deploy_Ruby.md "create_deploy_Ruby.md")
