cat > backend/app/core/third_party_integrations/natural_disasters/README.md << 'EOF'
# Natural Disasters

Integration for multi-hazard exposure (hurricanes, wildfires, earthquakes, etc.) for real estate risk analysis.

## Overview
- Hazard endpoints (health, hazard-by-location) with typed requests/responses
- FastAPI-ready routes and proxy helpers
- Consistent SDK interface with other integrations

## Environment Variables
- NATDIS_BASE_URL (required)
- NATDIS_API_KEY (optional, provider-dependent)
- NATDIS_TIMEOUT (default: 15)

Example .env:
NATDIS_BASE_URL=https://api.example.com/natural-disasters
NATDIS_API_KEY=your_api_key_if_required
NATDIS_TIMEOUT=15

## Endpoints (examples)
- GET /natural-disasters/health
- GET /natural-disasters/hazard?lat=...&lng=...

## Project Structure
- api/: base, requests, responses, exceptions, routes
- client.py: high-level client wrapper
- config.py: configuration and environment variables
- pyproject.toml: package metadata

## Usage
Import the client for programmatic access or mount routes into your FastAPI app.
EOF

git -C backend/app/core/third_party_integrations/natural_disasters add README.md
git -C backend/app/core/third_party_integrations/natural_disasters commit -m "Add/update README for natural_disasters"
git -C backend/app/core/third_party_integrations/natural_disasters push origin master