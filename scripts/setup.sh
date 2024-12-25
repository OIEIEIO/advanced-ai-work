#!/bin/bash
# Setup script for advanced-ai-work project

echo "Setting up the project environment..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Initialize Whoosh index
echo "Initializing Whoosh index..."
python -c "from search.whoosh_handler import initialize_index; initialize_index()"

# Create embeddings directory if not exists
mkdir -p embeddings
touch embeddings/.gitkeep

echo "Project setup complete."
