## 👋 Hi, I’m Antonio, welcome !
Google Specialist certificated as<br>
<b>Data Analyst</b> and <b>IT Assistantance</b>.

I help people turn their ideas 💡 into businesses 💼 by working smarter and using digital solutions consciously.

I’m always happy to collaborate on <i>something interesting</i> about<br>
<b>Web/Mobile APPs development</b> and/or <b>Data Analytics</b>.

`Contact:` <br>
antonio.web.lab@gmail.com <br>
https://www.linkedin.com/in/antonio-r-83937a25b/ <br>
https://anto-ru.github.io/anto-ru/ <br>

# Last project in development:
- [🔐 Validation Rules Gift Card Form](#validation-rules-gift-card-form)
- [Laracast-PHP](#laracast-php)
- [Try hack me](#try-hack-me)


## Validation Rules Gift Card Form
The gift card purchase form implements **client-side validation** using vanilla JavaScript to ensure data accuracy and improve user experience.

### 📞 Field `#phone_number` – User phone number
- **Valid input**: digits only (`0–9`)
- **Real-time validation**: any non-numeric character is dynamically removed (`\D`).
- **Goal**: ensure clean and compliant phone numbers.

---

### 🌍 Field `#country_code` – International dialing code
- **Valid input**: only the `+` symbol (mandatory in the first position) followed by digits (`0–9`)
- **Real-time validation**:
  - Removes all invalid characters (`[^+\d]`)
  - If `+` is typed elsewhere, it is automatically moved to the beginning.
- **Goal**: compliance with international standard E.164.

---

### 💳 Field `#gcard_amount` – Gift card amount
- **Valid input**: numeric digits only
- **Limit**: maximum of 4 digits
- **Real-time validation**: input is filtered and truncated to 4 numeric characters (`slice(0, 4)`).
- **Goal**: prevent invalid entries and enforce business limits on the gift card amount.

---

### ⚙️ Technical Details
- Validations are triggered via the `input` event to provide immediate feedback to users.
- The `inputmode="numeric"` attribute is used to enhance mobile usability.
- JavaScript validation supports the UI, but **server-side validation remains essential** for data integrity and security.

---

💡 **Note**: All functionalities are implemented using pure JavaScript, with no external dependencies, ensuring maximum performance and cross-browser compatibility.



## Laracast PHP

***https://github.com/anto-ru/laracast-PHP***


## Try hack me

***https://github.com/anto-ru/Flask_User-Authentication***

<b>✨ Special thanks to GitHub Group ✨</b>
<br/>

" Coming together is a beginning. Keeping together is progress.<br>
  Working together is success. " 
                                                       (H.Ford)
