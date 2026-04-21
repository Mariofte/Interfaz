import json
import threading
import tkinter as tk
from tkinter import scrolledtext

import requests
from requests import Response, Session
from requests.exceptions import RequestException


# ══════════════════════════════════════════════
#  Tu ScannerAPI — sin cambios
# ══════════════════════════════════════════════
class ScannerAPI:
    __slots__ = ("base_url", "endpoint", "headers", "_session")

    def __init__(self, base_url: str, endpoint: str, headers: dict[str, str] | None = None):
        self.base_url: str = base_url
        self.endpoint: str = endpoint
        self.headers: dict[str, str] | None = headers
        self._session: Session = Session()
        self._session.headers.update(headers or {})

    def __repr__(self) -> str:
        data: dict[str, str | None] = {
            "base_url": self.base_url,
            "endpoint": self.endpoint,
            "headers": self.headers,  # pyright: ignore[reportAssignmentType]
        }
        return f"ScannerAPI({data!r})"

    def __request(self, method: str, body: dict | None = None, params: dict | None = None) -> Response | None:
        try:
            response = self._session.request(
                method,
                f"{self.base_url}{self.endpoint}",
                json=body,
                params=params,
                timeout=5,
            )
            return response
        except RequestException:
            return None

    def get(self, params: dict | None = None) -> dict | None:
        response = self.__request("GET", params=params)
        if response and response.status_code == 200:
            return response.json()
        return None

    def post(self, body: dict) -> dict | None:
        response = self.__request("POST", body=body)
        if response and response.status_code == 201:
            return response.json()
        return None

    def put(self, body: dict) -> dict | None:
        response = self.__request("PUT", body=body)
        if response and response.status_code == 200:
            return response.json()
        return None

    def delete(self) -> bool:  # pyright: ignore[reportReturnType]
        response = self.__request("DELETE")
        if response is not None and response.status_code == 200:
            return True
        return False

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._session.close()


# ══════════════════════════════════════════════
#  TBA config
# ══════════════════════════════════════════════
BASE_URL = "https://www.thebluealliance.com/api/v3"
HEADERS  = {"X-TBA-Auth-Key": "Oyez8lIXExZYHTRATqXknF2NttU3iSdFBCJ6iDLQWoMb0kBao9SOljmY4o1MWWHS"}

def tba(endpoint: str) -> dict | None:
    with ScannerAPI(BASE_URL, endpoint, HEADERS) as api:
        return api.get()


# ══════════════════════════════════════════════
#  UI
# ══════════════════════════════════════════════
root = tk.Tk()
root.title("TBA Tester")
root.geometry("700x520")
root.configure(bg="#0E0E1A")

def lbl(parent, text):
    tk.Label(parent, text=text, bg="#0E0E1A", fg="#AAAAAA",
             font=("Consolas", 10)).pack()

frame_top = tk.Frame(root, bg="#0E0E1A")
frame_top.pack(fill="x", padx=16, pady=12)

team_var  = tk.StringVar(value="6647")
year_var  = tk.StringVar(value="2024")
event_var = tk.StringVar(value="2024camb")

for text, var in [("Team #", team_var), ("Year", year_var), ("Event key", event_var)]:
    col = tk.Frame(frame_top, bg="#0E0E1A")
    col.pack(side="left", padx=8)
    lbl(col, text)
    tk.Entry(col, textvariable=var, width=12, bg="#1C1C2E", fg="white",
             insertbackground="white", relief="flat",
             font=("Consolas", 11)).pack()

frame_btns = tk.Frame(root, bg="#0E0E1A")
frame_btns.pack(fill="x", padx=16)

output = scrolledtext.ScrolledText(root, bg="#111122", fg="#00FF90",
                                   font=("Consolas", 10), relief="flat")
output.pack(fill="both", expand=True, padx=16, pady=12)

def show(text: str):
    output.delete("1.0", "end")
    output.insert("end", text)

def run(endpoint_fn):
    show("⏳ Cargando...")
    def task():
        try:
            data    = tba(endpoint_fn())
            pretty  = json.dumps(data, indent=2, ensure_ascii=False)
            root.after(0, show, pretty)
        except Exception as e:
            root.after(0, show, f"❌ Error: {e}")
    threading.Thread(target=task, daemon=True).start()

ENDPOINTS = {
    "Team info":      lambda: f"/team/frc{team_var.get()}",
    "Team media":     lambda: f"/team/frc{team_var.get()}/media/{year_var.get()}",
    "Team matches":   lambda: f"/team/frc{team_var.get()}/matches/{year_var.get()}",
    "Events":         lambda: f"/events/{year_var.get()}",
    "Event info":     lambda: f"/event/{event_var.get()}",
    "Event teams":    lambda: f"/event/{event_var.get()}/teams",
    "Event matches":  lambda: f"/event/{event_var.get()}/matches",
    "Event rankings": lambda: f"/event/{event_var.get()}/rankings",
}

for label, endpoint_fn in ENDPOINTS.items():
    tk.Button(frame_btns, text=label, bg="#1A1A3E", fg="white",
              activebackground="#0F3460", relief="flat", cursor="hand2",
              font=("Consolas", 9), padx=8, pady=4,
              command=lambda f=endpoint_fn: run(f)).pack(side="left", padx=3, pady=4)

root.mainloop()