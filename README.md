# Tree-Pattern

This Python program prints a stylized tree shape using stars (`*`) based on the height input by the user. It demonstrates the use of loops, spacing, and pattern formation with ASCII characters.

---

## 📌 What the Program Does

- Prompts the user to enter the height of the tree.
- Prints two versions of a tree pattern made of stars:
  1. **Option 1:** Uses a `while` loop combined with nested `for` loops to print a centered tree shape.
  2. **Option 2:** Uses a `for` loop with string multiplication to print the tree shape more succinctly.
- Both options print a star "trunk" aligned beneath the tree.

---

## 🧠 How It Works

- **Option 1:**  
  - Uses a `while` loop to control the number of rows for the tree's branches.
  - Uses nested `for` loops to print spaces and stars for each level.
  - Adjusts the number of spaces and stars to form a centered triangular shape.
  - Prints a single star trunk beneath the tree.

- **Option 2:**  
  - Uses a `for` loop iterating backwards from the tree height.
  - Prints spaces and stars using string multiplication to create the tree branches.
  - Prints a star trunk aligned with the branches.

---

## 🚀 How to Run

1. Save the code as `star-tree.py`.
2. Run the script:

```bash
python star-tree.py

