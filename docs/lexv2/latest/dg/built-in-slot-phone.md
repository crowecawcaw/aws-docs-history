# AMAZON.PhoneNumber

Converts the numbers or words that represent a phone number
into a string format without punctuation as follows.

| Type                                                  | Description                                                   | Input                                | Result                           |
| ----------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------ | -------------------------------- |
| International number with leading plus (+)<br>sign    | 11-digit number with leading plus<br>sign.                    | +61 7 4445 1061<br>+1 (509) 555-1212 | `+61744431061`<br>`+15095551212` |
| International number without leading plus (+)<br>sign | 11-digit number without leading plus<br>sign                  | 1 (509) 555-1212<br>61 7 4445 1061   | `15095551212`<br>`61744451061`   |
| National number                                       | 10-digit number without international<br>code                 | (03) 5115 4444<br>(509) 555-1212     | `0351154444`<br>`5095551212`     |
| Local number                                          | phone number without an international<br>code or an area code | 555-1212                             | `5551212`                        |
