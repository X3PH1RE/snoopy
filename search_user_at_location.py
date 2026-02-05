"""
Search for Instagram posts by a specific user at locations near CUSAT, Kochi

Educational Purpose Only

This is a two-step process:
1. Find Instagram location IDs near CUSAT using instagram-location-search
2. (Optional) Use instagram-scraper to get posts at those locations

IMPORTANT: This tool respects Instagram's Terms of Service.
Use responsibly and only for educational purposes.
"""

import subprocess
import sys
import os
import csv

# CUSAT, Kochi, Kerala coordinates
CUSAT_LAT = 10.0456
CUSAT_LNG = 76.3271

# Output directory
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def step1_find_locations(cookie=None):
    """
    Step 1: Find Instagram location IDs near CUSAT.
    """
    print("\n" + "=" * 60)
    print("STEP 1: Finding Instagram locations near CUSAT")
    print("=" * 60)
    
    output_files = {
        'csv': os.path.join(OUTPUT_DIR, 'cusat_locations.csv'),
        'json': os.path.join(OUTPUT_DIR, 'cusat_locations.json'),
        'map': os.path.join(OUTPUT_DIR, 'cusat_map.html'),
        'ids': os.path.join(OUTPUT_DIR, 'cusat_location_ids.txt'),
    }
    
    cmd = [
        'instagram-location-search',
        '--lat', str(CUSAT_LAT),
        '--lng', str(CUSAT_LNG),
    ]
    
    if cookie:
        cmd.extend(['--cookie', cookie])
    
    for fmt, filepath in output_files.items():
        cmd.extend([f'--{fmt}', filepath])
    
    print(f"\nSearching near: {CUSAT_LAT}, {CUSAT_LNG}")
    print("(CUSAT, Kochi, Kerala, India)")
    
    if not cookie:
        print("\nA browser window will open for Instagram login...")
    
    try:
        result = subprocess.run(cmd, check=True)
        print("\n✓ Location search completed!")
        
        # Count locations found
        ids_file = output_files['ids']
        if os.path.exists(ids_file):
            with open(ids_file, 'r') as f:
                location_count = len(f.readlines())
            print(f"✓ Found {location_count} locations near CUSAT")
        
        return output_files
        
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error: {e}")
        return None
    except FileNotFoundError:
        print("\n✗ Error: instagram-location-search not found")
        print("  Run: pip install instagram-location-search")
        return None


def display_locations(csv_file):
    """Display found locations from the CSV file."""
    if not os.path.exists(csv_file):
        print("No locations file found.")
        return
    
    print("\n" + "-" * 60)
    print("LOCATIONS FOUND NEAR CUSAT:")
    print("-" * 60)
    
    try:
        # Try different encodings
        encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252', 'iso-8859-1']
        locations = None
        
        for encoding in encodings:
            try:
                with open(csv_file, 'r', encoding=encoding) as f:
                    reader = csv.DictReader(f)
                    locations = list(reader)
                break  # Success, exit the loop
            except UnicodeDecodeError:
                continue
        
        if locations is None:
            # Fallback: read with errors='replace'
            with open(csv_file, 'r', encoding='utf-8', errors='replace') as f:
                reader = csv.DictReader(f)
                locations = list(reader)
            
        # Display first 20 locations
        for i, loc in enumerate(locations[:20], 1):
            name = loc.get('name', 'Unknown')
            address = loc.get('address', '')
            # Try both 'external_id' and 'id' as column name
            loc_id = loc.get('external_id', loc.get('id', ''))
            url = loc.get('url', '')
            print(f"{i:3}. {name}")
            if address:
                print(f"     Address: {address}")
            if loc_id:
                print(f"     ID: {loc_id}")
            if url:
                print(f"     URL: {url}")
            print()
        
        if len(locations) > 20:
            print(f"... and {len(locations) - 20} more locations")
            print(f"See full list in: {csv_file}")
            
    except Exception as e:
        print(f"Error reading locations: {e}")


def step2_search_user_posts(username, credentials_file=None):
    """
    Step 2: Search for posts by a specific user at the found locations.
    
    This uses instagram-scraper (if installed).
    """
    print("\n" + "=" * 60)
    print(f"STEP 2: Search for posts by @{username}")
    print("=" * 60)
    
    ids_file = os.path.join(OUTPUT_DIR, 'cusat_location_ids.txt')
    
    if not os.path.exists(ids_file):
        print("\n✗ Location IDs file not found. Run Step 1 first.")
        return
    
    # Check if instagram-scraper is installed
    try:
        result = subprocess.run(['instagram-scraper', '--help'], 
                                capture_output=True, text=True)
    except FileNotFoundError:
        print("\n⚠ instagram-scraper is not installed.")
        print("\nTo install, run:")
        print("  pip install instagram-scraper")
        print("\nAlternatively, you can manually search for the user on Instagram")
        print("and check if they've posted at any of the locations found in Step 1.")
        return
    
    # Build command for instagram-scraper
    output_dir = os.path.join(OUTPUT_DIR, f'posts_{username}')
    
    cmd = [
        'instagram-scraper',
        '--filename', ids_file,
        '--location',
        '--include-location',
        '--destination', output_dir,
    ]
    
    if credentials_file and os.path.exists(credentials_file):
        cmd.insert(1, f'@{credentials_file}')
    
    print(f"\nThis will search for posts at all locations found near CUSAT.")
    print(f"Output will be saved to: {output_dir}")
    print("\n⚠ Note: instagram-scraper uses an undocumented API.")
    print("  Results may vary and this might not always work.")
    
    proceed = input("\nProceed with search? (y/n): ")
    if proceed.lower() != 'y':
        print("Search cancelled.")
        return
    
    try:
        subprocess.run(cmd)
    except Exception as e:
        print(f"\nError: {e}")


def manual_search_guide(username):
    """Provide guide for manual search."""
    print("\n" + "=" * 60)
    print(f"MANUAL SEARCH GUIDE FOR @{username}")
    print("=" * 60)
    
    csv_file = os.path.join(OUTPUT_DIR, 'cusat_locations.csv')
    
    print("""
To manually check if a user has posted at locations near CUSAT:

1. Open the cusat_map.html file in your browser
   - This shows all Instagram locations near CUSAT on a map
   
2. Click on location markers to see location names

3. On Instagram, go to each location page:
   - Open Instagram.com
   - Go to: instagram.com/explore/locations/[LOCATION_ID]
   - Browse posts at that location
   - Look for posts by the username you're interested in

4. Alternatively, check the user's profile:
   - Go to instagram.com/{username}
   - Look at their posts
   - Check if any posts are tagged at CUSAT area locations
""")
    
    print(f"\nYour target username: @{username}")
    print(f"Locations CSV file: {csv_file}")
    print(f"Interactive map: {os.path.join(OUTPUT_DIR, 'cusat_map.html')}")


def main():
    print("\n" + "=" * 60)
    print("  INSTAGRAM USER LOCATION SEARCH")
    print("  CUSAT, Kochi, Kerala, India")
    print("  Educational Purpose Only")
    print("=" * 60)
    
    # Get username
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("\nEnter Instagram username to search for: @")
    
    username = username.strip().lstrip('@')
    
    if not username:
        print("No username provided. Exiting.")
        return
    
    print(f"\nTarget username: @{username}")
    
    # Menu
    print("\n" + "-" * 60)
    print("OPTIONS:")
    print("-" * 60)
    print("1. Find all Instagram locations near CUSAT")
    print("2. Display found locations")
    print("3. Guide for manually searching user's posts")
    print("4. Run full automated search (requires instagram-scraper)")
    print("5. Exit")
    print("-" * 60)
    
    choice = input("\nSelect option (1-5): ").strip()
    
    if choice == '1':
        cookie = input("\nPaste Instagram cookie (or press Enter to use browser login): ").strip()
        if not cookie:
            cookie = None
        output_files = step1_find_locations(cookie)
        if output_files:
            display_locations(output_files['csv'])
            
    elif choice == '2':
        csv_file = os.path.join(OUTPUT_DIR, 'cusat_locations.csv')
        display_locations(csv_file)
        
    elif choice == '3':
        manual_search_guide(username)
        
    elif choice == '4':
        # First run location search
        cookie = input("\nPaste Instagram cookie (or press Enter to use browser login): ").strip()
        if not cookie:
            cookie = None
        output_files = step1_find_locations(cookie)
        
        if output_files:
            display_locations(output_files['csv'])
            step2_search_user_posts(username)
            
    elif choice == '5':
        print("\nGoodbye!")
        return
    else:
        print("\nInvalid option.")
    
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
