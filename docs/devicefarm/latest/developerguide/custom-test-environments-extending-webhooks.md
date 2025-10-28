# Using Webhooks and other APIs after your tests run

in Device Farm

You can have Device Farm call a webhook after every test suite finishes using **curl**. The process
to do this varies with the destination and formatting. For your specific webhook, see the documentation for that
webhook. The following example posts a message each time a test suite has finished to a Slack webhook:

```
phases:
  post_test:
    - curl -X POST -H 'Content-type: application/json' --data '{"text":"Tests on '$DEVICEFARM_DEVICE_NAME' have finished!"}' `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`
```

For more information on using webhooks with Slack, see [Sending your first Slack message using
Webhook](https://api.slack.com/tutorials/slack-apps-hello-world "https://api.slack.com/tutorials/slack-apps-hello-world") in the Slack API reference.

For more ways to extend your test suite and optimize your tests, see [Extending custom test environments in Device Farm](custom-test-environments-extending.md "custom-test-environments-extending.md").

You are not limited to using **curl** to call webhooks. Test packages can include extra scripts
and tools, as long as they are compatible with the Device Farm execution environment. For example, your test package may
include auxiliary scripts that make requests to other APIs. Make sure that any required packages are installed
alongside your test suite's requirements. To add a script that runs after your test suite is complete, include the
script in your test package and add the following to your test spec:

```
phases:
  post_test:
    - `python post_test.py`
```

###### Note

Maintaining any API keys or other authentication tokens used in your test package is your responsibility. We
recommend that you keep any form of security credential out of source control, use credentials with the fewest
possible privileges, and use revokable, short-lived tokens whenever possible. To verify security requirements,
see the documentation for the third-party APIs that you use.

If you plan on using AWS services as a part of your test execution suite, you should use IAM temporary
credentials, generated outside of your test suite and included in your test package. These credentials should have
the fewest granted permissions and shortest lifespan possible. For more information on creating temporary
credentials, see [Requesting temporary security credentials](../../../IAM/latest/UserGuide/id_credentials_temp_request.md "../../../IAM/latest/UserGuide/id_credentials_temp_request.md") in the _IAM User
Guide_.

For more ways to extend your test suite and optimize your tests, see [Extending custom test environments in Device Farm](custom-test-environments-extending.md "custom-test-environments-extending.md").
