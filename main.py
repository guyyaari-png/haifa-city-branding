import json
import webbrowser
from pathlib import Path


def run_campaign_simulation():
    print("=" * 50)
    print(" Haifa Reimagined: Marketing Budget & Reach Engine")
    print("=" * 50)

    # נתוני תקציב ראשוניים לקמפיין העירוני
    total_budget_ils = 250_000
    channels = {
        "Digital Social & Reels": {"share": 0.45, "cpm_ils": 18, "conv_rate": 0.035},
        "Tech Hub & Student Events": {"share": 0.30, "cost_per_event": 25000, "attendees": 1200},
        "Outdoor & Transit Displays": {"share": 0.25, "reach_fixed": 85000},
    }

    # חישוב אומדני חשיפה ואימפקט
    digital_budget = total_budget_ils * channels["Digital Social & Reels"]["share"]
    est_impressions = int((digital_budget / channels["Digital Social & Reels"]["cpm_ils"]) * 1000)
    est_leads = int(est_impressions * channels["Digital Social & Reels"]["conv_rate"])

    print(f"Total Campaign Budget: {total_budget_ils:,} ILS")
    print(f"-> Digital Budget (45%): {digital_budget:,.0f} ILS")
    print(f"-> Estimated Digital Reach: {est_impressions:,} impressions")
    print(f"-> Projected Interest Inquiries (Leads): {est_leads:,}")
    print("=" * 50)

    # שמירת נתונים לקובץ JSON לשילוב במצגת
    results = {
        "budget": total_budget_ils,
        "impressions": est_impressions,
        "leads": est_leads,
        "status": "Simulation Completed Successfully"
    }

    with open("campaign_metrics.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("Metrics exported to campaign_metrics.json")

    # פתיחה אוטומטית של המצגת בדפדפן
    html_path = Path(__file__).resolve().parent / "index.html"
    if html_path.exists():
        print("Launching presentation in browser...")
        webbrowser.open(html_path.as_uri())
    else:
        print("index.html not found in directory. Please create index.html first.")


if __name__ == "__main__":
    run_campaign_simulation()