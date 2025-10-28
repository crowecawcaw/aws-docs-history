# Billing for overlay ads in MediaTailor

MediaTailor bills customers based on the number of non-linear ads in the ADS response. This
number includes non-linear ads that extend past the break duration. After MediaTailor fills
the avail, it bills for the ads it filled.

For prefetch workflows, MediaTailor does not bill for ads when retrieving the prefetch, but
rather, when it sees a compatible ad avail in the consumption window for that
session.

For additional billing information, see [https://aws.amazon.com/mediatailor/pricing/](https://aws.amazon.com/mediatailor/pricing/ "https://aws.amazon.com/mediatailor/pricing/").
