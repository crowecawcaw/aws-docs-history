# Configuring custom start commands with a Procfile on Elastic Beanstalk

You can include a file that's called `Procfile` at the root of your source bundle to specify the command that starts your
application.

###### Example Procfile

```
web: node index.js
```

For information about `Procfile` usage see [Buildfile and Procfile](platforms-linux-extend.md "platforms-linux-extend.md").

###### Note

This feature replaces the legacy `NodeCommand` option in the `aws:elasticbeanstalk:container:nodejs`
namespace.
