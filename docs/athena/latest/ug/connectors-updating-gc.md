# Glue connections (recommended)

## Find the latest Athena Query Federation version

The latest version number of Athena data source connectors corresponds to the latest
Athena Query Federation version. In certain cases, the GitHub releases can be slightly
newer than what is available on the AWS Serverless Application Repository (SAR).

###### To find the latest Athena Query Federation version number

1. Visit the GitHub URL [https://github.com/awslabs/aws-athena-query-federation/releases/latest](https://github.com/awslabs/aws-athena-query-federation/releases/latest "https://github.com/awslabs/aws-athena-query-federation/releases/latest").
2. Note the release number in the main page heading in the following
   format:

**Release v**
`year`.`week_of_year`.`iteration_of_week`
**of Athena Query Federation**

For example, the release number for **Release v2023.8.3 of Athena Query
Federation** is 2023.8.3.

## Finding your connector version

Follow these steps to determine which version of your connector you are currently using.

###### To find your connector version

1. On the Lambda console page for your Lambda application, choose the **Image** tab.
2. Under Image tab, locate the Image URI. The URI follows this format:

```
`Image_location_account`.dkr.ecr.us-west-2.amazonaws.com/athena-federation-repository:`Version`
```

3. The version number in the Image URI follows the format `year.week_of_year.iteration_of_week` (for example, `2021.42.1`). This number represents your connector version.

## Deploying a new connector version

Follow these steps to deploy a new version of your connector.

###### To deploy a new connector version

1. Find the desired version by following the procedure to find the latest Athena Query Federation version.
2. In the federated connector Lambda function, locate the ImageURI and update the tag to the desired version. For example:

From:

```
509399631660.dkr.ecr.us-east-1.amazonaws.com/athena-federation-repository:2025.15.1
```

To:

```
509399631660.dkr.ecr.us-east-1.amazonaws.com/athena-federation-repository:2025.26.1
```

###### Note

If your current version is older than 2025.15.1, be aware of these important changes:

- The repository name has been updated to `athena-federation-repository`
- For versions before this update, the command override may not be set. You must set it to the composite handler.
