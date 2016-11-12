# proj7-Gcal

Author: Holden Oullette, hjo@uoregon.edu

This is the beginning of a Meeting Time webapp, currently connects to Google services
using oauth2 and requests read permissions for the Calendar API. The app then displays
conflicting events with the user's requested time slots.

## Installation & Deployment ##

```bash
git clone https://github.com/houllette/proj7-Gcal
cd proj7-Gcal
./configure
source env/bin/activate
make run
```