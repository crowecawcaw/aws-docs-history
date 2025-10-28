# Step 2: Executing the SNS-linked sample

application

1. In the AWS Lambda console, on the navigation panel, choose
   **Applications**.
2. On the **Applications** page, in the search field, search for
   `serverlessrepo-fork-example-ecommerce-`my-app``
   and then choose the application.
3. In the **Resources** section, do the following:
   1. To find the resource whose type is **ApiGateway
      RestApi**, sort the resources by **Type**,
      for example `ServerlessRestApi`, and then expand the
      resource.
   2. Two nested resources are displayed, of types **ApiGateway
      Deployment** and **ApiGateway
      Stage**.
   3. Copy the link **Prod API endpoint** and append
      `/checkout` to it, for example:

   ```
   https://abcdefghij.execute-api.us-east-2.amazonaws.com/Prod/checkout
   ```

4. Copy the following JSON to a file named `test_event.json`.

```
{
   "id": 15311,
   "date": "2019-03-25T23:41:11-08:00",
   "status": "confirmed",
   "customer": {
      "id": 65144,
	 "quantity": 2,
      "price": 25.00,
      "subtotal": 50.00
   }]
}
```

5. To send an HTTPS request to your API endpoint, pass the sample event payload
   as input by executing a `curl` command, for example:

```
curl -d "$(cat test_event.json)" https://abcdefghij.execute-api.us-east-2.amazonaws.com/Prod/checkout
```

The API returns the following empty response, indicating a successful
execution:

```
{ }
```
