# 🕵️‍♂️ SocialPhish - Advanced Phishing Tool

![SocialPhish Banner](https://via.placeholder.com/800x200?text=SocialPhish+Advanced+Phishing+Tool)

---

## ⚠️ Disclaimer

**This tool is for educational purposes only. The developer is not responsible for any misuse of this software. Always ensure you have proper authorization before testing any system. Unauthorized access to computer systems is illegal.**

---

## 📖 Overview

SocialPhish is a sophisticated phishing tool designed for ethical hacking, penetration testing, and cybersecurity education. It enables security professionals to simulate real-world phishing attacks and assess social engineering vulnerabilities using a wide range of templates and data capture techniques.

---

## ✨ Features

- **33+ Pre-built Templates** for popular platforms:
  - Social Media: Facebook, Instagram, Twitter, Snapchat
  - Email Services: Gmail, Yahoo, ProtonMail
  - Streaming: Netflix, Spotify
  - Payment: PayPal, Shopify
  - Gaming: Steam, Origin
  - And more...

- **Custom Page Creation**: Build personalized phishing pages with custom text and fields  
- **Real-time Credential Capture**: Instant alerts when credentials are submitted  
- **IP Address Tracking**: Geolocation and ISP detection  
- **User-Agent Detection**: Identify victim's browser and device  
- **Built-in PHP Server**: No external web server required  
- **Detailed Victim Information**:
  - IP Address
  - Geographical Location
  - ISP Details
  - Browser & Device Info

---

## 🛠️ Installation

### Prerequisites
- PHP (pre-installed on most Linux distros)
- curl
- git

### Setup Instructions
```bash
git clone https://github.com/xHak9x/SocialPhish.git
   ```
```bash
cd SocialPhish
   ```
```bash
chmod +x socialphish.sh
   ```
```bash
./socialphish.sh
   ```

1. Launch the tool:
   ```bash
   ./socialphish.sh
   ```

2. Select a phishing template (options 1–33)  
3. Choose a port (default: 8080)  
4. Share the generated link with the target  
5. Wait for credentials to be captured  
6. View captured data: usernames, passwords, IP info

### 🧪 Custom Phishing Pages
Use option 33 to create your own phishing page:
- Custom titles and messages  
- Personalized form field labels  
- Custom submit button text  

---

## 🔍 Technical Details

### Captured Information
- Usernames and passwords  
- IP address with geolocation  
- ISP and device/browser info  

### Network Requirements
- Local PHP server setup  
- For external access: configure port forwarding or use tools like **ngrok**

---

## 🛡️ Protection Against Phishing

### For Users
- Verify URLs before entering credentials  
- Use two-factor authentication  
- Avoid unexpected login prompts  
- Use password managers with phishing detection

### For Organizations
- Conduct regular security awareness training  
- Implement email and web filtering  
- Patch systems and update software regularly

---

## ⚖️ Legal & Ethical Use

- Always obtain proper authorization before testing  
- Never use this tool maliciously or without consent  
- Respect privacy laws and local regulations  
- Disclose testing activities to stakeholders

---

## 🎯 Common Use Cases

- Security awareness training  
- Penetration testing  
- Cybersecurity education  
- Research on phishing techniques

---

## 🧰 Troubleshooting

### Common Issues
1. **PHP not found**:  
   ```bash
   sudo apt install php
   ```
2. **Port conflict**: Choose a different port  
3. **No credentials captured**: Check firewall and network settings

### Solutions
- Ensure no other services are using the selected port  
- Confirm target can access your server IP  
- Disable antivirus/firewall if blocking the tool

---

## 🤝 Contributing

We welcome contributions to improve SocialPhish!

1. Fork the repository  
2. Create a feature branch  
3. Make your changes  
4. Test thoroughly  
5. Submit a pull request

### Suggested Improvements
- More phishing templates  
- Enhanced evasion techniques  
- Improved logging  
- Mobile compatibility

---

## 👤 Credits

- **Developer**: Hak9 ([GitHub](https://github.com/xHak9x))  
- **Inspired by**: SocialFish by UndeadSec  
- **Community**: Thanks to all contributors and testers

---

## 💬 Support

For questions or issues:
1. Check existing GitHub issues  
2. Open a new issue with details  
3. Include steps to reproduce the problem

---

## 📦 Version Info

- **Current Version**: 1.6  
- **Compatibility**: Linux, macOS (with tweaks), Windows (via WSL)  
- **Release Date**: See GitHub for latest updates

---

> **Reminder**: With great power comes great responsibility. Use this tool ethically and legally.

![Footer](https://via.placeholder.com/800x100?text=Use+Responsibly+-+Ethical+Hacking+Only)
