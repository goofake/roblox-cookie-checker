#!/usr/bin/env python3
"""
Roblox Cookie Checker - Advanced Edition

⚠️  EDUCATIONAL PURPOSE ONLY ⚠️
This tool is designed for checking YOUR OWN Roblox account information.
Unauthorized access to accounts you don't own is ILLEGAL.

Features:
- Cookie validation
- Username and Display Name extraction
- Robux balance checking
- Premium status verification
- Full inventory analysis
- Recent games played
- Groups information
- Friends count
- Multi-threaded processing
- Export to TXT and JSON formats
"""

import requests
import json
import time
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Optional, Any


class RobloxCookieChecker:
    """
    Advanced Roblox cookie checker with comprehensive account information retrieval.

    This class provides methods to validate Roblox authentication cookies and
    retrieve detailed account information including inventory, games, groups, etc.
    """

    def __init__(self, cookie: str):
        """
        Initialize the cookie checker with a Roblox authentication cookie.

        Args:
            cookie (str): The .ROBLOSECURITY cookie value
        """
        self.cookie = cookie.strip()
        self.session = requests.Session()
        self.session.cookies.set('.ROBLOSECURITY', self.cookie, domain='.roblox.com')
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        })
        self.user_data: Dict[str, Any] = {}

    def validate_cookie(self) -> bool:
        """
        Validate the Roblox cookie by attempting to retrieve user information.

        Returns:
            bool: True if cookie is valid, False otherwise
        """
        try:
            response = self.session.get(
                'https://www.roblox.com/mobileapi/userinfo',
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                if 'UserID' in data and data['UserID']:
                    self.user_data['user_id'] = data['UserID']
                    self.user_data['username'] = data.get('UserName', 'Unknown')
                    self.user_data['robux'] = data.get('RobuxBalance', 0)
                    self.user_data['premium'] = data.get('IsPremium', False)
                    return True
            return False
        except Exception as e:
            print(f"❌ Error validating cookie: {e}")
            return False

    def get_user_info(self) -> Optional[Dict[str, Any]]:
        """
        Retrieve detailed user information from Roblox API.

        Returns:
            Optional[Dict]: User information dictionary or None if failed
        """
        if 'user_id' not in self.user_data:
            return None

        try:
            user_id = self.user_data['user_id']
            response = self.session.get(
                f'https://users.roblox.com/v1/users/{user_id}',
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                self.user_data['display_name'] = data.get('displayName', 'N/A')
                self.user_data['description'] = data.get('description', 'N/A')
                self.user_data['created'] = data.get('created', 'N/A')
                self.user_data['is_banned'] = data.get('isBanned', False)
                return data
            return None
        except Exception as e:
            print(f"⚠️  Error getting user info: {e}")
            return None

    def get_robux_balance(self) -> int:
        """
        Get the current Robux balance for the account.

        Returns:
            int: Robux balance or 0 if unable to retrieve
        """
        if 'user_id' not in self.user_data:
            return 0

        try:
            user_id = self.user_data['user_id']
            response = self.session.get(
                f'https://economy.roblox.com/v1/users/{user_id}/currency',
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                robux = data.get('robux', 0)
                self.user_data['robux'] = robux
                return robux
            return 0
        except Exception as e:
            print(f"⚠️  Error getting Robux balance: {e}")
            return 0

    def get_inventory(self, limit: int = 50) -> List[Dict[str, Any]]:
        """
        Retrieve user's collectible inventory items.

        Args:
            limit (int): Maximum number of items to retrieve

        Returns:
            List[Dict]: List of inventory items
        """
        if 'user_id' not in self.user_data:
            return []

        inventory_items = []
        try:
            user_id = self.user_data['user_id']

            # Get collectibles
            response = self.session.get(
                f'https://inventory.roblox.com/v1/users/{user_id}/assets/collectibles',
                params={'limit': limit, 'sortOrder': 'Desc'},
                timeout=15
            )

            if response.status_code == 200:
                data = response.json()
                items = data.get('data', [])

                for item in items:
                    inventory_items.append({
                        'name': item.get('name', 'Unknown'),
                        'type': item.get('assetType', 'Unknown'),
                        'item_id': item.get('assetId', 0),
                    })

            self.user_data['inventory_count'] = len(inventory_items)
            time.sleep(0.5)  # Rate limiting
            return inventory_items
        except Exception as e:
            print(f"⚠️  Error getting inventory: {e}")
            return inventory_items

    def get_recent_games(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Retrieve games created by the user.

        Args:
            limit (int): Maximum number of games to retrieve

        Returns:
            List[Dict]: List of games created by the user
        """
        if 'user_id' not in self.user_data:
            return []

        games = []
        try:
            user_id = self.user_data['user_id']
            response = self.session.get(
                f'https://games.roblox.com/v1/users/{user_id}/games',
                params={'limit': limit, 'sortOrder': 'Desc'},
                timeout=15
            )

            if response.status_code == 200:
                data = response.json()
                game_data = data.get('data', [])

                for game in game_data:
                    games.append({
                        'name': game.get('name', 'Unknown'),
                        'game_id': game.get('id', 0),
                        'visits': game.get('placeVisits', 0),
                    })

            self.user_data['games_count'] = len(games)
            time.sleep(0.5)  # Rate limiting
            return games
        except Exception as e:
            print(f"⚠️  Error getting games: {e}")
            return games

    def get_groups(self) -> List[Dict[str, Any]]:
        """
        Retrieve user's group memberships and roles.

        Returns:
            List[Dict]: List of groups with roles
        """
        if 'user_id' not in self.user_data:
            return []

        groups = []
        try:
            user_id = self.user_data['user_id']
            response = self.session.get(
                f'https://groups.roblox.com/v1/users/{user_id}/groups/roles',
                timeout=15
            )

            if response.status_code == 200:
                data = response.json()
                group_data = data.get('data', [])

                for group_info in group_data:
                    group = group_info.get('group', {})
                    role = group_info.get('role', {})
                    groups.append({
                        'name': group.get('name', 'Unknown'),
                        'id': group.get('id', 0),
                        'role': role.get('name', 'Member'),
                    })

            self.user_data['groups_count'] = len(groups)
            time.sleep(0.5)  # Rate limiting
            return groups
        except Exception as e:
            print(f"⚠️  Error getting groups: {e}")
            return groups

    def get_friends_count(self) -> int:
        """
        Get the total number of friends for the account.

        Returns:
            int: Number of friends or 0 if unable to retrieve
        """
        if 'user_id' not in self.user_data:
            return 0

        try:
            user_id = self.user_data['user_id']
            response = self.session.get(
                f'https://friends.roblox.com/v1/users/{user_id}/friends/count',
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                friends_count = data.get('count', 0)
                self.user_data['friends_count'] = friends_count
                return friends_count
            return 0
        except Exception as e:
            print(f"⚠️  Error getting friends count: {e}")
            return 0

    def get_full_account_info(self) -> Dict[str, Any]:
        """
        Retrieve all available account information.

        Returns:
            Dict: Complete account information
        """
        print(f"🔍 Checking account...")

        if not self.validate_cookie():
            print("❌ Invalid cookie")
            return {}

        print(f"✅ Valid cookie - User: {self.user_data.get('username', 'Unknown')}")

        # Get detailed user info
        self.get_user_info()

        # Get Robux balance
        robux = self.get_robux_balance()
        print(f"💰 Robux: {robux}")

        # Get friends count
        friends = self.get_friends_count()
        print(f"👫 Friends: {friends}")

        # Get groups
        groups = self.get_groups()
        print(f"👥 Groups: {len(groups)}")

        # Get inventory
        inventory = self.get_inventory()
        print(f"📦 Inventory items: {len(inventory)}")

        # Get recent games
        games = self.get_recent_games()
        print(f"🎮 Games created: {len(games)}")

        # Store additional data
        self.user_data['groups'] = groups
        self.user_data['inventory'] = inventory
        self.user_data['games'] = games
        self.user_data['checked_at'] = datetime.now().isoformat()

        return self.user_data


def check_cookie(cookie: str) -> Optional[Dict[str, Any]]:
    """
    Helper function to check a single cookie.

    Args:
        cookie (str): Roblox authentication cookie

    Returns:
        Optional[Dict]: Account data if valid, None otherwise
    """
    checker = RobloxCookieChecker(cookie)
    return checker.get_full_account_info()


def load_cookies(filename: str = 'cookies.txt') -> List[str]:
    """
    Load cookies from a text file.

    Args:
        filename (str): Path to cookies file

    Returns:
        List[str]: List of cookies
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            cookies = [
                line.strip()
                for line in f
                if line.strip() and not line.strip().startswith('#')
            ]
        return cookies
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found!")
        print("📝 Create a 'cookies.txt' file with your cookies (one per line)")
        print("💡 See 'cookies.txt.example' for format")
        return []


def save_valid_cookies(valid_accounts: List[Dict[str, Any]]) -> None:
    """
    Save valid cookies to a text file.

    Args:
        valid_accounts (List[Dict]): List of valid account data
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'valid_cookies_{timestamp}.txt'

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for account in valid_accounts:
                username = account.get('username', 'Unknown')
                robux = account.get('robux', 0)
                premium = '⭐' if account.get('premium', False) else ''
                f.write(f"# {username} - {robux} Robux {premium}\n")
                f.write(f"{account.get('cookie', '')}\n\n")

        print(f"💾 Valid cookies saved to: {filename}")
    except Exception as e:
        print(f"❌ Error saving cookies: {e}")


def save_accounts_json(accounts_data: List[Dict[str, Any]]) -> None:
    """
    Save account data to a JSON file.

    Args:
        accounts_data (List[Dict]): List of account data
    """
    try:
        filename = 'accounts_data.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(accounts_data, f, indent=2, ensure_ascii=False)

        print(f"💾 Account data saved to: {filename}")
    except Exception as e:
        print(f"❌ Error saving JSON: {e}")


def print_banner():
    """Print the application banner with warnings."""
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║           🎮 ROBLOX COOKIE CHECKER - ADVANCED 🎮              ║
║                                                               ║
║  ⚠️  EDUCATIONAL PURPOSE ONLY - USE RESPONSIBLY ⚠️            ║
║                                                               ║
║  Features:                                                    ║
║  ✅ Cookie Validation                                         ║
║  👤 User Info Extraction                                      ║
║  💰 Robux Balance                                             ║
║  ⭐ Premium Status                                            ║
║  📦 Inventory Analysis                                        ║
║  🎮 Games History                                             ║
║  👥 Groups Information                                        ║
║  👫 Friends Count                                             ║
║                                                               ║
║  ⚖️  Legal Notice:                                            ║
║  Only check accounts you OWN or have permission to access.   ║
║  Unauthorized access is ILLEGAL and violates Terms of        ║
║  Service. You are responsible for your actions.              ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def main():
    """Main execution function."""
    print_banner()

    # Load cookies
    print("\n📂 Loading cookies from 'cookies.txt'...")
    cookies = load_cookies()

    if not cookies:
        sys.exit(1)

    print(f"📊 Found {len(cookies)} cookie(s) to check\n")

    valid_accounts = []
    invalid_count = 0

    # Use ThreadPoolExecutor for multi-threaded processing
    # Using 2-3 threads to avoid rate limiting
    max_workers = min(3, len(cookies))

    print(f"⚡ Using {max_workers} thread(s) for processing\n")
    print("=" * 70)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_cookie = {
            executor.submit(check_cookie, cookie): cookie
            for cookie in cookies
        }

        # Process completed tasks
        for future in as_completed(future_to_cookie):
            cookie = future_to_cookie[future]
            try:
                account_data = future.result()

                if account_data and 'user_id' in account_data:
                    account_data['cookie'] = cookie
                    valid_accounts.append(account_data)

                    # Display summary
                    print("\n✅ VALID ACCOUNT FOUND!")
                    print(f"   Username: {account_data.get('username', 'N/A')}")
                    print(f"   Display Name: {account_data.get('display_name', 'N/A')}")
                    print(f"   User ID: {account_data.get('user_id', 'N/A')}")
                    print(f"   Robux: {account_data.get('robux', 0)} 💰")
                    print(f"   Premium: {'Yes ⭐' if account_data.get('premium', False) else 'No'}")
                    print(f"   Friends: {account_data.get('friends_count', 0)} 👫")
                    print(f"   Groups: {account_data.get('groups_count', 0)} 👥")
                    print(f"   Inventory: {account_data.get('inventory_count', 0)} 📦")
                else:
                    invalid_count += 1
                    print(f"\n❌ Invalid cookie #{invalid_count}")

            except Exception as e:
                invalid_count += 1
                print(f"\n❌ Error checking cookie: {e}")

            print("=" * 70)

            # Add delay between requests to avoid rate limiting
            time.sleep(1)

    # Print summary
    print("\n" + "=" * 70)
    print("\n📊 SUMMARY:")
    print(f"   Total checked: {len(cookies)}")
    print(f"   ✅ Valid: {len(valid_accounts)}")
    print(f"   ❌ Invalid: {invalid_count}")

    # Save results
    if valid_accounts:
        print("\n💾 Saving results...")
        save_valid_cookies(valid_accounts)
        save_accounts_json(valid_accounts)

    print("\n✨ Done! Thank you for using Roblox Cookie Checker")
    print("⚠️  Remember: Use responsibly and only on accounts you own!\n")


if __name__ == '__main__':
    main()
