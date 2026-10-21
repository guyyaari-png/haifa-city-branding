import json
import webbrowser
from pathlib import Path
import matplotlib.pyplot as plt


def run_city_marketing_engine():
    print("=" * 60)
    print("   Haifa Reimagined: Data & Marketing Analytics Engine")
    print("=" * 60)

    # נתוני תקציב וחלוקת ערוצים
    total_budget_ils = 250_000
    channels = {
        "Digital Social & Reels": {"budget_share": 0.45, "cpm": 18, "conv_rate": 0.035},
        "Student & Tech Events": {"budget_share": 0.30, "fixed_reach": 15_000, "conv_rate": 0.12},
        "Outdoor & Transit Ads": {"budget_share": 0.25, "fixed_reach": 120_000, "conv_rate": 0.015},
    }

    # חישובי ביצועים
    channel_budgets = {}
    channel_reaches = {}
    total_estimated_leads = 0

    for name, data in channels.items():
        allocated_budget = total_budget_ils * data["budget_share"]
        channel_budgets[name] = allocated_budget

        if "cpm" in data:
            reach = int((allocated_budget / data["cpm"]) * 1000)
        else:
            reach = data["fixed_reach"]

        leads = int(reach * data["conv_rate"])
        channel_reaches[name] = reach
        total_estimated_leads += leads

    total_reach = sum(channel_reaches.values())

    print(f"Total Campaign Budget: {total_budget_ils:,} ILS")
    print(f"Estimated Gross Reach: {total_reach:,} impressions")
    print(f"Projected Qualified Inquiries (Leads): {total_estimated_leads:,}")
    print("-" * 60)

    # הפקת תרשים נתונים ויזואלי (Matplotlib Chart)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.patch.set_facecolor('#0d1b2a')

    # גרף עוגה: חלוקת תקציב
    colors = ['#00a896', '#028090', '#004b87']
    ax1.set_facecolor('#0d1b2a')
    wedges, texts, autotexts = ax1.pie(
        channel_budgets.values(),
        labels=channel_budgets.keys(),
        autopct='%1.0f%%',
        startangle=140,
        colors=colors,
        textprops=dict(color="#ffffff", fontsize=10)
    )
    for at in autotexts:
        at.set_color('#0d1b2a')
        at.set_weight('bold')
    ax1.set_title("Marketing Budget Allocation", color='#ffffff', fontsize=12, pad=15)

    # גרף עמודות: חשיפה משוערת
    ax2.set_facecolor('#1b263b')
    ax2.barh(list(channel_reaches.keys()), [r / 1000 for r in channel_reaches.values()], color='#00a896')
    ax2.set_xlabel("Estimated Reach (Thousands)", color='#ffffff')
    ax2.tick_params(colors='#ffffff')
    ax2.set_title("Estimated Audience Reach per Channel", color='#ffffff', fontsize=12, pad=15)
    for spine in ax2.spines.values():
        spine.set_color('#778da9')

    plt.tight_layout()
    chart_filename = "campaign_analytics_chart.png"
    plt.savefig(chart_filename, facecolor=fig.get_facecolor(), dpi=150)
    plt.close()
    print(f"Visual KPI Chart generated: {chart_filename}")

    # שמירת נתונים ל-JSON
    output_data = {
        "campaign_name": "Haifa Reimagined",
        "total_budget_ils": total_budget_ils,
        "total_reach": total_reach,
        "total_leads": total_estimated_leads,
        "breakdown": {
            name: {
                "budget_ils": channel_budgets[name],
                "reach": channel_reaches[name]
            }
            for name in channels
        }
    }

    with open("campaign_metrics.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print("KPIs exported to campaign_metrics.json")
    print("=" * 60)

    # פתיחת המצגת בדפדפן
    html_file = Path(__file__).resolve().parent / "index.html"
    if html_file.exists():
        print("Launching Haifa Presentation...")
        webbrowser.open(html_file.as_uri())


if __name__ == "__main__":
    run_city_marketing_engine()