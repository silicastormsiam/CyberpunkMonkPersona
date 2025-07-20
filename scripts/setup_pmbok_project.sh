#!/bin/bash
# File Name: setup_pmbok_project.sh
# Owner: Andrew Holland (@SilicaStormSiam)
# Purpose: Automates GitHub project creation with PMBOK Task Board view and 5 PMBOK process group columns.
# Version Control:
#   - Version 1.1 (2025-07-20): Added PMBOK Task Board view and columns for Initiating, Planning, Executing, Monitoring and Controlling, Closing.
#   - Version 1.0 (2025-07-20): Initial script for PMBOK project board setup.

set -e

# User and project details
USER="SilicaStormSiam"
PROJECT_NAME="SilicaStormSiam Projects"
PROJECT_DESC="Tracks SilicaStormSiam’s projects, including CPM - Chat Bot, home automation, and cybersecurity, following PMBOK guidelines."

# Create project and capture project number
PROJECT_NUMBER=$(gh project create --owner "$USER" --title "$PROJECT_NAME" --description "$PROJECT_DESC" --json number --jq '.number')

# Create PMBOK columns in Board view (PMBOK Task Board)
gh project field-create "$PROJECT_NUMBER" --owner "$USER" --name "Status" --data-type SINGLE_SELECT --options "Initiating,Planning,Executing,Monitoring and Controlling,Closing"

# Rename default view to PMBOK Task Board (requires manual step in UI for now due to API limitations)
echo "Project created: $PROJECT_NAME (Number: $PROJECT_NUMBER)"
echo "PMBOK columns added: Initiating, Planning, Executing, Monitoring and Controlling, Closing"
echo "Manual step required: Go to https://github.com/users/$USER/projects/$PROJECT_NUMBER, click Views > Table, and rename to 'PMBOK Task Board'."
