import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LupusCare AI",
    page_icon="💜",
    layout="wide"
)

# Add this below your existing st.set_page_config(...)

# Replace your existing global CSS block with this one.
# Keep this after st.set_page_config(...) and before page content.

st.markdown("""
<style>
/* ===== GLOBAL THEME ===== */
.stApp {
    background: #f4f8fb;
    color: #203447;
}

[data-testid="stAppViewContainer"] {
    background: #f4f8fb;
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 2.5rem;
}

/* ===== READABLE TEXT ===== */
.stApp p,
.stApp li,
.stApp label,
.stApp .stMarkdown,
.stApp [data-testid="stCaptionContainer"] {
    color: #334b5d;
}

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
    color: #17384a;
    font-weight: 700;
}

/* ===== SIDEBAR ===== */
[data-testid="stSidebar"] {
    background: #102b3f;
    border-right: 1px solid #29485a;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    color: #f2f8fc;
}

/* ===== INPUT FIELDS ===== */
.stApp input,
.stApp textarea,
.stApp [data-baseweb="select"] > div {
    background-color: #ffffff;
    color: #203447;
    border-color: #c9d9e2;
    border-radius: 9px;
}

/* Input placeholder contrast */
.stApp input::placeholder,
.stApp textarea::placeholder {
    color: #718596;
    opacity: 1;
}

/* Labels and form text */
.stApp [data-testid="stWidgetLabel"] p {
    color: #294458;
    font-weight: 600;
}

/* ===== BUTTONS ===== */
.stButton > button,
.stDownloadButton > button,
[data-testid="stFormSubmitButton"] > button {
    background: #087f8c;
    color: #ffffff;
    border: 1px solid #087f8c;
    border-radius: 10px;
    padding: 0.55rem 1rem;
    font-weight: 600;
    transition: background 0.2s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover,
[data-testid="stFormSubmitButton"] > button:hover {
    background: #066773;
    color: #ffffff;
    border-color: #066773;
}

/* ===== METRIC CARDS ===== */
[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #d8e6ec;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 3px 12px rgba(16, 43, 63, 0.05);
}

[data-testid="stMetricLabel"] {
    color: #52697a;
}

[data-testid="stMetricValue"] {
    color: #123d50;
}

/* ===== EXPANDERS AND CONTAINERS ===== */
[data-testid="stExpander"] {
    background: #ffffff;
    border: 1px solid #d8e6ec;
    border-radius: 12px;
}

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p {
    color: #203447;
}

/* ===== DATA TABLES ===== */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    border: 1px solid #d8e6ec;
    border-radius: 10px;
}

/* ===== TABS ===== */
.stTabs [data-baseweb="tab"] {
    color: #40586b;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    color: #087f8c;
}

/* ===== ALERTS AND DIVIDERS ===== */
[data-testid="stAlert"] p {
    color: inherit;
}

hr {
    border-color: #d8e6ec;
}

/* ===== MOBILE SPACING ===== */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem 1rem 2rem;
    }

    h1 {
        font-size: 1.7rem !important;
    }
}
</style>
""", unsafe_allow_html=True)


# Custom CSS

st.markdown("""
<style>
/* ===== LupusCare AI | Premium Healthcare Theme ===== */

:root {
    --navy: #142D4E;
    --teal: #138A83;
    --teal-dark: #0E706B;
    --mint: #E9F6F3;
    --page: #F5F8FC;
    --border: #E0E8F0;
    --text: #24364B;
    --muted: #66788A;
}

/* Main page */
.stApp {
    background: var(--page);
    color: var(--text);
}

[data-testid="stMainBlockContainer"] {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Headings */
h1 {
    color: var(--navy) !important;
    font-weight: 750 !important;
    letter-spacing: -0.8px;
}

h2, h3 {
    color: var(--navy) !important;
    font-weight: 650 !important;
}

p, label, .stMarkdown {
    color: var(--text);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: var(--navy);
    border-right: 1px solid #243F60;
}

[data-testid="stSidebar"] * {
    color: #F4F8FC;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    background: transparent;
    border-radius: 9px;
    padding: 7px 10px;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    background: var(--teal);
    color: white;
    border: 1px solid var(--teal);
    border-radius: 10px;
    padding: 0.55rem 1.1rem;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: var(--teal-dark);
    color: white;
    border-color: var(--teal-dark);
}

/* Text inputs and dropdowns */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stDateInput input,
.stTimeInput input {
    background: #FFFFFF;
    color: var(--text);
    border-radius: 9px;
    border: 1px solid var(--border);
}

[data-baseweb="select"] > div {
    border-radius: 9px;
    border-color: var(--border);
}

/* Metric cards */
[data-testid="stMetric"] {
    background: #FFFFFF;
    padding: 20px;
    border: 1px solid var(--border);
    border-radius: 14px;
    box-shadow: 0 3px 12px rgba(20, 45, 78, 0.04);
}

[data-testid="stMetricLabel"] {
    color: var(--muted);
}

[data-testid="stMetricValue"] {
    color: var(--navy);
    font-weight: 750;
}

/* Existing custom cards */
.hero {
    background: linear-gradient(135deg, #E2F5F1, #F2F8FF);
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #D5EAE6;
    margin-bottom: 24px;
    box-shadow: 0 5px 18px rgba(20, 45, 78, 0.04);
}

.card {
    background: #FFFFFF;
    padding: 23px;
    border-radius: 16px;
    border: 1px solid var(--border);
    min-height: 150px;
    margin-bottom: 16px;
    box-shadow: 0 4px 16px rgba(20, 45, 78, 0.045);
}

.card h3 {
    color: var(--teal-dark) !important;
}

.small-text {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.6;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    border-bottom: 1px solid var(--border);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 9px 9px 0 0;
    padding: 10px 16px;
}

/* Expanders */
[data-testid="stExpander"] {
    background: #FFFFFF;
    border: 1px solid var(--border);
    border-radius: 12px;
}

/* Alerts and separators */
[data-testid="stAlert"] {
    border-radius: 12px;
}

hr {
    border-color: var(--border);
}

/* Images */
[data-testid="stImage"] img {
    border-radius: 14px;
}

/* Responsive spacing */
@media (max-width: 768px) {
    [data-testid="stMainBlockContainer"] {
        padding: 1rem;
    }

    .hero {
        padding: 20px;
    }

    .card {
        padding: 17px;
    }
}
</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.title("💜 LupusCare AI")
    st.caption("Your health companion")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Home",
            "Symptom Diary",
            "Medicine Tracker",
            "Appointments",
            "Health Insights",
            "Doctor Summary",
            "LupusVision AI"
        ]
    )

    st.divider()
    st.caption("Supporting your health journey 💚")
# ---------- REUSABLE LUPUSCARE UI COMPONENTS ----------

def page_header(title, subtitle, icon="💙"):
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(120deg, #ffffff, #e8f7f5);
            padding: 24px;
            border-radius: 18px;
            border: 1px solid #d5e9e7;
            margin-bottom: 22px;
        ">
            <div style="font-size: 30px; margin-bottom: 8px;">
                {icon}
            </div>
            <h1 style="
                color: #17384a;
                font-size: 28px;
                margin: 0;
            ">{title}</h1>
            <p style="
                color: #526b78;
                font-size: 15px;
                margin-top: 8px;
                margin-bottom: 0;
            ">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def section_header(title, subtitle=None):
    st.markdown(
        f"""
        <div style="margin-top: 18px; margin-bottom: 12px;">
            <h3 style="
                color: #17384a;
                margin-bottom: 4px;
            ">{title}</h3>
            {
                f'<p style="color:#607784; margin-top:0;">{subtitle}</p>'
                if subtitle else ''
            }
        </div>
        """,
        unsafe_allow_html=True
    )


def empty_state(message):
    st.info(f"ℹ️ {message}")

# Home page

if page == "Home":

    import json
    from pathlib import Path
    from datetime import date

    # ==========================================
    # 1. LOAD SAVED HEALTH RECORDS
    # ==========================================

    def load_json_records(filename):
        file_path = Path(filename)

        if not file_path.exists():
            return []

        try:
            with file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            return data if isinstance(data, list) else []

        except (json.JSONDecodeError, OSError):
            return []

    symptoms = load_json_records("symptom_records.json")
    medicines = load_json_records("medicine_records.json")
    medicine_logs = load_json_records("medicine_log.json")
    appointments = load_json_records("appointments.json")

    today = date.today()

    # ==========================================
    # 2. FIND UPCOMING APPOINTMENTS
    # ==========================================

    upcoming_appointments = []

    for appointment in appointments:
        if not isinstance(appointment, dict):
            continue

        appointment_date = appointment.get("date", "")
        status = appointment.get("status", "Upcoming")

        try:
            parsed_date = date.fromisoformat(appointment_date)

            if parsed_date >= today and str(status).lower() == "upcoming":
                upcoming_appointments.append(appointment)

        except (ValueError, TypeError):
            continue

    upcoming_appointments.sort(
        key=lambda item: item.get("date", "")
    )

    # ==========================================
    # 3. WELCOME BANNER
    # ==========================================

    
    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #142D4E, #138A83);
        padding: 32px;
        border-radius: 20px;
        margin-bottom: 24px;
        box-shadow: 0 8px 24px rgba(20,45,78,0.12);
    ">
        <p style="color: #C9F4EA; letter-spacing: 2px; font-size: 12px; font-weight: 600;">
            YOUR PERSONAL HEALTH COMPANION
        </p>
        <h1 style="color: white; font-size: 34px; margin-bottom: 10px;">
            Welcome to LupusCare AI 💚
        </h1>
        <p style="color: #F0FAFA; font-size: 16px;">
            Your health journey, organised in one place.
        </p>
        <p style="color: #D8EAEF; font-size: 13px;">
            Track symptoms, manage medicine records and organise
            your healthcare appointments.
        </p>
    </div>
    """, unsafe_allow_html=True)


    # ==========================================
    # 4. HEALTH OVERVIEW
    # ==========================================

    st.subheader("📊 Your Health Overview")
    st.caption(
        "A quick overview of the records saved in your application."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🩺 Symptoms", len(symptoms))

    with col2:
        st.metric("💊 Medicines", len(medicines))

    with col3:
        st.metric("📅 Upcoming Visits", len(upcoming_appointments))

    with col4:
        st.metric("📝 Medicine Logs", len(medicine_logs))

    st.divider()

    # ==========================================
    # 5. RECENT ACTIVITY
    # ==========================================

    st.subheader("📋 Recent Activity")

    left, right = st.columns(2, gap="large")

    with left:
        with st.container(border=True):
            st.markdown("### 📔 Recent Symptoms")
            st.caption("Your latest saved symptom records")

            if symptoms:
                for record in symptoms[-3:][::-1]:

                    if not isinstance(record, dict):
                        continue

                    symptom_name = (
                        record.get("symptoms")
                        or record.get("Symptoms")
                        or record.get("symptom")
                        or record.get("Symptom")
                        or "Symptom record"
                    )

                    symptom_date = (
                        record.get("date")
                        or record.get("Date")
                        or record.get("symptom_date")
                        or record.get("Symptom Date")
                        or "Date unavailable"
                    )

                    severity = (
                        record.get("severity")
                        or record.get("Severity")
                        or "Not specified"
                    )

                    st.markdown(f"**🩺 {symptom_name}**")
                    st.caption(
                        f"Date: {symptom_date}  |  Severity: {severity}"
                    )
                    st.divider()

            else:
                st.info("No symptom records saved yet.")

    with right:
        with st.container(border=True):
            st.markdown("### 📅 Upcoming Appointments")
            st.caption("Your next scheduled visits")

            if upcoming_appointments:
                for appointment in upcoming_appointments[:3]:

                    doctor = appointment.get(
                        "doctor",
                        "Doctor name unavailable"
                    )

                    appointment_date = appointment.get("date", "")
                    appointment_time = appointment.get("time", "")

                    st.markdown(f"**👨‍⚕️ {doctor}**")
                    st.caption(
                        f"Date: {appointment_date}  |  "
                        f"Time: {appointment_time or 'Not specified'}"
                    )
                    st.divider()

            else:
                st.info("No upcoming appointments recorded.")

    # ==========================================
    # 6. HEALTH TOOLS
    # ==========================================

    st.divider()

    st.subheader("✨ Explore Your Health Tools")
    st.caption(
        "Choose a feature from the sidebar to manage your health records."
    )

    tool1, tool2, tool3 = st.columns(3, gap="medium")

    with tool1:
        with st.container(border=True):
            st.markdown("### 📔 Symptom Diary")
            st.write(
                "Record symptoms and keep track of your health history."
            )

    with tool2:
        with st.container(border=True):
            st.markdown("### 💊 Medicine Tracker")
            st.write(
                "Organise medicine records and track saved medicine logs."
            )

    with tool3:
        with st.container(border=True):
            st.markdown("### 📅 Appointments")
            st.write(
                "Keep your upcoming healthcare appointments organised."
            )

    tool4, tool5, tool6 = st.columns(3, gap="medium")

    with tool4:
        with st.container(border=True):
            st.markdown("### 🧠 LupusVision AI")
            st.write(
                "Explore experimental symptom-text analysis and basic "
                "image processing."
            )

    with tool5:
        with st.container(border=True):
            st.markdown("### 📈 Health Insights")
            st.write(
                "Review the health information available in your records."
            )

    with tool6:
        with st.container(border=True):
            st.markdown("### 📄 Doctor Summary")
            st.write(
                "Prepare a summary of recorded information to discuss "
                "with your healthcare professional."
            )

    # ==========================================
    # 7. HEALTH DISCLAIMER
    # ==========================================

    st.info(
        "💚 **Health reminder:** LupusCare AI is a patient-support "
        "prototype. Its experimental features do not diagnose lupus "
        "or recommend treatment. Please consult your healthcare "
        "professional for medical decisions."
    )

# Placeholder pages

elif page == "Symptom Diary":
    import pandas as pd
    from datetime import date
    import json
    from pathlib import Path

    st.title("📔 My Symptom Diary")
    st.write("Record how you feel each day.")

    file_path = Path("symptom_records.json")

    if file_path.exists():
        records = json.loads(file_path.read_text(encoding="utf-8"))
    else:
        records = []

    with st.form("symptom_form"):
        selected_date = st.date_input(
            "Date",
            value=date.today()
        )

        symptoms = st.multiselect(
            "What symptoms did you experience?",
            [
                "Fatigue",
                "Joint pain",
                "Headache",
                "Skin rash",
                "Fever",
                "Swelling",
                "Other"
            ]
        )

        severity = st.select_slider(
            "Overall symptom severity",
            options=["Mild", "Moderate", "Severe"]
        )

        notes = st.text_area(
            "Additional notes (optional)",
            placeholder="Describe how you felt today..."
        )

        submitted = st.form_submit_button("Save Record")

    if submitted:
        if not symptoms:
            st.warning("Please select at least one symptom.")
        else:
            records.append({
                "Date": selected_date.isoformat(),
                "Symptoms": ", ".join(symptoms),
                "Severity": severity,
                "Notes": notes
            })

            file_path.write_text(
                json.dumps(records, indent=2, ensure_ascii=False),
                encoding="utf-8"
            )

            st.success("Symptom record saved successfully!")

    st.subheader("📋 My Previous Records")

    if records:
        df = pd.DataFrame(records)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No records yet. Add your first symptom record above.")


elif page == "Medicine Tracker":
    import json
    import uuid
    from pathlib import Path
    from datetime import date, timedelta
    import pandas as pd

    st.title("💊 Medicine Tracker")
    st.write("Organise your doctor-prescribed medicine schedule.")

    medicine_file = Path("medicine_records.json")
    log_file = Path("medicine_log.json")

    def load_json(path):
        if path.exists():
            try:
                return json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                st.error(f"Could not read {path.name}. Check the file.")
                st.stop()
        return []

    def save_json(path, data):
        path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

    medicines = load_json(medicine_file)
    logs = load_json(log_file)

    today = date.today()
    today_text = today.isoformat()

    st.subheader("➕ Add a Prescribed Medicine")

    with st.form("add_medicine_form"):
        medicine_name = st.text_input(
            "Medicine name",
            placeholder="Enter sample medicine name"
        )

        instructions = st.text_input(
            "Doctor-prescribed instructions",
            placeholder="Enter instructions exactly as prescribed"
        )

        schedule = st.multiselect(
            "Scheduled times",
            ["Morning", "Afternoon", "Evening", "Bedtime"]
        )

        start_date = st.date_input(
            "Start date",
            value=today
        )

        end_date = st.date_input(
            "End date",
            value=today + timedelta(days=30)
        )

        add_clicked = st.form_submit_button("Save Medicine")

    if add_clicked:
        if not medicine_name.strip():
            st.warning("Please enter a medicine name.")
        elif not schedule:
            st.warning("Please select at least one scheduled time.")
        elif end_date < start_date:
            st.warning("End date cannot be before start date.")
        else:
            medicines.append({
                "id": str(uuid.uuid4()),
                "name": medicine_name.strip(),
                "instructions": instructions.strip(),
                "schedule": schedule,
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat()
            })

            save_json(medicine_file, medicines)
            st.success("Medicine saved successfully!")
            st.rerun()

    st.divider()
    st.subheader("📋 My Medicine Schedule")

    if not medicines:
        st.info(
            "No medicines added yet. "
            "Use the form above to add a sample record."
        )
    else:
        active_medicines = [
            m for m in medicines
            if m["start_date"] <= today_text <= m["end_date"]
        ]

        st.metric("Medicines scheduled today", len(active_medicines))

        for medicine in medicines:
            with st.container(border=True):
                st.markdown(f"### 💊 {medicine['name']}")
                st.write(
                    "**Prescribed instructions:**",
                    medicine["instructions"] or "Not entered"
                )
                st.write(
                    "**Schedule:**",
                    ", ".join(medicine["schedule"])
                )
                st.caption(
                    f"{medicine['start_date']} to {medicine['end_date']}"
                )

                is_active = (
                    medicine["start_date"]
                    <= today_text
                    <= medicine["end_date"]
                )

                if not is_active:
                    st.info("Outside the recorded date range.")
                    continue

                st.markdown("**Today's tracking**")

                for time_name in medicine["schedule"]:
                    log_id = (
                        f"{today_text}|{medicine['id']}|{time_name}"
                    )

                    existing = next(
                        (
                            item["status"] for item in logs
                            if item["log_id"] == log_id
                        ),
                        "Not recorded"
                    )

                    with st.form(f"track_{log_id}"):
                        st.write(time_name)

                        status = st.selectbox(
                            "Status",
                            [
                                "Not recorded",
                                "Taken",
                                "Not taken"
                            ],
                            index=[
                                "Not recorded",
                                "Taken",
                                "Not taken"
                            ].index(existing),
                            key=f"status_{log_id}"
                        )

                        save_status = st.form_submit_button(
                            f"Save {time_name} status"
                        )

                    if save_status:
                        logs = [
                            item for item in logs
                            if item["log_id"] != log_id
                        ]

                        logs.append({
                            "log_id": log_id,
                            "date": today_text,
                            "medicine": medicine["name"],
                            "time": time_name,
                            "status": status
                        })

                        save_json(log_file, logs)
                        st.success("Tracking status saved!")
                        st.rerun()

    st.divider()
    st.subheader("📜 Tracking History")

    if logs:
        history = pd.DataFrame(logs)
        history = history.sort_values(
            "date", ascending=False
        )
        st.dataframe(
            history[["date", "medicine", "time", "status"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No tracking history recorded yet.")

    st.caption(
        "This tracker records your entries only. "
        "It does not provide medical advice or send automatic reminders. "
        "Follow your healthcare professional's instructions."
    )



elif page == "Appointments":
    import json
    import uuid
    from pathlib import Path
    from datetime import date, time
    import pandas as pd

    st.title("📅 Doctor Appointment Tracker")
    st.write("Organise your upcoming and completed appointments.")

    appointment_file = Path("appointments.json")

    def load_appointments():
        if appointment_file.exists():
            try:
                return json.loads(
                    appointment_file.read_text(encoding="utf-8")
                )
            except (json.JSONDecodeError, OSError):
                st.error("Unable to read appointments.json.")
                st.stop()
        return []

    def save_appointments(items):
        appointment_file.write_text(
            json.dumps(items, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

    appointments = load_appointments()

    st.subheader("➕ Add Appointment")

    with st.form("appointment_form"):
        doctor = st.text_input("Doctor name")
        specialty = st.text_input("Specialty")
        clinic = st.text_input("Hospital / Clinic name")

        appointment_date = st.date_input(
            "Appointment date",
            value=date.today()
        )

        appointment_time = st.time_input(
            "Appointment time",
            value=time(10, 0)
        )

        purpose = st.text_area(
            "Purpose / Notes (optional)"
        )

        submitted = st.form_submit_button("Save Appointment")

    if submitted:
        if not doctor.strip() or not clinic.strip():
            st.warning("Enter both doctor and hospital/clinic name.")
        else:
            appointments.append({
                "id": str(uuid.uuid4()),
                "doctor": doctor.strip(),
                "specialty": specialty.strip(),
                "clinic": clinic.strip(),
                "date": appointment_date.isoformat(),
                "time": appointment_time.strftime("%H:%M"),
                "purpose": purpose.strip(),
                "status": "Upcoming"
            })

            save_appointments(appointments)
            st.success("Appointment saved!")
            st.rerun()

    st.divider()
    st.subheader("📋 My Appointments")

    if not appointments:
        st.info("No appointments yet. Add one using the form above.")
    else:
        appointments.sort(
            key=lambda a: (a["date"], a["time"])
        )

        today_text = date.today().isoformat()

        upcoming = [
            a for a in appointments
            if a["date"] >= today_text
            and a["status"] == "Upcoming"
        ]

        completed = [
            a for a in appointments
            if a["status"] == "Completed"
        ]

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Appointments", len(appointments))
        col2.metric("Upcoming", len(upcoming))
        col3.metric("Completed", len(completed))

        for appointment in appointments:
            with st.container(border=True):
                st.markdown(
                    f"### 🏥 {appointment['clinic']}"
                )

                st.write(
                    f"**Doctor:** {appointment['doctor']}"
                )

                st.write(
                    f"**Specialty:** "
                    f"{appointment['specialty'] or 'Not specified'}"
                )

                st.write(
                    f"**Date:** {appointment['date']}  "
                    f"**Time:** {appointment['time']}"
                )

                st.write(
                    f"**Purpose:** "
                    f"{appointment['purpose'] or 'Not specified'}"
                )

                current_status = appointment.get(
                    "status", "Upcoming"
                )

                new_status = st.selectbox(
                    "Appointment status",
                    ["Upcoming", "Completed", "Cancelled"],
                    index=[
                        "Upcoming", "Completed", "Cancelled"
                    ].index(current_status),
                    key=f"status_{appointment['id']}"
                )

                if st.button(
                    "Update Status",
                    key=f"update_{appointment['id']}"
                ):
                    for item in appointments:
                        if item["id"] == appointment["id"]:
                            item["status"] = new_status
                            break

                    save_appointments(appointments)
                    st.success("Appointment status updated!")
                    st.rerun()
                if st.button(
                    "🗑️ Delete Appointment",
                    key=f"delete_{appointment['id']}"
                ):
                    appointments = [
                        item for item in appointments
                        if item["id"] != appointment["id"]
                    ]

                    save_appointments(appointments)
                    st.success("Appointment deleted successfully!")
                    st.rerun()

    st.caption(
        "This prototype stores appointment details locally. "
        "It does not send automatic reminders or contact your doctor."
    )




elif page == "Health Insights":

    import json
    from pathlib import Path

    import pandas as pd
    import plotly.express as px

    # ---------- PAGE HEADER ----------
    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #102b3f, #087f8c);
        padding: 26px;
        border-radius: 18px;
        color: white;
        margin-bottom: 22px;
    ">
        <p style="font-size: 12px; letter-spacing: 2px;">
            PERSONAL HEALTH ANALYTICS
        </p>
        <h1 style="color: white; margin-bottom: 8px;">
            📊 Health Insights
        </h1>
        <p style="color: #e0f5f4; margin-bottom: 0;">
            Understand your recorded symptom history through interactive charts.
        </p>
    </div>
    """, unsafe_allow_html=True)

    file_path = Path("symptom_records.json")

    # ---------- LOAD SAVED DATA ----------
    try:
        if file_path.exists():
            records = json.loads(
                file_path.read_text(encoding="utf-8")
            )
        else:
            records = []

        if not isinstance(records, list):
            records = []

    except (json.JSONDecodeError, OSError):
        records = []
        st.error(
            "Could not read symptom_records.json. "
            "Please check the file format."
        )

    if not records:
        st.info(
            "📔 No symptom records found yet. "
            "Add records in Symptom Diary to see your insights."
        )

    else:
        df = pd.DataFrame(records)

        # Support common field-name variations.
        def find_column(possible_names):
            for name in possible_names:
                if name in df.columns:
                    return name
            return None

        date_col = find_column(["Date", "date"])
        symptoms_col = find_column(["Symptoms", "symptoms", "Symptom", "symptom"])
        severity_col = find_column(["Severity", "severity"])

        if not date_col or not symptoms_col:
            st.error(
                "Required date or symptom fields were not found. "
                "Check the field names in symptom_records.json."
            )

        else:
            df["Date"] = pd.to_datetime(
                df[date_col], errors="coerce"
            )

            df["Symptoms"] = (
                df[symptoms_col]
                .fillna("")
                .astype(str)
            )

            if severity_col:
                df["Severity"] = (
                    df[severity_col]
                    .fillna("Not specified")
                    .astype(str)
                )
            else:
                df["Severity"] = "Not specified"

            # Remove invalid dates and empty symptom records.
            df = df.dropna(subset=["Date"]).copy()
            df = df[
                df["Symptoms"].str.strip().ne("")
            ].copy()

            if df.empty:
                st.info(
                    "No valid symptom records available to analyse."
                )

            else:
                df["DateOnly"] = df["Date"].dt.date

                # ---------- DATE FILTER ----------
                st.subheader("🔎 Filter Your Records")

                min_date = df["DateOnly"].min()
                max_date = df["DateOnly"].max()

                selected_dates = st.date_input(
                    "Select date range",
                    value=(min_date, max_date),
                    min_value=min_date,
                    max_value=max_date,
                    key="health_insights_date_range"
                )

                if isinstance(selected_dates, (tuple, list)):
                    if len(selected_dates) == 2:
                        start_date, end_date = selected_dates
                    elif len(selected_dates) == 1:
                        start_date = end_date = selected_dates[0]
                    else:
                        start_date, end_date = min_date, max_date
                else:
                    start_date = end_date = selected_dates

                filtered = df[
                    (df["DateOnly"] >= start_date)
                    & (df["DateOnly"] <= end_date)
                ].copy()

                st.caption(
                    f"Showing records from {start_date} to {end_date}"
                )

                if filtered.empty:
                    st.info(
                        "No symptom records found in this date range."
                    )

                else:
                    # ---------- PREPARE SYMPTOM DATA ----------
                    symptom_list = (
                        filtered["Symptoms"]
                        .str.split(r"\s*,\s*")
                        .explode()
                        .str.strip()
                    )

                    symptom_list = symptom_list[
                        symptom_list.ne("")
                    ]

                    # ---------- KPI CARDS ----------
                    total_records = len(filtered)
                    total_symptoms = len(symptom_list)
                    recorded_days = filtered["DateOnly"].nunique()

                    st.subheader("Your Health Overview")

                    col1, col2, col3 = st.columns(3)

                    col1.metric(
                        "📔 Symptom Records",
                        total_records
                    )

                    col2.metric(
                        "🩺 Symptoms Recorded",
                        total_symptoms
                    )

                    col3.metric(
                        "📅 Days Tracked",
                        recorded_days
                    )

                    st.divider()

                    # ---------- CHART 1: FREQUENCY ----------
                    left, right = st.columns(
                        [1.3, 1],
                        gap="large"
                    )

                    with left:
                        st.subheader("Symptom Frequency")

                        if not symptom_list.empty:
                            symptom_counts = (
                                symptom_list.value_counts()
                                .rename_axis("Symptom")
                                .reset_index(name="Records")
                                .sort_values("Records")
                            )

                            fig1 = px.bar(
                                symptom_counts,
                                x="Records",
                                y="Symptom",
                                orientation="h",
                                text="Records",
                                color="Records",
                                color_continuous_scale=[
                                    "#d9f0ee",
                                    "#087f8c"
                                ],
                                title="Most Frequently Recorded Symptoms"
                            )

                            fig1.update_layout(
                                height=380,
                                template="plotly_white",
                                coloraxis_showscale=False,
                                xaxis_title="Number of records",
                                yaxis_title="",
                                margin=dict(l=10, r=15, t=55, b=15)
                            )

                            fig1.update_traces(
                                textposition="outside"
                            )

                            st.plotly_chart(
                                fig1,
                                use_container_width=True
                            )
                        else:
                            st.info("No symptom names available.")

                    # ---------- CHART 2: SEVERITY ----------
                    with right:
                        st.subheader("Severity Distribution")

                        severity_counts = (
                            filtered["Severity"]
                            .value_counts()
                            .rename_axis("Severity")
                            .reset_index(name="Records")
                        )

                        fig2 = px.pie(
                            severity_counts,
                            names="Severity",
                            values="Records",
                            hole=0.55,
                            title="Recorded Severity Levels"
                        )

                        fig2.update_layout(
                            height=380,
                            template="plotly_white",
                            legend_title_text="Severity",
                            margin=dict(l=10, r=10, t=55, b=15)
                        )

                        fig2.update_traces(
                            textposition="inside",
                            textinfo="percent+label"
                        )

                        st.plotly_chart(
                            fig2,
                            use_container_width=True
                        )

                    st.divider()

                    # ---------- CHART 3: DAILY TREND ----------
                    st.subheader("📈 Daily Symptom Record Trend")

                    daily = (
                        filtered.groupby("DateOnly")
                        .size()
                        .reset_index(name="Records")
                    )

                    daily.columns = ["Date", "Records"]

                    fig3 = px.line(
                        daily,
                        x="Date",
                        y="Records",
                        markers=True,
                        title="Number of Symptom Entries Over Time"
                    )

                    fig3.update_traces(
                        line=dict(width=3),
                        marker=dict(size=8)
                    )

                    fig3.update_layout(
                        height=350,
                        template="plotly_white",
                        xaxis_title="Date",
                        yaxis_title="Number of records",
                        margin=dict(l=10, r=15, t=55, b=15)
                    )

                    st.plotly_chart(
                        fig3,
                        use_container_width=True
                    )

                    # ---------- RECENT RECORDS ----------
                    st.subheader("📋 Recent Symptom History")

                    history = filtered.sort_values(
                        "Date", ascending=False
                    ).head(10).copy()

                    history["Date"] = (
                        history["Date"].dt.strftime("%d %b %Y")
                    )

                    st.dataframe(
                        history[["Date", "Symptoms", "Severity"]],
                        use_container_width=True,
                        hide_index=True
                    )

                    st.caption(
                        "These insights describe recorded information only. "
                        "They do not diagnose lupus, measure disease activity, "
                        "or predict future flares. Discuss health concerns "
                        "with your healthcare professional."
                    )


    
elif page == "LupusVision AI":
    import json
    from pathlib import Path
    from datetime import date

    import streamlit as st
    from lupusvision_nlp import find_symptoms
    from lupusvision_cv import analyze_image

    st.title("🧠 LupusVision AI")

    st.write(
        "Describe how you feel in your own words. "
        "The prototype will identify possible symptom mentions "
        "for you to review."
    )

    st.info(
        "Research prototype only — not a diagnostic tool. "
        "Symptom detection may be incorrect or incomplete."
    )

    symptom_file = Path("symptom_records.json")

    description = st.text_area(
        "Describe your symptoms",
        placeholder="Example: I feel exhausted and my joints hurt."
    )

    if st.button("🔍 Identify Symptoms"):
        if not description.strip():
            st.warning("Please describe how you feel first.")
        else:
            found, negated = find_symptoms(description)

            st.session_state["lv_found"] = found
            st.session_state["lv_negated"] = negated
            st.session_state["lv_description"] = description

    if "lv_found" in st.session_state:
        found = st.session_state["lv_found"]
        negated = st.session_state["lv_negated"]
        original_text = st.session_state["lv_description"]

        st.subheader("Possible symptoms detected")

        if found:
            st.write("Please select the symptoms you want to record.")

            selected = []
            for symptom in found:
                if st.checkbox(symptom, key=f"lv_{symptom}"):
                    selected.append(symptom)

        else:
            st.write("No known positive symptom mentions were detected.")
            selected = []

        if negated:
            st.caption(
                "Possible symptoms mentioned as absent: "
                + ", ".join(negated)
            )

        severity = st.selectbox(
            "Overall severity",
            ["Mild", "Moderate", "Severe"]
        )

        if st.button("💾 Save Confirmed Symptoms"):
            if not selected:
                st.warning(
                    "Select at least one symptom before saving."
                )
            else:
                try:
                    if symptom_file.exists():
                        with symptom_file.open(
                            "r", encoding="utf-8"
                        ) as file:
                            records = json.load(file)

                        if not isinstance(records, list):
                            records = []
                    else:
                        records = []

                    records.append({
                        "Date": str(date.today()),
                        "Symptoms": ", ".join(selected),
                        "Severity": severity,
                        "Notes": original_text,
                        "Source": "LupusVision AI"
                    })

                    with symptom_file.open(
                        "w", encoding="utf-8"
                    ) as file:
                        json.dump(
                            records, file, indent=4,
                            ensure_ascii=False
                        )

                    st.success(
                        "Your confirmed symptoms were saved "
                        "to the symptom diary."
                    )

                except (OSError, json.JSONDecodeError) as error:
                    st.error(f"Could not save symptoms: {error}")

    
    st.divider()
    st.subheader("📷 Skin Image Analysis")
    st.write(
        "Upload an image to view basic image-processing "
        "details. This feature does not diagnose lupus "
        "or identify a rash."
    )

    uploaded_image = st.file_uploader(
        "Choose a skin image",
        type=["jpg", "jpeg", "png"],
        key="lupusvision_skin_image"
    )

    if uploaded_image is not None:
        try:
            result = analyze_image(uploaded_image)

            st.image(
                result["image"],
                caption="Uploaded image",
                use_container_width=True
            )

            st.write("### Image information")

            col1, col2 = st.columns(2)

            col1.metric(
                "Width",
                f'{result["width"]} px'
            )
            col2.metric(
                "Height",
                f'{result["height"]} px'
            )

            st.write(
                "Average RGB colour:",
                [
                    round(value, 1)
                    for value in result["average_color"]
                ]
            )

            st.write(
                "Brightness measurement:",
                result["brightness"]
            )

            st.write(
                "Sharpness measurement:",
                result["sharpness"]
            )

            st.caption(
                "These measurements describe the image only. "
                "They are not medical findings."
            )

        except Exception as error:
            st.error(
                "Unable to process this image. "
                "Please try another JPG or PNG image."
            )
            st.caption(f"Technical detail: {error}")

elif page == "Doctor Summary":

    import json
    from pathlib import Path
    from datetime import date
    from io import BytesIO
    from xml.sax.saxutils import escape

    import streamlit as st
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    )

    # ---------- PAGE HEADER ----------
    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #102b3f, #087f8c);
        padding: 26px;
        border-radius: 18px;
        color: white;
        margin-bottom: 22px;
    ">
        <p style="font-size: 12px; letter-spacing: 2px;">
            YOUR PERSONAL HEALTH RECORD
        </p>
        <h1 style="color: white; margin-bottom: 8px;">
            📝 Doctor Summary
        </h1>
        <p style="color: #e0f5f4; margin-bottom: 0;">
            Prepare a summary of your recorded information for your doctor.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ---------- JSON LOADER ----------
    def load_records(filename):
        path = Path(filename)

        if not path.exists():
            return []

        try:
            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            return data if isinstance(data, list) else []

        except (json.JSONDecodeError, OSError):
            return []

    symptoms = load_records("symptom_records.json")
    medicines = load_records("medicine_records.json")
    appointments = load_records("appointments.json")

    st.subheader("📋 Your Health Record Overview")

    c1, c2, c3 = st.columns(3)
    c1.metric("Symptom Records", len(symptoms))
    c2.metric("Medicine Records", len(medicines))
    c3.metric("Appointment Records", len(appointments))

    st.divider()

    # ---------- PERSONAL NOTES ----------
    st.subheader("🩺 Notes for Your Doctor")

    st.caption(
        "Add questions, concerns or details you want to discuss "
        "during your appointment."
    )

    patient_notes = st.text_area(
        "Your notes",
        placeholder=(
            "Example: Symptoms I want to discuss, "
            "questions about my medicines, or recent changes..."
        ),
        height=120,
        key="doctor_summary_notes"
    )

    # ---------- PREVIEW ----------
    st.subheader("📄 Report Preview")

    st.markdown("**Symptom History**")

    if symptoms:
        for record in symptoms[-5:][::-1]:
            symptom_date = record.get(
                "Date", record.get("date", "Date not recorded")
            )
            symptom_name = record.get(
                "Symptoms",
                record.get("symptoms", record.get("symptom", "Not specified"))
            )
            severity = record.get(
                "Severity", record.get("severity", "Not specified")
            )

            st.markdown(
                f"- **{symptom_date}** — {symptom_name} "
                f"(Severity: {severity})"
            )
    else:
        st.info("No symptom records have been saved yet.")

    st.markdown("**Recorded Medicines**")

    if medicines:
        for medicine in medicines[:10]:
            name = medicine.get(
                "name",
                medicine.get(
                    "Medicine",
                    medicine.get("medicine", "Medicine name unavailable")
                )
            )
            st.markdown(f"- {name}")
    else:
        st.info("No medicine records found.")

    st.markdown("**Appointments**")

    if appointments:
        for appointment in appointments[:10]:
            appointment_date = appointment.get(
                "date", appointment.get("Date", "Date not recorded")
            )
            doctor = appointment.get(
                "doctor",
                appointment.get("Doctor", "Doctor name not recorded")
            )
            st.markdown(f"- {appointment_date} — {doctor}")
    else:
        st.info("No appointment records found.")

    # ---------- PDF GENERATOR ----------
    def create_pdf(symptom_records, medicine_records,
                   appointment_records, notes):

        buffer = BytesIO()

        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=1.8 * cm,
            leftMargin=1.8 * cm,
            topMargin=1.8 * cm,
            bottomMargin=1.8 * cm
        )

        styles = getSampleStyleSheet()

        styles.add(ParagraphStyle(
            name="SectionHeading",
            parent=styles["Heading2"],
            textColor=colors.HexColor("#087f8c"),
            spaceBefore=12,
            spaceAfter=6
        ))

        styles.add(ParagraphStyle(
            name="SmallBody",
            parent=styles["BodyText"],
            fontSize=9,
            leading=13
        ))

        story = []

        def add_paragraph(text, style="SmallBody"):
            safe_text = escape(str(text)).replace("\n", "<br/>")
            story.append(Paragraph(safe_text, styles[style]))
            story.append(Spacer(1, 5))

        add_paragraph("LupusCare AI", "Title")
        add_paragraph("Patient Health Summary")
        add_paragraph(f"Report generated: {date.today().isoformat()}")
        add_paragraph(
            "This report contains user-recorded information "
            "for discussion with a healthcare professional."
        )

        story.append(Paragraph("Symptom History", styles["SectionHeading"]))

        symptom_rows = [["Date", "Symptoms", "Severity"]]

        for record in symptom_records[-20:][::-1]:
            symptom_rows.append([
                str(record.get("Date", record.get("date", "Not recorded"))),
                str(record.get(
                    "Symptoms",
                    record.get("symptoms", record.get("symptom", "Not specified"))
                )),
                str(record.get(
                    "Severity",
                    record.get("severity", "Not specified")
                ))
            ])

        if len(symptom_rows) == 1:
            symptom_rows.append(["No records", "-", "-"])

        story.append(Table(
            [[Paragraph(escape(str(cell)), styles["SmallBody"])
              for cell in row] for row in symptom_rows],
            colWidths=[3.2 * cm, 9 * cm, 4 * cm],
            repeatRows=1,
            style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0),
                 colors.HexColor("#087f8c")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.lightgrey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ])
        ))

        story.append(Paragraph("Recorded Medicines", styles["SectionHeading"]))

        if medicine_records:
            for medicine in medicine_records[:30]:
                name = medicine.get(
                    "name",
                    medicine.get("Medicine", medicine.get(
                        "medicine", "Medicine name unavailable"
                    ))
                )
                details = medicine.get(
                    "dosage",
                    medicine.get("Dosage", "")
                )
                add_paragraph(f"{name} — {details}" if details else name)
        else:
            add_paragraph("No medicine records available.")

        story.append(Paragraph("Appointments", styles["SectionHeading"]))

        if appointment_records:
            for appointment in appointment_records[:30]:
                appointment_date = appointment.get(
                    "date", appointment.get("Date", "Not recorded")
                )
                doctor = appointment.get(
                    "doctor",
                    appointment.get("Doctor", "Not recorded")
                )
                add_paragraph(f"{appointment_date} — {doctor}")
        else:
            add_paragraph("No appointment records available.")

        story.append(Paragraph("Notes for the Doctor", styles["SectionHeading"]))
        add_paragraph(notes.strip() if notes.strip() else "No additional notes entered.")

        story.append(Spacer(1, 15))
        add_paragraph(
            "Important: This is a patient-generated summary, not a medical "
            "diagnosis or treatment recommendation. Please verify all "
            "information with your healthcare professional."
        )

        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()

    # ---------- DOWNLOAD ----------
    st.divider()
    st.subheader("⬇️ Export Your Health Summary")

    if st.button("Generate Doctor Summary PDF", type="primary"):

        try:
            pdf_bytes = create_pdf(
                symptoms,
                medicines,
                appointments,
                patient_notes
            )

            st.download_button(
                label="Download Health Summary PDF",
                data=pdf_bytes,
                file_name="LupusCare_Doctor_Summary.pdf",
                mime="application/pdf"
            )

        except Exception as error:
            st.error(f"PDF generation failed: {error}")

    st.caption(
        "Keep your health report private and share it only with "
        "people you trust, such as your healthcare professional."
    )

