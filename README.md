# 🔐 ROT Cipher Tool

A beautiful, interactive terminal-based cipher tool supporting customizable ROT encryption and decryption with stunning ASCII art, colorized output, and comprehensive logging.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Terminal](https://img.shields.io/badge/Interface-Terminal-black?logo=gnu-bash)

## ✨ Features

### 🎨 Visual Experience
- **Stunning ASCII Art**: Eye-catching ROT CIPHER logo on startup
- **Animated Effects**: Typewriter text animation and loading dots
- **Colorized Output**: Color-coded terminal interface for better readability
- **Clean Interface**: Professional menu system with clear navigation

### 🔒 Encryption Capabilities
- **Multiple ROT Values**: Support for ROT1 through ROT25 (not just ROT13)
- **Case Preservation**: Maintains original uppercase/lowercase formatting
- **Character Handling**: Non-alphabetic characters remain unchanged
- **Bidirectional**: Both encoding and decoding functionality

### 📊 Advanced Features
- **Operation Logging**: Automatic saving to `rot_cipher_history.txt`
- **History Viewer**: Browse recent encoding/decoding operations
- **Error Handling**: Comprehensive input validation and error management
- **Session Persistence**: Continue multiple operations in a single session

## 🚀 Quick Start

### Requirements
- Python 3.6 or higher
- No external dependencies (uses only standard libraries)

### Installation
1. Download the `rot_cipher_tool.py` file
2. Make it executable (Linux/Mac):
   ```bash
   chmod +x rot_cipher_tool.py
   ```

### Usage
Run the program:
```bash
python rot_cipher_tool.py
```
or
```bash
python3 rot_cipher_tool.py
```

## 📋 Menu Options

| Option | Description |
|--------|-------------|
| **[1] Encode Text** | Encrypt plain text using ROT cipher |
| **[2] Decode Text** | Decrypt ROT-encoded text |
| **[3] Change ROT Value** | Modify rotation value (1-25) |
| **[4] View History** | Display recent operations |
| **[5] Exit** | Close the program |

## 🎯 Example Session

```
    ██████╗  ██████╗ ████████╗     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔═══██╗╚══██╔══╝    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
    ██████╔╝██║   ██║   ██║       ██║     ██║██████╔╝███████║█████╗  ██████╔╝
    ██╔══██╗██║   ██║   ██║       ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
    ██║  ██║╚██████╔╝   ██║       ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝    ╚═╝        ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                         🔐 ROT CIPHER TOOL v1.0 by SPLO1T 🔐
================================================================================

MAIN MENU
========================================
[1] Encode Text
[2] Decode Text
[3] Change ROT Value (Current: 13)
[4] View History
[5] Exit
========================================

Choose an option (1-5): 1

🔒 ENCODE MODE (ROT13)
----------------------------------------
Enter text to encode: Hello World!

Original: Hello World!
Encoded: Uryyb Jbeyq!
✓ Saved to rot_cipher_history.txt
```

## 🛠️ How ROT Cipher Works

ROT (rotation) cipher is a simple letter substitution cipher that replaces each letter with a letter a fixed number of positions down the alphabet.

### Examples:
- **ROT13**: A ↔ N, B ↔ O, C ↔ P
- **ROT5**: A ↔ F, B ↔ G, C ↔ H
- **ROT25**: A ↔ Z, B ↔ A, C ↔ B

### Rules:
- ✅ Alphabetic characters are rotated
- ✅ Case is preserved (A→N, a→n)
- ✅ Numbers and symbols remain unchanged
- ✅ Wrapping: Z+1 = A, z+1 = a

## 📁 File Structure

```
rot-cipher-tool/
├── rotcipher.py                # Main program file
├── rot_cipher_history.txt      # Auto-generated log file
└── README.md                   # This documentation
```

## 📝 Log File Format

The tool automatically creates `rot_cipher_history.txt` with the following format:

```
[2024-01-15 14:30:25] ENCODE (ROT13)
Original: Hello World!
Result:   Uryyb Jbeyq!
--------------------------------------------------
[2024-01-15 14:31:10] DECODE (ROT13)
Original: Uryyb Jbeyq!
Result:   Hello World!
--------------------------------------------------
```

## 🎨 Visual Features

The tool provides an enhanced terminal experience with:
- **Colorized Output**: Different text colors for better readability
- **ASCII Art**: Professional logo display
- **Animations**: Typewriter effects and loading indicators
- **Clean Interface**: Organized menu system with clear navigation

| Element | Description |
|---------|-------------|
| **Encoded Text** | Displayed in green for easy identification |
| **Decoded Text** | Shown in cyan to distinguish from input |
| **Original Text** | Highlighted in yellow |
| **Menu Headers** | Blue styling for section headers |
| **Error Messages** | Red text for warnings and errors |
| **Success Messages** | Green confirmations and status updates |

## 🔧 Technical Details

### Code Architecture
- **Modular Design**: Separate functions for each major feature
- **Error Handling**: Comprehensive try-catch blocks
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Memory Efficient**: No external dependencies or heavy libraries

## 🚨 Usage Tips

### Best Practices
- **Test with Different ROT Values**: Try ROT1, ROT13, ROT25 for variety
- **Check History**: Use option [4] to review past operations
- **Case Sensitivity**: Remember that case is preserved in results
- **Special Characters**: Numbers and symbols pass through unchanged

### Common Use Cases
- **Learning Cryptography**: Educational tool for understanding basic ciphers
- **Quick Text Obfuscation**: Simple text scrambling for casual use
- **ROT13 Operations**: Classic internet text encoding/decoding
- **Cipher Analysis**: Testing different rotation values

## 🐛 Troubleshooting

### Common Issues

**Program won't start:**
```bash
# Check Python version
python --version

# Use python3 if needed
python3 rotcipher.py
```

**Colors not displaying:**
- Some older terminals may not support colored output
- The program works fully without colors, they're just visual enhancements

**Permission errors:**
```bash
# Make file executable (Linux/Mac)
chmod +x rotcipher.py
```

**History file issues:**
- The program creates `rot_cipher_history.txt` automatically
- Ensure write permissions in the current directory

## 🤝 Contributing

Feel free to contribute improvements:

1. **Bug Reports**: Open an issue with details
2. **Feature Requests**: Suggest new cipher types or features
3. **Code Improvements**: Submit pull requests with enhancements
4. **Documentation**: Help improve this README

## 📜 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **ASCII Art**: Generated using text-to-ASCII conversion
- **Terminal Interface**: Enhanced user experience with visual feedback
- **Inspiration**: Classic ROT13 cipher and modern terminal tools

---

**Made with ❤️ by SPLO1T**

*Happy Encrypting! 🔐*