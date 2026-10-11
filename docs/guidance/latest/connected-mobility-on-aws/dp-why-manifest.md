

# Why a transform manifest exists
<a name="dp-why-manifest"></a>

Three producers describe the same physical quantity three different ways, with three different severity scales — a battery state of charge arrives as a nested camelCase path from one, a snake\_case protobuf field from another, and a flat REST key from a third. Seeing `speedMph`, `vehicle_speed_mph` and `speed` all landing on one canonical signal is the entire argument for normalizing at the boundary rather than downstream.

The demonstration data is deliberately inconsistent across producers for this reason. Producer catalogs also deliberately do not cover every canonical signal, and coverage is displayed as a count of mapped signals against the total so gaps are visible rather than implied.

 **Severity is mapped, never inferred.** Producer event names and producer severity labels are both producer-private vocabulary — one producer’s `HIGH` is another’s `warning`. Downstream flows for safety, maintenance and reporting key on the canonical name and the canonical severity, so the mapping is an explicit pair on both. Inferring severity from the producer’s own label would mean a producer relabelling `HIGH` to `MEDIUM` silently changes this platform’s safety behavior.