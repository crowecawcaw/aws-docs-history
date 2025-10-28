# Filtering results

At the top of each page, you can filter the results for your bot analytics.

You can filter by the following parameters:

- **Time** – You can filter results by a
  relative or absolute time range. When you select a start and end time, Amazon Lex V2
  retrieves conversations that began _after_ the start time and
  ended _before_ the end time.
  - **Relative range** – Select
    **1d** to see results from the past day,
    **1w** for the past week, or
    **1m** for the past month.

  For more options, select **Custom** and
  choose a duration in the **Relative range**
  menu. For more control over the duration, select **Custom range**, enter a number in the **Duration** field, and choose a **Unit
  of time** from the dropdown menu.
  - **Absolute range** – Select
    **Custom** and choose the **Absolute
    range** menu to filter for conversations within a time
    range that you specify. You can choose a start and end date on the
    calendar or enter it in YYYY/MM/DD format.

###### Note

The analytics time range has the following restrictions:

    + The start date must be within the last 365 days from the current date.
    + The end date must not be more than 1 month after the start date.

- **Bot filters** – To filter by locale, alias, and version of your bot, select the dropdown menus labeled **All locales**, **All aliases**, and **All versions**.
- **Modality** – Select the gear icon and choose the **Modality** dropdown menu to choose whether to display results for **Speech** or **Text**.
- **Channel** – Select the gear icon and choose the **Channel** dropdown menu
  to choose the channel for which you want to display results. For more
  information about channel integration, see [Integrating an Amazon Lex V2
  bot with a messaging platform](deploying-messaging-platform.md "deploying-messaging-platform.md") and [Amazon Connect contact centers](../../../connect/latest/adminguide/amazon-connect-contact-centers.md "../../../connect/latest/adminguide/amazon-connect-contact-centers.md")
