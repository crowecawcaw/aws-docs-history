# MeetingInsights

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Contains a summary of the top 3 meetings along with meeting purpose, related
cross-app artifacts, and activities from tasks, emails, messages, and calendar
events.

| Parameter          | Description                                                                                                                                                                                                                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **insightId**      | The unique id for the generated insight.                                                                                                                                                                                                                                                                |
| **insightContent** | The description of the insight highlighting the details in a<br>string format. As in, why is this insight important.                                                                                                                                                                                    |
| **insightTitle**   | The title of the generated insight.                                                                                                                                                                                                                                                                     |
| **createdAt**      | When the insight was generated.                                                                                                                                                                                                                                                                         |
| **calendarEvent**  | The important calendar event or meeting that the user should<br>focus on.<br>Calendar Event object:<br>• `startTime` — The start time of the<br>event.<br>• `endTime` — The end time of the<br>event.<br>• `eventUrl` — The URL for the<br>calendar event on the ISV app.                               |
| **resources**      | The list containing the other resources related to the<br>generate the insight.<br>Resource object:<br>• `appName` — The app name to which<br>the resource belongs.<br>• `resourceTitle` — The resource<br>title.<br>• `resourceType` — The type of the<br>resource.<br>The possible values are: `EMAIL | EVENT | MESSAGE<br> | TASK`<br>• `resourceUrl`— The resource URL in<br>the app.<br>•`appIconUrl` — The image URL of the<br>app to which the resource belongs. |
| **nextToken**      | The pagination token to fetch the next set of insights. It’s<br>an optional field which if returned null means there are no more<br>insights to load.                                                                                                                                                   |
