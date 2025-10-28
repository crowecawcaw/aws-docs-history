# Examples of Agent Adherence

calculations in Amazon Connect

This topic shows two examples that illustrate how Agent Adherent and Non-Adherent
Time are calculated in Amazon Connect. It also includes a third example that shows adherence
with thresholds.

## Example 1

**The schedule**: Agent A is scheduled to work
from 8:00 to 11:00.

**What the agent does**: Agent A begins working
at 7:30 and then takes a break from 10:30 to 11:00.

**Their adherence**:

- From 7:30 to 8:00 Agent A is neither adherent or non-adherent since
  there is no schedule.
- From 8:00 to 10:30 Agent A is adherent and from 10:30 to 11:00 they
  are non-adherent because:
  - Their status was "Break" when it should have been "Available"
    because they were scheduled for "Work" and the "Work" activity
    is mapped to only the "Available" status.

This means that Agent A's Adherence was 83%. Adherence was calculated as
follows:

- (Total Adherent Time was 150 minutes/Total Scheduled Time 180
  minutes)

## Example 2

**The schedule**: Agent B is scheduled to work
from 9:00 to 10:30. They are scheduled to go on "Break" from 10:30 to 11:00, and
then go to a team meeting from 11:00 to 12:00.

**What the agent does**: Agent B begins working
at 9:00 and ends up working until 10:45. Then they set their status as "Break"
at 10:45 and forget to switch it to "Team Meeting" at 11. They leave their
status as "Break" from 10:45 to 12:00.

**Their adherence**:

- From 9:00 to 10:30 Agent B was adherent but from 10:30 to 10:45 they
  were non-adherent because:
  - They were scheduled for "Break," which was mapped to the
    "Break" status, but their actual status was "Available."

- They were also non-adherent from 11:00 to 12:00 because:
  - They were scheduled for the team meeting activity which maps
    to the "Team Meeting" status, but their actual status was
    "Break."

This means that Agent B's adherence was 58%. Adherence was calculated as
follows:

- (Total Adherent Time: 105 Minutes / Total Scheduled Time: 180
  Minutes)

## Example: Adherence with

thresholds

The schedule: Agent C is scheduled for a break at 10:00 AM

Configured threshold: 5 minutes early/late allowed for break activity

**What the agent does:**

- Starts break at 10:03 AM (3 minutes late).
- Returns from break at scheduled time.

**Their adherence:**

- Agent remains adherent because starting break 3 minutes late falls
  within the configured 5-minute threshold.
- The "Using thresholds" status would be displayed during this
  period.
