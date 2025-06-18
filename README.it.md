[🇬🇧 English](README.md) - [🇮🇹 Italiano](README.it.md) - [🇪🇸 Español](README.es.md) - [🇩🇪 Deutsch](README.de.md)
<br><br>

**🇮🇹 Versione Italiana**

👋 Ciao, mi chiamo Antonio, benvenuto!<br>
Sono **Google Specialist** certificato come **Data Analyst** e **IT Assistance**.

Aiuto le persone a trasformare le proprie idee 💡 in business 💼 lavorando in modo intelligente e usando soluzioni digitali consapevoli.

Sono sempre felice di collaborare su *qualcosa di interessante* riguardo lo sviluppo di 
**app web e mobile** e/o **analisi dei dati**.

`Contatti:`  
E-Mail: antonio.web.lab@gmail.com<br>
Linkedin: https://www.linkedin.com/in/antonio-r-83937a25b/<br>
Sito web: https://anto-ru.github.io/anto-ru/<br>

<h2>Nuovi progetti in sviluppo:</h2>

<!-- INCLUDE: sections/projects.md -->







<!-- START INCLUDE -->
- [Validation rules for `Gift Card Form`](#validation-rules-for-gift-card-form)
- [`Laracast` v.12 \& `PHP`](#laracast-v12--php)
- [Microsoft `Windows` CLI \& Services Utilities](#microsoft-windows-cli--services-utilities)
- [Try hack me on `Flask`](#try-hack-me-on-flask)

<br>

## Validation rules for `Gift Card Form`
The gift card purchase form implements **client-side validation** using vanilla JavaScript to ensure data accuracy and improve user experience.

📞 Field `#phone_number` – User phone number
- **Valid input**: digits only (`0–9`)
- **Real-time validation**: any non-numeric character is dynamically removed (`\D`).
- **Goal**: ensure clean and compliant phone numbers.


🌍 Field `#country_code` – International dialing code
- **Valid input**: only the `+` symbol (mandatory in the first position) followed by digits (`0–9`)
- **Real-time validation**:
  - Removes all invalid characters (`[^+\d]`)
  - If `+` is typed elsewhere, it is automatically moved to the beginning.
- **Goal**: compliance with international standard E.164.


💳 Field `#gcard_amount` – Gift card amount
- **Valid input**: numeric digits only
- **Limit**: maximum of 4 digits
- **Real-time validation**: input is filtered and truncated to 4 numeric characters (`slice(0, 4)`).
- **Goal**: prevent invalid entries and enforce business limits on the gift card amount.


⚙️ Technical Details
- Validations are triggered via the `input` event to provide immediate feedback to users.
- The `inputmode="numeric"` attribute is used to enhance mobile usability.
- JavaScript validation supports the UI, but **server-side validation remains essential** for data integrity and security.


💡 **Note**: All functionalities are implemented using pure JavaScript, with no external dependencies, ensuring maximum performance and cross-browser compatibility.


<br>

## `Laracast` v.12 & `PHP`

Repository: ***https://github.com/anto-ru/laracast-PHP***

<br>

## Microsoft `Windows` CLI & Services Utilities

Repository: **https://github.com/anto-ru/windows-batch-scripts-public**

...the **Windows Scripting Project** will arrive soon!

<br>

## Try hack me on `Flask`

Repository: ***https://github.com/anto-ru/Flask_User-Authentication***

<br>
<!-- END INCLUDE -->

---
**✨ Ringraziamento speciale al gruppo GitHub ✨**

... stare insieme è un inizio. Restare insieme è un progresso. Lavorare insieme è un successo!<br>
(H.Ford)
