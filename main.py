import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================
# EXPERT SYSTEM KNOWLEDGE BASE
# ============================================================

# Each case contains:
# - name: possible diagnosis
# - symptoms: symptoms associated with the diagnosis
# - advice: recommendation shown to the user

CASES = [
    {
        "name": "Common Cold",
        "symptoms": ["runny nose", "sneezing", "sore throat", "cough"],
        "advice": "Rest, drink plenty of fluids, and monitor your symptoms."
    },
    {
        "name": "Influenza (Flu)",
        "symptoms": ["fever", "headache", "body aches", "cough", "fatigue"],
        "advice": "Rest, stay hydrated, and consider consulting a healthcare professional."
    },
    {
        "name": "COVID-19",
        "symptoms": ["fever", "cough", "fatigue", "loss of taste", "loss of smell"],
        "advice": "Consider testing for COVID-19 and follow local health guidance."
    },
    {
        "name": "Allergic Rhinitis",
        "symptoms": ["sneezing", "runny nose", "itchy eyes", "watery eyes"],
        "advice": "Avoid known allergens and consider discussing treatment with a healthcare professional."
    },
    {
        "name": "Migraine",
        "symptoms": ["severe headache", "nausea", "sensitivity to light", "dizziness"],
        "advice": "Rest in a quiet, dark room and consider medical advice if headaches are severe or recurrent."
    },
    {
        "name": "Sinusitis",
        "symptoms": ["facial pain", "blocked nose", "headache", "runny nose"],
        "advice": "Drink fluids and seek medical advice if symptoms persist or become severe."
    },
    {
        "name": "Asthma",
        "symptoms": ["shortness of breath", "wheezing", "chest tightness", "cough"],
        "advice": "Follow your prescribed asthma action plan and seek urgent help for severe breathing difficulty."
    },
    {
        "name": "Bronchitis",
        "symptoms": ["cough", "chest discomfort", "fatigue", "shortness of breath"],
        "advice": "Rest and stay hydrated. Seek medical advice if breathing problems worsen."
    },
    {
        "name": "Pneumonia",
        "symptoms": ["fever", "cough", "shortness of breath", "chest pain", "fatigue"],
        "advice": "Pneumonia can be serious. Seek medical evaluation, especially with breathing difficulty."
    },
    {
        "name": "Gastroenteritis",
        "symptoms": ["nausea", "vomiting", "diarrhea", "stomach pain"],
        "advice": "Drink fluids to prevent dehydration and seek medical care if symptoms are severe."
    },
    {
        "name": "Food Poisoning",
        "symptoms": ["vomiting", "diarrhea", "stomach pain", "fever"],
        "advice": "Stay hydrated and seek medical attention if there is severe dehydration or persistent symptoms."
    },
    {
        "name": "Acid Reflux",
        "symptoms": ["heartburn", "chest discomfort", "sour taste", "belching"],
        "advice": "Avoid large meals and foods that trigger symptoms. Consult a healthcare professional if persistent."
    },
    {
        "name": "Dehydration",
        "symptoms": ["thirst", "dry mouth", "dizziness", "fatigue"],
        "advice": "Drink water or an appropriate rehydration solution and monitor your condition."
    },
    {
        "name": "Anemia",
        "symptoms": ["fatigue", "dizziness", "pale skin", "shortness of breath"],
        "advice": "Consult a healthcare professional for evaluation and blood tests."
    },
    {
        "name": "Urinary Tract Infection",
        "symptoms": ["painful urination", "frequent urination", "lower abdominal pain", "fever"],
        "advice": "Consult a healthcare professional because UTIs may require treatment."
    },
    {
        "name": "Tension Headache",
        "symptoms": ["headache", "neck pain", "stress", "fatigue"],
        "advice": "Rest, reduce stress, and maintain good sleep and hydration."
    },
    {
        "name": "Insomnia",
        "symptoms": ["difficulty sleeping", "daytime fatigue", "difficulty concentrating", "stress"],
        "advice": "Maintain a regular sleep schedule and reduce caffeine and screen use before bedtime."
    },
    {
        "name": "Conjunctivitis",
        "symptoms": ["red eyes", "itchy eyes", "watery eyes", "eye discharge"],
        "advice": "Avoid touching your eyes and seek medical advice, particularly if pain or vision changes occur."
    },
    {
        "name": "Dermatitis",
        "symptoms": ["skin rash", "itchy skin", "red skin", "dry skin"],
        "advice": "Avoid possible irritants and consult a healthcare professional if the rash persists."
    },
    {
        "name": "Chickenpox",
        "symptoms": ["fever", "skin rash", "itchy skin", "fatigue"],
        "advice": "Avoid contact with vulnerable people and seek medical advice."
    },
    {
        "name": "Dengue Fever",
        "symptoms": ["high fever", "severe headache", "joint pain", "skin rash"],
        "advice": "Seek medical evaluation promptly, especially if symptoms become severe."
    },
    {
        "name": "Malaria",
        "symptoms": ["fever", "chills", "sweating", "headache", "fatigue"],
        "advice": "Seek medical evaluation promptly, particularly if you have recently been in a malaria-risk area."
    },
    {
        "name": "Strep Throat",
        "symptoms": ["sore throat", "fever", "swollen glands", "difficulty swallowing"],
        "advice": "Seek medical evaluation because testing may be needed."
    },
    {
        "name": "Ear Infection",
        "symptoms": ["ear pain", "fever", "hearing difficulty", "fatigue"],
        "advice": "Consult a healthcare professional, especially for severe pain or fever."
    }
]


# ============================================================
# EXPERT SYSTEM ENGINE
# ============================================================

def diagnose(selected_symptoms):
    """
    Compare selected symptoms with the knowledge base.

    A score is calculated for every case:
        score = matched symptoms / total symptoms of case

    Cases are sorted from highest to lowest score.
    """

    results = []

    for case in CASES:
        matched = set(selected_symptoms) & set(case["symptoms"])

        if matched:
            score = len(matched) / len(case["symptoms"])

            results.append({
                "name": case["name"],
                "score": score,
                "matched": matched,
                "advice": case["advice"]
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results


# ============================================================
# GET ALL UNIQUE SYMPTOMS
# ============================================================

ALL_SYMPTOMS = sorted(
    set(
        symptom
        for case in CASES
        for symptom in case["symptoms"]
    )
)


# ============================================================
# TKINTER GUI
# ============================================================

class ExpertSystemGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Medical Expert System")
        self.root.geometry("900x700")
        self.root.configure(bg="#eef3f8")

        self.symptom_vars = {}

        self.create_header()
        self.create_symptom_area()
        self.create_buttons()
        self.create_result_area()

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    def create_header(self):
        header = tk.Frame(
            self.root,
            bg="#1f4e78",
            height=90
        )
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="MEDICAL EXPERT SYSTEM",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#1f4e78"
        )
        title.pack(pady=(15, 2))

        subtitle = tk.Label(
            header,
            text="Rule-Based Diagnosis System",
            font=("Arial", 12),
            fg="#dbeeff",
            bg="#1f4e78"
        )
        subtitle.pack()

    # --------------------------------------------------------
    # SYMPTOM AREA
    # --------------------------------------------------------

    def create_symptom_area(self):

        frame = tk.LabelFrame(
            self.root,
            text="Select Your Symptoms",
            font=("Arial", 13, "bold"),
            bg="#eef3f8",
            padx=10,
            pady=10
        )
        frame.pack(
            fill="both",
            expand=False,
            padx=20,
            pady=15
        )

        # Create a canvas so many symptoms can be displayed
        canvas = tk.Canvas(
            frame,
            bg="white",
            height=230
        )

        scrollbar = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=canvas.yview
        )

        symptom_frame = tk.Frame(
            canvas,
            bg="white"
        )

        symptom_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=symptom_frame,
            anchor="nw"
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Display symptoms in two columns
        for i, symptom in enumerate(ALL_SYMPTOMS):

            var = tk.BooleanVar()

            self.symptom_vars[symptom] = var

            checkbox = tk.Checkbutton(
                symptom_frame,
                text=symptom.title(),
                variable=var,
                font=("Arial", 11),
                bg="white",
                activebackground="white",
                anchor="w"
            )

            row = i // 2
            column = i % 2

            checkbox.grid(
                row=row,
                column=column,
                sticky="w",
                padx=20,
                pady=5
            )

    # --------------------------------------------------------
    # BUTTONS
    # --------------------------------------------------------

    def create_buttons(self):

        button_frame = tk.Frame(
            self.root,
            bg="#eef3f8"
        )
        button_frame.pack(pady=10)

        diagnose_button = tk.Button(
            button_frame,
            text="DIAGNOSE",
            command=self.run_diagnosis,
            font=("Arial", 12, "bold"),
            bg="#198754",
            fg="white",
            width=15,
            height=2,
            cursor="hand2"
        )

        diagnose_button.grid(
            row=0,
            column=0,
            padx=10
        )

        clear_button = tk.Button(
            button_frame,
            text="CLEAR",
            command=self.clear_selection,
            font=("Arial", 12, "bold"),
            bg="#dc3545",
            fg="white",
            width=15,
            height=2,
            cursor="hand2"
        )

        clear_button.grid(
            row=0,
            column=1,
            padx=10
        )

    # --------------------------------------------------------
    # RESULT AREA
    # --------------------------------------------------------

    def create_result_area(self):

        frame = tk.LabelFrame(
            self.root,
            text="Expert System Result",
            font=("Arial", 13, "bold"),
            bg="#eef3f8",
            padx=10,
            pady=10
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 15)
        )

        self.result_text = tk.Text(
            frame,
            font=("Consolas", 11),
            bg="#ffffff",
            fg="#222222",
            wrap="word",
            state="disabled"
        )

        self.result_text.pack(
            fill="both",
            expand=True
        )

    # --------------------------------------------------------
    # RUN DIAGNOSIS
    # --------------------------------------------------------

    def run_diagnosis(self):

        selected = [
            symptom
            for symptom, var in self.symptom_vars.items()
            if var.get()
        ]

        if not selected:
            messagebox.showwarning(
                "No Symptoms",
                "Please select at least one symptom."
            )
            return

        results = diagnose(selected)

        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)

        self.result_text.insert(
            tk.END,
            "SELECTED SYMPTOMS\n"
        )

        self.result_text.insert(
            tk.END,
            "-" * 60 + "\n"
        )

        for symptom in selected:
            self.result_text.insert(
                tk.END,
                f"• {symptom.title()}\n"
            )

        self.result_text.insert(
            tk.END,
            "\nPOSSIBLE CONDITIONS\n"
        )

        self.result_text.insert(
            tk.END,
            "-" * 60 + "\n"
        )

        # Display top 5 results
        for index, result in enumerate(results[:5], start=1):

            percentage = result["score"] * 100

            self.result_text.insert(
                tk.END,
                f"\n{index}. {result['name']}\n"
            )

            self.result_text.insert(
                tk.END,
                f"   Match: {percentage:.1f}%\n"
            )

            self.result_text.insert(
                tk.END,
                "   Matching symptoms: "
            )

            self.result_text.insert(
                tk.END,
                ", ".join(
                    symptom.title()
                    for symptom in result["matched"]
                )
            )

            self.result_text.insert(
                tk.END,
                "\n"
            )

            self.result_text.insert(
                tk.END,
                f"   Advice: {result['advice']}\n"
            )

        self.result_text.insert(
            tk.END,
            "\n" + "=" * 60 + "\n"
        )

        self.result_text.insert(
            tk.END,
            "IMPORTANT:\n"
        )

        self.result_text.insert(
            tk.END,
            "This program is an educational expert-system demonstration "
            "and does not provide a medical diagnosis. Consult a qualified "
            "healthcare professional for actual medical concerns.\n"
        )

        self.result_text.config(state="disabled")

    # --------------------------------------------------------
    # CLEAR
    # --------------------------------------------------------

    def clear_selection(self):

        for var in self.symptom_vars.values():
            var.set(False)

        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.config(state="disabled")


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = ExpertSystemGUI(root)

    root.mainloop()
