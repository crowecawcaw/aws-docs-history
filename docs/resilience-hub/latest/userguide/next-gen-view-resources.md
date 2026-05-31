# View discovered resources

###### To view resources (console)

1. Open the Next generation Resilience Hub console and navigate to your service.
2. Choose **Service topology**.
3. The resources graph and resources list show all discovered resources with their type, Region, and associated
   service function.
4. Use the filters to narrow by Region or service function.

###### To list resources (AWS CLI)

- Run the following command:

```

aws resiliencehubv2 list-resources \
  --service-arn "`service-arn`"

```

To filter by Region:

```

aws resiliencehubv2 list-resources \
  --service-arn "`service-arn`" \
  --aws-region "`region`"

```
