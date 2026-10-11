

# Mapping is confirmed, not inferred
<a name="dp-mapping-confirmed"></a>

An auto-match action proposes pairings by exact normalized match first, then by shortest producer name containing the canonical name, then the inverse. It is deliberately naive, and is labelled as a starting point rather than an answer.

Sophisticated matching — synonym sets, ontologies, embeddings — was rejected for a specific reason: the operator confirms every pair either way, so a simple scorer that visibly guesses is safer than a sophisticated one that quietly guesses. A wrong pairing that looks like a guess gets checked; a wrong pairing that looks authoritative does not.