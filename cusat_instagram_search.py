"""
Instagram Location Search - CUSAT, Kochi, Kerala, India
Educational Purpose Only

This script searches for Instagram locations near CUSAT 
(Cochin University of Science and Technology), Kochi, Kerala, India.

CUSAT Coordinates:
- Latitude: 10.0456
- Longitude: 76.3271
"""

import subprocess
import sys
import os

# CUSAT, Kochi, Kerala coordinates
CUSAT_LAT = 10.0456
CUSAT_LNG = 76.3271

# Output directory
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_location_search(cookie=None, output_formats=None):
    """
    Run the Instagram location search near CUSAT.
    
    Args:
        cookie: Instagram cookie string (optional - will open browser if not provided)
        output_formats: Dict with output format flags and filenames
    """
    
    if output_formats is None:
        output_formats = {
            'csv': os.path.join(OUTPUT_DIR, 'cusat_locations.csv'),
            'json': os.path.join(OUTPUT_DIR, 'cusat_locations.json'),
            'map': os.path.join(OUTPUT_DIR, 'cusat_map.html'),
            'ids': os.path.join(OUTPUT_DIR, 'cusat_location_ids.txt'),
        }
    
    # Build the command
    cmd = [
        'instagram-location-search',
        '--lat', str(CUSAT_LAT),
        '--lng', str(CUSAT_LNG),
    ]
    
    # Add cookie if provided
    if cookie:
        cmd.extend(['--cookie', cookie])
    
    # Add output formats
    for fmt, filepath in output_formats.items():
        cmd.extend([f'--{fmt}', filepath])
    
    print("=" * 60)
    print("Instagram Location Search - CUSAT, Kochi")
    print("=" * 60)
    print(f"\nSearching near coordinates:")
    print(f"  Latitude:  {CUSAT_LAT}")
    print(f"  Longitude: {CUSAT_LNG}")
    print(f"\nLocation: CUSAT (Cochin University of Science and Technology)")
    print(f"          Kochi, Kerala, India")
    print("=" * 60)
    
    if not cookie:
        print("\nNo cookie provided - a browser window will open.")
        print("Please log in to Instagram to authenticate.")
        print("\nNOTE: Your Instagram session ID should be treated like a password!")
    
    print(f"\nOutput files will be saved to: {OUTPUT_DIR}")
    print("\nRunning search...")
    print("-" * 60)
    
    try:
        # Run the command
        result = subprocess.run(cmd, check=True)
        
        print("\n" + "=" * 60)
        print("Search completed successfully!")
        print("=" * 60)
        print("\nGenerated files:")
        for fmt, filepath in output_formats.items():
            if os.path.exists(filepath):
                print(f"  - {filepath}")
        
        print("\nYou can:")
        print("  1. Open cusat_map.html in a browser to visualize locations")
        print("  2. Open cusat_locations.csv in Excel/Google Sheets")
        print("  3. Use cusat_location_ids.txt with instagram-scraper")
        
    except subprocess.CalledProcessError as e:
        print(f"\nError running search: {e}")
        return False
    except FileNotFoundError:
        print("\nError: instagram-location-search not found.")
        print("Please run: pip install instagram-location-search")
        return False
    
    return True


def main():
    """Main entry point."""
    print("\n" + "=" * 60)
    print("  INSTAGRAM LOCATION SEARCH - CUSAT KOCHI")
    print("  For Educational Purposes Only")
    print("=" * 60)
    
    # Check if cookie was provided as argument
    cookie = None
    if len(sys.argv) > 1:
        cookie = sys.argv[1]
        print("\nUsing provided cookie for authentication.")
    else:
        print("\nNo cookie provided.")
        print("A Chrome browser will open for you to log in to Instagram.")
        print("\nTo skip browser login, you can run:")
        print('  python cusat_instagram_search.py "YOUR_COOKIE_STRING"')
    
    input("\nPress Enter to continue...")
    
    run_location_search(cookie=cookie)


if __name__ == "__main__":
    main()
