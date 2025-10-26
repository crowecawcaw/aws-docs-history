#!/usr/bin/env python3
"""Extract start URLs and allowed prefixes for a specific service from the manifest."""

import json
import sys
from pathlib import Path


def get_service_urls(manifest_path: Path, service_id: str) -> tuple[list[str], list[str]]:
    """Get start URLs and allowed prefixes for a specific service.

    Args:
        manifest_path: Path to the service manifest JSON file
        service_id: The service ID to look up

    Returns:
        Tuple of (start_urls, allowed_prefixes)

    Raises:
        ValueError: If the service ID is not found
    """
    with manifest_path.open('r', encoding='utf-8') as f:
        data = json.load(f)

    services = data.get('services', [])

    for service in services:
        if service.get('id') == service_id:
            guides = service.get('guides', [])
            start_urls = [guide['url'] for guide in guides if 'url' in guide]
            allowed_prefixes = [guide['allowed_prefix'] for guide in guides if 'allowed_prefix' in guide]
            return start_urls, allowed_prefixes

    raise ValueError(f"Service ID '{service_id}' not found in manifest")


def main():
    if len(sys.argv) != 3:
        print("Usage: get_service_urls.py <manifest_path> <service_id>", file=sys.stderr)
        sys.exit(1)

    manifest_path = Path(sys.argv[1])
    service_id = sys.argv[2]

    try:
        start_urls, allowed_prefixes = get_service_urls(manifest_path, service_id)

        # Output in a format that can be easily consumed by bash
        print("START_URLS=" + " ".join(start_urls))
        print("ALLOWED_PREFIXES=" + " ".join(allowed_prefixes))

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
