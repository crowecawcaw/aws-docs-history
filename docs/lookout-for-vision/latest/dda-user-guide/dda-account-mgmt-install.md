Defect Detection App is in preview release and is subject to change.

# Installing the Defect Detection App Tenent API

You create and manage tenant customers by using the Defect Detection App Tenant SDK. In these instructions, you use
a file, `service2.json`, to install a version of the AWS Command Line Interface that includes
the Defect Detection App tenant API onto your computer. To use the
AWS CLI, your computer needs access to the internet.

###### To install the AWS CLI

1. Install the AWS CLI onto your computer. For more information, see [https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
2. Contact AWS to get a copy of the `service-2.json` for the Defect Detection App Tenant API.
3. On your computer, save `service-2.json` in a folder that you can access from the
   command prompt.
4. At the command prompt, enter the following command to the register the AWS CLI.
   Change the value of `--service-model` to the path to the `service-2.json` that you saved in the
   previous step.

```
aws configure add-model \
    --service-name dda \
    --service-model file://`path/to/downloaded/service2.json`
```

5. Enter the following command to confirm that you can call the Defect Detection App API by using the AWS CLI.
   Change the following values:
   - `--region` — The AWS Region for the Defect Detection App API.
     For beta, use `us-east-1`.
   - `--endpoint-url` — The endpoint for the Defect Detection App Tenant
     API. For beta, use `https://6do9jn9pi9.execute-api.us-east-1.amazonaws.com/live`.

```
aws dda list-tenants \
    --region `REGION` \
    --endpoint-url `TENANT_MANAGEMENT_ENDPOINT_URL`
```

If successful, the response code is `200`. If you haven't previously created a tenant, you should get an empty
response as you haven't created any tenants. for example:

```
{
    "Tenants": []
}
```

6. Next step: [Creating a Defect Detection App tenant](dda-create-tenant.md "dda-create-tenant.md").
