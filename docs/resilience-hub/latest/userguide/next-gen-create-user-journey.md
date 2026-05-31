# Create a user journey

###### To create a user journey (console)

1. Open the Next generation Resilience Hub console.
2. In the navigation pane, choose **Systems**, then choose the system you
   want to add a user journey to.
3. Choose the **User journeys** tab.
4. Choose **Create user journey**.
5. Provide the following details:
   - **Name** – Enter a name that describes the business
     capability (for example, "Path to purchase" or "Order fulfillment"). Name user journeys
     after what an end user does, not after technical components.
   - **Description** – (Optional) Enter a description of
     the user journey.
   - **Associated services** – (Optional) Select the
     services that support this user journey. You can add services later.

6. Choose **Create user journey**.

###### To create a user journey (AWS CLI)

- Run the following command:

```

aws resiliencehubv2 create-user-journey \
  --system-arn "arn:aws:resiliencehub:`region`:`account-id`:system/`system-name`:`id`" \
  --name "`journey-name`" \
  --description "`journey-description`"

```
