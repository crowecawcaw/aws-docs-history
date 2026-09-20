

# Generating dependency insights
<a name="next-gen-generating-insights"></a>

Next generation Resilience Hub analyzes up to 35 days of discovered dependency data to generate insights. You can generate insights from the console or by using the AWS CLI.

**To generate insights (console)**

Navigate to your service in the console and choose the **Dependencies** section. Then choose **Generate insights**. When insights already exist, choose **Generate insights** again to regenerate them.

**To generate insights (CLI)**

```
aws resiliencehubv2 start-dependency-insights \
  --service-arn "arn:aws:resiliencehub:us-east-1:123456789012:service/checkout:abc123"
```

The response returns the current generation `status`:

```
{
  "status": "IN_PROGRESS"
}
```

**Note**  
You can regenerate insights for a service once every 24 hours. Because new dependency data is summarized hourly, regenerating within the same day is unlikely to change the results. In the console, the **Generate insights** button is disabled until the rolling 24-hour window has passed.