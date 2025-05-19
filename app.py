from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route("/")
def dashboard():
    df = pd.read_csv("risk_data.csv")
    selected = request.args.get("category", "All")
    if selected != "All":
        df = df[df["Risk_Category"] == selected]
    categories = sorted(df["Risk_Category"].unique().tolist())

    fig = px.line(df, x="Date", y="Loss_Amount", title="Loss Over Time")
    chart = pio.to_html(fig, full_html=False)

    return render_template("dashboard.html",
                           chart=chart,
                           categories=categories,
                           selected=selected)
