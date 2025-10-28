# Clock panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The clock panel shows the current time or a countdown. It updates every second.

- Mode – The default is
  **time**. If you choose **countdown**, set
  the **Countdown Deadline** to start the countdown.
- 12 or 24 hour – The options for showing
  the time are 12-hour format and 24-hour format.
- Timezone – The time zones are supplied by
  the moment timezone library. The default is the time zone on your
  computer.
- Countdown Deadline – Specify the time and
  date to count down to, if you have set **Mode** to
  **countdown**.
- Countdown End Text – Specify the text to
  show when the countdown ends.
- Date/Time formatting options – Customize
  the font size, weight, and date/time formatting. If you are showing a countdown
  and don't want to see the seconds ticking down, change the time format to
  `hh:mm` for the 24-hour clock or `h:mm A` for the
  12-hour clock. For a complete list of options, see [Display](https://momentjs.com/docs/#/displaying/ "https://momentjs.com/docs/#/displaying/").
- Bg Color – Select a background color for
  the clock.
