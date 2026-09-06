# How auto-renewal for private offers works

Auto-renewal terms are set by the seller on the private offer. When an agreement with
auto-renewal terms reaches its end date, AWS Marketplace generates a renewal offer, auto-accepts it
on your behalf, and creates a new agreement with a new agreement ID. Your negotiated terms
carry forward automatically, so your software or service continues without interruption. Both
you and the seller are notified before a renewal proceeds and again after it completes. No
action is required unless you want to opt in or opt out.

The renewal terms define how the price carries forward each cycle. A private offer uses one
of three renewal pricing types:

- **No price uplift** – the agreement renews at the
  same price every cycle.
- **Fixed price uplift** – the price increases by a
  fixed percentage each cycle. Because the uplift compounds, a 10% uplift takes a $100 price
 to $110, then $121, and so on.
- **Price uplift with a range** – the seller
  finalizes an exact percentage within a defined minimum and maximum before each renewal's
  adjustment deadline. The seller can apply one flat percentage or a different uplift per
  dimension, as long as each stays within the range. If the seller does not finalize a value
  by the adjustment deadline, a default uplift applies.
  Two dates govern each renewal cycle:

- **Renewal decision deadline** – the last day you
  or the seller can change the auto-renewal decision before the upcoming cycle renews
  automatically. After this date, the renewal proceeds and can no longer be stopped for that
  cycle.
- **Adjustment deadline** (price uplift with a range only)
  – the date by which the seller must finalize the exact uplift percentage for the
  next cycle. If the seller does not finalize a value, the default uplift applies.
