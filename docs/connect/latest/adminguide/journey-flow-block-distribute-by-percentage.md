# Distribute by percentage

## Description

- This block is useful for doing A/B testing. It routes profiles randomly based on a percentage.
- Profiles are distributed randomly, so exact percentage splits may or may not occur.

## How it works

This block creates static allocation rules based on how you configure it. Internal logic generates a random number between 1-100. This number identifies which branch to take. It doesn't use current or historical volume as part of it's logic.

For example, say a block is configure like this:

- 20% = A
- 40% = B
- 40% remaining = Default

When a profile is being routed through a flow, Amazon Connect generates the random number.

- If number is between 0-20, the contact is routed down the A branch.
- Between 21-60 it's routed down the B branch.
- Greater than 60 it's routed down the Default branch.
