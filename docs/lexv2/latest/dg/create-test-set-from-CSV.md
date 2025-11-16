# Creating a test set from a CSV file for

Test Workbench

You can create a test set from the CSV file template provided in the Amazon Lex V2
console by entering the values directly by using a CSV spreadsheet editor. The test
set is a comma-separated value (CSV) file consisting of single user utterances and
multi-turn conversations recorded in the following columns:

- **Line #** – this column is an
  incremental counter that keeps track of the total filled rows to test.
- **Conversation #** – this column tracks
  the number of turns in a conversations. For single inputs, this column can
  be left empty, filled with "-" or "N/A". For conversations, each turn within
  a conversations will be assigned the same conversation number.
- **Source** – this column is set to
  "User" or "Agent". For single inputs, it will be always set to
  "User".
- **Input** – this column includes the
  user utterance or the bot prompts.
- **Expected Output Intent** – this
  column captures the intent fulfilled in the input.
- **Intent Expected Output Slot 1** –
  this column captures the first slot elicited in the user input. The test set
  should include a column called Expected Output Slot X for each slot in the
  user input.
  Example of a test set with single inputs:

| Line # | Conversation # | Source | Input                                     | Expected Output Intent | Expected Output Slot 1     | Expected Output Slot 2 |
| ------ | -------------- | ------ | ----------------------------------------- | ---------------------- | -------------------------- | ---------------------- |
| 1      |                | User   | book a cleaning appointment tomorrow      | MakeAppointment        | AppointmentType = cleaning | Date = tomorrow        |
| 2      | N/A            | User   | book a cleaning appointment on April 15th | MakeAppointment        | AppointmentType = cleaning | Date = 4/15/23         |
| 3      | N/A            | User   | book appointment for December first       | MakeAppointment        | Date = December first      |                        |
| 4      | N/A            | User   | book a cleaning appointment               | MakeAppointment        | AppointmentType = cleaning |                        |
| 1      |                | User   | Can you help me book an appointment?      | MakeAppointment        |                            |                        |

Example of a test set with conversations

| Line # | Conversation # | Source | Input                                                   | Expected Output Intent | Expected Output Slot 1       | Expected Output Slot 2 | Expected Output Slot 3 |
| ------ | -------------- | ------ | ------------------------------------------------------- | ---------------------- | ---------------------------- | ---------------------- | ---------------------- |
| 1      | 1              | User   | book an appointment                                     | MakeAppointment        |                              |                        |                        |
| 2      | 1              | Agent  | What type of appointment would you like to<br>schedule? | MakeAppointment        |                              |                        |                        |
| 3      | 1              | User   | cleaning                                                | MakeAppointment        | AppointmentType = cleaning   |                        |                        |
| 4      | 1              | Agent  | When should I schedule your appointment?                | MakeAppointment        |                              |                        |                        |
| 5      | 1              | User   | tomorrow                                                | MakeAppointment        |                              | Date = tomorrow        |                        |
| 6      | 2              | User   | book a root canal appointment today                     | MakeAppointment        | AppointmentType = root canal | Date = today           |                        |
| 7      | 2              | Agent  | At what time should I schedule your<br>appointment?     | MakeAppointment        |                              |                        |                        |
| 8      | 2              | User   | eleven a.m.                                             | MakeAppointment        |                              |                        | Time = eleven a.m.     |
