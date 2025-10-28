# Installing packages with a Gemfile on Elastic Beanstalk

To use RubyGems to install packages that your application requires, include a `Gemfile` file in the root of your project source.

###### Example Gemfile

```
source "https://rubygems.org"
gem 'sinatra'
gem 'json'
gem 'rack-parser'
```

When a `Gemfile` file is present, Elastic Beanstalk runs `bundle install` to install dependencies. For more information, see the
[Gemfiles](https://bundler.io/man/gemfile.5.html "https://bundler.io/man/gemfile.5.html") and [Bundle](https://bundler.io/man/bundle.1.html "https://bundler.io/man/bundle.1.html") pages on the
Bundler.io website.

###### Note

You can use a different version of Puma besides the default that's pre-installed with the Ruby platform. To do so, include an entry in a
`Gemfile` that specifies the version. You can also specify a different application server, such as Passenger, by using a
customized `Gemfile`.

For both of these cases you're required to configure a `Procfile` to start the
application server.

For more information see _[Configuring the application process with a Procfile](ruby-platform-procfile.md "ruby-platform-procfile.md")\*\*._
