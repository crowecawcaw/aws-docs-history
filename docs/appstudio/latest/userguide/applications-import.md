# Importing applications

You can import a copy of an exported application to your App Studio instance. You can import apps that
have been exported from other App Studio instances, or apps from a catalog provided by App Studio. Importing an app from the App Studio app catalog can help
you get started on an app with similar functionality, or help you learn about app building in App Studio by exploring the imported app.

When you import an app into your instance, a copy of the original app is created in your instance. After the new app is created, you are navigated
to the Development environment of the app, where you can preview it and browse the app's functionality.

###### Warning

When you import an app, you are importing all of the logic from the application, which could result in undesired or unexpected
behavior. For example, there could be destructive queries that delete data from databases you connect to the application. We recommend thoroughly reviewing the application and its
configuration, and testing it on non-production assets before connecting production data to it.

###### To import an application

1. In the navigation pane, choose **My applications** in the **Build** section to navigate
   to a list of your applications.
2. Choose the dropdown arrow next to **+ Create app**.
3. Choose **Import app**.
4. In the **Import app** dialog box, in **Import code**, enter the import code
   of the application that you want to import.
   For a list of apps provided by App Studio that can be imported, including app descriptions and import codes,
   see [Importable apps provided by App Studio](#app-catalog "#app-catalog").
5. Choose **Import** to import the app and go to the Development environment of the imported app to view or edit it.
   For information building apps in App Studio, see [How AWS App Studio works](how-it-works.md "how-it-works.md")

## Importable apps provided by App Studio

App Studio provides apps that can be imported into your instance to help you learn about app building. To see how specific app functionality is implemented
in App Studio, you can preview the applications and then browse their configuration in the Development environment.

The following table contains the list of applications, their import codes, and a brief description of the apps.
Each app includes a `README` page that contains information about the app that you can view after you import it.

| App name                            | Description                                                                                                                                                                                                                                                                                                                                                                                                               | Import code                                                          |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Swag Request Survey**             | An internal swag request application designed for employees to order branded company merchandise. Employees can select items and specify sizes and submit their request through a simple form. This application handles all data through built-in storage, removing the need for external connections.                                                                                                                    | Swag Request Survey/ec4f5faf-e2f8-42ee-ab8d-6723d8ca21b2             |
| **Sprint Tracking**                 | A sprint management application that teams can use to organize and track software development work. Users can create sprints, add tasks, assign work, and monitor progress through dedicated sprint, track, and task views. This application handles all data through built-in storage, removing the need for external connections.                                                                                       | Sprint Tracking/8f31e160-771f-48d7-87b0-374e285e2fbc                 |
| **Amazon Review Sentiment Tracker** | This application is a customer feedback analysis tool that generates sentiment scores from product reviews to help businesses understand customer satisfaction. The application includes sample data generation utilities for quick testing and requires an Amazon Bedrock connector for AI-powered insights, while maintaining all other data within the built-in storage system.                                        | Amazon Review Sentiment Tracker/60f0dae4-f8e2-4c20-9583-fa456f5ebfab |
| **Invoice and Receipt Processing**  | This receipt processing application saves time and reduces errors by automating manual data entry and streamlining document approval workflows. The solution requires Amazon Textract, Amazon S3 and Amazon SES connectors. It uses an Amazon Textract to analyze and extract data from receipts stored in Amazon S3, then processes and emails the extracted information to approvers using Amazon SES.                  | Invoice and Receipt Processing/98bde3ae-e454-4b18-a1e6-6f23e8b2a4f1  |
| **Inspection and Inventory Audit**  | An application for managing warehouse inspections and equipment tracking. Users can conduct pass/fail equipment assessments by room location, monitor inventory levels, and view inspection history. The application provides a centralized system for tracking both facility inspections and equipment status. This application handles all data through built-in storage, removing the need for external connections.   | Inspection and Inventory Audit/cf570a06-1c5e-4dd7-9ea8-5c04723d687f  |
| **Product Adoption Tracker**        | A comprehensive application for managing product development that centralizes customer feedback, feature requests and customer meeting notes. Teams can track customer interactions, organize requirements, and generate AI-powered reports for quarterly roadmap planning. The application includes sample data utilities and leverages Amazon Bedrock for AI insights and Amazon Aurora PostgreSQL for data management. | Product Adoption Tracker/9b3a4437-bb50-467f-ae9e-d108776b7ca1        |
| **Quick Suite Embedding**           | A demo application that enables users to view analytics while working with the underlying data. The app contains two methods for embedding Amazon Quick Suite dashboards in App Studio: an API-based approach for registered and anonymous users (requiring Quick Suite connector), and an iFrame integration for public dashboards.                                                                                      | Quicksight Embedding/0cdc15fc-ca8b-41b7-869e-ed13c9072bc8            |
| **Kitchen Sink**                    | A reference application showcasing advanced App Studio development tips and best practices. Includes working examples of state management, CSV data handling, browser API integration, and UI patterns that builders can study and implement in their own applications. None of the examples require external connections.                                                                                                | App Studio Kitchen Sink/1cfe6b2f-544c-4611-b82c-80eadc76a0c8         |
