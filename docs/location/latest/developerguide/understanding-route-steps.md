# Understanding route steps

This section defines various actions and steps that need to be taken to complete a leg
of a journey. Route steps vary by travel mode and provide guidance for both overview
applications and detailed turn-by-turn navigation.

## Route steps overview

The following types of route steps define the actions needed to complete a route
leg, varying by travel mode and the stage of the journey.

| **Step type**                | **Description**                                                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **`Default<br>steps`**       | Basic steps providing human-readable instructions, often used in<br>web-based applications to offer an overview of the route. |
| **`Turn by turn<br>steps`**  | Detailed steps for creating a turn-by-turn navigation<br>application, offering more granular directions.                      |
| **`Before travel<br>steps`** | Steps that need to be completed before starting the travel<br>section, such as boarding a ferry.                              |
| **`After travel<br>steps`**  | Steps to be performed after the travel section is complete, like<br>de-boarding a ferry.                                      |

## Step breakdown by travel mode

| **Section**    | **Step**        | **Before Travel** | **Travel** | **After Travel** |
| -------------- | --------------- | ----------------- | ---------- | ---------------- |
| **Vehicle**    | Arrive          | No                | Yes        | No               |
| **Vehicle**    | Continue        | No                | Yes        | No               |
| **Vehicle**    | ContinueHighway | No                | Yes        | No               |
| **Vehicle**    | Depart          | No                | Yes        | No               |
| **Vehicle**    | Exit            | No                | Yes        | No               |
| **Pedestrian** | Arrive          | No                | Yes        | No               |
| **Pedestrian** | Charge          | No                | Yes        | No               |
| **Ferry**      | Wait            | No                | No         | Yes              |
| **Ferry**      | Board           | Yes               | No         | No               |
| **Ferry**      | Deboard         | No                | No         | Yes              |
