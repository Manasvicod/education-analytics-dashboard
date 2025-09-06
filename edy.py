# =======================================
# 📊 Education Data Analysis with Python
# =======================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load CSV files
# -------------------------------
students = pd.read_csv("students.csv")
courses = pd.read_csv("courses.csv")
enrollments = pd.read_csv("enrollments.csv")

# -------------------------------
# 2. Standardize column names
# -------------------------------
students.columns = students.columns.str.strip().str.lower()
courses.columns = courses.columns.str.strip().str.lower()
enrollments.columns = enrollments.columns.str.strip().str.lower()

# -------------------------------
# 3. Data Cleaning
# -------------------------------
students.drop_duplicates(inplace=True)
courses.drop_duplicates(inplace=True)
enrollments.drop_duplicates(inplace=True)

if "gender" in students.columns:
    students["gender"].fillna(students["gender"].mode()[0], inplace=True)

if "department" in students.columns:
    students["department"].fillna("unknown", inplace=True)

# -------------------------------
# 4. Map Grades → GPA
# -------------------------------
grade_map = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
enrollments["gpa"] = enrollments["grade"].map(grade_map)

# Merge student + enrollment + courses
df = enrollments.merge(students, on="studentid", how="left")
df = df.merge(courses, on="courseid", how="left")

print("\n✅ Columns in merged df:", df.columns.tolist())

# -------------------------------
# 5. Exploratory Data Analysis
# -------------------------------
if "gender" in students.columns:
    print("\nGender distribution:\n", students["gender"].value_counts())

if "department" in students.columns:
    print("\nDepartment distribution:\n", students["department"].value_counts())

print("\nGrade counts:\n", enrollments["grade"].value_counts())

# -------------------------------
# 6. Visualizations
# -------------------------------
sns.set(style="whitegrid", palette="muted")

if "gender" in students.columns:
    plt.figure(figsize=(6,4))
    sns.countplot(data=students, x="gender")
    plt.title("Student Gender Distribution")
    plt.show()

if "department" in students.columns:
    plt.figure(figsize=(8,4))
    sns.countplot(data=students, x="department", order=students["department"].value_counts().index)
    plt.title("Students per Department")
    plt.xticks(rotation=45)
    plt.show()

plt.figure(figsize=(6,4))
sns.countplot(data=enrollments, x="grade", order=["A","B","C","D","F"])
plt.title("Grade Distribution")
plt.show()

if "admissionyear" in students.columns:
    plt.figure(figsize=(8,4))
    sns.countplot(data=students, x="admissionyear", order=sorted(students["admissionyear"].unique()))
    plt.title("Student Enrollment Over Years")
    plt.show()

if "department" in df.columns:
    dept_gpa = df.groupby("department")["gpa"].mean().reset_index()
    plt.figure(figsize=(8,4))
    sns.barplot(data=dept_gpa, x="department", y="gpa", order=dept_gpa.sort_values("gpa", ascending=False)["department"])
    plt.title("Average GPA by Department")
    plt.xticks(rotation=45)
    plt.show()

# -------------------------------
# 7. Simple ML Example
# -------------------------------
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

if all(col in df.columns for col in ["gender", "department", "gpa"]):
    ml_df = df[["gender","department","gpa"]].dropna()

    le_gender = LabelEncoder()
    le_dept = LabelEncoder()
    ml_df["gender"] = le_gender.fit_transform(ml_df["gender"])
    ml_df["department"] = le_dept.fit_transform(ml_df["department"])

    X = ml_df[["gender","department"]]
    y = ml_df["gpa"] >= 3   # classify High GPA vs Low GPA

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("\nML Classification Report:\n")
    print(classification_report(y_test, y_pred))
