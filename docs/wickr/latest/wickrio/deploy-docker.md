This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Step 3: Deploy and configure the Docker container

Complete the following procedure to deploy and configure the Docker container.

1. Start the Docker image on your host:

```
`docker run -v ~/WickrIO:/opt/WickrIO -ti public.ecr.aws/x3s2s6k3/wickrio/bot-cloud:latest`
```

2. Select your preference for the welcome message.

![The Wickr IO welcome message prompt.](images/wickrio-welcome-message-prompt.png)
