# Interactive Image Pixel Inspector

An interactive Python utility built with Matplotlib for analyzing images. This tool allows you to inspect specific pixels, identify coordinates, and retrieve precise RGBA color values through mouse and keyboard interaction.

## ✨ Features

- **Live Hover Inspection:** Real-time RGBA and coordinate overlay as you move the cursor.
- **Precision Navigation:** Use Arrow Keys for pixel-perfect movement.
- **Persistent Markers:** Click to "lock" a marker on a specific pixel of interest.
- **Dynamic Metadata:** Automatically calculates and displays image resolution in the workspace title.
- **Clean UI:** Toggle overlays on and off with hotkeys.

## 🛠 Installation

Ensure you have Python installed. You will need the `matplotlib` library:

```
pip install matplotlib
```

## 🚀 Usage

1. **Start the Script:** Run the Python file.

   ```
   python datatips_for_matplotlib.py
   ```

2. **Load Image:** When prompted, enter the file path to your image (e.g., `images/sample.png`).

3. **Interactive Controls:**

   - **Mouse Move:** Hover over any part of the image to see live pixel data.
   - **Left Click:** Place a persistent red crosshair (+) on a pixel. Click the crosshair again to remove it.
   - **Arrow Keys (Up/Down/Left/Right):** Shift the selection by exactly one pixel for fine-tuning.
   - **'H' Key:** Toggle the hover details.

## 📂 Project Structure

- `datatips_for_matplotlib.py`: The main Python script.
- `README.md`: Project documentation.
- `LICENSE`: The GNU GPL v3.0 license text.

## 👤 Author

**Achyuta Shrimate**
