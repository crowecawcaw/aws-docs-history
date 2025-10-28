# Deregistering an Amazon S3 location

You can deregister an Amazon Simple Storage Service (Amazon S3) location if you no longer want it to be managed by
Lake Formation. Deregistering a location does not affect Lake Formation data location permissions that are
granted on that location. You can reregister a location that you deregistered, and the data
location permissions remain in effect. You can use a different role to reregister the
location.

###### To deregister a location (console)

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign in as the data lake
   administrator or as a user with the `lakeformation:RegisterResource`
   IAM permission.
2. In the navigation pane, under **Administration**, choose
   **Data lake locations**.
3. Select a location, and on the **Actions** menu, choose
   **Remove**.
4. When prompted for confirmation, choose **Remove**.
