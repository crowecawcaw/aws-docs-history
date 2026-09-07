

This guide provides documentation for Wickr IO Integrations. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Develop a custom Wickr IO integration on AWS Wickr
<a name="develop-new-integration"></a>

**High Level Overview**

![The Wickr IO overview image.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickrio-overview.png)


To customize your experience with integrations in AWS Wickr, Wickr IO offers a [JavaScript](https://github.com/WickrInc/wickrio-bot-api) library which makes it easy to develop your own bots. This document contains the process of creating a new integration, an “emoji bot,” which responds to messages with a random emoji.