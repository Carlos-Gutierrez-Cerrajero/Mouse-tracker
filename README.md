# Mouse-tracker

## Description
<p id="Description">
  A small program that constantly updates the cursor x and y positions and the RGB color of the current pixel. Useful for GUI automation, although I've used it to save RGB color codes for a variety of reasons.<br>
  This is my attempt to replicate the <a href="https://pypi.org/project/MouseInfo/">Mouse info module</a> prompted by the excellent book <a href="https://automatetheboringstuff.com/#toc">Automate the Boring Stuff with Python</a>, specifically chapter 20
</p>

## Dependencies
<p id="Dependencies">
  Language: Python 3<br>
  Modules: <a href="https://pyautogui.readthedocs.io/en/latest/">PyAutoGUI</a> and <a href="https://pypi.org/project/keyboard/">keyboard</a> (logging and time as well, but those are part of the standard library).
</p>

## Usage
<p id="Usage">
  Run mouse_tracker.py<br>
  The program will constantly display x, y coordinates and RGB color for cursor position and has some shortcuts to save information:
  <ul>
    <li><b>Alt+R</b>: Save current cursor's position and color</li>
    <li><b>Alt+S</b>: Save current cursor's position and color with input custom tag</li>
    <li><b>Alt+L</b>: Write all saved positions and colors, with and without tag, to path = "./mouse_tracker_log.txt"</li>
    <li><b>Alt+Q</b>: Stops program, displays saved position and exits</li>
  </ul>
</p>
