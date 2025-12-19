# 📄 O‘quv markaz CRM

## ✅ **Technical Requirements (MVP)**

---

## 1️⃣ Loyiha maqsadi

Oddiy tilda:

Excel yoki boshqa jadvallar o‘rniga **bitta tizim** orqali:

* studentlar ro‘yxati
* guruhlar
* davomat
* to‘lovlar

hammasi **bir joyda boshqarilsin**.

---

## 2️⃣ Rollar

### 👑 Admin

* Barcha ma’lumotlarni ko‘radi va boshqaradi: student, guruh, davomat, to‘lovlar.

### 👩‍🏫 Teacher

* Faqat **o‘z guruhlari** bo‘yicha davomat qo‘yadi va guruhdagi studentlarni ko‘radi.

### 🧑‍🎓 Student

* Faqat **o‘z ma’lumotlarini** va davomat / to‘lov holatini ko‘radi.

---

## 3️⃣ Asosiy funksiyalar (MVP)

### 🔹 3.1 Student

* Ism, telefon, email (agar kerak bo‘lsa)
* Status: `active | inactive`
* Qaysi guruhga tegishli
* **Student panel**:

  * O‘z guruhini ko‘rish
  * Davomatini ko‘rish (`present | absent`)
  * To‘lov holatini ko‘rish (`paid | unpaid`)

---

### 🔹 3.2 Group

* Nom
* Teacher
* O‘quvchilar ro‘yxati
* Guruhdagi darslar va davomatlarni ko‘rish

---

### 🔹 3.3 Attendance

* Har dars uchun: `present | absent`
* Agar student **3 marta kelmasa** → tizim avtomatik `risk = true` belgilaydi
* Teacher faqat o‘z guruhidagi studentlar uchun davomat qo‘yadi
* Admin barcha guruhlarni ko‘radi

---

### 🔹 3.4 Payment

* Oyiga 1 marta to‘lov
* Status: `paid | unpaid`
* Agar to‘lov qilinmasa → admin ko‘radi
* Student panelida o‘z to‘lov holatini ko‘rish mumkin

---

## 4️⃣ Qoidalar (hardcoded / oddiy)

* 3 marta kelmasa → `risk = true`
* To‘lov qilinmasa → `unpaid`

Keyinchalik: kengaytirish imkoniyati (muhim statistikalar, avtomatik email/xabar yuborish va hokazo).
