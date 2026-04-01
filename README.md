# Pixel-Art-Generator

**A terminal-based pixel art editor with color palette, image import/export, and intuitive controls.**

## Features

- **Real-time editing**: Draw, erase, and navigate a 30x20 pixel canvas
- **Color palette**: 15 colors with terminal-compatible RGB mapping
- **Image import**: Convert images to pixel art (supports most formats)
- **Export to text**: Save artwork as color-coded text files
- **Keyboard controls**: Arrow keys, color shortcuts, and command keys
- **Responsive UI**: Adapts to different terminal sizes

## Tech Stack

- **Python** 3.7+
- **Curses** for terminal UI
- **Pillow** (PIL) for image processing
- **Colorama** for color initialization

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aliii-codes/Pixel-Art-Generator.git
   cd Pixel-Art-Generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure your terminal supports 256 colors (most modern terminals do).

## Usage

Run the application:
```bash
python pixelforge.py
```

**Controls:**
- **Arrows**: Move cursor
- **Space**: Draw current color
- **E**: Erase pixel
- **C/Z**: Cycle colors (+/-)
- **L**: Load image (enter path when prompted)
- **S**: Save canvas as text file
- **X**: Clear canvas
- **Q**: Quit

## Project Structure

```
Pixel-Art-Generator/
├── pixelforge.py      # Main application
├── LICENSE            # MIT License

```

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
```
