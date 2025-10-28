# Deleting a Device Farm desktop browser testing project

To delete a project using the AWS CLI, you need the project ARN.

###### Warning

Deleting a project is not reversible.

You cannot delete a project that has in-progress sessions.

Device Farm Console

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. On the Device Farm navigation panel, choose **Desktop Browser
   Testing**, then choose
   **Projects**.
3. Choose the project you want to delete.
4. Choose the **Delete** action.
5. Confirm that you want to delete the project and any associated
   content, then choose **Delete**.

AWS CLI

1. If you don't know the ARN, use the `list-test-grid-projects` command to
   list your current Device Farm Selenium projects:

```
aws devicefarm list-test-grid-projects
```

The result contains your current Selenium testing projects:

```
{
    "testGridProjects": [
        {
            "arn": "arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:123e4567-e89b-12d3-a456-426655440000",
            "name": "Peculiar Things"
        },
        {
            "arn": "arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:123e4567-e89b-12d3-a456-426655441111",
            "name": "Wumbo's Wild WiFi Emporium"
        },
        {
            "arn": "arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:123e4567-e89b-12d3-a456-426655442222",
            "name": "Banana Stand 2: This is Bananas"
        }
    ]
}
```

2. Use the `delete-test-grid-project` command to delete the project and any
   sessions and artifacts associated with the project:

```
aws devicefarm delete-test-grid-project --project-arn arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:`123e4567-e89b-12d3-a456-426655440000`
```
