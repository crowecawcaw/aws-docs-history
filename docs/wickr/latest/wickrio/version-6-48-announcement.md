This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Version 6.48 announcement

Version 6.48 of the Bots docker image contains the upgrade to Node 20. If you are using any
bots, you will need to make the following modifications to them to ensure they work with this
latest bot version. Upgrading to the new version without completing these steps will disrupt the
functionality of your custom bots:

1.  If you are creating custom bots/integrations, you will need to update the integration to
    include the following changes:

        * Bump wickrio-bot-api version to 7.1.x. (If you have wickrio\_addon as a dependency, it
         should also be bumped to 7.1.x).
        * Remove occurrences of Node 16 usage.
        * Make changes to work with asynchronous APIs.

    This is an [example](https://github.com/WickrInc/wickrio-hello-world-bot/pull/36/files "https://github.com/WickrInc/wickrio-hello-world-bot/pull/36/files") of changes to be made to any custom integration to accommodate compatibility
    with version 6.48 (and later).

2.  If you are using any of the officially supported integrations, please make sure to upgrade
    your integrations to the latest version using `upgrade` command in Docker CLI. For
    more information, see [Upgrading bots](troubleshooting.md#upgrading-bots "troubleshooting.md#upgrading-bots").
    As of version 6.48, the Bots docker image has the following major changes:

3.  Upgraded to use Node 20 (previously used Node 16).
4.  Deprecated multiple integrations. This is the list of officially supported
    integrations:
    - wickrio-broadcast-bot
    - wickrio_web_interface_bot
    - wickrio-compliance-bot (only available for Enterprise environments)

5.  This is the list of sample integrations that can be pulled from NPM registry for testing
    purposes:
    1. @wickr-sample-integrations/wickrio-hello-world-bot
    2. @wickr-sample-integrations/wickrio-example-app
    3. @wickr-sample-integrations/wickrio-lex-bot
    4. @wickr-sample-integrations/wickrio-rekognition-bot
    5. @wickr-sample-integrations/wickrio-translation-bot

6.  The WickrIO addon has been updated to use ZeroMq to interact with WickrIO client,
    making the WickrIO APIs asynchronous.
