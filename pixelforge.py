import curses
# import windows_curses as curses
import os
from PIL import Image
from colorama import init

init()

COLORS = [
    (curses.COLOR_WHITE,   255, 255, 255),
    (curses.COLOR_RED,     255, 0,   0),
    (curses.COLOR_GREEN,   0,   255, 0),
    (curses.COLOR_BLUE,    0,   0,   255),
    (curses.COLOR_YELLOW,  255, 255, 0),
    (curses.COLOR_CYAN,    0,   255, 255),
    (curses.COLOR_MAGENTA, 255, 0,   255),
    (8,                    128, 128, 128),  # gray
    (9,                    255, 165, 0),    # orange
    (10,                   139, 0,   0),    # dark red
    (11,                   0,   128, 0),    # dark green
    (12,                   0,   0,   139),  # dark blue
    (13,                   255, 20,  147),  # pink
    (14,                   0,   0,   0),    # black
    (15,                   210, 180, 140),  # tan
]

COLOR_NAMES = [
    "White", "Red", "Green", "Blue", "Yellow",
    "Cyan", "Magenta", "Gray", "Orange", "DkRed",
    "DkGreen", "DkBlue", "Pink", "Black", "Tan"
]

PIXEL = "██"
CANVAS_W = 30
CANVAS_H = 20

def init_colors():
    curses.start_color()
    curses.can_change_color()
    for idx, (cnum, r, g, b) in enumerate(COLORS):
        try:
            curses.init_color(cnum, int(r * 1000 / 255), int(g * 1000 / 255), int(b * 1000 / 255))
            curses.init_pair(idx + 1, cnum, curses.COLOR_BLACK)
        except:
            curses.init_pair(idx + 1, cnum, curses.COLOR_BLACK)

def image_to_pixels(path):
    img = Image.open(path).convert("RGB")
    img = img.resize((CANVAS_W, CANVAS_H), Image.LANCZOS)
    canvas = {}
    for y in range(CANVAS_H):
        for x in range(CANVAS_W):
            r, g, b = img.getpixel((x, y))
            best = 0
            best_dist = float('inf')
            for idx, (_, cr, cg, cb) in enumerate(COLORS):
                dist = (r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2
                if dist < best_dist:
                    best_dist = dist
                    best = idx
            canvas[(x, y)] = best
    return canvas

def save_canvas(canvas):
    path = "pixel_art.txt"
    with open(path, "w") as f:
        for y in range(CANVAS_H):
            line = ""
            for x in range(CANVAS_W):
                c = canvas.get((x, y), -1)
                line += COLOR_NAMES[c] + " " if c >= 0 else "     "
            f.write(line + "\n")
    return path

def draw_ui(stdscr, canvas, cx, cy, color_idx, mode, message):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    # Title
    title = " PixelForge — Terminal Pixel Art "
    try:
        stdscr.addstr(0, max(0, (w - len(title)) // 2), title, curses.A_BOLD | curses.color_pair(5))
    except:
        pass

    # Canvas
    canvas_start_y = 2
    canvas_start_x = 2
    for y in range(CANVAS_H):
        for x in range(CANVAS_W):
            sx = canvas_start_x + x * 2
            sy = canvas_start_y + y
            if sy >= h - 1 or sx + 1 >= w:
                continue
            pixel = canvas.get((x, y), -1)
            is_cursor = (x == cx and y == cy)
            if is_cursor:
                attr = curses.A_REVERSE
                pair = curses.color_pair(color_idx + 1)
                try:
                    stdscr.addstr(sy, sx, PIXEL, pair | attr)
                except:
                    pass
            elif pixel >= 0:
                try:
                    stdscr.addstr(sy, sx, PIXEL, curses.color_pair(pixel + 1))
                except:
                    pass
            else:
                try:
                    stdscr.addstr(sy, sx, "· ", curses.color_pair(8))
                except:
                    pass

    # Sidebar
    sidebar_x = canvas_start_x + CANVAS_W * 2 + 3
    if sidebar_x + 20 < w:
        try:
            stdscr.addstr(2,  sidebar_x, "COLOR PALETTE", curses.A_BOLD)
            for i, name in enumerate(COLOR_NAMES):
                marker = "► " if i == color_idx else "  "
                try:
                    stdscr.addstr(3 + i, sidebar_x, marker + "██ " + name, curses.color_pair(i + 1))
                except:
                    pass

            stdscr.addstr(3 + len(COLOR_NAMES) + 1, sidebar_x, "CONTROLS", curses.A_BOLD)
            controls = [
                "Arrows  move",
                "Space   draw",
                "E       erase",
                "C       color+",
                "Z       color-",
                "L       load img",
                "S       save",
                "X       clear",
                "Q       quit",
            ]
            for i, ctrl in enumerate(controls):
                try:
                    stdscr.addstr(3 + len(COLOR_NAMES) + 2 + i, sidebar_x, ctrl)
                except:
                    pass
        except:
            pass

    # Status bar
    status = f" Mode: {mode} | Color: {COLOR_NAMES[color_idx]} | Pos: ({cx},{cy}) "
    if message:
        status += f"| {message} "
    try:
        stdscr.addstr(h - 1, 0, status[:w - 1], curses.A_REVERSE)
    except:
        pass

    stdscr.refresh()

def get_image_path(stdscr):
    h, w = stdscr.getmaxyx()
    curses.echo()
    curses.curs_set(1)
    try:
        stdscr.addstr(h - 2, 0, "Image path: " + " " * 40)
        stdscr.move(h - 2, 12)
        path = stdscr.getstr(h - 2, 12, 60).decode("utf-8").strip()
    except:
        path = ""
    curses.noecho()
    curses.curs_set(0)
    return path

def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    init_colors()

    canvas = {}
    cx, cy = 0, 0
    color_idx = 0
    mode = "DRAW"
    message = ""

    while True:
        draw_ui(stdscr, canvas, cx, cy, color_idx, mode, message)
        message = ""
        key = stdscr.getch()

        if key == curses.KEY_UP:
            cy = max(0, cy - 1)
        elif key == curses.KEY_DOWN:
            cy = min(CANVAS_H - 1, cy + 1)
        elif key == curses.KEY_LEFT:
            cx = max(0, cx - 1)
        elif key == curses.KEY_RIGHT:
            cx = min(CANVAS_W - 1, cx + 1)
        elif key == ord(' '):
            canvas[(cx, cy)] = color_idx
        elif key == ord('e') or key == ord('E'):
            canvas.pop((cx, cy), None)
        elif key == ord('c') or key == ord('C'):
            color_idx = (color_idx + 1) % len(COLORS)
        elif key == ord('z') or key == ord('Z'):
            color_idx = (color_idx - 1) % len(COLORS)
        elif key == ord('x') or key == ord('X'):
            canvas.clear()
            message = "Canvas cleared!"
        elif key == ord('l') or key == ord('L'):
            path = get_image_path(stdscr)
            if os.path.exists(path):
                try:
                    canvas = image_to_pixels(path)
                    message = f"Loaded: {os.path.basename(path)}"
                except Exception as ex:
                    message = f"Error: {ex}"
            else:
                message = "File not found!"
        elif key == ord('s') or key == ord('S'):
            saved = save_canvas(canvas)
            message = f"Saved to {saved}"
        elif key == ord('q') or key == ord('Q'):
            break

curses.wrapper(main)