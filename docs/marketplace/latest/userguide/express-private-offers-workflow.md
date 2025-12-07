# How express private offers work

Express private offers enable automated private offer generation through a structured three-phase process. This workflow ensures that standard deals are processed efficiently while complex opportunities receive appropriate sales attention.

## 1. Rate card setup

The initial phase requires sellers to establish rate card configurations within AWS Marketplace. During this setup, sellers define their base pricing structure and dimension descriptions, ensuring each dimension has detailed explanations (minimum 250 characters) to help guide buyers in their selection process.

The configuration includes setting fundamental offer parameters such as contract duration limits, EULA requirements, and offer expiration timeframes. Sellers must consider their discounting strategy, choosing between dimension-based, TCV-based, or buyer-profile based rate cards, or approved combinations thereof. The system allows sellers to implement sophisticated qualification criteria and pricing rules while maintaining control through global maximum thresholds for both total contract value and discount percentages.

For more information, see [Creating custom dimensions for private offers](express-private-offers-custom-dimensions.md "express-private-offers-custom-dimensions.md").

## 2. Buyer request process

When buyers engage with the express private offer system, they begin by selecting the **Get Express Private Offer** button on the AWS Marketplace product listing. The system then guides buyers through a structured qualification process, leveraging an AI agent that uses the seller's predefined criteria to match against the buyer's needs. The agent operates within strict parameters set by the seller's configuration. For sellers using buyer-profile based qualifications, the system presents relevant questions to buyers, collecting self-reported information that determines discount eligibility and offer access.

## 3. Private offer generation

The final phase of the workflow involves automated offer creation and routing decisions. The system evaluates buyer inputs against the seller's predefined criteria, including dimension selections, total contract value, and any profile-based qualifications. For qualified buyers, the system instantly generates a private offer incorporating all applicable discounts, calculated according to the seller's configuration.

These offers are clearly identified with "express private offer" in their naming convention and follow standard AWS Marketplace private offer processes for notification and management. When buyers don't meet qualification criteria, such as exceeding the global TCV maximum or failing specific profile requirements, the system automatically redirects them to a sales-assisted workflow. This ensures that complex or high-value deals receive appropriate attention while maintaining the efficiency of the automated system for standard transactions.
