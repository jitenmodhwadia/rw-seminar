# Builds index.html from form_template.html + logo.txt + Google Form wiring.
# Fill FORM_ID and ENTRY ids after the Google Form backend exists, then: python build.py
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))

FORM_ID = "__FORM_ID__"   # the long 1FAIpQLS... id from the form's public /viewform URL
ENTRIES = {               # entry.<id> per question, in form order
    "__E_NAME__":  "",    # Full Name
    "__E_PHONE__": "",    # WhatsApp Number
    "__E_CITY__":  "",    # City / Village
    "__E_OCC__":   "",    # Occupation
    "__E_INV__":   "",    # Existing investor Yes/No
    "__E_CNT__":   "",    # How many attending
    "__E_SRC__":   "",    # Who invited you
    "__E_REF__":   "",    # Inviter name
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
