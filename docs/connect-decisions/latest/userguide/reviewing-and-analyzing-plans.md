

# Reviewing and Analyzing Plans
<a name="reviewing-and-analyzing-plans"></a>

**To review a demand plan:**

1. Navigate to Plans from your AWS Connect Decisions homepage.

1. Select your active plan from the available options.

1. The system displays a high-level view of forecasts aggregated across products and sites.

1. Use the filtering options to focus on specific products, locations, or time periods.

1. Review different forecast types:
   + **Baseline forecast**: AI-generated forecast based on historical patterns
   + **Consensus plan**: Combined forecast incorporating multiple inputs (if configured)
   + **Forecast inputs**: Individual inputs from sales, customers, and marketing

## Understanding Quantile Selection
<a name="reviewing-and-analyzing-plans-quantile-selection"></a>

The system uses statistical quantiles to represent forecast uncertainty:
+ **Plans without consensus rules**: The system automatically selects the optimal quantile based on your planning grain.
+ **Consensus plans**: The system defaults all products to the P50 quantile.

To see which quantile is used for the product or product-site, filter to the finest grain level view to identify the optimal quantile.