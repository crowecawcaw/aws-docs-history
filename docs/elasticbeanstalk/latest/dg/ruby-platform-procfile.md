# Configuring the application process with a Procfile on Elastic Beanstalk.

To specify the command that starts your Ruby application, include a file called `Procfile` at the root of your source
bundle.

###### Note

Elastic Beanstalk doesn't support this feature on Amazon Linux AMI Ruby platform branches (preceding Amazon Linux 2). Platform branches with names containing _with
Puma_ or _with Passenger_, regardless of their Ruby versions, precede Amazon Linux 2 and don't support the
`Procfile` feature.

For details about writing and using a `Procfile`,
see [Buildfile and Procfile](platforms-linux-extend.md "platforms-linux-extend.md").

When you don't provide a `Procfile`, Elastic Beanstalk generates a default `Procfile`. If your `Gemfile`
includes Puma, Elastic Beanstalk assumes you want to use your provided version of Puma and generates the following default `Procfile`.

```
web: bundle exec puma -C /opt/elasticbeanstalk/config/private/pumaconf.rb
```

If your `Gemfile` does not include Puma, Elastic Beanstalk assumes you're using the pre-installed Puma application server and generates
the following default `Procfile`. On Amazon Linux 2 Ruby platform branches, Elastic Beanstalk always generates the following default
`Procfile` if you don't provide a `Procfile`.

```
web: puma -C /opt/elasticbeanstalk/config/private/pumaconf.rb
```

###### Note

On [October 10, 2024](../relnotes/release-2024-10-10-al2-10-2024-retire.md "../relnotes/release-2024-10-10-al2-10-2024-retire.md"),
the last Ruby Amazon Linux 2 platform branches were retired. All currently [supported Ruby platform branches](../platforms/platforms-supported.md#platforms-supported.ruby "../platforms/platforms-supported.md#platforms-supported.ruby") are based on Amazon Linux 2023.
For information about migration, see [Migration from Amazon Linux 2 to Amazon Linux 2023](using-features.migration-al.generic.md "using-features.migration-al.generic.md").

If you want to use the Passenger application server, use the following example files to configure your Ruby environment to install and use
Passenger.

1. Use this example file to install Passenger.

###### Example Gemfile

```
source 'https://rubygems.org'
gem 'passenger'
```

2. Use this example file to instruct Elastic Beanstalk to start Passenger.

###### Example Procfile

```
web: bundle exec passenger start /var/app/current --socket /var/run/puma/my_app.sock
```

###### Note

You don't have to change anything in the configuration of the nginx proxy server to use Passenger. To use other application servers, you might need
to customize the nginx configuration to properly forward requests to your application.
