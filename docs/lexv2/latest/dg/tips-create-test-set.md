# Tips for creating a successful test

set

- You can create an IAM role for the Test Workbench in the console, or you
  can configure your IAM role step-by-step. For more information, see [Create an IAM role for the Test Workbench](create-iam-test-set.md "create-iam-test-set.md").
- Before executing a test, validate the test set and the bot definition for
  any inconsistencies using the **Validate discrepancy**
  button. If the intent and slot naming conventions used in the test set are
  consistent with the bot, proceed to execute the test. If any anomalies are
  identified, revise the test set, update the test set, and choose
  **Validate discrepancy**. Repeat this sequence again
  until no inconsistencies are noted, then execute the test.
- The Test Workbench can test with different slot value formats in the
  **Expected Output Slot** column. For any built-in slot,
  you can choose the value provided in the user input (for example, Date =
  tomorrow), or provide its absolute resolved value (for example, Date =
  2023-03-21). For more information around built-in slots and their absolute
  values, see [Built-in
  slots](howitworks-builtins-slots.md "howitworks-builtins-slots.md").
- For consistency and readability in the **Expected Output
  Slot** columns, follow the convention of "SlotName = SlotValue"
  (for example, AppointmentType = cleaning) with a space before and after the
  equal sign.
- If the bot includes composite slots, in **Expected Output
  Slot** define subslots to the slot name, separated by a period
  (for example, “Car.Color”). No other syntax and punctuation will
  work.
- If the bot includes multi-value slots, in **Expected Output
  Slot** provide multiple slot values, separated by a comma
  ("FlowerType = roses, lilies"). No other syntax and punctuation will
  work.
- Make sure that the test set is created from valid conversation logs.
- Slot:slot value will be in the same column after the intent columns in the
  CSV format.
- DTMF input from a User turn is interpreted as an expected transcription
  and does not list an Amazon S3 location.
