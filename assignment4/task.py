import sqlite3
import random
import matplotlib.pyplot as plt

# --------------------------
# Connect to DB and read data
# --------------------------
conn = sqlite3.connect("students_ge.db")
cursor = conn.cursor()
cursor.execute(
    "SELECT gpa, subj_01, subj_02, subj_03, subj_04, subj_05, subj_06, subj_07, subj_08, subj_09, subj_10 FROM Student"
)
rows = cursor.fetchall()
conn.close()

gpas = [row[0] for row in rows]
subjects = [row[1:] for row in rows]

# --------------------------
# Map grades to groups
# --------------------------
def grade_to_group(g):
    if g == -1:
        return "missed"
    elif 41 <= g <= 50:
        return "points_41_50"
    elif 51 <= g <= 60:
        return "points_51_60"
    elif 61 <= g <= 70:
        return "points_61_70"
    elif 71 <= g <= 80:
        return "points_71_80"
    elif 81 <= g <= 90:
        return "points_81_90"
    elif 91 <= g <= 100:
        return "points_91_100"
    else:
        return "unknown"

# --------------------------
# Select 4 random subjects
# --------------------------
subject_indices = random.sample(range(10), 4)
subject_names = [f"subject_{i+1}" for i in subject_indices]
all_counts = []

for idx in subject_indices:
    grades = [grade_to_group(s[idx]) for s in subjects]
    counts = {
        g: grades.count(g)
        for g in ["missed", "points_41_50", "points_51_60", "points_61_70",
                  "points_71_80", "points_81_90", "points_91_100"]
    }
    all_counts.append(counts)

# --------------------------
# 2x2 Figure with swapped left-right positions
# --------------------------
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# ----- 1. Pie Chart (GPA) -----
bins = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
counts_gpa = [0] * 8
for g in gpas:
    for i in range(8):
        if bins[i] <= g < bins[i + 1]:
            counts_gpa[i] += 1
            break
        elif g == 4:
            counts_gpa[-1] += 1
counts_pie = list(all_counts[3].values())
labels_pie = list(all_counts[3].keys())
axs[0, 1].pie(counts_pie, labels=labels_pie, autopct='%1.1f%%', startangle=90)
axs[0, 1].axis('equal')
axs[0, 1].set_title(f"Pie chart: {subject_names[3]}")
axs[0, 1].pie(counts_gpa, startangle=90, counterclock=False)
axs[0, 1].axis('equal')
axs[0, 1].set_title(f"Pie chart: {subject_names[3]}")

# ----- 2. Bar Chart -----
counts = list(all_counts[0].values())
labels = list(all_counts[0].keys())
axs[0, 0].barh(labels, counts, color='skyblue')  # horizontal bar
axs[0, 0].set_xlim(0, max(counts) + 100)
axs[0, 0].set_title(f"BarH Chart: {subject_names[0]}")

# ----- 3. BarH Chart -----
counts = list(all_counts[1].values())
labels = list(all_counts[1].keys())
axs[1, 1].bar(labels, counts, color='orange')  # vertical bar
axs[1, 1].set_ylim(0, max(counts) + 100)
axs[1, 1].set_title(f"Bar Chart: {subject_names[1]}")

# ----- 4. Line Chart -----
counts = list(all_counts[2].values())
labels = list(all_counts[2].keys())
axs[1, 0].plot(range(7), counts, marker='o', linestyle='--', color='blue')
axs[1, 0].set_xticks(range(7))
axs[1, 0].set_xticklabels(labels)
axs[1, 0].set_ylim(0, max(counts) + 100)
axs[1, 0].set_title(f"Line Chart: {subject_names[2]}")

plt.tight_layout()
plt.show()
