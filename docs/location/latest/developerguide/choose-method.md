# Choose an authentication method

API keys and Amazon Cognito are used in similar ways for similar scenarios, so why would you
choose one instead of the other? The following list highlights some of the differences
between the two.

- **Performance:**
  - **API key:** Relatively faster
  - **Amazon Cognito:** Relatively slower

- **Availability:**
  - **API key:** Amazon Location APIs for Maps,
    Places, and Routes
  - **Amazon Cognito:** All APIs

- **Combines with another authentication method?**

      + **API key:** No
      + **Amazon Cognito:** Yes

  **Comparison**

- API keys are available only for maps, places, and routes actions. Amazon Cognito can be
  used to authenticate access to most Amazon Location Service APIs.
- The performance of map requests with API keys is typically faster than similar
  scenarios with Amazon Cognito. Simpler authentication means fewer round trips to the
  service and cached requests when getting the same map tile again in a short time
  period.
- With Amazon Cognito, you can use your own authentication process or combine multiple
  authentication methods, using Amazon Cognito Federated Identities.

For more information, see [Getting Started with Federated Identities](../../../cognito/latest/developerguide/getting-started-with-identity-pools.md "../../../cognito/latest/developerguide/getting-started-with-identity-pools.md") in the
Amazon Cognito Developer Guide.
