#!/bin/bash

PROFILE_FILE=$(date "+%d-%b-%Y-%H:%M")-profile.bin

memray run --follow-fork -o /app/profiles/$PROFILE_FILE -m gunicorn app:app -b 0.0.0.0:8000 --timeout 600 --access-logfile "-" --error-logfile "-"
