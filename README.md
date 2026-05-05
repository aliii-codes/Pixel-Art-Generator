# 🖼️ Pixel Art Generator
**Create stunning pixel art right in your terminal!**

[![GitHub stars](https://img.shields.io/github/stars/aliii-codes/Pixel-Art-Generator?style=for-the-badge)](https://github.com/aliii-codes/Pixel-Art-Generator/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/aliii-codes/Pixel-Art-Generator?style=for-the-badge)](https://github.com/aliii-codes/Pixel-Art-Generator/network/members)
[![GitHub issues](https://img.shields.io/github/issues/aliii-codes/Pixel-Art-Generator?style=for-the-badge)](https://github.com/aliii-codes/Pixel-Art-Generator/issues)
[![License](https://img.shields.io/github/license/aliii-codes/Pixel-Art-Generator?style=for-the-badge)](LICENSE)

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python)
![Curses](https://img.shields.io/badge/Curses-Terminal%20UI-yellow?style=for-the-badge)
![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-green?style=for-the-badge&logo=python)
![Colorama](https://img.shields.io/badge/Colorama-Color%20Initialization-red?style=for-the-badge)

---

## ✨ Highlights
- **Terminal-Based Creativity**: Draw, edit, and export pixel art directly in your terminal.
- **Rich Color Palette**: 15 terminal-compatible colors with intuitive RGB mapping.
- **Image Import/Export**: Convert images to pixel art and save your creations as text files.
- **Responsive UI**: Adapts seamlessly to different terminal sizes.

---

## 🎨 Features

| Feature                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **Real-time Editing**    | Draw, erase, and navigate a 30x20 pixel canvas in real-time.                |
| **Color Palette**        | 15 colors with terminal-compatible RGB mapping.                            |
| **Image Import**         | Convert images to pixel art (supports most formats).                       |
| **Export to Text**       | Save artwork as color-coded text files.                                    |
| **Keyboard Controls**    | Intuitive controls using arrow keys, color shortcuts, and command keys.    |
| **Responsive UI**        | Adapts to different terminal sizes for a seamless experience.              |

---

## 🛠️ Tech Stack

| Category        | Technologies                                                                 |
|-----------------|------------------------------------------------------------------------------|
| **Language**    | Python 3.7+                                                                 |
| **Terminal UI** | Curses                                                                      |
| **Image Processing** | Pillow (PIL)                                                                |
| **Color Initialization** | Colorama                                                                    |

---

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aliii-codes/Pixel-Art-Generator.git
   cd Pixel-Art-Generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure terminal compatibility**:
   Make sure your terminal supports 256 colors (most modern terminals do).

---

## ▶️ Usage

**Run the application**:
```bash
python pixelforge.py
```

**Controls**:

| Key            | Action                          |
|----------------|---------------------------------|
| **Arrows**     | Move cursor                    |
| **Space**      | Draw current color             |
| **E**          | Erase pixel                    |
| **C/Z**        | Cycle colors (+/-)             |
| **L**          | Load image (enter path)        |
| **S**          | Save canvas as text file       |
| **X**          | Clear canvas                   |
| **Q**          | Quit                           |

---

## 📁 Project Structure

```
Pixel-Art-Generator/
├── pixelforge.py      # Main application
└── LICENSE            # MIT License
```

---

## 🤝 Contributing

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Add some feature"
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a pull request**.

---

## 🐞 Bug Reports & Feature Requests

Found a bug or have a feature request? [Open an issue](https://github.com/aliii-codes/Pixel-Art-Generator/issues).

---

## 📜 License & Acknowledgements

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

**Shoutout to**:
- The Python community for their amazing libraries.
- The Curses and Pillow teams for enabling terminal-based creativity.
