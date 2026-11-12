#!/bin/bash
set -euo pipefail

echo "Starting deployment simulation..."

mkdir -p deployment

cp app.py deployment/

echo "Application copied successfully."

echo "Verifying deployed application..."

python3 deployment/app.py

echo "Deployment simulation completed successfully."
