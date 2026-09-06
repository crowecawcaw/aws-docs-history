# Auto-generated private offers

When AWS Marketplace generates offers on your behalf based on instructions you configured, they
appear on the **Auto-generated private offers** tab of the
**Offers** page. Two categories of offers appear here:

- **Renewal offers** – generated to renew an agreement
  with auto-renewal terms. Each offer links back to the agreement it renews and inherits its
  renewal terms. Buyers do not need to act; renewal offers are auto-accepted on the buyer's
  behalf if neither you nor the buyer opt out. You do not need to act either, unless the offer
  has a **Pending uplift** status and you need to finalize the price uplift
  percentage.
- **Express private offers** – generated when a
  qualified buyer builds their own offer from a rate card you published.
  Offer status tells you what, if anything, you need to do:

- **Pending uplift** – the offer uses percentage-range pricing and
  needs you to finalize the uplift percentage. The status is escalated to a warning and an
  alert appears when you are within 30 days of the adjustment deadline. If the deadline passes,
  the default uplift applies automatically.
- **Active** – the offer is finalized and available to the
  buyer.
- **Expired** – the offer has expired.
  Clicking into a renewal offer shows an offer summary (offer ID, offer currency, offer
  status, publish and expiration dates, net payment terms, and offer purpose) and a product
  summary, along with the following tabs:

- **Offer details** – the pricing model, contract start date and
  duration, buyers, region availability, and legal terms and offer documentation.
- **Offer pricing** – the contract dimensions and the usage
  dimensions, including the per-unit usage prices. After you finalize a range uplift, the
  final prices appear here.
- **Installment plan** (for applicable offers) – the contract
  total and the installment schedule (payment amount and invoice date for each
  installment).
- **Agreements** – the agreements created from that offer.
- **Renewal details** – the renewal terms for the next cycle:
  renewal status, renewal pricing, price uplift, renewal maximum, renewal decision deadline,
  previous agreement ID, and the renewal installment plan. You can opt out of auto-renewal
  from this tab. Seller opt-out is a one-time action that can't be reversed; it stops the
  renewal and notifies the buyer. Buyers, by contrast, can opt in and out until the renewal
  decision deadline. Once you opt out, the buyer can't opt back in – they see
  **Seller opted out** and must request a new offer.
- **Renewal history** – all past and upcoming offers and
  agreements in this renewal chain. Only the next projected renewal cycle is shown, regardless
  of how many future cycles are scheduled.
- **Request log** – logs for the offer.

## Finalizing the price uplift percentage

To finalize the price uplift percentage for a percentage-range renewal offer, set the
exact uplift for the next cycle within the range you configured at offer creation:

###### To finalize the price uplift percentage

1. Open the renewal offer from the **Auto-generated private offers**
   tab, or open the **Renewal details** tab of the agreement set to
   auto-renew.
2. Choose **Finalize uplift percentage**.
3. Set the uplift. You can apply one flat percentage across all dimensions, or set a new
   price per dimension. Prices must stay within the configured range. As you adjust the
   percentage, the preview updates the current TCV, the renewal TCV, and the price
   change.
4. Save your selection:

   - **Save as draft** – keeps your selection editable; nothing
     is sent to the buyer.
   - **Publish to buyer** – locks in the percentage and
     notifies the buyer immediately. This action is irreversible.

If you do not publish before the adjustment deadline, the most recently saved value
applies, or the default uplift if you never saved one. After the uplift is finalized, you can
see the final prices on the **Offer pricing** tab.
