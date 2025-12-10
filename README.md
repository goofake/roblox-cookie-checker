# 🎮 Roblox Cookie Checker - Advanced Edition

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Educational](https://img.shields.io/badge/purpose-educational-green.svg)](https://github.com/goofake/roblox-cookie-checker)

> ⚠️ **IMPORTANT DISCLAIMER**: This tool is for **EDUCATIONAL PURPOSES ONLY**. Only use it to check accounts you **OWN** or have **explicit permission** to access. Unauthorized access to accounts is **ILLEGAL** and violates the Computer Fraud and Abuse Act (CFAA) and similar laws worldwide, as well as Roblox's Terms of Service.

## 📋 Description

Advanced Roblox cookie checker with comprehensive account information retrieval. This tool validates Roblox authentication cookies and provides detailed insights into account status, inventory, games, groups, and more.

## ✨ Features

- ✅ **Cookie Validation** - Verify if cookies are valid and active
- 👤 **User Information** - Extract username, display name, user ID, and account details
- 💰 **Robux Balance** - Check current Robux balance
- ⭐ **Premium Status** - Verify if account has Roblox Premium
- 📦 **Inventory Analysis** - Scan collectible items, hats, gear, faces, accessories, and clothing
- 🎮 **User-Created Games** - Retrieve games created by the user
- 👥 **Groups Information** - List all groups and roles
- 👫 **Friends Count** - Get total number of friends
- ⚡ **Multi-threaded Processing** - Fast checking with 2-3 concurrent threads
- 💾 **Export Results** - Save valid cookies to TXT and detailed data to JSON
- 🎨 **Rich Console Output** - Beautiful formatting with emojis and progress indicators
- 🛡️ **Rate Limiting** - Built-in delays to prevent API bans

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/goofake/roblox-cookie-checker.git
cd roblox-cookie-checker
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively, install manually:

```bash
pip install requests>=2.31.0
```

### Step 3: Prepare Cookies File

1. Copy the example file:
   ```bash
   cp cookies.txt.example cookies.txt
   ```

2. Edit `cookies.txt` and add your Roblox cookies (one per line)

## 🚀 Usage

### Basic Usage

```bash
python roblox_cookie_checker_advanced.py
```

The script will:
1. Read cookies from `cookies.txt`
2. Validate each cookie
3. Retrieve detailed account information
4. Display results in the console
5. Save valid cookies to `valid_cookies_TIMESTAMP.txt`
6. Save detailed account data to `accounts_data.json`

### How to Get Your Roblox Cookie

1. **Log in to Roblox** in your web browser
2. **Open Developer Tools** (F12 or right-click → Inspect)
3. Go to **Application/Storage** tab → **Cookies** → `https://www.roblox.com`
4. Find the `.ROBLOSECURITY` cookie
5. Copy its **entire value** (starts with `_|WARNING:-DO-NOT-SHARE-THIS...`)
6. Paste it into `cookies.txt`

⚠️ **WARNING**: Your `.ROBLOSECURITY` cookie is like a password. Never share it with anyone!

## 📊 Output Examples

### Console Output

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║           🎮 ROBLOX COOKIE CHECKER - ADVANCED 🎮              ║
║                                                               ║
║  ⚠️  EDUCATIONAL PURPOSE ONLY - USE RESPONSIBLY ⚠️            ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

📂 Loading cookies from 'cookies.txt'...
📊 Found 2 cookie(s) to check

⚡ Using 2 thread(s) for processing

======================================================================
🔍 Checking account...
✅ Valid cookie - User: JohnDoe123
💰 Robux: 1500
👫 Friends: 234
👥 Groups: 12
📦 Inventory items: 45
🎮 Games created: 3

✅ VALID ACCOUNT FOUND!
   Username: JohnDoe123
   Display Name: John Doe
   User ID: 123456789
   Robux: 1500 💰
   Premium: Yes ⭐
   Friends: 234 👫
   Groups: 12 👥
   Inventory: 45 📦
======================================================================

📊 SUMMARY:
   Total checked: 2
   ✅ Valid: 1
   ❌ Invalid: 1

💾 Saving results...
💾 Valid cookies saved to: valid_cookies_20241210_123045.txt
💾 Account data saved to: accounts_data.json

✨ Done! Thank you for using Roblox Cookie Checker
⚠️  Remember: Use responsibly and only on accounts you own!
```

### JSON Output Format

The `accounts_data.json` file contains detailed information:

```json
[
  {
    "user_id": 123456789,
    "username": "JohnDoe123",
    "display_name": "John Doe",
    "robux": 1500,
    "premium": true,
    "description": "Pro Roblox developer!",
    "created": "2018-05-15T10:30:00.000Z",
    "is_banned": false,
    "friends_count": 234,
    "groups_count": 12,
    "groups": [
      {
        "name": "Awesome Builders",
        "id": 987654,
        "role": "Owner"
      }
    ],
    "inventory_count": 45,
    "inventory": [
      {
        "name": "Awesome Hat",
        "type": "Hat",
        "item_id": 111222333
      }
    ],
    "games_count": 3,
    "games": [
      {
        "name": "My Epic Game",
        "game_id": 555666777,
        "visits": 10000
      }
    ],
    "checked_at": "2024-12-10T12:30:45.123456"
  }
]
```

## 🔧 Configuration

### Thread Count

By default, the script uses 2-3 threads to avoid rate limiting. This is automatically calculated based on the number of cookies:

```python
max_workers = min(3, len(cookies))
```

### Rate Limiting

The script includes delays between API requests:
- 0.5 seconds between different API calls for the same account
- 1 second between checking different accounts

These delays help prevent API rate limiting and temporary bans.

## 📁 File Structure

```
roblox-cookie-checker/
│
├── roblox_cookie_checker_advanced.py  # Main script
├── requirements.txt                    # Python dependencies
├── cookies.txt.example                 # Example cookies file
├── cookies.txt                         # Your cookies (not tracked by git)
├── LICENSE                             # MIT License
├── README.md                           # This file
├── .gitignore                          # Git ignore rules
│
└── Output files (generated):
    ├── valid_cookies_TIMESTAMP.txt     # Valid cookies export
    └── accounts_data.json              # Detailed account data
```

## 🛡️ Security Warnings

### ⚠️ Critical Security Information

1. **Never share your `.ROBLOSECURITY` cookie** - It provides full access to your account
2. **The `cookies.txt` file is automatically ignored by git** - Your cookies won't be committed
3. **Use strong, unique passwords** for your Roblox accounts
4. **Enable 2-factor authentication** on your Roblox account
5. **Regularly change your password** if you suspect compromise
6. **Don't run this tool on public/shared computers**
7. **Clear cookies.txt after use** if on a shared system

### Protected Files

The following files are automatically excluded from git (in `.gitignore`):
- `cookies.txt` - Your actual cookies
- `valid_cookies*.txt` - Generated valid cookies files
- `accounts_data.json` - Account information export
- Python cache files and virtual environments

## ⚖️ Legal Disclaimer

### Educational Purpose Only

This software is provided **for educational purposes only**. It is designed to help users:
- Understand web API interactions
- Learn about account security
- Check their **OWN** accounts for security purposes

### Terms of Use

By using this software, you agree to:

✅ **You MUST:**
- Only check accounts you **own** or have **explicit written permission** to access
- Comply with **Roblox's Terms of Service**
- Use this tool **responsibly and ethically**
- Accept **full responsibility** for your actions

❌ **You MUST NOT:**
- Access accounts without authorization
- Use this tool for malicious purposes
- Violate any laws or regulations
- Share or distribute cookies belonging to others

### Legal Consequences

**Unauthorized access to computer systems or accounts is ILLEGAL** and may violate:
- **Computer Fraud and Abuse Act (CFAA)** in the United States
- **Computer Misuse Act 1990** in the United Kingdom  
- **Cybercrime laws** in other jurisdictions

Penalties may include:
- Criminal prosecution
- Substantial fines
- Imprisonment
- Civil lawsuits
- Permanent criminal record

### Disclaimer of Liability

The authors and contributors of this software:
- Do **NOT** condone unauthorized access to any accounts
- Are **NOT** responsible for any misuse of this software
- Provide this tool **"as is"** without any warranties
- **Disclaim all liability** for any damages or legal consequences

## 🤝 Contributing

Contributions are welcome! Please ensure any contributions:
- Maintain educational focus
- Include appropriate warnings
- Follow PEP 8 style guidelines
- Add comprehensive comments

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Additional Educational Clause:** This software is intended solely for educational purposes and authorized use only.

## 🔗 Resources

- [Roblox Developer Hub](https://create.roblox.com/docs)
- [Roblox API Documentation](https://roblox.fandom.com/wiki/Roblox_API)
- [Python Requests Library](https://requests.readthedocs.io/)
- [Computer Security Resources](https://www.cisa.gov/cybersecurity)

## ❓ FAQ

### Q: Is this tool safe to use?
**A:** Yes, when used on your **own accounts**. The tool only reads information and doesn't modify anything.

### Q: Will I get banned for using this?
**A:** If used responsibly (2-3 threads, proper delays, own accounts), the risk is minimal. However, excessive use may trigger rate limiting.

### Q: Can I check multiple accounts at once?
**A:** Yes! Add multiple cookies to `cookies.txt`, one per line. The tool will process them with multi-threading.

### Q: What if a cookie is invalid?
**A:** The tool will skip invalid cookies and report them in the summary.

### Q: How often should I check my cookies?
**A:** Cookies typically remain valid until you log out or change your password. Check as needed, but avoid excessive checking.

### Q: Can I modify the script?
**A:** Yes! The code is open-source under MIT License. Feel free to customize it for your needs.

## 🐛 Troubleshooting

### "cookies.txt not found"
Create the file using `cookies.txt.example` as a template.

### "Invalid cookie" errors
- Ensure you copied the **complete** `.ROBLOSECURITY` value
- Check that you're logged in to Roblox
- Try logging out and back in to get a fresh cookie

### Rate limiting errors
- Reduce the number of threads (edit `max_workers` in code)
- Increase delays between requests
- Check fewer cookies at once

### Connection errors
- Check your internet connection
- Verify Roblox services are online
- Try again after a few minutes

## 📧 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/goofake/roblox-cookie-checker/issues)
- **Discussions**: [GitHub Discussions](https://github.com/goofake/roblox-cookie-checker/discussions)

---

**Remember:** This tool is for **educational purposes** and checking **your own accounts** only. Stay safe, stay legal, and use responsibly! 🛡️

Made with ❤️ for the Roblox community
