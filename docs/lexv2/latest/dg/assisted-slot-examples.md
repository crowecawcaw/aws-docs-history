# Examples of assisted slot resolution used in Lex V2

Below are some examples where assisted slot resolution is able to intelligently resolve user utterances into a value.

AMAZON.Number

| Vertical | slotType      | slotName                   | slotPrompt                                 | utterance                  | Resolved Value |
| -------- | ------------- | -------------------------- | ------------------------------------------ | -------------------------- | -------------- |
| Travel   | AMAZON.Number | numberOfNightsStayed       | How many nights did you stay for the trip? | A whole week, 7 nights.    | 7              |
| Banking  | AMAZON.Number | numberOfPeopleOnTheAccount | How many people are on the account?        | Me and my wife.            | 2              |
| Travel   | AMAZON.Number | numberOfStops              | How many stops?                            | Once in Japan. Once in LA. | 2              |

AMAZON.AlphaNumeric

| Vertical   | slotType            | slotName         | slotPrompt                                            | utterance                                                               | Resolved Value |
| ---------- | ------------------- | ---------------- | ----------------------------------------------------- | ----------------------------------------------------------------------- | -------------- |
| Car Rental | AMAZON.Alphanumeric | transactionId    | What is your transaction id?                          | I believe it was alpha whiskey echo eight three four nine romeo juliet. | AWE8349RJ      |
| Travel     | AMAZON.Alphanumeric | confirmationCode | What is the confirmation number for your reservation? | The confirmation number is BLT2UE.                                      | BLT2UE         |

AMAZON.Date

| Vertical   | slotType    | slotName   | slotPrompt                                  | utterance                                 | Resolved Value | currentDate |
| ---------- | ----------- | ---------- | ------------------------------------------- | ----------------------------------------- | -------------- | ----------- |
| Car Rental | AMAZON.Date | dueDate    | When is the rental agreement due to expire? | The lease is up on the 1st of next month. | 2023-12-01     | 2023-11-09  |
| Travel     | AMAZON.Date | returnDate | When are you returning?                     | Later today around 7.                     | 2023-11-09     | 2023-11-09  |

AMAZON.PhoneNumber

| Vertical  | slotType           | slotName     | slotPrompt                                            | utterance                                               | Resolved Value |
| --------- | ------------------ | ------------ | ----------------------------------------------------- | ------------------------------------------------------- | -------------- |
| Insurance | AMAZON.PhoneNumber | policyHolder | What is the phone number of the policy holder?        | The phone number for the policy holder is 123-456-7890. | 1234567890     |
| Retail    | AMAZON.PhoneNumber | phoneLookup  | What is your phone number so I can find your account? | I think it's under 413-570-9617, let me double check.   | 4135709617     |

AMAZON.Country

| Vertical | slotType       | slotName         | slotPrompt                                                    | utterance                          | Resolved Value |
| -------- | -------------- | ---------------- | ------------------------------------------------------------- | ---------------------------------- | -------------- |
| Travel   | AMAZON.Country | nativeCountry    | What is your country of origin?                               | I am Indian.                       | India          |
| Banking  | AMAZON.Country | countryItinerary | What countries will you be traveling to with your debit card? | I will be travelling to New Delhi. | India          |

AMAZON.City

| Vertical  | Slot Type   | Intent           | Question                                    | Response                | Resolved Value |
| --------- | ----------- | ---------------- | ------------------------------------------- | ----------------------- | -------------- |
| Insurance | AMAZON.City | policyHolderCity | What city does the policy holder reside in? | I live in Springfield.  | Springfield    |
| Travel    | AMAZON.City | destinationCity  | Which city are you traveling to?            | I'm traveling to Tokyo. | Tokyo          |

AMAZON.Confirmation

| Vertical  | slotType            | slotName       | slotPrompt                        | utterance                           | Resolved Value |
| --------- | ------------------- | -------------- | --------------------------------- | ----------------------------------- | -------------- |
| Insurance | AMAZON.Confirmation | policyExpired  | Has the insurance policy expired? | Yes, unfortunately it has expired.  | Yes            |
| Banking   | AMAZON.Confirmation | hasInvestments | Do you have any investments?      | I haven't invested in anything yet. | No             |
