# Buildfile and Procfile

Some platforms allow you to customize how you build or prepare your application, and to specify the processes that run your application. Each
individual platform topic specifically mentions _Buildfile_ and/or _Procfile_ if the platform supports them. Look
for your specific platform under [Elastic Beanstalk platforms](concepts-all-platforms.md "concepts-all-platforms.md").

For all supporting platforms, syntax and semantics are identical, and are as described on this page. Individual platform topics mention specific usage
of these files for building and running applications in their respective languages.

## Buildfile

To specify a custom build and configuration command for your application, place a file named `Buildfile` in the root directory of
your application source. The file name is case sensitive. Use the following syntax for your `Buildfile`.

```
`<process_name>`: `<command>`
```

The command in your `Buildfile` must match the following regular expression: `^[A-Za-z0-9_-]+:\s*[^\s].*$`

Elastic Beanstalk doesn't monitor the application that is run with a `Buildfile`. Use a `Buildfile` for commands that run
for short periods and terminate after completing their tasks. For long-running application processes that should not exit, use a [Procfile](#platforms-linux-extend.proc "#platforms-linux-extend.proc").

All paths in the `Buildfile` are relative to the root of the source bundle. In the following example of a
`Buildfile`, `build.sh` is a shell script located at the root of the source bundle.

###### Example Buildfile

```
make: ./build.sh
```

If you want to provide custom build steps, we recommend that you use `predeploy` platform hooks for anything but the simplest
commands, instead of a `Buildfile`. Platform hooks allow richer scripts and better error handling. Platform hooks are described in
the next section.

## Procfile

To specify custom commands to start and run your application, place a file named `Procfile` in the root directory of your
application source. The file name is case sensitive. Use the following syntax for your `Procfile`. You can specify one or more
commands.

```
`<process_name1>`: `<command1>`
`<process_name2>`: `<command2>`
...
```

Each line in your `Procfile` must match the following regular expression: `^[A-Za-z0-9_-]+:\s*[^\s].*$`

Use a `Procfile` for long-running application processes that shouldn't exit. Elastic Beanstalk expects processes run from the
`Procfile` to run continuously. Elastic Beanstalk monitors these processes and restarts any process that terminates. For short-running
processes, use a [Buildfile](#platforms-linux-extend.build "#platforms-linux-extend.build").

All paths in the `Procfile` are relative to the root of the source bundle. The following example `Procfile`
defines three processes. The first one, called `web` in the example, is the _main web application_.

###### Example Procfile

```
web: `bin/myserver`
cache: `bin/mycache`
foo: `bin/fooapp`
```

Elastic Beanstalk configures the proxy server to forward requests to your main web application on port 5000, and you can configure this port number. A common
use for a `Procfile` is to pass this port number to your application as a command argument. For details about proxy configuration,
see [Reverse proxy configuration](platforms-linux-extend.md "platforms-linux-extend.md").

Elastic Beanstalk captures standard output and error streams from `Procfile` processes in log files. Elastic Beanstalk names the log files after the
process and stores them in `/var/log`. For example, the `web` process in the preceding example generates logs named
`web-1.log` and `web-1.error.log` for `stdout` and `stderr`, respectively.
