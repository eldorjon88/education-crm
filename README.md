# 📘 Education CRM (DRF)

## 👨‍💻 Developer Documentation (Internal)

---

## 1️⃣ Project overview

**Education CRM** – o‘quv markazlar uchun minimal CRM tizimi.

**Scope (MVP):**

* Student
* Group
* Attendance
* Payment
* Risk flag (oddiy, 3 ta kelmaslik)

Maqsad: **Excel yoki jadvallar o‘rniga yagona tizim**. Keyinchalik kengaytirish mumkin bo‘lgan modul struktura.

---

## 2️⃣ Tech stack

* Python 3.11+
* Django 4+
* Django Rest Framework (DRF)
* PostgreSQL
* Token Authentication (DRF built-in)
* Django Admin

---

## 3️⃣ Architecture (high-level)

```
Client (Admin / Teacher / Student)
        ↓
      DRF API
        ↓
     Business Logic / Services
        ↓
    PostgreSQL
```

Har bir modul quyidagi prinsiplarda ishlaydi:

* Model
* Serializer
* View
* URL
* Optional: Service / utils functions

---

## 4️⃣ Project structure

```
education_crm/
 ├── core/
 │    ├── settings.py
 │    ├── urls.py
 │    └── permissions.py
 ├── students/
 │    ├── models.py
 │    ├── serializers.py
 │    ├── views.py
 │    └── urls.py
 ├── groups/
 ├── attendance/
 ├── payments/
 └── manage.py
```

**Tip:** har modul mustaqil, keyinchalik reusable bo‘lishi uchun.

---

## 5️⃣ Data models (minimal)

### Student

```text
id
full_name
phone
status (active/inactive)
is_risk (bool, default=False)
created_at
```

---

### Group

```text
id
name
teacher (User FK)
students (M2M -> Student)
```

---

### Attendance

```text
id
student (FK)
group (FK)
date
status (present/absent)
```

---

### Payment

```text
id
student (FK)
month (DateField / Month)
status (paid/unpaid)
```

---

## 6️⃣ Business logic

### 🔹 Attendance → Risk

* Agar student **3 marta absent** bo‘lsa, `student.is_risk = True`.
* Yozish joyi: **signal yoki service function** Attendance save’ida.

### 🔹 Payment

* Har oy 1 payment record
* Status `unpaid` bo‘lsa → admin ko‘radi
* Student panelda faqat **o‘z holatini** ko‘radi

---

## 7️⃣ Permissions

| Action       | Admin | Teacher              | Student              |
| ------------ | ----- | -------------------- | -------------------- |
| Student CRUD | ✅     | ❌                    | ❌                    |
| Group CRUD   | ✅     | ❌                    | ❌                    |
| Attendance   | ✅     | ✅ (faqat o‘z guruhi) | ❌                    |
| Payment      | ✅     | ❌                    | ✅ (faqat o‘z holati) |

**Custom permissions:**

```python
class IsAdmin
class IsTeacherOfGroup
```

---

## 8️⃣ API endpoints

### Students

```
POST   /api/students/
GET    /api/students/
PUT    /api/students/{id}/
```

### Groups

```
POST /api/groups/
GET  /api/groups/
```

### Attendance

```
POST /api/attendance/
GET  /api/attendance/?group_id=1&date=2025-01-01
```

### Payments

```
POST /api/payments/
GET  /api/payments/?student_id=1
```

---

## 9️⃣ Error handling

* 400 → validation error
* 401 → not authenticated
* 403 → permission denied
* 404 → not found

**Serializer validation** ishlatiladi.

---

## 🔟 Coding rules

* Fat view’da logic yozma → service / utils
* Modelni haddan ortiq semirtirma
* Reusable function yoz → DRY principle
* `print()` emas → `logging`

---

## 1️⃣1️⃣ Development plan (step-by-step)

### Day 1

* Django project yaratish
* User model / auth
* Student + Group models

### Day 2

* Attendance modeli
* Attendance API
* Risk logic

### Day 3

* Payment modeli
* Payment API
* Permissions

### Day 4

* Cleanup / refactor
* Admin panel
* README & docs

---

## 1️⃣2️⃣ Done definition

* [ ] API’lar ishlayapti
* [ ] Permission buzilmayapti
* [ ] Risk flag avtomatik qo‘yilyapti
* [ ] Admin hamma narsani ko‘ra oladi
* [ ] Teacher faqat o‘z guruhini ko‘radi
* [ ] Student panel minimal ishlaydi
