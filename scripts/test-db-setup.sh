#!/bin/bash

# Set environment variables (adjust as needed)
PGUSER="sve"
PGPASSWORD="123"
PGHOST="localhost"
PGPORT="5433"  # Use a custom port (e.g., 5433) for the test server

# Create the "postgres" role if it doesn't exist
psql -h "$PGHOST" -p "$PGPORT" -U "$PGUSER" -d postgres -c "CREATE ROLE IF NOT EXISTS postgres WITH LOGIN PASSWORD 'your_password';"

# Grant necessary privileges to the "postgres" role
psql -h "$PGHOST" -p "$PGPORT" -U "$PGUSER" -d postgres -c "ALTER ROLE postgres CREATEDB;"

# Create the "inventory" database if it doesn't exist
psql -h "$PGHOST" -p "$PGPORT" -U "$PGUSER" -d postgres -c "CREATE DATABASE IF NOT EXISTS inventory;"

# Add the "uuid-ossp" extension to the "inventory" database
psql -h "$PGHOST" -p "$PGPORT" -U "$PGUSER" -d inventory -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"

# Print a success message
echo "Test database setup completed."

# Note: Replace the values above with your actual configuration.
# Make sure the PostgreSQL server is running and accessible.
