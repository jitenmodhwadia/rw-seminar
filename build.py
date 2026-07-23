# Builds index.html from form_template.html + logo.txt + Google Form wiring.
# Fill FORM_ID and ENTRY ids after the Google Form backend exists, then: python build.py
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))

FORM_ID = "1FAIpQLSe_1AiUpPLv2H1Z5B-IkGMloIOYN1pakgyExwtYpVcGvcA5Kg"

# Seminar date & time shown on the page (venue goes out on WhatsApp only).
# Update these lines for each new seminar, then rerun: python build.py
WHEN_EN  = "Sunday, 2 August 2026 · 11:00 AM"
WHEN_GUJ = "રવિવાર, ૨ ઓગસ્ટ ૨૦૨૬ · સવારે ૧૧:૦૦ વાગ્યે"

ENTRIES = {                       # entry.<id> per question, in form order
    "__E_NAME__":  "1008521861",  # Full Name
    "__E_PHONE__": "1575132814",  # WhatsApp Number
    "__E_CITY__":  "882496880",   # City / Village
    "__E_OCC__":   "2049252346",  # Occupation
    "__E_INV__":   "351091380",   # Existing investor Yes/No
    "__E_SRC__":   "796520081",   # Who invited you
    "__E_REF__":   "8602321",     # Inviter name
}

html = io.open(os.path.join(HERE, "form_template.html"), encoding="utf-8").read()
logo = io.open(os.path.join(HERE, "logo.txt"), encoding="utf-8").read().strip()
html = html.replace("__LOGO__", logo)
html = html.replace("__WHEN_EN__", WHEN_EN).replace("__WHEN_GUJ__", WHEN_GUJ)
if WHEN_EN == "__WHEN_EN__":
    print("WARNING: WHEN_EN/WHEN_GUJ not set - date/time placeholders still on the page")

if FORM_ID != "__FORM_ID__":
    html = html.replace("__FORM_ID__", FORM_ID)
    for token, eid in ENTRIES.items():
        assert eid, "missing entry id for " + token
        html = html.replace(token, eid)
else:
    print("WARNING: FORM_ID not set yet - building with placeholder wiring (form submit won't work)")

io.open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html)
print("index.html written,", len(html), "bytes")
