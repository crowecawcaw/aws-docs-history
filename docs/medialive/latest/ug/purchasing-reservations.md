# Purchasing a reservation

On the console, use the **Reservations** tab to
purchase one or more reservations.

###### To purchase a reservation (console)

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Reservations**,
   and then choose **Reserve offerings**. On the
   **Offerings** page, complete the **Filter
   offerings** section to filter for specific offerings. For
   more information, see [Filtering
   on the Offering Page](#filtering-offerings "#filtering-offerings").
3. Choose an offering.

If you are purchasing a reservation to target a specific output,
and that output has the frame rate set to initialize from source, make
sure that you purchase a reservation that specifies
`30-60fps`. Don't purchase a reservation that
specifies `=30fps`. 4. Select a number for the specific offering you are choosing, enter
it in the **Count** field. For example, if you are
reserving five HD AVC outputs, enter `5` in the
**Count** field. 5. Choose **Add to cart**. The
**Cart** tab title in the upper-left pane
increments to show the total offerings currently in the cart. To
remove an offering that you added to the cart, switch to the
**Cart** tab. 6. To view the cart contents, choose the **Cart**
tab. Optionally, while viewing the cart contents, you can set the
reservation to automatically renew by selecting **Enable
auto-renewal**. This option is off by default. 7. To purchase all of the offerings that are displayed on the
**Cart** tab, choose
**Purchase**.

###### Important

You can't cancel a reservation after you have purchased
it.

## Filtering on the offerings

page

The **Offerings** page shows the different
reservations that you can purchase.

**Input and output offerings, which are
described as follows:**

- Resolution
  – Codec – Input/output – Bitrate – Frame rate (for outputs only) –
  Region

For example: UHD AVC input at 10-20 Mbps in US West
(Oregon)

**Channel (add-ons) offerings, which are
described as follows:**

- Add-on – Region

For example: Advanced Audio reserved outputs in US West
(Oregon)

**You can filter the offerings by using the
filters in the left pane, as follows:**

- Filter reservation type: input, output, or channel (for
  add-ons).
- Filter offerings based on attributes, such as resolution or
  bitrate.
- Use the **Match existing channel** filter to
  show only offerings that match the inputs and outputs in the chosen
  channel.
- Use the **Special feature** filter to show only
  add-on offerings.

Filtering does not affect the items in the cart.
