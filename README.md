# Fake Coin Detection Algorithm

## Overview
This project implements a **Fake Coin Detection Algorithm** using a simple **divide-and-compare approach**.  

The program assumes there are **8 coins**, and **one coin is fake (lighter)** than the others. The algorithm identifies the fake coin using a minimal number of **weighings (comparisons)**.

The program also calculates:
- Number of weighings performed
- Best case and worst case time
- Execution time of the algorithm

---

## How the Algorithm Works

### 1. Initialize Coins
- All coins initially have weight **10**.
- One coin is chosen as fake and assigned weight **9**.

### 2. Divide Coins into Groups
The coins are divided into three groups:

- **Group A:** Coins 1–3  
- **Group B:** Coins 4–6  
- **Group C:** Coins 7–8  

### 3. First Weighing
- Compare the total weight of **Group A** and **Group B**.
- If **Group A < Group B**, the fake coin is in **Group A**.
- If **Group B < Group A**, the fake coin is in **Group B**.
- If both groups are equal, the fake coin must be in **Group C**.

### 4. Second Weighing
The algorithm then compares coins **inside the selected group** sequentially to determine the exact fake coin.

### 5. Output
The program prints:
- Position of the fake coin
- Number of weighings
- Best case time
- Worst case time
- Execution time

---
