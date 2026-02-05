"""
Instagram Profile Viewer - Educational Purpose Only

This script helps you view publicly available information
from an Instagram profile.

IMPORTANT: This only accesses PUBLIC information that anyone
can see by visiting the profile. Respect privacy and Instagram's ToS.
"""

import webbrowser
import sys


def view_instagram_profile(username):
    """
    Opens the Instagram profile page for a given username.
    
    This is the legitimate way to view someone's public profile info:
    - Bio
    - Public posts
    - Tagged locations in their posts
    - Any contact info they've chosen to make public
    """
    username = username.strip().lstrip('@')
    
    if not username:
        print("No username provided.")
        return
    
    profile_url = f"https://www.instagram.com/{username}/"
    
    print("\n" + "=" * 60)
    print(f"  Instagram Profile: @{username}")
    print("=" * 60)
    print(f"\nProfile URL: {profile_url}")
    print("\nPublicly available information on Instagram profiles:")
    print("  - Display name and bio")
    print("  - Profile picture")
    print("  - Public posts (if account is not private)")
    print("  - Location tags on their posts")
    print("  - Contact buttons (if they've enabled them)")
    print("  - Links in bio")
    print("  - Follower/following count")
    print("\n" + "-" * 60)
    
    open_browser = input("Open profile in browser? (y/n): ").strip().lower()
    
    if open_browser == 'y':
        print(f"\nOpening {profile_url} in your browser...")
        webbrowser.open(profile_url)
    
    print("\n" + "-" * 60)
    print("TIPS FOR FINDING CONTACT INFO:")
    print("-" * 60)
    print("""
1. CHECK THEIR BIO
   - Many users put contact info, email, or links in their bio
   - Look for "Contact" or "Email" buttons on business accounts

2. CHECK THEIR LINK IN BIO
   - Often leads to a Linktree or personal website with more info

3. LOOK AT THEIR POSTS
   - Posts tagged at CUSAT locations might confirm they're nearby
   - Business posts may contain contact details

4. BUSINESS ACCOUNTS
   - Business/Creator accounts may show:
     * Email button
     * Phone button  
     * Address
     * Business category

5. CONNECTED ACCOUNTS
   - Check if they've linked other social media
   - Facebook, Twitter, YouTube links may have more info
""")
    
    # Also show the CUSAT location URLs for cross-reference
    print("\n" + "-" * 60)
    print("CUSAT AREA INSTAGRAM LOCATIONS:")
    print("-" * 60)
    print("Check if they've posted at any of these locations:\n")
    
    cusat_locations = [
        ("CUSAT Main", "https://www.instagram.com/explore/locations/110239289004365"),
        ("Cochin University", "https://www.instagram.com/explore/locations/108304335856378"),
        ("CUSAT Science Park", "https://www.instagram.com/explore/locations/112012320244256"),
        ("School of Engineering CUSAT", "https://www.instagram.com/explore/locations/104022516300858"),
        ("School of Legal Studies CUSAT", "https://www.instagram.com/explore/locations/333572720106408"),
        ("Kalamassery", "https://www.instagram.com/explore/locations/128591473842836"),
    ]
    
    for name, url in cusat_locations:
        print(f"  {name}")
        print(f"    {url}\n")


def main():
    print("\n" + "=" * 60)
    print("  INSTAGRAM PROFILE VIEWER")
    print("  Educational Purpose Only")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("\nEnter Instagram username: @")
    
    view_instagram_profile(username)
    
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
