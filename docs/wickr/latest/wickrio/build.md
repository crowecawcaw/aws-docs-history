This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Build

Custom integrations in Wickr IO must be made available to the Wickr IO Docker
container as a tarball named `software.tar.gz`. You can build that tarball from
your source directory:

```

tar czf software.tar.gz —exclude=software.tar.gz .

```

Here's an example of what the output to this command will look like:

```

tar czf software.tar.gz —exclude=software.tar.gz .

tar: .: file changed as we read it

```

After you run this command, you will have the `software.tar.gz` file containing
your source code and dependencies for your bot. Upload it to the server where you want to
deploy your bot integration to continue on with the next deployment step.
