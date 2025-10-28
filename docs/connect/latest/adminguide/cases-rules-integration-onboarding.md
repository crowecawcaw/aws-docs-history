# Allow Amazon Connect Cases to send

updates to Contact Lens rules

###### Note

To perform the instructions in this procedure, you need to have developer skills,
or be experienced with Amazon Connect CLI.

Complete this one-time procedure so your users can set up rules that run when a case
is created or updated.

1.  Verify Amazon Connect Cases is [enabled](enable-cases.md "enable-cases.md") for your
    Amazon Connect instance.
2.  Complete the steps to enable Amazon Connect Cases event streams. For more information
    see [Set up Amazon Connect Cases event streams](case-event-streams-enable.md "case-event-streams-enable.md"). Note the following changes to
    the procedure:
    1. You can skip the part that asks you to create a SQS queue, as it is
       not required.
    2. Run the `put-case-event-configuration` CLI command to
       include all case fields information in the event. Make sure to include
       all of the fields that you need for the Rules engine to work.

    ###### Note

    To ensure that Cases SLA Breach rules work properly, you must set
    `relatedItemData.includeContent` to
    `true`, as shown in the following example.

    ```
    aws connectcases put-case-event-configuration --domain-id 01310a0e-24ba-4a3c-89e9-9e1daeaxxxx --event-bridge "{
        \"enabled\": true,
        \"includedData\": {
           \"caseData\": {
               \"fields\": [
                 {
                   \"id\": \"status\"
                 },
                 {
                   \"id\": \"title\"
                 },
                 {
                   \"id\": \"assigned_queue\"
                 },
                 {
                   \"id\": \"assigned_user\"
                 },
                 {
                   \"id\": \"case_reason\"
                 },
                 {
                   \"id\": \"last_closed_datetime\"
                 },
                 {
                   \"id\": \"created_datetime\"
                 },
                 {
                   \"id\": \"last_updated_datetime\"
                 },
                 {
                   \"id\": \"reference_number\"
                 },
                 {
                   \"id\": \"summary\"
                 }
               ]
          },
          \"relatedItemData\": {
          \"includeContent\": true
          }
        }
      }"
    ```

    3. If there are custom case fields, make sure to include a custom field
       ID the fields array in the previous payload as well. You can find field
       IDs by running the following `list-fields` CLI
       command:

    ```
    aws connectcases list-fields --domain-id 01310a0e-24ba-4a3c-89e9-9e1daeaxxxx

    ```

    4. Repeat step 2 if you need to add new custom fields.

3.  Make a [CreateEventIntegration](../../../appintegrations/latest/APIReference/API_CreateEventIntegration.md "../../../appintegrations/latest/APIReference/API_CreateEventIntegration.md") API call, or run the
    `create-event-integration` CLI command, as shown in the following
    example command.
    - Payload:

    ```
    aws appintegrations create-event-integration --name amazon-connect-cases --description amazon-connect-cases --event-filter '{"Source":"aws.cases"}' --event-bridge-bus default

    ```

    - The output will look similar to the following sample:

    ```
    {
        "EventIntegrationArn": "arn:aws:app-integrations:us-west-2:111222333444:event-integration/amazon-connect-cases"
    }
    ```

4.  Make a [CreateIntegrationAssociation](../APIReference/API_CreateIntegrationAssociation.md "../APIReference/API_CreateIntegrationAssociation.md") API call, or run the
    `create-integration-association` CLI command, as shown in the
    following example command.

        * Payload:


        The `IntegrationArn` is the response you get from step
         3.



        ```
        aws connect create-integration-association --instance-id bba5df5c-6a5f-421f-a81d-9c16402xxxx --integration-type EVENT --integration-arn arn:aws:app-integrations:us-west-2:111222333444:event-integration/amazon-connect-cases --source-type CASES

        ```
        * The output will be similar to the following sample:



        ```
        {
            "IntegrationAssociationId": "d49048cd-497d-4257-ab5c-8de797a123445",
            "IntegrationAssociationArn": "arn:aws:connect:us-west-2:111222333444:instance/bba5df5c-6a5f-421f-a81d-9c16402bxxxx/integration-association/d49048cd-497d-4257-ab5c-8de797a123445"
        }
        ```

    Your users should now be able to create rules that run when a case is created or
    updated.
