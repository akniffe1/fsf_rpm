#! /usr/bin/bash
# 
# Add fsf user
if ! id "fsf" >/dev/null 2>&1; then useradd -M fsf
fi
