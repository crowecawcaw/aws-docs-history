

# Retrieving experiment treatments
<a name="appconfig-integration-retrieving-experiment-treatments"></a>

When an experiment runs on a feature flag, you retrieve the assigned treatment the same way you retrieve any feature flag from AWS AppConfig Agent. This requires two additions: you identify the entity, and you provide the caller context that your experiment audience rule evaluates.

1. Retrieve the flag from AWS AppConfig Agent.

1. Specify the exact flag or flags for which you want treatments by using the `?flag={{FLAG_KEY}}` query parameter.

1. Provide an entity identifier, such as an end-user ID, in the `Entity-Id` header. The agent returns the same treatment for the same entity for the life of the run.

1. Pass the request context that your experiment audience rule evaluates in the `Context` header.

For example, to discover which treatment `user123` is assigned to for an experiment running on the `inference-settings` flag, make this request:

```
curl "http://localhost:2772/applications/MyApp/environments/MyEnv/configurations/MyFlags?flag=inference-settings" \
-H "Entity-Id: user123"
```

If `user123` is assigned to treatment `t1`, the agent returns a response like the following:

```
{
  "_variant": "__t1__",
  "enabled": true
}
```

The `_variant` field identifies the flag variant assigned to the entity. When you start an experiment, AWS AppConfig maps each treatment to a flag variant that is named for the assigned treatment (`__c__` for the control and `__t1__`, `__t2__`, and so on for treatments). If the treatment defines attribute values, they also appear in the response.

**Note**  
If the entity is not part of the experiment audience, or is part of the audience but is not currently exposed to the experiment (based on the experiment exposure percentage), the agent does not return an experiment treatment. Instead, it falls through to the flag value currently deployed to the environment.