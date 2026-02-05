# Snoopy - Instagram Location Sleuth - CUSAT Edition

> "Find Instagram hotspots near campus. Or figure out if that account is actually from around here."

A Python toolkit for discovering Instagram locations around CUSAT (Cochin University of Science and Technology), Kochi. Use it to explore tagged spots or cross-reference whether an account posts from the area.

---

## Can Do

- Find Instagram spots near CUSAT
- Make a pretty map of those spots
- Help you figure out if someone actually posts from this area
- Export everything to CSV, JSON, and HTML

## Cannot Do

- Hack into private accounts (obviously)
- Read minds, DMs, or anything Instagram hides
- Give you info people didn't make public themselves
- Work magic without you logging in first

---

## Files

| File | Purpose |
|------|---------|
| `cusat_instagram_search.py` | Main location search script |
| `search_user_at_location.py` | Interactive menu with user search features |
| `view_profile.py` | Opens profiles, shows tips for finding public info |
| `run_search.bat` | Quick launcher (double-click) |
| `search_user.bat` | Quick launcher for user search |

---

## Setup

**Requirements:** Python 3.8+, Google Chrome, Instagram account

**Install:**
```bash
pip install instagram-location-search
```

---

## Usage

### Find Locations Near CUSAT
```bash
python cusat_instagram_search.py
```
Chrome opens, you log into Instagram, locations get saved.

### Check If An Account Is From This Area
```bash
python search_user_at_location.py
```
1. Run option 1 to get all CUSAT-area locations
2. Visit the location URLs to see who posts there
3. Cross-reference with the account you're investigating

### View A Profile
```bash
python view_profile.py
```
Opens the profile and shows where to find public contact info.

---

## Output Files

After running, you get:
- `cusat_locations.csv` - Spreadsheet of all locations
- `cusat_locations.json` - Same data, JSON format
- `cusat_map.html` - Interactive map (open in browser)
- `cusat_location_ids.txt` - Just the IDs

---

## Coordinates

```
CUSAT, Kochi, Kerala, India
Lat: 10.0456 | Lng: 76.3271
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Chrome won't open | Install Google Chrome (not Chromium/Brave) |
| Package not found | Run `pip install instagram-location-search` |
| Session expired | Log into Instagram again |

---

## Credits

Built on [Bellingcat's instagram-location-search](https://github.com/bellingcat/instagram-location-search).

---

*For educational purposes. Don't be creepy.*
