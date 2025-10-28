# Developing application code for App Runner

This chapter discusses runtime information and development guidelines that you should consider when developing or migrating application code for
deployment to AWS App Runner.

## Runtime information

Whether you provide a container image or App Runner builds one for you, App Runner runs your application code in a container instance. Here are a few key aspects
of the container instance runtime environment.

- Framework support – App Runner supports any image that implements a web application. It's agnostic to the
  programming language that you choose and to the web application server or framework that you use, if you use any. For your convenience, we provide
  platform-specific managed runtimes for various programming platforms, to streamline the application build process and abstract image creation.
- Web requests – App Runner provides support for HTTP 1.0 and HTTP 1.1 to the container instances. For more information about
  configuring your service, see [Configuring an App Runner service](manage-configure.md "manage-configure.md"). You don't need to implement handling of HTTPS secure traffic. App Runner redirects all
  incoming HTTP requests to corresponding HTTPS endpoints. You don't need to configure any settings to enable redirecting the HTTP web requests. App Runner terminates the TLS before passing requests to your application container instance.

###### Note

    + There is a total of 120 seconds request timeout limit on the HTTP requests.
     The 120 seconds include the time the application takes to read the request, including the body, and complete writing the HTTP response.
    + The request read and response timeout limit is contingent on the applications that you use. These applications may have their own internal
     timeouts, such as the HTTP server for Python, Gunicorn, has a 30 second default timeout limit. In such cases, the application's timeout limit overrides
     the App Runner 120 second timeout limit.
    + You don't need to configure TLS cipher suites or any other parameters as App Runner being a fully managed service, manages the TLS termination for
     you.

- Stateless apps – Currently App Runner doesn't support a stateful app. Hence, App Runner doesn't guarantee state
  persistence beyond the duration of processing a single incoming web request.
- Storage – App Runner automatically scales the instances up or down for your App Runner application in accordance to incoming traffic volume.
  You can configure [Auto scaling options](manage-autoscaling.md "manage-autoscaling.md") for your App Runner application.
  Since the number of currently active instances processing the web requests is based on the incoming traffic volume, App Runner cannot guarantee that
  the files can persist beyond the processing of a single request. Hence, App Runner implements the file system in your container instance as ephemeral storage, which entails that the files are transient.
  For example, the files don't persist when you pause and resume your App Runner service.

App Runner provides you with 3 GB of ephemeral storage and uses a part of the 3 GB of ephemeral storage for its pulled, compressed, and the uncompressed container image on the instance.
The remaining ephemeral storage can be used by your App Runner service. However, this is _not a permanent storage_ owing to its stateless nature.

###### Note

There could be scenarios when the storage files do persist across requests. For example, if the next request lands on the same instance the storage files will persist.
The persistence of storage files across requests can be useful in
certain situations. For example, when handling a request, you can cache files that your application downloads if future requests might need them.
This might speed up future request handling, but can't guarantee the speed gains. Your code shouldn't assume that a file that has been downloaded in
a previous request still exists.

For guaranteed caching using a high throughput, low latency in-memory data store, use a service such as [Amazon ElastiCache](https://aws.amazon.com/elasticache/ "https://aws.amazon.com/elasticache/").

- Environment variables –
  By default, App Runner makes the `PORT` environment variable available in your
  container instance. You can configure the variable value with port information, and add custom environment variables and values. You can also
  reference sensitive data stored in _AWS Secrets Manager_ or _AWS Systems Manager Parameter Store_ as environment variables. For more
  information about creating environment variables, see [Referencing environment variables](env-variable.md "env-variable.md").
- Instance role – If your application code makes calls to any AWS services, using the service APIs or one of
  the AWS SDKs, create an instance role using AWS Identity and Access Management (IAM). Then, attach it to your App Runner service when you create it. Include all AWS service
  action permissions that your code requires in your instance role. For more information, see [Instance role](security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service.instance "security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service.instance").

## Code development guidelines

Consider these guidelines when developing code for an App Runner web application.

- Patching container images – When providing container images,
  you are responsible for regularly updating and patching these images. While App Runner manages the
  infrastructure, you should ensure the security and up-to-date status of the provided container images. For more information,
  see the [AWS App Runner Documentation](security-shared-responsibility.md#security-shared-responsibility.patch-images "security-shared-responsibility.md#security-shared-responsibility.patch-images")
- Design stateless code – Design the web
  application you deploy to your App Runner service to be stateless. Your code should assume that
  no state persists beyond the duration of processing a single incoming web request.
- Delete temporary files – When you create files, they're stored on a file system, and take up part of the
  storage allocation of your service. To avoid out-of-storage errors, don't keep temporary files for extended periods. Balance storage size with request
  handling speed when making file caching decisions.
- Instance startup – App Runner provides five minutes of instance startup time.
  Your instance must listen for requests on their configured listening ports and be healthy within five minutes of their startup. During the startup time,
  App Runner instances are allocated virtual CPU (vCPU) based on your vCPU configuration.
  For more information about available vCPU configuration, see [App Runner supported configurations](architecture.md#architecture.vcpu-memory "architecture.md#architecture.vcpu-memory").

After the instance successfully starts up, it goes into an idle state and waits for requests.
You pay based on the instance startup duration, with the minimum charge of one minute per instance start.
For information about pricing, see [AWS App Runner pricing](https://aws.amazon.com/apprunner/pricing "https://aws.amazon.com/apprunner/pricing").
