# Builds index.html from form_template.html + logo.txt + Google Form wiring.
# Fill FORM_ID and ENTRY ids after the Google Form backend exists, then: python build.py
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))

FORM_ID = "1FAIpQLSe_1AiUpPLv2H1Z5B-IkGMloIOYN1pakgyExwtYpVcGvcA5Kg"
ENTRIES = {                       # entry.<id> per question, in form order
    "__E_NAME__":  "1008521861",  # Full Name
    "__E_PHONE__": "1575132814",  # WhatsApp Number
    "__E_CITY__":  "882496880",   # City / Village
    "__E_OCC__":   "2049252346",  # Occupation
    "__E_INV__":   "351091380",   # Existing investor Yes/No
    "__E_CNT__":   "13852270",    # How many attending
    "__E_SRC__":   "796520081",   # Who invited you
    "__E_REF__":   "8602321",     # Inviter name
}

html = io.open(os.path.join(HERE, "form_template.html"), encoding="utf-8").read()
logo = io.open(os.path.join(HERE, "logo.txt"), encoding="utf-8").read().strip()
html = html.replace("__LOGO__", logo)

if FORM_ID != "__FORM_ID__":
    html = html.replace("__FORM_ID__", FORM_ID)
    for token, eid in ENTRIES.items():
        assert eid, "missing entry id for " + token
        html = html.replace(token, eid)
else:
    print("WARNING: FORM_ID not set yet - building with placeholder wiring (form submit won't work)")

io.open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html)
print("index.html written,", len(html), "bytes")
