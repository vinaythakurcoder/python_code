## 📂 File Handling

File handling allows a program to read, write, and manage data stored in files.  
📌 It is one of the most important concepts in Python for working with external data.

---

### 🔧 File Modes

| Mode | Description |
|------|------------|
| `r`  | Read file (default) |
| `w`  | Write file (creates or overwrites) |
| `a`  | Append to file |
| `x`  | Create new file (fails if file exists) |
| `b`  | Binary mode |
| `t`  | Text mode (default) |
| `+`  | Read and write |

---

### 📖 Examples

#### 1️⃣ Read File
```python
with open("data.txt", "r") as f:
    print(f.read())
