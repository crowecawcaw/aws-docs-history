

# Delete a log delivery for REST API execution logs
<a name="rest-api-delete-log-delivery"></a>

When you delete a log delivery, API Gateway resumes writing execution logs to the auto-managed log group (`API-Gateway-Execution-Logs_{rest-api-id}/{stage_name}`), as long as execution logging is still enabled on the stage.

## Delete a log delivery (AWS CLI)
<a name="rest-api-delete-log-delivery-cli"></a>

To delete a delivery, you delete the delivery and then optionally delete the delivery source and destination.

1. 

**Delete the delivery**

   ```
   aws logs delete-delivery --id {{{delivery-id}}}
   ```

1. 

**(Optional) Delete the delivery source**

   ```
   aws logs delete-delivery-source --name {{my-apigw-source}}
   ```

1. 

**(Optional) Delete the delivery destination**

   ```
   aws logs delete-delivery-destination --name {{my-log-destination}}
   ```

**Note**  
Deleting the delivery source or destination is optional. You can reuse them to create new deliveries later.

## Delete a log delivery (API Gateway console)
<a name="rest-api-delete-log-delivery-console"></a>

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose your REST API, and then choose **Stages**.

1. Choose a stage.

1. In the **Logs and tracing** section, under **Log delivery destinations**, select the destination you want to remove.

1. Choose **Delete**.

## Maintain log continuity
<a name="rest-api-delete-log-delivery-existing-group"></a>

**Tip**  
To keep logs in the same log group and maintain existing retention settings and subscription filters, set the auto-managed log group (`API-Gateway-Execution-Logs_{rest-api-id}/{stage_name}`) as a delivery destination. Log stream names will differ from those created by standard logging.